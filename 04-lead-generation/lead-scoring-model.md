# Lead Scoring Model

Two separate dimensions, so we know **who** the lead is and **how interested** they are.

## Fit Score (0–50): Does the lead match our ICP?

| Attribute | Points |
|---|---|
| Industry | Healthcare 15 · BFSI 12 · Retail / Manufacturing / Automotive 10 · Other 0 |
| Company size | 1,000+ employees 10 · 500+ 7 · 200+ 4 · under 200: 0 |
| Seniority | C-level / President 20 · VP / Head 17 · Director 14 · Manager / Lead 8 |
| Region | North America 5 · EMEA 4 · APAC 3 |

## Engagement Score (0–50): Are they showing buying intent?

| Behavior | Points |
|---|---|
| Email opens | 1 each (max 5) |
| Page visits | 1 each (max 10) |
| Pricing page visit | 8 |
| Content download | 3 each (max 3 downloads) |
| Webinar attended | 7 |
| Demo requested | 15 |

**Decay:** engagement is multiplied by 1.0 if active in the last 7 days, 0.75 within 30 days, 0.4 within 60 days and 0.2 after that. Old interest isn't current interest.

## Grades & Routing

| Grade | Rule | Action |
|---|---|---|
| **A** | Total ≥ 80 | Route to account executive within 4 hours |
| **B** | Total ≥ 60 (MQL) | Inside sales follow-up within 24 hours |
| **C** | Below 60, fit ≥ 20 | ABM program if fit is high, otherwise nurture |
| **D** | Fit < 20 | Disqualify or self-serve nurture, however engaged |

## Calibration

The weights are a starting point. Every quarter:
1. Compare scores of closed-won vs. closed-lost leads
2. Raise weights for attributes common in wins; lower the rest
3. Check that MQL → SQL conversion is rising and Sales agrees with the grades

Implementation: [scripts/lead_scoring.py](scripts/lead_scoring.py). The same rules can be built in HubSpot, Pardot or Salesforce scoring, or in an n8n workflow ([05 — Business Automation](../05-business-automation/)).
