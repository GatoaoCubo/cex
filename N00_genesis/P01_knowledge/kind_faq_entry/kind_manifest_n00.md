---
id: n00_faq_entry_manifest
kind: knowledge_card
pillar: P01
nucleus: n00
title: "FAQ Entry -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, faq_entry, p01, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
FAQ Entry is a structured question-answer pair with a canonical, authoritative answer. It is the atomic unit of a FAQ knowledge base used by support agents, chatbots, and documentation systems. Each entry includes the question in natural language, its canonical answer, related questions, and metadata for RAG retrieval.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `faq_entry` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Question as the title |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| question | string | yes | Canonical question text |
| answer | string | yes | Authoritative answer (concise) |
| category | string | yes | FAQ category or topic cluster |
| related_questions | list | no | Variant phrasings or related queries |
| confidence | enum | yes | high\|medium\|low -- answer certainty |

## When to use
- When building a support knowledge base for a chatbot or agent
- When creating product documentation FAQ sections
- When populating a RAG corpus with structured Q&A pairs

## Builder
`archetypes/builders/faq_entry-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind faq_entry --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N04 or N02)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- end users seeking support or information
- `{{DOMAIN_CONTEXT}}` -- product or service domain

## Example (minimal)
```yaml
---
id: faq_entry_cex_what_is_8f
kind: faq_entry
pillar: P01
nucleus: n04
title: "What is the 8F pipeline?"
version: 1.0
quality: null
---
question: "What is the 8F pipeline?"
answer: "The 8F pipeline is CEX's universal reasoning protocol: Constrain, Become, Inject, Reason, Call, Produce, Govern, Collaborate. Every task passes through all 8 functions."
category: CEX architecture
confidence: high
```

## Related kinds
- `knowledge_card` (P01) -- deeper atomic facts for complex answers
- `glossary_entry` (P01) -- term definitions referenced by FAQ answers
- `context_doc` (P01) -- broader domain context for FAQ curation
