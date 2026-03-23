---
# TEMPLATE: Chain (P03 Prompt)
# Valide contra P03_prompt/_schema.yaml (types.chain)
# Max 2048 bytes

id: p03_ch_{{PIPELINE_SLUG}}
type: chain
steps: [{{STEP_1}}, {{STEP_2}}, {{STEP_3}}]
flow: {{STEP_1}} > {{STEP_2}} > {{STEP_3}}
---

# Chain: {{PIPELINE_SLUG}}

## Flow
<!-- INSTRUCAO: descrever a progressao entre prompts sem ambiguidade. -->
`{{STEP_1}} -> {{STEP_2}} -> {{STEP_3}}`

## Steps
| Step | Prompt Role | Input | Output |
|------|-------------|-------|--------|
| {{STEP_1}} | {{PAPEL_1}} | {{INPUT_1}} | {{OUTPUT_1}} |
| {{STEP_2}} | {{PAPEL_2}} | {{OUTPUT_1}} | {{OUTPUT_2}} |
| {{STEP_3}} | {{PAPEL_3}} | {{OUTPUT_2}} | {{OUTPUT_3}} |

## Control Rules
1. {{REGRA_DE_PASSAGEM_ENTRE_STEPS}}
2. {{REGRA_DE_RETRY_OU_STOP}}
3. {{REGRA_DE_VALIDACAO_FINAL}}
