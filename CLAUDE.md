# CEX Boot Chain

> **You are inside CEX** -- a typed knowledge system for LLM agents.
> 99 kinds, 99 builders, 12 pillars, 7 nuclei, 8F pipeline.

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

## STEP 3: KEY PATHS

| What | Where |
|------|-------|
| Builders (99) | `archetypes/builders/{kind}-builder/` (13 ISOs) |
| Schemas (12) | `P{01-12}_*/_schema.yaml` |
| Kind KCs (99) | `P01_knowledge/library/kind/kc_{kind}.md` |
| Templates | `archetypes/TYPE_TO_TEMPLATE.yaml` |
| Kind Registry | `.cex/kinds_meta.json` (source of truth) |
| Nuclei (7) | `N{01-07}_*/` (12 subdirs each) |
| Instances | `_instances/{name}/N{01-07}_*/` |
| Tools (10) | `_tools/cex_*.py` |
| Boot Scripts | `boot/cex.cmd` (N07) `boot/n03.cmd` (builder) |
| Spawn Scripts | `_spawn/spawn_*.ps1` |
| Handoffs | `.cex/handoffs/` |
| Signals | `.cex_signals/` |

## STEP 4: TOOLS

| Tool | Command | Purpose |
|------|---------|---------|
| Motor | `python _tools/cex_8f_motor.py --intent "..."` | Intent to kind |
| Runner | `python _tools/cex_8f_runner.py --kind X` | Build artifact |
| Doctor | `python _tools/cex_doctor.py` | Health check |
| Compile | `python _tools/cex_compile.py PATH` | .md to .yaml |
| Index | `python _tools/cex_index.py` | Rebuild index |
| Register | `python _tools/cex_kind_register.py --kind X` | Add new kind |
| Nucleus | `python _tools/cex_nucleus_builder.py --nucleus N0x` | Build nucleus |
| Forge | `python _tools/cex_forge.py` | Batch build |
| Feedback | `python _tools/cex_feedback.py` | Quality feedback |

## STEP 5: ORCHESTRATION (N07 only)

### Dispatch Commands

```powershell
# Solo (1 builder)
powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n03 -task "TASK" -interactive

# Grid (up to 6 builders parallel)
powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_grid.ps1 -mission NAME -interactive

# Grid continuous (auto-refill from queue)
powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_grid.ps1 -mission NAME -mode continuous -interactive

# Monitor
powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_monitor.ps1

# Stop all
powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_stop.ps1
```

### Handoff Format

Write to `.cex/handoffs/{mission}_{nucleus}.md`:

```markdown
# {NUCLEUS} Task: {Title}
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## TAREFAS
1. ...
2. ...

## COMMIT
git add -A && git commit -m "[{NUCLEUS}] {message}"

## SIGNAL
python -c "from _tools.signal_writer import write_signal; write_signal('{nucleus}', 'complete', 9.0)"
```

### Routing

| Domain | Nucleus | CLI | Model | Why |
|--------|---------|-----|-------|-----|
| Build artifacts, scaffold | N03 | claude | opus | Complex construction, 8F pipeline |
| Research, analysis, papers | N01 | gemini | 2.5-pro | 1M context for large docs |
| Marketing, copy, ads | N02 | claude | sonnet | Creative writing |
| Knowledge, docs, RAG | N04 | gemini | 2.5-pro | 1M context for indexing |
| Deploy, test, debug, code | N05 | codex | GPT-5.4 | Code review, testing |
| Sales, pricing, courses | N06 | claude | sonnet | Persuasive copy |

## STEP 6: QUALITY

| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Reference example |
| PUBLISH | >= 8.0 | Standard publication |
| REVIEW | >= 7.0 | Needs revision |
| REJECT | < 7.0 | Redo |

## CONSTRAINTS

**NEVER**: Skip frontmatter | Publish below 8.0 | Reference proprietary systems | Overwrite without git
**ALWAYS**: Load builder ISOs first | Check existing examples | Compile after save | Signal on complete
