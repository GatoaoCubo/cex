---
id: p04_hook_pre_commit_qa
kind: pre
trigger_event: pre_commit
script_path: records/core/python/quality_gate.py
pillar: P04
version: 1.0.0
created: 2026-03-24
author: builder_agent
quality: 9.0
tags: [hook, pre-commit, quality, scoring]
updated: "2026-04-07"
domain: "tool integration"
title: "Hook Pre Commit Qa"
density_score: 0.92
tldr: "Defines pre for hook pre commit qa, with validation gates and integration points."
---

# Hook: pre_commit_qa

## Trigger
1. Type: pre
2. Event: pre_commit (git hook)
3. Script: `python records/core/python/quality_gate.py --staged-only`

## Behavior
1. Collect staged files via `git diff --cached --name-only`
2. Score each file on 5 dimensions (syntax 3.0, structure 2.0, size 1.5, lint 2.0, completeness 1.5)
3. Block commit if weighted score < 7.0; warn if < 9.0; pass if >= 9.0

## Safety
1. Fail mode: block (score < 7.0 = exit 2, rollback recommended)
2. Idempotent: yes (read-only analysis, no file mutations)
3. Timeout: 30s
4. Escalation: >=3 consecutive fails triggers architecture review alert

## Metadata

```yaml
id: p04_hook_pre_commit_qa
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p04-hook-pre-commit-qa.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `pre` |
| Pillar | P04 |
| Domain |  |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
