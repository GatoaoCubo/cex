---
id: env_dependencies_newpc
kind: context_doc
8f: F3_inject
title: N05 Environment Dependencies -- New PC Map
nucleus: N05
version: 2.0.0
pillar: P01
quality: 8.9
created: 2026-04-13
mission: NEWPC_SETUP
tags: [dependencies, environment, newpc, operations]
related:
  - self_audit_newpc
  - spec_zero_install
  - kc_cex_distribution_model
  - bld_collaboration_agent_package
  - audit_pi_references
  - n06_api_access_pricing
  - agent-package-builder
  - bld_tools_model_provider
  - p01_kc_api_client
  - kc_api_reference
---

# Environment Dependencies -- New PC (2026-04-13)

> Complete dependency map for CEX development on Windows 11 Pro 10.0.26200

## Core Runtimes

| Runtime | Version | Path | Status |
|---------|---------|------|--------|
| Python | 3.14.4 | `{{USER_HOME}}\AppData\Local\Python\pythoncore-3.14-64\python.exe` | Installed |
| Node.js | v24.14.1 | System PATH | Installed |
| npm | 11.11.0 | System PATH | Installed |
| Git | 2.53.0.windows.2 | System PATH | Installed |
| Git LFS | Configured | lfs.repositoryformatversion=0 | Installed |

## CLI Tools

| Tool | Version | Purpose | Status |
|------|---------|---------|--------|
| claude | 2.1.104 | Claude Code CLI (N01-N07 nucleus runtime) | Installed |
| gh | 2.89.0 | GitHub CLI (PRs, issues, checks) | Installed |
| pip | 26.0.1 | Python package manager | Installed |
| uv | 0.11.6 | Fast Python package installer | Installed (pip pkg) |

## Python Packages (Installed)

### AI/LLM Providers

| Package | Version | Used By |
|---------|---------|---------|
| anthropic | 0.94.0 | Claude API -- all nuclei via cex_router.py |
| openai | 2.31.0 | OpenAI-compatible providers |
| google-genai | 1.72.0 | Gemini API -- fallback provider |
| tiktoken | 0.12.0 | Token counting -- cex_token_budget.py |

### Data & Validation

| Package | Version | Used By |
|---------|---------|---------|
| PyYAML | 6.0.3 | Frontmatter parsing, config loading |
| pydantic | 2.12.5 | Schema validation, type safety |
| pydantic_core | 2.41.5 | Pydantic internals |
| annotated-types | 0.7.0 | Pydantic type annotations |
| typing_extensions | 4.15.0 | Backported typing features |
| typing-inspection | 0.4.2 | Runtime type inspection |

### HTTP & Networking

| Package | Version | Used By |
|---------|---------|---------|
| httpx | 0.28.1 | Async HTTP (anthropic SDK) |
| httpcore | 1.0.9 | HTTP/1.1 + HTTP/2 transport |
| requests | 2.33.1 | Sync HTTP client |
| urllib3 | 2.6.3 | Connection pooling |
| certifi | 2026.2.25 | CA certificates |
| h11 | 0.16.0 | HTTP/1.1 state machine |
| websockets | 16.0 | WebSocket client |

### Utilities

| Package | Version | Used By |
|---------|---------|---------|
| regex | 2026.4.4 | Advanced regex (Unicode, lookahead) |
| tqdm | 4.67.3 | Progress bars (batch operations) |
| tenacity | 9.1.4 | Retry with backoff (API calls) |
| colorama | 0.4.6 | ANSI colors on Windows terminal |
| docstring_parser | 0.17.0 | Docstring extraction |
| jiter | 0.14.0 | Fast JSON parsing |
| sniffio | 1.3.1 | Async library detection |
| anyio | 4.13.0 | Async I/O abstraction |
| idna | 3.11 | Internationalized domain names |
| charset-normalizer | 3.4.7 | Character encoding detection |
| distro | 1.9.0 | OS distribution detection |

