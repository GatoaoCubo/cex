---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for lens production
sources: [domain-driven design, aspect-oriented analysis, CEX content layer]
---

# Domain Knowledge: lens

## Foundational Concept
Lenses are analytical perspectives applied to artifacts to filter, emphasize, or
re-interpret information. Rooted in aspect-oriented analysis and domain-driven design
bounded contexts. In CEX, lenses sit in the content layer of P02 — they define
HOW to look at artifacts, not WHAT the artifacts are.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| DDD Bounded Contexts | Scoped interpretation of domain models | scope + applies_to fields |
| Aspect-Oriented Programming | Cross-cutting concerns as separable aspects | filters + focus fields |
| Data visualization filters | Attribute selection for visual emphasis | filters list |
| Multi-criteria decision analysis | Weighted perspectives for evaluation | weight + priority fields |
| Wardley Maps value chain | Positional analysis through evolution lens | bias + interpretation fields |

## Key Patterns
- Lenses are DECLARATIVE: they state what to emphasize, not how to execute
- Each lens has ONE focus (not a collection of unrelated filters)
- Bias is EXPLICIT: declared upfront, never hidden
- applies_to is SCOPED: specific artifact kinds, not "everything"
- Filters are CONCRETE: named attributes, not abstract categories
- Weight enables COMPOSITION: multiple lenses can be combined
- Limitations are MANDATORY: every perspective has blind spots

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| applies_to | Scopes lens to specific artifact kinds | DDD bounded context |
| bias | Explicit directional preference | MCDA criteria weighting |
| weight | Multi-lens composition support | Ensemble methods |
| priority | Lens ordering in pipelines | AOP advice ordering |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT lens |
|------|------------|-------------------|
| agent (P02) | Entity with capabilities and tools | Agents ACT; lenses FILTER |
| mental_model (P02) | Routing/decision map for an agent | mental_model ROUTES; lens INTERPRETS |
| model_card (P02) | LLM specification (pricing, context) | model_card DESCRIBES a model; lens VIEWS artifacts |
| scoring_rubric (P07) | Evaluation criteria with scores | rubric SCORES; lens FILTERS without scoring |
| context_doc (P01) | Domain background for hydration | context_doc PROVIDES background; lens APPLIES perspective |

## References
- Evans, Eric. Domain-Driven Design (2003) — Bounded Contexts
- Kiczales et al. Aspect-Oriented Programming (1997) — Cross-cutting concerns
- Belton & Stewart. Multiple Criteria Decision Analysis (2002) — Weighted perspectives
