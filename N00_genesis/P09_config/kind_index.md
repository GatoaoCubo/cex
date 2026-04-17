---
id: n00_p09_kind_index
kind: knowledge_card
pillar: P09
nucleus: n00
title: "P09 Config -- Kind Index"
version: 1.0
quality: null
tags: [index, p09, archetype, n00]
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+schema F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Master index of all 28 kinds in pillar P09. Reference for /mentor, nucleus builders, and the 8F pipeline.

## Pillar: P09 Config
Runtime configuration: environment variables, rate limits, secrets, feature flags, RBAC policies, and sandbox specs. The operational layer that governs how agents run in production.

## Kinds in P09

| Kind | Purpose | Primary Nucleus | Builder |
|------|---------|-----------------|---------|
| `batch_config` | Async batch processing config for bulk API operations (OpenAI Batch, A | N05 | `batch_config-builder` |
| `cost_budget` | Token budget allocation, spend tracking, cost alerts per provider/mode | N05 | `cost_budget-builder` |
| `data_residency` | Data residency configuration for GDPR and regional compliance | N05 | `data_residency-builder` |
| `effort_profile` | Effort and thinking level configuration for builder execution | N05 | `effort_profile-builder` |
| `env_config` | Environment variables | N05 | `env_config-builder` |
| `experiment_config` | A/B test and prompt experiment configuration with variants, metrics, a | N05 | `experiment_config-builder` |
| `feature_flag` | Feature flag (on/off, gradual rollout) | N05 | `feature_flag-builder` |
| `kubernetes_ai_requirement` | CNCF Kubernetes AI Requirement (KAR) conformance artifact: GPU topolog | N05 | `kubernetes_ai_requirement-builder` |
| `marketplace_app_manifest` | Marketplace app manifest spec for Claude/LangChain/HuggingFace listing | N05 | `marketplace_app_manifest-builder` |
| `oauth_app_config` | OAuth2/PKCE app config for partner integrations: scopes, redirects, to | N05 | `oauth_app_config-builder` |
| `path_config` | System paths | N05 | `path_config-builder` |
| `permission` | Permission rule (read/write/execute) | N05 | `permission-builder` |
| `playground_config` | Playground/sandbox config for interactive product evaluation | N05 | `playground_config-builder` |
| `prosody_config` | Voice personality and emotion settings | N05 | `prosody_config-builder` |
| `quantization_config` | Model quantization and compression settings | N05 | `quantization_config-builder` |
| `rate_limit_config` | Rate limiting: RPM, TPM, budget | N05 | `rate_limit_config-builder` |
| `rbac_policy` | Role-based access control policy for multi-tenant isolation | N05 | `rbac_policy-builder` |
| `realtime_session` | Live bidirectional session configuration | N05 | `realtime_session-builder` |
| `runtime_rule` | Runtime rule (timeouts, retries, limits) | N05 | `runtime_rule-builder` |
| `sandbox_config` | Isolated code execution environment config | N05 | `sandbox_config-builder` |
| `sandbox_spec` | Isolated sandbox environment spec for enterprise pilot procurement gat | N05 | `sandbox_spec-builder` |
| `secret_config` | Secret management | N05 | `secret_config-builder` |
| `sso_config` | SSO/SAML/OIDC identity provider integration configuration | N05 | `sso_config-builder` |
| `thinking_config` | Extended thinking and budget token settings | N05 | `thinking_config-builder` |
| `transport_config` | Network transport layer for realtime communication | N05 | `transport_config-builder` |
| `usage_quota` | Usage quota and fair-use enforcement configuration | N05 | `usage_quota-builder` |
| `vad_config` | Voice activity detection settings | N05 | `vad_config-builder` |
| `white_label_config` | White-label/reseller configuration for branded deployments | N05 | `white_label_config-builder` |

## Usage
```python
# Build any of these via 8F:
python _tools/cex_8f_runner.py "your intent" --kind {kind} --execute
```

## CoC Hierarchy Note
These 28 kinds follow the convention-over-configuration hierarchy: each instance
(N01-N07) inherits this schema and fills the variables for its sin lens.
N00_genesis holds the canonical archetype; nuclei hold the instantiated versions.
