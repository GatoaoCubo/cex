---
id: bld_memory_domain_vocabulary
kind: entity_memory
pillar: P10
llm_function: INJECT
version: 1.0.0
quality: 5.8
tags: [domain_vocabulary, memory, patterns]
title: "Memory Patterns: domain_vocabulary"
density_score: 0.95
updated: "2026-04-17"
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
