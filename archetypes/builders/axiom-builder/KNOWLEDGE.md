---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for axiom production
sources: formal logic, system design principles, CEX architecture
---

# Domain Knowledge: axiom

## Foundational Concept
An axiom is a statement accepted as true without proof — a self-evident foundation.
In formal systems (Euclid, Peano, ZFC), axioms are irreducible starting points.
In software architecture, axioms are invariant rules that define system identity.
If an axiom changes, the system it belongs to becomes a different system.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| Mathematical axioms (Euclid) | Self-evident truths in formal systems | Irreducibility: cannot derive from other rules |
| DDD invariants (Evans 2003) | Business rules that must always hold | Scope: axiom bound to a domain |
| 12-Factor App principles | Immutable infrastructure tenets | Enforcement: violations break the system |
| AWS Architecture Tenets | Decisions constraining all choices | Priority: axioms outrank operational rules |
| CEX Laws (P08) | Operational rules (can evolve) | Boundary: law changes, axiom never does |

## Key Patterns
- FALSIFIABLE: if you cannot detect a violation, it is not an axiom
- IMMUTABLE: if it changes, it was a law or policy, not an axiom
- ATOMIC: one truth per axiom, no conjunctions ("and", "or")
- UNIVERSAL within scope: no exceptions within defined boundary
- DECLARATIVE: states WHAT is true, not HOW to implement
- FOUNDATIONAL: other rules derive from axioms, never the inverse

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| enforcement | How to detect violations | DDD invariant check |
| immutable | Boolean permanence flag | 12-Factor principle status |
| violations | Known cases that broke axiom | Invariant test cases |
| priority | Relative weight among axioms | Tenet ordering |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT axiom |
|------|------------|---------------------|
| law (P08) | Operational rule | Laws evolve with system; axioms never change |
| guardrail (P11) | Safety restriction | Guardrails restrict behavior; axioms define truth |
| lifecycle_rule (P11) | Lifecycle policy | Lifecycle manages artifact state; axioms are permanent |
| instruction (P03) | Executable steps | Instructions tell HOW; axioms state WHAT |
| learning_record (P10) | Experience captured | Learning evolves; axioms are eternal |

## References
- Euclid's Elements — axiom as foundational truth
- Domain-Driven Design (Evans 2003) — invariants and aggregates
- AWS Well-Architected Tenets — immutable design decisions
