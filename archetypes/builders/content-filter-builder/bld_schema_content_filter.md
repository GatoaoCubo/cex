---
kind: schema
id: bld_schema_content_filter
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for content_filter
quality: 9.1
title: "Schema Content Filter"
version: "1.0.0"
author: wave1_builder_gen
tags: [content_filter, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for content_filter"
domain: "content_filter construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_schema_reranker_config
  - bld_schema_sandbox_config
  - bld_schema_usage_report
  - bld_schema_search_strategy
  - bld_schema_thinking_config
  - bld_schema_quickstart_guide
  - bld_schema_rl_algorithm
  - bld_schema_voice_pipeline
  - bld_schema_agent_profile
  - bld_schema_pitch_deck
---

## Frontmatter Fields

This ISO defines a content filter -- the moderation rules that gate output or input.
### Required
| Field      | Type   | Required | Default | Notes |
|------------|--------|----------|---------|-------|
| id         | string | yes      | -       | Unique identifier |
| kind       | string | yes      | "content_filter" | CEX kind |
| pillar     | string | yes      | "P11"    | Pillar classification |
| title      | string | yes      | -       | Human-readable name |
| version    | string | yes      | "1.0"   | Schema version |
| created    | date   | yes      | -       | ISO 8601 date |
| updated    | date   | yes      | -       | ISO 8601 date |
| author     | string | yes      | -       | Owner/creator |
| domain     | string | yes      | -       | Application domain |
| quality    | string | yes      | "draft" | Quality status |
| tags       | list   | yes      | []      | Metadata tags |
| tldr       | string | yes      | -       | Summary |
| filter_type | string | yes      | -       | Filter category (e.g., "moderation") |
| sensitivity_level | integer | yes | 1 | 1-5 sensitivity rating |

### Recommended
| Field              | Type   | Notes |
|--------------------|--------|-------|
| review_status      | string | "pending" / "approved" |
| deprecated         | bool   | False |
| last_reviewed      | date   | ISO 8601 date |

## ID Pattern
^p11_cf_[a-zA-Z0-9_]+\.md$

## Body Structure
1. **Overview**
   - Purpose, scope, and use case for the content filter.

2. **Filter Rules**
   - Detailed list of patterns, keywords, or criteria to block/allow.

3. **Scope**
   - Contexts where the filter applies (e.g., user input, URLs).

4. **Enforcement**
   - Technical implementation details (e.g., regex, API checks).

5. **Examples**
   - Sample inputs/outputs demonstrating filter behavior.

## Constraints
- ID must match naming pattern and be unique.
- Required fields must be present and valid.
- File size must not exceed 4096 bytes.
- Sensitivity_level must be integer between 1-5.
- Filter rules must be non-empty and syntactically valid.
- Domain must align with application context.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.66 |
| [[bld_schema_sandbox_config]] | sibling | 0.66 |
| [[bld_schema_usage_report]] | sibling | 0.66 |
| [[bld_schema_search_strategy]] | sibling | 0.66 |
| [[bld_schema_thinking_config]] | sibling | 0.65 |
| [[bld_schema_quickstart_guide]] | sibling | 0.64 |
| [[bld_schema_rl_algorithm]] | sibling | 0.64 |
| [[bld_schema_voice_pipeline]] | sibling | 0.64 |
| [[bld_schema_agent_profile]] | sibling | 0.64 |
| [[bld_schema_pitch_deck]] | sibling | 0.63 |
