---
kind: instruction
id: bld_instruction_hook
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for hook
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Hook"
version: "1.0.0"
author: n03_builder
tags: [hook, builder, examples]
tldr: "Golden and anti-examples for hook construction, demonstrating ideal structure and common pitfalls."
domain: "hook construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_hook_builder
  - bld_instruction_hook_config
  - bld_knowledge_card_hook
  - bld_collaboration_hook
  - bld_architecture_hook
  - hook-builder
  - p11_qg_hook
  - bld_examples_hook
  - bld_knowledge_card_hook_config
  - bld_schema_hook
---

# Instructions: How to Produce a hook
## Phase 1: RESEARCH
1. Identify the system event to intercept — which event triggers this hook (tool use, session start, prompt submit, stop)?
2. Determine trigger timing — should this run before the event (pre) or after it (post)?
3. Define the script to execute — what is the script path, language, and argument signature?
4. Specify conditions for activation — does this hook run always, or only when certain event data matches a pattern?
5. Set timeout and blocking behavior — blocking hooks must be fast (at or below 10000ms); async hooks may extend to 30000ms
6. Check existing hooks for the same event — avoid registering a duplicate hook that fires on the same event and condition
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all 16 required fields
2. Read OUTPUT_TEMPLATE.md — use exact template structure
3. Fill frontmatter: all 16 required fields, quality: null (never self-score)
4. Write Event section: which system event triggers this hook, with the exact event name from the enum
5. Write Timing section: pre or post, blocking or async, with justification for the choice
6. Write Script section: script path, language, arguments, and any environment variables the script reads
7. Write Conditions section: when to activate — always, conditional on event data, or pattern match on input
8. Write Timeout section: max execution time in milliseconds, and behavior on timeout (kill, warn, or ignore)
9. Write Error Handling section: what happens on script failure — block the operation, continue silently, or retry
10. Check body size — must stay at or below 1024 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — run all HARD gates manually
2. HARD gates:
   - [ ] id matches `p04_hk_[a-z][a-z0-9_]+`
   - [ ] kind == `hook`
   - [ ] quality == null
   - [ ] trigger event specified from valid enum
   - [ ] timing (pre/post) defined
   - [ ] script path present
   - [ ] timeout > 0 and <= 30000
   - [ ] blocking hooks have timeout <= 10000
   - [ ] body <= 1024 bytes
3. SOFT gates: conditions section present, error handling defined, environment variables documented
4. Cross-check: event interception not lifecycle policy (that is lifecycle_rule)? Not a persistent process (that is daemon)? Not a system extension (that is plugin)? Script is idempotent — safe to run multiple times with same result?
5. If score < 8.0: revise in the same pass before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify hook
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | hook construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_hook_builder]] | related | 0.47 |
| [[bld_instruction_hook_config]] | sibling | 0.46 |
| [[bld_knowledge_card_hook]] | upstream | 0.46 |
| [[bld_collaboration_hook]] | downstream | 0.43 |
| [[bld_architecture_hook]] | downstream | 0.43 |
| [[hook-builder]] | downstream | 0.43 |
| [[p11_qg_hook]] | downstream | 0.41 |
| [[bld_examples_hook]] | downstream | 0.39 |
| [[bld_knowledge_card_hook_config]] | upstream | 0.38 |
| [[bld_schema_hook]] | downstream | 0.36 |
