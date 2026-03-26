---
lp: P11
llm_function: GOVERN
purpose: Quality gates for knowledge_card validation (aligned with validate_kc.py v2.0)
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
source: _tools/validate_kc.py v2.0
---

# Quality Gates: knowledge_card

## HARD Gates (block publish if ANY fails)

| Gate | Check | Detail |
|------|-------|--------|
| H01 | YAML frontmatter parses without error | Broken YAML = broken artifact |
| H02 | id == filename stem | Brain search relies on id-file match |
| H03 | id matches `p\d{2}_kc_[a-z][a-z0-9_]+` | Namespace compliance |
| H04 | type == "knowledge_card" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 12 required fields present (excl quality) | Completeness |
| H07 | tags is list (not string) | YAML type correctness |
| H08 | body 200-5120 bytes | Size bounds |
| H09 | no internal paths (records/, .claude/, /home/) | Portability |
| H10 | author != "STELLA" | STELLA orchestrates, never authors |

## SOFT Gates (contribute to score, 20 gates)

| Gate | Check | What it measures |
|------|-------|-----------------|
| S01 | tldr <= 160 chars, non-empty | Concision |
| S02 | tldr standalone (no self-reference) | Independence |
| S03 | title 5-100 chars | Appropriate length |
| S04 | version matches X.Y.Z semver | Versioning standard |
| S05 | created/updated match YYYY-MM-DD | Date format |
| S06 | >= 4 body sections (## headings) | Structure depth |
| S07 | largest section >= 30% of body | Content balance |
| S08 | no thin sections (< 3 non-empty lines) | Section substance |
| S09 | no filler phrases | Density |
| S10 | all bullets <= 80 chars | Concision per line |
| S11 | body contains tables | Visual density |
| S12 | body contains code blocks | Technical depth |
| S13 | body contains external URLs | Source citation |
| S14 | body references other CEX artifacts | Knowledge graph |
| S15 | data_source present and non-null | Provenance |
| S16 | keywords list, len >= 2 | BM25 searchability |
| S17 | long_tails list, len >= 1 | Semantic searchability |
| S18 | axioms list, len >= 1 | Actionable rules |
| S19 | no duplicate sentences (Jaccard < 0.85) | Originality |
| S20 | linked_artifacts has primary + related | Graph structure |

## Scoring Formula
```
hard_pass = all 10 HARD gates pass
soft_score = (soft_passed / soft_total) * 10
final = hard_pass ? soft_score : REJECTED

GOLDEN:     >= 9.5 (all HARD + 19/20 SOFT)
PUBLISH:    >= 8.0 (all HARD + 16/20 SOFT)
ACCEPTABLE: >= 7.0 (all HARD + 14/20 SOFT)
NEEDS_WORK: < 7.0 (all HARD but < 14/20 SOFT)
REJECTED:   any HARD fail
```

## Automation
Primary: `python _tools/validate_kc.py <file>` (ACTIVE)
Batch: `python _tools/validate_kc.py <dir> --summary`
Machine: `python _tools/validate_kc.py <file> --json`

## Pre-Production Checklist
- [ ] Topic is atomic (not too broad)
- [ ] No existing KC for this topic (brain_query check)
- [ ] Source material available
- [ ] Body structure chosen (domain_kc or meta_kc)
