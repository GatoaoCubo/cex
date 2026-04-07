---
id: p01_kc_db_connector
kind: knowledge_card
type: kind
pillar: P01
title: "DB Connector — Deep Knowledge for db_connector"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: marketing_agent
domain: db_connector
quality: 9.1
tags: [db_connector, P04, CALL, kind-kc]
tldr: "Typed adapter to structured data sources (SQL, GraphQL, REST-to-DB) with pooling, retries, and schema introspection — NOT an api_client nor a retriever"
when_to_use: "Building, reviewing, or reasoning about db_connector artifacts"
keywords: [sql, database, pooling, connector]
feeds_kinds: [db_connector]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
---

# DB Connector

## Spec
```yaml
kind: db_connector
pillar: P04
llm_function: CALL
max_bytes: 1024
naming: p04_db_{{source}}.md + .yaml
core: false
```

## What It Is
A db_connector wraps structured data access (SQL, GraphQL, REST-to-DB) behind a typed interface with connection pooling, query building, and schema introspection. Its boundary is accessing structured, queryable data. It is NOT an api_client (which targets generic REST/gRPC endpoints without schema introspection), NOT a retriever (which performs embedding/keyword search over unstructured vector chunks).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | SQLDatabase, SQLDatabaseToolkit | ORM adapter; exposes as LLM tool |
| LlamaIndex | DatabaseReader, SQLDatabase | Ingests SQL rows as Document nodes |
| CrewAI | Custom SQLAlchemy tool | No native kind; user wraps psycopg2 |
| DSPy | dspy.ColBERTv2 (SQL variant) | Minimal native DB abstraction |
| Haystack | SQLDocumentStore | Stores/retrieves documents via SQL |
| OpenAI | function_def over SQL tool | No native; uses function_def schema |
| Anthropic | tool_use + psycopg2/asyncpg | No native; LLM calls user-defined tool |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| pool_size | int | 5 | Higher = throughput; lower = resource use |
| timeout_s | float | 30 | Lower = fast fail; higher = tolerant |
| ssl_mode | str | require | Disable only on trusted internal networks |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Pool-per-tenant | Isolated agent_group DBs | operations_agent gets its own pg pool |
| Read replica routing | Analytics vs write path | SELECT to replica; INSERT to primary |
| Parameterized queries | All user-facing queries | cursor.execute(sql, params) always |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Sync driver in async loop | Blocks event loop; degrades throughput | Use asyncpg or aiomysql |
| Hardcoded DSN in code | Credential exposure in git | os.environ["DATABASE_URL"] |
| No connection pool | New connection per query, high latency | SQLAlchemy pool or asyncpg Pool |

## Integration Graph
```
[raw_query / LLM tool_call] --> [db_connector] --> [structured_rows / typed_result]
                                      |
                         [connection_pool, schema_introspection]
```

## Decision Tree
- IF need vector/keyword search over chunks THEN use retriever
- IF need generic REST/GraphQL endpoint THEN use api_client
- IF need event-driven inbound THEN use webhook
- DEFAULT: db_connector for any SQL or GraphQL structured data store

## Quality Criteria
- GOOD: pooling configured, timeout set, parameterized queries only
- GREAT: async driver, schema validation, retry with exponential backoff, ssl enforced
- FAIL: no pooling, string-formatted queries, credentials hardcoded in source
