---
id: p11_qg_naming_rule
kind: quality_gate
pillar: P11
title: "Gate: naming_rule"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: naming_rule
quality: 9.0
tags: [quality-gate, naming-rule, P11, P05, governance, conventions]
tldr: "Gates for naming_rule artifacts — pattern, scope, case style, and collision resolution for consistent identifiers."
density_score: 0.85
llm_function: GOVERN
---
# Gate: naming_rule
## Definition
| Field     | Value                                          |
|-----------|------------------------------------------------|
| metric    | pattern validity + scope coverage + example completeness |
| threshold | 8.0                                            |
| operator  | >=                                             |
| scope     | all naming_rule artifacts (P05)                |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = rule silently ignored |
| H02 | id matches `^p05_nr_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "naming_rule" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All required fields present: id, kind, pillar, version, created, updated, author, domain, quality, tags, tldr | Completeness |
| H07 | pattern field is present and non-empty (regex or glob string) | Rule must be machine-checkable |
| H08 | scope field is non-empty string <= 120 chars | Unbounded scope = unenforced rule |
| H09 | case_style field is present (kebab-case, snake_case, PascalCase, camelCase, UPPER_SNAKE, or other) | Case ambiguity causes collisions |
| H10 | valid_examples list has >= 2 entries; each entry matches pattern | Rule must be demonstrated correct |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty, references scope and pattern | 1.0 |
| S02 | tags is list, len >= 3, includes "naming-rule" | 0.5 |
| S03 | density_score >= 0.80 | 0.5 |
| S04 | pattern is a valid regex (compiles without error) and tested against all examples | 1.0 |
| S05 | invalid_examples list has >= 2 entries with stated violation reason | 1.0 |
| S06 | separator field documented (hyphen, underscore, dot, none, or other) | 0.5 |
| S07 | collision_resolution strategy defined (numbered suffix, error, timestamp, or other) | 1.0 |
| S08 | scope boundaries clearly exclude at least one adjacent domain | 0.5 |
| S09 | versioning_in_name field states whether version appears in identifier | 0.5 |
| S10 | human_rationale explains WHY this convention, not just WHAT it is | 1.0 |
| S11 | No filler phrases ("this rule", "designed to", "various cases") | 1.0 |
| S12 | related_rules cross-references >= 1 sibling naming rule if any exist | 0.5 |
Weights sum: 9.0. Normalize: divide each by 9.0 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as canonical naming convention reference |
| >= 8.0 | PUBLISH — enforce in linting and authoring guides |
| >= 7.0 | REVIEW — tighten pattern, add missing examples or rationale |
| < 7.0  | REJECT — rework pattern definition and scope boundary |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Migration window requiring temporary dual-format support before full rename |
| approver | p05-chief |
| audit_trail | Log in records/audits/ with bypass reason, affected artifacts, and timestamp |
| expiry | 72h — rule must fully pass before expiry or migration reverts |
| never_bypass | H01 (YAML), H05 (quality null) |
