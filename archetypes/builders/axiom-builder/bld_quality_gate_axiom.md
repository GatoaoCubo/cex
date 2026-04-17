---
id: p11_qg_axiom
kind: quality_gate
pillar: P11
title: "Gate: axiom"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: axiom
quality: 9.0
tags: [quality-gate, axiom, P11, P10, governance, immutable, fundamental-truth]
tldr: "Gates for axiom artifacts — immutable fundamental rules that govern a domain permanently."
density_score: 0.89
llm_function: GOVERN
---
# Gate: axiom
## Definition
| Field     | Value                                          |
|-----------|------------------------------------------------|
| metric    | immutability rigor + scope boundary precision  |
| threshold | 8.0                                            |
| operator  | >=                                             |
| scope     | all axiom artifacts (P10)                      |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = axiom invisible to system |
| H02 | id matches `^p10_ax_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "axiom" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All 13 required fields present | Completeness |
| H07 | tags is list, len >= 3 | Searchability minimum |
| H08 | rule field is ONE sentence (no period-separated compound rules) | Atomicity — one axiom, one truth |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty | 1.0 |
| S02 | rationale present with >= 2 distinct reasons | 1.0 |
| S03 | scope names concrete domain boundary (not "everything") | 1.0 |
| S04 | enforcement describes detection mechanism, not just intent | 1.0 |
| S05 | immutable == true field present | 0.5 |
| S06 | body has all 7 required sections | 1.0 |
| S07 | Examples section has >= 2 cases (valid and invalid) | 1.0 |
| S08 | Violations section has >= 1 concrete breach scenario | 1.0 |
| S09 | density_score >= 0.80 | 1.0 |
| S10 | keywords present, len >= 2 | 0.5 |
Weights sum: 9.0. Normalize: divide each by 9.0 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as canonical axiom |
| >= 8.0 | PUBLISH — active governance enforcement |
| >= 7.0 | REVIEW — sharpen rule atomicity or add violation scenarios |
| < 7.0  | REJECT — rule is not immutable, or scope is underdefined |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Axiom required to block active system violation in production |
| approver | p10-chief |
| audit_trail | Log in records/audits/ with violation evidence and timestamp |
| expiry | 24h — axioms must be fully specified before expiry |
| never_bypass | H01 (YAML), H05 (quality null) |
