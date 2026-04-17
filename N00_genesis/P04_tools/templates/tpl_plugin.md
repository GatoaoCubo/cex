---
# TEMPLATE: Plugin (P04 Tools)
# Valide contra P04_tools/_schema.yaml (types.plugin)
# Max 2048 bytes

id: p04_plug_{{PLUGIN_SLUG}}
kind: plugin
name: {{PLUGIN_NAME}}
version: 1.0.0
entrypoint: {{MODULE_OR_COMMAND}}
capabilities: [{{CAP_1}}, {{CAP_2}}]
repository: {{GITHUB_URL}}
license: MIT
keywords: [{{KW1}}, {{KW2}}, {{KW3}}]
author_url: {{AUTHOR_URL}}
quality: 9.0
title: "Tpl Plugin"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for tool integration, demonstrating ideal structure and common pitfalls."
domain: "tool integration"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Plugin: {{PLUGIN_NAME}}

## Purpose
<!-- INSTRUCAO: explicar extensao e fronteira do plugin. -->
1. Extends: {{HOST_SYSTEM}}
2. Adds: {{CAPABILIDADE_PRINCIPAL}}
3. Does not own: {{AREA_FORA_DE_ESCOPO}}

## Integration
| Field | Value |
|-------|-------|
| Entrypoint | {{MODULE_OR_COMMAND}} |
| Inputs | {{INPUTS_ESPERADOS}} |
| Outputs | {{OUTPUTS_GERADOS}} |
| Dependencies | {{DEP_1}}, {{DEP_2}} |

## Lifecycle
1. Load: {{COMO_CARREGA}}
2. Execute: {{COMO_OPERA}}
3. Unload: {{COMO_LIBERA_ESTADO}}

## Failure Handling
1. Retry: {{POLITICA_DE_RETRY}}
2. Fallback: {{COMPORTAMENTO_DEGRADADO}}
3. Audit: {{ONDE_LOGAR}}

## Metadata

```yaml
id: p04_plug_{{PLUGIN_SLUG}}
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p04-plug-{{PLUGIN-SLUG}}.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `plugin` |
| Pillar |  |
| Domain | tool integration |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## System Context

This artifact participates in the CEX typed knowledge system, a fractal
architecture with 12 pillars, 8 nuclei, and 125 specialized builders.
Artifacts flow through the 8F pipeline: Focus, Frame, Fetch, Filter,
Format, Forge, Furnish, and Feedback.

Quality is enforced via 3-layer scoring: structural (30%), rubric (30%),
and semantic (40%). All artifacts target quality >= 9.0.

| Layer | Weight | Method |
|-------|--------|--------|
| Structural | 30% | Automated count-based checks |
| Rubric | 30% | Quality gate dimension scoring |
| Semantic | 40% | LLM evaluation (when L1+L2 >= 8.5) |
