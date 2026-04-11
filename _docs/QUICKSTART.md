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
  archetypes/builders/          # 123 builders (13 ISOs each = 1,599 files)
  P01_knowledge/ .. P12_orchestration/  # 12 pillars (kind schemas + templates)
  N00_genesis/                  # Archetype mold
  N01_intelligence/ .. N07_admin/       # 7 runtime nuclei (domain instances)
  _tools/                       # 91 Python tools (8F engine, quality, retrieval)
  boot/                         # Boot scripts (1 per nucleus)
  .claude/                      # Claude Code config (rules, agents, commands)
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

*CEX Quick Start v3.0 -- Claude Code native. 2026-04-08.*
