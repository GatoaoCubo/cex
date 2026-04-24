---
quality: 9.1
quality: 8.3
id: p01_kc_autoresearch
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Autoresearch -- Autonomous Experiment Loop for Artifact Evolution"
version: 1.0.0
created: "2026-04-20"
updated: "2026-04-20"
author: n04_knowledge
domain: autonomous_improvement
tags: [autoresearch, karpathy, evolve, experiment, keep-discard, overnight, cluster]
tldr: "Karpathy's autoresearch loop mapped to CEX: cex_evolve.py modifies one artifact, scores it, keeps if improved or discards via git reset. Extended with cluster evolution (related artifacts evolve together) and diff tracking (hypothesis + delta per round)."
when_to_use: "When running overnight evolution loops, designing experiment harnesses, or reasoning about autonomous self-improvement"
keywords: [autoresearch, evolve, keep-discard, experiment, overnight, cluster, diff-log, scalar-metric]
density_score: 0.93
related:
  - p01_kc_autoresearch_loop
  - p01_kc_cross_reference
  - p01_kc_llm_wiki
  - p01_kc_experiment_driven_development
  - p12_wf_auto_evolve
  - p01_kc_knowledge_distillation
  - eval-metric-builder
  - p01_kc_quality_gates
  - p01_kc_gap_detection
  - p01_kc_optimizer
---

# Autoresearch

## Origin

Andrej Karpathy's [autoresearch](https://github.com/karpathy/autoresearch) pattern: give an AI agent one file to modify, one metric to optimize, and let it run experiments autonomously. Keep what improves, discard what does not.

## 3 Preconditions

1. **Clear scalar metric** -- one number, one direction (higher = better)
2. **Automated evaluation** -- no human in the loop during iterations
3. **Single modifiable target** -- scope constraint prevents cascading breakage

## 3-File Architecture

| Role | Karpathy | CEX Equivalent |
|------|----------|---------------|
| Goals + constraints | `program.md` | CLAUDE.md + spec + quality_gate |
| Modifiable target | `train.py` | Any .md artifact |
| Immutable evaluator | `prepare.py` | cex_score.py + cex_compile.py |
| Experiment ledger | git history | .cex/experiments/results.tsv |

## The Loop

```
LOOP:
  1. Analyze artifact -> form hypothesis
  2. Modify artifact (one .md file)
  3. Compile: cex_compile.py {path}
  4. Score: cex_score.py {path}
  5. IF quality_after > quality_before:
       git commit (KEEP)
       append to results.tsv
     ELSE:
       git restore (DISCARD)
       append to results.tsv with kept=false
  6. Log round to diff_log.jsonl
  7. REPEAT until interrupted or target quality reached
```

## CEX Implementation

| Component | Tool | Purpose |
|-----------|------|---------|
| Evolution engine | `cex_evolve.py` | Core loop: modify -> score -> keep/discard |
| Below-9 sweeper | `cex_evolve_below9.py` | Batch target: all artifacts with quality < 9.0 |
| Ollama variant | `cex_evolve_ollama.py` | Local model evolution (zero API cost) |
| Overnight harness | `_spawn/overnight_evolve.sh` | Unattended multi-hour runs |
| Experiment log | `.cex/experiments/results.tsv` | TSV ledger (grep-friendly, zero deps) |

## Cluster Evolution (W5 Extension)

Standard autoresearch evolves one file at a time. Cluster evolution evolves related artifacts together:

```
--cluster flag:
  1. Read artifact's related: field -> extract cluster (max 5 neighbors)
  2. Git snapshot ALL cluster files
  3. Evolve primary artifact
  4. Run cex_ripple.py on cluster (propagate changes)
  5. Score ALL cluster files
  6. IF average quality improved: keep ALL
  7. IF average quality dropped: discard ALL (git restore)
```

Cluster evolution prevents the scenario where improving one artifact degrades its neighbors. The unit of improvement is the cluster, not the file.

## Diff Tracking (W5 Extension)

Each round logs structured experiment data:

```json
{
  "timestamp": "ISO-8601",
  "filepath": "path/to/artifact.md",
  "round": 14,
  "hypothesis": "add cross-provider comparison table",
  "diff_summary": "added 1 table (5 rows), removed 2 filler paragraphs",
  "quality_before": 8.4,
  "quality_after": 8.9,
  "delta": 0.5,
  "kept": true,
  "affected_refs": ["p01_kc_universal_llm", "p01_kc_caching"]
}
```

Stored in `.cex/experiments/diff_log.jsonl` for aggregation.

## Convergence Behavior

| Phase | Rounds | Typical Delta | Dominant Strategy |
|-------|--------|---------------|-------------------|
| Quick wins | 1-5 | +0.3 to +1.0 | Add missing sections, fix frontmatter |
| Refinement | 6-15 | +0.1 to +0.3 | Add tables, tighten density, cross-refs |
| Plateau | 15+ | +0.0 to +0.1 | Diminishing returns, need human insight |

Artifacts below 7.0 typically reach 8.5 in 5-8 rounds. Reaching 9.0+ often requires cluster evolution or manual intervention.

## Anti-Patterns

| Anti-Pattern | Consequence | Fix |
|-------------|-------------|-----|
| Bad metric (subjective evaluation) | Confident optimization in wrong direction | Use structural scoring (cex_score.py) |
| Multiple files per round | Cannot attribute quality delta to specific change | One file, one hypothesis |
| No git snapshot | Cannot discard bad experiments | Always snapshot before modifying |
| Infinite loop without ceiling | Token burn with no improvement | Set max_rounds or delta_threshold |
| Ignoring cluster effects | Improving A degrades B | Use --cluster for connected artifacts |

## Industry Mapping

| CEX | Industry | Domain |
|-----|----------|--------|
| cex_evolve.py | Hyperparameter tuning loop | ML training |
| keep/discard | Accept/reject step | MCMC sampling |
| results.tsv | Experiment tracker | MLflow, W&B |
| --cluster | Population-based training | DeepMind PBT |
| --diff-log | Experiment lineage | DVC, MLflow |
| quality score | Objective function | Optimization theory |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_autoresearch_loop]] | upstream | 0.52 |
| [[p01_kc_cross_reference]] | sibling | 0.40 |
| [[p01_kc_llm_wiki]] | sibling | 0.38 |
| [[p01_kc_experiment_driven_development]] | upstream | 0.36 |
| [[p12_wf_auto_evolve]] | downstream | 0.32 |
| [[p01_kc_knowledge_distillation]] | sibling | 0.30 |
| [[eval-metric-builder]] | downstream | 0.28 |
| [[p01_kc_quality_gates]] | upstream | 0.27 |
| [[p01_kc_gap_detection]] | sibling | 0.25 |
| [[p01_kc_optimizer]] | sibling | 0.24 |
