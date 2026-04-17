---
id: bld_sp_tools_software_project
kind: tools
pillar: P04
title: "Tools — Software Project Builder"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.1
tags: [builder, tools, software-project, python-tooling]
tldr: "Tool inventory: 4 build tools (hatch, uv, pip, setuptools), 3 quality tools (ruff, mypy, pytest), 3 deploy tools (docker, railway, render), 3 security tools (bandit, gitleaks, pip-audit), 2 MCP tools (github, fetch)."
density_score: 0.89
llm_function: CALL
---
# Tools

This ISO describes a software project: its repository layout, modules, and build graph.

## Build Tools

| Tool | Purpose | Install |
|------|---------|---------|
| **hatch** | Build backend (pyproject.toml → wheel) | `pip install hatch` |
| **uv** | Fast package manager (10-100x pip) | `pip install uv` |
| **pip** | Standard package installer (fallback) | Built-in |
| **setuptools** | Legacy build (avoid for new projects) | Built-in |

## Quality Tools

| Tool | Purpose | Install |
|------|---------|---------|
| **ruff** | Lint + format (replaces flake8+black+isort) | `pip install ruff` |
| **mypy** | Static type checking | `pip install mypy` |
| **pytest** | Test framework + coverage | `pip install pytest pytest-cov` |
| **pytest-asyncio** | Async test support | `pip install pytest-asyncio` |
| **hypothesis** | Property-based testing | `pip install hypothesis` |

## Deploy Tools

| Tool | Purpose | Install |
|------|---------|---------|
| **docker** | Container build + run | System install |
| **docker-compose** | Multi-container orchestration | System install |
| **railway** | PaaS deploy CLI | `npm i -g @railway/cli` |
| **supabase** | Database CLI (migrations, functions) | `npm i -g supabase` |

## Security Tools

| Tool | Purpose | Install |
|------|---------|---------|
| **bandit** | Python SAST | `pip install bandit` |
| **gitleaks** | Secret detection in git history | GitHub Action |
| **pip-audit** | Dependency vulnerability scan | `pip install pip-audit` |
| **trivy** | Container vulnerability scan | GitHub Action |
| **semgrep** | Multi-language SAST | GitHub Action |

## MCP Tools (N03 Config)

```json
{
  "mcpServers": {
    "github": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@anthropic/mcp-server-github"],
      "env": { "GITHUB_TOKEN": "${GITHUB_TOKEN}" }
    },
    "fetch": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@anthropic/mcp-server-fetch"]
    }
  }
}
```

## CEX Tools (Internal)

| Tool | Purpose |
|------|---------|
| cex_8f_runner | Build CEX artifacts via 8F pipeline |
| cex_compile | Compile .md → .yaml |
| cex_doctor | Health check |
| cex_score | Quality scoring |
| cex_hooks | Pre-commit validation |
| cex_system_test | Full system test |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |
