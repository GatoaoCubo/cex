---
kind: instruction
id: bld_instruction_social_publisher
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for social publisher artifacts
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.1
title: "Instruction Social Publisher"
version: "1.0.0"
author: n03_builder
tags: [social_publisher, builder, examples]
tldr: "Golden and anti-examples for social publisher construction, demonstrating ideal structure and common pitfalls."
domain: "social publisher construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Instructions: How to Produce a social_publisher

## Phase 1: RESEARCH
1. Identify the target business: niche, tone, persona, platforms, audience
2. Determine catalog source: Supabase, Shopify API, Airtable, CSV, manual YAML
3. List target platforms and their API constraints (rate limits, media formats, caption lengths)
4. Define content mix ratio: product% + educational% + tips% + trends% = 100%
5. Research optimal posting times for each platform in the business timezone
6. Identify publisher API: Ayrshare (hosted), Postiz (self-hosted), Meta Graph (direct)
7. Define notification channels: Discord webhook, Slack, email, none
8. Check existing social_publisher artifacts to avoid config overlap

## Phase 2: COMPOSE
1. Read bld_schema_social_publisher.md — source of truth for config fields
2. Read bld_output_template_social_publisher.md — template structure
3. Fill frontmatter: id, kind, pillar, title, version, quality: null
4. Write Pipeline section: 10 steps (LOAD→FETCH→SELECT→GENERATE→OPTIMIZE→HASHTAGS→PUBLISH→LOG→NOTIFY→ROTATE)
5. Write Config Schema section: all variable fields grouped by category
6. For each pipeline step document: input, process, output, failure mode
7. Write Platform Matrix: supported platforms × API × limits × best posting times
8. Write Content Strategy: mix ratios, calendar template, rotation rules
9. Write Quality Gates: caption length, hashtag count, image dimensions, score threshold
10. Write Scheduling: cron expression format, timezone handling, retry policy
11. Ensure zero hardcoded company names — ALL via `{{variable}}`

## Phase 3: VALIDATE
1. Check all 10 pipeline steps are documented with input/output
2. Verify config schema covers: identity, platforms, schedule, catalog, publisher, hashtags, notifications
3. Verify no API keys appear in plaintext — only ENV_VAR references
4. Verify content mix percentages sum to 100
5. Verify retry/backoff is defined for API calls
6. Verify posting times are timezone-aware
7. Check body <= 4096 bytes per file
8. Cross-check: does any hardcoded value exist that should be in config?

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify social
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | social publisher construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
