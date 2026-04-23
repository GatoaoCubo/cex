---
kind: instruction
id: bld_instruction_supervisor
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for supervisor
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Supervisor"
version: "1.0.0"
author: n03_builder
tags: [supervisor, builder, examples]
tldr: "Golden and anti-examples for supervisor construction, demonstrating ideal structure and common pitfalls."
domain: "supervisor construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_director_builder
  - supervisor-builder
  - p11_qg_director
  - bld_knowledge_card_supervisor
  - bld_collaboration_supervisor
  - bld_architecture_supervisor
  - bld_config_supervisor
  - bld_schema_supervisor
  - p01_kc_supervisor
  - bld_instruction_agent
---

# Instructions: How to Produce a supervisor
## Phase 1: RESEARCH
1. Identify the mission or goal this supervisor coordinates — what outcome do the builders collectively produce?
2. List all builders required: name each builder, its nucleus, and what it contributes to the mission
3. Map dependencies: which builders must complete before others can start?
4. Determine dispatch_mode: sequential (safe, ordered), parallel (fast, independent), or conditional (route by task content)
5. Define signal protocol: what signal files does each builder emit on completion?
6. Identify fallback behavior per builder: retry, skip, substitute, or abort-mission
7. Search for existing directors in the same domain to avoid duplicate orchestration definitions
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — template to fill
3. Fill frontmatter: topic, builders (list), dispatch_mode, signal_check, quality: null
4. Set llm_function: ORCHESTRATE (always for directors, never override)
5. Write Identity section: 2-4 sentences on orchestration scope, domain, and coordination strategy
6. Write Builders section: list each builder with role and nucleus assignment
7. Write Wave Topology section: waves in sequence, builders per wave, signal gates between waves
8. Write Dispatch Config section: mode, timeout, fallback_per_builder
9. Write Routing section: keywords and triggers that activate this supervisor
10. Write Crew Role section: the coordination question this supervisor answers, and explicit exclusions
11. Check body <= 2048 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually
2. HARD gate: id matches `ex_director_` pattern
3. HARD gate: kind == supervisor
4. HARD gate: quality == null
5. HARD gate: builders list has >= 2 entries (a supervisor with 1 builder is pointless)
6. HARD gate: dispatch_mode is one of: sequential, parallel, conditional
7. HARD gate: llm_function == ORCHESTRATE
8. HARD gate: signal_check field is set (not blank)
9. Cross-check: does the supervisor contain ANY task execution logic? If yes, remove it — directors dispatch, not execute
10. Cross-check: is wave topology consistent with dispatch_mode? (parallel mode should not have wave dependencies)
11. Cross-check: does every builder in the list have a fallback defined?
12. If score < 8.0: revise before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify supervisor
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | supervisor construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_director_builder]] | related | 0.52 |
| [[supervisor-builder]] | upstream | 0.47 |
| [[p11_qg_director]] | downstream | 0.46 |
| [[bld_knowledge_card_supervisor]] | upstream | 0.46 |
| [[bld_collaboration_supervisor]] | downstream | 0.45 |
| [[bld_architecture_supervisor]] | downstream | 0.43 |
| [[bld_config_supervisor]] | downstream | 0.42 |
| [[bld_schema_supervisor]] | downstream | 0.41 |
| [[p01_kc_supervisor]] | downstream | 0.41 |
| [[bld_instruction_agent]] | sibling | 0.41 |
