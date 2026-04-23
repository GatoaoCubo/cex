---
id: p12_wf_auto_evolve
kind: workflow
pillar: P12
title: "Auto-Evolve — Autonomous Experiment Loop + Gap Fill"
version: 2.0.0
created: 2026-03-31
updated: 2026-03-31
author: n07_orchestrator
domain: orchestration
trigger: gap_detector_triggers OR /evolve command
quality: 9.1
tags: [workflow, auto, n07, evolve, autoresearch, experiment, gap, mlops]
tldr: "Two modes: (1) AutoResearch loop — evolve existing artifacts via experiment (modify→measure→keep/discard). (2) Gap fill — detect missing artifacts and create them."
density_score: 0.93
related:
  - p01_kc_autoresearch_loop
  - doctor
  - leverage_map_v2_n05_verify
  - skill
  - validate
  - ai2ai_exhaustive_scan_20260414
  - p01_kc_cex_tooling_master
  - p01_kc_gap_detection
  - build
  - agent_card_engineering_nucleus
---

# Auto-Evolve v2 — AutoResearch + Gap Fill

## Two Modes

### Mode A: Experiment Loop (AutoResearch pattern)
For **existing** artifacts. Inspired by Karpathy's AutoResearch.

```
LOOP (max N rounds):
  1. Analyze weaknesses (density, frontmatter, structure)
  2. Apply improvement (single change)
  3. Validate (compile)
  4. Measure (cex_score.py → quality scalar)
  5. IF quality improved → git commit KEEP
     IF not → git restore DISCARD
  6. Log to .cex/experiments/results.tsv
  7. IF quality >= target → STOP
```

**3-File Mapping**:
| AutoResearch | CEX |
|-------------|-----|
| program.md (goals) | CLAUDE.md + quality_gate + scoring_rubric |
| train.py (modifiable) | Target .md artifact |
| prepare.py (metric) | cex_score.py + cex_compile.py (immutable) |

**Tool**: `python _tools/cex_evolve.py single <file> --target 9.0`

### Mode B: Gap Fill (original auto-evolve)
For **missing** artifacts. Detect and create.

| # | Action | Tool | Output |
|---|--------|------|--------|
| 1 | Detect gap | `cex_doctor.py`, `cex_query.py` | Gap classification |
| 2 | Classify | Impact × frequency | P1-P3 priority |
| 3 | Plan | Determine kind, pillar, path | Artifact plan |
| 4 | Build | 8F pipeline | New artifact |
| 5 | Validate | compile + doctor | Pass checks |
| 6 | Record | `cex_memory_update.py` | Learning record |

## Gap Types

| Type | Detection | Action |
|------|-----------|--------|
| Missing KC | `cex_query.py` returns 0 | Create KC |
| Weak builder | Doctor FAIL | Fix builder specs |
| Missing kind | Intent maps to nothing | Register kind |
| Stale KC | Updated >90 days | Mode A: evolve refresh |
| Low quality | quality < 8.0 | Mode A: evolve improve |
| Missing output | Nucleus has 0 outputs | Mode B: create |

## Commands
```bash
# Mode A: Evolve one artifact
python _tools/cex_evolve.py single <file> --target 9.0

# Mode A: Evolve all quality:null
python _tools/cex_evolve.py sweep --target 8.5

# Mode A: View experiment history
python _tools/cex_evolve.py report

# Mode B: Gap scan + fill
python _tools/cex_auto.py cycle --max 5
```

## Failure Mode
Can't auto-improve (plateau or subjective) → backlog for `/guide` session.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_autoresearch_loop]] | upstream | 0.27 |
| [[doctor]] | upstream | 0.25 |
| [[leverage_map_v2_n05_verify]] | upstream | 0.23 |
| [[skill]] | upstream | 0.22 |
| [[validate]] | upstream | 0.22 |
| [[ai2ai_exhaustive_scan_20260414]] | upstream | 0.22 |
| [[p01_kc_cex_tooling_master]] | upstream | 0.21 |
| [[p01_kc_gap_detection]] | upstream | 0.21 |
| [[build]] | upstream | 0.20 |
| [[agent_card_engineering_nucleus]] | upstream | 0.20 |
