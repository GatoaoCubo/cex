---
id: n00_webinar_script_manifest
kind: knowledge_card
pillar: P03
nucleus: n00
title: "Webinar Script -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, webinar_script, p03, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_reranker_config
  - bld_schema_multimodal_prompt
  - bld_schema_pitch_deck
  - bld_schema_integration_guide
  - bld_schema_usage_report
  - bld_schema_quickstart_guide
  - bld_schema_benchmark_suite
  - bld_schema_action_paradigm
  - bld_schema_webinar_script
  - bld_schema_dataset_card
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A webinar_script is a complete scripted presentation artifact covering intro, agenda, content segments, Q&A handling, and call-to-action sequences for live or recorded webinars. It structures the speaker's narrative, slide transitions, and audience engagement moments into a production-ready document. The output enables speakers to deliver consistent, high-conversion presentations without improvisation risk.

## Pillar
P03 -- prompt

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `webinar_script` |
| pillar | string | yes | Always `P03` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| duration_minutes | integer | yes | Total presentation duration target |
| segments | list | yes | Ordered segments: intro, agenda, content_N, qa, cta |
| audience_persona | string | yes | Target audience role and knowledge level |
| primary_cta | string | yes | The conversion action requested at close |

## When to use
- When N02 Marketing needs a scripted webinar for lead generation or product education
- When a course launch requires a live demonstration presentation with structured Q&A
- When building a series of educational webinars with consistent structure across sessions

## Builder
`archetypes/builders/webinar_script-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind webinar_script --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: ws_cex_product_demo_q2
kind: webinar_script
pillar: P03
nucleus: n02
title: "CEX Product Demo Webinar Q2"
version: 1.0
quality: null
---
duration_minutes: 60
audience_persona: "Senior AI engineers and CTOs at 50-500 person companies"
primary_cta: "Book a 30-minute custom CEX demo"
segments:
  - intro: 5min
  - agenda: 2min
  - problem_framing: 10min
  - live_demo: 25min
  - case_study: 10min
  - qa: 5min
  - cta_close: 3min
```

## Related kinds
- `sales_playbook` (P03) -- sales motion context injected into the CTA segment
- `prompt_template` (P03) -- templates for generating segment-specific script content
- `landing_page` (P05) -- registration page that feeds attendees into the webinar
- `content_monetization` (P11) -- monetization mechanics behind the webinar offer

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | downstream | 0.42 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.41 |
| [[bld_schema_pitch_deck]] | downstream | 0.41 |
| [[bld_schema_integration_guide]] | downstream | 0.41 |
| [[bld_schema_usage_report]] | downstream | 0.41 |
| [[bld_schema_quickstart_guide]] | downstream | 0.41 |
| [[bld_schema_benchmark_suite]] | downstream | 0.40 |
| [[bld_schema_action_paradigm]] | downstream | 0.40 |
| [[bld_schema_webinar_script]] | downstream | 0.40 |
| [[bld_schema_dataset_card]] | downstream | 0.40 |
