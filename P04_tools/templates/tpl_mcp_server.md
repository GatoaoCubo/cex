---
# TEMPLATE: MCP Server (P04 Tools)
# Valide contra P04_tools/_schema.yaml (types.mcp_server)
# Max 2048 bytes

id: p04_mcp_[server_slug]
name: [nome_do_servidor]
transport: [stdio|sse|http]
tools_provided: [[tool_1], [tool_2]]
resources_provided: [[resource_1], [resource_2]]
---

# MCP Server: [nome_do_servidor]

## Name
<!-- INSTRUCAO: nome e responsabilidade do servidor. -->
- Name: [nome_do_servidor]
- Role: [responsabilidade_principal]

## Transport
<!-- INSTRUCAO: protocolo e constraints. -->
- Transport: [stdio|sse|http]
- Auth: [none|token|oauth]
- Timeout: [segundos]

## Tools Provided
<!-- INSTRUCAO: listar tools com verbo + objeto. -->
| Tool | Purpose |
|------|---------|
| [tool_1] | [o_que_faz] |
| [tool_2] | [o_que_faz] |

## Resources Provided
<!-- INSTRUCAO: recursos legiveis pelo cliente MCP. -->
| Resource | Shape |
|----------|-------|
| [resource_1] | [json|text|binary] |
| [resource_2] | [json|text|binary] |

## Integration Notes
<!-- INSTRUCAO: startup, env vars e fallback. -->
- Start command: [comando_de_boot]
- Required env: [env_1], [env_2]
- Fallback: [comportamento_em_falha]
