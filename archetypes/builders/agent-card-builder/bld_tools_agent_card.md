---
kind: tools
id: bld_tools_director
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for agent_card production
---

# Tools: agent-card-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing agent_cards in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P08_architecture/_schema.yaml | Field definitions for agent_card |
| CEX Examples | P08_architecture/examples/ | Real agent_card artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | P08_agent_card seeds |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| PRIME files | records/satellites/{name}/PRIME_{NAME}.md | Existing satellite definitions |
| MCP configs | .mcp-{sat}.json | Per-satellite MCP server configs |
| Spawn scripts | records/framework/powershell/spawn_*.ps1 | Boot and spawn patterns |
## Interim Validation
No automated validator exists yet for agent_cards.
Manually check each QUALITY_GATES.md gate against produced artifact:
- [ ] YAML parses without error
- [ ] id matches p08_sat_ prefix
- [ ] name is non-empty
- [ ] model is valid LLM identifier
- [ ] mcps is list
- [ ] role is non-empty
- [ ] quality is null
- [ ] All 7 body sections present
