---
kind: schema
id: bld_schema_secret_config
pillar: P09
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for secret_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Secret Config"
version: "1.0.0"
author: n03_builder
tags: [secret_config, builder, examples]
tldr: "Golden and anti-examples for secret config construction, demonstrating ideal structure and common pitfalls."
domain: "secret config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_memory_scope
  - bld_schema_retriever_config
  - bld_schema_constraint_spec
  - bld_schema_handoff_protocol
  - bld_schema_output_validator
  - bld_schema_chunk_strategy
  - bld_schema_smoke_eval
  - bld_schema_prompt_version
  - bld_schema_golden_test
  - bld_schema_search_tool
---

# Schema: secret_config
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_sec_{slug}) | YES | - | Namespace compliance |
| kind | literal "secret_config" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable config name |
| provider | enum: vault/k8s/aws/portkey/1password/sops | YES | - | Secret backend provider |
| rotation_policy | map {frequency, method} | YES | - | How secrets rotate |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "secret_config" |
| tldr | string <= 160ch | YES | - | Dense summary |
| encryption | map {at_rest, in_transit} | YES | - | Encryption posture |
| access_pattern | enum: dynamic/static/injected/env | YES | - | How agents retrieve secrets |
| description | string <= 200ch | REC | - | What this config governs |
| secret_paths | list[string] | REC | - | Provider paths / ARNs / keys |
| lease_duration | string | REC | - | Vault lease or token TTL |
| audit_log | boolean | REC | true | Audit access events |
| namespaces | list[string] | REC | - | K8s namespaces or AWS regions |
| fallback | string | REC | - | Fallback provider if primary fails |
## ID Pattern
Regex: `^p09_sec_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what credentials this config governs and why
2. `## Provider` — backend details, auth method, paths/ARNs
3. `## Rotation Policy` — frequency, method, trigger, rollback
4. `## Access Pattern` — how agents/services retrieve secrets at runtime
## Constraints
- max_bytes: 1024 (body only — compact credential spec)
- naming: p09_sec_{slug}.md (single file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- rotation_policy MUST include both frequency and method fields
- quality: null always
- NO actual secrets or credentials in body — placeholders only
- access_pattern MUST be one of: dynamic, static, injected, env

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_memory_scope]] | sibling | 0.67 |
| [[bld_schema_retriever_config]] | sibling | 0.66 |
| [[bld_schema_constraint_spec]] | sibling | 0.65 |
| [[bld_schema_handoff_protocol]] | sibling | 0.65 |
| [[bld_schema_output_validator]] | sibling | 0.64 |
| [[bld_schema_chunk_strategy]] | sibling | 0.64 |
| [[bld_schema_smoke_eval]] | sibling | 0.62 |
| [[bld_schema_prompt_version]] | sibling | 0.62 |
| [[bld_schema_golden_test]] | sibling | 0.62 |
| [[bld_schema_search_tool]] | sibling | 0.62 |
