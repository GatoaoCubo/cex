---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for router validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: router

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p02_router_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "router" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 14 required fields present (id, kind, pillar, version, created, updated, author, routes_count, fallback_route, confidence_threshold, domain, quality, tags, tldr) | Completeness |
| H07 | routes_count matches actual rows in Routes table | Frontmatter-body integrity |
| H08 | confidence_threshold between 0.0 and 1.0 | Valid probability range |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty, not filler | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "router" | 0.5 | 10 |
| S03 | Routes table has >= 2 rows with all columns filled | 1.0 | 10 |
| S04 | Decision Logic section present with algorithm description | 1.0 | 10 |
| S05 | Fallback section present with concrete destination | 1.0 | 10 |
| S06 | Escalation section present with trigger and action | 0.5 | 10 |
| S07 | Each route has unique pattern (no duplicates) | 1.0 | 10 |
| S08 | fallback_route is valid satellite name or "escalate" | 0.5 | 10 |
| S09 | density_score >= 0.80 | 0.5 | 10 |
| S10 | No filler phrases ("this document", "in summary", "helps route") | 1.0 | 10 |

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
Primary: validate_artifact.py --kind router [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Routing domain identified with clear task categories
- [ ] All destination satellites/agents listed and valid
- [ ] No existing router for this domain (brain_query checked)
- [ ] Fallback route defined (not blank)
- [ ] Confidence threshold set (default 0.7 if unsure)
