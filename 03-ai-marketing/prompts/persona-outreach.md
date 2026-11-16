# Prompt — Persona Outreach Email

**Inputs:** persona, account brief, message house, proof point
**Output:** 3 short email variants for a human to choose from and edit

```text
You are writing a first-touch B2B email to a {{persona title}} at {{company}}.

What this persona cares about: {{persona goals}}
Relevant account context: {{2-3 points from the account brief}}
Our message for this persona: {{message house pillar}}
Approved proof point: {{proof point}}

Write 3 variants. Each must:
- Be under 110 words, plain text, no buzzwords
- Open with something specific to their company, not to us
- Make one point and include the proof point
- End with a low-friction ask (a 15-minute conversation or a relevant resource)
- Include a subject line under 7 words

Do not make claims beyond the proof point provided.
```
