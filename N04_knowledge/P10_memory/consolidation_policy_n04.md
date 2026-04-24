---
id: p10_cp_n04_knowledge
kind: consolidation_policy
8f: F1_constrain
pillar: P10
nucleus: n04
title: "Consolidation Policy -- N04 Memory Consolidation Rules"
version: "1.0.0"
quality: 9.2
tags: [consolidation_policy, memory, episodic, n04, P10, TTL, similarity]
domain: knowledge management
status: active
created: "2026-04-17"
updated: "2026-04-17"
author: n04_knowledge
tldr: "Rules governing when and how N04 consolidates memory: episodic session compression, semantic deduplication, procedural versioning, and TTL-based eviction. Prevents memory bloat while preserving signal."
density_score: null
related:
  - bld_knowledge_card_consolidation_policy
  - bld_output_template_memory_architecture
  - bld_knowledge_card_memory_architecture
  - p01_kc_memory_scope
  - bld_instruction_consolidation_policy
  - bld_output_template_consolidation_policy
  - p01_kc_memory_summary
  - atom_22_memory_taxonomy
  - memory-summary-builder
  - consolidation-policy-builder
---

# Consolidation Policy: N04 Memory Consolidation Rules

## Purpose

Unconstrained memory accumulation is just hoarding. Consolidation converts
raw episodic data into distilled semantic knowledge while evicting noise.
This policy governs WHEN to consolidate, HOW to consolidate, and WHAT to preserve.

---

## Trigger Conditions

| Trigger | Condition | Action |
|---------|-----------|--------|
| Session end | Always | Compress session transcript -> episodic summary |
| Context overflow | > 80% context window used | Page least-important content to episodic |
| Duplicate detection | Similarity >= 0.95 between two KCs | Merge: keep higher quality, append unique facts |
| TTL expiry | Episodic record age > 90 days, score < 0.3 | Archive to cold storage or delete |
| Periodic sweep | Weekly cron | Deduplicate semantic corpus, score all orphans |
| Manual trigger | `/consolidate` command | Full consolidation cycle |
| Post-grid | After mission wave completion | Consolidate all nuclei learning records |

---

## Session Consolidation (Episodic Layer)

Runs at session end via `cex_hooks_native.py post-compact`.

### Steps

1. **Extract key facts** -- scan session transcript for novel entities, facts, procedures
2. **Score each fact** by: novelty (vs existing corpus), specificity, cross-nucleus relevance
3. **Discard noise** -- facts with score < 0.4 (casual conversation, repetition, artifacts)
4. **Write learning record** -- structured summary to `N04_knowledge/P11_feedback/learning_record_n04.md`
5. **Update entity memories** -- new entities or changed entities -> `P10_memory/p10_entity_*.md`
6. **Index session summary** -- embed and store in pgvector `session_memory`

### Session Summary Format
```yaml
session_id: {uuid}
date: {ISO 8601}
nucleus: n04
task_summary: "one sentence"
facts_extracted: N
entities_updated: N
procedures_learned: N
quality_gate: {passed|failed}
key_learnings:
  - fact 1
  - fact 2
```

---

## Semantic Deduplication Policy

Runs as part of weekly sweep or manual consolidation.

### Similarity Thresholds

| Similarity | Action |
|-----------|--------|
| >= 0.97 | Merge: identical content, keep latest version |
| 0.92-0.96 | Flag for human review: near-duplicate |
| 0.85-0.91 | Keep both: similar but distinct angles |
| < 0.85 | No action: distinct content |

### Merge Rules

1. Merged KC inherits the HIGHER quality score (or null if both null)
2. Merged KC version = max(v1, v2) bumped by patch (1.0.0 -> 1.0.1)
3. All unique facts from both versions preserved in merged body
4. Old KC redirects: frontmatter `deprecated: true`, `replaced_by: {new_id}`
5. Compile merged KC: `python _tools/cex_compile.py {path}`

---

## Knowledge Card Compression

When a KC cluster (>= 5 KCs on same domain) exists, N04 may create a
`memory_summary` that compresses the cluster into a single dense artifact.

### When to compress
- >= 5 KCs covering same narrow domain (e.g., 5 KCs on BM25 variations)
- Query recall shows all 5 are always retrieved together (co-occurrence > 80%)
- Individual KCs each below 8.5 quality

### How to compress
1. Load all KCs in cluster
2. Extract unique facts (deduplicate overlapping claims)
3. Write `memory_summary_{domain}.md` to P10_memory/
4. Mark original KCs as `consolidated: true`, reference memory_summary
5. Keep originals (never delete) -- memory_summary is a synthesis layer

---

## Procedural Memory Versioning

Procedures are never deleted -- they are versioned.

| Event | Action |
|-------|--------|
| Procedure improved | Append new version section with date |
| Procedure superseded | Mark `deprecated: true`, add `replaced_by` pointer |
| Procedure split | Create two new procedures, mark original as `split_into: [id1, id2]` |
| Procedure generalized | Promote to `N00_genesis/P10_memory/` for cross-nucleus use |

---

## TTL and Eviction Rules

### Episodic (session) memories

| Age | Usage Score | Action |
|-----|------------|--------|
| < 7 days | any | Keep |
| 7-30 days | > 0.5 | Keep |
| 7-30 days | <= 0.5 | Decay weight by 0.1/week |
| 30-90 days | > 0.3 | Keep, reduced weight |
| 30-90 days | <= 0.3 | Archive to `_archive/sessions/` |
| > 90 days | any | Delete (facts already promoted to semantic if valuable) |

### Entity memories

| Condition | Action |
|-----------|--------|
| Entity not referenced in 180 days | Mark `dormant: true` |
| Entity contradicted by newer source | Update with source citation, preserve history |
| Entity merged with another | Create `entity_alias` pointer |

---

## Quality Gate for Consolidation

Before consolidation commit, verify:
- [ ] No two KCs in output have similarity >= 0.97 (cex_retriever.py --deduplicate check)
- [ ] All merged KCs have compile-passing frontmatter
- [ ] learning_record appended for this session
- [ ] Entity memories updated for any new entities discovered
- [ ] Weekly sweep: cex_doctor.py reports 0 compile errors on P10_memory/

---

## Integration

| Tool | Role |
|------|------|
| `cex_memory_age.py` | Freshness decay calculation for episodic TTL |
| `cex_memory_update.py` | Memory decay + append + prune operations |
| `cex_retriever.py --deduplicate` | Similarity-based duplicate detection |
| `cex_compile.py` | Compile merged KCs after consolidation |
| `memory_architecture_n04.md` | Defines what each layer stores (policy consumes architecture) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_consolidation_policy]] | upstream | 0.38 |
| [[bld_output_template_memory_architecture]] | upstream | 0.28 |
| [[bld_knowledge_card_memory_architecture]] | upstream | 0.27 |
| [[p01_kc_memory_scope]] | upstream | 0.25 |
| [[bld_instruction_consolidation_policy]] | upstream | 0.25 |
| [[bld_output_template_consolidation_policy]] | upstream | 0.24 |
| [[p01_kc_memory_summary]] | related | 0.24 |
| [[atom_22_memory_taxonomy]] | related | 0.23 |
| [[memory-summary-builder]] | related | 0.23 |
| [[consolidation-policy-builder]] | related | 0.23 |
