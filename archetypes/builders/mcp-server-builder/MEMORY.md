---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: mcp-server-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Using hyphens in id slug (must be underscores: p04_mcp_brain_search not p04_mcp_brain-search)
2. Setting quality to a number instead of null (H05 rejects any non-null value)
3. tools_provided list not matching ## Tools section names exactly (S03 drift)
4. resources_provided list not matching ## Resources URI templates (S04 drift)
5. Selecting auth: none for SSE/HTTP transport (invalid pairing — use api_key or oauth)
6. Including implementation code in body (this is a spec, not source)
7. Writing tool descriptions without parameters or return type (S06 incomplete)
8. Exceeding 2048 bytes body limit (mcp_server is compact — tightest limit in P04)
9. Confusing mcp_server with connector (connector integrates service; mcp_server exposes via protocol)
10. Omitting resources_provided field entirely when server has no resources (use empty list `[]`)

### Effective Patterns
- Tool naming: verb_noun snake_case — `search_documents`, `read_file`, `deploy_service`
- Resource URI: `scheme://{variable}` — always use curly braces for template variables
- Transport selection: "Is this running locally?" -> stdio. "Is this a remote API?" -> http
- tools_provided mirror: write the list in frontmatter FIRST, then expand each in body
- Overview pattern: "Exposes {capability} to {consumer} via {transport} transport."
- Body budget: Overview(100B) + Tools(1200B) + Resources(400B) + Transport(200B) = ~1900B

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | id hyphens, tools_provided drift, auth/transport mismatch |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a mcp_server, update:
- New common mistake (if encountered)
- New effective pattern (if discovered)
- Production counter increment
