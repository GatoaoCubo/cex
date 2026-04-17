---
id: p08_pat_construction_triad
kind: pattern
pillar: P08
title: Construction Triad -- Three Universal Build Patterns
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.2
tags: [pattern, construction, template-first, validate, service-mode]
tldr: Three battle-tested patterns that govern every artifact build. Template-First searches before creating. Validate-Before-Save enforces quality floor. Service-Mode enables headless operation.
density_score: 0.93
---

# Construction Triad: Three Universal Build Patterns

These three patterns emerged from 700+ build cycles. They are not optional.
Every artifact passes through all three in sequence.

## Pattern 1: Template-First Building (SP_001)

> "Never build from scratch when a precedent exists."

**Trigger**: Any artifact creation request.

| Step | Action | Gate |
|------|--------|------|
| 1 | Search existing artifacts for similar kind | Glob/index |
| 2 | Calculate similarity score against matches | >= 0.0 |
| 3 | If similarity >= 60%: ADAPT and IMPROVE the template | Never copy verbatim |
| 4 | If similarity < 60%: Build from base schema pattern | Use builder ISOs |

**Why**: Reuse compounds quality. Each adaptation inherits lessons from prior builds.
**Anti-pattern**: NIH (Not Invented Here) -- building from scratch when 80% of the work exists.

### Decision Tree

```
INTENT received
  |
  +-> Search: pool/ + examples/ + compiled/
  |     |
  |     +-> Match >= 60%: ADAPT (load, diff, improve, validate)
  |     +-> Match 30-59%: HYBRID (use structure, rewrite content)
  |     +-> Match < 30%: FRESH (load builder ISOs, build from schema)
  |
  +-> In ALL cases: run through F1-F8 pipeline
```

## Pattern 2: Validate-Before-Save (SP_002)

> "The repository is sacred. Nothing enters without proof of quality."

**Trigger**: Any save/commit/publish operation.

| Step | Action | Gate |
|------|--------|------|
| 1 | Generate artifact content via F6 | Content exists |
| 2 | Run validation checklist (all points, no shortcuts) | 12 checkpoints |
| 3 | Calculate quality score across dimensions | Numeric score |
| 4 | Score >= 8.0: SAVE with confidence | Publish-ready |
| 5 | Score 7.0-7.9: ITERATE (never save without exhausting improvements) | Max 2 retries |
| 6 | Score < 7.0: DESTROY and rebuild from scratch | No mercy |

**Why**: Quality debt compounds faster than technical debt. One bad artifact pollutes search results, templates, and downstream builds.
**Anti-pattern**: "Good enough" saves that erode the baseline.

### Score Thresholds

| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Reference example, promoted to showcase |
| 8.0-9.4 | PUBLISH | Standard quality, committed |
| 7.0-7.9 | ITERATE | Retry F6-F7 loop (max 2) |
| < 7.0 | REJECT | Delete draft, restart from F4 |

## Pattern 3: Service Mode (SP_003)

> "When called by another builder, silence is not neglect -- it is concentration."

**Trigger**: Input is structured (JSON/YAML), not conversational.

| Step | Action | Gate |
|------|--------|------|
| 1 | Detect structured input (handoff file, JSON, grid dispatch) | Format check |
| 2 | Parse and validate schema rigorously | Schema valid |
| 3 | Enter silent mode (no questions, no clarifications) | Full autonomy |
| 4 | Build artifact at SAME quality as interactive mode | Score >= 8.0 |
| 5 | Return structured response with quality proof | JSON signal |

**Why**: Grid dispatch (6 parallel builders) requires zero-interaction execution. Quality cannot degrade in headless mode.
**Anti-pattern**: Asking clarifying questions in batch mode, blocking the pipeline.

## Composition

Every build executes all three in order:

```
1. Template-First  -> Find starting point
2. [F1-F6 pipeline] -> Build the artifact
3. Validate-Before-Save -> Gate the output
4. Service-Mode (if headless) -> Signal completion
```