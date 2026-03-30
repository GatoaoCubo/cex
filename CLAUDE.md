# CEX Boot Chain

> **You are inside CEX** -- a typed knowledge system for LLM agents.
> 99 kinds, 99 builders, 12 pillars, 7 nuclei, 8F pipeline, 101 sub-agents.

---

## STEP 1: WHO AM I?

Check env `CEX_NUCLEUS`. If N07 -> you are the Orchestrator. If N03 -> you are the Builder.
If not set -> read this file and decide based on user intent.

## STEP 2: THE 8F PIPELINE

Every artifact is produced by running 8 functions in sequence:

| # | Function | Verb | What it does |
|---|----------|------|-------------|
| F1 | CONSTRAIN | Restrict | Load schema + config for the kind |
| F2 | BECOME | Be | Load agent identity + system prompt |
| F3 | INJECT | Know | Load knowledge cards + memory |
| F4 | REASON | Think | LLM plans the approach |
| F5 | CALL | Do | Parse available tools |
| F6 | PRODUCE | Generate | LLM generates the artifact |
| F7 | GOVERN | Evaluate | 7 gates validate output |
| F8 | COLLABORATE | Coordinate | Save + compile + index + signal |

## STEP 2.1: 8F IS MANDATORY (NOT OPTIONAL)

**Every artifact build MUST execute all 8 functions. No exceptions.**

**Enforcement**: `.claude/rules/n03-8f-enforcement.md` (auto-loaded)

**Evidence required**: Every build shows the 8F trace:
```
F1 CONSTRAIN: kind=X, pillar=PXX
F2 BECOME: builder loaded (13 ISOs)
F3 INJECT: KC + examples loaded
F4 REASON: plan decided
F5 CALL: tools ready
F6 PRODUCE: draft generated
F7 GOVERN: score X/10, gates pass
F8 COLLABORATE: saved, compiled, committed
```

## STEP 3: KEY PATHS

| What | Where |
|------|-------|
| Builders (99) | `archetypes/builders/{kind}-builder/` (13 ISOs) |
| Sub-agents (101) | `.claude/agents/{kind}-builder.md` (materialized from ISOs) |
| Schemas (12) | `P{01-12}_*/_schema.yaml` |
| Kind KCs (99) | `P01_knowledge/library/kind/kc_{kind}.md` |
| Kind Registry | `.cex/kinds_meta.json` (source of truth) |
| Nuclei (7) | `N{01-07}_*/` (12 subdirs each) |
| Instances | `_instances/{name}/N{01-07}_*/` |
| Tools | `_tools/cex_*.py` |
| Boot Scripts | `boot/cex.cmd` (N07) `boot/n0{1-6}.cmd` (nuclei) |
| Spawn Scripts | `_spawn/dispatch.sh` + `spawn_*.ps1` |
| Handoffs | `.cex/runtime/handoffs/` (gitignored, ephemeral) |
| Signals | `.cex/runtime/signals/` (gitignored, ephemeral) |
| Playbook | `_docs/PLAYBOOK.md` |

## STEP 4: TOOLS

| Tool | Command | Purpose |
|------|---------|---------|
| Motor | `python _tools/cex_8f_motor.py --intent "..."` | Intent to kind |
| Runner | `python _tools/cex_8f_runner.py --kind X` | Build artifact (dry-run) |
| Doctor | `python _tools/cex_doctor.py` | Health check (98 PASS 0 WARN) |
| Compile | `python _tools/cex_compile.py PATH` | .md to .yaml |
| Materialize | `python _tools/cex_materialize.py --all` | Builders → .claude/agents/ |
| Index | `python _tools/cex_index.py` | Rebuild index |
| Register | `python _tools/cex_kind_register.py --kind X` | Add new kind |
| Forge | `python _tools/cex_forge.py` | Batch build |
| Feedback | `python _tools/cex_feedback.py` | Quality feedback |
| Signal | `python _tools/signal_writer.py` | Write completion signals |

## STEP 5: ORCHESTRATION (N07 only)

### Dispatch Commands (COPY THESE EXACTLY)

```bash
# Solo — 1 builder in new window
bash _spawn/dispatch.sh solo n03 "task description"

# Grid — up to 6 parallel builders
bash _spawn/dispatch.sh grid MISSION_NAME

# Monitor
bash _spawn/dispatch.sh status

# Stop all
bash _spawn/dispatch.sh stop
```

> **NEVER** use `start cmd`, `cmd /c`, or raw `powershell -File` from pi.
> **ALWAYS** use `bash _spawn/dispatch.sh` — it wraps PowerShell correctly.

### Boot Architecture (all subscription, zero API cost)

All boots are ALWAYS interactive — task comes from handoff file, never CLI args.
This avoids nested-quote hell that kills CMD.

| Nucleus | Boot | CLI | Model | Auth | MCPs |
|---------|------|-----|-------|------|------|
| **N07** | `boot/cex.cmd` | pi | opus xhigh | Anthropic Max | — |
| N03 | `boot/n03.cmd` | claude | opus | Anthropic Max | github |
| N02 | `boot/n02.cmd` | claude | sonnet | Anthropic Max | markitdown, fetch |
| N06 | `boot/n06.cmd` | claude | sonnet | Anthropic Max | fetch |
| N01 | `boot/n01.cmd` | gemini | 2.5-pro | Google One | — |
| N04 | `boot/n04.cmd` | gemini | 2.5-pro | Google One | — |
| N05 | `boot/n05.cmd` | codex | GPT | OpenAI Plus | — |

### Handoff Protocol

Write to `.cex/runtime/handoffs/{mission}_{nucleus}.md`:

```markdown
# {NUCLEUS} Task: {Title}
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## TAREFAS
1. ...

## COMMIT
git add -A && git commit -m "[{NUCLEUS}] {message}"

## SIGNAL
python -c "from _tools.signal_writer import write_signal; write_signal('{nucleus}', 'complete', 9.0, '{mission}')"
```

For grid dispatch, name handoffs as `{MISSION}_{nucleus}.md` (last segment = nucleus).

### Consolidate (after nucleus completes)

1. Check signals + git log for nucleus commits
2. Verify: `python _tools/cex_doctor.py`
3. Stop: `bash _spawn/dispatch.sh stop`
4. Commit if needed (Gemini nuclei can't git — N07 commits for them)
5. Emit signal if nucleus couldn't

### Routing

| Domain | Nucleus | CLI | Model | Sub-agents? |
|--------|---------|-----|-------|-------------|
| Build/scaffold | N03 | claude | opus | ✅ Yes (5 parallel via Task) |
| Marketing/copy | N02 | claude | sonnet | ✅ Yes |
| Commercial | N06 | claude | sonnet | ✅ Yes |
| Research/analysis | N01 | gemini | 2.5-pro | ❌ No (1M ctx, loads all ISOs at once) |
| Knowledge/docs | N04 | gemini | 2.5-pro | ❌ No (1M ctx) |
| Code/test/deploy | N05 | codex | GPT | ❌ No (sequential by nature) |

### Known Behaviors

- **Gemini (N01, N04)**: Does work but CANNOT git commit or emit signals. N07 must consolidate.
- **Claude/Codex (N02, N03, N05, N06)**: Fully autonomous — commits and signals on their own.
- **Boot scripts**: Always interactive, no args. Task is in `.cex/runtime/handoffs/{nucleus}_task.md`.

## STEP 6: SUB-AGENTS (Crew Pattern)

### Architecture

```
archetypes/builders/          ← SOURCE OF TRUTH (99 × 13 ISOs, CLI-agnostic)
        │
        ├── cex_compile.py    → compiled/*.yaml (universal)
        └── cex_materialize.py → .claude/agents/*.md (Claude CLI sub-agents)
```

### How It Works

- **Claude CLI nuclei (N02, N03, N06)**: Use `.claude/agents/{kind}-builder.md` via Task tool. Opus orchestrates, Sonnet sub-agents execute. Up to 5 parallel.
- **Gemini CLI nuclei (N01, N04)**: No sub-agents needed. 1M token context loads all 13 ISOs of a builder in one shot.
- **Codex CLI (N05)**: No sub-agents. Sequential prompt injection.

### Crew Dispatch Pattern (proven)

```
N03 (opus, orchestrator)
  ├── Task → kind-builder (sonnet): produces artifact via 8F
  ├── Task → validator (sonnet, read-only): checks quality gates
  └── Opus decides: ACCEPT (≥8.0) | REVISE (7-7.9, max 2) | REBUILD (<7.0)
```

Pattern documented: `N03_engineering/architecture/p08_pat_crew_dispatch.md`

### Available Sub-Agents

| Agent | Count | Source | Purpose |
|-------|-------|--------|---------|
| `{kind}-builder` | 99 | `cex_materialize.py` from builders | Build specific kind artifact |
| `validator` | 1 | Manual | Read-only quality gate check |
| `kind-builder` | 1 | Manual | Generic builder (loads ISOs dynamically) |

Regenerate all: `python _tools/cex_materialize.py --all`

## STEP 7: QUALITY

| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Reference example |
| PUBLISH | >= 8.0 | Standard publication |
| REVIEW | >= 7.0 | Needs revision |
| REJECT | < 7.0 | Redo |

## STEP 8: CURRENT STATE (2026-03-30)

### Bootstrap Progress

| Phase | Status | What |
|-------|--------|------|
| Fase 0 | ✅ DONE | Tools validated (doctor, compile, runner) |
| Fase 1 | ✅ DONE | N07 rebuilt (13 artifacts, 10 compiled) |
| Fase 2 | ✅ DONE | 13 oversized builder ISOs fixed (doctor 98 PASS 0 WARN) |
| Fase 3 | ✅ DONE | N01-N06 rebuilt via grid (51 artifacts, all compiled) |
| Fase 4 | ✅ DONE | Sub-agents: crew test passed + materializer built (101 agents) |
| Fase 5 | 🔲 TODO | Cross-validation: N05 validates N03, N03 validates N01, etc. |
| Fase 6 | 🔲 TODO | Quality scoring: peer-review to replace quality:null |
| Fase 7 | 🔲 TODO | 8F Runner --execute: end-to-end without human pasting |
| Fase 8 | 🔲 TODO | Hooks (pre/post build validation) |
| Fase 9 | 🔲 TODO | Feedback loop: instance → learning_record → builder improvement |
| Fase 10 | 🔲 TODO | Full grid test: 6 nuclei parallel, real mission |

### Artifact Inventory

| Nucleus | Artifacts | Compiled | quality:set | quality:null |
|---------|-----------|----------|-------------|-------------|
| N03 Engineering | 34 | 2 | 34 (9.0-9.3) | 0 |
| N07 Admin | 13 | 10 | 3 | 10 |
| N01 Intelligence | 14 | 11 | 0 | 14 |
| N02 Marketing | 10 | 10 | 0 | 10 |
| N04 Knowledge | 12 | 12 | 0 | 12 |
| N05 Operations | 9 | 9 | 0 | 9 |
| N06 Commercial | 9 | 9 | 0 | 9 |

### Infrastructure

| Component | Status |
|-----------|--------|
| 99 Builders (13 ISOs each) | ✅ 98 PASS 0 WARN |
| 99 Kind KCs | ✅ Complete |
| 12 Pillar Schemas | ✅ Complete |
| 101 Sub-agents (.claude/agents/) | ✅ Materialized |
| 7 Boot scripts | ✅ All interactive, no nested quotes |
| Spawn system | ✅ dispatch.sh → solo/grid/status/stop |
| MCPs | ⚠️ Only N02, N03, N06 |
| .claude/rules | ⚠️ Only N03, N07 |
| .claude/commands | ⚠️ Only /consolidate |
| Hooks | ❌ None |

## CONSTRAINTS

**NEVER**: Skip frontmatter | Publish below 8.0 | Reference proprietary systems | Overwrite without git | Pass task as CLI arg (nested quotes kill CMD)
**ALWAYS**: Load builder ISOs first | Check existing examples | Compile after save | Signal on complete | Boot interactive (task via handoff file)
