---
kind: instruction
id: bld_instruction_consolidation_policy
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for consolidation_policy
quality: 9.0
title: "Instruction: consolidation_policy-builder"
version: "2.0.0"
author: n06_commercial
tags: [consolidation_policy, builder, instruction]
tldr: "8F production process for LLM agent memory consolidation policy: load schema, define promotion rules, eviction strategy, importance scoring, tier matrix, compliance"
domain: "LLM agent memory consolidation"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
---

## Phase 1: RESEARCH

1. Identify the parent memory_architecture artifact (which layers are active, what tier).
2. Determine which memory transitions need consolidation rules:
   - Does the agent have episodic memory? If yes, define working -> episodic promotion.
   - Does the agent have semantic memory? If yes, define episodic -> semantic promotion.
3. Map the target commercial tier (free/pro/enterprise) against the tier matrix
   in bld_knowledge_card_consolidation_policy.md.
4. Review reference pipelines: MemGPT/Letta consolidation pipeline (Packer 2023),
   mem0 selective extraction, Zep deduplication/merge.
5. Identify compliance requirements: GDPR Art. 17, HIPAA, data residency constraints.
6. Check bld_schema_consolidation_policy.md for required frontmatter and body structure.

## Phase 2: COMPOSE

1. Write frontmatter per bld_schema_consolidation_policy.md (all required fields,
   quality: null, consolidation_async: true).
2. Write Overview: agent type, tier, consolidation strategy summary.
3. Write Promotion Rules table:
   - Columns: Trigger | Source Layer | Target Layer | Condition | Action
   - Row per active transition (working->episodic on session end, etc.)
4. Write Eviction Rules table:
   - Columns: Layer | Strategy | Trigger | Action
   - Row per active layer with concrete trigger (TTL, importance floor, LRU budget)
5. Write Importance Scoring section: formula, model reference, or scoring rubric.
6. Write Consolidation Job section: async trigger, schedule, timeout, failure handling.
7. Write Commercial Tier Matrix: FREE/PRO/ENTERPRISE capability comparison.
8. Write Compliance Config (required for enterprise): retention_days, data_residency,
   gdpr_erasure procedure, audit_trail config.

## Phase 3: VALIDATE

- [ ] Schema compliance: all required frontmatter fields present, ID matches pattern.
- [ ] Domain accuracy: content is agent memory consolidation, not OS/GC memory.
- [ ] consolidation_async: true in frontmatter.
- [ ] Promotion Rules table: at least one row for active tier.
- [ ] Eviction Rules table: at least one row per active layer.
- [ ] Tier matrix present: FREE/PRO/ENTERPRISE differentiation explicit.
- [ ] Compliance section present if tier=enterprise.
- [ ] No OS memory terminology: GC, slab, heap, TLB, fragmentation, compaction.
- [ ] quality: null in frontmatter (never self-score).
- [ ] No Unicode characters (ASCII only per ascii-code-rule.md).
