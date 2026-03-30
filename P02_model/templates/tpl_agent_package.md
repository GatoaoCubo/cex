---
# TEMPLATE: ISO Package (P02 Model)
# Valide contra P02_model/_schema.yaml (types.agent_package)
# Max 4096 bytes | density_min: 0.8

id: p02_iso_[agent_name]
kind: agent_package
pillar: P02
title: [agent_package_do_agente]
tldr: [pacote_portavel_do_agente_em_uma_frase]
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
- `architecture.md`: [visao_estrutural]
- `output_template.md`: [contrato_de_saida]
- `examples.md`: [casos_reais]
- `error_handling.md`: [recuperacao]

## Optional Files
<!-- INSTRUCAO: registrar quando o tier passar de standard. -->
- `quick_start.md`: [onboarding_rapido]
- `input_schema.yaml`: [contrato_de_entrada]
- `upload_kit.md`: [material_para_instalacao]
- `upload_kit_whitelabel.md`: [variacao_white_label]

## Tier
<!-- INSTRUCAO: minimal, standard, complete ou whitelabel. -->
- Selected tier: [minimal|standard|complete|whitelabel]
- Files included: [n]

## Quality Gates
<!-- INSTRUCAO: gates objetivos do schema. -->
- `system_instruction.md` <= [4096_tokens]
- Examples >= [2]
- Density >= [0.80]
- Score >= [8.0]
- No hardcoded paths: [true]

## LP Mapping
<!-- INSTRUCAO: mostrar interseccao entre arquivos e LPs. -->
- `manifest.yaml` -> P02
- `system_instruction.md` -> P03
- `instructions.md` -> P03
- `[arquivo_extra]` -> [lp_correspondente]
