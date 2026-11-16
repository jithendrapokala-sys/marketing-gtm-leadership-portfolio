# 04 — Lead Generation & Demand Generation

Demand generation that Sales trusts: clear definitions, the right accounts, multi-channel programs, and fast follow-up. I've led this from both sides of the funnel, as a marketing leader and as a head of sales and inside-sales manager.

## Contents

| File | Purpose |
|---|---|
| [demand-gen-framework.md](demand-gen-framework.md) | Full-funnel demand generation framework |
| [abm-playbook.md](abm-playbook.md) | Account-Based Marketing playbook (1:1, 1:few, 1:many) |
| [lead-scoring-model.md](lead-scoring-model.md) | Fit + engagement scoring model and routing rules |
| [scripts/lead_scoring.py](scripts/lead_scoring.py) | Working Python implementation of the scoring model |
| [data/sample_leads.csv](data/sample_leads.csv) | **Synthetic** sample leads |
| [nurture-sequence.md](nurture-sequence.md) | 6-touch B2B email nurture sequence template |
| [case-studies.md](case-studies.md) | Demand-gen results from Dell, Tata, InterScripts and BuyOnlineCrackers.in |

## Run the Lead-Scoring Model

```bash
python scripts/lead_scoring.py data/sample_leads.csv --out scored_leads.csv
```

```
Lead  Company                      Fit Eng Tot  Gr  Action
L001  Northfield Health System      50  50 100  A   Route to account executive within 4 hours
L007  Summit Care Network           41  30  71  B   MQL: inside sales follow-up within 24 hours
...
L005  Student Freelancer             3  31  34  D   Disqualify or self-serve nurture
```

Note L005: the most engaged lead in the file, but a poor fit, so it isn't sent to Sales. Fit gates the grade, which protects the sales team's time.

## Highlights From My Career

- **$16M USD** annual revenue from a **195+** person sales organization at Dell, plus a social media sales unit generating **$10M USD** a year
- **~$3.5M+** qualified enterprise pipeline at InterScripts
- **30,000** qualified inquiries from **45,000** visitors through SEO alone (BuyOnlineCrackers.in)
- Multi-channel ABM, Pardot automation and LinkedIn outreach across BFSI, Manufacturing, Automotive and Retail at Tata Business Support Services; **CEO Key Contributor Award**
