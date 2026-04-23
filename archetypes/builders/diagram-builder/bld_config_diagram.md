---
pillar: P00
id: bld_config_diagram
kind: config
builder: diagram-builder
version: 1.0.0
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Diagram"
author: n03_builder
tags: [diagram, builder, examples]
tldr: "Golden and anti-examples for diagram construction, demonstrating ideal structure and common pitfalls."
domain: "diagram construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: CONSTRAIN
related:
  - p11_qg_diagram
  - p03_sp_diagram_builder
  - bld_collaboration_diagram
  - p08_diag_{{SCOPE_SLUG}}
  - bld_instruction_diagram
  - bld_knowledge_card_diagram
  - p01_kc_diagram
  - bld_architecture_diagram
  - bld_schema_diagram
  - diagram-builder
---
# diagram-builder — CONFIG
## Naming Conventions
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p08_diag_{scope_slug}.md` | `p08_diag_agent_group_orchestration.md` |
| Builder directory | kebab-case | `diagram-builder/` |
| Frontmatter fields | snake_case | `zoom_level`, `notation` |
| Scope slug | lowercase + underscores only | `agent_group_orchestration` |
| Tags | lowercase, no spaces | `[diagram, orchestration, ascii]` |
## File Paths
| Purpose | Path |
|---------|------|
| Output | `cex/P08_architecture/examples/p08_diag_{scope_slug}.md` |
| Compiled | `cex/P08_architecture/compiled/p08_diag_{scope_slug}.yaml` |
| Builder | `cex/archetypes/builders/diagram-builder/` |
## Size Limits
| Limit | Value |
|-------|-------|
| Body max bytes | 4096 |
| Total (with frontmatter) | ~5500 bytes |
| Density minimum | 0.80 |
| tldr max chars | 160 |
## Diagram-Specific Constraints
| Constraint | Rule |
|-----------|------|
| Notation | One of [ascii, mermaid] — no mixing within a single diagram |
| ASCII characters | Use box-drawing: `┌─┐│└─┘` for boxes, `→▼←▲` for arrows |
| Mermaid | Must be valid Mermaid syntax that renders without errors |
| Components minimum | 2 labeled components required |
| Legend | Mandatory — explain all symbols and arrow types |
| Scope boundary | Explicit — state what IS and IS NOT included |
| Zoom guidance | system: 10+ components; subsystem: 3-10; component: 1-3 detailed |
## Enum Values
| Field | Valid Values |
|-------|-------------|
| notation | ascii, mermaid |
| zoom_level | system, subsystem, component |
| kind | diagram (literal, no variation) |
| pillar | P08 (literal) |
| quality | null (always) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_diagram]] | related | 0.51 |
| [[p03_sp_diagram_builder]] | related | 0.49 |
| [[bld_collaboration_diagram]] | related | 0.48 |
| [[p08_diag_{{SCOPE_SLUG}}]] | related | 0.47 |
| [[bld_instruction_diagram]] | related | 0.46 |
| [[bld_knowledge_card_diagram]] | related | 0.45 |
| [[p01_kc_diagram]] | related | 0.44 |
| [[bld_architecture_diagram]] | related | 0.44 |
| [[bld_schema_diagram]] | related | 0.42 |
| [[diagram-builder]] | related | 0.41 |
