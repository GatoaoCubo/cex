# CEX — Typed Knowledge System for LLM Agents

> 99 kinds · 99 builders · 12 pillars · 7 nuclei · 8F pipeline · 101 sub-agents

## Who Am I?

Check `CEX_NUCLEUS`. N07 = Orchestrator. N03 = Builder. Not set = read and decide.

## Pointers

| What | Where |
|------|-------|
| **8F pipeline** | `.claude/rules/n03-8f-enforcement.md` |
| **Orchestrator rules** | `.claude/rules/n07-orchestrator.md` |
| **Nucleus rules** | `.claude/rules/n{01-06}-*.md` (1 per nucleus) |
| **Commands** | `.claude/commands/` → /build, /validate, /dispatch, /status, /doctor, /mission |
| **Builders (source of truth)** | `archetypes/builders/{kind}-builder/` (13 ISOs each) |
| **Sub-agents** | `.claude/agents/{kind}-builder.md` (101 files) |
| **Pillar schemas** | `P{01-12}_*/_schema.yaml` |
| **Kind KCs** | `P01_knowledge/library/kind/kc_{kind}.md` (99 files) |
| **Kind registry** | `.cex/kinds_meta.json` (99 kinds) |
| **Nucleus fractals** | `N{01-07}_*/` (13 subdirs each, mirrors 12 pillars) |
| **Boot scripts** | `boot/cex.cmd` (N07) · `boot/n0{1-6}.cmd` |
| **Runtime** | `.cex/runtime/{handoffs,signals,pids}/` |
| **Learning records** | `.cex/learning_records/` |
| **Session state** | `_instances/codexa/N07_admin/checkpoints/` |

## 3 Rules

1. **8F is mandatory.** Every artifact passes F1→F8. No exceptions.
2. **N07 never builds.** Dispatch via `bash _spawn/dispatch.sh`. Always.
3. **quality: null.** Never self-score. Peer-review assigns quality.

## Commands

| Command | Purpose |
|---------|---------|
| `/build <intent>` | Create artifact via 8F pipeline |
| `/validate [file\|all]` | Check artifact quality |
| `/dispatch <nucleus> <task>` | Send task to nucleus builder |
| `/mission <goal>` | Decompose goal → build artifacts |
| `/status` | System health dashboard |
| `/doctor` | Full diagnostics |
| `/consolidate` | Post-dispatch cleanup |

## Tools (run with `--help`)

| Tool | Purpose |
|------|---------|
| `cex_8f_runner.py` | Full 8F pipeline (--execute, --nucleus, --kind) |
| `cex_auto.py` | Self-healing flywheel (scan, plan, cycle) |
| `cex_mission.py` | Goal → decomposed artifacts |
| `cex_batch.py` | Multi-intent processing from file |
| `cex_compile.py` | .md → .yaml compilation (--all) |
| `cex_doctor.py` | Builder health check (98 PASS) |
| `cex_hooks.py` | Pre/post validation + git hook |
| `cex_score.py` | Peer review scoring (--apply) |
| `cex_feedback.py` | Quality tracking + archive |
| `cex_materialize.py` | Builder ISOs → sub-agents |
| `cex_system_test.py` | Full system validation (52 tests) |
| `signal_writer.py` | Inter-nucleus signals |

## Quick Dispatch

```bash
bash _spawn/dispatch.sh solo n03 "task"   # 1 builder
bash _spawn/dispatch.sh grid MISSION      # up to 6 parallel
bash _spawn/dispatch.sh status            # monitor
bash _spawn/dispatch.sh stop              # kill all
```

## Nucleus Routing

| Domain | Nucleus | CLI | Model |
|--------|---------|-----|-------|
| Build/create | N03 | claude | opus |
| Research/analysis | N01 | gemini | 2.5-pro |
| Marketing/copy | N02 | claude | sonnet |
| Knowledge/docs | N04 | gemini | 2.5-pro |
| Code/test/deploy | N05 | codex | GPT |
| Sales/pricing | N06 | claude | sonnet |
| Orchestration | N07 | pi | opus |

## Constraints

**NEVER**: skip frontmatter · publish below 8.0 · pass task as CLI arg · overwrite without git
**ALWAYS**: load builder ISOs first · compile after save · signal on complete · boot interactive
