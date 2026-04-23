---
kind: knowledge_card
id: bld_knowledge_card_axiom
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for axiom production — immutable fundamental rules
sources: formal logic (Euclid), DDD invariants (Evans 2003), AWS tenets, 12-Factor principles
quality: 9.1
title: "Knowledge Card Axiom"
version: "1.0.0"
author: n03_builder
tags: [axiom, builder, examples]
tldr: "Golden and anti-examples for axiom construction, demonstrating ideal structure and common pitfalls."
domain: "axiom construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p01_kc_axiom
  - p10_lr_axiom-builder
  - p03_sp_axiom_builder
  - bld_collaboration_axiom
  - axiom-builder
  - tpl_axiom
  - bld_instruction_axiom
  - bld_config_axiom
  - p11_qg_axiom
  - bld_architecture_axiom
---

# Domain Knowledge: axiom
## Executive Summary
Axioms are immutable foundational truths that define system identity — if an axiom changes, the system becomes a different system. They use ALWAYS/NEVER/IF-THEN form with explicit condition, action, and consequence. Axioms differ from laws (operational, can evolve), guardrails (safety boundaries), and lifecycle rules (temporal state triggers).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P10 (memory/knowledge) |
| Max size | 3072 bytes |
| Density | >= 0.80 |
| Frontmatter fields | 20 |
| Quality gates | 8 HARD + 10 SOFT |
| Required form | ALWAYS/NEVER/IF-THEN |
| Key fields | enforcement, immutable, violations, priority |
## Patterns
- **Immutability test**: if a rule could change via config update or version bump, it is a law or policy — not an axiom
- **ALWAYS/NEVER/IF-THEN form**: "NEVER delete production data without backup" not "be careful with deletions"
- **Falsifiability**: every axiom must be testsble — if you cannot write a check that detects violation, the axiom is too vague
- **Atomicity**: one truth per axiom, no conjunctions — "X AND Y" should be two separate axioms
- **Universality within scope**: axioms hold without exception within their defined domain boundary
- **Foundation ordering**: other rules derive from axioms — axioms never derive from laws or guardrails
| Source | Concept | Application |
|--------|---------|-------------|
| Euclid's Elements | Self-evident irreducible truths | Axioms cannot be derived from other rules |
| DDD invariants (Evans) | Business rules that must always hold | Axioms are domain-scoped invariants |
| 12-Factor principles | Immutable infrastructure tenets | Violations break the system |
| AWS tenets | Decisions constraining all choices | Axioms outrank operational rules |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Vague rule ("be careful with data") | No threshold, no action, untestsble |
| Mutable axiom ("use model X") | Model choice changes; this is config |
| No consequence stated | "NEVER do X" without "because Y" lacks enforcement rationale |
| Compound axiom ("X and Y and Z") | Not atomic; split into independent axioms |
| Subjective ("quality must be high") | No measurable threshold = not falsifiable |
| Too many (>10 per domain) | Cognitive overload; some are likely laws in disguise |
## Application
1. Identify candidate: what rule NEVER changes in this domain?
2. Immutability test: would this change with a version bump? If yes → law
3. Write in ALWAYS/NEVER/IF-THEN form with explicit consequence
4. Falsifiability check: can a script detect violation?
5. Atomicity check: does it contain "and"/"or"? If yes → split
6. Validate: <= 3072 bytes, density >= 0.80, form matches pattern
## References
- Euclid's Elements: axiom as irreducible foundational truth
- Evans 2003: Domain-Driven Design — invariants and aggregates
- AWS Well-Architected: immutable architectural tenets
- 12-Factor App: principles as system-defining constraints

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_axiom]] | sibling | 0.52 |
| [[p10_lr_axiom-builder]] | downstream | 0.50 |
| [[p03_sp_axiom_builder]] | downstream | 0.49 |
| [[bld_collaboration_axiom]] | downstream | 0.44 |
| [[axiom-builder]] | downstream | 0.39 |
| [[tpl_axiom]] | downstream | 0.39 |
| [[bld_instruction_axiom]] | downstream | 0.39 |
| [[bld_config_axiom]] | downstream | 0.39 |
| [[p11_qg_axiom]] | downstream | 0.39 |
| [[bld_architecture_axiom]] | downstream | 0.37 |
