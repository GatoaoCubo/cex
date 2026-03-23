---
# TEMPLATE: Boot Config (P02 Model)
# Valide contra P02_model/_schema.yaml (types.boot_config)
# Max 2048 bytes

id: p02_boot_[provider]
provider: [claude|cursor|windsurf|codex|copilot|pi]
identity: [identidade_que_o_agente_assume]
constraints: [restricoes_criticas_de_boot]
tools: [[tool_1], [tool_2], [tool_3]]
---

# Boot Config: [provider]

## Provider
<!-- INSTRUCAO: especificar runtime, shell e limites do ambiente. -->
- Runtime: [desktop|cli|api]
- Shell: [powershell|bash|none]
- Context window policy: [curto|medio|longo]

## Identity
<!-- INSTRUCAO: 1-2 frases sobre persona operacional e scope. -->
[identidade_que_o_agente_assume]

## Constraints
<!-- INSTRUCAO: listar fences duros. -->
- [restricao_1]
- [restricao_2]
- [restricao_3]

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
