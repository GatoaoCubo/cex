---
kind: schema
id: bld_schema_competitive_matrix
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for competitive_matrix
quality: 9.1
title: "Schema Competitive Matrix"
version: "1.1.0"
author: wave1_builder_gen_v2
tags: [competitive_matrix, builder, schema]
tldr: "Formal schema -- feature-parity grid + battle card + Gartner MQ positioning for competitive_matrix."
domain: "competitive_matrix construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string | yes | | Must match ID Pattern |
| kind | string | yes | | Always "competitive_matrix" |
| pillar | string | yes | | P01 |
| title | string | yes | | "{Market Segment} Competitive Matrix" |
| version | string | yes | | Artifact version (e.g., "1.0.0") |
| created | string | yes | | ISO 8601 YYYY-MM-DD |
| updated | string | yes | | ISO 8601 YYYY-MM-DD |
| author | string | yes | | Analyst username |
| domain | string | yes | | Market domain |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | list | yes | | Market segment, competitive_matrix |
| tldr | string | yes | | "Our product vs N competitors on M dimensions" |
| competitors | list | yes | | Named vendors (min 3) |
| metrics | list | yes | | Capability dimensions compared |
| analysis_date | string | yes | | ISO 8601 YYYY-MM-DD of data collection |
| key_insights | string | yes | | Top differentiator in one sentence |

### Recommended
| Field | Type | Notes |
|-------|------|-------|
| primary_competitor | string | Competitor most frequently in evaluated deals |
| data_sources | list | Source names with access dates |
| reviewers | list | Peer reviewer usernames |

## ID Pattern
^p01_cm_[a-z][a-z0-9_]+\\.md$

## Body Structure
1. **Market Context** -- Segment, analysis date, data sources, analyst
2. **Feature Parity Grid** -- Rows = capabilities, cols = us + competitors; Yes/No/Partial/Roadmap Q# YYYY
3. **Gartner MQ Positioning** -- Ability to Execute (1-5) x Completeness of Vision (1-5) per vendor
4. **Battle Card** -- Us vs primary competitor: capability, our strength, their weakness, win reason
5. **Pricing Comparison** -- Entry/mid/enterprise tiers + pricing model per vendor
6. **Strategic Insights** -- Top 3 differentiators, 2 gaps, anti-FUD guide

## Constraints
- ID must match ^p01_cm_[a-z][a-z0-9_]+\\.md$ exactly.
- analysis_date must be ISO 8601 format.
- competitors list must name at least 3 vendors (no placeholder names).
- File size must not exceed 5120 bytes.
- quality field must be null (peer-reviewed only).
- All capability values must use: Yes / No / Partial / Roadmap Q# YYYY (no vague adjectives).
- All claims must cite a primary source with access date.
- Roadmap items must include target quarter and year.
