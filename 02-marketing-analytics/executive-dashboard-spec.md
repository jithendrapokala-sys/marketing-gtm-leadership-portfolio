# Executive Marketing Dashboard — Specification

A one-page view for the CEO and leadership team. Built in HubSpot, Salesforce or a BI tool fed by the CRM.

## Layout

```
┌──────────────────────────────────────────────────────────────────┐
│ Pipeline created │ Revenue (sourced) │ Pipeline coverage │ CAC   │  ← headline tiles vs target
├──────────────────────────────────────────────────────────────────┤
│ Pipeline created by month (actual vs target)                     │  ← trend
├────────────────────────────────┬─────────────────────────────────┤
│ Funnel: Lead→MQL→SQL→Opp→Won   │ Pipeline per $ by channel       │
│ with conversion % per stage    │ (ranked bar)                    │
├────────────────────────────────┼─────────────────────────────────┤
│ Target-account engagement      │ Top 10 open opportunities        │
│ (Tier 1 / 2 / 3)               │ influenced by marketing         │
└────────────────────────────────┴─────────────────────────────────┘
```

## Review Rhythm

| Forum | Frequency | Focus | Decisions |
|---|---|---|---|
| Marketing stand-up | Weekly | Program metrics, launches | Fix or pause underperforming programs |
| Marketing + Sales pipeline review | Weekly | SQLs, SLA, opportunity progress | Follow-up, enablement gaps |
| Leadership review | Monthly | Layers 1–2 | Budget shifts between channels |
| Board / QBR | Quarterly | Pipeline, revenue, CAC trend | Strategy, targets, investment |

## Data Rules

- One source of truth: CRM. Spend is imported monthly from finance and ad platforms.
- Required fields enforced at creation: lead source, campaign, account tier.
- UTM convention documented and applied to every campaign link.
