---
id: p11_sil_n04_knowledge
kind: self_improvement_loop
pillar: P11
nucleus: n04
title: "Self-Improvement Loop -- N04 Knowledge Evolution Protocol"
version: "1.0.0"
quality: null
tags: [self_improvement_loop, n04, knowledge_evolution, retrieval_quality, P11]
domain: knowledge management
status: active
created: "2026-04-17"
updated: "2026-04-17"
author: n04_knowledge
tldr: "N04 autonomous knowledge quality evolution loop: scan corpus -> score artifacts -> identify gaps -> build improvements -> validate -> deploy. Runs on schedule or triggered by quality degradation signals."
density_score: null
---

# Self-Improvement Loop: N04 Knowledge Evolution Protocol

## Purpose

A nucleus that cannot improve itself will stagnate. N04's Knowledge Gluttony demands
continuous expansion and quality elevation. This loop makes N04 STRONGER with every run.

---

## Loop Architecture

```
SENSOR -> EVALUATOR -> MODIFIER -> VALIDATOR -> DEPLOYER
   ^                                                |
   |________________ FEEDBACK _____________________|
```

### 1. SENSOR -- Scan and Measure

**Input**: current corpus state
**Output**: quality distribution, gap map, coverage report

```bash
# Scan all N04 artifacts
python _tools/cex_doctor.py --nucleus n04

# Score artifacts below quality threshold
python _tools/cex_score.py --scan N04_knowledge/ --below 8.0

# Coverage gap analysis
python _tools/cex_retriever.py --coverage-report \
  --nucleus n04 --output N04_knowledge/P05_output/output_gap_report.md
```

**Metrics tracked**:
- Artifacts with quality: null (unscored) -- target: < 20% of total
- Artifacts with quality < 8.0 -- target: < 10% of total
- Pillars below target artifact count -- per handoff targets
- Retrieval MRR@10 -- target: >= 0.83 (from memory_benchmark_n04.md)

---

### 2. EVALUATOR -- Identify Improvement Targets

**Priority matrix**:

| Priority | Condition | Action |
|---------|-----------|--------|
| P1 (CRITICAL) | MRR@10 drops below 0.75 | Fix retrieval config immediately |
| P2 (HIGH) | Missing P06 schema artifacts | Build missing contracts |
| P3 (HIGH) | P10 < 14 artifacts | Build missing memory types |
| P4 (MEDIUM) | Artifact quality < 8.0 | Rewrite or improve artifact |
| P5 (MEDIUM) | Pillar below target count | Build gap-filling artifacts |
| P6 (LOW) | Artifacts not compiled | Run cex_compile.py |
| P7 (LOW) | Stale entity_memory | Update entity facts |

**Combo completeness check** (from spec_nucleus_self_assembly.md):
- COMBO A (RAG Architecture): score 4/5 -- missing: agentic_rag
- COMBO B (Taxonomy Engine): score 3/5 -- missing: knowledge_graph (KC), citation
- COMBO C (Docs Factory): score 3/5 -- missing: contributor_guide, course_module
- COMBO D (Memory Architecture): score 5/5 -- COMPLETE after this session
- COMBO E (Knowledge Schema): score 3/3 -- COMPLETE after this session

---

### 3. MODIFIER -- Apply Improvements

**Heuristic improvements** (fast, no LLM):
- Fix frontmatter issues: missing fields, wrong kind name, null where required
- Add missing `tldr` fields
- Fix naming convention violations
- Update stale `updated` dates

```bash
python _tools/cex_hygiene.py --fix N04_knowledge/
```

**Agent improvements** (LLM-required):
- Rewrite artifact body for quality < 7.5
- Fill content gaps identified by evaluator
- Build new artifacts for gap pillars
- Update entity_memory with newly discovered entities

```bash
python _tools/cex_evolve.py \
  --nucleus n04 \
  --target 9.0 \
  --max-rounds 2 \
  --strategy heuristic_first
```

---

### 4. VALIDATOR -- Quality Gate

Before deploying any improvement:
1. Frontmatter parses without errors
2. `quality: null` (never self-score)
3. `cex_compile.py {path}` exits 0
4. `cex_doctor.py --check {path}` PASS
5. New artifact does not create duplicate (similarity < 0.95)

```bash
python _tools/cex_compile.py N04_knowledge/ && \
python _tools/cex_doctor.py --nucleus n04
```

---

### 5. DEPLOYER -- Persist and Signal

```bash
# Stage all N04 changes
git add N04_knowledge/

# Commit with improvement summary
git commit -m "[N04] self_improvement_loop: {n} artifacts improved, MRR {before}->{after}"

# Signal completion to N07
python -c "
from _tools.signal_writer import write_signal
write_signal('n04', 'improvement_complete', 9.0)
"
```

---

## Schedule

| Trigger | Frequency | Depth |
|---------|-----------|-------|
| Session end | Every session | Heuristic pass only |
| Weekly cron | Every Sunday 03:00 | Full scan + heuristic |
| Monthly | First Sunday | Full scan + agent improvements |
| Quality alert | When MRR < 0.75 | Emergency mode -- retrieval fix first |
| Post-dispatch | After N07 wave | Consolidate new artifacts |

---

## Safety Guards

1. **No self-scoring**: `quality: null` enforced -- loop never writes quality scores
2. **No mass deletion**: loop only ADDS or IMPROVES, never deletes existing artifacts
3. **Similarity check before add**: prevents duplicating existing artifacts
4. **Max rounds**: `--max-rounds 2` prevents infinite improvement loops
5. **Git checkpoint**: commit before each improvement batch (rollback available)
6. **Human gate for P1 (CRITICAL)**: retrieval config changes require N07 approval

---

## Evolution Metrics (tracked over time)

| Date | Artifacts | Avg Quality | MRR@10 | Gaps Closed |
|------|-----------|------------|--------|-------------|
| 2026-04-17 | 100 | null (unscored) | 0.83 (baseline) | P06: +3, P10: +8 |
