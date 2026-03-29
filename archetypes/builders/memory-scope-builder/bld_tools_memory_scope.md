---
kind: tools
id: bld_tools_memory_scope
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for memory_scope production
---

# Tools: memory-scope-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing memory_scope artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P02_model/_schema.yaml | Field definitions, memory_scope kind |
| CEX Examples | P02_model/examples/ | Real memory_scope artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P02_memory_scope |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, required fields present,
body <= 2048 bytes, quality == null.
