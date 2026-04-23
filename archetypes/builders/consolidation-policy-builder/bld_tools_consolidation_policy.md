---
kind: tools
id: bld_tools_consolidation_policy
pillar: P04
llm_function: CALL
purpose: Tools available for consolidation_policy production
quality: 9.0
title: "Tools: consolidation_policy-builder"
version: "2.0.0"
author: n06_commercial
tags: [consolidation_policy, builder, tools]
tldr: "CEX tools for consolidation_policy production: compile, score, retriever, doctor, query. Validation: grep for OS terms, check consolidation_async."
domain: "LLM agent memory consolidation"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - bld_tools_procedural_memory
  - bld_tools_memory_architecture
  - bld_instruction_consolidation_policy
  - bld_instruction_memory_architecture
  - p03_sp_consolidation_policy_builder
  - p10_qg_consolidation_policy
  - consolidation-policy-builder
  - bld_collaboration_consolidation_policy
  - p10_mem_consolidation_policy_builder
  - bld_examples_consolidation_policy
---

## CEX Production Tools

| Tool | Purpose | When |
|------|---------|------|
| `python _tools/cex_compile.py {path}` | Compile .md to .yaml + validate frontmatter | After every write |
| `python _tools/cex_score.py --apply {path}` | Score artifact against quality gate | After compile |
| `python _tools/cex_retriever.py {query}` | Find similar consolidation_policy artifacts | Before writing (Template-First) |
| `python _tools/cex_doctor.py` | Health check on builder ISOs | After batch edits |
| `python _tools/cex_query.py consolidation_policy` | Discover related kinds (memory_architecture, procedural_memory) | F1 CONSTRAIN |

## External Reference Systems

| System | Purpose |
|--------|---------|
| mem0 SDK | Reference for importance scoring + selective extraction |
| Zep SDK | Reference for deduplication + merge strategies |
| MemGPT/Letta | Reference for sleep-time consolidation pipeline |
| pgvector | Episodic memory backend for TTL + semantic search eviction |
| Redis | Procedural memory backend + TTL-based eviction |

## Validation Checklist (run before commit)

- [ ] `grep -i "GC\|garbage\|slab\|heap\|fragmentation\|compaction\|TLB\|malloc\|dealloc" {file}` returns nothing
- [ ] `consolidation_async: true` in frontmatter
- [ ] `tier` field present in frontmatter
- [ ] Promotion Rules section present with table
- [ ] Eviction Rules section present with table
- [ ] Commercial Tier Matrix present in body
- [ ] Compliance Config present if `tier: enterprise`
- [ ] `quality: null` in frontmatter

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_procedural_memory]] | sibling | 0.50 |
| [[bld_tools_memory_architecture]] | sibling | 0.48 |
| [[bld_instruction_consolidation_policy]] | upstream | 0.38 |
| [[bld_instruction_memory_architecture]] | upstream | 0.33 |
| [[p03_sp_consolidation_policy_builder]] | upstream | 0.33 |
| [[p10_qg_consolidation_policy]] | downstream | 0.32 |
| [[consolidation-policy-builder]] | downstream | 0.30 |
| [[bld_collaboration_consolidation_policy]] | downstream | 0.29 |
| [[p10_mem_consolidation_policy_builder]] | downstream | 0.28 |
| [[bld_examples_consolidation_policy]] | downstream | 0.28 |
