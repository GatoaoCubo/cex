---
id: n00_course_module_manifest
kind: knowledge_card
8f: F3_inject
pillar: P05
nucleus: n00
title: "Course Module -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, course_module, p05, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_quickstart_guide
  - bld_schema_course_module
  - bld_schema_usage_report
  - bld_schema_pitch_deck
  - bld_schema_onboarding_flow
  - bld_schema_search_strategy
  - bld_schema_benchmark_suite
  - bld_schema_contributor_guide
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Course module produces a structured online learning unit with explicit learning objectives, lesson content, knowledge checks, and assessments. It follows instructional design principles (Bloom's taxonomy, spaced repetition cues) to maximize knowledge retention. Each module is self-contained and sequenceable within a larger course curriculum.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `course_module` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Module title (Bloom verb + topic) |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| learning_objectives | list | yes | 3-5 measurable outcomes (Bloom verb + topic) |
| estimated_duration_min | int | yes | Time to complete in minutes |
| prerequisite_modules | list | no | IDs of modules that should precede this |
| lesson_sections | list | yes | Ordered lesson content sections |
| knowledge_checks | list | yes | Mid-module comprehension questions |
| assessment | object | yes | Final quiz or practical exercise spec |

## When to use
- Building a paid online course or certification program
- Creating internal training content for onboarding or upskilling
- Packaging domain expertise as a monetizable educational product

## Builder
`archetypes/builders/course_module-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind course_module --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N06 commercial monetizes; N02 markets; N04 structures content
- `{{SIN_LENS}}` -- Strategic Greed: maximum value delivery that justifies price point
- `{{TARGET_AUDIENCE}}` -- learner persona with prerequisite knowledge level
- `{{DOMAIN_CONTEXT}}` -- subject matter, skill level, platform (Teachable, Kajabi, etc.)

## Example (minimal)
```yaml
---
id: course_module_cex_8f_pipeline_m01
kind: course_module
pillar: P05
nucleus: n06
title: "Apply the 8F Pipeline to Any AI Task"
version: 1.0
quality: null
---
learning_objectives:
  - "Identify the 8 functions of the CEX reasoning pipeline"
  - "Apply F1-F4 to a given user intent"
estimated_duration_min: 25
```

## Related kinds
- `scoring_rubric` (P07) -- defines assessment criteria for module completion
- `onboarding_flow` (P05) -- sequences modules into a guided activation path
- `content_monetization` (P11) -- pricing and packaging for course products

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_integration_guide]] | downstream | 0.45 |
| [[bld_schema_reranker_config]] | downstream | 0.45 |
| [[bld_schema_quickstart_guide]] | downstream | 0.44 |
| [[bld_schema_course_module]] | downstream | 0.43 |
| [[bld_schema_usage_report]] | downstream | 0.43 |
| [[bld_schema_pitch_deck]] | downstream | 0.42 |
| [[bld_schema_onboarding_flow]] | downstream | 0.42 |
| [[bld_schema_search_strategy]] | downstream | 0.42 |
| [[bld_schema_benchmark_suite]] | downstream | 0.42 |
| [[bld_schema_contributor_guide]] | downstream | 0.42 |
