---
id: bld_kc_domain_vocabulary
kind: knowledge_card
pillar: P01
llm_function: INJECT
version: 1.0.0
quality: 6.5
tags: [domain_vocabulary, ubiquitous-language, ddd, knowledge]
title: "Knowledge: Domain Vocabulary Pattern"
density_score: 1.0
updated: "2026-04-17"
---
# Domain Knowledge: domain_vocabulary
## Core Facts
- DDD Ubiquitous Language (Evans 2003 ch.2): shared language between domain experts + developers
- domain_vocabulary = the registry artifact that GOVERNS this shared language
- Scope: one vocabulary per bounded_context (not global -- BCs have different meanings for same word)
- Classic ambiguity example: "Account" means different things in Sales vs. Banking vs. Social
- CEX uses domain_vocabulary to prevent F2b SPEAK failures across nuclei
- Term lifecycle: proposed (draft) -> active (enforced) -> deprecated (replaced)

## Boundary vs. Similar Kinds
| Aspect | domain_vocabulary | glossary_entry | ontology |
|--------|------------------|----------------|---------|
| Scope | Whole BC registry | Single term | Formal relations |
| Structure | Table of terms | Single definition | Graph |
| Enforces | Ubiquitous Language | Clarity | Semantic web |
| Pattern | DDD UL | Dictionary | OWL/RDF |

## Loading Protocol
Agents load domain_vocabulary at F2b SPEAK (before F3 INJECT).
Every nucleus has: N0X_{domain}/P01_knowledge/kc_{domain}_vocabulary.md
This matches the domain_vocabulary kind -- it IS the controlled vocabulary.

## Anti-Patterns
| Anti-Pattern | Correct Approach |
|-------------|-----------------|
| One global vocabulary | One per bounded context (ambiguity varies by BC) |
| Vocabulary = documentation | Vocabulary = enforced in every artifact produced |
| Terms without anti_patterns | Anti-patterns prevent drift when term is loaded |
| Stale terms (never deprecated) | Lifecycle management: mark deprecated + replaced_by |
