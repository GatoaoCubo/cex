---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for daemon validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: daemon

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p04_daemon_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "daemon" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | Required fields present: id, kind, pillar, version, created, updated, author, name, schedule, restart_policy, signal_handling, quality, tags, tldr | Completeness |
| H07 | body has ## Overview, ## Lifecycle, ## Signal Handling, ## Monitoring | Core sections required |
| H08 | body <= 1024 bytes | Compact daemon spec |
| H09 | schedule is concrete: cron expr, interval, or "continuous" (not vague) | Unambiguous lifecycle |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "daemon" | 0.5 | 10 |
| S03 | restart_policy is valid enum: always, on_failure, never | 1.0 | 10 |
| S04 | signal_handling includes SIGTERM behavior | 1.0 | 10 |
| S05 | ## Signal Handling has table with >= 3 signals | 0.5 | 10 |
| S06 | health_check field present with concrete strategy | 1.0 | 10 |
| S07 | resource_limits specified (memory, CPU, or fd) | 0.5 | 10 |
| S08 | monitoring field present with metrics or alerting | 0.5 | 10 |
| S09 | graceful_shutdown described (not just "exit") | 1.0 | 10 |
| S10 | density_score >= 0.80 (no filler phrases) | 0.5 | 10 |
| S11 | description <= 200 chars and non-generic | 0.5 | 10 |
| S12 | max_restarts defined with window (circuit breaker) | 0.5 | 10 |

## Scoring Formula
```text
hard_pass = all 9 HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5 (all HARD + 95% SOFT)
PUBLISH: >= 8.0 (all HARD + 80% SOFT)
REVIEW:  >= 7.0 (all HARD + 70% SOFT)
REJECT:  < 7.0 or any HARD fail
```

## Pre-Production Checklist
- [ ] Background task identified (not suitable for one-shot cli_tool)
- [ ] Schedule determined: cron, interval, or continuous
- [ ] Restart policy selected based on failure tolerance
- [ ] No existing daemon for this purpose (brain_query checked)
- [ ] Signal handling defined with at least SIGTERM behavior
