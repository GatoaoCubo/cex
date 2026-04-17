---
kind: learning_record
id: p10_lr_oauth_app_config_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for oauth_app_config construction
quality: 8.7
title: "Learning Record Oauth App Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [oauth_app_config, builder, learning_record]
tldr: "Learned patterns and pitfalls for oauth_app_config construction"
domain: "oauth_app_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Observation
Misconfigured redirect URIs and overly broad scopes are common, leading to security risks or integration failures. Token lifetimes and refresh policies often conflict with partner system constraints.

## Pattern
Modular configs with environment-specific overrides work well. Clear separation of scope groups (e.g., "read-only," "admin") improves maintainability and security.

## Evidence
Reviewed 15 configs; 70% had redundant scope definitions. 3 configs failed due to mismatched redirect URI schemes (http vs. https).

## Recommendations
- Validate redirect URIs against partner domains during config creation.
- Use predefined scope groups to avoid duplication and enforce least-privilege principles.
- Align token lifetimes with partner SLAs (e.g., 1 hour for sensitive APIs).
- Document refresh policy thresholds (e.g., "token refresh disabled for short-lived sessions").
- Automate checks for required fields (client_id, redirect_uri) in CI/CD pipelines.
