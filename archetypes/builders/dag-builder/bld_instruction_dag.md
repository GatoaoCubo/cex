---
kind: instruction
id: bld_instruction_dag
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for dag
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Dag"
version: "1.0.0"
author: n03_builder
tags: [dag, builder, examples]
tldr: "Golden and anti-examples for dag construction, demonstrating ideal structure and common pitfalls."
domain: "dag construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Instructions: How to Produce a dag
## Phase 1: DISCOVER
1. Identify the pipeline or mission that requires dependency ordering
2. List all tasks (nodes) that make up the pipeline — assign each a unique id and descriptive label
3. Map dependencies between tasks: for each node, list which other nodes must complete before it can start
4. Verify acyclicity: trace every dependency chain and confirm no node depends on itself directly or transitively
5. Identify parallelism opportunities: find groups of nodes with no dependency between them (can execute simultaneously)
6. Assess critical path: trace the longest dependency chain and sum estimated durations
7. Check existing DAGs for overlapping pipeline scope to avoid duplicates
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write Nodes section: for each node list id, label, type, and estimated duration
5. Write Edges section: for each dependency list source node id, target node id, and dependency type
6. Write Topological Order section: compute a valid linear execution sequence respecting all edges
7. Write Parallel Groups section: list groups of nodes that can execute simultaneously in each wave
8. Write Critical Path section: list the longest dependency chain with each node's duration and total duration
9. Verify body <= 3072 bytes
10. Verify id matches `^p12_dag_[a-z][a-z0-9_]+$`
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p12_dag_`
4. Confirm kind == dag
5. Confirm graph is acyclic: no node appears as both ancestor and descendant of another node
6. Confirm every edge target exists as a node id in the Nodes section
7. Confirm topological order is valid: no node appears before its dependencies
8. Confirm body <= 3072 bytes
9. HARD gates: frontmatter valid, id pattern matches, acyclic, all edge targets are valid node ids, topological order valid
10. SOFT gates: parallel groups identified, critical path computed, score against QUALITY_GATES.md
11. Cross-check: pure static dependency structure (not a runtime execution record = workflow)? Not a routing policy (dispatch_rule)? Not a visual drawing (diagram)?
12. Revise if score < 8.0 before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify dag
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | dag construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
