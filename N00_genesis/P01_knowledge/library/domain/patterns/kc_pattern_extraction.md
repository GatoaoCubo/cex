---
id: p01_kc_pattern_extraction
kind: knowledge_card
type: domain
pillar: P01
title: "Pattern Extraction — Mining Reusable Patterns from Code and Conversations"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: patterns
quality: 9.1
tags: [pattern, extraction, mining, reuse, knowledge]
tldr: "Identify recurring solutions in code/conversations, abstract into reusable patterns. Input: N examples. Output: pattern template + when_to_use + anti-patterns."
when_to_use: "After completing multiple similar tasks, consolidate learnings into a reusable pattern"
keywords: [pattern-extraction, mining, abstraction, reuse, template]
density_score: 0.91
updated: "2026-04-07"
---

# Pattern Extraction

## The Process
```
OBSERVE: N similar solutions exist
ABSTRACT: Remove specifics, keep structure
NAME: Give it a memorable, searchable name
DOCUMENT: template + when + anti-patterns + examples
VALIDATE: Apply pattern to new case, verify it works
```

## Pattern Template
```markdown
# Pattern: {Name}
## Problem: {recurring situation}
## Solution: {abstracted approach}
## When to Use: {conditions}
## When NOT to Use: {counter-conditions}
## Example: {concrete application}
## Anti-Pattern: {common mistakes}
```

## CEX Application
- Builder specs ARE extracted patterns (13 templates per kind)
- KCs document domain patterns
- Auto-evolve workflow detects pattern opportunities

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_pattern_extraction`
- **Tags**: [pattern, extraction, mining, reuse, knowledge]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Quality Criteria

| Dimension | Requirement | Weight |
|-----------|------------|--------|
| Factual accuracy | Verifiable claims only | 0.25 |
| Atomicity | One concept per card | 0.20 |
| Actionability | Reader knows next steps | 0.20 |
| Density | No filler sentences | 0.20 |
| Searchability | Tags enable retrieval | 0.15 |
