---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for pattern production
sources: GoF, POSA, enterprise integration, CEX architecture
---

# Domain Knowledge: pattern

## Foundational Concept
A pattern is a named, reusable solution to a recurring problem in a given context.
Originated by Christopher Alexander (1977) for architecture, formalized for software
by Gamma et al. (1994, "Gang of Four"). Structure: Name, Problem, Context, Forces,
Solution, Consequences. Patterns are DESCRIPTIVE (document what works), not
PRESCRIPTIVE (mandate what must happen).

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| GoF (Gamma 1994) | 23 OOP design patterns | Structure: problem, solution, consequences |
| POSA (Buschmann 1996) | Architecture-scale patterns | Scale: system-level, not class-level |
| Enterprise Integration (Hohpe 2003) | Messaging patterns | Domain: distributed agent coordination |
| Cloud Patterns (Microsoft) | Cloud architecture solutions | Context: infrastructure patterns |
| CEX Patterns | Agent orchestration solutions | Domain: multi-satellite, signal-driven |

## Key Patterns (about patterns)
- NAMED: every pattern has a concise, memorable name (2-5 words)
- RECURRING: must solve a problem that happens repeatedly
- CONTEXT-FIRST: problem and forces before solution
- FORCES: competing tensions that make simple solutions inadequate
- CONSEQUENCES: always include trade-offs (benefits AND costs)
- EXAMPLES: at least 2 concrete applications proving the pattern works
- COMPOSABLE: patterns combine with related patterns
- ANTI-PATTERNS: document what NOT to do (negative space)

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| anti_patterns | Common wrong approaches | GoF "Related Patterns" |
| applicability | When to use / when not to | GoF "Applicability" |
| forces | Tensions driving the problem | Alexander's "Forces" |
| related_patterns | Navigation between solutions | GoF "Related Patterns" |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT pattern |
|------|------------|----------------------|
| law (P08) | Inviolable rule | Laws MANDATE; patterns RECOMMEND |
| workflow (P12) | Executable step sequence | Workflows RUN; patterns DESCRIBE |
| diagram (P08) | Visual representation | Diagrams SHOW; patterns EXPLAIN |
| component_map (P08) | Structural connections | Maps INVENTORY; patterns SOLVE |
| satellite_spec (P08) | Satellite specification | Specs DEFINE one component; patterns SOLVE recurring problems |
| instruction (P03) | Procedural steps | Instructions TELL HOW; patterns EXPLAIN WHY |

## References
- Alexander, C. (1977) A Pattern Language
- Gamma et al. (1994) Design Patterns: Elements of Reusable OO Software
- Buschmann et al. (1996) Pattern-Oriented Software Architecture
- Hohpe & Woolf (2003) Enterprise Integration Patterns
