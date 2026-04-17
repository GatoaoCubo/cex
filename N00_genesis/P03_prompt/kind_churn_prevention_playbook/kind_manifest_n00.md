---
id: n00_churn_prevention_playbook_manifest
kind: knowledge_card
pillar: P03
nucleus: n00
title: "Churn Prevention Playbook -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, churn_prevention_playbook, p03, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A churn_prevention_playbook defines signal detection rules, intervention triggers, and recovery sequences for retaining customers at risk of cancellation. It maps early warning indicators to specific playbook branches (automated outreach, discount offer, success call) and codifies the decision logic as LLM-executable prompts. The output is a structured retention protocol that reduces involuntary and voluntary churn.

## Pillar
P03 -- prompt

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `churn_prevention_playbook` |
| pillar | string | yes | Always `P03` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| churn_signals | list | yes | Leading indicators that trigger playbook (usage drop, NPS, etc.) |
| intervention_triggers | list | yes | Conditions that activate each intervention branch |
| escalation_matrix | map | yes | Signal severity -> response owner mapping |
| recovery_sequences | list | no | Step-by-step recovery flows per segment |

## When to use
- When building automated retention workflows for SaaS or subscription products
- When customer success teams need codified escalation logic for at-risk accounts
- When churn signal data needs to be translated into LLM-executable intervention prompts

## Builder
`archetypes/builders/churn_prevention_playbook-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind churn_prevention_playbook --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: cpp_saas_retention_2024
kind: churn_prevention_playbook
pillar: P03
nucleus: n06
title: "SaaS Retention Playbook Q4"
version: 1.0
quality: null
---
churn_signals:
  - login_frequency_drop_7d: ">50%"
  - feature_adoption_score: "<30"
intervention_triggers:
  - signal: login_drop + low_adoption
    action: success_call_within_48h
```

## Related kinds
- `sales_playbook` (P03) -- counterpart focused on acquisition rather than retention
- `expansion_play` (P03) -- upsell logic triggered after churn risk is resolved
- `content_monetization` (P11) -- revenue mechanics that inform retention value props
- `guardrail` (P11) -- safety rules that prevent overly aggressive churn interventions
