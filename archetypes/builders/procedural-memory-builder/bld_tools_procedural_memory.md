---
kind: tools
id: bld_tools_procedural_memory
pillar: P04
llm_function: CALL
purpose: Tools available for procedural_memory production
quality: 9.0
title: "Tools: procedural_memory-builder"
version: "2.0.0"
author: n06_commercial
tags: [procedural_memory, builder, tools]
tldr: "CEX tools for procedural_memory production: compile, score, retriever, doctor, query. External: Redis, Voyager SDK, Reflexion patterns."
domain: "LLM agent procedural memory"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - bld_tools_consolidation_policy
  - bld_instruction_procedural_memory
  - bld_tools_memory_architecture
  - p03_sp_procedural_memory_builder
  - procedural-memory-builder
  - bld_knowledge_card_procedural_memory
  - p10_qg_procedural_memory
  - bld_collaboration_procedural_memory
  - bld_tools_skill
  - bld_output_template_procedural_memory
---

## CEX Production Tools

| Tool | Purpose | When |
|------|---------|------|
| `python _tools/cex_compile.py {path}` | Compile .md to .yaml + validate frontmatter | After every write |
| `python _tools/cex_score.py --apply {path}` | Score artifact against quality gate | After compile |
| `python _tools/cex_retriever.py {query}` | Find similar procedural_memory artifacts | Before writing (Template-First) |
| `python _tools/cex_doctor.py` | Health check on builder ISOs | After batch edits |
| `python _tools/cex_query.py procedural_memory` | Discover related kinds (memory_architecture, consolidation_policy) | F1 CONSTRAIN |

## External Reference Systems

| System | Purpose |
|--------|---------|
| Voyager (Wang 2023) | Reference for skill library design and verify-before-store pattern |
| Reflexion (Shinn 2023) | Reference for self-note storage and retrieval patterns |
| ExpeL (Zhao 2023) | Reference for experience extraction from trajectories |
| Redis | Skill KV store backend with TTL |
| PostgreSQL | Persistent skill store with versioning |
| E2B / Docker sandbox | Skill verification execution environment |

## Validation Checklist (run before commit)

- [ ] `grep -i "motor schema\|basal ganglia\|ACT-R\|cerebellum\|subsumption\|neural pathway" {file}` returns nothing
- [ ] `skill_format` field present in frontmatter
- [ ] `tier` field present in frontmatter
- [ ] Skills section present in body (or explicitly states "no skills - free tier")
- [ ] Verification strategy defined
- [ ] Commercial Tier Matrix present
- [ ] `quality: null` in frontmatter

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_consolidation_policy]] | sibling | 0.50 |
| [[bld_instruction_procedural_memory]] | upstream | 0.40 |
| [[bld_tools_memory_architecture]] | sibling | 0.39 |
| [[p03_sp_procedural_memory_builder]] | upstream | 0.36 |
| [[procedural-memory-builder]] | downstream | 0.34 |
| [[bld_knowledge_card_procedural_memory]] | upstream | 0.33 |
| [[p10_qg_procedural_memory]] | downstream | 0.32 |
| [[bld_collaboration_procedural_memory]] | downstream | 0.31 |
| [[bld_tools_skill]] | sibling | 0.30 |
| [[bld_output_template_procedural_memory]] | downstream | 0.30 |
