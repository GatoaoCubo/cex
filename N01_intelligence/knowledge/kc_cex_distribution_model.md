---
id: kc_cex_distribution_model
kind: knowledge_card
pillar: P01
title: "CEX Distribution Model -- From PI Wrapper to Claude Code Native"
version: 1.0.0
quality: 9.1
created: 2026-04-08
tags: [distribution, runtime, claude-code, pi, migration, architecture]
tldr: "CEX distributes as git repo + Claude Code CLI. PI wrapper abandoned 2026-04-08 due to Anthropic auth policy. 3 runtimes + 1 CLI + pip deps = full system."
---

# CEX Distribution Model

## Why PI Was Abandoned

| Factor | Detail |
|--------|--------|
| **Root cause** | Anthropic blocks third-party app subscriptions (OAuth policy change) |
| **Impact** | PI (`@mariozechner/pi-coding-agent`) cannot authenticate against Anthropic API |
| **Date** | 2026-04-08 |
| **Decision** | Permanent pivot to Claude Code native |
| **Reversibility** | None -- policy is Anthropic's, not CEX's |

### PI's value proposition was:

1. Custom themes per nucleus (visual identity in terminal)
2. Extension system (.pi/extensions/) for subagents, handoffs, providers
3. `--continue` flag for session persistence
4. `pi compact()` for context window management
5. Custom agent definitions in `.pi/agents/`

### What killed it:

PI wraps Anthropic's API. Anthropic's OAuth now requires first-party apps only.
PI users would need an API key (paid per token) instead of Max/Pro subscription.
This breaks CEX's zero-cost-at-idle principle -- nuclei should cost $0 when not running.

## How CEX Distributes Now

```
Distribution = git clone + Claude Code CLI

User's machine:
  Layer 0: Windows/macOS/Linux
  Layer 1: Python 3.12+ / Node.js 18+ / Git 2.40+ (3 runtimes, user installs)
  Layer 2: Claude Code CLI + pyyaml + tiktoken + uv (setup.cmd installs)
  Layer 3: MCP servers (auto-install on first use via npx/uvx)
```

### Bootstrap sequence:

```cmd
:: Fresh PC to running (4 commands):
npm install -g @anthropic-ai/claude-code
pip install pyyaml tiktoken uv
git clone https://github.com/<user>/cex.git && cd cex
boot\cex.cmd
```

Or: run `setup.cmd` (validates runtimes, installs deps, runs doctor).

Reference: `setup.cmd` (repo root), `_docs/specs/spec_zero_install.md`

## Dependency Stack

| Layer | What | Who Installs | Count |
|-------|------|-------------|-------|
| 0 | OS (Windows 10+, macOS, Linux) | User (pre-existing) | 1 |
| 1 | Python 3.12+, Node.js 18+, Git 2.40+ | User (manual) | 3 executables |
| 2 | @anthropic-ai/claude-code (npm) | setup.cmd | 1 CLI |
| 2 | pyyaml, tiktoken, uv (pip) | setup.cmd | 3 packages |
| 3 | MCP servers (firecrawl, fetch, brave, etc.) | Auto (npx/uvx) | 7 servers |

**Total user effort**: Install 3 runtimes, run 1 script, authenticate once in browser.

## What Claude Code Provides as Runtime

| Capability | How CEX Uses It | PI Equivalent (dead) |
|------------|-----------------|---------------------|
| LLM conversation loop | Each nucleus = 1 Claude Code instance | PI session |
| `--model` flag | Routes nucleus to configured model | `pi --model` |
| `--append-system-prompt` | Injects agent card + context | PI system prompt |
| Tools (read, bash, edit, write) | Nuclei read/write artifacts, run Python | PI tools |
| CLAUDE.md auto-load | Project rules loaded automatically | PI project config |
| `.claude/agents/` | 125 builder sub-agents | `.pi/agents/` |
| `.claude/commands/` | /build, /mission, /status, etc. | PI skills (cex-pi-package) |
| `.claude/rules/` | Behavioral rules per session | PI extensions |
| MCP server support | Per-nucleus MCP configs | PI extension providers |
| Sub-agents (Agent tool) | Parallel task execution within nucleus | PI subagent extension |
| Context compression | Automatic compaction when window fills | `pi compact()` |
| `--dangerously-skip-permissions` | Autonomous mode for dispatched nuclei | PI auto-approve |
| OAuth login (browser) | Free with Max/Pro subscription | Blocked for 3rd-party |

