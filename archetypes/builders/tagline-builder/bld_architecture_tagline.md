---
id: bld_architecture_tagline
kind: architecture
pillar: P08
builder: tagline-builder
version: 1.0.0
quality: 9.0
title: "Architecture Tagline"
author: n03_builder
tags: [tagline, builder, examples]
tldr: "Golden and anti-examples for tagline construction, demonstrating ideal structure and common pitfalls."
domain: "tagline construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: CONSTRAIN
related:
  - bld_collaboration_tagline
  - bld_tools_tagline
  - bld_instruction_tagline
  - bld_memory_tagline
  - tagline-builder
  - bld_collaboration_landing_page
  - bld_config_tagline
  - bld_quality_gate_tagline
  - bld_system_prompt_tagline
  - bld_output_template_tagline
---
# Architecture: Tagline Builder

## Pipeline
```
DISCOVER → EXTRACT_USP → GENERATE(5 approaches × 3 lengths) → FILTER(3 tests) → RANK → ADAPT(contexts) → DELIVER
```

## Data Flow
1. Input: brand_config.yaml OR user answers (industry, audience, tone, differentiator)
2. Processing: 15+ candidates → filter → top 5 → adapt → recommend 1
3. Output: YAML with variants, scores, context adaptations, reasoning

## Dependencies
1. brand_config.yaml (optional — falls back to user interview)
2. Competitor taglines (optional — for differentiation check)

## Integration Points
1. N02 Marketing: consumes taglines for campaigns, ads, social posts
2. N06 Commercial: uses taglines in pricing pages, pitch decks, brand book
3. landing-page-builder: uses recommended tagline as hero headline

## Properties

| Property | Value |
|----------|-------|
| Kind | `architecture` |
| Pillar | P08 |
| Domain | tagline construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_tagline]] | downstream | 0.45 |
| [[bld_tools_tagline]] | upstream | 0.40 |
| [[bld_instruction_tagline]] | upstream | 0.38 |
| [[bld_memory_tagline]] | downstream | 0.36 |
| [[tagline-builder]] | upstream | 0.35 |
| [[bld_collaboration_landing_page]] | downstream | 0.34 |
| [[bld_config_tagline]] | upstream | 0.34 |
| [[bld_quality_gate_tagline]] | upstream | 0.34 |
| [[bld_system_prompt_tagline]] | upstream | 0.33 |
| [[bld_output_template_tagline]] | upstream | 0.31 |
