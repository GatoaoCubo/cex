---
id: n00_db_connector_manifest
kind: knowledge_card
8f: F3_inject
pillar: P04
nucleus: n00
title: "DB Connector -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, db_connector, p04, n00, archetype, template]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_search_strategy
  - bld_schema_integration_guide
  - bld_schema_benchmark_suite
  - bld_schema_multimodal_prompt
  - bld_schema_voice_pipeline
  - bld_schema_sandbox_spec
  - bld_schema_action_paradigm
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A db_connector is a structured database connector that gives agents typed access to SQL databases, GraphQL APIs, and REST-to-database bridges. It encapsulates connection pooling, query parameterization, schema introspection, and result serialization so agents can read and write data without constructing raw queries. The output is a production-safe database access module with built-in injection prevention and audit logging.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `db_connector` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| db_type | string | yes | postgres, mysql, sqlite, mongodb, supabase, neo4j |
| connection_method | string | yes | env_var, secret_config, or inline (dev only) |
| allowed_operations | list | yes | read, write, schema_read (no delete by default) |
| pool_size | integer | no | Connection pool size for concurrent agent access |

## When to use
- When an agent needs to read application data, product metrics, or knowledge from a database
- When building a RAG pipeline that queries structured data alongside vector search
- When N05 Operations needs to instrument database operations for observability

## Builder
`archetypes/builders/db_connector-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind db_connector --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: dbc_postgres_analytics
kind: db_connector
pillar: P04
nucleus: n05
title: "Analytics Postgres Connector"
version: 1.0
quality: null
---
db_type: postgres
connection_method: env_var
allowed_operations: [read, schema_read]
pool_size: 5
```

## Related kinds
- `supabase_data_layer` (P04) -- Supabase-specific connector with RLS and edge functions
- `retriever` (P04) -- vector search connector that complements db_connector for RAG
- `function_def` (P04) -- LLM-callable wrapper exposing db_connector as an agent tool
- `secret_config` (P09) -- configuration that stores database credentials securely

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | downstream | 0.41 |
| [[bld_schema_usage_report]] | downstream | 0.40 |
| [[bld_schema_dataset_card]] | downstream | 0.40 |
| [[bld_schema_search_strategy]] | downstream | 0.40 |
| [[bld_schema_integration_guide]] | downstream | 0.40 |
| [[bld_schema_benchmark_suite]] | downstream | 0.39 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.39 |
| [[bld_schema_voice_pipeline]] | downstream | 0.39 |
| [[bld_schema_sandbox_spec]] | downstream | 0.39 |
| [[bld_schema_action_paradigm]] | downstream | 0.39 |
