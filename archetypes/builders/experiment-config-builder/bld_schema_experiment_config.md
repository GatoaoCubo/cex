---
kind: schema
id: bld_schema_experiment_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for experiment_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Experiment Config"
version: "1.0.0"
author: n03_builder
tags: [experiment_config, builder, schema, P09]
tldr: "Schema for experiment_config: A/B test artifact with variants, traffic splits, metrics, and hypothesis lifecycle."
domain: "experiment config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_output_validator
  - bld_schema_memory_scope
  - bld_schema_handoff_protocol
  - bld_schema_usage_report
  - bld_schema_prompt_version
  - bld_schema_smoke_eval
  - bld_schema_action_prompt
  - bld_schema_golden_test
  - bld_schema_constraint_spec
---

# Schema: experiment_config
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_ec_{name_slug}) | YES | - | Namespace compliance |
| kind | literal "experiment_config" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| hypothesis | string <= 200ch | YES | - | Falsifiable hypothesis the experiment tests |
| variants | list[string], len >= 2 | YES | - | Names of all variants; first MUST be "control" |
| primary_metric | string | YES | - | Single metric the experiment optimizes |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "experiment_config" |
| tldr | string <= 160ch | YES | - | Dense summary |
| status | enum: draft, running, paused, concluded | YES | draft | Lifecycle state |
| traffic_split | object | YES | - | Variant name -> percentage (must sum to 100) |
| guardrail_metrics | list[string] | REC | [] | Metrics that must not regress |
| significance_threshold | float 0.0-1.0 | REC | 0.05 | p-value threshold for significance |
| min_detectable_effect | string | REC | - | Minimum change worth detecting (e.g., "+2% CTR") |
| sample_size_target | integer | REC | - | Total samples needed per variant |
| duration_days | integer | REC | - | Planned experiment run length |
| segment | string | OPT | "all" | Audience segment for experiment (all, power_users, etc.) |
| concluded_at | date YYYY-MM-DD | OPT | - | Populated when status: concluded |
| winning_variant | string | OPT | - | Populated when concluded with clear winner |
## ID Pattern
Regex: `^p09_ec_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` -- what is being tested, why, and what decision it enables
2. `## Variants` -- table: name, type (control/treatment), description, parameter changes
3. `## Traffic Split` -- allocation table and any segment/hold-out rules
4. `## Metrics` -- primary metric definition + guardrail metrics with acceptable thresholds
5. `## Statistical Parameters` -- significance threshold, MDE, sample size, duration
6. `## Lifecycle` -- current status, key dates, decision criteria for conclusion
## Constraints
- max_bytes: 4096 (body only)
- naming: p09_ec_{name_slug}.yaml
- machine_format: yaml (compiled artifact)
- id == filename stem
- variants list MUST include "control" as first entry
- traffic_split percentages MUST sum to 100
- quality: null always
- NEVER hardcode PII or user data in variant parameters

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.63 |
| [[bld_schema_output_validator]] | sibling | 0.62 |
| [[bld_schema_memory_scope]] | sibling | 0.62 |
| [[bld_schema_handoff_protocol]] | sibling | 0.61 |
| [[bld_schema_usage_report]] | sibling | 0.61 |
| [[bld_schema_prompt_version]] | sibling | 0.61 |
| [[bld_schema_smoke_eval]] | sibling | 0.61 |
| [[bld_schema_action_prompt]] | sibling | 0.61 |
| [[bld_schema_golden_test]] | sibling | 0.61 |
| [[bld_schema_constraint_spec]] | sibling | 0.61 |
