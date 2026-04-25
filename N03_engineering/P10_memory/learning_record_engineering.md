---
id: p10_lr_builder_genesis
kind: learning_record
8f: F7_govern
pillar: P10
title: Learning Record -- Builder Genesis Session
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [learning-record, builder, N03, genesis]
tldr: "6 genesis-session lessons: bigram regex [^a-z]->[^a-z0-9_] (94->99/99 resolution), 624 proprietary author fields cleaned, TYPE_TO_TEMPLATE sync gap, heredoc failure on complex content, missing F8 auto-index, N03 autopoiesis (builds itself)."
density_score: 0.85
related:
  - p07_bm_builder_nucleus
  - n04_knowledge_memory_index
  - p03_pt_builder_construction
  - p12_sig_builder_nucleus
  - p06_if_builder_nucleus
  - p04_fd_builder_toolkit
  - p08_ac_builder_nucleus
  - p12_dr_builder_nucleus
  - self_audit_newpc_2026_04_12
  - bld_instruction_kind
---

# Learning Record: Builder Genesis

## L01: Bigram Parser Needs Digits
The Motor regex stripped digits from words, breaking kinds like e2e_eval.
Fix: changed [^a-z] to [^a-z0-9_] in bigram/trigram resolution.
Impact: 94/99 to 99/99 kind resolution.

## L02: Proprietary Terms Leak Everywhere
624 author: fields contained agent_group names. 81 content files had company refs.
Fix: systematic grep + replace across entire repo.
Lesson: run proprietary check BEFORE any release.

## L03: TYPE_TO_TEMPLATE Must Stay in Sync
3 kinds were in kinds_meta but missing from TYPE_TO_TEMPLATE.yaml.
Fix: cex_kind_register.py --validate catches this automatically.
Lesson: always validate registries after any kind change.

## L04: Heredocs Break on Complex Content
Bash heredocs fail on content with backticks, quotes, dollar signs, or backslashes.
Fix: use Python chr(10).join() or direct Python file writes.
Lesson: never use heredocs for artifact content.

## L05: F8 Must Auto-Index
Originally F8 only saved + compiled. Missing index step meant new artifacts
were invisible to search until manual re-index.
Fix: added cex_index.py call after compile in Runner.F8.

## L06: N03 is Self-Referential
The builder nucleus builds itself. Phase 1 must be manual (genesis).
Phase 2 uses the builder to complete itself (autopoiesis).
Phase 3 rewrites originals with full context (strange loop).

## Impact Assessment

| Lesson | Files Fixed | Prevention Mechanism |
|--------|-----------|---------------------|
| L01 Bigram regex | 5 (motor parser) | Unit test in cex_system_test.py |
| L02 Proprietary terms | 624 author + 81 content | Pre-commit hook + F7 G07 gate |
| L03 Registry sync | 3 kinds | cex_kind_register.py --validate |
| L04 Heredoc failure | All builder scripts | Python file writes only |
| L05 Missing auto-index | 1 (runner.py) | F8 step now includes index call |
| L06 Autopoiesis | Architectural | N03 bootstraps via own pipeline |

## Applicability

These lessons remain load-bearing -- the regex fix, proprietary check, and registry validation
are still active enforcement mechanisms. L04 (no heredocs) is enforced by convention
since all artifact writes go through Python's file I/O, not shell scripts.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p07_bm_builder_nucleus]] | upstream | 0.28 |
| [[n04_knowledge_memory_index]] | related | 0.25 |
| [[p03_pt_builder_construction]] | upstream | 0.25 |
| [[p12_sig_builder_nucleus]] | downstream | 0.25 |
| [[p06_if_builder_nucleus]] | upstream | 0.24 |
| [[p04_fd_builder_toolkit]] | upstream | 0.23 |
| [[p08_ac_builder_nucleus]] | upstream | 0.22 |
| [[p12_dr_builder_nucleus]] | downstream | 0.22 |
| [[self_audit_newpc_2026_04_12]] | upstream | 0.21 |
| [[bld_instruction_kind]] | upstream | 0.21 |
