---
id: p11_rc_n04_knowledge
kind: regression_check
8f: F7_govern
pillar: P07
nucleus: n04
title: "Regression Check -- N04 Retrieval and Knowledge Quality"
version: "1.0.0"
quality: 9.1
tags: [regression_check, n04, retrieval, quality, MRR, P11]
domain: knowledge management
status: active
created: "2026-04-17"
updated: "2026-04-17"
author: n04_knowledge
tldr: "Regression detection suite for N04: checks retrieval metrics (MRR, NDCG, latency), corpus integrity, and artifact quality distribution against baselines from memory_benchmark_n04.md."
density_score: null
related:
  - p07_regression_check
  - p11_qg_knowledge
  - p07_regression_check_operations
  - regression-check-builder
  - p07_regcheck_latency_baseline
  - p11_qg_admin_orchestration
  - bld_collaboration_regression_check
  - p07_bm_builder_nucleus
  - bld_examples_regression_check
  - doctor
---

# Regression Check: N04 Retrieval and Knowledge Quality

## Purpose

Changes to embedding models, chunking strategies, or corpus composition can silently
degrade retrieval quality. This regression check suite detects those regressions before
they reach production queries.

---

## Check Suite

### RC-01: MRR@10 Regression

```bash
python _tools/cex_retriever.py --mrr \
  --queries N04_knowledge/P07_evals/eval_dataset_n04.md \
  --mode hybrid_rerank \
  --threshold 0.75

# PASS: MRR@10 >= 0.75
# FAIL: MRR@10 < 0.75 -> alert N07, do not deploy embedding changes
```

**Baseline**: 0.83 | **Alert threshold**: 0.75 | **Revert threshold**: < 0.70

---

### RC-02: Corpus Coverage Check

```bash
python _tools/cex_doctor.py --check-index --nucleus n04

# PASS: >= 95% of N04 artifacts are indexed
# FAIL: < 95% indexed -> run cex_compile.py --all then reindex
```

**Baseline**: 100% | **Alert threshold**: < 95%

---

### RC-03: Compile Error Check

```bash
python _tools/cex_compile.py N04_knowledge/ --check-only

# PASS: 0 compile errors
# FAIL: any error -> fix frontmatter before commit
```

**Baseline**: 0 errors | **Alert threshold**: any error

---

### RC-04: Duplicate Detection

```bash
python _tools/cex_retriever.py --deduplicate \
  --corpus N04_knowledge/ \
  --threshold 0.95

# PASS: 0 near-duplicate pairs
# FAIL: pairs found -> merge per consolidation_policy_n04.md
```

**Baseline**: 0 duplicates | **Alert threshold**: any pair >= 0.97 similarity

---

### RC-05: Quality Distribution Check

```bash
python _tools/cex_score.py --scan N04_knowledge/ \
  --report-distribution

# PASS: < 10% of scored artifacts below 8.0
# WARN: 10-20% below 8.0 -> flag for improvement loop
# FAIL: > 20% below 8.0 -> trigger full self_improvement_loop_n04.md run
```

---

### RC-06: Retrieval Latency Check

```bash
python _tools/cex_retriever.py --latency-check \
  --mode hybrid_rerank \
  --sample 10 \
  --threshold-ms 1000

# PASS: p95 latency < 1000ms
# FAIL: p95 > 1000ms -> check backend availability, consider fallback
```

**Baseline**: 480ms | **Alert threshold**: > 1000ms

---

## Regression Check Schedule

| Check | Frequency | Trigger |
|-------|-----------|---------|
| RC-01 (MRR) | Before any embedding config change | Pre-change gate |
| RC-02 (Coverage) | After every compile --all | Post-commit hook |
| RC-03 (Compile) | Every session end | Automatic |
| RC-04 (Dedup) | Weekly | Cron |
| RC-05 (Quality) | Monthly | Cron |
| RC-06 (Latency) | Before production deployment | Release gate |

---

## Regression Response Protocol

| Severity | Condition | Response |
|---------|-----------|---------|
| CRITICAL | MRR drops > 15% | Revert embedding change, escalate to N07 |
| HIGH | Corpus coverage < 95% | Run full reindex immediately |
| HIGH | > 5 compile errors | Fix all before next commit |
| MEDIUM | Quality distribution degrades | Queue for self_improvement_loop |
| LOW | 1-3 duplicates | Flag for next consolidation run |

---

## Integration

| Artifact | Role |
|---------|------|
| `memory_benchmark_n04.md` | Baseline values for all RC checks |
| `eval_dataset_n04.md` | Test queries for RC-01 |
| `self_improvement_loop_n04.md` | Response action when RC-05 fails |
| `consolidation_policy_n04.md` | Response action when RC-04 fails |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p07_regression_check]] | sibling | 0.33 |
| [[p11_qg_knowledge]] | downstream | 0.26 |
| [[p07_regression_check_operations]] | sibling | 0.25 |
| [[regression-check-builder]] | related | 0.25 |
| [[p07_regcheck_latency_baseline]] | sibling | 0.25 |
| [[p11_qg_admin_orchestration]] | downstream | 0.24 |
| [[bld_collaboration_regression_check]] | downstream | 0.23 |
| [[p07_bm_builder_nucleus]] | related | 0.23 |
| [[bld_examples_regression_check]] | related | 0.23 |
| [[doctor]] | downstream | 0.22 |
