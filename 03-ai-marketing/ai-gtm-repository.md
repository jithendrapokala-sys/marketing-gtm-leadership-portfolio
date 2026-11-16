# Designing a Centralized AI Repository for GTM

At InterScripts I built the organization's centralized AI repository and automated marketing workflows from scratch. This document describes the design approach I use. It's a general architecture, not company-confidential detail.

## Why a Repository, Not Scattered Tools

Without one, every marketer writes their own prompts, results vary, knowledge is lost when people leave, and nobody can measure impact. A shared repository makes AI work **repeatable, consistent and measurable**.

## Architecture

```
            ┌──────────────────── Knowledge layer ────────────────────┐
            │ Positioning & message house · Personas · Case studies    │
            │ Product docs · Brand voice guide · Approved proof points │
            └──────────────────────────┬──────────────────────────────┘
                                       │ (retrieval)
┌──────────────┐   ┌───────────────────▼──────────────────┐   ┌─────────────────┐
│  Triggers     │──▶│  Orchestration (n8n)                  │──▶│  Outputs         │
│  CRM events   │   │  ┌─────────────────────────────────┐ │   │  CRM notes/fields│
│  Form fills   │   │  │ Agent workflows (LangChain /     │ │   │  Seller briefs   │
│  Schedules    │   │  │ LangGraph): research → enrich →  │ │   │  Draft emails    │
│  Slack/manual │   │  │ draft → check → hand-off         │ │   │  Landing pages   │
└──────────────┘   │  └─────────────────────────────────┘ │   │  Dashboards      │
                   │  Prompt library · Guardrails · Logs   │   └─────────────────┘
                   └──────────────────────────────────────┘
                                       │
                         Enrichment & CRM APIs (REST)
```

## Components

| Component | What it holds | Owner |
|---|---|---|
| Knowledge layer | Approved messaging, personas, proof points, brand voice | Product marketing |
| Prompt library | Versioned, tested prompt templates (see [prompts/](prompts/)) | Marketing ops |
| Workflows | n8n flows calling LLMs, enrichment and CRM APIs | Marketing ops |
| Guardrails | Review steps, banned claims, data rules (see [governance](governance.md)) | Marketing leader |
| Measurement | Time saved, output volume, conversion of AI-assisted vs. manual work | Marketing ops |

## Example Workflow — Account Research Brief (LangGraph-style)

1. **Trigger:** account moves to Tier 1 in CRM
2. **Research node:** collect public company information and recent news
3. **Enrich node:** call enrichment API for firmographics and technology stack
4. **Analyze node:** LLM maps findings to our ICP pains and value pillars
5. **Draft node:** produce a one-page brief + 3 persona outreach angles
6. **Check node:** verify claims cite a source; flag gaps for a human
7. **Deliver:** write the brief to the CRM account record and alert the owner

**Impact measured:** research time per account before vs. after, and meeting rate on accounts with a brief vs. without.

## Rollout Approach

1. Pick 2–3 high-value, low-effort use cases
2. Build, measure the time saved, share the wins
3. Add to the library; train the team
4. Expand to the next use cases each quarter
