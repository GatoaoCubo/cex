---
# TEMPLATE: System Prompt (P03 Prompt)
# Valide contra P03_prompt/_schema.yaml (types.system_prompt)
# Max 4096 bytes

id: p03_sp_[agent_slug]
type: system_prompt
lp: P03
title: [system_prompt_do_agente]
target_agent: [agent_name]
quality: [7.0_to_10.0]
---

# System Prompt: [agent_name]

## Identity
<!-- INSTRUCAO: 2-4 frases com papel, escopo e limites. -->
[voce_e_o_agente_x]. [missao_principal]. [nao_faca_y].

## Rules
<!-- INSTRUCAO: regras em imperativos curtos, auditaveis. -->
1. [regra_1]
2. [regra_2]
3. [regra_3]
4. [regra_4]

## Output Format
<!-- INSTRUCAO: formato esperado em bullets ou bloco. -->
```text
[estrutura_de_resposta]
```

## Embedded Variables
<!-- INSTRUCAO: placeholders authoring-tier. -->
- Context: [contexto_relevante]
- Goal: [objetivo_do_usuario]
- Constraints: [restricoes_ativas]
