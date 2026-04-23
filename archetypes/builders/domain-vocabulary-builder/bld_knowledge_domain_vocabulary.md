---
id: bld_kc_domain_vocabulary
kind: knowledge_card
pillar: P01
llm_function: INJECT
version: 1.0.0
quality: 7.6
tags: [domain_vocabulary, ubiquitous-language, ddd, knowledge]
title: "Knowledge: Domain Vocabulary Pattern"
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - p01_kc_glossary_entry
  - bld_collaboration_glossary_entry
  - bld_instruction_glossary_entry
  - p03_sp_glossary_entry_builder
  - bld_knowledge_card_glossary_entry
  - bld_architecture_glossary_entry
  - p01_gl_TERM_SLUG
  - ontology-builder
  - taxonomy_completeness_audit
  - bld_examples_glossary_entry
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

## Knowledge Injection Checklist

- Verify domain facts are sourced and citable
- Validate density_score >= 0.85 (no filler content)
- Cross-reference with related KCs for consistency
- Check for outdated facts that need refresh

## Injection Pattern

```yaml
# KC injection at F3
source: verified
density: 0.85+
cross_refs: checked
freshness: current
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_retriever.py --query "{DOMAIN}"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_glossary_entry]] | sibling | 0.26 |
| [[bld_collaboration_glossary_entry]] | downstream | 0.25 |
| [[bld_instruction_glossary_entry]] | downstream | 0.24 |
| [[p03_sp_glossary_entry_builder]] | downstream | 0.23 |
| [[bld_knowledge_card_glossary_entry]] | sibling | 0.20 |
| [[bld_architecture_glossary_entry]] | downstream | 0.18 |
| [[p01_gl_TERM_SLUG]] | related | 0.17 |
| [[ontology-builder]] | related | 0.17 |
| [[taxonomy_completeness_audit]] | sibling | 0.16 |
| [[bld_examples_glossary_entry]] | downstream | 0.15 |
