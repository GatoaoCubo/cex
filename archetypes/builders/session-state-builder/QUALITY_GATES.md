---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for session_state validation
pattern: HARD gates block publish, SOFT gates improve operational quality
---

# Quality Gates: session_state

## HARD Gates

| Gate | Check | Why |
|------|-------|-----|
| H01 | filename matches `p10_ss_{session}.yaml` | namespace compliance |
| H02 | payload parses as valid YAML | machine readability |
| H03 | all required fields present: id, kind, lp, version, created, updated, author, session_id, agent, status, started_at, domain, quality, tags, tldr | completeness |
| H04 | `kind` is literal `session_state` | type integrity |
| H05 | `status` in (`active`, `paused`, `completed`, `aborted`) | lifecycle contract |
| H06 | `quality` is null | never self-score |
| H07 | payload size <= 3072 bytes | schema constraint |
| H08 | no persistent fields: no `routing_decisions`, no `accumulated_scores`, no `learned_patterns` | boundary against runtime_state and learning_record |
| H09 | `started_at` is ISO 8601 string | temporal integrity |

## SOFT Gates

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | agent value is lowercase slug | 0.5 | 10 |
| S02 | session_id is unique and descriptive | 0.5 | 10 |
| S03 | optional fields are omitted when unknown | 0.5 | 10 |
| S04 | `active_tasks` and `completed_tasks` are short and specific | 0.5 | 10 |
| S05 | `error_count` matches `errors` length when both exist | 0.5 | 10 |
| S06 | `ended_at` appears only on completed/aborted sessions | 1.0 | 10 |
| S07 | payload stays <= 2048 bytes when feasible | 0.5 | 10 |
| S08 | checkpoints have both label and timestamp | 0.5 | 10 |
| S09 | tldr is <= 160 characters and informative | 1.0 | 10 |

## Scoring Formula
```text
hard_pass = all 9 HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5
PUBLISH: >= 8.0
REVIEW:  >= 7.0
REJECT:  < 7.0 or any HARD fail
```

## Pre-Publish Checklist
- [ ] filename uses `p10_ss_` prefix
- [ ] required fields present
- [ ] no runtime_state or learning_record drift
- [ ] YAML remains compact and parseable
