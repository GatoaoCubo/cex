# CEX Quick Start

> Fresh PC to first artifact in 5 minutes.

---

## 1. Prerequisites (3 runtimes)

| Runtime | Version | Install |
|---------|---------|---------|
| Python | 3.12+ | `winget install Python.3` or python.org |
| Node.js | 18+ LTS | `winget install OpenJS.NodeJS.LTS` or nodejs.org |
| Git | 2.40+ | `winget install Git.Git` or git-scm.com |

---

## 2. Clone + Setup

```bash
git clone https://github.com/your-org/cex.git && cd cex
setup.cmd
```

`setup.cmd` does everything:
1. Validates Python, Node.js, Git
2. Installs Claude Code CLI (`npm install -g @anthropic-ai/claude-code`)
3. Installs Python deps (`pyyaml`, `tiktoken`, `uv`)
4. Runs `cex_doctor.py` health check
5. Prints next steps

---

## 2.5. Validate Setup

After `setup.cmd` completes, run the setup validator:

```bash
python _tools/cex_setup_validator.py
```

This checks all runtimes, dependencies, MCP configs, and runtime directories.
Fix any FAIL items before booting. If everything passes, you're ready.

---

## 2.6. Environment Variables

| Variable | Required? | Purpose | How to set |
|----------|-----------|---------|-----------|
| (none for OAuth) | -- | Claude Code uses browser login | Automatic on first `claude` run |
| ANTHROPIC_API_KEY | Optional | API access (alternative to OAuth) | `setx ANTHROPIC_API_KEY sk-ant-...` |
| FIRECRAWL_API_KEY | Optional | Web scraping (N01 research) | `setx FIRECRAWL_API_KEY fc-...` |
| BRAVE_API_KEY | Optional | Brave Search (N01 research) | `setx BRAVE_API_KEY BSA...` |

Set via `setx VAR value` in CMD, or System Properties > Environment Variables on Windows.
After `setx`, restart your terminal for the variable to take effect.

---

## 2.7. Power Settings (for long runs)

For grid/mission work (multi-nucleus dispatch that can run 30-60 min):

```
Settings > System > Power > Screen and sleep: set both to "Never"
```

Or from CMD: `powercfg -change -standby-timeout-ac 0`

Re-enable after the mission completes to save power.

---

## 3. Boot

```bash
boot\cex.ps1            # Start N07 orchestrator (main entry point)
# -- OR --
boot\n03.ps1            # Start a specific nucleus (builder)
# -- OR --
claude                  # Raw Claude Code in the repo directory
```

First run opens your browser for Anthropic OAuth login.
Requires: Anthropic Max (unlimited Opus) or Pro or API key.

---

## 4. Configure Your Brand

In the Claude Code chat:

```
/init
```

CEX asks ~6 questions about your brand (name, values, audience, tone).
Takes ~2 minutes. After this, every artifact matches YOUR voice and identity.

---

## 5. Build Something

```
/build knowledge_card about React Server Components
```

Or run a full mission:

```
/mission build a SaaS landing page with pricing tiers
```

Or go guided (co-pilot mode):

```
/guide build a content marketing kit
```

---

## What Just Happened

```
cex/
  archetypes/builders/          # 125 builders (13 ISOs each = 1,625 files)
  P01_knowledge/ .. P12_orchestration/  # 12 pillars (kind schemas + templates)
  N00_genesis/                  # Archetype mold
  N01_intelligence/ .. N07_admin/       # 7 runtime nuclei (domain instances)
  _tools/                       # 59 Python tools (8F engine, quality, retrieval)
  boot/                         # Boot scripts (1 per nucleus + N07 orchestrator)
  .claude/P02_model/               # 125 builder sub-agents
  .claude/rules/                # Behavioral rules (auto-loaded per session)
  .claude/commands/             # Custom /commands (/build, /mission, etc.)
  .cex/                         # Runtime state (kinds_meta, config, signals)
```

---

## Key Concepts

| Concept | What It Means |
|---------|--------------|
| Kind | A type of artifact (e.g., knowledge_card, agent, workflow). 123 defined. |
| Pillar | A category of kinds (e.g., P01 Knowledge, P04 Tools). 12 total. |
| Nucleus | A domain-specialized agent (e.g., N03 Engineering). 8 total (N00-N07). |
| Builder | A factory for a kind. 13 ISO files define HOW to build it. |
| 8F Pipeline | The 8-step reasoning protocol every task passes through. |
| GDP | Guided Decision Protocol -- user decides WHAT, LLM decides HOW. |

---

## Essential Commands

| Command | Purpose |
|---------|---------|
| `/init` | First-time brand configuration |
| `/build <intent>` | Build a single artifact via 8F pipeline |
| `/mission <goal>` | Full lifecycle: plan + guide + spec + grid + consolidate |
| `/guide [topic]` | Co-pilot mode: ask before building |
| `/status` | System health dashboard |
| `/doctor` | Full diagnostics |
| `/validate [file]` | Check artifact quality |

---

## Validate

```bash
python _tools/cex_doctor.py      # Full health check (123 builders, schemas, density)
python _tools/cex_compile.py --all   # Compile all .md to .yaml
```

---

## Next Steps

- Read `_docs/ARCHITECTURE.md` for the 5-layer, 12-pillar, 8-nuclei model
- Read `_docs/HIERARCHY.md` for the fractal structure
- Explore `archetypes/builders/` for builder blueprints (13 ISO files each)
- Read `_docs/PLAYBOOK.md` for dispatch and orchestration operations

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `uvx not found` | `pip install uv` -- uv provides the `uvx` command for MCP servers |
| MCP server 404 / install fails | Check `.mcp-n0X.json` -- old `@anthropic/*` packages moved to `@modelcontextprotocol/*` |
| `cex_retriever.py` warnings | `pip install numpy scikit-learn` -- optional but improves TF-IDF performance |
| Pre-commit hook not running | `python _tools/cex_hooks.py install` -- installs the git pre-commit hook |
| `claude` command not found | `npm install -g @anthropic-ai/claude-code` -- or check Node.js is in PATH |
| Python `UnicodeEncodeError` | Windows terminal uses cp1252 by default; set `PYTHONIOENCODING=utf-8` or use `chcp 65001` |
| Nuclei die mid-grid | Check Windows power settings -- disable sleep for long runs (see section 2.7) |
| `setup.cmd` fails at pip | Ensure Python is in PATH (`python --version` should work from CMD) |

---

*CEX Quick Start v4.0 -- Claude Code native. 2026-04-12.*
