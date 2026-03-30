# CEX — Typed Knowledge System for LLM Agents

> 99 kinds · 99 builders · 12 pillars · 7 nuclei · 8F pipeline · 101 sub-agents

## Who Am I?

Check `CEX_NUCLEUS`. N07 = Orchestrator. N03 = Builder. Not set = read and decide.

## Pointers

| What | Where |
|------|-------|
| **8F pipeline** | `.claude/rules/n03-8f-enforcement.md` |
| **Orchestrator rules** | `.claude/rules/n07-orchestrator.md` |
| **Dispatch & spawn** | `_docs/PLAYBOOK.md` |
| **Builders (source of truth)** | `archetypes/builders/{kind}-builder/` (13 ISOs each) |
| **Sub-agents (materialized)** | `.claude/agents/{kind}-builder.md` (101 files) |
| **Pillar schemas** | `P{01-12}_*/_schema.yaml` |
| **Kind KCs** | `P01_knowledge/library/kind/kc_{kind}.md` |
| **Kind registry** | `.cex/kinds_meta.json` |
| **Nucleus fractals** | `N{01-07}_*/` (12 subdirs each) |
| **Tools** | `_tools/cex_*.py` (run with `--help`) |
| **Boot scripts** | `boot/cex.cmd` (N07) · `boot/n0{1-6}.cmd` |
| **Runtime (ephemeral)** | `.cex/runtime/{handoffs,signals,pids}/` |
| **Mission state** | `N07_admin/orchestration/mission_bootstrap_2026Q1.md` |
| **Session state** | `_instances/codexa/N07_admin/checkpoints/` |

## 3 Rules

1. **8F is mandatory.** Every artifact passes F1→F8. No exceptions.
2. **N07 never builds.** Dispatch via `bash _spawn/dispatch.sh`. Always.
3. **quality: null.** Never self-score. Peer-review assigns quality.

## Quick Dispatch

```bash
bash _spawn/dispatch.sh solo n03 "task"   # 1 builder
bash _spawn/dispatch.sh grid MISSION      # up to 6 parallel
bash _spawn/dispatch.sh status            # monitor
bash _spawn/dispatch.sh stop              # kill all
```

## Constraints

**NEVER**: skip frontmatter · publish below 8.0 · pass task as CLI arg · overwrite without git
**ALWAYS**: load builder ISOs first · compile after save · signal on complete · boot interactive
