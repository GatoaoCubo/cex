---
id: "p08_law_{{NUMBER}}"
kind: invariant
pillar: P08
version: 1.0.0
title: Template - Law
tags: [template, law, principle, architecture, invariant]
tldr: "Architectural law: stronger than guideline, MUST be followed. Violations are bugs."
quality: 9.0
updated: "2026-04-07"
domain: "system architecture"
author: n03_builder
created: "2026-04-07"
density_score: 0.96
---

# Law: [NAME]

## Purpose
[WHAT this law does]
## Statement
> **[LAW — imperative, unambiguous, one sentence]**
## Rationale
[WHY — what property it preserves, what breaks if violated]
## Enforcement
| Method | Tool | When |
|--------|------|------|
| Static | [TOOL] | Every commit |
| Review | Checklist | Every PR |
| Runtime | [ASSERT] | On startup |
## Violations
| Pattern | Consequence | Fix |
|---------|------------|-----|
| [VIOLATION_1] | [BREAKS_X] | [HOW] |
| [VIOLATION_2] | [BREAKS_Y] | [HOW] |
## Relationships
1. **Depends on**: [OTHER_LAW]
2. **Supports**: [PROPERTY — modularity, testability]
## Quality Gate
1. [ ] Statement is 1 sentence
2. [ ] Enforcement method identified
3. [ ] >= 1 violation example
4. [ ] Rationale explains consequences

## Cross-References

1. **Pillar**: P08 (Architecture)
2. **Kind**: `invariant`
3. **Artifact ID**: `p08_law_{{NUMBER}}`
4. **Tags**: [template, law, principle, architecture, invariant]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P08 | Architecture domain |
| Kind `invariant` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Artifact Metadata

```yaml
kind: invariant
pillar: P08
pipeline: 8F
scoring: hybrid_3_layer
compilation: cex_compile
```
