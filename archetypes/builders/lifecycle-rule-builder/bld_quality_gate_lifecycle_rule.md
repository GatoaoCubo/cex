---
id: p11_qg_lifecycle_rule
kind: quality_gate
pillar: P11
title: "Gate: Lifecycle Rule"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder_agent
domain: lifecycle_rule
quality: 9.0
tags: [quality-gate, lifecycle-rule, governance, P11, state-machine]
tldr: "Quality gate for lifecycle_rule artifacts: enforces state list, measurable transitions, and periodic review cycle."
density_score: 0.85
llm_function: GOVERN
---
# Gate: Lifecycle Rule
## Definition
A `lifecycle_rule` governs how an artifact kind moves through states from creation to sunset. It defines valid states, the measurable criteria that permit transitions, and the review cadence that keeps the rule current. Gates here ensure no rule is published with vague triggers, missing ownership, or an unverifiable review cycle.
## HARD Gates
All HARD gates must pass. Any single failure sets score to 0 and blocks publish.
| ID  | Check | Failure consequence |
|-----|-------|---------------------|
| H01 | YAML frontmatter parses without error | Artifact unparseable by tooling |
| H02 | `id` matches `^p11_lc_[a-z][a-z0-9_]+$` | Namespace violation — not discoverable |
| H03 | `id` equals filename stem exactly | Brain search failure — id/file mismatch |
| H04 | `kind` == literal string `"lifecycle_rule"` | Type integrity failure |
| H05 | `quality` == `null` | Self-scoring violation — pool metric corruption |
| H06 | All required fields present and non-empty (`id`, `kind`, `pillar`, `version`, `created`, `updated`, `author`, `scope`, `ownership`, `freshness_days`, `review_cycle`, `tags`, `tldr`) | Incomplete artifact |
| H07 | `States` section present with >= 3 named states | Lifecycle incomplete — cannot govern transitions |
| H08 | `Transitions` section present with entry criteria per transition | Transitions without criteria are unenforceable |
| H09 | `Review Cycle` section present with explicit periodicity | No cadence means rule decays silently |
| H10 | `review_cycle` value is one of: `weekly`, `monthly`, `quarterly`, `yearly` | Free-text cycle cannot be scheduled |
## SOFT Scoring
Weights sum to 100%. Each dimension scores 0 or its full weight.
| ID  | Dimension | Weight | Criteria |
|-----|-----------|--------|----------|
| S01 | tldr quality | 1.0 | `tldr` <= 160 chars, names the governed artifact kind |
| S02 | States exhaustive for domain | 1.0 | No reachable real state missing from States table |
| S03 | Transitions have measurable criteria | 1.0 | Each transition criterion is checkable without human judgment |
| S04 | Review cycle realistic | 1.0 | Cycle matches actual volatility of governed domain |
| S05 | Ownership assigned per state | 1.0 | Each state has a named owner role or agent_group |
| S06 | Freshness threshold justified | 0.5 | `freshness_days` rationale present (not arbitrary) |
| S07 | Sunset conditions explicit | 1.0 | Defines what triggers end-of-life and who approves it |
| S08 | `tags` includes artifact `kind` name | 0.5 | Enables filtering by governed kind |
| S09 | Edge cases documented | 1.0 | Handles: orphaned artifacts, failed transitions, emergency overrides |
| S10 | Compatible with quality gate tiers | 0.5 | States map to: DRAFT, REVIEW, PUBLISH, GOLDEN, SUNSET |
| S11 | Density >= 0.80 | 1.0 | No filler: "when apownte", "as needed", "feels outdated" |
| S12 | Automation section present | 0.5 | Names at least one automated check or script for transition validation |
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool + record in memory |
| >= 8.0 | PUBLISH | Commit to pool |
| >= 7.0 | REVIEW | Acceptable with documented improvement items |
| < 7.0 | REJECT | Revise and resubmit — do not publish |
| 0 (HARD fail) | REJECTED | Fix failing HARD gate(s) first |
## Bypass
Bypasses are logged and expire automatically.
| Field | Value |
|-------|-------|
| condition | New artifact kind with no prior lifecycle precedent; states are draft and under active definition |
| approver | P11 governance owner (human) |
