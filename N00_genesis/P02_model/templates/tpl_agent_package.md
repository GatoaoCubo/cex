---
# TEMPLATE: ISO Package (P02 Model)
# Valide contra P02_model/_schema.yaml (types.agent_package)
# Max 4096 bytes | density_min: 0.8

id: p02_iso_[agent_name]
kind: agent_package
8f: F2_become
pillar: P02
title: [agent_package_do_agente]
tldr: [pacote_portavel_do_agente_em_uma_frase]
quality: 9.1
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
domain: "model config"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_agent_package
  - p02_iso_organization_agent
  - bld_schema_agent_package
  - bld_output_template_agent_package
  - bld_examples_agent_package
  - bld_knowledge_card_agent_package
  - bld_config_agent_package
  - p01_kc_agent_package
  - p02_agent_[name_slug]
  - p03_sp_agent_package_builder
---

# ISO Package: [agent_name]

## Required Files
<!-- INSTRUCAO: mapear os 3 obrigatorios com funcao exata. -->
| File | Purpose |
|------|---------|
| `manifest.yaml` | [metadados_e_manifesto_do_pacote] |
| `system_instruction.md` | [identidade_regras_guardrails] |
| `instructions.md` | [procedimento_operacional] |

## Recommended Files
<!-- INSTRUCAO: incluir apenas se agregarem reuso. -->
1. `architecture.md`: [visao_estrutural]
2. `output_template.md`: [contrato_de_saida]
3. `examples.md`: [casos_reais]
4. `error_handling.md`: [recuperacao]

## Optional Files
<!-- INSTRUCAO: registrar quando o tier passar de standard. -->
1. `quick_start.md`: [onboarding_rapido]
2. `input_schema.yaml`: [contrato_de_entrada]
3. `upload_kit.md`: [material_para_instalacao]
4. `upload_kit_whitelabel.md`: [variacao_white_label]

## Tier
<!-- INSTRUCAO: minimal, standard, complete ou whitelabel. -->
1. Selected tier: [minimal|standard|complete|whitelabel]
2. Files included: [n]

## Quality Gates
<!-- INSTRUCAO: gates objetivos do schema. -->
1. `system_instruction.md` <= [4096_tokens]
2. Examples >= [2]
3. Density >= [0.80]
4. Score >= [8.0]
5. No hardcoded paths: [true]

## LP Mapping
<!-- INSTRUCAO: mostrar interseccao entre arquivos e LPs. -->
1. `manifest.yaml` -> P02
2. `system_instruction.md` -> P03
3. `instructions.md` -> P03
4. `[arquivo_extra]` -> [lp_correspondente]

## Metadata

```yaml
id: p02_iso_[agent_name]
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p02-iso-[agent-name].md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `agent_package` |
| Pillar | P02 |
| Domain | model config |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_agent_package]] | downstream | 0.50 |
| [[p02_iso_organization_agent]] | sibling | 0.41 |
| [[bld_schema_agent_package]] | downstream | 0.39 |
| [[bld_output_template_agent_package]] | downstream | 0.38 |
| [[bld_examples_agent_package]] | downstream | 0.37 |
| [[bld_knowledge_card_agent_package]] | upstream | 0.36 |
| [[bld_config_agent_package]] | downstream | 0.36 |
| [[p01_kc_agent_package]] | related | 0.34 |
| [[p02_agent_[name_slug]]] | related | 0.33 |
| [[p03_sp_agent_package_builder]] | downstream | 0.31 |
