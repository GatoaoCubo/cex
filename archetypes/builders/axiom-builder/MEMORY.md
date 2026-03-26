---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: axiom-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any value)
2. Using hyphens in id slug (must be underscores: p10_ax_my_rule not p10_ax_my-rule)
3. Writing compound rule with "and" — split into two axioms instead
4. Confusing axiom with law — ask "can this EVER change?" If yes, use law-builder
5. Scope too vague ("the system") — must name concrete domain boundary
6. Including HOW-to details in body — axiom states WHAT, not HOW
7. Dependencies referencing laws or guardrails — only reference other axioms

### Axiom Domain Patterns

| Domain | Common axiom types | Key boundary |
|--------|--------------------|-------------|
| Quality | Scoring rules, validation invariants | vs quality_gate (P11) |
| Identity | System identity truths | vs mental_model (P10) |
| Architecture | Structural invariants | vs law (P08) |
| Safety | Absolute safety truths | vs guardrail (P11) |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | immutability verification, boundary with law |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing an axiom, update:
- New common mistake (if encountered)
- New domain pattern (if discovered)
- Production counter increment
