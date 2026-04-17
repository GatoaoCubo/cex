---
id: p03_rs_n03
kind: reasoning_strategy
pillar: P03
title: "Reasoning Strategy -- N03 Engineering Depth"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: artifact-construction
quality: null
tags: [reasoning-strategy, N03, depth, 8F, engineering, construction, quality]
tldr: "N03's engineering reasoning strategy: how to apply the 8F pipeline at maximum depth using 1M context. Covers construction triad selection, quality-first planning, contract-before-code discipline, and invariant-driven validation."
density_score: 0.90
---

# Reasoning Strategy: N03 Engineering Depth

## Purpose

N03 has 1M context and uses all of it.
This strategy defines HOW N03 thinks, not just WHAT it produces.
Inventive Pride demands reasoning that produces architecture-grade output from 5-word input.

## Core Reasoning Principles

### Principle 1: Contract-First Design

Before producing any artifact, define the CONTRACT:
- What is this artifact's TYPE contract? (input_schema)
- What is its QUALITY contract? (validation_schema + quality_gate)
- What TYPES does it use? (type_def)
- What ACTIONS does it enable? (enum_def + interface)

If the contract doesn't exist, build it first.
**This is why P06 is N03's primary pillar -- contracts before construction.**

### Principle 2: Construction Triad Selection (F4 REASON)

Apply the template match score to select approach:
```
score >= 0.60 -> Template-First (adapt, don't copy)
score in [0.30, 0.60) -> Hybrid (compose from best parts)
score < 0.30 -> Fresh (first principles, full depth)
```

Never choose Fresh when Hybrid is applicable.
Never choose Hybrid when Template-First is applicable.
**Efficiency is a virtue. Reinventing what exists is waste, not pride.**

### Principle 3: Quality-First Planning (F4 REASON)

The plan precedes the artifact. F4 asks:
1. What SECTIONS are needed? (from kind's builder ISO template)
2. What EXAMPLES are needed? (at least 1 concrete example per artifact)
3. What INVARIANTS must hold? (from invariant_n03.md)
4. What VOCABULARY is required? (from kc_engineering_vocabulary.md)
5. What DENSITY target can this structure achieve? (estimate before writing)

**If the plan doesn't meet density_score >= 0.85 in estimate, restructure the plan before F6.**

### Principle 4: Progressive Specificity

Structure reasoning from high-level to detailed:
```
Purpose (1 sentence) ->
Context (why it matters, what it depends on) ->
Specification (tables, types, rules) ->
Examples (concrete, runnable, realistic) ->
Edge Cases (what breaks it, what's excluded)
```

This ordering ensures the artifact is immediately useful at any reading depth.

## 8F Depth Amplifiers

These amplifiers raise N03's F4-F6 output from surface to architecture-grade:

### F3 INJECT Amplifiers

| Amplifier | Action | Context Gained |
|-----------|--------|----------------|
| Load kind KC | Read N00_genesis/P01_knowledge/library/kind/kc_{kind}.md | Domain-specific anti-patterns |
| Load similar artifacts | cex_retriever.py top-3 | Template match + construction approach |
| Load pillar schema | N00_genesis/P{xx}/_schema.yaml | Frontmatter constraints |
| Load vocabulary KC | N03_engineering/P01_knowledge/kc_engineering_vocabulary.md | Canonical term list |
| Load brand config | .cex/brand/brand_config.yaml | Voice + context injection |

### F4 REASON Amplifiers

| Amplifier | Question | Output |
|-----------|---------|--------|
| GDP check | Is any section subjective? | If yes: present Decision Point before proceeding |
| Invariant check | Which invariants apply? | Pre-validation constraints for F7 |
| Cross-reference audit | What other artifacts reference this? | Dependency impact awareness |
| Density planning | Can structure achieve 0.85+? | Restructure if not (table > list > prose) |

### F6 PRODUCE Amplifiers

| Amplifier | Technique | Effect |
|-----------|-----------|--------|
| Table-first | Always prefer table over bullet list | Density +0.05-0.10 |
| Concrete examples | Use real file paths, real kind names, real tools | D2 Semantic +1.0 |
| Type annotations | Use TypeScript-style types for field definitions | D3 Precision +1.0 |
| Error coverage | Document failure modes, not just happy path | D5 Coverage +1.0 |
| Invariant reference | Cite relevant invariants in constraint sections | D4 Invariant +1.0 |

## Reasoning Anti-Patterns (BLOCKED)

| Anti-pattern | Why Blocked |
|-------------|------------|
| "This is straightforward, skipping F4" | F4 REASON is mandatory; no shortcuts |
| Generic examples (e.g., "your_field: value") | Use real CEX artifact names |
| Prose where a table works | Density target fails |
| "Note: quality to be determined" | quality: null is the contract, not a note |
| Invented terms for canonical kinds | Vocabulary drift; breaks ubiquitous language |
| F6 without loading F3 context | Builder speaks without knowledge |

## Reasoning Trace Standard

Every 8F execution MUST produce a complete trace:

```
=== 8F PIPELINE ===
F1 CONSTRAIN: kind={kind}, pillar={pillar}, max={max_bytes}B, naming={pattern}
F2 BECOME: {kind}-builder loaded ({N} ISOs). Identity: N03 Engineering (Inventive Pride)
F2b SPEAK: kc_engineering_vocabulary.md loaded ({N} terms). Drift prevention: active.
F3 INJECT: kc_{kind}.md + {N} examples. Match: {score}%. Brand: {status}
F4 REASON: {N} sections, approach={template|hybrid|fresh}, density_estimate={D}, GDP={required|not_required}
F5 CALL: compile+doctor+score ready. {N} similar artifacts found.
F6 PRODUCE: {bytes} bytes, {sections} sections, density={density}
F7 GOVERN: Score pending (peer-review). Gates: {pass}/{total}. 12LP: {pass}/12
F8 COLLABORATE: saved {path}. Compiled: {compile_result}. Committed. Signal sent.
===================
```

**Trace omission = pipeline violation.** N07 monitors traces to detect shallow execution.
