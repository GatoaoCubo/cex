---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for mcp_server production
sources: MCP Specification (modelcontextprotocol.io), Anthropic MCP docs, real server examples
---

# Domain Knowledge: mcp_server

## Foundational Concept
MCP (Model Context Protocol) is an open standard by Anthropic for connecting LLMs to
external tools and data sources. An mcp_server EXPOSES capabilities (tools + resources)
that agents consume via a standardized protocol. Servers are providers; agents are consumers.
Three transports exist: stdio (local subprocess), SSE (server-sent events, remote),
HTTP (streamable, remote). The protocol is JSON-RPC 2.0 over the chosen transport.

## Transport Comparison

| Transport | Where | Auth | Use Case |
|-----------|-------|------|----------|
| stdio | Local process | none | Dev tools, filesystem, local CLI wrappers |
| SSE | Remote HTTP | api_key / oauth | Cloud services, shared infra, web APIs |
| http (streamable) | Remote HTTP | api_key / bearer | High-throughput, streaming results |

Rule: stdio = local only; SSE/HTTP = remote; never mix transport with auth mismatch.

## Tool Schema Pattern
MCP tools follow JSON-Schema for parameters. Each tool has:
- `name`: snake_case identifier (e.g., `search_documents`)
- `description`: one sentence, what it does and when to use it
- `inputSchema`: JSON-Schema object with `properties`, `required`, `type: object`
- Returns: unstructured text or structured JSON (tool decides)

## Resource URI Patterns

| Pattern | Example | Content |
|---------|---------|---------|
| file://{path} | file:///home/user/doc.txt | File contents |
| db://{table}/{id} | db://products/42 | Database row |
| api://{endpoint} | api://weather/current | API snapshot |
| mem://{key} | mem://session/context | In-memory state |

Resources are READ-ONLY snapshots; tools are ACTIONS. Do not confuse them.

## Auth by Transport

| Transport | Recommended Auth | How |
|-----------|-----------------|-----|
| stdio | none | Process-level trust |
| sse | api_key | `Authorization: Bearer {key}` header |
| http | api_key or oauth | Header or OAuth 2.0 flow |

## Real Server Examples

| Server | Transport | Tools | Resources |
|--------|-----------|-------|-----------|
| brain (search) | stdio | brain_query, brain_list | mem://index/status |
| firecrawl (scrape) | http | scrape_url, crawl_site | - |
| railway (deploy) | http | deploy_service, get_logs | api://services |
| filesystem | stdio | read_file, write_file, list_dir | file://{path} |
| postgres | stdio | query, describe_table | db://{table} |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT mcp_server |
|------|------------|--------------------------|
| connector | Bidirectional service integration | Does not expose MCP protocol tools |
| client | Unidirectional API consumer | Consumes, does not expose |
| plugin | Pluggable system extension | Lifecycle-based, not protocol-based |
| daemon | Persistent background process | No tool/resource exposure via MCP |
| skill | Reusable capability with phases | LLM-level abstraction, not protocol server |

## References
- MCP Specification: https://modelcontextprotocol.io/
- Anthropic MCP docs: https://docs.anthropic.com/en/docs/agents-and-tools/mcp
- JSON-RPC 2.0: https://www.jsonrpc.org/specification
- JSON Schema: https://json-schema.org/
