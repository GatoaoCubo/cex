---
id: p10_ax_shokunin_quality
kind: axiom
pillar: P10
version: "1.0.0"
created: "2026-03-28"
updated: "2026-03-28"
author: "builder_agent"
domain: "quality"
quality: 9.0
tags: [axiom, shokunin, quality, immutable]
tldr: "All artifacts must pass quality gate >= 7.0 before pool admission. No exceptions, no manual overrides."
rule: "No artifact enters the pool with quality score below 7.0"
scope: "All organization artifact kinds across all pillars"
rationale: "Quality floor prevents knowledge rot and ensures every pool artifact is reliable for downstream consumers"
enforcement: "quality_gate validator rejects artifacts scoring < 7.0; publish pipeline blocks on gate failure"
immutable: true
priority: 1
dependencies: []
keywords: [quality, gate, pool, shokunin, threshold]
linked_artifacts:
  primary: quality-gate-builder
  related: [scoring-rubric-builder, validator-builder]
density_score: 0.92
title: "Axiom Shokunin Quality"
---
## Rule Statement
No artifact enters the pool with quality score below 7.0 — the Shokunin quality floor is non-negotiable.
## Rationale
- Quality floor prevents accumulation of low-value artifacts that erode trust in pool search results
- Downstream consumers (agents, skills, agent_groups) depend on pool artifacts being production-ready
- Without enforcement, Gresham's Law applies: bad artifacts drive out good ones as noise drowns signal
## Scope
- Domain: all artifact kinds (P01-P12)
- System: pool admission pipeline, publish workflow
- Layer: validation layer between LLM production and pool storage
## Enforcement
- Detection: quality_gate validator runs HARD gates (pass/fail) + SOFT scoring (weighted sum)
- Response: score < 7.0 = REJECT with specific gate failures listed; author must fix and resubmit
## Examples
1. Agent artifact scores 8.5 on SOFT gates, all HARD gates pass -> admitted to pool
2. Knowledge card scores 9.6 -> admitted as Golden reference, used for few-shot examples
## Violations
1. Manual pool insertion bypassing quality gate
   - Impact: unreliable artifacts pollute search results, agents consume bad context
   - Resolution: remove artifact, run gate retroactively, re-admit only if >= 7.0

## Artifact Metadata

```yaml
kind: axiom
pillar: P10
pipeline: 8F
scoring: hybrid_3_layer

compilation: cex_compile
```
