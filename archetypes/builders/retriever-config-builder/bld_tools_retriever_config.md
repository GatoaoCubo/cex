---
kind: tools
id: bld_tools_retriever_config
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for retriever_config production
---

# Tools: retriever-config-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing retriever_config artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P01_knowledge/_schema.yaml | Field definitions, retriever_config kind |
| CEX Examples | P01_knowledge/examples/ | Real retriever_config artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P01_retriever_config |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, required fields present,
body <= 2048 bytes, quality == null.
