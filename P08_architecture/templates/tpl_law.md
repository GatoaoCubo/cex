---
id: "p08_law_{{NUMBER}}"
kind: law
pillar: P08
version: 1.0.0
title: Template - Law
tags: [template, law, principle, architecture, invariant]
tldr: "Architectural law: stronger than guideline, MUST be followed. Violations are bugs."
quality: null
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
- **Depends on**: [OTHER_LAW]
- **Supports**: [PROPERTY — modularity, testability]
## Quality Gate
- [ ] Statement is 1 sentence
- [ ] Enforcement method identified
- [ ] >= 1 violation example
- [ ] Rationale explains consequences
