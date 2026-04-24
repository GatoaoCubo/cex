---
id: n00_edtech_vertical_manifest
kind: knowledge_card
8f: F3_inject
pillar: P01
nucleus: n00
title: "EdTech Vertical -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, edtech_vertical, p01, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_edtech_vertical
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_schema_dataset_card
  - bld_schema_quickstart_guide
  - bld_schema_usage_report
  - bld_schema_search_strategy
  - bld_schema_action_paradigm
  - bld_schema_benchmark_suite
  - bld_schema_pitch_deck
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
EdTech Vertical packages domain knowledge for the Education Technology sector, covering learning management systems, instructional design patterns, accreditation requirements, and key buyer personas. It enables nuclei to generate education-aware content, agents, and analyses without requiring repeated domain briefing. Particularly relevant for N06 (course monetization) and N02 (learning-focused copy).

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `edtech_vertical` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Vertical name and scope |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| sub_verticals | list | no | K-12, higher-ed, corporate learning, bootcamp |
| key_kpis | list | yes | Completion rate, NPS, ARPU, course revenue |
| regulatory | list | no | FERPA, LGPD, accessibility (WCAG) |
| lms_platforms | list | no | Moodle, Canvas, Hotmart, Teachable |
| buyer_personas | list | yes | Learner, instructor, institution buyer |

## When to use
- When building content or agents for education platforms
- When pricing or packaging online courses
- When analyzing EdTech market segments for competitive intelligence

## Builder
`archetypes/builders/edtech_vertical-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind edtech_vertical --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N01, N02, N06)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- course creators, EdTech operators
- `{{DOMAIN_CONTEXT}}` -- geography and learning modality

## Example (minimal)
```yaml
---
id: edtech_vertical_online_courses_latam
kind: edtech_vertical
pillar: P01
nucleus: n06
title: "Online Courses LATAM"
version: 1.0
quality: null
---
sub_verticals: [bootcamp, self-paced]
key_kpis: [completion_rate, course_revenue, NPS]
lms_platforms: [Hotmart, Kiwify, Teachable]
buyer_personas: [lifelong_learner, career_switcher]
```

## Related kinds
- `context_doc` (P01) -- domain context for EdTech
- `customer_segment` (P02) -- learner and institutional ICPs
- `competitive_matrix` (P01) -- EdTech platform comparison
- `healthcare_vertical` (P01) -- adjacent for medical education

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_edtech_vertical]] | downstream | 0.41 |
| [[bld_schema_reranker_config]] | downstream | 0.39 |
| [[bld_schema_integration_guide]] | downstream | 0.39 |
| [[bld_schema_dataset_card]] | downstream | 0.38 |
| [[bld_schema_quickstart_guide]] | downstream | 0.37 |
| [[bld_schema_usage_report]] | downstream | 0.37 |
| [[bld_schema_search_strategy]] | downstream | 0.36 |
| [[bld_schema_action_paradigm]] | downstream | 0.36 |
| [[bld_schema_benchmark_suite]] | downstream | 0.36 |
| [[bld_schema_pitch_deck]] | downstream | 0.35 |
