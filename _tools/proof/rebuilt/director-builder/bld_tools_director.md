---
kind: tools
id: bld_tools_director
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for director artifact production
---

# Tools: director-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing directors and crew designs in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 4 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P08_architecture/_schema.yaml | Field definitions for director |
| CEX Examples | P08_architecture/examples/ | Real director artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | P08_director seeds |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| Builder catalog | records/agents/ | Available builder ids for crew composition |
| Collaboration files | archetypes/builders/{name}/bld_collaboration_{name}.md | Builder handoff contracts |
| Crew patterns | P08_architecture/patterns/ | Reusable crew composition patterns |
## Interim Validation
No automated validator exists yet for director artifacts.
Manually check each QUALITY_GATES.md gate against produced artifact:
- [ ] YAML frontmatter parses without error
- [ ] id matches p08_dir_ prefix
- [ ] mission is non-empty
- [ ] entry_point is a valid builder id in builders list
- [ ] exit_point is a valid builder id in builders list
- [ ] dag_edges form a valid acyclic graph
- [ ] quality is null
- [ ] All 7 body sections present
