---
id: p01_kc_zero_touch
kind: knowledge_card
type: domain
pillar: P01
title: "Zero-Touch Operations"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: operations
quality: 9.1
tags: [zero-touch, automation, ops, autonomous, deploy]
tldr: "Operations that require zero human intervention: auto-detect → auto-diagnose → auto-fix → auto-verify. The goal of mature agent systems."
when_to_use: "Designing fully autonomous operational workflows"
keywords: [zero-touch, automation, self-service, auto-remediation]
density_score: 0.91
updated: "2026-04-07"
---

# Zero-Touch Operations

## The Spectrum
```
MANUAL → SCRIPTED → AUTOMATED → AUTONOMOUS → ZERO-TOUCH
  ↑                                                ↑
  human does everything            system does everything
```

## Requirements for Zero-Touch
1. **Detection**: System knows when something is wrong
2. **Diagnosis**: System identifies root cause
3. **Remediation**: System applies fix
4. **Verification**: System confirms fix worked
5. **Learning**: System prevents recurrence

## CEX Zero-Touch Mapping

| Operation | Detection | Remediation | Verification |
|-----------|-----------|-------------|--------------|
| Build artifact | Intent parser | 8F pipeline | Doctor + compile |
| Fix error | Auto-debug | Self-healing retry | Tests pass |
| Deploy | Auto-ship | CI/CD pipeline | Health probe |
| Recover | Auto-diagnose | Auto-rollback | Doctor green |
| Evolve | Gap detector | Auto-evolve | New KC passes |

## Key Principles

- Domain-specific knowledge must be verifiable and traceable
- Artifacts reference this card via `tags` matching
- Updates trigger re-scoring of dependent artifacts
- Card freshness tracked via `created`/`updated` timestamps
- Cross-references validated by `cex_compile.py`

## Quality Criteria

| Dimension | Requirement | Weight |
|-----------|------------|--------|
| Factual accuracy | Verifiable claims only | 0.25 |
| Atomicity | One concept per card | 0.20 |
| Actionability | Reader knows next steps | 0.20 |
| Density | No filler sentences | 0.20 |
| Searchability | Tags enable retrieval | 0.15 |
