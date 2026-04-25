---
id: bld_context_sources_domain_vocabulary
kind: rag_source
pillar: P10
llm_function: CONSTRAIN
version: 1.0.0
quality: 8.3
tags: [domain_vocabulary, context, rag]
title: "Context Sources: domain_vocabulary"
author: builder
tldr: "Domain Vocabulary memory: naming conventions, output paths, and production limits"
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_architecture_kind
  - bld_collaboration_glossary_entry
  - p01_kc_glossary_entry
  - bld_instruction_glossary_entry
  - bld_tools_kind
  - bld_instruction_kind
  - bld_collaboration_kind
  - bld_architecture_glossary_entry
  - bld_collaboration_type_def
  - p01_gl_TERM_SLUG
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

## Configuration Checklist

- Verify all required fields are present in frontmatter before saving
- Validate config values against schema constraints (type, range, enum)
- Cross-reference with related configs to avoid contradictions
- Test config loading in target runtime before committing

## Validation

```yaml
# Required config validation
fields_present: true
types_valid: true
ranges_checked: true
cross_refs_verified: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | upstream | 0.28 |
| [[bld_collaboration_glossary_entry]] | downstream | 0.26 |
| [[p01_kc_glossary_entry]] | upstream | 0.26 |
| [[bld_instruction_glossary_entry]] | upstream | 0.23 |
| [[bld_tools_kind]] | upstream | 0.22 |
| [[bld_instruction_kind]] | upstream | 0.22 |
| [[bld_collaboration_kind]] | downstream | 0.22 |
| [[bld_architecture_glossary_entry]] | upstream | 0.20 |
| [[bld_collaboration_type_def]] | upstream | 0.20 |
| [[p01_gl_TERM_SLUG]] | upstream | 0.20 |
