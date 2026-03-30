---
kind: examples
id: bld_examples_mcp_server
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of mcp_server artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: mcp-server-builder
## Golden Example
INPUT: "Create MCP server for a document search service with hybrid BM25+vector search"
OUTPUT:
```yaml
id: p04_mcp_document_search
kind: mcp_server
pillar: P04
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
name: "Document Search MCP Server"
transport: stdio
tools_provided:
  - search_documents
  - get_document
  - list_collections
resources_provided:
  - mem://index/status
  - db://collections/{name}
auth: none
description: "MCP server exposing hybrid BM25+vector search over document collections via stdio"
health_check: "python server.py --health"
rate_limit: "100 req/min"
versioning: "semver, negotiated at connect"
quality: null
tags: [mcp_server, search, documents, P04]
tldr: "Document search MCP server: 3 tools, 2 resources, stdio transport, hybrid BM25+vector"
```
## Overview
Exposes document search capabilities to agents via MCP stdio transport.
Consumed by research agents and knowledge retrieval pipelines.
## Tools
### search_documents
Search documents using hybrid BM25+vector scoring.
Parameters:
- `query` (string, required): Natural language search query
- `collection` (string, optional): Target collection name; defaults to all
- `limit` (integer, optional): Max results; default 10, max 50
Returns: List of {id, title, score, excerpt} objects
### get_document
Retrieve full document by ID.
Parameters:
- `id` (string, required): Document identifier
- `collection` (string, required): Collection containing the document
Returns: {id, title, content, metadata} object
### list_collections
List available document collections with stats.
Parameters: none
Returns: List of {name, doc_count, last_updated} objects
## Resources
### mem://index/status
Content-Type: application/json
Current index health: doc count, last rebuild timestamp, vector dimensions.
### db://collections/{name}
Content-Type: application/json
Collection metadata: schema, doc count, embedding model, index type.
## Transport & Auth
Transport: stdio (local subprocess via `python server.py`)
Auth: none (process-level trust, no network exposure)
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p04_mcp_ pattern (H02 pass)
- kind: mcp_server (H04 pass)
- 19 required+recommended fields present (H06 pass)
- body has all 4 sections: Overview, Tools, Resources, Transport & Auth (H07 pass)
- tools_provided list matches ## Tools names exactly: search_documents, get_document, list_collections (S03 pass)
- resources_provided list matches ## Resources URI templates exactly (S04 pass)
- transport: stdio with auth: none (valid pairing per KNOWLEDGE.md) (S05 pass)
- tldr: 80 chars <= 160 (S01 pass)
- tags: 4 items, includes "mcp_server" (S02 pass)
- body well under 2048 bytes (H08 pass)
- No implementation code in body (S08 pass)
## Anti-Example
INPUT: "Create MCP server for weather data"
BAD OUTPUT:
```yaml
id: weather-mcp
kind: tool_server
pillar: tools
name: Weather Server
tools: [get_weather, forecast]
auth: "yes"
quality: 9.0
tags: [weather]
```
Provides weather data to agents.
## Tools
get_weather: gets weather
forecast: gets forecast
FAILURES:
1. id: "weather-mcp" has hyphens and no `p04_mcp_` prefix -> H02 FAIL
2. kind: "tool_server" not "mcp_server" -> H04 FAIL
3. pillar: "tools" not "P04" -> H06 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. Missing fields: transport, tools_provided, resources_provided, version, created, updated, author, tldr -> H06 FAIL
6. auth: "yes" not a valid enum value (must be none/api_key/oauth/bearer) -> S05 FAIL
7. tags: only 1 item, missing "mcp_server" -> S02 FAIL
8. tools_provided field absent — SCHEMA requires it -> H06 FAIL
9. resources_provided field absent — SCHEMA requires it -> H06 FAIL
10. Body missing ## Overview, ## Resources, ## Transport & Auth sections -> H07 FAIL
