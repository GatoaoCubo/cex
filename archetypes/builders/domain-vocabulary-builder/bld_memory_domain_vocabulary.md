---
id: bld_memory_domain_vocabulary
kind: entity_memory
pillar: P10
llm_function: INJECT
version: 1.0.0
quality: 8.3
tags: [domain_vocabulary, memory, patterns]
title: "Memory Patterns: domain_vocabulary"
author: builder
tldr: "Domain Vocabulary memory: context persistence, recall triggers, and state management"
density_score: 0.95
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_collaboration_glossary_entry
  - p01_kc_glossary_entry
  - taxonomy_completeness_audit
  - bld_instruction_glossary_entry
  - bld_collaboration_type_def
  - p03_sp_glossary_entry_builder
  - n04_rag_pipeline_memory
  - cex_llm_vocabulary_whitepaper
  - bld_tools_collaboration_pattern
  - p03_sp_builder_nucleus
---
# Memory Patterns: domain_vocabulary
## What to Remember
- One vocabulary per bounded_context -- NOT global
- Vocabulary is ENFORCED (loaded at F2b SPEAK), not just documented
- Terms need anti_patterns to be useful -- just definitions aren't enough
- Lifecycle management: propose -> active -> deprecate (never delete)
- domain_vocabulary IS the controlled vocabulary KC pattern in CEX

## Common Mistakes
| Mistake | Correction |
|---------|-----------|
| Global vocabulary for all BCs | Scope to single BC (Account != Account across BCs) |
| Terms without anti_patterns | Add what NOT to call it -- drift prevention |
| Vocabulary as documentation | Load at F2b SPEAK; enforce in every artifact |
| Never deprecating old terms | Deprecated terms cause drift; mark + replace |

## Cross-Kind Memory
- bounded_context: every BC has its own domain_vocabulary
- glossary_entry: single-term detail; domain_vocabulary references, doesn't duplicate
- ubiquitous-language rule (ubiquitous-language.md): the protocol that LOADS domain_vocabulary
- kc_{domain}_vocabulary.md: existing nucleus KCs ARE domain_vocabulary artifacts

## Reuse Signals
- Check if nucleus already has kc_{domain}_vocabulary.md (maps to this kind)
- Check bounded_context definition for vocabulary references
- grep P01 for dv_ prefix files before creating new vocabulary

## Memory Persistence Checklist

- Verify memory type matches taxonomy (entity, episodic, procedural, working)
- Validate retention policy aligns with data lifecycle rules
- Cross-reference with memory_scope for boundary correctness
- Check for stale entries that need decay or pruning

## Memory Pattern

```yaml
# Memory lifecycle
type: classified
retention: defined
scope: bounded
decay: configured
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_memory_update.py --check
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_glossary_entry]] | downstream | 0.23 |
| [[p01_kc_glossary_entry]] | upstream | 0.22 |
| [[taxonomy_completeness_audit]] | upstream | 0.18 |
| [[bld_instruction_glossary_entry]] | upstream | 0.18 |
| [[bld_collaboration_type_def]] | upstream | 0.17 |
| [[p03_sp_glossary_entry_builder]] | upstream | 0.16 |
| [[n04_rag_pipeline_memory]] | related | 0.16 |
| [[cex_llm_vocabulary_whitepaper]] | upstream | 0.16 |
| [[bld_tools_collaboration_pattern]] | upstream | 0.15 |
| [[p03_sp_builder_nucleus]] | upstream | 0.15 |
