---
id: spec_zero_install
kind: context_doc
title: "CEX Zero-Install: Dependencies and Bootstrap on Fresh Machine"
version: 1.0.0
quality: null
created: 2026-04-07
purpose: Everything needed to run CEX on a PC with nothing installed
---

# CEX Zero-Install Spec

## Dependency Stack (4 layers)

```
Layer 0: OS (Windows 10+, macOS, Linux)
  │
  ├── Layer 1: Runtimes
  │     ├── Python 3.12+
  │     ├── Node.js 22+ (LTS)
  │     └── Git
  │
  ├── Layer 2: Package Managers (come with runtimes)
  │     ├── pip (comes with Python)
  │     ├── npm (comes with Node.js)
  │     └── npx (comes with npm)
  │
  ├── Layer 3: Core Packages
  │     ├── pip: pyyaml, tiktoken
  │     ├── npm: @mariozechner/pi-coding-agent (pi CLI)
  │     └── npm: @gatoaocubo/cex (CEX themes + skills + extensions)
  │
  └── Layer 4: Optional (per feature)
        ├── pip: anthropic, openai, google-genai (LLM providers)
        ├── uvx: mcp-server-fetch (MCP servers)
        ├── npx: firecrawl-mcp, markitdown-mcp, etc. (MCP auto-install)
        ├── Ollama (local models, zero cost)
        └── API keys (ANTHROPIC_API_KEY, etc.)
```

## Minimum Install (5 commands)

For a fresh Windows PC:

```cmd
:: 1. Install Python (https://python.org/downloads)
:: 2. Install Node.js (https://nodejs.org — LTS version)
:: 3. Install Git (https://git-scm.com/downloads)

:: 4. Install CEX dependencies
pip install pyyaml tiktoken
npm install -g @mariozechner/pi-coding-agent

:: 5. Clone and run
git clone https://github.com/<user>/cex.git
cd cex
boot\cex.cmd
```

That's it. 3 runtimes + 2 packages + clone. CEX boots.

## Dependency Matrix

### Layer 1: Runtimes (REQUIRED)

