---
id: p01_kc_pattern
kind: knowledge_card
type: kind
pillar: P08
title: "Pattern — Deep Knowledge for pattern"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: commercial_agent
domain: pattern
quality: 9.1
tags: [pattern, P08, INJECT, kind-kc]
tldr: "pattern is a reusable architectural solution to a recurring problem — encoding intent, forces, structure, and explicit when_not conditions for safe application."
when_to_use: "Building, reviewing, or reasoning about pattern artifacts"
keywords: [design_pattern, reusable_solution, architectural_pattern]
feeds_kinds: [pattern]
density_score: null
---

# Pattern

## Spec
```yaml
kind: pattern
pillar: P08
llm_function: INJECT
max_bytes: 4096
naming: p08_pat_{{name}}.md + .yaml
core: true
```

## What It Is
A pattern is a named, reusable solution to a recurring architectural problem — it encodes the forces (tensions being resolved), the structure (component roles and relationships), and critically the when_not conditions (where it fails). It is NOT a law (which is inviolable with no exceptions), NOT a workflow (P12, which is an executable sequence with specific steps and triggers).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | LCEL composition patterns | Chain-of-responsibility, map-reduce, routing via `RunnableParallel` |
| LlamaIndex | Workflow patterns | Agentic RAG, multi-step retrieval, reflection loop |
| CrewAI | Process patterns | Sequential pipeline, hierarchical delegation, parallel crews |
| DSPy | Program patterns | `Predict`, `ChainOfThought`, `ReAct`, `Ensemble` compositions |
| Haystack | Pipeline patterns | Indexing pipeline, RAG pipeline, hybrid search pattern |
| OpenAI | Agentic patterns | Run lifecycle, parallel tool calls, handoff patterns |
| Anthropic | Orchestration patterns | Subagent spawning, tool result chains, multi-turn agentic loop |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| name | string | required | Unique kebab-case; memorable = faster adoption |
| intent | string | required | One sentence — precise = fewer misapplications |
| forces | list[str] | required | Tensions resolved; missing = pattern is just a recipe |
| when_not | list[str] | required | Explicit exclusions; missing = overapplication |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Batching pattern | Process N independent items in parallel waves | `continuous-batching`: N tasks → M slots → refill on completion |
| Retry pattern | Resilient execution with exponential backoff | 3-attempt, 1s/2s/4s delays, skip after 3 failures |
| Handoff pattern | Pass structured context across sessions or agents | handoff file → new session reads → continues work |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Pattern without forces | Forces expose the tradeoff — without them it's a recipe | Always document forces: what tensions does this resolve? |
| Premature extraction | Pattern used once, extracted speculatively | Test in ≥3 different contexts before extracting |
| God pattern | Pattern that "solves everything" with no when_not | Every pattern must have explicit when_not conditions |

## Integration Graph
```
law, decision_record --> [pattern] --> workflow, agent_card, instruction
                              |
                         example, diagram, component_map
```

## Decision Tree
- IF solution used ≥3 times across different contexts THEN extract as pattern
- IF decision involves real tradeoffs THEN forces section is mandatory
- IF pattern has known failure modes THEN when_not required before publish
- DEFAULT: document intent + forces + structure + when_not; validate in 3 contexts first

## Quality Criteria
- GOOD: name, intent, forces, structure, when_not all present and non-empty
- GREAT: ASCII/Mermaid structure diagram, ≥2 real usage examples, linked to ADR
- FAIL: missing forces, no when_not, structure described in prose only (no schema)
