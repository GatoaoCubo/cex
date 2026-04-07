---
id: p01_kc_github_actions
kind: knowledge_card
pillar: P01
title: "GitHub Actions — CI/CD Workflow Patterns"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.2
tags: [github-actions, ci-cd, workflows, automation, deploy]
tldr: "11 production workflows distilled from codexa-core: CI (lint+test+build), quality gate (5D validation), security (5 scanners), deploy (Railway+Docker), release (PyPI), PR validation, self-hydrate cron."
density_score: 0.92
---

# GitHub Actions Patterns

## Workflow Catalog (codexa-core — 11 workflows)

| Workflow | Trigger | Jobs | Purpose |
|----------|---------|------|---------|
| ci.yml | push/PR | lint → test → build → docker | Full CI pipeline |
| quality.yml | push/PR (*.md,*.py) | pytest + 5D validate + python-checks | Artifact quality gate |
| security.yml | push/PR + weekly cron | dependency + secret + SAST + container + CodeQL | 5-layer security |
| deploy-cloud.yml | push main | quality → build → deploy | Railway + Render |
| deploy-railway.yml | push/release | validate → deploy → health → rollback → notify | Railway with rollback |
| pr-validation.yaml | PR | lint + k8s-validate + docker-build + pr-size + deps-check | PR hygiene |
| publish.yml | release/tag | build → test-install (3x3 matrix) → publish | PyPI publish |
| release.yml | dispatch/tag | prepare → build → release → notify | GitHub Release |
| ci-cd.yaml | push/dispatch | test → security → build → deploy | Composite pipeline |
| self-hydrate-cron.yml | daily 03:00 UTC | extract → threshold-check → commit | Self-improvement |
| deploy-eks.yml | dispatch | build → deploy EKS | Kubernetes deploy |

## Core Patterns

### Concurrency Control

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true  # Kill old runs on new push
```

### Path Filtering

```yaml
on:
  push:
    paths:
      - 'src/**/*.py'
      - 'tests/**'
      - '.github/workflows/ci.yml'
    paths-ignore:
      - '**.md'
      - 'docs/**'
```

### Matrix Testing

```yaml
strategy:
  fail-fast: false
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
    python-version: ['3.10', '3.11', '3.12']
```

### Caching

```yaml
- uses: actions/setup-python@v5
  with:
    python-version: '3.12'
    cache: 'pip'  # Auto-cache pip downloads
```

### Job Dependencies + Outputs

```yaml
jobs:
  build:
    outputs:
      version: ${{ steps.ver.outputs.version }}
    steps:
      - id: ver
        run: echo "version=1.0.0" >> $GITHUB_OUTPUT

  deploy:
    needs: [build]
    if: needs.build.outputs.version != ''
```

### Secrets + Environment

```yaml
jobs:
  deploy:
    environment:
      name: production
      url: https://api.example.com
    steps:
      - run: railway up
        env:
          RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}
```

## CI Pipeline (Standard)

```yaml
name: CI
on: [push, pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12', cache: 'pip' }
      - run: pip install ruff && ruff check .

  test:
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12', cache: 'pip' }
      - run: pip install -e ".[dev]"
      - run: pytest --cov --cov-report=xml
      - uses: codecov/codecov-action@v4

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-buildx-action@v3
      - uses: docker/build-push-action@v5
        with: { push: false, cache-from: 'type=gha', cache-to: 'type=gha,mode=max' }
```

## Security Pipeline (5-Layer)

1. **Dependency scan**: `pip-audit` + `safety check`
2. **Secret scan**: `gitleaks/gitleaks-action@v2`
3. **SAST**: `bandit -r src/` + `semgrep` (p/python, p/security-audit)
4. **Container scan**: `aquasecurity/trivy-action` (CRITICAL,HIGH)
5. **CodeQL**: `github/codeql-action` (python, security-extended)

## Deploy Pipeline (Railway)

```yaml
deploy:
  needs: [validate]
  steps:
    - uses: actions/checkout@v4
    - run: npm i -g @railway/cli
    - run: railway up --service $SERVICE --environment $ENV
      env: { RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }} }
    - name: Health check
      run: |
        for i in $(seq 1 10); do
          curl -sf "$URL/health" && exit 0 || sleep 15
        done
        exit 1
```

## Step Summary (Reporting)

```yaml
- run: |
    echo "## Test Results" >> $GITHUB_STEP_SUMMARY
    echo "| Check | Status |" >> $GITHUB_STEP_SUMMARY
    echo "|-------|--------|" >> $GITHUB_STEP_SUMMARY
    echo "| Tests | ${{ needs.test.result }} |" >> $GITHUB_STEP_SUMMARY
```

## Anti-Patterns

- ❌ No `concurrency` — parallel runs waste resources and conflict
- ❌ `fail-fast: true` in matrix — hides platform-specific failures
- ❌ Secrets in workflow files (use repository secrets)
- ❌ `continue-on-error: true` without explicit failure check
- ❌ No path filtering — runs on every commit including docs
