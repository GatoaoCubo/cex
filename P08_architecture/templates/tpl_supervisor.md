---
id: tpl_supervisor
kind: supervisor
pillar: P08
version: 1.0.0
title: "Template — Supervisor"
tags: [template, supervisor, orchestration, crew, multi-agent]
tldr: "A supervisor coordinates a crew of builders to produce complex artifacts. Defines crew composition, task decomposition, handoff protocol, and quality aggregation."
quality: 9.0
updated: "2026-04-07"
domain: "system architecture"
author: n03_builder
created: "2026-04-07"
density_score: 0.97
---

# Supervisor: [DIRECTOR_NAME]

## Purpose
[WHAT complex task this supervisor manages — multi-artifact production, cross-pillar workflow]

## Crew Composition

| Role | Builder | Responsibility | Priority |
|------|---------|---------------|----------|
| Lead | [BUILDER_1] | [Primary artifact production] | 1 |
| Support | [BUILDER_2] | [Supplementary artifacts] | 2 |
| Reviewer | [BUILDER_3] | [Quality validation] | 3 |

## Task Decomposition
```
Complex Task → Subtask_1 (Builder_1) → Subtask_2 (Builder_2) → Merge → Review
```

| Subtask | Builder | Input | Output | Depends On |
|---------|---------|-------|--------|-----------|
| [SUBTASK_1] | [BUILDER_1] | [intent] | [artifact_1.md] | — |
| [SUBTASK_2] | [BUILDER_2] | [artifact_1] | [artifact_2.md] | SUBTASK_1 |
| [REVIEW] | [BUILDER_3] | [all artifacts] | [score, feedback] | SUBTASK_1+2 |

## Orchestration Strategy
- **Mode**: [sequential | parallel | DAG]
- **Max concurrent**: [1 | 3 | 6]
- **Timeout per subtask**: [60s | 300s]
- **On failure**: [retry | skip | abort_all]

## Quality Aggregation
Supervisor aggregates quality from all crew members:
```
Final quality = weighted_avg(subtask_scores)
  where weight = priority_inverse (lead=3, support=2, reviewer=1)
Pass threshold: all subtasks ≥ 8.0 AND aggregate ≥ 8.5
```

## Quality Gate
- [ ] Crew has ≥ 2 members (otherwise use solo builder)
- [ ] Task decomposition is explicit (DAG or sequence)
- [ ] Handoff format defined between builders
- [ ] Quality aggregation formula specified
