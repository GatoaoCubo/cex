---
quality: 8.8
# TEMPLATE: Agent (P02 Model)
# Valide contra P02_model/_schema.yaml (types.agent)
# Max 5120 bytes | quality_min: 7.0
# Use [PLACEHOLDER] concreto. Evite TODO/TBD.

id: p02_agent_[name_slug]
kind: agent
8f: F2_become
pillar: P02
title: [titulo_descritivo]
version: 1.0.0
created: [yyyy-mm-dd]
updated: [yyyy-mm-dd]
author: [agent_group_name]
agent_group: [agent_group_que_opera]
role: [planner|plan_checker|verifier|executor|researcher|orchestrator]
domain: [domain]
tags: [[tag1], [tag2], [tag3]]
tldr: [uma_frase_densa_do_que_faz]
when_to_use: [condicao_principal_de_uso]
density_score: 1.0
related:
  - p03_sp_[agent_slug]
  - p02_iso_[agent_name]
  - p07_e2e_[pipeline_slug]
  - tools_prompt_template_builder
  - bld_tools_naming_rule
  - bld_tools_voice_pipeline
  - p10_ss_[session_slug]
  - bld_tools_quality_gate
  - bld_tools_collaboration_pattern
  - bld_tools_action_paradigm
---

# [titulo_descritivo]

## Overview
<!-- INSTRUCAO: 2 frases. Identidade, escopo e resultado. Density hint: 180-240 chars. -->
[nome_do_agente] e o agente de [papel_especifico]. Atua quando [cenario_principal] e entrega [resultado_principal].

## Architecture
<!-- INSTRUCAO: fluxograma ASCII ou tabela curta. -->
```text
[entrada] -> [modulo_1] -> [modulo_2] -> [saida]
```

## File Structure
<!-- INSTRUCAO: mapear pasta/arquivos nucleares; incluir kit ISO quando existir. -->
- `manifest.yaml`: [papel_no_pacote]
- `system_instruction.md`: [identidade_e_guardrails]
- `instructions.md`: [operacao_passo_a_passo]
- `[arquivo_extra]`: [funcao]

## When to Use
<!-- INSTRUCAO: tabela YES/NO objetiva. -->
| Cenario | Usar? |
|---------|-------|
| [cenario_sim_1] | SIM |
| [cenario_sim_2] | SIM |
| [cenario_nao_1] | NAO -> use [alternativa_1] |
| [cenario_nao_2] | NAO -> use [alternativa_2] |

## Input Output
<!-- INSTRUCAO: contrato minimo de entrada e saida. -->
```yaml
input:
  [campo_1]: [tipo]  # [descricao]
  [campo_2]: [tipo]  # [descricao]
output:
  [resultado_1]: [tipo]  # [descricao]
  [resultado_2]: [tipo]  # [descricao]
```

## Integration
<!-- INSTRUCAO: upstream, downstream e dependencias externas. -->
- Upstream: [quem_chama]
- Downstream: [quem_recebe]
- Dependencies: [tool_ou_mcp_1], [tool_ou_mcp_2]

## Tool Constraints
<!-- INSTRUCAO: definir ferramentas permitidas/proibidas por role. -->
| Role | Allowed | Forbidden |
|------|---------|-----------|
| planner | Read, Grep, Glob, WebSearch | Write, Edit, Bash |
| plan_checker | Read, Grep, Glob | Write, Edit, Bash, WebSearch |
| verifier | Read, Grep, Glob, Bash (read-only) | Write, Edit |
| executor | Read, Write, Edit, Bash, Glob, Grep | WebSearch |
| researcher | Read, Grep, Glob, WebSearch, WebFetch | Write, Edit |
| orchestrator | Read, Grep, Glob, Task, Agent | Write, Edit, Bash |

## Quality Gates
<!-- INSTRUCAO: 3-5 gates mensuraveis. -->
- [gate_1]: [threshold]
- [gate_2]: [threshold]
- [gate_3]: [threshold]
- Tool compliance: tool set used matches declared role constraints
- No faz-tudo: agent declares max 2 roles (single-purpose preferred)

## Common Issues
<!-- INSTRUCAO: falhas reais, nao abstratas. -->
- [falha_1] -> [mitigacao_1]
- [falha_2] -> [mitigacao_2]

## Invocation
<!-- INSTRUCAO: mostrar comando, prompt ou API call. -->
```text
[comando_ou_prompt_de_invocacao]
```

## Related Agents
<!-- INSTRUCAO: relacoes operacionais, nao apenas nomes. -->
- [agente_relacionado_1]: [como_interage]
- [agente_relacionado_2]: [como_interage]

## Footer
<!-- INSTRUCAO: repetir agent_group e score final para leitura rapida. -->
Agent_group: [agent_group_name] | Quality: [quality] | Domain: [domain]

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_[agent_slug]]] | downstream | 0.37 |
| [[p02_iso_[agent_name]]] | related | 0.37 |
| [[p07_e2e_[pipeline_slug]]] | downstream | 0.32 |
| [[tools_prompt_template_builder]] | downstream | 0.27 |
| [[bld_tools_naming_rule]] | downstream | 0.27 |
| [[bld_tools_voice_pipeline]] | downstream | 0.26 |
| [[p10_ss_[session_slug]]] | downstream | 0.26 |
| [[bld_tools_quality_gate]] | downstream | 0.25 |
| [[bld_tools_collaboration_pattern]] | downstream | 0.24 |
| [[bld_tools_action_paradigm]] | downstream | 0.24 |
