---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for fallback_chain validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: fallback_chain

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p02_fc_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "fallback_chain" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 15 required fields present (id, kind, pillar, version, created, updated, author, steps_count, timeout_per_step_ms, quality_threshold, domain, quality, tags, tldr) | Completeness |
| H07 | steps_count matches rows in Chain table AND steps_count >= 2 | Chain integrity |
| H08 | Steps ordered by decreasing capability (primary first, minimum last) | Graceful degradation |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty, not filler | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "fallback_chain" | 0.5 | 10 |
| S03 | Chain table has >= 2 rows with all columns filled | 1.0 | 10 |
| S04 | Degradation Logic section present with trigger conditions | 1.0 | 10 |
| S05 | Circuit Breaker section present with threshold and recovery | 1.0 | 10 |
| S06 | Cost Analysis section present with per-step costs | 0.5 | 10 |
| S07 | Each step has valid provider (anthropic, openai, google, local) | 0.5 | 10 |
| S08 | timeout_per_step_ms > 0 for every step | 0.5 | 10 |
| S09 | density_score >= 0.80 | 0.5 | 10 |
| S10 | No filler phrases ("this document", "robust mechanism", "gracefully") | 1.0 | 10 |

## Scoring Formula
```text
hard_pass = all 8 HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5 (all HARD + 95% SOFT)
PUBLISH: >= 8.0 (all HARD + 80% SOFT)
REVIEW:  >= 7.0 (all HARD + 70% SOFT)
REJECT:  < 7.0 or any HARD fail
```

## Automation
Primary: validate_artifact.py --kind fallback_chain [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Models identified with pricing and capability tier
- [ ] No existing fallback_chain for this domain (brain_query checked)
- [ ] Steps ordered from highest to lowest capability
- [ ] Timeout per step defined (not zero or negative)
- [ ] Circuit breaker threshold set