### Crypto & Auth

| Package | Version | Used By |
|---------|---------|---------|
| cryptography | 46.0.7 | TLS, token signing |
| cffi | 2.0.0 | C Foreign Function Interface |
| pycparser | 3.0 | C parser for cffi |
| google-auth | 2.49.2 | Google API authentication |
| pyasn1 | 0.6.3 | ASN.1 codec |
| pyasn1_modules | 0.4.2 | ASN.1 module definitions |

## Node.js Global Packages

| Package | Status |
|---------|--------|
| (none) | No global packages installed |

**Note**: MCP servers are installed on-demand via `npx -y`. No global installs required.

## Environment Variables

| Variable | Shell Session (2026-04-13) | Prior Session (2026-04-12) | Purpose |
|----------|---------------------------|---------------------------|---------|
| GITHUB_TOKEN | MISSING | SET | GitHub API (gh CLI, MCP server) |
| ANTHROPIC_API_KEY | MISSING | SET | Claude API (all nuclei) |
| FIRECRAWL_API_KEY | MISSING | SET | Web scraping (N01 research) |
| BRAVE_API_KEY | MISSING | SET | Brave Search API (N01 research) |
| SUPABASE_ACCESS_TOKEN | MISSING | SET | Supabase database access |
| CANVA_CLIENT_ID | MISSING | SET | Canva design API (N02 marketing) |
| STRIPE_SECRET_KEY | MISSING | SET | Stripe payments (N06 commercial) |
| HOTMART_CLIENT_ID | MISSING | SET | Hotmart marketplace (N06 commercial) |

**Note**: All 8 were SET in prior session. Current Claude Code session has ANTHROPIC_API_KEY via its own config -- nucleus execution is unaffected. Other vars affect external tool integrations only.

## MCP Servers (N05 config: .mcp-n05.json)

| Server | Configured Package | npm Status | Action Needed |
|--------|--------------------|------------|---------------|
| postgres | `@anthropic-ai/mcp-server-postgres` | 404 NOT FOUND | Update to `@modelcontextprotocol/server-postgres` |
| github | `@anthropic/mcp-server-github` | 404 NOT FOUND | Update to `@modelcontextprotocol/server-github` |

## Missing / Not Installed

| Item | Category | Impact | Priority |
|------|----------|--------|----------|
| Git pre-commit hook | Dev tooling | ASCII enforcement not automated | MEDIUM |
| Docker | Containerization | No local container testing | LOW (not required for CEX core) |
| PostgreSQL client | Database | No local DB testing | LOW (MCP server handles remote) |

## Disk

| Drive | Total | Used | Free | Use% |
|-------|-------|------|------|------|
| C:/ | 1.9 TB | 430 GB | 1.5 TB | 23% |

## Compatibility Notes

- Python 3.14.4 is bleeding-edge. All CEX tools tested and working.
- Node v24.14.1 is current LTS. npx functional for MCP server on-demand install.
- Windows terminal defaults to cp1252. ASCII-only code rule prevents UnicodeEncodeError.
- Git LFS configured but no tracked patterns detected (no large binaries in repo).

## Boundary

Domain context for prompt hydration. NOT a knowledge_card (no density gate) nor a glossary_entry (does not define a term).


## 8F Pipeline Function

Primary function: **INJECT**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[self_audit_newpc]] | sibling | 0.31 |
| [[spec_zero_install]] | sibling | 0.28 |
| [[kc_cex_distribution_model]] | related | 0.21 |
| [[bld_collaboration_agent_package]] | downstream | 0.20 |
| [[audit_pi_references]] | related | 0.18 |
| [[n06_api_access_pricing]] | downstream | 0.18 |
| [[agent-package-builder]] | downstream | 0.17 |
| [[bld_tools_model_provider]] | downstream | 0.17 |
| [[p01_kc_api_client]] | downstream | 0.17 |
| [[kc_api_reference]] | related | 0.17 |
