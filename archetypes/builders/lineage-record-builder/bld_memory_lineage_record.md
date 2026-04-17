---
id: bld_memory_lineage_record
kind: knowledge_card
pillar: P10
title: "Memory: lineage_record Builder Patterns"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: lineage_record
quality: null
tags: [memory, lineage_record, P01]
llm_function: INJECT
tldr: "Recalled patterns and corrections for lineage_record builder sessions."
density_score: null
---

# Memory: lineage_record Builder

## Persistent Patterns
| Pattern | Frequency | Note |
|---------|-----------|------|
| At least 1 source entity required | HIGH | Gate H06 |
| ISO 8601 timestamps on all entities and activities | HIGH | Gate H07 |
| PROV-O vocabulary in derivation relations | HIGH | Domain standard |
| Agent identified for each activity | HIGH | Gate H08 |

## Common Corrections
| Mistake | Correction |
|---------|-----------|
| User conflates with audit_log | Redirect: audit_log is compliance events; lineage_record is knowledge provenance |
| User conflates with citation | Teach: citation is in-text ref; lineage_record is full derivation chain |
| User omits timestamps | Block: add timestamps or mark as unknown with note |
| User lists agents without roles | Add role field: synthesizer, curator, validator |
| sources_count mismatch | Recount and correct frontmatter field |
