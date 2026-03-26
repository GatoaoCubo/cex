---
lp: P11
llm_function: GOVERN
purpose: Quality gates for knowledge_card validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
source: validate_kc.py v2.0 (direct code alignment)
---

# Quality Gates: knowledge_card

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses without error | Broken YAML = broken artifact |
| H02 | id == filename stem | Brain search relies on this |
| H03 | id matches `^p01_kc_[a-z][a-z0-9_]+$` | Namespace compliance |
| H04 | type == "knowledge_card" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 13 required fields present and non-empty | Completeness |
| H07 | tags is list (not string) | YAML type safety |
| H08 | body size 200-5120 bytes | Size bounds |
| H09 | no internal paths (records/, .claude/, /home/) | Portability |
| H10 | author != STELLA | STELLA orchestrates, never authors |

## SOFT Gates (contribute to score, 20 checks)

| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty | 1.0 |
| S02 | tldr standalone (no "this document/kc" refs) | 1.0 |
| S03 | title 5-100 chars | 1.0 |
| S04 | version is semver X.Y.Z | 1.0 |
| S05 | created/updated are YYYY-MM-DD | 1.0 |
| S06 | >= 4 sections in body | 1.0 |
| S07 | largest section >= 30% of body | 1.0 |
| S08 | no thin sections (< 3 non-empty lines) | 1.0 |
| S09 | no filler phrases | 1.0 |
| S10 | all bullets <= 80 chars | 1.0 |
| S11 | has tables | 1.0 |
| S12 | has code blocks | 1.0 |
| S13 | has external URLs (https://) | 1.0 |
| S14 | references other CEX artifacts (p\d{2}_) | 1.0 |
| S15 | data_source field present and non-null | 1.0 |
| S16 | keywords list >= 2 items | 1.0 |
| S17 | long_tails list >= 1 item | 1.0 |
| S18 | axioms list >= 1 item | 1.0 |
| S19 | no duplicate sentences (Jaccard >= 0.85) | 1.0 |
| S20 | linked_artifacts has primary + related keys | 1.0 |

## Scoring Formula
```
hard_pass = all 10 HARD gates pass
soft_score = (soft_passed / soft_total) * 10
final = hard_pass ? soft_score : 0

GOLDEN:     >= 9.5  (all HARD + 19/20 SOFT)
PUBLISH:    >= 8.0  (all HARD + 16/20 SOFT)
ACCEPTABLE: >= 7.0  (all HARD + 14/20 SOFT)
NEEDS_WORK: < 7.0   (all HARD pass, SOFT low)
REJECTED:   any HARD fail
```

## Automation
Primary: `python _tools/validate_kc.py <file>` (ACTIVE)
Flags: `--json` (machine), `--summary` (batch overview)

## Pre-Production Checklist
- [ ] Topic identified, not duplicate (brain_query check)
- [ ] Sources gathered with URLs
- [ ] KC type chosen (domain_kc or meta_kc)
- [ ] Body density estimated >= 0.80
