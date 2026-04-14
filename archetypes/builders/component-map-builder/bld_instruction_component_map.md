---
kind: instruction
id: bld_instruction_component_map
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for component_map
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Component Map"
version: "1.0.0"
author: n03_builder
tags: [component_map, builder, examples]
tldr: "Golden and anti-examples for component map construction, demonstrating ideal structure and common pitfalls."
domain: "component map construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Instructions: How to Produce a component_map
## Phase 1: DISCOVER
1. Identify the system scope to inventory (what boundary defines "inside" vs "outside")
2. List all components within scope (services, modules, databases, queues, external APIs)
3. Map connections between components: data flow direction, dependency type, and signal type
4. Determine ownership per component (team, service, or person responsible)
5. Assess health status indicator for each component: active, deprecated, or planned
6. Check existing component_maps to avoid overlapping scope
7. Verify component count and connection count are consistent with scope
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all 19 required fields (quality: null — never self-score)
4. Write Components section: for each component list name, type, owner, health status, and description
5. Write Connections section: for each connection list source, target, protocol, and data type
6. Write Dependencies section: external services, libraries, and infrastructure the system relies on
7. Write Data Flows section: named flows with the path each takes through components
8. Write Boundaries section: explicit statement of what is inside vs outside this map's scope
9. Verify component_count in frontmatter matches actual rows in Components section
10. Verify connection_count in frontmatter matches actual rows in Connections section
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p08_cm_`
4. Confirm kind == component_map
5. Confirm components are listed with at least name and owner
6. Confirm every connection has both source and target
7. Confirm scope boundary is defined (Boundaries section present)
8. HARD gates: frontmatter valid, id pattern matches, components listed, connections have source+target, boundary defined
9. SOFT gates: no orphan components (every component has at least 1 connection), score against QUALITY_GATES.md
10. Cross-check: structured data inventory (not a visual diagram)? Covers many components (not a single-component agent_card)? Describes existing state (not prescribes future patterns)?
11. Revise if score < 8.0 before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify component
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | component map construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
