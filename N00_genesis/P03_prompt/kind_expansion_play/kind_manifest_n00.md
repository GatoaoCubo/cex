---
id: n00_expansion_play_manifest
kind: knowledge_card
8f: F3_inject
pillar: P03
nucleus: n00
title: "Expansion Play -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, expansion_play, p03, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_expansion_play
  - bld_schema_sales_playbook
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - expansion-play-builder
  - p03_sp_expansion_play_builder
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_benchmark_suite
  - bld_schema_churn_prevention_playbook
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An expansion_play is an account expansion playbook that defines upsell triggers, cross-sell opportunity maps, and net revenue retention (NRR) mechanics for existing customers. It translates product usage signals and account health data into LLM-executable prompts that guide sales or success teams through expansion conversations. The output is a structured playbook that systematically grows revenue within the existing customer base.

## Pillar
P03 -- prompt

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `expansion_play` |
| pillar | string | yes | Always `P03` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| upsell_triggers | list | yes | Product signals that indicate upgrade readiness |
| cross_sell_map | map | yes | Current product -> adjacent product opportunity mapping |
| nrr_target | float | yes | Net revenue retention target (e.g. 120%) |
| expansion_sequences | list | no | Step-by-step conversation flows per segment |

## When to use
- When building automated expansion workflows for SaaS or subscription businesses
- When product usage data needs to be converted into structured sales motion prompts
- When customer success teams need codified playbooks for upsell and cross-sell conversations

## Builder
`archetypes/builders/expansion_play-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind expansion_play --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: ep_saas_seat_expansion
kind: expansion_play
pillar: P03
nucleus: n06
title: "Seat Expansion Play -- SMB Tier"
version: 1.0
quality: null
---
upsell_triggers:
  - seats_at_90pct_capacity: true
  - api_calls_above_plan_limit: true
nrr_target: 125.0
cross_sell_map:
  core_product: [analytics_addon, sso_addon]
```

## Related kinds
- `churn_prevention_playbook` (P03) -- retention counterpart triggered before expansion readiness
- `sales_playbook` (P03) -- new logo acquisition playbook that feeds accounts into expansion plays
- `content_monetization` (P11) -- revenue model that defines expansion SKUs and pricing
- `scoring_rubric` (P07) -- account health scoring that triggers expansion_play activation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_expansion_play]] | downstream | 0.43 |
| [[bld_schema_sales_playbook]] | downstream | 0.41 |
| [[bld_schema_integration_guide]] | downstream | 0.39 |
| [[bld_schema_reranker_config]] | downstream | 0.38 |
| [[expansion-play-builder]] | related | 0.38 |
| [[p03_sp_expansion_play_builder]] | related | 0.37 |
| [[bld_schema_usage_report]] | downstream | 0.36 |
| [[bld_schema_dataset_card]] | downstream | 0.36 |
| [[bld_schema_benchmark_suite]] | downstream | 0.36 |
| [[bld_schema_churn_prevention_playbook]] | downstream | 0.36 |
