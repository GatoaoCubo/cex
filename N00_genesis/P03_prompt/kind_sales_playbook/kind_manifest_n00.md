---
id: n00_sales_playbook_manifest
kind: knowledge_card
pillar: P03
nucleus: n00
title: "Sales Playbook -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, sales_playbook, p03, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A sales_playbook codifies buyer personas, discovery conversation flows, objection handling scripts, and deal qualification criteria into LLM-executable prompts. It translates the institutional knowledge of top-performing salespeople into a structured protocol that AI agents and human reps can follow consistently. The output is a complete sales motion artifact covering the full funnel from qualification to close.

## Pillar
P03 -- prompt

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `sales_playbook` |
| pillar | string | yes | Always `P03` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| target_personas | list | yes | Buyer personas with role, pain points, decision criteria |
| discovery_flow | list | yes | Ordered discovery questions with branching logic |
| objection_scripts | map | yes | Common objection -> reframe response mapping |
| qualification_criteria | list | yes | MEDDIC or BANT criteria fields |

## When to use
- When building AI-assisted sales agents that need structured conversation protocols
- When onboarding new sales reps with codified institutional knowledge
- When N06 Commercial needs to generate outreach prompts grounded in proven sales motion

## Builder
`archetypes/builders/sales_playbook-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind sales_playbook --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: sp_saas_smb_outbound
kind: sales_playbook
pillar: P03
nucleus: n06
title: "SaaS SMB Outbound Playbook"
version: 1.0
quality: null
---
target_personas:
  - role: "Head of Operations"
    pain: "Manual reporting takes 10h/week"
    decision_criteria: [ROI, ease_of_integration, support_quality]
qualification_criteria: [budget_confirmed, authority_identified, need_validated, timeline_set]
```

## Related kinds
- `expansion_play` (P03) -- post-close playbook for growing the account
- `churn_prevention_playbook` (P03) -- retention playbook triggered when deal health drops
- `content_monetization` (P11) -- pricing and packaging context injected into sales conversations
- `prompt_template` (P03) -- templates for outreach emails, call scripts, and follow-ups
