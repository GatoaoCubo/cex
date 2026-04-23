---
id: n00_social_publisher_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Social Publisher -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, social_publisher, p04, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_usage_report
  - bld_schema_search_strategy
  - bld_schema_integration_guide
  - bld_schema_voice_pipeline
  - bld_schema_pitch_deck
  - bld_schema_quickstart_guide
  - bld_schema_dataset_card
  - bld_schema_action_paradigm
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A social_publisher is an automatic content publishing agent that executes the full social media workflow: LOAD content -> FETCH platform specs -> SELECT best content piece -> GENERATE platform-optimized post -> OPTIMIZE for engagement -> HASHTAGS -> PUBLISH. It abstracts platform APIs (LinkedIn, Twitter/X, Instagram, TikTok) into a single publishing interface with brand voice enforcement and performance tracking. The output is published social content with post IDs and performance baseline metrics.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `social_publisher` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| platforms | list | yes | Target platforms: linkedin, twitter, instagram, tiktok |
| content_source | string | yes | Where content originates: knowledge_card, prompt_template, manual |
| brand_voice_id | string | yes | Reference to brand_config.yaml for voice enforcement |
| approval_required | boolean | yes | Whether human review is needed before publishing |

## When to use
- When N02 Marketing needs automated social media content publishing from CEX artifacts
- When a content calendar (schedule artifact) needs automatic execution and publishing
- When building a fully autonomous marketing pipeline that produces and publishes content

## Builder
`archetypes/builders/social_publisher-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind social_publisher --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: sp_linkedin_weekly_publisher
kind: social_publisher
pillar: P04
nucleus: n02
title: "LinkedIn Weekly Content Publisher"
version: 1.0
quality: null
---
platforms: [linkedin]
content_source: prompt_template
brand_voice_id: "brand_config_gatoaocubo"
approval_required: true
```

## Related kinds
- `notifier` (P04) -- alert tool that social_publisher uses for approval requests
- `prompt_template` (P03) -- template used in the GENERATE stage of the publishing pipeline
- `schedule` (P12) -- schedule artifact that triggers social_publisher on a cron
- `api_client` (P04) -- API client that social_publisher uses to call platform publishing APIs

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | downstream | 0.38 |
| [[bld_schema_benchmark_suite]] | downstream | 0.38 |
| [[bld_schema_usage_report]] | downstream | 0.38 |
| [[bld_schema_search_strategy]] | downstream | 0.37 |
| [[bld_schema_integration_guide]] | downstream | 0.37 |
| [[bld_schema_voice_pipeline]] | downstream | 0.37 |
| [[bld_schema_pitch_deck]] | downstream | 0.37 |
| [[bld_schema_quickstart_guide]] | downstream | 0.37 |
| [[bld_schema_dataset_card]] | downstream | 0.37 |
| [[bld_schema_action_paradigm]] | downstream | 0.37 |
