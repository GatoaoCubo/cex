---
id: p11_qg_secret_config
kind: quality_gate
pillar: P11
title: "Gate: secret_config"
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
domain: "credential and secret management specification — provider, rotation policy, encryption posture, and access pattern"
quality: 9.0
tags: [quality-gate, secret-config, P09, credentials, rotation, encryption]
tldr: "Pass/fail gate for secret_config artifacts: provider validity, rotation policy completeness, encryption posture, access pattern, and no plaintext secrets."
density_score: 0.90
llm_function: GOVERN
---
# Gate: secret_config
## Definition
| Field | Value |
|---|---|
| metric | secret_config artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: secret_config` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p09_sec_[a-z][a-z0-9_]+$` | ID contains uppercase, hyphens, or missing prefix |
| H03 | ID equals filename stem | `id: p09_sec_foo` but file is `p09_sec_bar.md` |
| H04 | Kind equals literal `secret_config` | `kind: config` or `kind: env_config` or any other value |
| H05 | Quality field is null | `quality: 7.5` or any non-null value |
| H06 | All required fields present | Missing `provider`, `rotation_policy`, `encryption`, or `access_pattern` |
| H07 | All 4 body sections present | Missing Overview, Provider, Rotation Policy, or Access Pattern section |
| H08 | Provider is valid enum | `provider: database` or any non-enum value |
| H09 | rotation_policy has both frequency and method | Missing frequency or method sub-field |
| H10 | NO plaintext secrets in file | Real API keys, passwords, or tokens found (not placeholders) |
| H11 | encryption has both at_rest and in_transit | Missing either at_rest or in_transit sub-field |
| H12 | access_pattern is valid enum | Value not in: dynamic, static, injected, env |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Rotation policy completeness | 1.0 | frequency, method, trigger, and rollback all defined |
| Encryption specificity | 1.0 | Algorithm named (AES-256-GCM, not just "encrypted") |
| Access pattern documentation | 1.0 | Step-by-step retrieval instructions in body |
| Secret path completeness | 0.5 | All relevant paths listed as placeholders |
| Lease and TTL definition | 0.5 | lease_duration set when access_pattern == dynamic |
| Audit log posture | 1.0 | audit_log declared; justification provided if false |
| Fallback definition | 0.5 | Fallback provider or method defined for critical secrets |
| Namespace/region scoping | 0.5 | namespaces listed when provider == k8s or aws |
| Boundary clarity | 1.0 | Explicitly not env_config, permission, or feature_flag |
| Domain specificity | 1.0 | Content specific to declared credential type and use case |
| Provider auth method | 1.0 | Auth method (AppRole, IAM, SA token) documented in Provider section |
| Rollback procedure | 1.0 | What happens if rotation fails — recovery steps defined |
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
| conditions | Internal development stub only, never used in production agents |
| approver | Author self-certification with comment explaining dev-only scope |
| audit_trail | Bypass note in frontmatter comment with expiry date |
| expiry | 7d — secret configs must reach >= 7.0 or be removed (shorter than cli_tool — security risk) |
| never_bypass | H01 (unparseable YAML), H05 (self-scored artifacts), H10 (plaintext secrets — immediate security violation) |
