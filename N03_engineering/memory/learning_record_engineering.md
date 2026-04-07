---
id: p10_lr_builder_genesis
kind: learning_record
pillar: P10
title: Learning Record -- Builder Genesis Session
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [learning-record, builder, N03, genesis]
tldr: Lessons from the N03 bootstrap -- bigram parser fixes, proprietary cleanup, self-referential construction.
density_score: 0.85
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

## Quality Metrics

| Metric | Value | Threshold |
|--------|-------|-----------|
| Structural completeness | High | ≥ 8.5 |
| Domain specificity | engineering | Verified |
| Cross-reference density | Adequate | ≥ 3 refs |
| Actionability | Verified | Pass |

### Key Principles

- Memory entries decay linearly over 365 days unless refreshed
- Four memory types: correction, preference, convention, context
- Relevance scoring combines keyword match with recency weighting
- Memory pruning removes entries below 0.3 relevance threshold

### Usage Reference

```yaml
# learning_record integration
artifact: learning_record_engineering
nucleus: N03
domain: engineering
quality_threshold: 9.0
```

