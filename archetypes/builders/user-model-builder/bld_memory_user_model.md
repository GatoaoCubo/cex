---
id: p10_lr_user_model_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-04-18
updated: 2026-04-18
author: n03_builder
observation: "User_model artifacts built without explicit compaction_cadence_turns configuration led to unbounded Collection growth in long-running deployments. SQLite-backed peers without pgvector_enabled declaration caused silent fallback to in-memory storage in 2 test environments when SQLite file was on a network drive. Artifacts missing the 3-collection minimum (preferences, working_style, context_history) produced insufficient retrieval diversity for the pre_response_insight query to return useful grounding."
pattern: "Always declare compaction_cadence_turns explicitly (default 50). Always declare pgvector_enabled: false explicitly when not using pgvector -- silence causes ambiguity. Minimum 3 collections: preferences + working_style + context_history. Never store raw message content in user_model body -- derived facts only."
evidence: "3 deployments with missing compaction_cadence: Collections grew 10x expected size in 500+ turn sessions. 2 storage ambiguity incidents: SQLite silent-fallback lost data on restart. 4 user_model builds with < 3 collections: pre_response_insight queries returned empty results for 60% of test queries."
confidence: 0.87
outcome: SUCCESS
domain: user_model
tags: [user_model, honcho, dialectic, collections, compaction, storage, builder]
tldr: "Compaction cadence, 3-collection minimum, and explicit pgvector_enabled are load-bearing. Never store raw messages in artifact body."
impact_score: 8.5
decay_rate: 0.02
keywords: [user model, honcho, compaction, collections, storage, SQLite, pgvector, dialectic]
memory_scope: project
observation_types: [feedback, project]
quality: 8.6
title: "Memory: user-model-builder"
density_score: 0.90
llm_function: INJECT
related:
  - bld_manifest_memory_type
  - bld_config_memory_type
  - bld_tools_memory_type
  - bld_output_template_builder
  - bld_output_template_signal
  - bld_config_tagline
  - bld_tools_agent
  - p10_lr_input_schema_builder
  - p10_lr_env_config_builder
  - p10_lr_golden_test_builder
---

## Summary
The three load-bearing decisions for user_model quality are: (1) explicit compaction cadence,
(2) 3-collection minimum, and (3) unambiguous storage declaration. Skipping any of these produces
a user model that appears valid but fails silently in production.

## Pattern
**Compaction + collection diversity + storage explicitness.**

1. compaction_cadence_turns: 50 (default) -- lower for support agents (20), higher for copilots (100)
2. Minimum 3 collections: `preferences` (communication style), `working_style` (domain expertise, tool prefs), `context_history` (per-session derived insights)
3. pgvector_enabled: false MUST be explicit -- silence causes env-dependent behavior
4. Never write raw message content to artifact body -- Collections store DERIVED insights only

Retention rules:
1. messages_ttl_days: 365 (default) -- GDPR-sensitive: use 180
2. derived_facts_ttl_days: null (default) -- keep derived facts forever unless legal constraint
3. If compliance requirement: set both to explicit values, document in artifact

## Anti-Pattern
1. compaction_cadence_turns omitted -- unbounded growth, inject cost explodes after 500 turns
2. pgvector_enabled omitted -- storage behavior env-dependent, silent failures
3. Only 1-2 collections -- pre_response_insight queries return empty; no personalization
4. Raw messages in body -- user_model is a derived fact model, not a transcript store
5. Confusing user_model with entity_memory -- user_model implements dialectic loop, entity_memory does not

## Builder Context

This ISO operates within the `user-model-builder` stack, one of 300 kinds in the CEX
architecture. Each builder has 13 ISOs covering system prompt, instruction, output template,
quality gate, examples, schema, config, tools, memory, manifest, architecture, knowledge card,
and collaboration.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3 (Compose), merges them
with relevant memory from `cex_memory_select.py`, and produces artifacts that must pass the
quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Reference

```yaml
id: p10_lr_user_model_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_user_model_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | user_model |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_manifest_memory_type]] | upstream | 0.45 |
| [[bld_config_memory_type]] | upstream | 0.36 |
| [[bld_tools_memory_type]] | upstream | 0.35 |
| [[bld_output_template_builder]] | upstream | 0.34 |
| [[bld_output_template_signal]] | upstream | 0.33 |
| [[bld_config_tagline]] | upstream | 0.32 |
| [[bld_tools_agent]] | upstream | 0.32 |
| [[p10_lr_input_schema_builder]] | sibling | 0.32 |
| [[p10_lr_env_config_builder]] | sibling | 0.30 |
| [[p10_lr_golden_test_builder]] | sibling | 0.30 |
