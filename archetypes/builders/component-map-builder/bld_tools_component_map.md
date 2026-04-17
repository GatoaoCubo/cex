---
pillar: P00
id: bld_tools_component_map
kind: tools
parent: component-map-builder
version: 1.0.0
quality: 9.1
title: "Tools Component Map"
author: n03_builder
tags: [component_map, builder, examples]
tldr: "Golden and anti-examples for component map construction, demonstrating ideal structure and common pitfalls."
domain: "component map construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: CALL
---
# Tools — component-map-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query | Search existing maps | Phase 1 step 5 | CONDITIONAL [MCP] |
| validate_artifact.py | Generic validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate from seeds | Alternative to manual | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P08_architecture/_schema.yaml | Field definitions, constraints |
| CEX Taxonomy | archetypes/TAXONOMY_LAYERS.yaml | Layers, overlaps, boundaries |
| Seed Bank | archetypes/SEED_BANK.yaml | Seeds: scope, components, connections |
| Existing maps | P08_architecture/examples/ | Reference artifacts |
| CMDB (ITIL) | ITIL v4 | Configuration management patterns |
| Backstage | https://backstage.io/docs/features/software-catalog | Component catalog patterns |
## brain_query Usage [IF MCP]
```
brain_query("component map {scope_keywords}")
brain_query("p08_cmap {domain}")
brain_query("component inventory {system_name}")
```
Use to: find existing maps (avoid duplicates), find sibling agent_cards for component details, find related diagrams.
## Validation Checklist (manual until validate_artifact.py ships)
```
[ ] YAML frontmatter parses (H01)
[ ] id matches ^p08_cmap_[a-z][a-z0-9_]+$ (H02)
[ ] id == filename stem (H03)
[ ] kind == "component_map" (H04)
[ ] quality == null (H05)
[ ] 15 required fields present (H06)
[ ] tags len >= 3 (H07)
[ ] scope non-empty (H08)
[ ] component_count >= 2 (H09)
[ ] tldr <= 160 chars (S01)
[ ] connection_count >= 1 (S02)
[ ] Connections table has direction (S03)
[ ] Components table has name/role/owner/status (S04)
[ ] No orphan components (S05)
[ ] Interfaces section present (S06)
[ ] All 7 body sections present (S07)
[ ] density >= 0.80 (S08)
[ ] Dependencies with failure impact (S09)
[ ] keywords len >= 2 (S10)
```

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |
