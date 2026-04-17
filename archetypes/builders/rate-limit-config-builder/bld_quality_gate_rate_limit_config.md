---
id: p11_qg_rate_limit_config
kind: quality_gate
pillar: P11
title: "Gate: rate_limit_config"
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
domain: "rate limiting configuration — RPM, TPM, budget, and tier management for LLM API providers"
quality: 9.0
tags: [quality-gate, rate-limit-config, P09, rpm, tpm, budget, tier]
tldr: "Pass/fail gate for rate_limit_config artifacts: numeric limit completeness, tier validity, budget cap presence, and provider identification."
density_score: 0.90
llm_function: GOVERN
---
# Gate: rate_limit_config

This ISO encodes a rate limit policy -- throttle bounds, quota windows, and backoff behavior.
## Definition
| Field | Value |
|---|---|
| metric | rate_limit_config artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: rate_limit_config` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p09_rl_[a-z][a-z0-9_]+$` | ID contains uppercase, hyphens, or missing prefix |
| H03 | ID equals filename stem | `id: p09_rl_foo` but file is `p09_rl_bar.md` |
| H04 | Kind equals literal `rate_limit_config` | `kind: config` or any other value |
| H05 | Quality field is null | `quality: 8.0` or any non-null value |
| H06 | All required fields present | Missing `provider`, `rpm`, `tpm`, `tier`, or `tags` |
| H07 | rpm is a positive integer | rpm: 0, rpm: -1, rpm: "50", or absent |
| H08 | tpm is a positive integer | tpm: 0, tpm: -1, tpm: "80000", or absent |
| H09 | tags includes "rate_limit_config" | tags list does not contain "rate_limit_config" |
| H10 | Body has all 4 required sections | Missing ## Overview, ## Limits, ## Tier, or ## Budget |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Limit completeness | 1.0 | RPM, TPM, RPD, and concurrent all documented |
| Tier description | 1.0 | Tier named, described, and upgrade path provided |
| Budget cap | 1.0 | budget_usd present with alert_threshold and overage policy |
| Model overrides | 0.5 | Per-model rpm/tpm overrides present when provider supports them |
| Retry policy | 0.5 | retry_after documented for 429 handling |
| Provider accuracy | 1.0 | Limits match known provider documentation for stated tier |
| Alert threshold | 0.5 | alert_threshold in [0.0, 1.0], actionable value (e.g. 0.8) |
| tldr quality | 1.0 | tldr <= 160ch, includes provider + tier + key limits |
| Boundary clarity | 1.0 | Explicitly not runtime_rule (timeouts/retries) or env_config |
| Domain specificity | 1.0 | Numbers are real provider limits, not placeholders |
| Testability | 1.0 | Each limit value verifiable against provider dashboard/docs |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Internal placeholder used only during development with fictional limits |
| approver | Author self-certification noting placeholder status |
| audit_trail | Bypass note in frontmatter comment with expiry date |
| expiry | 7d — placeholder configs must be replaced with real limits or removed |
| never_bypass | H01 (unparseable YAML), H05 (self-scored gates corrupt quality metrics), H07/H08 (zero/negative limits break all consumers) |
