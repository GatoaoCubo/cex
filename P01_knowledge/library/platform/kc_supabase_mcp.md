---
id: p01_kc_supabase_mcp
kind: knowledge_card
type: platform
pillar: P01
title: "Supabase MCP Server — AI Agent Tools for Database Management"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.0
tags: [supabase, mcp, ai-agent, tools, schema, rls, migrations, platform]
tldr: "@supabase/mcp-server-supabase: 20+ tools para AI agents gerenciarem Supabase — list tables, execute SQL, manage RLS, deploy functions, tudo via MCP protocol"
when_to_use: "Quando conectar AI agents (Claude, Cursor, pi) ao Supabase via MCP"
keywords: [supabase-mcp, mcp-server, ai-agent-tools, model-context-protocol]
long_tails:
  - Como configurar Supabase MCP server no Claude Desktop
  - Quais tools o Supabase MCP server disponibiliza
  - Como usar MCP para criar migrations automaticamente com AI
axioms:
  - SEMPRE use service_role_key no MCP (agent precisa de acesso completo)
  - NUNCA exponha MCP server para internet — stdio only, local
  - SEMPRE revise SQL gerado pelo agent antes de aplicar em produção
linked_artifacts:
  primary: null
  related: [p01_kc_supabase_cli, p01_kc_supabase_database]
density_score: 0.88
data_source: "https://github.com/supabase/mcp-server-supabase"
---

# Supabase MCP Server

## Quick Reference
```yaml
topic: supabase_mcp_server
scope: @supabase/mcp-server-supabase, AI agent tools, MCP protocol
owner: n04_knowledge
criticality: high
package: @supabase/mcp-server-supabase (npx)
transport: stdio (local only)
```

## Configuração MCP
```json
{
  "mcpServers": {
    "supabase": {
      "command": "npx",
      "args": ["-y", "@supabase/mcp-server-supabase", "--access-token", "sbp_xxx"],
      "env": {}
    }
  }
}
```

## Tools Disponíveis
| Tool | Funcao | Categoria |
|------|--------|-----------|
| list_projects | Lista projetos da org | Project |
| get_project | Detalhes de um projeto | Project |
| get_cost | Custos do projeto | Project |
| list_tables | Lista tabelas com colunas e types | Schema |
| list_extensions | Lista extensions habilitadas | Schema |
| list_migrations | Lista migrations aplicadas | Schema |
| apply_migration | Aplica SQL migration | Schema |
| execute_sql | Executa SQL arbitrário (SELECT, DDL) | SQL |
| get_logs | Logs do projeto (API, Auth, DB) | Monitoring |
| list_edge_functions | Lista edge functions deployadas | Functions |
| create_edge_function | Cria nova edge function | Functions |
| list_secrets | Lista secrets (nomes, sem valores) | Functions |
| create_branch | Cria branch do DB | Branching |
| list_branches | Lista branches existentes | Branching |
| list_organizations | Lista organizações | Org |
| get_organization | Detalhes de uma org | Org |

## Fluxo de Uso com AI Agent
```text
[User] "cria tabela de produtos com RLS"
    → [AI Agent] chama list_tables (ver schema atual)
    → [AI Agent] gera SQL migration
    → [AI Agent] chama apply_migration (aplica)
    → [AI Agent] chama execute_sql (verifica)
    → [User] recebe confirmação + schema atualizado
```

## MCP Servers Complementares
| MCP Server | Quando Usar |
|------------|-------------|
| @supabase/mcp-server-supabase | Gestão: projetos, migrations, functions, logs |
| @anthropic/mcp-server-postgres | SQL direto, queries complexas, bulk ops |
| Combinar ambos | Cobertura total (gestão + data) |

## Capacidades do Agent com MCP
| Tarefa | Tools Usadas |
|--------|-------------|
| Criar schema completo | list_tables → apply_migration (DDL) |
| Adicionar RLS policies | execute_sql (CREATE POLICY) |
| Debug query lenta | get_logs → execute_sql (EXPLAIN ANALYZE) |
| Deploy edge function | create_edge_function |
| Criar branch para feature | create_branch → apply_migration |
| Auditar schema | list_tables → list_extensions → execute_sql |

## Segurança
| Aspecto | Recomendação |
|---------|-------------|
| Access token | Personal access token (sbp_*), não project key |
| Escopo | Token tem acesso a TODA a org — cuidado |
| Transporte | stdio (local) — nunca expor via rede |
| SQL review | SEMPRE revise SQL gerado antes de apply em prod |
| Branching | Teste migrations em branch antes de main |

## Anti-Patterns
| Anti-Pattern | Risco | Fix |
|-------------|-------|-----|
| MCP exposto via HTTP | Acesso total ao DB para internet | Manter stdio only |
| apply_migration direto em prod | Sem teste, sem rollback | Usar branch primeiro |
| Agent sem supervisão | DROP TABLE acidental | Human review obrigatório |
| Token shared entre envs | Dev acessa prod | Tokens separados por env |

## Golden Rules
- CONFIGURE MCP separado para dev e prod (tokens distintos)
- REVISE todo SQL gerado pelo agent antes de apply em produção
- USE branches para testar migrations via MCP antes de main
- COMBINE Supabase MCP (gestão) + Postgres MCP (queries) para cobertura total

## References
- Package: https://www.npmjs.com/package/@supabase/mcp-server-supabase
- GitHub: https://github.com/supabase/mcp-server-supabase
- MCP Protocol: https://modelcontextprotocol.io/
