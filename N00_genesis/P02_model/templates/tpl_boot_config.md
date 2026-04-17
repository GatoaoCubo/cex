---
# TEMPLATE: Boot Config (P02 Model)
# Valide contra P02_model/_schema.yaml (types.boot_config)
# Max 2048 bytes

id: p02_boot_[provider]
provider: [claude|cursor|windsurf|codex|copilot|pi]
identity: [identidade_que_o_agente_assume]
constraints: [restricoes_criticas_de_boot]
tools: [[tool_1], [tool_2], [tool_3]]
quality: 9.0
title: "Tpl Boot Config"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for model config, demonstrating ideal structure and common pitfalls."
domain: "model config"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Boot Config: [provider]

## Provider
<!-- INSTRUCAO: especificar runtime, shell e limites do ambiente. -->
1. Runtime: [desktop|cli|api]
2. Shell: [powershell|bash|none]
3. Context window policy: [curto|medio|longo]

## Identity
<!-- INSTRUCAO: 1-2 frases sobre persona operacional e scope. -->
[identidade_que_o_agente_assume]

## Constraints
<!-- INSTRUCAO: listar fences duros. -->
1. [restricao_1]
2. [restricao_2]
3. [restricao_3]

## Tools
<!-- INSTRUCAO: mapear ferramenta para uso permitido. -->
| Tool | Use |
|------|-----|
| [tool_1] | [quando_usar] |
| [tool_2] | [quando_usar] |
| [tool_3] | [quando_usar] |

## Boot Sequence
<!-- INSTRUCAO: 3-5 passos maximo. -->
1. [carregar_contexto]
2. [verificar_restricoes]
3. [selecionar_ferramentas]
4. [executar_primeira_acao]

## Metadata

```yaml
id: p02_boot_[provider]
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p02-boot-[provider].md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `` |
| Pillar |  |
| Domain | model config |
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
