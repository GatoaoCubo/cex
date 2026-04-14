---
id: p11_qg_pattern
kind: quality_gate
pillar: P11
title: "Gate: pattern"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: pattern
quality: 9.0
tags: [quality-gate, pattern, P11, P08, governance, architecture, reuse]
tldr: "Gates for pattern artifacts — recurring problem, concrete solution, balanced forces, and documented anti-pattern."
density_score: 0.85
llm_function: GOVERN
---
# Gate: pattern
## Definition
| Field     | Value                                              |
|-----------|----------------------------------------------------|
| metric    | problem recurrence + solution concreteness + force balance |
| threshold | 8.0                                                |
| operator  | >=                                                 |
| scope     | all pattern artifacts (P08)                        |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = pattern not discoverable |
| H02 | id matches `^p08_pat_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "pattern" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All required fields present: id, kind, pillar, version, created, updated, author, domain, quality, tags, tldr | Completeness |
| H07 | problem field describes a recurring situation, not a one-off fix (contains recurrence signal word: "repeatedly", "often", "whenever", "each time", or equivalent) | One-off fixes are not patterns |
| H08 | solution field describes the approach at implementation level (not abstract advice) | "Use better design" is not a solution |
| H09 | forces list has >= 2 entries documenting opposing tensions that make the problem hard | No forces = no pattern, just a preference |
| H10 | consequences list includes >= 1 negative trade-off (cost, complexity, or constraint) | Benefits-only = marketing, not engineering |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty | 1.0 |
| S02 | tags is list, len >= 3, includes "pattern" | 0.5 |
| S03 | density_score >= 0.80 | 0.5 |
| S04 | applicability block states both when-to-use AND when-not-to-use conditions | 1.0 |
| S05 | examples block has >= 2 concrete applications of the pattern in a real context | 1.0 |
| S06 | anti_pattern block documents >= 1 wrong approach that looks similar but fails | 1.0 |
| S07 | related_patterns block cross-references >= 1 other pattern with stated relationship | 0.5 |
| S08 | variants list documents known adaptations or specializations of the base pattern | 0.5 |
| S09 | code_or_pseudocode block provides a minimal working illustration | 1.0 |
| S10 | name is 2–5 words, title-case, and self-describing without context | 0.5 |
| S11 | No filler phrases ("this pattern", "in order to", "various scenarios") | 1.0 |
Weights sum: 8.5. Normalize: divide each by 8.5 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as canonical reference pattern |
| >= 8.0 | PUBLISH — index in pattern catalog and cross-link from related patterns |
| >= 7.0 | REVIEW — strengthen forces, add anti-pattern, or provide concrete example |
| < 7.0  | REJECT — rework problem statement and solution into implementable form |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Pattern needed to unblock active architecture decision with no existing equivalent in catalog |
| approver | p08-chief |
| audit_trail | Log in records/audits/ with linked decision record and timestamp |
| expiry | 72h — pattern must pass all gates and be indexed before expiry |
| never_bypass | H01 (YAML), H05 (quality null) |
