---
id: p02_bc_builder_nucleus
kind: boot_config
pillar: P02
title: Boot Config -- Builder Nucleus
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [boot-config, builder, N03]
tldr: Initialization config -- env vars, paths, model defaults, feature flags.
density_score: 0.88
related:
  - bld_architecture_kind
  - bld_tools_kind
  - kind-builder
  - bld_collaboration_kind
  - ex_env_config_default
  - bld_instruction_kind
  - p06_schema_env_contract
  - p12_sc_builder_nucleus
  - bld_config_kind
  - p04_ct_fix_frontmatter
---

# Boot Config: Builder Nucleus

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| CEX_ROOT | no | auto-detect | Path to CEX repo |
| ANTHROPIC_API_KEY | yes (for LLM) | none | API key |
| CEX_MODEL | no | opus | Default model |
| CEX_DRY_RUN | no | false | Global dry-run |
| CEX_QUALITY_MIN | no | 8.0 | Quality floor |
| CEX_MAX_RETRIES | no | 2 | Max F6-F7 cycles |

## Paths

| Path | Purpose |
|------|---------|
| .cex/kinds_meta.json | Kind registry |
| archetypes/builders/ | Builder ISOs |
| archetypes/TYPE_TO_TEMPLATE.yaml | Kind-template map |
| P01_knowledge/library/kind/ | Kind KCs |
| _tools/ | Pipeline scripts |

## Feature Flags

| Flag | Default | Effect |
|------|---------|--------|
| auto_compile | true | Compile after build |
| auto_index | true | Index after build |
| strict_density | false | 0.85 instead of 0.80 |
| crew_mode | false | Multi-kind crews |

## Startup

1. Detect CEX_ROOT
2. Verify kinds_meta.json
3. Count builders
4. Check API key if not dry-run
5. Load mental_model
6. Ready

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | downstream | 0.35 |
| [[bld_tools_kind]] | downstream | 0.34 |
| [[kind-builder]] | downstream | 0.31 |
| [[bld_collaboration_kind]] | downstream | 0.29 |
| [[ex_env_config_default]] | downstream | 0.28 |
| [[bld_instruction_kind]] | downstream | 0.27 |
| [[p06_schema_env_contract]] | downstream | 0.24 |
| [[p12_sc_builder_nucleus]] | downstream | 0.23 |
| [[bld_config_kind]] | downstream | 0.22 |
| [[p04_ct_fix_frontmatter]] | downstream | 0.21 |
