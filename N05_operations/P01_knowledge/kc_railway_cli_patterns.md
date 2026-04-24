---
id: KC_N05_RAILWAY_CLI_PATTERNS
kind: knowledge_card
8f: F3_inject
pillar: P01
title: Railway CLI — Commands, CI/CD & Deploy Patterns
domain: N05_operations
tags: [railway, cli, deploy, ci-cd, automation]
quality: 9.0
sources:
  - https://docs.railway.com/guides/cli
created: 2026-04-01
related:
  - p01_kc_railway_cli_patterns
  - p01_kc_railway_platform_deep
  - p08_ac_railway_superintendent
  - p02_agent_railway_superintendent
  - p12_dr_railway_superintendent
  - p03_sp_railway_superintendent
  - KC_N05_RAILWAY_PLATFORM_DEEP
  - p01_kc_deploy_paas
  - KC_N05_POSTGRESQL_RAILWAY
  - spec_n05_railway_superintendent
---

# Railway CLI — Commands, CI/CD & Deploy Patterns

## 1. Installation

```bash
# macOS/Linux (npm)
npm install -g @railway/cli

# macOS (Homebrew)
brew install railway

# Windows (scoop)
scoop install railway

# Verify
railway --version
```

## 2. Authentication

```bash
railway login                    # browser-based OAuth
railway login --browserless      # for headless/CI environments (shows token in terminal)
railway logout
railway whoami                   # show current authenticated user
```

## 3. Project Management

```bash
railway init                     # create new Railway project
railway link                     # link current directory to existing project (interactive)
railway link --project-id <id>   # link by project ID
railway unlink                   # remove project link from current dir
railway list                     # list all projects for current user
railway status                   # show linked project/environment/service info
railway open                     # open current project in browser
railway delete                   # delete current project
```

## 4. Service Management

```bash
railway service                  # interactive service selector (sets default for session)
railway add                      # add service interactively
railway add --database postgres  # add PostgreSQL plugin
railway add --database redis     # add Redis plugin
railway add --database mysql     # add MySQL plugin
railway add --database mongo     # add MongoDB plugin
railway scale                    # adjust service resources (replicas, vCPU, RAM)
```

## 5. Deployment

```bash
railway up                       # deploy current directory to linked service
railway up --detach              # deploy without streaming logs (non-blocking)
railway up --service my-api      # deploy to specific service
railway up --environment staging # deploy to specific environment

railway deploy --template postgres  # deploy from template marketplace
railway redeploy                    # redeploy current active deployment (same image)
railway restart                     # restart running service
railway down                        # remove latest deployment (keeps service)
```

**Flag reference:**
| Flag | Short | Effect |
|------|-------|--------|
| `--service` | `-s` | Target service by name |
| `--environment` | `-e` | Target environment |
| `--detach` | | Don't stream logs |
| `--json` | | Output as JSON |
| `--yes` | `-y` | Skip confirmations |

## 6. Environment Management

```bash
railway environment              # interactive environment switcher
railway environment new staging  # create environment named "staging"
railway environment delete dev   # delete environment
```

## 7. Variable Management

```bash
railway variable list            # list all variables for current service/env
railway variable list --json     # output as JSON
railway variable set KEY=value   # create or update variable
railway variable set KEY=value OTHER=val  # set multiple at once
railway variable delete KEY      # remove variable
```

**Import from file:**
```bash
railway variable set < .env      # import from .env file (pipe)
```

## 8. Local Development

```bash
# Run local command with Railway env vars injected
railway run npm start
railway run python app.py
railway run -- python -m pytest  # use -- to pass flags

# Open shell with all Railway variables injected
railway shell

# Run all project services locally via Docker
railway dev
```

`railway run` injects all variables from the linked service + environment. No `.env` file needed locally.

## 9. Logs

```bash
railway logs                     # stream live deployment logs
railway logs --build             # view build (not runtime) logs
railway logs -n 100              # last 100 lines
railway logs --service api       # logs for specific service
railway logs --environment prod  # logs for specific environment
railway logs --json              # JSON structured output
```

## 10. SSH & Database Access

```bash
railway ssh                      # SSH into running container
railway connect                  # interactive DB shell (psql, redis-cli, etc.)
railway connect postgres         # connect to specific DB service
```

## 11. Networking & Domains

```bash
railway domain                        # generate railway.app subdomain
railway domain example.com            # assign custom domain
railway domain --service frontend     # domain for specific service
```

## 12. CI/CD with RAILWAY_TOKEN

### Token Types

| Token | Variable | Scope |
|-------|----------|-------|
| Project token | `RAILWAY_TOKEN` | Project-level actions (deploy, vars) |
| Account token | `RAILWAY_API_TOKEN` | Account-level actions (create projects, etc.) |

### GitHub Actions Pattern

```yaml
# .github/workflows/deploy.yml
name: Deploy to Railway
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install Railway CLI
        run: npm install -g @railway/cli
      - name: Deploy
        run: railway up --detach
        env:
          RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}
```

### Non-interactive deploy pattern
```bash
# Minimal CI deploy (no prompts)
RAILWAY_TOKEN=xxx railway up --detach --environment production --service api
```

### Browserless login for CI
```bash
# Get token interactively first, then use RAILWAY_TOKEN
railway login --browserless
# Copy the token shown, set as secret in CI
```

## 13. Common Workflows

### Deploy + Check Logs
```bash
railway up && railway logs -n 50
```

### Deploy to Multiple Environments
```bash
# Staging first
RAILWAY_TOKEN=$STAGING_TOKEN railway up --environment staging
# After approval, production
RAILWAY_TOKEN=$PROD_TOKEN railway up --environment production
```

### Debug Production Issue
```bash
railway logs --environment production -n 200
railway ssh --service api --environment production
```

### Rollback
```bash
railway redeploy  # re-runs last successful deployment
# Or: use web UI to select a specific historical deployment
```

### Link Project in CI
```bash
# Use environment variables instead of interactive link
export RAILWAY_TOKEN=xxx
export RAILWAY_PROJECT_ID=yyy
export RAILWAY_SERVICE_ID=zzz
railway up --detach
```

## 14. Global Flags (All Commands)

```
-s, --service       Target service
-e, --environment   Target environment
--json              JSON output mode
-y, --yes           Skip all confirmations
-h, --help          Help for any command
-V, --version       CLI version
```

## Anti-Patterns

- Never run `railway up` without confirming `railway status` first (wrong service/env)
- Never use `RAILWAY_API_TOKEN` for deploy-only CI (use `RAILWAY_TOKEN` — least privilege)
- Never `railway delete` without confirming the project name (irreversible)
- Avoid `railway logs` without `-n` flag in CI (hangs waiting for new log lines)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_railway_cli_patterns]] | sibling | 0.81 |
| [[p01_kc_railway_platform_deep]] | sibling | 0.73 |
| [[p08_ac_railway_superintendent]] | downstream | 0.70 |
| [[p02_agent_railway_superintendent]] | downstream | 0.61 |
| [[p12_dr_railway_superintendent]] | downstream | 0.61 |
| [[p03_sp_railway_superintendent]] | downstream | 0.58 |
| [[KC_N05_RAILWAY_PLATFORM_DEEP]] | sibling | 0.57 |
| [[p01_kc_deploy_paas]] | sibling | 0.56 |
| [[KC_N05_POSTGRESQL_RAILWAY]] | sibling | 0.50 |
| [[spec_n05_railway_superintendent]] | downstream | 0.49 |
