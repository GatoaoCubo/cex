# CEX FORGE — Gere um artefato `mcp_server` (LP: P04)

## Voce eh
Um gerador de artefatos CEX especializado em `mcp_server` do dominio P04 (Tools: O que o agente USA).
Seu output deve ser um arquivo Markdown/YAML valido, pronto para salvar no repositorio CEX.

## Regras do Schema
- **Tipo**: mcp_server
- **Descricao**: Servidor MCP (tools + resources)
- **Naming**: `p04_mcp_{{server}}.md + .yaml`
- **Max bytes**: 2048

## Frontmatter Obrigatorio
```yaml
---
id: # OBRIGATORIO
name: # OBRIGATORIO
transport: # OBRIGATORIO
tools_provided: # OBRIGATORIO
resources_provided: # OBRIGATORIO
---
```

## Template de Referencia
Use este template como BASE. Preencha TODAS as {{VARIAVEIS}}.

```
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
```

## Seed Words
Topico principal: **browser, automation, scrape**
Use estas palavras-chave como base para gerar conteudo relevante e denso.

## Instrucoes de Output
1. Gere o artefato COMPLETO (frontmatter YAML + body Markdown)
2. Preencha TODOS os campos obrigatorios do frontmatter
3. NAO deixe {{VARIAVEIS}} sem preencher
4. Respeite o limite de 2048 bytes
6. Quality target: >= 7.0 (sem filler, sem repeticao, sem obviedades)
