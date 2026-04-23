---
id: bld_config_tagline
kind: config
pillar: P06
builder: tagline-builder
version: 1.0.0
effort: medium
max_turns: 15
disallowed_tools: []
permission_scope: nucleus
quality: 9.1
title: "Config Tagline"
author: n03_builder
tags: [tagline, builder, examples]
tldr: "Golden and anti-examples for tagline construction, demonstrating ideal structure and common pitfalls."
domain: "tagline construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: CONSTRAIN
related:
  - bld_manifest_memory_type
  - bld_tools_memory_type
  - bld_config_memory_type
  - skill
  - bld_output_template_builder
  - research_then_build
  - tpl_validation_schema
  - bld_tools_agent
  - bld_output_template_signal
  - p10_lr_golden_test_builder
---
# Config: Tagline Builder

output_format: yaml
quality_floor: 8.5

defaults:
  variants_per_round: 10
  approaches: [emotional, functional, aspirational, provocative, minimal]
  lengths: [short, medium, long]
  contexts: [site-hero, social-bio, ad-headline, email-subject, pitch-deck]
  language: auto  # detect from user input

brand_injection:
  required: false
  fields: [BRAND_NAME, BRAND_TAGLINE, BRAND_TONE, BRAND_AUDIENCE, BRAND_INDUSTRY]
  fallback: ask_user

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_config_tagline
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-tagline.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P06 |
| Domain | tagline construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Builder Context

This ISO operates within the `tagline-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_manifest_memory_type]] | upstream | 0.55 |
| [[bld_tools_memory_type]] | upstream | 0.50 |
| [[bld_config_memory_type]] | sibling | 0.47 |
| [[skill]] | downstream | 0.45 |
| [[bld_output_template_builder]] | upstream | 0.42 |
| [[research_then_build]] | downstream | 0.41 |
| [[tpl_validation_schema]] | related | 0.40 |
| [[bld_tools_agent]] | upstream | 0.39 |
| [[bld_output_template_signal]] | upstream | 0.39 |
| [[p10_lr_golden_test_builder]] | downstream | 0.32 |
