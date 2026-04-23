---
kind: instruction
id: bld_instruction_handoff
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for handoff
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Handoff"
version: "1.0.0"
author: n03_builder
tags: [handoff, builder, examples]
tldr: "Golden and anti-examples for handoff construction, demonstrating ideal structure and common pitfalls."
domain: "handoff construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_action_prompt
  - bld_instruction_instruction
  - bld_knowledge_card_handoff
  - bld_instruction_golden_test
  - p01_kc_handoff
  - bld_collaboration_handoff
  - bld_instruction_handoff_protocol
  - bld_instruction_context_doc
  - bld_instruction_dispatch_rule
  - p03_sp_handoff_builder
---

# Instructions: How to Produce a handoff
## Phase 1: RESEARCH
1. Identify the task to delegate — what work needs to be done and what is the concrete deliverable?
2. Determine the target executor — which agent_group or agent will carry out this work?
3. Define required context — what background does the executor need to understand why this task matters?
4. Scope the deliverable — what exactly should be produced, to what quality threshold, by when?
5. Identify scope fence — which file paths and directories are allowed, and which are strictly forbidden?
6. Determine commit convention — what git add pattern and commit message format should the executor use?
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all required fields
2. Read OUTPUT_TEMPLATE.md — use exact template structure
3. Set filename as `p12_ho_{task_slug}.md`
4. Fill frontmatter: all required fields, quality: null (never self-score)
5. Write Context section: background and motivation — why this task exists and what it unblocks
6. Write Task section: clear deliverable description with acceptance criteria — specific enough for autonomous execution without clarification
7. Write Seeds section: 5 to 10 domain keywords the executor can use for context retrieval
8. Write Scope Fence section: allowed paths (SOMENTE) and forbidden paths (NAO TOQUE) as explicit lists
9. Write Commit Convention section: exact git add pattern and commit message format
10. Write Signal section: the completion notification mechanism the executor must trigger when done
11. Check body size — must stay at or below 3072 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — run all HARD gates manually
2. HARD gates:
   - [ ] id matches `p12_ho_[a-z][a-z0-9_]+`
   - [ ] kind == `handoff`
   - [ ] quality == null
   - [ ] context section present
   - [ ] task has acceptance criteria
   - [ ] scope fence has both allowed and forbidden paths
   - [ ] body <= 3072 bytes
3. SOFT gates: seeds list has 5+ keywords, commit convention specified, signal mechanism defined
4. Cross-check: delegation package not execution recipe (that is instruction)? Not a status event (that is signal)? Not a routing policy (that is dispatch_rule)? Task is clear enough for autonomous execution without back-and-forth?
5. If score < 8.0: revise in the same pass before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify handoff
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | handoff construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_action_prompt]] | sibling | 0.40 |
| [[bld_instruction_instruction]] | sibling | 0.38 |
| [[bld_knowledge_card_handoff]] | upstream | 0.38 |
| [[bld_instruction_golden_test]] | sibling | 0.38 |
| [[p01_kc_handoff]] | downstream | 0.37 |
| [[bld_collaboration_handoff]] | downstream | 0.36 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.36 |
| [[bld_instruction_context_doc]] | sibling | 0.36 |
| [[bld_instruction_dispatch_rule]] | sibling | 0.36 |
| [[p03_sp_handoff_builder]] | related | 0.35 |
