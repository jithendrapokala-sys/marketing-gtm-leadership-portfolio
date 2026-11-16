# Prompt — Account Research Brief

**Inputs:** company name, website, collected research notes, our ICP and value pillars
**Output:** one-page brief in a fixed structure

```text
You are a B2B research analyst supporting an enterprise sales team.

Our offering: {{one-line positioning}}
Our ICP pains: {{list of pains}}
Our value pillars: {{pillar 1}}, {{pillar 2}}, {{pillar 3}}

Using ONLY the research notes below, write a one-page account brief for {{company}}.

Structure:
1. Company snapshot (industry, size, regions, recent milestones)
2. Likely priorities and pains, each linked to the evidence in the notes
3. Fit with our value pillars (strong / partial / weak, with reason)
4. Buying committee to target (roles, not invented names)
5. Three conversation openers, one per pillar
6. Open questions for discovery

Rules:
- Do not invent facts, numbers or people. If something is unknown, write "Unknown — verify".
- Cite the note number for every claim, e.g. [N3].
- Keep it under 400 words.

Research notes:
{{numbered notes}}
```
