---
id: spec_mcp_security_policy
kind: constraint_spec
pillar: P06
title: "MCP Security Policy -- CEX Open-Source"
version: "1.0.0"
created: "2026-04-20"
author: "n04_knowledge"
domain: security
quality: 8.7
tags: [security, mcp, open-source, access-control, secrets]
tldr: "Read-only MCP policy for N07 pre-flight; zero secrets in repo; graceful degradation when keys absent; full audit trail per Phase 0 run."
density_score: 1.0
---

# MCP Security Policy -- CEX Open-Source

## Executive Summary

CEX grants N07 a curated **read-only** MCP set for pre-flight context gathering.
No nucleus holds write/mutate capability through MCP except N03 (GitHub write)
and N05 (GitHub + postgres write), which are explicitly scoped and documented.
This policy governs token safety, access control, secret management, audit
trail, and contributor safety for a public open-source deployment.

## Threat Model

| Threat | Likelihood | Mitigation |
|--------|-----------|------------|
| Hardcoded secrets committed to repo | High (common mistake) | env-var-only policy + pre-commit hook |
| N07 writing to GitHub via MCP | Medium | `deny` list in `n07.json`; allowlist is get/list/search only |
| API key exfiltration via logs | Medium | `cex_preflight_mcp.py` never logs auth headers or key values |
| Contributor accidentally activating paid providers | Low | `disabled: true` default on firecrawl + brave-search |
| Pre-flight crash blocking dispatch | Medium | Graceful skip on missing keys; Phase 0 failures are non-fatal |
| Cross-nucleus credential bleed | Low | Per-nucleus MCP config files (`.mcp-n0X.json`), no shared secrets |

## N07 MCP Access Policy (PREFLIGHT_EXPANSION)

N07 is the SOLE MCP gateway for pre-flight context gathering. N07 has:

### Allowed Operations

| Server | Allowed | Rationale |
|--------|---------|-----------|
| `fetch` | ALL (public URLs only) | Direct HTTP GET for web context; no auth |
| `markitdown` | ALL | Pure document conversion; no auth; no external calls |
| `github` | `get_*`, `list_*`, `search_*` | Read-only repo/issue context for code-related kinds |
| `firecrawl` | `scrape`, `search`, `map` | Research kinds; requires API key; off by default |
| `brave-search` | ALL | Web search fallback; requires API key; off by default |

### Denied Operations (N07)

All GitHub mutation operations are explicitly denied in `.claude/nucleus-settings/n07.json`:

```json
"deny": [
  "mcp__github__create_*",
  "mcp__github__update_*",
  "mcp__github__merge_*",
  "mcp__github__push_*",
  "mcp__github__fork_*",
  "mcp__github__delete_*",
  "mcp__firecrawl__firecrawl_crawl",
  "mcp__firecrawl__firecrawl_agent",
  "mcp__firecrawl__firecrawl_browser_*"
]
```

### Excluded from N07 (by design)

| Server | Reason |
|--------|--------|
| `playwright` | Browser automation is a BUILD tool; security: full browser control |
| `postgres` | DB queries are nucleus-specific; security: full write access |
| `supabase` | Backend API; security: data mutation capability |
| `canva` | Design write access; zero pre-flight value |
| `notebooklm` | Session-stateful; interactive auth required |
| `stripe` | Financial API; zero pre-flight value; high risk |

## Secret Management

### Rules

1. **No secrets in the repo**. `.env`, `*.key`, `*_secret*` are gitignored.
2. **`.mcp-n07.json` references env vars only**: `${GITHUB_TOKEN}`, `${BRAVE_API_KEY}`,
   `${FIRECRAWL_API_KEY}`. Never hardcoded values. Pre-commit hook rejects secrets.
3. **GITHUB_TOKEN scope for N07**: read-only PAT with `repo:read`, `issues:read`,
   `pull_requests:read`. The spec recommends a separate PAT from N03's write token,
   but a shared token is accepted if scoped to these operations (DP1 decision: shared).
4. **Graceful degradation**: if `GITHUB_TOKEN` is absent, GitHub server is excluded
   from the session. If `BRAVE_API_KEY` is absent, brave-search is skipped. Phase 0
   continues with available providers and never crashes on missing credentials.

### Environment Variable Reference

| Variable | Required | Default behavior if absent |
|----------|----------|---------------------------|
| `GITHUB_TOKEN` | Optional | GitHub MCP absent; no crash |
| `BRAVE_API_KEY` | Optional | brave-search skipped (disabled by default) |
| `FIRECRAWL_API_KEY` | Optional | firecrawl skipped (disabled by default) |

## No Logging of Secrets

`_tools/cex_preflight_mcp.py` enforces:
- Auth headers are NEVER written to log files
- API key values are NEVER included in audit JSON
- Only these fields are logged: query text, result count, latency_ms, provider, status
- Audit file path: `.cex/cache/preflight/{hash}_audit.json`

