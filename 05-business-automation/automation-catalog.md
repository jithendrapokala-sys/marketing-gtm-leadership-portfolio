# Marketing & Sales Automation Catalog

| # | Automation | Trigger | Steps | Impact |
|---|---|---|---|---|
| 1 | **Inbound lead routing** | Form submit | Enrich → score → CRM upsert → route to owner or nurture | Faster speed to lead; no lost leads ([workflow](workflows/)) |
| 2 | **Account research brief** | Account set to Tier 1 | AI research → enrich → brief → CRM note → alert AE | Hours of research per account become minutes |
| 3 | **Meeting booked → prep pack** | Calendar booking | Pull CRM history + account brief → send to seller | Better first calls |
| 4 | **Lead score decay** | Daily schedule | Reduce engagement scores for inactive leads | Sales sees current interest only |
| 5 | **MQL SLA watchdog** | Hourly schedule | Find MQLs with no touch past the SLA → escalate to manager | Follow-up discipline |
| 6 | **Event lead processing** | Event list upload | Clean → de-duplicate → enrich → score → assign → follow-up email | Event leads contacted within 48 hours |
| 7 | **Webinar follow-up** | Webinar ends | Attendee vs. no-show split → personalized email with recording | Higher post-event conversion |
| 8 | **Closed-lost recycle** | Opportunity lost | Wait 90 days → re-enroll in a relevant nurture | Revives future pipeline |
| 9 | **Content repurposing** | New long-form asset | AI drafts blog, social and email versions → human review queue | More content from the same effort |
| 10 | **Landing page generation** | New campaign brief | Python template + AI copy variants → publish for A/B test | Faster campaign launch |
| 11 | **Weekly pipeline digest** | Monday schedule | CRM query → KPI summary → email or Slack to leadership | No manual reporting |
| 12 | **CRM hygiene** | Nightly schedule | Normalize titles, merge duplicates, flag missing fields | Trustworthy data ([rules](crm-hygiene.md)) |

## Prioritization

Score each candidate automation on (a) hours saved per month, (b) revenue impact and (c) build effort and risk. Build the top three, measure them, then move on to the next.
