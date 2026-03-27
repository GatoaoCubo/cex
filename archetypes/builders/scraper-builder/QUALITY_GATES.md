---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for scraper validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: scraper

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p04_scraper_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "scraper" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | Required fields present: id, kind, pillar, version, created, updated, author, name, target, selectors, output_format, quality, tags, tldr | Completeness |
| H07 | body has ## Overview, ## Selectors, ## Pagination & Rate Limiting, ## Output | Core sections |
| H08 | body <= 1024 bytes | Compact scraper spec |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "scraper" | 0.5 | 10 |
| S03 | selectors list matches field names in ## Selectors section (zero drift) | 1.0 | 10 |
| S04 | pagination and rate_limit fields present | 1.0 | 10 |
| S05 | Each selector has: CSS/XPath, type, extraction rule | 1.0 | 10 |
| S06 | anti_bot field present and valid enum | 0.5 | 10 |
| S07 | No implementation code in body (spec only) | 1.0 | 10 |
| S08 | target is valid URL format | 0.5 | 10 |
| S09 | description <= 200 chars and non-generic | 0.5 | 10 |
| S10 | density_score >= 0.80 (no filler phrases) | 0.5 | 10 |
| S11 | validation rules defined for extracted data | 0.5 | 10 |
| S12 | freshness threshold defined | 0.5 | 10 |

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

## Pre-Production Checklist
- [ ] Target site identified with URL
- [ ] All data fields enumerated with selectors
- [ ] Pagination strategy determined
- [ ] Rate limits and anti-bot level assessed
- [ ] No existing scraper for this target (brain_query checked)
