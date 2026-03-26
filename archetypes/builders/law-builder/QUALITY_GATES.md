---
id: law-builder-quality-gates
kind: quality_gate
pillar: P11
parent: law-builder
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [quality-gates, law-builder, validation, P08, governance]
---

# law-builder — QUALITY GATES

## HARD Gates (9)

All HARD gates MUST pass. Any single failure = artifact rejected (score = 0).

| Gate | Check | Failure consequence |
|------|-------|-------------------|
| H01 | YAML frontmatter parses without error | Broken artifact — unparseable by tooling |
| H02 | id matches `^p08_law_[0-9]+$` | Namespace violation — not discoverable |
| H03 | id equals filename stem exactly | Brain search failure — id/file mismatch |
| H04 | kind == literal string "law" | Type integrity failure — wrong kind |
| H05 | quality == null | Self-scoring violation — pool metric corruption |
| H06 | All 15 required fields present and non-empty (quality: null counts as present) | Incomplete artifact — missing critical metadata |
| H07 | tags is a list with length >= 3 | Unsearchable — minimum tagging not met |
| H08 | number is a positive integer | Law identification failure — unidentifiable |
| H09 | statement uses imperative mood (contains MUST, SHALL, NEVER, or ALWAYS) | Law is advisory, not mandatory — not a law |

## SOFT Gates (10)

SOFT gates contribute to quality score. Target: pass all 10 for score >= 9.0.

| Gate | Check | Weight | Points |
|------|-------|--------|--------|
| S01 | tldr is <= 160 chars and non-empty | 1.0 | 10 |
| S02 | rationale explains WHY (does not merely restate statement) | 1.0 | 10 |
| S03 | enforcement names a specific detection mechanism (automated, review, or runtime) | 1.0 | 10 |
| S04 | exceptions field is present: list of conditions or explicitly "None" | 1.0 | 10 |
| S05 | scope is specified (system, satellite, or domain) | 1.0 | 10 |
| S06 | Examples section has >= 2 correct applications | 1.0 | 10 |
| S07 | Violations section has >= 2 breach scenarios with consequences | 1.0 | 10 |
| S08 | Body has all 8 required sections (Statement, Rationale, Enforcement, Exceptions, Examples, Violations, History, References) | 1.0 | 10 |
| S09 | density >= 0.80 (no filler phrases: "is important", "helps the system", "in summary", "basically") | 1.0 | 10 |
| S10 | keywords field present with >= 2 terms | 0.5 | 10 |

## Scoring Formula

```
hard_pass = all(H01..H09)
if not hard_pass: score = 0, REJECTED

soft_points = sum(weight * 10 for each passing SOFT gate)
soft_max = sum(weights) * 10 = 9.5 * 10 = 95
soft_score = (soft_points / soft_max) * 10

score = soft_score  # range: 0.0 - 10.0
```

Thresholds:
| Score | Tier | Action |
|-------|------|--------|
| 0 | HARD FAIL | Rejected — fix and resubmit |
| < 7.0 | Below threshold | Revise before output |
| 7.0 - 7.9 | Experimental | Acceptable, improvement recommended |
| 8.0 - 9.4 | Pool eligible | Commit to pool |
| >= 9.5 | Golden | Pool + memory() |

## Validation Checklist

Run before every output:

```
[ ] H01: YAML parses
[ ] H02: id = p08_law_{number}
[ ] H03: id == filename stem
[ ] H04: kind = "law"
[ ] H05: quality = null
[ ] H06: 15 required fields present
[ ] H07: tags list len >= 3
[ ] H08: number is positive integer
[ ] H09: statement contains MUST/SHALL/NEVER/ALWAYS

[ ] S01: tldr <= 160 chars
[ ] S02: rationale explains WHY
[ ] S03: enforcement names mechanism
[ ] S04: exceptions present
[ ] S05: scope specified
[ ] S06: >= 2 examples
[ ] S07: >= 2 violations
[ ] S08: all 8 body sections
[ ] S09: density >= 0.80
[ ] S10: keywords >= 2 terms
```
