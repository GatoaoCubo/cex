---
id: p01_kc_learning_record
kind: knowledge_card
type: kind
pillar: P10
title: "Learning Record — Deep Knowledge for learning_record"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: research_agent
domain: learning_record
quality: 9.1
tags: [learning_record, P10, INJECT, kind-kc]
tldr: "Persistent record of what worked or failed in a session, accumulated across runs for agent improvement"
when_to_use: "Building, reviewing, or reasoning about learning_record artifacts"
keywords: [learning, memory, retrospective]
feeds_kinds: [learning_record]
density_score: null
---

# Learning Record

## Spec
```yaml
kind: learning_record
pillar: P10
llm_function: INJECT
max_bytes: 3072
naming: p10_lr_{{topic}}.md + .yaml
core: true
```

## What It Is
A learning record is a persistent, structured log of what an agent discovered across one or more sessions — which approaches succeeded, which failed, and why. It accumulates over time via append-or-update writes and is injected into future sessions to bias behavior. It is NOT session_state (ephemeral, discarded after session) nor an axiom (immutable truth; learning records evolve with evidence).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `BaseChatMessageHistory` + custom persistence | Persist structured feedback entries beyond message history |
| LlamaIndex | `DocumentStore` with metadata versioning | Store learning entries as versioned Documents |
| CrewAI | `Memory` (long-term scope) | LTM in CrewAI stores task outcomes; learning_record is explicit structured version |
| DSPy | `History` type + optimizer traces | Optimizer demonstrations capture what worked — equivalent concept |
| Haystack | `DocumentStore` with TTL=never | No native learning record; use persistent doc store with append writes |
| OpenAI | Thread metadata + fine-tune JSONL | Accumulated examples feed fine-tuning pipelines |
| Anthropic | Custom file-based persistence | Inject via system prompt on next session |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| topic | string | required | Narrow topic = precise recall vs broad = noisy injection |
| score | float [0,10] | null | Higher score = stronger bias; use null until validated |
| pattern | string | required | Actionable summary; vague patterns add noise |
| anti_pattern | string | null | Explicit negatives prevent repeated failures |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Score-gated append | Only record outcomes >= 7.0 | `if score >= 7.0: append to p10_lr_topic.md` |
| Anti-pattern capture | After 2+ consecutive failures on same approach | `anti: tried X, failed because Y` |
| Cross-topic federation | Same learning applies to multiple domains | Tag with multiple topics; inject into all matching sessions |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Recording every session | Noise overwhelms signal; LLM context fills with low-value entries | Gate on score >= 7.0 or explicit user confirmation |
| Mutable axioms disguised as learning | Permanent facts that should never change get overwritten | Use axiom kind for immutable knowledge |
| Injecting all records regardless of session topic | Irrelevant learning fills context window | Filter by topic match before injection |

## Integration Graph
```
[session_state] --> [learning_record] --> [action_prompt]
                         |
                    [memory_summary]
```

## Decision Tree
- IF outcome score >= 9.0 THEN promote to pool (golden pattern)
- IF outcome score 7.0–8.9 THEN write learning_record, inject next session
- IF outcome score < 7.0 THEN discard or write anti-pattern entry
- DEFAULT: Score before writing; never record without evaluation

## Quality Criteria
- GOOD: Has topic, score, pattern, date; under 3072 bytes; actionable summary
- GREAT: Includes anti-pattern, cross-topic tags, concrete example with context
- FAIL: No score; vague pattern ("it worked"); records every session regardless of quality
