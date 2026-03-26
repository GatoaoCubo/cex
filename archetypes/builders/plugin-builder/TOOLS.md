---
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for plugin production
---

# Tools: plugin-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing plugins to avoid duplicates | Phase 1 (research) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 (validate) | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | SCHEMA.md (this builder) | Field definitions, method/config objects |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P04_plugin |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| Existing plugins | P04_tools/examples/p04_plug_*.md | Real plugin artifacts |
| Interface patterns | CEX interface definitions | Contract references |
| Plugin architecture | Martin Fowler plugin patterns | Design guidance |

## Interim Validation
No automated validator exists yet. Check each QUALITY_GATES.md gate manually.
Key checks: YAML parses, id pattern match, kind == plugin, quality == null,
api_surface_count matches methods, lifecycle includes on_load+on_unload,
dependencies declared, isolation level set.
