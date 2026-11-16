# CRM Hygiene Rules

Dashboards are only as good as the data behind them. These rules are enforced automatically wherever possible.

## Required Fields

| Object | Required at creation |
|---|---|
| Contact / Lead | Email, company, lead source, campaign, country |
| Account | Domain, industry, employee band, account tier, owner |
| Opportunity | Amount, close date, stage, primary campaign, product |

## Standardization

- **Job titles** → mapped to seniority (C-level / VP / Director / Manager / IC) and function
- **Company names** → matched to account by domain, not name
- **Country / state** → picklists only, no free text
- **Lead source** → fixed values tied to the UTM convention

## Automated Checks (nightly)

| Check | Action |
|---|---|
| Duplicate contacts (same email) | Auto-merge, keeping the most recent activity |
| Duplicate accounts (same domain) | Flag for RevOps review |
| Opportunities past close date | Alert owner to update |
| Missing required fields | Owner task created |
| Bounced emails | Mark invalid; exclude from sends |

## Ownership

Marketing ops owns the rules; every record owner fixes their own flagged records within the week. Data quality score (% of records complete and valid) is reported monthly.
