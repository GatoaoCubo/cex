---
id: p01_kc_supabase_api
kind: knowledge_card
8f: F3_inject
type: platform
pillar: P01
title: "Supabase REST + GraphQL — PostgREST Auto-Generated API"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [supabase, postgrest, graphql, rest-api, filtering, pagination, platform]
tldr: "PostgREST gera REST API automaticamente do schema PostgreSQL; pg_graphql gera GraphQL; ambos respeitam RLS e suportam filtering, pagination, embedding"
when_to_use: "Quando consumir dados Supabase via REST ou GraphQL em clients e servers"
keywords: [postgrest, graphql, supabase-api, filtering, pagination]
long_tails:
  - Como filtrar dados com operadores no PostgREST Supabase
  - Paginacao com range headers no Supabase REST API
  - GraphQL queries automaticas no Supabase via pg_graphql
axioms:
  - SEMPRE use select() com colunas específicas, nunca select('*') em produção
  - NUNCA bypass RLS usando service_role_key no client-side
  - SEMPRE pagine queries com range/limit para evitar timeout
linked_artifacts:
  primary: null
  related: [p01_kc_supabase_database, p01_kc_supabase_auth]
density_score: 0.89
data_source: "https://supabase.com/docs/guides/api"
related:
  - bld_tools_supabase_data_layer
  - p01_kc_supabase_self_hosting
  - p01_kc_supabase_cli
  - p01_kc_supabase_database
  - p01_kc_supabase_edge_functions
  - bld_manifest_supabase_data_layer
  - bld_output_template_competitive_matrix
  - p12_mission_supabase_data_layer
  - p01_rag_source_supabase
  - bld_instruction_supabase_data_layer
---

# Supabase REST + GraphQL API

## Quick Reference
```yaml
topic: supabase_api
scope: PostgREST (REST), pg_graphql (GraphQL), filtering, pagination
owner: n04_knowledge
criticality: high
service: PostgREST (porta 3000), pg_graphql (extension)
```

## Dois Endpoints Automáticos
| API | URL | Gerado De | Auth |
|-----|-----|-----------|------|
| REST | `https://[ref].supabase.co/rest/v1/` | PostgREST lê schema public | apikey header + JWT |
| GraphQL | `https://[ref].supabase.co/graphql/v1` | pg_graphql lê schema public | apikey header + JWT |

## REST — Client SDK Patterns
```javascript
// SELECT com filtros
const { data } = await supabase
  .from('products')
  .select('id, name, price, category:categories(name)')  // join!
  .eq('status', 'active')
  .gte('price', 10)
  .order('created_at', { ascending: false })
  .range(0, 24)  // pagination: items 0-24

// INSERT
const { data } = await supabase
  .from('orders')
  .insert({ user_id: auth.uid(), total: 99.90, status: 'pending' })
  .select()  // retorna o inserido

// UPDATE
const { data } = await supabase
  .from('orders')
  .update({ status: 'shipped' })
  .eq('id', orderId)
  .select()

// DELETE
await supabase.from('orders').delete().eq('id', orderId)

// RPC (call function)
const { data } = await supabase.rpc('match_documents', {
  query_embedding: [0.1, 0.2, ...],
  match_threshold: 0.78,
  match_count: 10
})
```

## Operadores de Filtro
| Operador | SDK | SQL Equivalente | Exemplo |
|----------|-----|-----------------|---------|
| eq | `.eq('col', val)` | `= val` | Status exato |
| neq | `.neq('col', val)` | `!= val` | Excluir status |
| gt / gte | `.gt('col', val)` | `> val` | Preço mínimo |
| lt / lte | `.lt('col', val)` | `< val` | Preço máximo |
| like | `.like('col', '%term%')` | `LIKE` | Busca texto |
| ilike | `.ilike('col', '%term%')` | `ILIKE` | Case-insensitive |
| in | `.in('col', [a,b,c])` | `IN (a,b,c)` | Lista valores |
| is | `.is('col', null)` | `IS NULL` | Nulos |
| contains | `.contains('col', {k:v})` | `@>` | JSONB contains |
| overlaps | `.overlaps('col', [a,b])` | `&&` | Array overlap |
| textSearch | `.textSearch('col', 'q')` | `@@` | Full-text |

## GraphQL (pg_graphql)
```graphql
query {
  productsCollection(
    filter: { status: { eq: "active" }, price: { gte: 10 } }
    orderBy: [{ created_at: DescNullsLast }]
    first: 25
  ) {
    edges {
      node { id name price categoriesCollection { edges { node { name } } } }
    }
    pageInfo { hasNextPage endCursor }
  }
}
```

## Pagination Patterns
| Metodo | Como | Quando |
|--------|------|--------|
| Range (offset) | `.range(0, 24)` | Páginas simples, <10K rows |
| Cursor | `pageInfo.endCursor` + `after:` | Infinite scroll, >10K rows |
| Keyset | `.gt('id', lastId).limit(25)` | Performance máxima |

## Performance Tips
| Tip | Impacto |
|-----|---------|
| `select('id,name,price')` vs `select('*')` | 2-5x menos dados |
| Index nas colunas de filtro | 10-100x query speed |
| `.limit(25)` em toda query | Previne timeout |
| Relacionamento via FK | Join automático sem N+1 |

## Anti-Patterns
| Anti-Pattern | Risco | Fix |
|-------------|-------|-----|
| `select('*')` sem limit | Timeout, payload enorme | Colunas + limit |
| Filtros no client em vez do server | Transfere tudo, filtra JS | Filtros no `.from().eq()` |
| N+1 queries manuais | Performance 100x pior | Usar joins: `select('*, rel(*)')` |

## Golden Rules
- FILTRE server-side sempre — nunca traga dados para filtrar no client
- PAGINE toda query com `.range()` ou `.limit()`
- USE joins automáticos via FK — não faça queries separadas
- PREFIRA REST (PostgREST) para CRUD simples, GraphQL para queries complexas

## References
- REST: https://supabase.com/docs/guides/api
- GraphQL: https://supabase.com/docs/guides/graphql
- PostgREST: https://postgrest.org/en/stable/

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_supabase_data_layer]] | downstream | 0.32 |
| [[p01_kc_supabase_self_hosting]] | sibling | 0.30 |
| [[p01_kc_supabase_cli]] | sibling | 0.27 |
| [[p01_kc_supabase_database]] | sibling | 0.26 |
| [[p01_kc_supabase_edge_functions]] | sibling | 0.23 |
| [[bld_manifest_supabase_data_layer]] | downstream | 0.20 |
| [[bld_output_template_competitive_matrix]] | downstream | 0.20 |
| [[p12_mission_supabase_data_layer]] | downstream | 0.20 |
| [[p01_rag_source_supabase]] | related | 0.20 |
| [[bld_instruction_supabase_data_layer]] | downstream | 0.18 |
