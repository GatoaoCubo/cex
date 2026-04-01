---
id: spec_autoresearch_assimilation
title: "AutoResearch Pattern Assimilation"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
status: EXECUTED
source: "https://github.com/karpathy/autoresearch + video tutorial"
quality: null
---

# Spec: AutoResearch Pattern Assimilation

## Core Insight

Karpathy's AutoResearch = **autonomous experiment loop**:
- 3-file architecture: `program.md` (human goals) + `train.py` (agent modifies) + `prepare.py` (immutable metric)
- Loop: hypothesis → modify → run → measure → keep/discard → repeat
- Never stop. Git-based versioning. One scalar metric.

**Key quote from video**: "If you can score it, you can auto-research it."

## CEX Already Has

| AutoResearch concept | CEX equivalent | Status |
|---------------------|----------------|--------|
| `program.md` | CLAUDE.md + specs + decision manifest | ✅ exists |
| `prepare.py` (metric) | quality_gate + scoring_rubric + cex_score.py | ✅ exists |
| `train.py` (modifiable) | Any .md artifact | ✅ exists |
| `results.tsv` | `.cex/quality/latest_snapshot.json` | ✅ exists |
| `git commit` on success | cex_hooks.py + git | ✅ exists |
| `git reset` on failure | Not automated | ❌ gap |
| Autonomous loop | cex_auto.py (scan/plan/cycle) | ⚠️ partial |
| Time-boxed experiments | Not implemented | ❌ gap |
| Never-stop protocol | Not implemented | ❌ gap |

## What CEX is MISSING

The **glue**: an autonomous loop that connects score → decide → iterate on a SINGLE artifact
until it crosses a quality threshold, using git as the experiment ledger.

## Deliverables

### Wave 1: Core Tool (1 file)
- `_tools/cex_evolve.py` — The autonomous experiment loop for CEX

### Wave 2: Knowledge Cards (2 files)
- `P01_knowledge/library/domain/patterns/kc_autoresearch_loop.md`
- `P01_knowledge/library/domain/patterns/kc_experiment_driven_development.md`

### Wave 3: Integration (2 files)
- `N07_admin/orchestration/auto/wf_auto_evolve.md` — REWRITE (add autoresearch loop)
- `.claude/commands/evolve.md` — new `/evolve` command

### Wave 4: Score + Consolidate
- Score all new artifacts from N01/N04 verticalization (40 files)
- Score Wave 1-3 deliverables
- Compile, doctor, commit
