---
id: spec_autoresearch_assimilation
title: "AutoResearch Pattern Assimilation"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
status: EXECUTED
source: "https://github.com/karpathy/autoresearch + video tutorial"
quality: 9.0
density_score: 1.0
updated: "2026-04-07"
domain: "system specification"
tldr: "Defines the artifact specification for autoresearch pattern assimilation, with structural rules, validation gates, and integration points."
---

# Spec: AutoResearch Pattern Assimilation

## Core Insight

Karpathy's AutoResearch = **autonomous experiment loop**:
1. 3-file architecture: `program.md` (human goals) + `train.py` (agent modifies) + `prepare.py` (immutable metric)
2. Loop: hypothesis → modify → run → measure → keep/discard → repeat
3. Never stop. Git-based versioning. One scalar metric.

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
1. `_tools/cex_evolve.py` — The autonomous experiment loop for CEX

### Wave 2: Knowledge Cards (2 files)
1. `P01_knowledge/library/domain/patterns/kc_autoresearch_loop.md`
2. `P01_knowledge/library/domain/patterns/kc_experiment_driven_development.md`

### Wave 3: Integration (2 files)
1. `N07_admin/P12_orchestration/auto/wf_auto_evolve.md` — REWRITE (add autoresearch loop)
2. `.claude/commands/evolve.md` — new `/evolve` command

### Wave 4: Score + Consolidate
1. Score all new artifacts from N01/N04 verticalization (40 files)
2. Score Wave 1-3 deliverables
3. Compile, doctor, commit

## Cross-References

1. **Pillar**:  (System)
2. **Kind**: `artifact`
3. **Artifact ID**: `spec_autoresearch_assimilation`
4. **Tags**: []

## Integration Points

| Component | Role |
|-----------|------|
| Pillar  | System domain |
| Kind `artifact` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Artifact Metadata

```yaml
kind: artifact
pillar: 
pipeline: 8F
scoring: hybrid_3_layer
compilation: cex_compile
```
