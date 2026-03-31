---
kind: tools
id: bld_tools_mcp_server
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for mcp_server production
---

# Tools: mcp-server-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing mcp_server artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P04_tools/_schema.yaml | Field definitions, mcp_server kind |
| CEX Examples | P04_tools/examples/ | Real mcp_server artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P04_mcp_server |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| MCP Spec | https://modelcontextprotocol.io/ | Transport, tool schema, resource URIs |
| Anthropic MCP docs | https://docs.anthropic.com/en/docs/agents-and-tools/mcp | Auth, transports |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, tools_provided matches body,
resources_provided matches body, body <= 2048 bytes, quality == null.
