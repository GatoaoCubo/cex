---
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for satellite_spec production
---

# Tools: satellite-spec-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing satellite_specs in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P08_architecture/_schema.yaml | Field definitions for satellite_spec |
| CEX Examples | P08_architecture/examples/ | Real satellite_spec artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | P08_satellite_spec seeds |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| PRIME files | records/satellites/{name}/PRIME_{NAME}.md | Existing satellite definitions |
| MCP configs | .mcp-{sat}.json | Per-satellite MCP server configs |
| Spawn scripts | records/framework/powershell/spawn_*.ps1 | Boot and spawn patterns |

## Interim Validation
No automated validator exists yet for satellite_specs.
Manually check each QUALITY_GATES.md gate against produced artifact:
- [ ] YAML parses without error
- [ ] id matches p08_sat_ prefix
- [ ] name is non-empty
- [ ] model is valid LLM identifier
- [ ] mcps is list
- [ ] role is non-empty
- [ ] quality is null
- [ ] All 7 body sections present
