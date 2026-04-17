---
kind: schema
id: bld_schema_batch_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for batch_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.2
title: "Schema Batch Config"
version: "1.0.0"
author: n03_builder
tags: [batch_config, builder, schema, P09]
tldr: "Schema for batch_config artifacts: async bulk API job configuration fields, constraints, and body structure."
domain: "batch config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Schema: batch_config

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_bc_{name_slug}) | YES | - | Namespace compliance |
| kind | literal "batch_config" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| provider | enum: openai, anthropic, azure_openai, custom | YES | - | API provider for batch jobs |
| model | string | YES | - | Model ID for batch inference |
| endpoint | string | YES | - | API endpoint path (e.g., /v1/chat/completions) |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "batch_config" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What this batch config covers |
| max_requests | integer | REC | - | Max requests per batch submission |
| completion_window | string | REC | - | Time window for batch completion (e.g., 24h) |
| cost_cap_usd | number | REC | - | Maximum spend allowed per batch job |
| concurrency | integer | REC | - | Max concurrent in-flight requests |
| retry_policy | string | REC | - | Summary of retry strategy |
| input_format | enum: jsonl, csv, json | REC | jsonl | Input file format |
| output_format | enum: jsonl, csv, json | REC | jsonl | Output file format |

## ID Pattern
Regex: `^p09_bc_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)
1. `## Overview` -- purpose of this batch job, provider context, who triggers it
2. `## Job Parameters` -- table: parameter, value, description for all job settings
3. `## Cost Controls` -- cost cap, token budget, discount expectations (batch API typically 50% cheaper)
4. `## Retry and Error Policy` -- max retries, backoff strategy, error classification, dead-letter handling
5. `## Input/Output Format` -- JSONL schema for requests and responses, storage paths

## Constraints
- max_bytes: 2048 (body only -- batch configs are concise specs)
- naming: p09_bc_{name_slug}.yaml
- machine_format: yaml (compiled artifact)
- id == filename stem
- provider MUST be one of: openai, anthropic, azure_openai, custom
- quality: null always
- NEVER include actual API keys or credentials -- reference env var names only
- completion_window MUST be >= 1h (batch is async, not real-time)
