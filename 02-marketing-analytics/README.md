# 02 — Marketing Analytics

I run marketing as a revenue function: every program is measured by the pipeline and revenue it creates, not just by clicks or leads. This project shows the KPI framework and executive dashboard I use, plus a working script that turns raw campaign data into a board-ready report.

## Contents

| File | Purpose |
|---|---|
| [kpi-framework.md](kpi-framework.md) | 4-layer KPI framework, metric definitions and formulas |
| [executive-dashboard-spec.md](executive-dashboard-spec.md) | What goes on a CEO/CMO dashboard, and how often it's reviewed |
| [scripts/funnel_report.py](scripts/funnel_report.py) | Python script: funnel conversion, CAC, ROI, pipeline per $ and velocity by channel |
| [data/sample_campaigns.csv](data/sample_campaigns.csv) | **Synthetic** sample data (5 channels × 2 quarters) |
| [sample-report.md](sample-report.md) | Example output generated from the sample data |

## Run It

Needs Python 3.8+ and no extra libraries.

```bash
python scripts/funnel_report.py data/sample_campaigns.csv --out sample-report.md
```

To use your own data, export campaign results from your CRM (HubSpot, Salesforce, Zoho) with the same columns as the sample file.

## How This Connects to My Experience

- Built **ROI tracking dashboards** and proof-point reporting with the CEO, Sales and Product at InterScripts, aligning marketing OKRs with revenue targets.
- Built **executive KPI dashboards** across HubSpot, Salesforce, Pardot, Zoho CRM and GA4.
- Lean Six Sigma Black Belt: measure → analyze → improve is how I run every funnel.

> The numbers in the sample data and report are synthetic and illustrate the method only.
