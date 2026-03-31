---
kind: tools
id: bld_tools_router
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for router production
---

# Tools: router-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing routers to avoid duplicates | Phase 1 (research) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 (validate) | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | SCHEMA.md (this builder) | Field definitions, route object |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P02_router |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| Existing routers | P02_model/examples/p02_router_*.md | Real router artifacts |
| dispatch-rule-builder | archetypes/builders/dispatch-rule-builder/ | Boundary reference |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Check each QUALITY_GATES.md gate manually.
Key checks: YAML parses, id pattern match, kind == router, quality == null,
routes_count matches table rows, confidence_threshold in 0.0-1.0, fallback_route set.
