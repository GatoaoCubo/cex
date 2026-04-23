---
id: p01_kc_knowledge_card
kind: knowledge_card
type: kind
pillar: P01
title: "Knowledge Card — Deep Knowledge for knowledge_card"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: knowledge_card
quality: 9.1
tags: [knowledge_card, p01, INJECT, kind-kc]
tldr: "The primary atomic knowledge unit — density-gated, versioned, searchable facts optimized for LLM injection"
when_to_use: "Building, reviewing, or reasoning about knowledge_card artifacts"
keywords: [knowledge-card, atomic-knowledge, density, distillation]
feeds_kinds: [knowledge_card]
density_score: null
aliases: ["knowledge document", "fact card", "information unit", "KC", "knowledge base entry"]
user_says: ["document this", "documentar isso", "write a KC", "store this knowledge", "I need to capture what we know about X"]
long_tails: ["I need to document what we know about this topic for retrieval", "store this information so the AI can use it later", "create a dense factual reference about this domain", "write down everything important about X in a searchable format"]
cross_provider:
  langchain: "Document with metadata"
  llamaindex: "TextNode / Document"
  crewai: "Knowledge source / tool result"
  dspy: "dspy.Example / passage"
  openai: "File search chunk / knowledge base"
  anthropic: "Context window injection"
  haystack: "Document dataclass"
related:
  - p01_kc_context_doc
  - bld_collaboration_knowledge_card
  - knowledge-card-builder
  - p01_kc_rag_source
  - bld_architecture_knowledge_card
  - bld_knowledge_card_knowledge_card
  - bld_examples_response_format
  - p01_kc_input_hydration
  - bld_knowledge_card_context_doc
  - bld_instruction_kind
---

# Knowledge Card

## Spec
```yaml
kind: knowledge_card
pillar: P01
llm_function: INJECT
max_bytes: 5120
naming: p01_kc_{{topic}}.md + .yaml
core: true
```

## What It Is
A knowledge_card is the foundational knowledge unit in CEX — a distilled, static, versioned fact optimized for vector search and LLM injection. Every KC has a density gate (>0.8): each sentence must carry non-obvious information. It is NOT an instruction (P03, which tells the LLM what to do), NOT a template (which defines output structure), and NOT a configuration (which sets runtime parameters). KCs answer "what is true" — instructions answer "what to do."

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `Document` with metadata | KCs are Documents with structured frontmatter as metadata |
| LlamaIndex | `TextNode` / `Document` | Nodes with metadata; KCs map to indexed documents |
| CrewAI | Knowledge sources / tool results | Injected via RAG tools or agent knowledge base |
| DSPy | `dspy.Example` / passages | Retrieved passages in RAG pipelines |
| Haystack | `Document` dataclass | Documents with meta dict; KCs as curated documents |
| OpenAI | File search chunks / knowledge base | Assistants API file_search indexes documents |
| Anthropic | Context window injection | No native knowledge store; KCs injected as system context |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| density_score | float | >0.8 required | Higher density = more info per token but harder to author |
| max_bytes | int | 5120 | Larger = more comprehensive but slower retrieval |
| quality | float | >7.0 min | Pool threshold 8.0; Golden threshold 9.5 |
| type | enum | domain/kind/meta | Determines body_structure sections |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Domain KC | Vertical-specific knowledge | Brazilian e-commerce marketplace rules |
| Kind KC | Meta-knowledge about a CEX kind | This file — describing what a knowledge_card is |
| Meta KC | Cross-cutting system knowledge | Architecture patterns, framework comparisons |
| Cluster KC | Reference material absorbed by kind KCs | Raw research collected before distillation |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Low density filler sentences | Wastes tokens; dilutes retrieval signal | Every sentence must pass "is this non-obvious?" test |
| Instructions disguised as knowledge | KC says "you should" instead of "X is" | Move imperative content to P03 instructions |
| Unstable facts without versioning | Knowledge drifts silently | Always increment version on content changes |

## Integration Graph
```
[rag_source] --> [knowledge_card] --> [template (P03), context_doc]
                       |
              [few_shot_example, glossary_entry]
```

## Decision Tree
- IF content is a single term definition THEN glossary_entry
- IF content is broad domain background THEN context_doc
- IF content is distilled, dense, searchable facts THEN knowledge_card
- IF content describes a CEX kind THEN knowledge_card (type: kind)
- IF content is raw research not yet distilled THEN cluster KC in _reference/
- DEFAULT: knowledge_card for any factual content with density > 0.8

## Quality Criteria
- GOOD: Density > 0.8; frontmatter complete; under 5120 bytes; clear boundary
- GREAT: Density > 0.9; cross-references linked_artifacts; tested in retrieval pipeline; quality >= 8.0
- FAIL: Density < 0.8; contains instructions; missing required frontmatter; no clear boundary from other kinds

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_context_doc]] | sibling | 0.36 |
| [[bld_collaboration_knowledge_card]] | downstream | 0.31 |
| [[knowledge-card-builder]] | downstream | 0.28 |
| [[p01_kc_rag_source]] | sibling | 0.27 |
| [[bld_architecture_knowledge_card]] | downstream | 0.26 |
| [[bld_knowledge_card_knowledge_card]] | sibling | 0.26 |
| [[bld_examples_response_format]] | downstream | 0.25 |
| [[p01_kc_input_hydration]] | sibling | 0.24 |
| [[bld_knowledge_card_context_doc]] | sibling | 0.24 |
| [[bld_instruction_kind]] | downstream | 0.24 |
