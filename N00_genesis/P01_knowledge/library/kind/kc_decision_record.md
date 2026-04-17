---
id: p01_kc_decision_record
kind: knowledge_card
type: kind
pillar: P08
title: "Decision Record — Deep Knowledge for decision_record"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: commercial_agent
domain: decision_record
quality: 9.1
tags: [decision_record, P08, REASON, kind-kc, ADR]
tldr: "decision_record (ADR) captures an architectural decision with its context, the decision itself, rejected alternatives, and consequences — making reasoning durable across sessions and team members."
when_to_use: "Building, reviewing, or reasoning about decision_record artifacts"
keywords: [ADR, architectural_decision, rationale]
feeds_kinds: [decision_record]
density_score: null
---

# Decision Record

## Spec
```yaml
kind: decision_record
pillar: P08
llm_function: REASON
max_bytes: 4096
naming: p08_adr.md
core: true
```

## What It Is
A decision_record is a versioned document capturing a significant architectural decision: the context (forces at play), the decision made, alternatives considered and rejected, and the consequences (positive and negative). It is NOT a law (laws are inviolable operational rules), NOT a pattern (patterns are reusable solutions without the narrative of why alternatives were rejected).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | N/A | Decisions embedded in code comments; no formal ADR |
| LlamaIndex | N/A | `Settings` object captures some config decisions implicitly |
| CrewAI | N/A | Process choice (sequential vs hierarchical) is typically undocumented |
| DSPy | N/A | Optimizer selection rationale lives in experiment logs, not ADRs |
| Haystack | N/A | Pipeline topology decisions implicit in `Pipeline.connect()` calls |
| OpenAI | N/A | API design decisions in changelogs; no formal ADR format |
| Anthropic | N/A | Model selection and tool_choice rationale documented in system prompts |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| status | enum | proposed | proposed → accepted → superseded → deprecated |
| context | string | required | More context = easier future decisions; too much = noise |
| alternatives | list[string] | required | More alternatives = richer rationale; minimum 2 |
| consequences | list[string] | required | Both positive and negative mandatory |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Technology choice | Comparing 2+ infrastructure/library options | Railway vs Fly.io ADR with cost/ops tradeoffs |
| Architecture pivot | Recording why system design fundamentally changed | Sync → async migration rationale |
| Policy decision | Encoding team-wide operational rules | Rate-limit policy, deployment freeze ADR |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| No alternatives | No alternatives = no real decision documented | Always document ≥2 rejected alternatives |
| Consequence-free ADR | Missing consequences makes ADR useless for future teams | Mandate ≥1 positive + ≥1 negative consequence |
| Post-hoc rationalization | Writing ADR after implementation loses original context | Write ADR before or during decision, not after |

## Integration Graph
```
law, pattern, component_map --> [decision_record] --> law (consequent), pattern
                                       |
                                  agent_card, workflow, naming_rule
```

## Decision Tree
- IF decision affects >1 agent_group or >1 team THEN ADR mandatory
- IF reversing a previous decision THEN supersede old ADR + create new ADR
- IF small tactical choice (1 file, 1 function) THEN inline comment sufficient
- DEFAULT: ADR for any cross-team, cross-agent_group, or persistent architectural choice

## Quality Criteria
- GOOD: status, context, decision statement, consequences all present with date
- GREAT: alternatives section with explicit rejection rationale, links to superseded ADRs
- FAIL: missing consequences, no date, vague decision ("we decided to improve things")
