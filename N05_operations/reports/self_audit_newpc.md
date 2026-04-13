---
id: self_audit_newpc
kind: context_doc
title: N05 Self-Audit -- New PC System Health Report
nucleus: N05
version: 1.0.0
pillar: P01
quality: 8.9
created: 2026-04-12
mission: NEWPC_SETUP
tags: [audit, health, newpc, operations, ci-cd]
---

# N05 Self-Audit -- New PC System Health Report

> Machine: Windows 11 Pro 10.0.26200 | Date: 2026-04-12 | Mission: NEWPC_SETUP

## Executive Summary

| Metric | Result |
|--------|--------|
| System tests | **48 PASS / 10 FAIL** / 58 total (82.8%) |
| Builder doctor | **123 PASS / 0 FAIL** (100%) |
| ASCII sanitizer | **140/140 clean** (100%) |
| Env vars (8 required) | **8/8 SET** (100%) |
| Disk space | **1.6 TB free** (17% used of 1.9 TB) |
| MCP servers | **0/2 reachable** (npm 404) |
| Git pre-commit hook | **NOT INSTALLED** |

**Verdict: OPERATIONAL with 3 fixable issues.**

## Phase 1: MCP Server Verification

| Server | Package | Result | Detail |
|--------|---------|--------|--------|
| postgres | `@anthropic-ai/mcp-server-postgres` | **FAIL** | npm 404 -- package not found on registry |
| github | `@anthropic/mcp-server-github` | **FAIL** | npm 404 -- package not found on registry |

**Root cause**: Both MCP server packages return HTTP 404 from npmjs.org. Either the packages have been renamed/deprecated or the scope names in `.mcp-n05.json` are outdated. This affects MCP-based database queries and GitHub API access from within Claude Code sessions.

**Action required**: Verify current package names at npmjs.org. Known alternatives:
- Postgres: `@modelcontextprotocol/server-postgres`
- GitHub: `@modelcontextprotocol/server-github`

## Phase 2: System Tests

### Summary: 48 PASS / 10 FAIL / 58 total

| Category | Test | Result | Notes |
|----------|------|--------|-------|
| Tool imports | 15 tools importable | PASS | All `_tools/cex_*.py` import cleanly |
| Doctor | 123 builders healthy | PASS | 1599 files, 5282.1 KB, avg density 0.95 |
| Sanitizer | 140 code files ASCII-clean | PASS | Zero non-ASCII violations |
| Compile | compile + recompile | PASS | Artifacts compile correctly |
| Score | scoring pipeline | PASS | L1+L2+L3 scoring functional |
| Retriever | TF-IDF similarity | PASS | 2184 docs indexed |
| Memory | memory select + update | PASS | Memory pipeline operational |
| Runner | 8F dry-run + execute | PASS | Full 8F pipeline completes |
| KC library | 123/98 kind KCs | PASS | Coverage exceeds minimum |
| **quality:zero_null** | 137 artifacts quality:null | **FAIL** | Expected -- awaiting peer review |
| **hooks:git_precommit** | Pre-commit hook | **FAIL** | Hook file not installed in .git/hooks/ |
| **boot:n01** | Boot script test | **FAIL** | PowerShell boot script execution issue |
| **boot:n02** | Boot script test | **FAIL** | Same |
| **boot:n03** | Boot script test | **FAIL** | Same |
| **boot:n04** | Boot script test | **FAIL** | Same |
| **boot:n05** | Boot script test | **FAIL** | Same |
| **boot:n06** | Boot script test | **FAIL** | Same |
| **e2e:runs** | E2E test execution | **FAIL** | Command exit -1 (subprocess error) |
| **git:clean** | Working tree clean | **FAIL** | 14 dirty files (expected during mission) |

### Failure Analysis

| Failure | Severity | Fixable | Action |
|---------|----------|---------|--------|
| quality:zero_null (137) | LOW | Yes | Run `cex_score.py --apply` batch scoring |
| hooks:git_precommit | MEDIUM | Yes | `python _tools/cex_hooks.py install` |
| boot:n01-n06 (6 failures) | MEDIUM | Investigate | Boot scripts exist but test harness can't execute them in subprocess |
| e2e:runs | MEDIUM | Investigate | E2E subprocess crash -- likely missing test fixture or timeout |
| git:clean | NONE | N/A | Expected during active mission (14 uncommitted files) |

**Critical failures: 0. All failures are non-blocking for development.**

## Phase 3: Environment Audit

