---
id: p09_rr_agent_group_spawn
kind: runtime_rule
pillar: P09
title: "Runtime Rule: Agent_group Spawn Constraints"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: knowledge_agent
quality: 9.1
tags: [runtime, agent_group, spawn, constraints, bsod]
tldr: "Spawn rules: max 3 agent_groups + orchestrator (BSOD at 4), 5s between terminals, -p flag mandatory for TSP, inline prompt < 200 chars"
max_bytes: 512
density_score: 0.91
source: organization-core/.claude/rules/boot-autonomy-flags.md + MEMORY.md constraints
linked_artifacts:
  spawn_config: p12_spawn_grid_continuous
domain: "config"
related:
  - bld_memory_spawn_config
  - spawn-config-builder
  - bld_knowledge_card_spawn_config
  - bld_output_template_spawn_config
  - bld_tools_spawn_config
  - bld_examples_spawn_config
  - p02_boot_edison_claude
  - research_then_build
  - p12_spawn_grid_continuous
  - p03_sp_spawn-config-builder
---

# Runtime Rule: Agent_group Spawn Constraints

## Hard Limits

```yaml
spawn_limits:
  max_concurrent_agent_groups: 3   # + orchestrator = 4 total. BSOD confirmed at 5
  delay_between_terminals: 5s    # RAM stability — never skip
  max_inline_prompt_chars: 200   # TSP -p flag limit — longer prompts hang
  agent_group_boot_timeout: 30s    # Kill and retry if no output after 30s
```

## Required Flags

```bash
# TSP agent_group spawn (mandatory flags):
claude --dangerously-skip-permissions --no-chrome -p

# -p (non-interactive): skips workspace trust dialog — MANDATORY for automation
# --dangerously-skip-permissions: skips tool permission prompts
# --no-chrome: all agent_groups (chrome only via boot/chrome.cmd)
```

## Spawn Script Rules

```powershell
# CORRECT:
spawn_solo.ps1 -sat pytha -task "Read handoff and execute" -interactive

# WRONG (all cause failures):
tsp_manager.py spawn        # invisible window, cannot kill claude.exe
spawn with --mcp-config     # absolute paths hang in PS->cmd chain
```

## Environment Variables

```batch
# REQUIRED in boot scripts (v2.1.50+ fix):
set CLAUDECODE=
set organization_AGENT_GROUP={SAT_NAME}&&claude --dangerously-skip-permissions ...

# Note: set VAR=val&& (no space before &&)
```

## BSOD Prevention

```yaml
bsod_history: 2026-02-18
cause: USB power suspend + Intel I219-V driver race condition
prevention:
  - hybrid_sleep: disabled
  - usb_selective_suspend: disabled
  - hibernate: disabled
  - wake_on_lan: disabled
threshold: NEVER spawn 4+ agent_groups simultaneously
```

## Handoff Offload Rule

When task > 200 chars, write to handoff file:
```bash
# Inline prompt (PASS):
"Read .claude/handoffs/CEX7_batch_2_pytha.md e execute"  # 53 chars

# Inline prompt (FAIL — hangs with -p):
"Execute these 10 tasks: [1] research market... [2] build agent..." # 400+ chars
```

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Properties

| Property | Value |
|----------|-------|
| Kind | `runtime_rule` |
| Pillar | P09 |
| Domain |  |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_memory_spawn_config]] | downstream | 0.36 |
| [[spawn-config-builder]] | downstream | 0.34 |
| [[bld_knowledge_card_spawn_config]] | downstream | 0.33 |
| [[bld_output_template_spawn_config]] | upstream | 0.33 |
| [[bld_tools_spawn_config]] | upstream | 0.32 |
| [[bld_examples_spawn_config]] | upstream | 0.28 |
| [[p02_boot_edison_claude]] | upstream | 0.28 |
| [[research_then_build]] | upstream | 0.27 |
| [[p12_spawn_grid_continuous]] | downstream | 0.27 |
| [[p03_sp_spawn-config-builder]] | upstream | 0.27 |