Violation example (NEVER do this):
```python
# WRONG
logger.info(f"Calling GitHub with token={os.environ['GITHUB_TOKEN']}")

# CORRECT
logger.info(f"Calling GitHub (token present: {bool(os.environ.get('GITHUB_TOKEN'))})")
```

## Rate Limiting

| Provider | Free Tier Limit | Phase 0 Behavior |
|----------|----------------|-----------------|
| `fetch` | Unlimited (no API) | Max 3 URL fetches per run |
| `markitdown` | Unlimited (local) | No limit |
| `github` | 5000 req/hr (authenticated) | Max 3 queries per run; 1s delay between |
| `brave-search` | 2000 queries/month | Max 3 queries per run; 1s delay between |
| `firecrawl` | Varies by plan | Max 2 scrapes per run; 2s delay between |

Phase 0 budget: max 8192 tokens of external context per handoff (DP2 decision).
Phase 0 timeout: 60s wall time per run (DP3 decision).

## Audit Trail

Every Phase 0 run writes `.cex/cache/preflight/{hash}_audit.json`:

```json
{
  "timestamp": "2026-04-20T14:30:00Z",
  "kind": "knowledge_card",
  "nucleus": "n04",
  "task_hash": "abc123",
  "providers_used": ["fetch", "github"],
  "providers_skipped": ["brave-search"],
  "skip_reasons": {"brave-search": "BRAVE_API_KEY not set"},
  "queries": ["EdTech pricing 2026"],
  "urls_fetched": ["https://example.com/pricing"],
  "tokens_consumed": 3847,
  "latency_ms": 4200,
  "status": "ok"
}
```

Audit files are gitignored (`.cex/cache/` in `.gitignore`).
They are retained for 30 days then pruned by `cex_memory_age.py`.

## Contributor Safety

### Zero paid API keys required for base functionality

Contributors can run CEX with no API keys at all:
- `fetch` + `markitdown` work with zero config
- `github` token is free (any GitHub account, read scope)
- `firecrawl` and `brave-search` are `disabled: true` in `preflight_sources.yaml`

### Clear opt-in for premium providers

To enable premium providers, edit `.cex/config/preflight_sources.yaml`:
```yaml
optional_providers:
  - name: brave-search
    enabled: true        # <-- change from false to true
    ...
```

### First-run validation

`python _tools/cex_setup_validator.py` checks MCP config health:
- Verifies `.mcp-n07.json` exists
- Checks for hardcoded secrets (regex scan)
- Reports which providers are active vs. skipped
- Never fails hard; always reports graceful degradation path

## Per-Nucleus Access Summary

| Nucleus | Config | Write Access | Read-Only Servers |
|---------|--------|-------------|-------------------|
| N01 | `.mcp-n01.json` | none | brave-search, fetch, firecrawl, markitdown, notebooklm |
| N02 | `.mcp-n02.json` | canva (create assets) | markitdown, notebooklm, browser |
| N03 | `.mcp-n03.json` | github (write), canva | fetch |
| N04 | `.mcp-n04.json` | supabase, postgres | fetch, firecrawl, notebooklm |
| N05 | `.mcp-n05.json` | github (write), postgres | none |
| N06 | `.mcp-n06.json` | stripe, canva | fetch, markitdown, notebooklm |
| **N07** | `.mcp-n07.json` | **NONE** | fetch, markitdown, github(get/list/search), firecrawl(opt), brave-search(opt) |

N07 has the most restrictive MCP policy: read-only across all servers.
This is intentional. The orchestrator gathers context; it never mutates.

## Incident Response

If a secret is accidentally committed:
1. Rotate the key immediately (GitHub PAT, Brave, Firecrawl)
2. Run `git filter-repo --path .env --invert-paths` to purge from history
3. Force-push to invalidate cached refs
4. File a post-mortem in `.cex/learning_records/` with root cause

If a mutation is detected via N07 MCP (audit shows `create_*` or `push_*`):
1. Check `n07.json` deny list for drift
2. Verify `.mcp-n07.json` was not replaced by a broader config
3. Revoke and rotate the GitHub token
4. Update this policy with the new constraint

## References

| Resource | Path |
|----------|------|
| N07 settings (allow/deny) | `.claude/nucleus-settings/n07.json` |
| MCP config (N07) | `.mcp-n07.json` |
| Provider config | `.cex/config/preflight_sources.yaml` |
| Phase 0 module | `_tools/cex_preflight_mcp.py` |
| Access matrix | `_docs/security/mcp_access_matrix.md` |
| Kind tool dependencies | `_docs/security/kind_tool_dependency_matrix.md` |
| Smart router | `_tools/cex_router_v2.py` |
| Dispatch-depth rule | `.claude/rules/dispatch-depth.md` |
| Orchestrator rule | `.claude/rules/n07-orchestrator.md` |
