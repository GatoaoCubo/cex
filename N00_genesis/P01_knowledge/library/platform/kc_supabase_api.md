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
tldr: "PostgREST auto-generates REST API from PostgreSQL schema; pg_graphql generates GraphQL; both respect RLS and support filtering, pagination, embedding"
when_to_use: "When consuming Supabase data via REST or GraphQL in clients and servers"
keywords: [postgrest, graphql, supabase-api, filtering, pagination]
long_tails:
  - How to filter data with operators in PostgREST Supabase
  - Pagination with range headers in Supabase REST API
  - Automatic GraphQL queries in Supabase via pg_graphql
axioms:
  - ALWAYS use select() with specific columns, never select('*') in production
  - NEVER bypass RLS using service_role_key on the client-side
  - ALWAYS paginate queries with range/limit to avoid timeout
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

## Two Automatic Endpoints
| API | URL | Generated From | Auth |
|-----|-----|-----------|------|
| REST | `https://[ref].supabase.co/rest/v1/` | PostgREST reads public schema | apikey header + JWT |
| GraphQL | `https://[ref].supabase.co/graphql/v1` | pg_graphql reads public schema | apikey header + JWT |

## REST — Client SDK Patterns
```javascript
// SELECT with filters
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
  .select()  // returns the inserted row

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

## Filter Operators
| Operator | SDK | SQL Equivalent | Example |
|----------|-----|----------------|---------|
| eq | `.eq('col', val)` | `= val` | Exact status |
| neq | `.neq('col', val)` | `!= val` | Exclude status |
| gt / gte | `.gt('col', val)` | `> val` | Minimum price |
| lt / lte | `.lt('col', val)` | `< val` | Maximum price |
| like | `.like('col', '%term%')` | `LIKE` | Text search |
| ilike | `.ilike('col', '%term%')` | `ILIKE` | Case-insensitive |
| in | `.in('col', [a,b,c])` | `IN (a,b,c)` | Value list |
| is | `.is('col', null)` | `IS NULL` | Nulls |
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
| Method | How | When |
|--------|-----|------|
| Range (offset) | `.range(0, 24)` | Simple pages, <10K rows |
| Cursor | `pageInfo.endCursor` + `after:` | Infinite scroll, >10K rows |
| Keyset | `.gt('id', lastId).limit(25)` | Maximum performance |

## Performance Tips
| Tip | Impact |
|-----|--------|
| `select('id,name,price')` vs `select('*')` | 2-5x less data |
| Index on filter columns | 10-100x query speed |
| `.limit(25)` on every query | Prevents timeout |
| FK relationship | Automatic join without N+1 |

## Anti-Patterns
| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| `select('*')` without limit | Timeout, huge payload | Columns + limit |
| Filters on client instead of server | Transfers everything, filters in JS | Filters in `.from().eq()` |
| Manual N+1 queries | 100x worse performance | Use joins: `select('*, rel(*)')` |

## Golden Rules
- ALWAYS filter server-side -- never bring data to filter on client
- PAGINATE every query with `.range()` or `.limit()`
- USE automatic joins via FK -- do not make separate queries
- PREFER REST (PostgREST) for simple CRUD, GraphQL for complex queries

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
