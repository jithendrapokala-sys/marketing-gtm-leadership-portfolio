# n8n Workflow — Inbound Lead Routing

```
Form Webhook ─┬─▶ Enrich Company ─┐
              └──────────────────▶ Merge ─▶ Score Lead ─▶ Upsert to CRM ─▶ Is MQL? ─┬─ yes ─▶ Alert Sales Owner
                                                                                    └─ no ──▶ Enroll in Nurture
```

| Step | What happens |
|---|---|
| Form Webhook | Receives a form submission (name, email, company, title, industry, employees, intent flags) |
| Enrich Company | Looks up firmographics from the email domain (placeholder enrichment API) |
| Score Lead | Applies a simplified version of the [fit + engagement model](../../04-lead-generation/lead-scoring-model.md) |
| Upsert to CRM | Creates or updates the contact with score and grade |
| Is MQL? | Score ≥ 60 goes to Sales; everything else goes to nurture |
| Alert Sales Owner | Slack alert so follow-up happens within the SLA |
| Enroll in Nurture | Adds the lead to the [nurture sequence](../../04-lead-generation/nurture-sequence.md) |

## Import

1. In n8n: **Workflows → Import from File** → select `inbound-lead-routing.n8n.json`
2. Replace the placeholder URLs (`*.example.com`) with your enrichment provider, CRM and Slack webhook, or swap in n8n's native HubSpot / Salesforce / Slack nodes
3. Add credentials in n8n (never hard-code keys in the workflow)
4. Test with a sample payload:

```json
{
  "name": "Test Lead",
  "email": "cio@example-hospital.org",
  "company": "Example Hospital",
  "title": "Chief Information Officer",
  "industry": "Healthcare",
  "employees": 4200,
  "demo_requested": true,
  "webinar_attended": true,
  "pricing_page_visit": true
}
```

**Business impact:** speed to lead goes from hours or days of manual triage to near-instant routing, with consistent scoring and a clean CRM record for every lead.

> This is a portfolio example with placeholder endpoints. It demonstrates the design, not a specific client's implementation.
