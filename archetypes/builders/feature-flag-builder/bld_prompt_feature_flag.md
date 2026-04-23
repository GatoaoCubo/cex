---
kind: instruction
id: bld_instruction_feature_flag
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for feature_flag
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Feature Flag"
version: "1.0.0"
author: n03_builder
tags: [feature_flag, builder, examples]
tldr: "Golden and anti-examples for feature flag construction, demonstrating ideal structure and common pitfalls."
domain: "feature flag construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_env_config
  - bld_instruction_experiment_config
  - bld_instruction_context_doc
  - bld_instruction_chunk_strategy
  - bld_instruction_retriever_config
  - bld_instruction_memory_scope
  - bld_instruction_output_validator
  - p03_sp_feature_flag_builder
  - bld_instruction_session_backend
  - bld_instruction_trace_config
---

# Instructions: How to Produce a feature_flag
## Phase 1: RESEARCH
1. Identify the feature to flag and write a one-sentence description of what it enables or disables
2. Classify the flag type: release (controls a new feature shipping), experiment (A/B or multivariate test), ops (operational kill switch), or permission (access control by user segment)
3. Determine the initial state: on or off at the moment of creation
4. Define the rollout strategy: instant (flip to 100% at once), gradual percentage (increase over a schedule), or cohort-based (specific user segments only)
5. Identify targeting rules: which user segments, environments, or override conditions see which state
6. Define kill switch behavior: how to emergency-disable the flag, who is notified, and what the system falls back to
7. Check existing feature_flags via brain_query [IF MCP] for conflicts — two flags must not control the same code path simultaneously
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints
3. Fill all required frontmatter fields; set `quality: null` — never self-score
4. Write **Flag Definition** section: name, type, description, initial state (on/off)
5. Write **Rollout Strategy** section: method name, percentage schedule with dates, cohort definition if applicable
6. Write **Targeting Rules** section: who sees which state — segments, environments, per-user overrides
7. Write **Kill Switch** section: emergency disable procedure, notification targets, fallback behavior
8. Write **Defaults** section: value returned when the flag service is unavailable or the flag key is missing
9. Write **Lifecycle** section: creation date, expected removal date (required — flags without removal dates accumulate as technical debt), and owner
10. Confirm body <= 1536 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm `id` matches `^p09_ff_[a-z][a-z0-9_]+$`
4. Confirm `default_state` is the string "on" or "off" — no other values
5. Confirm rollout strategy is defined with a concrete method
6. Confirm kill switch behavior is documented
7. Confirm Lifecycle section includes a removal date
8. Confirm `quality` is null
9. Confirm body <= 1536 bytes
10. Cross-check: is this an on/off toggle for a specific feature? If it catalogs general runtime variables it belongs in `env_config`. If it controls user access roles it belongs in `permission`. If it specifies file system locations it belongs in `path_config`. Flags toggle discrete behaviors, they do not store configuration values.
11. If score < 8.0: revise in the same pass before outputting


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_env_config]] | sibling | 0.42 |
| [[bld_instruction_experiment_config]] | sibling | 0.40 |
| [[bld_instruction_context_doc]] | sibling | 0.38 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.38 |
| [[bld_instruction_retriever_config]] | sibling | 0.38 |
| [[bld_instruction_memory_scope]] | sibling | 0.38 |
| [[bld_instruction_output_validator]] | sibling | 0.38 |
| [[p03_sp_feature_flag_builder]] | related | 0.38 |
| [[bld_instruction_session_backend]] | sibling | 0.37 |
| [[bld_instruction_trace_config]] | sibling | 0.36 |
