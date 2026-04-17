---
id: bld_context_sources_domain_vocabulary
kind: rag_source
pillar: P10
llm_function: INJECT
version: 1.0.0
quality: null
tags: [domain_vocabulary, context, rag]
title: "Context Sources: domain_vocabulary"
---
# Context Sources: domain_vocabulary
## Mandatory Sources (load at F3 INJECT)
| Source | Path | Why |
|--------|------|-----|
| Kind KC | N00_genesis/P01_knowledge/library/kind/kc_domain_vocabulary.md | Definition + boundary |
| Schema | archetypes/builders/domain-vocabulary-builder/bld_schema_domain_vocabulary.md | Required structure |
| Examples | archetypes/builders/domain-vocabulary-builder/bld_examples_domain_vocabulary.md | Golden patterns |
| UL rule | .claude/rules/ubiquitous-language.md | Loading protocol |

## Optional Sources (load if relevant)
| Source | Path | When to Load |
|--------|------|-------------|
| bounded_context KC | N00_genesis/P01_knowledge/library/kind/kc_bounded_context.md | BC scoping rules |
| Existing vocabulary | {nucleus}/P01_*/dv_*.md | Consistency with existing vocabs |
| Nucleus vocabulary KCs | N0X_{domain}/P01_knowledge/kc_{domain}_vocabulary.md | Maps to this kind |

## Search Queries for Retrieval
- "ubiquitous language domain model DDD bounded context"
- "controlled vocabulary semantic drift prevention"
- "term registry canonical terms anti-patterns"
- "F2b SPEAK vocabulary loading protocol"

## Anti-Sources (do NOT confuse with)
- glossary_entry (single term, not registry)
- ontology (formal relations, not term registry)
- knowledge_card (facts about domain, not term governance)
