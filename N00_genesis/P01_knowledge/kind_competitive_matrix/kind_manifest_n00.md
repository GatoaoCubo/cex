---
id: n00_competitive_matrix_manifest
kind: knowledge_card
pillar: P01
nucleus: n00
title: "Competitive Matrix -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, competitive_matrix, p01, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_competitive_matrix
  - bld_schema_dataset_card
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_integration_guide
  - bld_schema_search_strategy
  - bld_schema_quickstart_guide
  - bld_schema_benchmark_suite
  - bld_schema_pitch_deck
  - bld_schema_action_paradigm
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Competitive Matrix is a structured feature comparison table used as a sales battle card and strategic intelligence artifact. It maps competitors against a defined feature set, revealing positioning gaps and differentiation opportunities. It produces a living document that enables sales teams to handle objections and identify where to compete or avoid.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `competitive_matrix` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Human-readable matrix name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| market_segment | string | yes | Target market category |
| evaluation_date | date | yes | When data was last verified |
| competitors | list | yes | Competitor names being compared |
| features | list | yes | Feature dimensions being evaluated |
| ratings | map | yes | competitor -> feature -> score/status |
| our_differentiators | list | yes | Where we win vs. field |

## When to use
- When preparing sales enablement materials for competitive deals
- When conducting market positioning analysis for a new product launch
- When intelligence on competitor feature parity is needed

## Builder
`archetypes/builders/competitive_matrix-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind competitive_matrix --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (typically N01 or N06)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- sales team, product managers, executives
- `{{DOMAIN_CONTEXT}}` -- market segment and product category

## Example (minimal)
```yaml
---
id: competitive_matrix_ai_orchestration_q2_2026
kind: competitive_matrix
pillar: P01
nucleus: n01
title: "AI Orchestration Platforms Q2 2026"
version: 1.0
quality: null
---
market_segment: Enterprise AI Orchestration
evaluation_date: 2026-04-17
competitors: [LangChain, CrewAI, AutoGen]
features: [multi-agent, typed-knowledge, brand-aware]
our_differentiators: [typed-knowledge-system, sin-lens, 8F-pipeline]
```

## Related kinds
- `citation` (P01) -- sourced data backing the matrix
- `knowledge_card` (P01) -- atomic competitor facts
- `discovery_questions` (P01) -- MEDDIC questions that reveal competitor gaps
- `customer_segment` (P02) -- ICPs who care about competitive differentiation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_competitive_matrix]] | downstream | 0.53 |
| [[bld_schema_dataset_card]] | downstream | 0.47 |
| [[bld_schema_reranker_config]] | downstream | 0.46 |
| [[bld_schema_usage_report]] | downstream | 0.46 |
| [[bld_schema_integration_guide]] | downstream | 0.44 |
| [[bld_schema_search_strategy]] | downstream | 0.44 |
| [[bld_schema_quickstart_guide]] | downstream | 0.44 |
| [[bld_schema_benchmark_suite]] | downstream | 0.43 |
| [[bld_schema_pitch_deck]] | downstream | 0.43 |
| [[bld_schema_action_paradigm]] | downstream | 0.42 |
