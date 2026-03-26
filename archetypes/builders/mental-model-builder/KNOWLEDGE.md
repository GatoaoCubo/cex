---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for mental_model (P02) production
sources: CEX schema, cognitive science, decision theory, agent design patterns
---

# Domain Knowledge: mental_model

## Foundational Concept
A mental model (P02) is a design-time cognitive blueprint that codifies how an agent
routes tasks, makes decisions, and prioritizes work. Rooted in cognitive science
(Johnson-Laird 1983) and decision theory, it provides the reasoning framework that
an agent internalizes when loaded. Unlike P10 mental_model (runtime session state),
P02 mental_model is static, versioned, and part of the agent's permanent identity.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| Johnson-Laird Mental Models | Internal representations for reasoning | routing_rules + decision_tree |
| Decision trees (CART/ID3) | If-then branching classifiers | decision_tree object |
| Expert systems rule engines | Production rules (if condition then action) | routing_rules |
| Cognitive task analysis | Domain expertise decomposition | domain_map + heuristics |
| BDI agent architecture | Beliefs, Desires, Intentions | priorities + personality |

## Key Patterns
- Routing specificity: keywords must be concrete nouns/verbs, never vague categories
- Confidence thresholds: 0.8+ for direct routing, 0.5-0.8 for tentative, <0.5 for fallback
- Decision tree depth: max 3 levels deep to avoid reasoning complexity
- Priority ordering: highest first, max 5-7 priorities (Miller's law)
- Heuristic formulation: "when X, prefer Y because Z" — actionable, not philosophical
- Domain map: explicit covers/routes_to prevents boundary drift over time
- Personality coherence: tone + verbosity + risk_tolerance must be consistent

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| routing_rules | Keyword-triggered action routing | Expert system production rules |
| domain_map.routes_to | Explicit delegation to other agents | No direct equivalent |
| personality | Behavioral traits as structured data | BDI desires |
| fallback.escalate_to | Named escalation target | Exception handling |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT mental_model (P02) |
|------|------------|----------------------------------|
| mental_model (P10) | Runtime session state (ephemeral, mutable) | P10 changes per session; P02 is permanent design |
| agent (P02) | Full identity + capabilities + iso_vectorstore | Agent is WHAT; mental_model is HOW it thinks |
| router (P02) | Task-to-satellite routing rules | Router routes tasks externally; mental_model guides internal decisions |
| system_prompt (P03) | Persona and rules for LLM | How agent speaks; not how it decides |
| decision_tree (standalone) | Generic classifier | CEX mental_model embeds decision_tree as one component |

## References
- Johnson-Laird 1983 — Mental Models
- CEX P02_model/_schema.yaml — canonical mental_model fields
- BDI architecture — Belief-Desire-Intention agent model
- TAXONOMY_LAYERS.yaml — P02/P10 overlap resolution
