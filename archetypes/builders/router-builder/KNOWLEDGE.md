---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for router production
sources: CEX taxonomy, intent-based routing literature, load balancing patterns
---

# Domain Knowledge: router

## Foundational Concept
A router is a decision-making artifact that directs incoming tasks to the appropriate
destination (satellite, agent, or service) based on pattern matching, confidence scoring,
and priority rules. Unlike simple dispatch rules (keyword-destination maps), a router
applies LOGIC: confidence thresholds, load balancing, fallback routes, and escalation
policies. The CEX router (P02) is the canonical routing decision artifact.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| API Gateway routing | URL pattern to backend service | route table pattern matching |
| Load balancer rules | Traffic distribution strategies | load_balance field (round_robin, weighted, priority) |
| Intent classifiers | NLP-based task categorization | confidence_threshold for pattern matching |
| Service mesh routing | Service-to-service traffic rules | escalation and retry policies |

## Key Patterns
- Route specificity: more specific patterns take priority over generic ones
- Confidence gating: routes only activate above confidence_threshold
- Fallback chain: unmatched tasks go to fallback_route, not dropped
- Escalation: ambiguous matches (multiple routes with similar confidence) trigger escalation
- Load awareness: load_balance distributes tasks across equivalent destinations
- Stateless decisions: router evaluates each task independently, no session memory
- Pattern types: keywords (simple), regex (flexible), intent classification (advanced)

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| fallback_route | Mandatory — CEX never drops unroutable tasks | API gateway default backend |
| confidence_threshold | CEX uses soft routing, not hard keyword matching | Intent classifier threshold |
| routes_count | Integrity check: frontmatter must match body | No direct equivalent |
| load_balance | Multi-satellite systems need traffic distribution | Load balancer algorithm |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT router |
|------|------------|---------------------|
| dispatch_rule (P12) | Simple keyword-satellite map | No logic, no confidence, no fallback |
| workflow (P12) | Multi-step orchestration flow | Sequence of steps, not single decision |
| agent (P02) | Runtime identity entity | Destination of routing, not the routing logic |
| fallback_chain (P02) | Model degradation sequence | Degrades MODEL quality, not TASK destination |

## References
- CEX TAXONOMY_LAYERS.yaml — router position in runtime layer
- CEX SEED_BANK.yaml — P02_router seeds
- API gateway routing patterns: specificity-based priority
