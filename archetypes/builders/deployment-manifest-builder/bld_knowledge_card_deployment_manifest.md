---
id: bld_knowledge_card_deployment_manifest
kind: knowledge_card
pillar: P01
title: "Knowledge Card: deployment_manifest"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: deployment_manifest
quality: null
tags: [knowledge_card, deployment_manifest, P09]
llm_function: INJECT
tldr: "Domain knowledge for building deployment_manifest artifacts: patterns, anti-patterns, and decision rules."
density_score: null
---

# Knowledge Card: deployment_manifest

## What It Is
A deployment_manifest specifies WHAT artifacts to deploy, WHERE (environment/target), and HOW (configuration overrides, secrets, rollback). Industry analogs: Kubernetes manifest, Helm values.yaml, AWS CloudFormation template.

## When to Use
- Deploying one or more versioned artifacts to a known environment
- Encoding deployment configuration that differs from defaults
- Specifying rollback plan before triggering a deployment pipeline
- Documenting what was deployed (post-deploy audit trail)

## When NOT to Use
- Defining runtime environment variables in isolation -> use env_config
- Configuring a test/ephemeral environment -> use sandbox_spec
- Splitting traffic between versions -> use canary_config
- Defining contractual SLA with external parties -> use enterprise_sla

## Key Patterns
| Pattern | When | Notes |
|---------|------|-------|
| Blue-green | Zero-downtime swap | Two identical envs; switch traffic atomically |
| Rolling update | Gradual pod replacement | Reduces risk; slower than blue-green |
| Recreate | Simple stateless services | Downtime acceptable; simplest manifest |
| Pin versions | Always | Never use "latest" in production manifests |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Inline secrets | Security leak in version control | Reference secrets by vault path or k8s secret name |
| Missing rollback_to | No recovery path | Always specify prior revision or known-good version |
| "latest" tag | Non-reproducible deployments | Always pin exact version or SHA |
| No health check | Cannot detect failed deploy | Always specify health_check_endpoint |
