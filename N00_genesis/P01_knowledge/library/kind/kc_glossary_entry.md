---
id: p01_kc_glossary_entry
kind: knowledge_card
type: kind
pillar: P01
title: "Glossary Entry — Deep Knowledge for glossary_entry"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: glossary_entry
quality: 9.1
tags: [glossary_entry, p01, INJECT, kind-kc]
tldr: "Short term definition injected for vocabulary grounding — the lightest P01 knowledge unit"
when_to_use: "Building, reviewing, or reasoning about glossary_entry artifacts"
keywords: [glossary, term-definition, vocabulary, grounding]
feeds_kinds: [glossary_entry]
density_score: 0.99
linked_artifacts:
  primary: null
  related: []
related:
  - p01_gl_TERM_SLUG
  - bld_instruction_glossary_entry
  - bld_knowledge_card_glossary_entry
  - p03_sp_glossary_entry_builder
  - bld_collaboration_glossary_entry
  - p10_lr_glossary_entry_builder
  - bld_architecture_glossary_entry
  - bld_schema_glossary_entry
  - p01_kc_context_doc
  - bld_examples_glossary_entry
---

# Glossary Entry

## Spec
```yaml
kind: glossary_entry
pillar: P01
llm_function: INJECT
max_bytes: 512
naming: p01_gl_{{term}}.md + .yaml
core: false
```

## What It Is
A glossary_entry provides a concise definition of a domain-specific term, injected into prompts to ensure consistent vocabulary usage. It is the lightest knowledge unit in P01 — no density minimum, no complex structure, just term + definition + synonyms. It is NOT a knowledge_card (which requires density > 0.8 and formal sections) nor a context_doc (which provides broader domain scope rather than single-term definitions). Max 3 lines of definition.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | No dedicated class; injected via system prompt | Often part of a larger context template |
| LlamaIndex | Metadata dictionary on nodes | Terms as metadata for filtered retrieval |
| CrewAI | Agent backstory vocabulary | Embedded in natural language agent descriptions |
| DSPy | `dspy.InputField(desc=...)` | Term definitions in field descriptions |
| Haystack | `PromptBuilder` variables | Injected as template context |
| OpenAI | System prompt glossary section | Common pattern: "Glossary: term = definition" |
| Anthropic | System prompt definitions | Same pattern; works well with structured blocks |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| term | string | required | Must be the canonical form used in outputs |
| definition | string | required | Shorter = less tokens; longer = more precise |
| synonyms | list | [] | Helps LLM recognize variants but adds tokens |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Inline glossary | 5-15 terms for a specific domain | "KC = Knowledge Card; FSE = Few-Shot Example" |
| Dynamic glossary | Large term set, query-dependent | Retrieve relevant terms based on user query embedding |
| Disambiguation | Terms with multiple meanings | "Pool: in organization = curated knowledge repository (not thread pool)" |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Definition > 3 lines | Becomes a context_doc; wastes glossary budget | Split: short def in glossary, detail in context_doc |
| Glossary with 50+ terms | Token-heavy; most terms unused per query | Use dynamic selection or split by subdomain |
| Synonyms without canonical form | LLM uses random variant in output | Mark one term as canonical; others as synonyms |

## Integration Graph
```
[rag_source] --> [glossary_entry] --> [template (P03), context_doc]
                       |
                [knowledge_card]
```

## Decision Tree
- IF single term needs consistent usage THEN glossary_entry
- IF term needs multi-paragraph explanation THEN context_doc
- IF content has density > 0.8 with structured sections THEN knowledge_card
- IF term is obvious to LLM (e.g., "API") THEN skip — don't over-define
- DEFAULT: glossary_entry for any domain-specific jargon the LLM might misinterpret

## Quality Criteria
- GOOD: Term + clear 1-3 line definition + relevant synonyms
- GREAT: Disambiguates from similar terms; canonical form marked; tested that LLM uses term correctly
- FAIL: Definition exceeds 3 lines; term is universally known; duplicates a knowledge_card's scope

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_gl_TERM_SLUG]] | related | 0.55 |
| [[bld_instruction_glossary_entry]] | downstream | 0.54 |
| [[bld_knowledge_card_glossary_entry]] | sibling | 0.54 |
| [[p03_sp_glossary_entry_builder]] | downstream | 0.51 |
| [[bld_collaboration_glossary_entry]] | downstream | 0.50 |
| [[p10_lr_glossary_entry_builder]] | downstream | 0.50 |
| [[bld_architecture_glossary_entry]] | downstream | 0.50 |
| [[bld_schema_glossary_entry]] | downstream | 0.44 |
| [[p01_kc_context_doc]] | sibling | 0.42 |
| [[bld_examples_glossary_entry]] | downstream | 0.40 |
