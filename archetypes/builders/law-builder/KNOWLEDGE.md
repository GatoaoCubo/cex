---
id: law-builder-knowledge
kind: knowledge_card
pillar: P08
parent: law-builder
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [knowledge, law-builder, governance, enforcement, P08]
---

# law-builder — KNOWLEDGE

## Foundational

Operational laws descend from governance frameworks — mandatory rules that ALL participants must follow without exception. Unlike guidelines (advisory) or patterns (recommended), laws are enforced with consequences. In software engineering: database constraints (invariants the DB enforces), SLAs (mandatory service levels), RBAC policies (access rules with no bypass), RFC 2119 MUST/SHALL requirements.

In CEX: laws are inviolable operational rules that constrain ALL artifacts, agents, and processes. They differ from instructions (P03, flexible procedural guides) in that violation of a law triggers a consequence; violation of an instruction triggers a correction.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| Database constraints | Invariants that DB enforces automatically | Enforcement mechanism pattern |
| SLA/SLO (Google SRE) | Mandatory service levels with consequences | Scope + threshold + enforcement |
| RBAC policies | Access rules with no bypass path | Exception handling pattern |
| RFC 2119 (MUST/SHALL) | Requirement levels: MUST vs SHOULD | Statement clarity standard |
| OWASP Security Laws | Inviolable security mandates | Violation + consequence pattern |
| CEX Laws v3 | 11 operational laws governing multi-agent system | Domain: CEX governance |

## Key Patterns

- **IMPERATIVE**: statement as clear command using RFC 2119 keywords: MUST, SHALL, NEVER, ALWAYS
- **RATIONALE**: every law has a "why" — prevents blind obedience, enables evolution
- **ENFORCEMENT**: mechanism that detects or prevents violation (automated check, review gate, runtime guard)
- **EXCEPTIONS**: explicit list with conditions — prevents "well technically..." ambiguity
- **SCOPE**: precise boundaries (system-wide, satellite-specific, domain-specific)
- **PRIORITY**: integer 1-10; when laws conflict, higher priority resolves (10 = highest)
- **EXAMPLES**: concrete scenarios demonstrating correct law application
- **VIOLATIONS**: concrete scenarios showing law broken with consequence

## Law Anatomy

```
number: 5          <- unique integer, sequential
statement: "No artifact producer SHALL self-assign a quality score"
rationale: "Self-scoring inflates pool metrics; bias averages 20-30%"
enforcement: "H05 gate in every builder QUALITY_GATES.md rejects quality != null"
exceptions: []     <- explicit: empty list means NO exceptions
scope: system      <- system | satellite | domain
priority: 9        <- high priority, near-inviolable even in conflicts
```

## Boundary vs Nearby Types

| Type | What it is | Why NOT law |
|------|------------|-------------|
| instruction (P03) | Flexible procedural guide with steps | Instructions SUGGEST behavior; laws MANDATE it |
| guardrail (P11) | Safety boundary preventing harm | Guardrails RESTRICT (safety-focused); laws GOVERN (operational) |
| axiom (P10) | Abstract permanent truth | Axioms are PHILOSOPHICAL ("truth exists"); laws are OPERATIONAL ("MUST commit") |
| lifecycle_rule (P11) | Lifecycle transition rule | Lifecycle rules manage STATE TRANSITIONS; laws govern BEHAVIOR |
| pattern (P08) | Reusable solution with proven value | Patterns RECOMMEND adoption; laws MANDATE compliance |
| quality_gate (P11) | Pass/fail validation barrier | Gates SCORE artifacts; laws govern BEHAVIOR that gates check |
| satellite_spec (P08) | Component definition | Specs DEFINE structure; laws GOVERN operation |
| diagram (P08) | Visual representation | Diagrams VISUALIZE; laws CONSTRAIN |

## Enforcement Taxonomy

| Mechanism | Example | When to use |
|-----------|---------|-------------|
| Automated gate | YAML parser checks `quality == null` | Always preferred |
| CI/CD hook | Pre-commit rejects non-compliant files | File-level compliance |
| Runtime guard | Satellite refuses to output without signal | Behavioral compliance |
| Review gate | Human validator rejects artifact | When automation is not feasible |
| Monitoring | Alert fires when law is violated in production | Post-hoc detection |

## Scope Definitions

| Scope | Meaning | Example |
|-------|---------|---------|
| system | Applies to all actors, artifacts, satellites | "quality: null always" |
| satellite | Applies to specific satellite only | "STELLA NEVER executes tasks" |
| domain | Applies within a specific domain | "KC MUST have density >= 0.80" |

## CEX Laws Catalog (existing, for collision avoidance)

Current laws in `records/framework/docs/LAWS_v3_PRACTICAL.md`:
- Law 1-11 cover: quality threshold, pool eligibility, self-scoring, commit protocol, scope fence, signal protocol, quality provenance, naming convention, density minimum, routing mandate, terminal limit
- New laws MUST be numbered 12+ to avoid collision
- Verify uniqueness via brain_query [IF MCP] before assigning number
