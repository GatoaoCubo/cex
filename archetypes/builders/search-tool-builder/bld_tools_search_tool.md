---
kind: tools
id: bld_tools_search_tool
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for search_tool production
---

# Tools: search-tool-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing search_tool artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P04_tools/_schema.yaml | Field definitions, search_tool kind |
| CEX Examples | P04_tools/examples/ | Real search_tool artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P04_search_tool |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| Tavily Docs | tavily.com/docs | Provider reference |
| Serper Docs | serper.dev/docs | Provider reference |
| Brave Docs | brave.com/search/api | Provider reference |
| Exa Docs | exa.ai/docs | Provider reference |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, provider specified,
body <= 2048 bytes, quality == null, max_results >= 1, no API keys.
