---
id: spec_zero_install
kind: context_doc
title: "CEX Zero-Install: Dependencies and Bootstrap on Fresh Machine"
version: 2.0.0
quality: null
created: 2026-04-07
updated: 2026-04-08
purpose: Everything needed to run CEX on a PC with nothing installed
---

# CEX Zero-Install Spec

## Dependency Stack (3 layers)

```
Layer 0: OS (Windows 10+, macOS, Linux)
  |
  +-- Layer 1: Runtimes (USER installs manually)
  |     +-- Python 3.12+
  |     +-- Node.js 18+ (LTS)
  |     +-- Git 2.40+
  |
  +-- Layer 2: Core Packages (setup.cmd installs)
  |     +-- npm: @anthropic-ai/claude-code (Claude Code CLI)
  |     +-- pip: pyyaml, tiktoken
  |     +-- pip: uv (for MCP server auto-install)
  |
  +-- Layer 3: Auto-managed (Claude Code handles)
        +-- MCP servers (npx/uvx auto-install on first use)
        +-- Any pip/npm deps Claude needs during work
```

## Runtime: Claude Code (the nucleus runtime)

Claude Code is the CLI that runs EVERY nucleus. CEX without Claude Code is a library without an interpreter.

| What Claude Code provides | How CEX uses it |
|---------------------------|-----------------|
| LLM conversation loop | Each nucleus = 1 Claude Code instance with Opus |
| `--model` flag | Routes each nucleus to its configured model |
| `--append-system-prompt` | Injects agent card + context + boot prompt |
| Tools (read, bash, edit, write) | How nuclei read/write artifacts, run Python tools |
| CLAUDE.md auto-load | Project rules, routing, pipeline loaded automatically |
| `.claude/agents/` | 125 builder sub-agents available to all nuclei |
| `.claude/commands/` | /build, /mission, /status, /validate, etc. |
| `.claude/rules/` | Behavioral rules auto-loaded per session |
| MCP server support | Each nucleus loads its `.mcp-n0X.json` config |
| Sub-agents | Parallel task execution within each nucleus |
| Context compression | Automatic compaction when window fills |
| `--dangerously-skip-permissions` | Autonomous mode for dispatched nuclei |

**Auth**: Claude Code uses Anthropic OAuth directly. No API key needed for Max/Pro plans.
On first run, it opens a browser for login. API keys are optional (set ANTHROPIC_API_KEY).

## Minimum Install (4 commands)

For a fresh Windows PC after runtimes are installed:

```cmd
:: 1. Install Claude Code
npm install -g @anthropic-ai/claude-code

:: 2. Install Python deps
pip install pyyaml tiktoken uv

:: 3. Clone and run
git clone https://github.com/<user>/cex.git
cd cex
boot\cex.cmd
```

Or just run `setup.cmd` which does all of the above with validation.

## Dependency Matrix

### Layer 1: Runtimes (USER installs -- 3 executables)

| Runtime | Version | Purpose | Install |
|---------|---------|---------|---------|
| **Python** | 3.12+ | All _tools/*.py (59 tools) | python.org or `winget install Python.3` |
| **Node.js** | 18+ LTS | Claude Code runtime | nodejs.org or `winget install OpenJS.NodeJS.LTS` |
| **Git** | 2.40+ | Version control, nucleus commits | git-scm.com or `winget install Git.Git` |

### Layer 2: Core Packages (setup.cmd installs)

| Package | Manager | Purpose | Size |
|---------|---------|---------|------|
| **@anthropic-ai/claude-code** | npm (global) | Agent CLI -- runs all nuclei | ~15MB |
| **pyyaml** | pip | YAML parsing (schemas, configs, kinds_meta) | 150KB |
| **tiktoken** | pip | Token counting (budget allocation) | 2MB |
| **uv** | pip | Python package runner for MCP servers (uvx) | 5MB |

### Layer 3: MCP Servers (AUTO-INSTALL on first use)

MCP servers install automatically via `npx -y` or `uvx`. No pre-install needed.

| Server | Auto-installs via | Used by |
|--------|-------------------|---------|
| firecrawl-mcp | `npx -y firecrawl-mcp` | N01, N04 |
| mcp-server-fetch | `uvx mcp-server-fetch` | N01, N04, N06 |
| markitdown-mcp | `npx -y markitdown-mcp` | N01, N02, N06 |
| brave-search | `npx -y @anthropic/mcp-server-brave-search` | N01 |
| notebooklm | `npx -y notebooklm-mcp@latest` | N01, N02, N04, N06 |
| puppeteer | `npx -y @anthropic-ai/mcp-server-puppeteer` | N02 |
| github | `npx -y @anthropic/mcp-server-github` | N03, N05 |

### What Claude Code installs on its own

Once Claude Code boots, it can `pip install` or `npm install` anything it needs.
The user never needs to pre-install anything beyond Layer 1 + Layer 2.

## Claude Code Config Files in CEX Repo

| Path | Purpose | Count |
|------|---------|-------|
| `CLAUDE.md` | Master project config (auto-loaded) | 1 |
| `.claude/rules/*.md` | Behavioral rules (auto-loaded) | 16 |
| `.claude/commands/*.md` | Custom /commands (/build, /mission, etc.) | 13+ |
| `.claude/agents/*.md` | Builder sub-agents (1 per kind) | 125 |
| `.claude/nucleus-settings/n0X.json` | Per-nucleus settings | 6 |
| `.mcp-n0X.json` | MCP server configs per nucleus | 6 |
| `boot/n0X.cmd` | Boot scripts that launch Claude Code with flags | 7+ |
| `.cex/config/context_self_select.md` | Self-select context injected on boot | 1 |

## Environment Variables

### Required for operation

| Variable | Purpose | How to get |
|----------|---------|-----------|
| None | Claude Code uses OAuth login (browser popup) | Free with Max/Pro subscription |

### Optional (per provider/service)

| Variable | Purpose | When needed |
|----------|---------|-------------|
| ANTHROPIC_API_KEY | Anthropic API access | Only for SDK/programmatic mode |
| FIRECRAWL_API_KEY | Firecrawl web scraping | Research features (N01) |
| BRAVE_API_KEY | Brave Search API | Research features (N01) |
| SUPABASE_URL | Supabase database | CRM features |
| SUPABASE_KEY | Supabase auth | CRM features |

## Tiers: What Works at Each Level

| Tier | Install | What works | What doesn't |
|------|---------|-----------|-------------|
| **Minimal** (Python + Node + Git) | 3 runtimes | All _tools/, doctor, compile, score | No LLM, no nuclei |
| **Core** (+ Claude Code + pip deps) | + 2 packages | Everything above + nucleus boot + grid | No MCP servers |
| **Full** (+ OAuth login) | + browser login | Everything: 6 nuclei, MCP, autoresearch | Needs subscription |

## Cross-Platform

| OS | Runtimes | Spawn method | Notes |
|----|----------|-------------|-------|
| **Windows** | python.org + nodejs.org + git | CMD + PowerShell | Current default, setup.cmd |
| **macOS** | `brew install python node git` | bash + tmux | Boot scripts need .sh equivalents |
| **Linux** | `apt install python3 nodejs git` | bash + tmux | Boot scripts need .sh equivalents |

## Bootstrap Script

`setup.cmd` in repo root. Validates runtimes, installs packages, clones if needed, runs doctor.

```
setup.cmd                              -- run from CEX directory
setup.cmd https://github.com/x/cex    -- clone + setup
```
