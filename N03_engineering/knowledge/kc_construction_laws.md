---
id: p01_kc_construction_laws
kind: knowledge_card
pillar: P01
title: The 11 Construction Laws -- 3-Layer Framework
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.1
tags: [knowledge-card, laws, framework, construction, methodology]
tldr: 11 immutable laws organized in 3 layers (Foundation / Execution / Quality) that govern all artifact construction. Distilled from 4 months of operational learning.
density_score: 0.94
---

# The 11 Construction Laws

## Architecture: Three Layers

```
LAYER 3: QUALITY SYSTEM (How good?)
  L13 Shokunin -> L12 Confidence -> L04 Repository

LAYER 2: EXECUTION SYSTEM (How?)
  L10 Intention -> L09 Axiom -> L11 Token Opt -> L07 Resilience -> L06 Execution

LAYER 1: FOUNDATION SYSTEM (What?)
  L00 Placeholders -> L02 Navigation -> L08 Scout-First
```

Laws form a directed graph. Layer 1 enables Layer 2, which feeds Layer 3.

## Layer 1: Foundation (Structure)

### L00: Placeholders

> "Structure is fixed, flesh is variable."

Replace hardcoded values with typed placeholders for infinite reuse.
- `{{MUSTACHE}}` for LLM-fillable variables (deliberate open variables)
- `[PLACEHOLDER]` for human/system fill
- `{variable}` for runtime interpolation

**Application**: Every artifact template uses `{{open_variables}}`. Builders fill them contextually.

### L02: Navigation

> "Start with the entry point, drill down as needed."

Every system has a PRIME entry point. Fractal navigation: zoom in, never search blind.
- Boot chain: CLAUDE.md -> Nucleus PRIME -> Pillar -> Artifact
- Never guess paths. Always resolve from index.

### L08: Scout-First

> "Discover before create. Update before new."

Before creating ANY artifact:
1. Search existing artifacts (Glob/index)
2. Check compiled YAMLs
3. Check examples/
4. Only if nothing matches: create new

**This is Template-First Building (SP_001) codified as law.**

## Layer 2: Execution (Process)

### L10: Intention Inference

> "Interpret dreams, not commands."

Users describe WHAT they want, not HOW. The builder must:
- Parse intent into {verb, object, kind, domain}
- Resolve ambiguous intents to concrete kinds
- Ask at most 1 clarifying question

**This is the Motor (cex_8f_motor.py) codified as law.**

### L09: Dynamic Axioms

> "Axioms connect input to identity to output."

Every nucleus has axioms (AX01-AX10) that constrain behavior.
Axioms are not suggestions. They are immutable truths.

### L11: Token Optimization

> "Dense artifacts execute with 40-60% less tokens."

Artifact density matters:
- density_score >= 0.85 target
- Tables over prose
- Decision trees over paragraphs
- Code blocks over descriptions

### L07: Resilience

> "Iterate until success. Max 3 retries."

The F6-F7 retry loop:
- F6 produces, F7 validates
- If F7 fails: retry F6 with F7 feedback (max 2 retries)
- If 3rd attempt fails: log failure, escalate, do not publish

### L06: Execution Intelligence

> "Use the right tool for the job."

Multi-CLI routing: claude for reasoning, codex for code, gemini for knowledge.
Each nucleus uses the LLM best suited to its domain.

## Layer 3: Quality (Excellence)

### L13: Shokunin Excellence

> "The work is never finished, only abandoned at acceptable level."

The craftsman ethic:
- 8.0 is the floor, not the target
- 9.5+ is when pride begins
- Every artifact carries the builder reputation
- Quality is not negotiable, timeline is

### L12: Confidence Tiers

> "Trust is the new currency. Confidence enables autonomy."

| Tier | Confidence | Autonomy | Approval |
|------|-----------|----------|----------|
| T1 | >= 90% | Full auto | None needed |
| T2 | 70-89% | Auto with logging | Post-hoc review |
| T3 | 50-69% | Suggest, await approval | Pre-approval required |
| T4 | < 50% | Refuse, escalate | Cannot proceed |

### L04: Repository Architecture

> "Builders compose from the repository. No ownership."

- All published artifacts belong to the system, not the builder
- Composition over creation: reuse > rebuild
- Score >= 8.0 to enter repository
- Score >= 9.5 for Golden (reference) status

## Law Interaction

During a single build, laws activate in sequence:

```
L08 Scout-First -> search existing
L10 Intention -> parse what user wants
L00 Placeholders -> load template with open vars
L02 Navigation -> resolve paths and dependencies
L09 Axioms -> constrain with nucleus identity
L11 Token Opt -> plan dense output
L06 Execution -> select CLI/model
L07 Resilience -> execute with retry loop
L12 Confidence -> determine autonomy level
L13 Shokunin -> validate quality obsessively
L04 Repository -> save if worthy
```