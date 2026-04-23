---
kind: config
id: bld_config_multi_modal_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 20
disallowed_tools: []
fork_context: fork
hooks:
  pre_build: null
  post_build: null
permission_scope: nucleus
quality: 9.0
title: "Config Multi Modal Config"
version: "1.0.0"
author: n03_builder
tags: [multi_modal_config, builder, examples]
tldr: "Golden and anti-examples for multi modal config construction, demonstrating ideal structure and common pitfalls."
domain: "multi modal config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_output_template_multi_modal_config
  - bld_collaboration_multi_modal_config
  - bld_knowledge_card_multi_modal_config
  - bld_examples_multi_modal_config
  - bld_instruction_multi_modal_config
  - bld_config_retriever_config
  - bld_tools_multi_modal_config
  - multi-modal-config-builder
  - bld_schema_multi_modal_config
  - bld_config_memory_scope
---
# Config: multi_modal_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_mmc_{capability_slug}.yaml` | `p04_mmc_document_analysis.yaml` |
| Builder directory | kebab-case | `multi-modal-config-builder/` |
| Frontmatter fields | snake_case | `supported_modalities`, `routing_model` |
Rule: id MUST equal filename stem.
## File Paths
1. Output: `P04_tools/examples/p04_mmc_{capability}.yaml`
2. Compiled: `P04_tools/compiled/p04_mmc_{capability}.yaml`
## Size Limits
1. Total file: max 2048 bytes
2. tldr: <= 160 chars
## Modality Defaults
| Modality | Default Resolution/Duration | Token Estimate |
|----------|---------------------------|----------------|
| Image (low) | 768x768 | ~400 tokens |
| Image (med) | 1024x1024 | ~750 tokens |
| Image (high) | 2048x2048 | ~1500 tokens |
| Audio | 600s max | ~300 tokens/min (transcribed) |
| Video | 60s max | ~1500 tokens (keyframes) |
| Document (PDF) | per page | ~1200 tokens/page |

## Metadata

```yaml
id: bld_config_multi_modal_config
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-multi-modal-config.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_multi_modal_config]] | upstream | 0.39 |
| [[bld_collaboration_multi_modal_config]] | downstream | 0.35 |
| [[bld_knowledge_card_multi_modal_config]] | upstream | 0.34 |
| [[bld_examples_multi_modal_config]] | upstream | 0.33 |
| [[bld_instruction_multi_modal_config]] | upstream | 0.32 |
| [[bld_config_retriever_config]] | sibling | 0.30 |
| [[bld_tools_multi_modal_config]] | upstream | 0.30 |
| [[multi-modal-config-builder]] | upstream | 0.29 |
| [[bld_schema_multi_modal_config]] | upstream | 0.28 |
| [[bld_config_memory_scope]] | sibling | 0.27 |
