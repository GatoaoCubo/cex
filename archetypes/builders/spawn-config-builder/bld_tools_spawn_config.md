---
kind: tools
id: bld_tools_spawn_config
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for spawn_config production
---

# Tools: spawn-config-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing spawn_configs in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P12_orchestration/_schema.yaml | Field definitions, spawn_config kind |
| Spawn Scripts | records/framework/powershell/spawn_*.ps1 | Execution scripts (solo, grid, stop, monitor) |
| MCP Configs | .mcp-*.json | Per-agent_node MCP profiles |
| Satellite PRIMEs | records/agent_nodes/*/PRIME_*.md | Satellite routing table |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P12_spawn_config |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, mode enum valid,
flags include baseline set, timeout is reasonable.
