---
id: p01_kc_railway_cli_patterns
kind: knowledge_card
pillar: P01
title: "Railway CLI Patterns — Commands, Deploy & CI/CD"
version: 1.0.0
created: 2026-04-01
updated: 2026-04-01
author: knowledge-card-builder
domain: infrastructure
quality: 9.0
tags: [railway, cli, deploy, paas, infrastructure]
tldr: "Railway CLI core patterns: login→link→up workflow, env vars via railway run, GitHub Actions CI/CD with RAILWAY_TOKEN, project/service/environment hierarchy"
when_to_use: "Deploying to Railway platform, setting up Railway CI/CD, or debugging Railway deployments"
keywords: [railway, cli, deploy, paas, environment, variables]
long_tails:
  - railway cli commands cheat sheet
  - railway github actions deployment
  - railway environment variables injection
axioms:
  - "ALWAYS verify `railway status` before `railway up` to prevent wrong service deploys"
  - "NEVER use RAILWAY_API_TOKEN for CI deploys — use project-scoped RAILWAY_TOKEN"  
  - "IF deploying in CI THEN use --detach flag to prevent log streaming hangs"
linked_artifacts:
  primary: null
  related: []
density_score: 0.88
data_source: "https://docs.railway.com/guides/cli"
---

# Railway CLI Patterns

## Quick Reference
```yaml
topic: Railway CLI deployment patterns
scope: Core commands, CI/CD integration, variable management
owner: infrastructure_team
criticality: high
```

## Key Concepts

- **Project Hierarchy**: Account → Project → Service → Environment (prod/staging)
- **Authentication Flow**: `railway login` → browser OAuth → token stored locally
- **Link Pattern**: `railway link` connects local dir to Railway project/service
- **Deploy Command**: `railway up` builds + deploys current directory to linked service  
- **Variable Injection**: `railway run <cmd>` executes with all Railway vars injected
- **Environment Targeting**: `-e/--environment` flag targets staging vs production
- **Service Targeting**: `-s/--service` flag when multiple services in project

## Patterns

### 1. Local Development Pattern
```bash
railway link          # connect to project
railway run npm start  # run with Railway env vars
railway shell         # interactive shell with vars
```

### 2. CI/CD GitHub Actions Pattern  
```yaml
- name: Deploy
  run: railway up --detach --service api
  env:
    RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}
```

### 3. Multi-Environment Deploy Pattern
```bash
# Staging
railway up -e staging -s api
# Production (after approval)
railway up -e production -s api
```

## Golden Rules

- **Verify Before Deploy**: Always `railway status` before `railway up`
- **Use Project Tokens**: RAILWAY_TOKEN (not RAILWAY_API_TOKEN) for CI
- **Detach in CI**: Use `--detach` flag to prevent log streaming hangs
- **Environment Explicit**: Always specify `-e` in multi-env projects

## References

- Railway CLI Docs: https://docs.railway.com/guides/cli
- Related artifact: kc_railway_platform_deep.md
- GitHub Actions Railway: https://github.com/railwayapp/cli

**F7 GOVERN**: Score estimate 8.8/10. Gates: 7/7 hard gates. Density: 0.88
**F8 COLLABORATE**: Ready for save, compile, commit, signal