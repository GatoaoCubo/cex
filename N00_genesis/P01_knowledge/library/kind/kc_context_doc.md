---
id: p01_kc_context_doc
kind: knowledge_card
type: kind
pillar: P01
title: "Context Doc — Deep Knowledge for context_doc"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: context_doc
quality: 9.1
tags: [context_doc, p01, INJECT, kind-kc]
tldr: "Domain context injected into prompts to ground LLM reasoning — richer than glossary, looser than knowledge_card"
when_to_use: "Building, reviewing, or reasoning about context_doc artifacts"
keywords: [context, domain-knowledge, prompt-hydration, grounding]
feeds_kinds: [context_doc]
density_score: null
---

# Context Doc

## Spec
```yaml
kind: context_doc
pillar: P01
llm_function: INJECT
max_bytes: 2048
naming: p01_ctx_{{topic}}.md + .yaml
core: false
```

## What It Is
A context_doc provides domain-specific background knowledge injected into prompts to improve LLM grounding. It carries broader scope than a glossary_entry (which defines a single term) and has no density gate unlike a knowledge_card (which requires density > 0.8). Context docs fill the gap between raw documents and distilled knowledge cards — they provide enough context for the LLM to reason correctly about a domain without requiring formal structure.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | System message / context in prompt templates | Injected via `SystemMessage` or template variables |
| LlamaIndex | `ServiceContext` / metadata injection | Attached as node metadata or query context |
| CrewAI | Agent backstory / task context | `backstory` field and `context` parameter on tasks |
| DSPy | `dspy.InputField` with desc | Context passed as typed input to signatures |
| Haystack | `PromptBuilder` template variables | Jinja2 templates with context slots |
| OpenAI | System prompt or `additional_instructions` | Assistants API uses `instructions` field |
| Anthropic | System prompt block | First content block in messages API |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| scope | string | required | Broader scope = more tokens consumed but fewer docs needed |
| domain | string | required | Cross-domain context risks confusion vs. specificity |
| freshness | date | created | Stale context = hallucination risk; fresh = maintenance cost |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Domain primer | Agent entering unfamiliar vertical | "Brazilian e-commerce uses Mercado Livre as primary marketplace..." |
| Regulatory backdrop | Compliance-sensitive outputs | ANVISA rules injected before product description generation |
| Project state | Multi-session continuity | Current sprint goals, recent decisions, team conventions |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Context too large (> 2KB) | Exceeds budget, competes with user query | Split into focused context docs per subdomain |
| Stale context | LLM uses outdated facts confidently | Add freshness date; review monthly |
| Duplicating knowledge_card content | Redundant tokens, version drift | Reference the KC; context_doc adds framing only |

## Integration Graph
```
[rag_source, knowledge_card] --> [context_doc] --> [system_prompt, template]
                                      |
                               [glossary_entry]
```

## Decision Tree
- IF defining a single term THEN use glossary_entry instead
- IF content requires density > 0.8 and formal structure THEN use knowledge_card instead
- IF providing broad domain background for prompt grounding THEN context_doc
- IF content is a raw external document THEN use rag_source instead
- DEFAULT: context_doc for any domain context that doesn't fit other P01 kinds

## Quality Criteria
- GOOD: Clear scope boundary; useful domain context; under 2KB
- GREAT: Specific enough to improve output quality measurably; includes freshness date; links to authoritative sources
- FAIL: No scope defined; duplicates knowledge_card content; exceeds max_bytes; contains instructions (should be P03)
