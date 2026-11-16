"""Lead scoring model: fit + engagement, with decay and routing.

Scores each lead on two dimensions:
  * FIT (0-50): how well the account and person match the ICP
  * ENGAGEMENT (0-50): how actively they are engaging, decayed by inactivity
Then assigns a grade (A-D) and a routing action.

Usage:
    python scripts/lead_scoring.py data/sample_leads.csv [--out scored_leads.csv]

Standard library only. Weights are illustrative; calibrate them against your own
closed-won / closed-lost data. Sample data is synthetic.
"""
import argparse
import csv
import re

ICP_INDUSTRIES = {"Healthcare": 15, "BFSI": 12, "Retail": 10, "Manufacturing": 10, "Automotive": 10}
SENIORITY = [  # (keywords, points) - first match wins
    (("chief", "cio", "cfo", "ceo", "cto", "president"), 20),
    (("vp", "vice president", "head"), 17),
    (("director",), 14),
    (("manager", "lead"), 8),
]
TARGET_REGIONS = {"North America": 5, "EMEA": 4, "APAC": 3}
MQL_THRESHOLD = 60


def yes(v):
    return str(v).strip().lower() in {"yes", "y", "true", "1"}


def fit_score(lead):
    score = ICP_INDUSTRIES.get(lead["industry"], 0)
    emp = int(lead["employees"])
    score += 10 if emp >= 1000 else 7 if emp >= 500 else 4 if emp >= 200 else 0
    title = lead["title"].lower()
    score += next((pts for kws, pts in SENIORITY
                   if any(re.search(rf"\b{re.escape(k)}\b", title) for k in kws)), 0)
    score += TARGET_REGIONS.get(lead["region"], 0)
    return min(score, 50)


def engagement_score(lead):
    raw = (min(int(lead["email_opens"]), 5) * 1
           + min(int(lead["page_visits"]), 10) * 1
           + (8 if yes(lead["pricing_page_visit"]) else 0)
           + min(int(lead["content_downloads"]), 3) * 3
           + (7 if yes(lead["webinar_attended"]) else 0)
           + (15 if yes(lead["demo_requested"]) else 0))
    days = int(lead["days_since_last_activity"])
    decay = 1.0 if days <= 7 else 0.75 if days <= 30 else 0.4 if days <= 60 else 0.2
    return min(round(raw * decay), 50)


def grade(fit, eng):
    """Fit gates the grade: a highly engaged but poor-fit lead is never an A."""
    total = fit + eng
    if fit < 20:
        return "D", "Disqualify or self-serve nurture"
    if total >= 80:
        return "A", "Route to account executive within 4 hours"
    if total >= MQL_THRESHOLD:
        return "B", "MQL: inside sales follow-up within 24 hours"
    if fit >= 35:
        return "C", "Good fit, low engagement: add to ABM / nurture"
    return "C", "Nurture sequence"


def score_all(rows):
    out = []
    for lead in rows:
        f, e = fit_score(lead), engagement_score(lead)
        g, action = grade(f, e)
        out.append({**lead, "fit": f, "engagement": e, "total": f + e,
                    "mql": "yes" if g in {"A", "B"} else "no", "grade": g, "action": action})
    return sorted(out, key=lambda r: r["total"], reverse=True)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("csv_path")
    p.add_argument("--out", help="write all scored fields to this CSV")
    a = p.parse_args()
    with open(a.csv_path, newline="", encoding="utf-8") as f:
        scored = score_all(list(csv.DictReader(f)))

    print(f"{'Lead':<5} {'Company':<28} {'Fit':>3} {'Eng':>3} {'Tot':>3}  Gr  Action")
    for r in scored:
        print(f"{r['lead_id']:<5} {r['company'][:28]:<28} {r['fit']:>3} {r['engagement']:>3} "
              f"{r['total']:>3}  {r['grade']:<2}  {r['action']}")
    print(f"\nMQLs: {sum(r['mql'] == 'yes' for r in scored)} of {len(scored)} leads")

    if a.out:
        with open(a.out, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(scored[0].keys()))
            w.writeheader()
            w.writerows(scored)
        print(f"Scored leads written to {a.out}")


if __name__ == "__main__":
    main()
