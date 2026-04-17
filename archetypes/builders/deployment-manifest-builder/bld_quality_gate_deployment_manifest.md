---
id: bld_quality_gate_deployment_manifest
kind: quality_gate
pillar: P07
title: "Gate: deployment_manifest"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: deployment_manifest
quality: null
tags: [quality_gate, deployment_manifest, P09]
llm_function: GOVERN
tldr: "Validates deployment manifests for artifact pinning, rollback strategy, secrets handling, and environment targeting."
density_score: null
---

## Definition
A deployment_manifest specifies what artifacts to deploy, to which environment, with what config, and how to roll back. This gate ensures every manifest is safe to hand to an automated deployment pipeline without human interpretation.

## HARD Gates
Failure on any HARD gate causes immediate REJECT.

| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML frontmatter is valid with no syntax errors |
| H02 | ID matches namespace | `id` matches pattern `^p09_dm_[a-z][a-z0-9_]+$` |
| H03 | Kind matches literal | `kind` is exactly `deployment_manifest` |
| H04 | No inline secrets | No plaintext secret values in frontmatter or body |
| H05 | Quality is null | `quality` field is `null` |
| H06 | Artifacts list non-empty | At least 1 artifact with name + version |
| H07 | No "latest" version tags | All artifact versions are pinned (semver or SHA) |
| H08 | rollback_to is set | `rollback_to` field is non-null and non-empty |

## SOFT Scoring
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| Artifacts have checksums | 1.0 | SHA256 present per artifact |
| Target environment fully specified | 1.0 | namespace + region + cluster all present |
| Health check endpoint present | 1.0 | health_check_endpoint is non-empty |
| Config overrides documented | 0.5 | env_vars table present (even if empty) |
| Auto-rollback flag set | 0.5 | auto_rollback: true or false (not missing) |
| Tags include deployment_manifest | 0.5 | tags contains "deployment_manifest" |
| tldr <= 160 chars | 0.5 | Concise summary |

Sum of weights: 5.0. `soft_score = sum(weight * gate_score) / 5.0 * 10`

## Actions
| Score | Action |
|-------|--------|
| >= 9.0 | PUBLISH -- safe for automated pipeline |
| >= 7.0 | REVIEW -- deploy with manual approval |
| < 7.0 | REJECT -- incomplete; do not deploy |
