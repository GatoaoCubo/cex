---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for signal validation
pattern: HARD gates block publish, SOFT gates improve operational quality
---

# Quality Gates: signal

## HARD Gates

| Gate | Check | Why |
|------|-------|-----|
| H01 | filename matches `p12_sig_{event}.json` | namespace compliance |
| H02 | payload parses as JSON object | machine readability |
| H03 | `satellite` is non-empty string | emitter identity |
| H04 | `status` in (`complete`, `error`, `progress`) | runtime contract |
| H05 | `quality_score` is numeric and within `0.0-10.0` | score integrity |
| H06 | `timestamp` is ISO 8601 string | event ordering |
| H07 | payload size <= 4096 bytes | schema constraint |
| H08 | payload contains no instruction fields (`steps`, `scope_fence`, `tasks`) | boundary against handoff |
| H09 | payload contains no routing fields (`keywords`, `fallback_sat`, `model`) | boundary against dispatch_rule |

## SOFT Gates

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | satellite value is lowercase slug | 0.5 | 10 |
| S02 | event slug and payload status semantically align | 0.5 | 10 |
| S03 | optional fields are omitted when unknown | 0.5 | 10 |
| S04 | `task` is short and specific | 0.5 | 10 |
| S05 | `artifacts_count` matches `artifacts` length when both exist | 0.5 | 10 |
| S06 | `progress_pct` appears only on `progress` signals | 1.0 | 10 |
| S07 | payload stays <= 1024 bytes when feasible | 0.5 | 10 |
| S08 | message is concise and machine-safe | 0.5 | 10 |
| S09 | payload adds useful automation hints (`commit_hash`, `artifacts`, `error_code`) without bloat | 1.0 | 10 |

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
- [ ] filename uses `p12_sig_` prefix
- [ ] required fields present
- [ ] no handoff or dispatch_rule drift
- [ ] JSON remains compact
