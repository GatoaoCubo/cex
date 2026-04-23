---
id: p04_output_github_actions
kind: hook_config
pillar: P04
title: GitHub Actions CI/CD Pipeline Configuration
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n05_operations
domain: ci-cd-operations
quality: 9.0
tags: [hook_config, ci-cd, operations, N05, github-actions, pipeline]
tldr: "GitHub Actions CI/CD pipeline with pre-commit hooks, artifact validation, system tests, quality gates, and Railway deploy automation."
density_score: 0.96
related:
  - p01_kc_github_actions
  - n05_output_monetization_infra
  - p01_kc_deploy_paas
  - validate
  - bld_sp_output_template_software_project
  - p01_kc_railway_cli_patterns
  - doctor
  - skill
  - n03_output_monetization_architecture
  - KC_N05_RAILWAY_CLI_PATTERNS
---

# GitHub Actions CI/CD Pipeline

## Overview

This configuration defines the complete CI/CD pipeline for CEX via GitHub
Actions. Three workflows cover validation, testing, and deployment. Every
push and PR is gated. No merge without green checks. No deploy without
passing all quality gates.

## Workflow 1: Validate (on every push and PR)

```yaml
# .github/workflows/validate.yml
name: CEX Validate
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Encoding check
        run: python _tools/cex_sanitize.py --all

      - name: Frontmatter validation
        run: python _tools/cex_hooks.py --all

      - name: YAML compilation
        run: python _tools/cex_compile.py --all --dry-run

      - name: Builder health
        run: python _tools/cex_doctor.py

      - name: Quality snapshot
        run: python _tools/cex_quality_monitor.py --snapshot
```

## Workflow 2: Test (on PR to main)

```yaml
# .github/workflows/test.yml
name: CEX Test
on:
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: System tests (54 tests)
        run: python _tools/cex_system_test.py

      - name: Flywheel audit (109 checks)
        run: python _tools/cex_flywheel_audit.py

      - name: Regression check
        run: python _tools/cex_quality_monitor.py --compare

      - name: Release gate
        run: python _tools/cex_release_check.py
```

## Workflow 3: Deploy (on merge to main, manual trigger)

```yaml
# .github/workflows/deploy.yml
name: CEX Deploy
on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    if: github.event_name == 'push' || github.event_name == 'workflow_dispatch'
    environment: production
    steps:
      - uses: actions/checkout@v4

      - name: Setup Railway CLI
        run: npm install -g @railway/cli

      - name: Pre-flight checks
        run: |
          python _tools/cex_release_check.py
          python _tools/cex_hooks.py --all

      - name: Deploy to Railway
        env:
          RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}
        run: railway up --detach

      - name: Smoke eval (30s budget)
        run: bash N05_operations/P05_output/smoke_eval_deploy.sh ${{ vars.API_URL }}
        timeout-minutes: 1

      - name: Post-deploy health verification
        run: |
          sleep 10
          curl -sf ${{ vars.API_URL }}/health | jq .
```

## Branch Protection Rules

| rule | value |
|------|-------|
| Required status checks | validate, test |
| Required reviews | 1 minimum |
| Dismiss stale reviews | true |
| Require up-to-date branch | true |
| Restrict pushes to main | only via PR |
| Allow force push | never |

## Secrets Required

| secret | purpose |
|--------|---------|
| RAILWAY_TOKEN | Railway CLI authentication for deploys |
| ANTHROPIC_API_KEY | LLM API access for runtime tests |
| DATABASE_URL | PostgreSQL connection for integration tests |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_github_actions]] | upstream | 0.45 |
| [[n05_output_monetization_infra]] | downstream | 0.25 |
| [[p01_kc_deploy_paas]] | upstream | 0.25 |
| [[validate]] | downstream | 0.24 |
| [[bld_sp_output_template_software_project]] | downstream | 0.22 |
| [[p01_kc_railway_cli_patterns]] | upstream | 0.22 |
| [[doctor]] | downstream | 0.21 |
| [[skill]] | downstream | 0.21 |
| [[n03_output_monetization_architecture]] | downstream | 0.20 |
| [[KC_N05_RAILWAY_CLI_PATTERNS]] | upstream | 0.20 |