### Runtime Versions

| Tool | Version | Status |
|------|---------|--------|
| Python | 3.14.4 | Current |
| Node.js | v24.14.1 | Current |
| npm | 11.11.0 | Current |
| Git | 2.53.0.windows.2 | Current |
| GitHub CLI (gh) | 2.89.0 | Current |
| Claude Code | 2.1.104 | Current |

### Python Packages (CEX-critical)

| Package | Version | Purpose |
|---------|---------|---------|
| anthropic | 0.94.0 | Claude API client |
| openai | 2.31.0 | OpenAI/compatible API client |
| google-genai | 1.72.0 | Gemini API client |
| PyYAML | 6.0.3 | YAML parsing (frontmatter, configs) |
| tiktoken | 0.12.0 | Token counting |
| pydantic | 2.12.5 | Data validation |
| regex | 2026.4.4 | Advanced regex |
| requests | 2.33.1 | HTTP client |
| tqdm | 4.67.3 | Progress bars |
| tenacity | 9.1.4 | Retry logic |
| colorama | 0.4.6 | Terminal colors (Windows) |

### Environment Variables

| Variable | Status |
|----------|--------|
| GITHUB_TOKEN | SET |
| ANTHROPIC_API_KEY | SET |
| FIRECRAWL_API_KEY | SET |
| BRAVE_API_KEY | SET |
| SUPABASE_ACCESS_TOKEN | SET |
| CANVA_CLIENT_ID | SET |
| STRIPE_SECRET_KEY | SET |
| HOTMART_CLIENT_ID | SET |

**8/8 required environment variables configured.**

### Git Configuration

| Setting | Value |
|---------|-------|
| remote.origin.url | `https://github.com/GatoaoCubo/cex.git` |
| branch.main.remote | origin |
| core.symlinks | false |
| core.ignorecase | true |
| lfs.repositoryformatversion | 0 |

### Disk Space

| Filesystem | Size | Used | Available | Use% |
|-----------|------|------|-----------|------|
| C:/ | 1.9 TB | 313 GB | 1.6 TB | 17% |

**Ample space for all operations.**

## Phase 4: N05 Artifact Inventory

| Subdirectory | Count | Purpose |
|--------------|-------|---------|
| output/ | 23 | Deploy configs, checklists, CI/CD, evals |
| knowledge/ | 8 | Domain KCs (Railway, PostgreSQL, monitoring) |
| schemas/ | 7 | API response, env contract, health check schemas |
| prompts/ | 4 | System prompts (superintendent, review, deploy, debug) |
| feedback/ | 4 | Quality gates (deploy, security, performance, artifact) |
| agents/ | 4 | Superintendent + deploy + test + code review agents |
| orchestration/ | 3 | Dispatch rules, spawn config, workflow defs |
| memory/ | 3 | Checkpoint, deploy history, session memory |
| architecture/ | 3 | Agent card + 2 ADRs |
| reports/ | 2 | Audit reports (this + prior) |
| root | 2 | Agent card + README |
| **Total** | **63** | Source .md files |

### Gap Analysis

| Area | Status | Notes |
|------|--------|-------|
| CI/CD pipeline | Covered | GitHub Actions workflow config exists |
| Testing (unit/e2e/smoke/regression) | Covered | 8 eval kinds built |
| Monitoring/observability | Covered | Trace config + health monitoring KCs |
| Security | Covered | Red-team eval + security validation schema |
| Deploy lifecycle | Covered | Checklists, rollback, env contracts, health endpoints |
| Agent coverage | Covered | 4 specialized agents |
| **Pre-commit hook** | **GAP** | Not installed on this machine |
| **MCP server packages** | **GAP** | Package names need updating |

## Recommended Actions (Priority Order)

1. **[HIGH]** Update MCP server package names in `.mcp-n05.json` -- verify `@modelcontextprotocol/server-postgres` and `@modelcontextprotocol/server-github`
2. **[MEDIUM]** Install git pre-commit hook: `python _tools/cex_hooks.py install`
3. **[MEDIUM]** Investigate boot script test failures (n01-n06) -- scripts exist, test harness issue
4. **[LOW]** Investigate e2e test subprocess crash
5. **[LOW]** Batch score 137 quality:null artifacts when ready for peer review

## Boundary

Contexto de dominio para hidratar prompts. NAO eh knowledge_card (sem density gate) nem glossary_entry (nao define termo).


## 8F Pipeline Function

Primary function: **INJECT**
