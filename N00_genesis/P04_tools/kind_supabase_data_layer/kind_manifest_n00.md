---
id: n00_supabase_data_layer_manifest
kind: knowledge_card
8f: F3_inject
pillar: P04
nucleus: n00
title: "Supabase Data Layer -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, supabase_data_layer, p04, n00, archetype, template]
density_score: 1.0
related:
  - p01_kc_supabase_data_layer
  - bld_tools_supabase_data_layer
  - bld_schema_dataset_card
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_schema_usage_report
  - bld_schema_search_strategy
  - bld_schema_action_paradigm
  - bld_schema_sandbox_spec
  - bld_schema_kind
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A supabase_data_layer is a Supabase-specific data access layer that specifies table definitions, Row Level Security (RLS) policies, edge function integrations, and real-time subscription configurations. It gives agents typed, policy-enforced access to Supabase projects without writing raw SQL. The output is a complete data layer specification covering schema, security, and serverless function contracts.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `supabase_data_layer` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| project_ref | string | yes | Supabase project reference ID |
| tables | list | yes | Table definitions with columns, types, and RLS policies |
| edge_functions | list | no | Edge function names exposed to agent |
| realtime_enabled | boolean | no | Whether real-time subscriptions are active |

## When to use
- When building agents that use Supabase as their primary database and auth backend
- When N05 Operations configures data access for a Supabase-backed product
- When the agent needs RLS-enforced database access rather than admin-level db_connector access

## Builder
`archetypes/builders/supabase_data_layer-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind supabase_data_layer --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: sdl_cex_knowledge_store
kind: supabase_data_layer
pillar: P04
nucleus: n05
title: "CEX Knowledge Store Supabase Layer"
version: 1.0
quality: null
---
project_ref: "abcdefghijklmnop"
realtime_enabled: false
tables:
  - name: knowledge_cards
    rls_policy: "auth.uid() = owner_id"
    columns: [id, kind, pillar, content, quality, created_at]
edge_functions: [search_knowledge, index_artifact]
```

## Related kinds
- `db_connector` (P04) -- generic database connector that supabase_data_layer specializes
- `secret_config` (P09) -- configuration that stores Supabase anon key and service key
- `api_client` (P04) -- REST client for Supabase APIs not covered by the data layer
- `retriever` (P04) -- vector retriever using pgvector extension on the Supabase tables

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_supabase_data_layer]] | sibling | 0.54 |
| [[bld_tools_supabase_data_layer]] | related | 0.35 |
| [[bld_schema_dataset_card]] | downstream | 0.35 |
| [[bld_schema_reranker_config]] | downstream | 0.34 |
| [[bld_schema_integration_guide]] | downstream | 0.34 |
| [[bld_schema_usage_report]] | downstream | 0.34 |
| [[bld_schema_search_strategy]] | downstream | 0.34 |
| [[bld_schema_action_paradigm]] | downstream | 0.34 |
| [[bld_schema_sandbox_spec]] | downstream | 0.34 |
| [[bld_schema_kind]] | downstream | 0.34 |