## Comparison: PI Wrapper vs Claude Code Native

| Dimension | PI Wrapper (dead) | Claude Code Native (current) |
|-----------|-------------------|------------------------------|
| **Auth** | Blocked by Anthropic policy | Native OAuth, free with subscription |
| **Cost model** | API key (pay-per-token) | Max subscription (unlimited Opus) |
| **Sub-agents** | Custom extension (.pi/extensions/) | Native Agent tool (built-in) |
| **Commands** | cex-pi-package skills | .claude/commands/ (native) |
| **Context mgmt** | pi compact() (SDK method) | Auto-compression (built-in) |
| **Session resume** | pi --continue | claude --continue |
| **Themes** | 7 nucleus themes (visual) | No themes (functional only) |
| **Agent defs** | .pi/agents/*.md | .claude/agents/*.md |
| **Rules** | Manual prompt injection | .claude/rules/ (auto-loaded) |
| **MCP servers** | Extension-based providers | Native MCP support |
| **Install** | npm install -g @mariozechner/pi-coding-agent | npm install -g @anthropic-ai/claude-code |
| **Maintenance** | Community (1 dev) | Anthropic (enterprise team) |
| **1M context** | Depends on PI updates | Native support |
| **IDE integration** | Terminal only | VS Code, JetBrains, Web, Desktop |

### What CEX lost in the pivot:

| Lost Feature | Impact | Mitigation |
|-------------|--------|------------|
| Terminal themes | Cosmetic -- no functional loss | Title bars via CMD `title` command |
| Extension API | Can't write TypeScript extensions | Claude Code has native extensibility via MCP |
| Fine-grained providers | PI supported multiple LLM backends via extensions | nucleus_models.yaml + fallback chains |

### What CEX gained:

| Gained Feature | Impact |
|---------------|--------|
| Anthropic-maintained runtime | No dependency on community project |
| Native 1M context | Guaranteed, not version-dependent |
| Built-in sub-agents | No extension install needed |
| Auto-loaded rules | .claude/rules/ injected every session |
| IDE support | VS Code, JetBrains, web app, desktop app |
| OAuth login | Free with Max/Pro, no API key management |
| Faster updates | Anthropic ships weekly |

## Architecture After Pivot

```
CEX Repo (git clone)
  |
  +-- CLAUDE.md              (master config, auto-loaded)
  +-- .claude/
  |     +-- rules/            (16 behavioral rules, auto-loaded)
  |     +-- commands/         (13+ custom /commands)
  |     +-- agents/           (125 builder sub-agents)
  |     +-- nucleus-settings/ (per-nucleus JSON configs)
  |
  +-- boot/
  |     +-- cex.cmd           (N07 orchestrator boot)
  |     +-- n01.cmd - n06.cmd (nucleus boot scripts)
  |
  +-- .mcp-n0X.json           (MCP server configs, 1 per nucleus)
  +-- .cex/config/
  |     +-- nucleus_models.yaml (model routing: cli + model + flags)
  |
  +-- _tools/                 (59 Python tools)
  +-- setup.cmd               (fresh machine bootstrap)
```

Each boot script calls:
```cmd
claude --model claude-opus-4-6 --append-system-prompt "N0X_*/agent_card_n0X.md" ...
```

No PI. No extensions. No themes. Just Claude Code + repo structure.
