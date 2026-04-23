---
kind: instruction
id: bld_instruction_diagram
pillar: P08
llm_function: REASON
purpose: Step-by-step production process for diagram
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Diagram"
version: "1.0.0"
author: n03_builder
tags: [diagram, builder, examples]
tldr: "Golden and anti-examples for diagram construction, demonstrating ideal structure and common pitfalls."
domain: "diagram construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_component_map
  - bld_instruction_input_schema
  - p03_sp_diagram_builder
  - bld_instruction_golden_test
  - p11_qg_diagram
  - bld_knowledge_card_diagram
  - bld_instruction_action_prompt
  - bld_instruction_output_validator
  - bld_instruction_instruction
  - bld_instruction_memory_scope
---

# Instructions: How to Produce a diagram
## Phase 1: DISCOVER
1. Identify the architecture scope to visualize (what system or subsystem is the subject)
2. Determine zoom level: system (entire platform), subsystem (one service group), or component (internals of one service)
3. List every component within that scope (services, stores, queues, gateways, agents)
4. Map connections between components: data flow direction, dependency edges, signal paths, and relationship labels
5. Choose notation: ASCII for portability in any viewer, Mermaid for rendered output in Markdown environments
6. Identify layers present in the scope (infrastructure, runtime, content, governance) and decide which to show
7. Check existing diagrams at the same scope level to avoid duplicating an artifact that already exists
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints
3. Fill frontmatter: all 15 required fields + 4 extended fields (null is acceptable for optional fields)
4. Set `quality: null` — never assign a numeric score at authoring time
5. Write **Scope** section: what is visualized, where the boundary is, what is explicitly excluded
6. Write **Components** section: labeled boxes or nodes, one line of description per component
7. Write **Connections** section: labeled arrows showing the relationship type and direction
8. Write **Diagram** section: the actual ASCII art or Mermaid code block — must contain visual characters, not prose
9. Write **Legend** section: every symbol, box style, and arrow type explained
10. Write **Annotations** section: non-obvious design decisions that cannot be read from the diagram alone
11. Verify diagram body contains actual visual characters (pipes, dashes, arrows, Mermaid syntax) not descriptive text
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually — no automated validator
2. HARD gates: YAML parses, `id` matches `^p08_diag_[a-z][a-z0-9_]+$`, `kind` is the literal string `diagram`, `quality` is null, all 15 required fields present, notation field specified, Diagram section contains actual visual characters
3. SOFT gates: score each S01–S10 from QUALITY_GATES.md against the artifact
4. Cross-check: is this purely a visual representation? If it reads as a structured inventory, it belongs in `component_map`. If it prescribes a process, it belongs in a `pattern`. Diagrams show, they do not list or instruct.
5. If score < 8.0: revise in the same pass before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify diagram
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P08 |
| Domain | diagram construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_component_map]] | sibling | 0.47 |
| [[bld_instruction_input_schema]] | sibling | 0.40 |
| [[p03_sp_diagram_builder]] | upstream | 0.39 |
| [[bld_instruction_golden_test]] | sibling | 0.39 |
| [[p11_qg_diagram]] | downstream | 0.39 |
| [[bld_knowledge_card_diagram]] | upstream | 0.39 |
| [[bld_instruction_action_prompt]] | sibling | 0.38 |
| [[bld_instruction_output_validator]] | sibling | 0.37 |
| [[bld_instruction_instruction]] | sibling | 0.37 |
| [[bld_instruction_memory_scope]] | sibling | 0.36 |
