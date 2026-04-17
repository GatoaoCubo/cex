---
id: p11_qg_knowledge_index
kind: quality_gate
pillar: P11
title: "Gate: knowledge_index"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: knowledge_index
quality: 9.0
tags: [quality-gate, knowledge-index, P11, P10, governance, search, retrieval, hybrid-search]
tldr: "Gates for knowledge_index artifacts — search index configs combining BM25, FAISS, or hybrid retrieval."
density_score: 0.87
llm_function: GOVERN
---
# Gate: knowledge_index
## Definition
| Field     | Value                                                  |
|-----------|--------------------------------------------------------|
| metric    | algorithm completeness + freshness policy coverage     |
| threshold | 8.0                                                    |
| operator  | >=                                                     |
| scope     | all knowledge_index artifacts (P10)                        |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = index unreachable at query time |
| H02 | id matches `^p10_bi_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "knowledge_index" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All required fields present: id, kind, pillar, version, created, updated, author, algorithm, scope, corpus_type, rebuild_schedule, freshness_max_days, quality, tags, tldr | Completeness |
| H07 | algorithm in [bm25, faiss, hybrid] | Only supported retrieval algorithms |
| H08 | corpus_type in [text, vector, structured] | Valid corpus classification |
| H09 | rebuild_schedule in [on_change, hourly, daily, weekly, manual] | Valid schedule value |
| H10 | freshness_max_days is non-negative integer | Freshness policy must be numeric |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty | 1.0 |
| S02 | tags is list, len >= 3, includes "knowledge-index" | 0.5 |
| S03 | Algorithm Config section has parameters specific to chosen algorithm | 1.0 |
| S04 | Filters section has >= 2 entries with type and condition | 1.0 |
| S05 | Ranking section has >= 2 factors with explicit weights | 1.0 |
| S06 | Rebuild section specifies both schedule and trigger event | 1.0 |
| S07 | Monitoring section has >= 2 metrics with alert thresholds | 0.5 |
| S08 | scope boundary is specific (names included/excluded paths) | 1.0 |
| S09 | density_score >= 0.80 | 1.0 |
| S10 | No generic retrieval advice (content must be config, not tutorial) | 1.0 |
Weights sum: 9.0. Normalize: divide each by 9.0 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as reference search index configuration |
| >= 8.0 | PUBLISH — active retrieval index |
| >= 7.0 | REVIEW — complete ranking weights or monitoring thresholds |
| < 7.0  | REJECT — algorithm config missing or scope undefined |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Critical search gap requiring temporary index before full spec |
| approver | p10-chief |
| audit_trail | Log in records/audits/ with retrieval gap description and timestamp |
| expiry | 72h — full algorithm config required before expiry |
| never_bypass | H01 (YAML), H05 (quality null) |