| Runtime | Version | Purpose | Install |
|---------|---------|---------|---------|
| **Python** | 3.12+ | All _tools/*.py (59 tools) | python.org or `winget install Python.3` |
| **Node.js** | 22+ LTS | pi CLI + MCP servers (npx) | nodejs.org or `winget install OpenJS.NodeJS.LTS` |
| **Git** | 2.40+ | Version control, branch management | git-scm.com or `winget install Git.Git` |

### Layer 3: Core Packages (REQUIRED)

| Package | Manager | Purpose | Size |
|---------|---------|---------|------|
| **pyyaml** | pip | YAML parsing (schemas, configs, kinds_meta) | 150KB |
| **tiktoken** | pip | Token counting (budget allocation) | 2MB |
| **pi** | npm (global) | Agent CLI — runs all nuclei | 15MB |

### Pi Deep Dive (the nucleus runtime)

Pi is the CLI that runs EVERY nucleus. CEX without pi is a library without an interpreter.

| What pi provides | How CEX uses it |
|-----------------|-----------------|
| LLM conversation loop | Each nucleus = 1 pi instance talking to Opus/Sonnet/Haiku |
| `--model` flag | Routes each nucleus to its configured model |
| `--append-system-prompt` | Injects agent card + sin lens + self-select protocol |
| Tools (read, bash, edit, write) | How nuclei read/write artifacts, run Python tools |
| Session persistence | `--continue` resumes after context exhaustion |
| `/login` OAuth | Free auth for Claude Max, Gemini CLI, Copilot |
| MCP server support | Each nucleus loads its `.mcp-n0X.json` config |
| Extensions | Subagent extension enables parallel sub-tasks per nucleus |
| Themes | 7 sin-colored themes (one per nucleus) |
| Skills | /build, /mission, /status commands |
| Prompt templates | /implement, /scout-and-plan workflows |
| Compaction | Automatic context compression when window fills |

**Install**:
```cmd
npm install -g @mariozechner/pi-coding-agent
```

**Auth** (first run — pick ONE):
```
pi                          :: starts pi
/login                      :: in session, select provider:
  - Claude Max/Pro          :: unlimited Opus (recommended)
  - Gemini CLI              :: free, rate limited
  - GitHub Copilot          :: free with GitHub account
  - OpenAI Codex            :: ChatGPT Plus/Pro subscription
  - Google Antigravity      :: free sandbox
```

**No API key needed** for subscription plans. Pi handles OAuth tokens automatically.
API keys (ANTHROPIC_API_KEY etc.) are only for SDK/programmatic mode.

### Pi Config Files in CEX Repo

| Path | Purpose | Count |
|------|---------|-------|
| `.pi/agents/*.md` | Sub-agent definitions (scout, builder, etc.) | 6 |
| `.pi/extensions/subagent/` | Subagent extension (parallel tasks) | 2 files |
| `.claude/rules/*.md` | Behavioral rules auto-loaded by pi | 16 |
| `.claude/commands/*.md` | Custom /commands | 13 |
| `.claude/agents/*.md` | Builder sub-agents (1 per kind) | 125 |
| `.claude/nucleus-settings/n0X.json` | Per-nucleus pi settings | 6 |
| `.mcp-n0X.json` | MCP server configs per nucleus | 6 |
| `boot/n0X.cmd` | Boot scripts that launch pi with flags | 7+ |

### CEX Pi Package (themes + skills + extensions)

| Component | Count | Purpose |
|-----------|-------|---------|
| Themes | 7 | Visual identity per nucleus (sin colors) |
| Skills | 3 | /build, /mission, /status |
| Extensions | 2 | cex-nucleus-ui.ts, cex-subagent/ |
| Prompts | 3 | /implement, /build-and-review, /research-then-build |

**Install**:
```cmd
cd cex-pi-package && npm link
```

This registers the package locally so pi auto-discovers themes, skills, and extensions.

### Layer 4: Optional Packages

| Package | Manager | Purpose | When needed |
|---------|---------|---------|-------------|
| anthropic | pip | Anthropic API (Claude) | If using API key auth |
| openai | pip | OpenAI API (GPT) | If using OpenAI |
| google-genai | pip | Google API (Gemini) | If using Gemini API key |
| ollama | system | Local LLM inference | Free tier, no API key |

**Note**: pi handles auth via OAuth for subscription plans (Claude Max, Gemini CLI, Copilot).
API key packages are only needed for programmatic SDK access, NOT for nucleus operation.

### Layer 4: MCP Servers (AUTO-INSTALL)

MCP servers install automatically via `npx -y` on first use. No pre-install needed.

| Server | Auto-installs via | Used by |
|--------|------------------|---------|
| firecrawl-mcp | `npx -y firecrawl-mcp` | N01, N04 |
| mcp-server-fetch | `uvx mcp-server-fetch` | N01, N04, N06 |
| markitdown-mcp | `npx -y markitdown-mcp` | N01, N02, N06 |
| brave-search | `npx -y @anthropic/mcp-server-brave-search` | N01 |
| notebooklm | `npx -y notebooklm-mcp@latest` | N01, N02, N04, N06 |
| puppeteer | `npx -y @anthropic-ai/mcp-server-puppeteer` | N02 |
| github | `npx -y @anthropic/mcp-server-github` | N03, N05 |
| supabase | `npx -y @supabase/mcp-server-supabase` | N04 |
| postgres | `npx -y @anthropic-ai/mcp-server-postgres` | N04, N05 |
| stripe | `npx -y @anthropic/mcp-stripe` | N06 |
| canva | `npx -y @mcp_factory/canva-mcp-server` | N02, N03, N06 |

**Requirement**: `uvx` (from `uv`) for Python-based MCP servers:
```cmd
pip install uv
```

## Environment Variables

### Required for operation

| Variable | Purpose | How to get |
|----------|---------|-----------|
| None | pi uses OAuth login (`/login` in session) | Free with subscription |

### Optional (per provider/service)

| Variable | Purpose | When needed |
|----------|---------|-------------|
| ANTHROPIC_API_KEY | Anthropic API access | SDK-mode only |
| OPENAI_API_KEY | OpenAI API access | SDK-mode only |
| GOOGLE_API_KEY | Gemini API access | SDK-mode only |
| SUPABASE_URL | Supabase database | CRM features |
| SUPABASE_KEY | Supabase auth | CRM features |
| FIRECRAWL_API_KEY | Firecrawl web scraping | Research features |
| BRAVE_API_KEY | Brave Search API | Research features |

## Bootstrap Script: boot/cex_setup.cmd

One-click setup for fresh machine (checks + installs everything):

```cmd
@echo off
title CEX Setup
echo Checking dependencies...

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [MISSING] Python 3.12+ — install from python.org
    set MISSING=1
) else (
    echo [OK] Python
)

:: Check Node
node --version >nul 2>&1
if errorlevel 1 (
    echo [MISSING] Node.js 22+ — install from nodejs.org
    set MISSING=1
) else (
    echo [OK] Node.js
)

:: Check Git
git --version >nul 2>&1
if errorlevel 1 (
    echo [MISSING] Git — install from git-scm.com
    set MISSING=1
) else (
    echo [OK] Git
)

if defined MISSING (
    echo.
    echo Install missing runtimes first, then re-run this script.
    pause
    exit /b 1
)

:: Install Python deps
echo Installing Python dependencies...
pip install pyyaml tiktoken uv

:: Install pi
echo Installing pi coding agent...
npm install -g @mariozechner/pi-coding-agent

:: Install CEX package
echo Installing CEX themes + skills...
cd cex-pi-package && npm link && cd ..

:: Verify
echo.
echo === Verification ===
python _tools/cex_doctor.py 2>&1 | findstr "Result:"
echo.
echo Setup complete. Run: boot\cex.cmd
pause
```

## Tiers: What Works at Each Level

| Tier | Install | What works | What doesn't |
|------|---------|-----------|-------------|
| **Minimal** (Python + Node + Git) | 3 runtimes | All tools, doctor, flywheel, compile, score, evolve heuristic | No LLM, no nuclei |
| **Core** (+ pip deps + pi) | + 3 packages | Everything above + nucleus boot + grid dispatch | No MCP servers |
| **Full** (+ OAuth login) | + `/login` in pi | Everything: 6 nuclei, MCP servers, autoresearch, overnight | Needs subscription |
| **Free** (+ Ollama) | + Ollama | Everything above with local models | Slower, rate limited |

## Cross-Platform

| OS | Runtimes | Spawn method | Notes |
|----|----------|-------------|-------|
| **Windows** | python.org + nodejs.org + git | PowerShell + CMD | Current default |
| **macOS** | `brew install python node git` | bash + tmux | Replace .ps1 with .sh |
| **Linux** | `apt install python3 nodejs git` | bash + tmux | Replace .ps1 with .sh |

### What needs porting for macOS/Linux

| Component | Windows | macOS/Linux equivalent |
|-----------|---------|----------------------|
| `_spawn/spawn_solo.ps1` | PowerShell + Start-Process | bash + tmux new-window |
| `_spawn/spawn_grid.ps1` | PowerShell + MoveWindow | tmux split-pane layout |
| `_spawn/spawn_stop.ps1` | taskkill /F /PID /T | kill -9 (process group) |
| `boot/*.cmd` | CMD batch | bash .sh scripts |
| Window positioning | Win32 MoveWindow API | tmux pane layout |

Effort: N05 creates `_spawn/*.sh` equivalents. ~1 dispatch.
