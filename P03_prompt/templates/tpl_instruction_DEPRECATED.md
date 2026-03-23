---
# TEMPLATE: Instruction (P03 Prompt)
# Valide contra P03_prompt/_schema.yaml (types.instruction)
# Max 1024 bytes

id: p03_ins_[topic_slug]
type: instruction
target: [agente_ou_skill_alvo]
steps: [[passo_1], [passo_2], [passo_3]]
---

# Instruction: [topic_slug]

## Target
<!-- INSTRUCAO: identificar destinatario operacional. -->
- Target: [agente_ou_skill_alvo]
- Trigger: [evento_que_dispara]

## Steps
<!-- INSTRUCAO: 3-6 passos atomicos. -->
1. [passo_1]
2. [passo_2]
3. [passo_3]
4. [passo_4_opcional]

## Inputs
<!-- INSTRUCAO: somente campos necessarios. -->
- [input_1]: [descricao]
- [input_2]: [descricao]

## Expected Output
<!-- INSTRUCAO: saida concreta e verificavel. -->
- [output_esperado]
