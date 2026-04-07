---
kind: schema
id: bld_schema_regression_check
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for regression_check
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: regression_check
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p07_rc_{slug}) | YES | - | Namespace compliance |
| kind | literal "regression_check" | YES | - | Type integrity |
| pillar | literal "P07" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable check name |
| baseline_ref | string | YES | - | Reference experiment/version to compare against |
| threshold | number (0.0–1.0 or %) | YES | - | Max acceptable deviation before failure |
| metrics | list[string], len >= 1 | YES | - | Dimensions to compare (accuracy, latency, cost, etc.) |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "regression_check" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What this check compares |
| tool | enum: braintrust, promptfoo, langsmith, deepeval, costm | REC | - | Comparison framework |
| comparison_mode | enum: relative, absolute | REC | relative | How threshold is applied |
| fail_action | enum: block, warn, log | REC | warn | Action when regression detected |
| notify | list[string] | REC | - | Channels or owners to notify |
| cadence | string | REC | - | When check runs (on_deploy, daily, on_pr, etc.) |
| scope | string | REC | - | Which prompt/model/pipeline is under test |
## ID Pattern
Regex: `^p07_rc_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what this check detects, which system, who owns it
2. `## Baseline` — baseline_ref meaning, how baseline was captured, update cadence
3. `## Metrics` — each metric: definition, measurement method, threshold, direction (higher/lower is better)
4. `## Failure Protocol` — what happens when regression detected, who is notified, fail_action
## Constraints
- max_bytes: 2048 (body only — comparison config with metric detail)
- naming: p07_rc_{slug}.md (single file, matches naming field in _schema.yaml)
- machine_format: yaml (compiled artifact)
- id == filename stem
- metrics list MUST match metric names defined in ## Metrics section
- baseline_ref MUST be a resolvable reference (experiment ID, tag, version string)
- threshold MUST be numeric — percentage (5.0) or decimal (0.05), document which
- quality: null always
- NO implementation code in body — config spec only
