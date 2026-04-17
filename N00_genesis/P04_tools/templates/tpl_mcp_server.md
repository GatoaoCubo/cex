---
# TEMPLATE: MCP Server (P04 Tools)
# Valide contra P04_tools/_schema.yaml (types.mcp_server)
# Max 2048 bytes

id: p04_mcp_[server_slug]
name: [nome_do_servidor]
transport: [stdio|sse|http]
tools_provided: [[tool_1], [tool_2]]
resources_provided: [[resource_1], [resource_2]]
quality: 9.0
title: "Tpl Mcp Server"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for tool integration, demonstrating ideal structure and common pitfalls."
domain: "tool integration"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
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

## Debugging
<!-- INSTRUCAO: passos comuns de debug e falhas frequentes. -->

**Debug Checklist**:
1. Check logs: `~/.claude/logs/[server_slug].log`
2. Validate API key / env vars are set
3. Validate JSON config format (`.mcp.json` or `.mcp-{sat}.json`)
4. Enable verbose: `DEBUG=1 [start_command]`

**Common Failures**:
| Symptom | Cause | Fix |
|---------|-------|-----|
| Server not found | NVM path not resolved | Use absolute node path: `$(which node)` |
| Connection refused | Port conflict | `lsof -i :[PORT]` or `netstat -ano \| findstr :[PORT]` |
| Silent failure | Missing env var | Check `Required env` above, verify with `echo $VAR` |
| Timeout on start | Heavy init / missing deps | Increase timeout, check `npm ls` for missing packages |
