---
id: consolidation_policy_n01
kind: consolidation_policy
8f: F1_constrain
pillar: P10
nucleus: n01
title: "N01 Memory Consolidation Policy"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.1
tags: [consolidation_policy, memory_management, n01, decay, archival, compaction]
tldr: "Rules for N01 memory consolidation: when to merge duplicate entities, when to archive stale KCs, how to compact session records, and when to rebuild the knowledge index. Prevents corpus bloat while preserving compound intelligence."
density_score: 0.88
updated: "2026-04-17"
related:
  - bld_examples_lifecycle_rule
  - kc_consolidation_policy
  - bld_collaboration_entity_memory
  - p01_kc_memory_management
  - bld_knowledge_card_consolidation_policy
  - p04_ct_cex_feedback
  - p11_lc_{{RULE_SLUG}}
  - p01_kc_session_state
  - bld_collaboration_knowledge_index
  - bld_memory_session_state
---

<!-- 8F: F1 constrain=P10/consolidation_policy F2 become=N00 generic builder pattern F3 inject=memory_architecture_n01+knowledge_index_n01+entity_memory_n01+mem_memory_summary_n01 F4 reason=without consolidation, the corpus grows unboundedly and retrieval quality degrades F5 call=cex_compile F6 produce=consolidation_policy_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P10_memory/ -->

## Purpose

Analytical Envy creates insatiable accumulation. Without a consolidation policy:
- Entity memory spawns duplicates (co_openai.yaml + co_open_ai.yaml + co_OpenAI.yaml)
- Session records accumulate indefinitely (90-day archive = 900MB/year)
- Knowledge cards become stale while new ones duplicate them
- Knowledge index accuracy degrades (deleted files still indexed)

This policy governs when and how N01 reduces memory size while preserving intelligence quality.

## Consolidation Triggers

| Trigger | Condition | Action |
|---------|-----------|--------|
| Entity duplicate | 2 entity files for same company (fuzzy match > 0.9) | MERGE |
| KC staleness | knowledge_card.last_updated > 90 days + topic still active | REFRESH |
| KC superseded | new KC covers same topic at higher quality | ARCHIVE old |
| Session age | session record > 30 days | SUMMARIZE + COMPRESS |
| Index stale | index.last_build + 24h < now AND new files exist | REBUILD |
| Corpus size | total corpus > 500MB | ARCHIVE oldest 20% |

## Entity Consolidation Rules

### Duplicate Detection

```
for entity_a, entity_b in combinations(entity_files):
    similarity = fuzzy_match(entity_a.name, entity_b.name)
    if similarity > 0.90:
        flag_duplicate(entity_a, entity_b)
```

### Merge Protocol

| Field | Merge Rule |
|-------|-----------|
| `name` | keep canonical (most official: SEC / LinkedIn) |
| `slug` | keep lowercase, no punctuation |
| `products` | union of both lists |
| `strategic_moves` | union, sorted by date |
| `sources` | union, deduplicated |
| `pricing_snapshot` | keep most recent (by pricing_date) |
| `strengths / weaknesses` | union, deduplicated |
| `last_updated` | max(entity_a.last_updated, entity_b.last_updated) |

## Knowledge Card Consolidation Rules

| Scenario | Detection | Action |
|----------|-----------|--------|
| Stale KC | last_updated > 90 days | add `[STALE - refresh by {date}]` banner |
| Superseded KC | new KC score > old KC by >= 1.0 | archive old to `P01_knowledge/archive/` |
| Duplicate KC | 2 KCs with cosine_similarity > 0.85 | merge into single, delete lower-quality |
| Orphaned KC | KC references entity that no longer exists | update reference or archive |

## Session Record Compaction

| Age | Action |
|-----|--------|
| 0-7 days | retain full session record |
| 7-30 days | compress: retain only key_findings + entities_discovered |
| 30-90 days | summarize: 1-paragraph session summary only |
| > 90 days | archive to `P10_memory/archive/{year}/` |

Compaction output format:
```yaml
session_id: "string"
date: ISO8601
goal: "string"
summary: "one paragraph"
entities_discovered: ["slugs only"]
artifacts_created: ["paths only"]
```

## Index Rebuild Schedule

| Trigger | Rebuild Type | Duration |
|---------|-------------|---------|
| New file written (F8) | incremental (1 doc) | < 1s |
| Daily cron | incremental (all new since last) | < 10s |
| Weekly Sunday | full rebuild | < 60s |
| Consolidation complete | full rebuild (mandatory) | < 60s |

## Corpus Size Budget

| Component | Target Size | Alert | Action |
|-----------|------------|-------|--------|
| Entity YAML files | < 50MB | > 100MB | archive old events |
| Session records (30d) | < 20MB | > 50MB | compress earlier sessions |
| Knowledge cards | < 100MB | > 200MB | archive superseded |
| Embedding index | < 50MB | > 150MB | rebuild with pruning |
| BM25 index | < 10MB | > 50MB | rebuild |

## Anti-Over-Consolidation Rules

Analytical Envy means NEVER deleting intelligence prematurely:

| Rule | Rationale |
|------|-----------|
| Never hard-delete entity files | archive only; may need historical view |
| Never delete KCs without 30-day archive period | lost knowledge = regression |
| Never rebuild index during active research session | retrieval consistency |
| Never consolidate without git commit before and after | rollback safety |

## Comparison: Consolidation Approaches

| Approach | Automation | Safety | N01 Fit |
|----------|-----------|--------|---------|
| No consolidation | N/A | N/A | corpus bloat, retrieval degrades |
| Manual cleanup | 0% | high | impractical at scale |
| Aggressive auto-delete | 100% | low | data loss risk |
| This policy (conservative auto) | 80% | high | optimal |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_lifecycle_rule]] | related | 0.23 |
| [[kc_consolidation_policy]] | upstream | 0.23 |
| [[bld_collaboration_entity_memory]] | downstream | 0.23 |
| [[p01_kc_memory_management]] | upstream | 0.22 |
| [[bld_knowledge_card_consolidation_policy]] | upstream | 0.21 |
| [[p04_ct_cex_feedback]] | upstream | 0.20 |
| [[p11_lc_{{RULE_SLUG}}]] | downstream | 0.20 |
| [[p01_kc_session_state]] | related | 0.20 |
| [[bld_collaboration_knowledge_index]] | downstream | 0.19 |
| [[bld_memory_session_state]] | related | 0.19 |
