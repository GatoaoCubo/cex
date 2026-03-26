---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for rag_source validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: rag_source

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses without error | Broken YAML = broken artifact |
| H02 | id matches `^p01_rs_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on exact match |
| H04 | kind == "rag_source" | Type integrity |
| H05 | quality == null | Never self-score — pipeline scores |
| H06 | Required fields present: id, kind, url, domain, last_checked | Minimum viable pointer |
| H07 | Body <= 1024 bytes | Size constraint from _schema.yaml |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "rag-source" | 0.5 | 10 |
| S03 | URL format valid (starts with https:// or http://) | 1.5 | 10 |
| S04 | Source Description section present and non-empty | 1.0 | 10 |
| S05 | Freshness Policy section present with re-check interval | 1.0 | 10 |
| S06 | Body contains no extracted content (pointer only) | 1.5 | 10 |
| S07 | domain matches CEX taxonomy (not freeform string) | 0.5 | 10 |

## Scoring Formula

```text
hard_pass = all 7 HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5 (all HARD + 95% SOFT)
PUBLISH: >= 8.0 (all HARD + 80% SOFT)
REVIEW:  >= 7.0 (all HARD + 70% SOFT)
REJECT:  < 7.0 or any HARD fail
```

## Automation
Primary: `validate_artifact.py --kind rag_source --file p01_rs_{slug}.md` [PLANNED]
Interim: validate manually against each gate above before delivering.

## Pre-Production Checklist
- [ ] URL verified accessible (not 404)
- [ ] brain_query checked — no duplicate rag_source for same URL
- [ ] id prefix is p01_rs_ (not rs_, not rag_source_)
- [ ] quality field is YAML null (not string "null", not 0, not omitted)
- [ ] Body contains no extracted content paragraphs
- [ ] last_checked set to today
- [ ] Both .md and .yaml files named identically
