---
kind: memory
id: bld_memory_context_file
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for context_file artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 8.9
title: "Memory: context-file-builder"
version: "1.0.0"
author: n03_builder
tags: [context_file, builder, memory, hermes_origin, workspace_instructions]
tldr: "Production lessons for context_file: scope classification mistakes, injection cost traps, inheritance pitfalls, byte budget failures."
domain: "workspace instruction auto-injection"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.91
related:
  - bld_collaboration_memory_scope
  - memory-scope-builder
  - bld_knowledge_card_context_doc
  - bld_memory_naming_rule
  - p01_kc_context_doc
  - p03_sp_engineering_nucleus
  - bld_knowledge_card_system_prompt
  - bld_config_memory_scope
  - p06_is_quality_audit
  - bld_instruction_context_doc
---

# Memory: context-file-builder

## Summary
Context files are the CEX equivalent of HERMES CLAUDE.md / AGENTS.md: ambient project-scoped
instructions that shape every agent turn without repeating in every prompt. The critical
production lesson is scope misclassification: authors default to workspace scope when nucleus
scope would be correct, polluting broader context with narrow conventions. The second lesson
is injection_point economics: every_turn is used too liberally when session_start is sufficient,
doubling token cost for stable rules that never change mid-session.

## Pattern
1. Default injection_point to session_start unless rules must apply every turn -- session_start pays once
2. Classify scope conservatively: only go as broad as the rule actually applies
3. Build inheritance_chain from actual parent IDs -- never reference non-existent IDs
4. Write child context_files as pure overrides: if rule exists in parent, do not repeat it
5. Cap nucleus scope max_bytes at 4096 and session scope at 2048 -- enforce byte discipline early
6. Tag every context_file with hermes_origin -- provenance chain must be complete

## Anti-Pattern
1. Scope too broad: repo-specific conventions put in global scope = pollutes all repos
2. every_turn injection for stable rules = 10-30x token cost for zero behavioral gain
3. Duplicating parent rules in child = drift risk when parent updates but child was not
4. Missing inheritance_chain entry = child re-specifies rules that parent already covers
5. Facts in body = knowledge_cards and context_files get confused; retrieval breaks
6. Template vars `{{var}}` in static context_file = harness injects raw var text into context
7. scope: session + injection: every_turn = most expensive combination; rare legitimate use
8. Omitting max_bytes = harness uses system default which may truncate large files silently

## Context
Context files sit at the F3 INJECT stage of 8F. They load after the agent's identity
(system_prompt at F2 BECOME) and before task execution (action_prompt). The inheritance
model means a global_context.md rule survives even if workspace or nucleus contexts are
absent -- authoring root context_files first is the most resilient strategy.

In the HERMES assimilation: CLAUDE.md = workspace context_file; AGENTS.md = nucleus/workspace
context_file focused on multi-agent coordination instructions. CEX elevates both to the same
schema with explicit scope control.

## Impact
Session_start injection vs every_turn: ~30x token cost reduction for stable rules
(tested in N03 build context injection). Scope narrowing from workspace to nucleus:
~60% reduction in context_file size (nucleus-only rules excluded from workspace).
Child-extends-parent inheritance: ~40% rule duplication reduction in multi-scope setups.

## Reproducibility
For reliable context_file production:
(1) classify scope -- use narrowest applicable
(2) select injection_point -- session_start unless compliance-critical
(3) build inheritance_chain -- list all broader-scope parents
(4) write instructions only -- no facts, no vars
(5) stay within byte budget -- narrower scope = smaller budget
(6) set quality: null -- never self-score
(7) validate against H01-H08 HARD gates

## References
1. HERMES assimilation spec: `_docs/compiled/spec_hermes_assimilation.yaml`
2. context_file schema: `archetypes/builders/context-file-builder/bld_schema_context_file.md`
3. 8F pipeline: `.claude/rules/8f-reasoning.md` (F3 INJECT is where context_file loads)

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | workspace instruction auto-injection |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_memory_scope]] | downstream | 0.26 |
| [[memory-scope-builder]] | upstream | 0.24 |
| [[bld_knowledge_card_context_doc]] | upstream | 0.23 |
| [[bld_memory_naming_rule]] | sibling | 0.21 |
| [[p01_kc_context_doc]] | upstream | 0.20 |
| [[p03_sp_engineering_nucleus]] | upstream | 0.20 |
| [[bld_knowledge_card_system_prompt]] | upstream | 0.20 |
| [[bld_config_memory_scope]] | upstream | 0.20 |
| [[p06_is_quality_audit]] | upstream | 0.19 |
| [[bld_instruction_context_doc]] | upstream | 0.19 |
