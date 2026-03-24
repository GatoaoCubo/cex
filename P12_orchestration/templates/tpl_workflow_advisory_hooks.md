---
# TEMPLATE: Workflow — Advisory Hooks (P12 Orchestration)
# Valide contra P12_orchestration/_schema.yaml (types.workflow)
# Max 2048 bytes | density_min: 0.80 | quality_min: 8.0

id: p12_wf_{{NAME_SLUG}}
type: workflow
lp: P12
title: "Workflow: Advisory Hooks"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{SATELLITE_NAME}}
quality: {{QUALITY_8_TO_10}}
tags: [hooks, advisory, orchestration, workflow]
tldr: "5 advisory hook types that inject context without blocking execution"
density_score: {{0.80_TO_1.00}}
timeout: 10 min
---

# Workflow: Advisory Hooks

## Overview

| Property | Value |
|----------|-------|
| Trigger | Any hook event (PreToolUse, PostToolUse, UserPromptSubmit, Stop, Notification) |
| Input | stdin JSON from Claude Code hook system |
| Output | additionalContext string injected into conversation |
| Timeout | Per-hook (3-10s); universal timeout-guard wraps all |

## Universal Pattern
```
timeout-guard ({{TIMEOUT_S}}s)
  → read stdin JSON
  → compute advisory
  → write additionalContext to stdout
  → exit 0 (ALWAYS — never block)
```

## 5 Advisory Hook Types

### 1. Statusline
- **Event**: PostToolUse
- **Purpose**: Update terminal status bar with satellite state, progress, token usage
- **Timeout**: 3s
- **Output**: Status string for display (no additionalContext needed)
- **Value**: LOW (cosmetic) — nice to have for monitoring

### 2. Context Monitor
- **Event**: PostToolUse (debounce: every 5 tool calls)
- **Purpose**: Track context window usage, warn when running low
- **Timeout**: 5s
- **Thresholds**:
  - `>35%` remaining: silent (no output)
  - `<=35%` remaining: warning in additionalContext ("Context at {{pct}}% — consider committing")
  - `<=25%` remaining: critical ("CRITICAL: Context at {{pct}}% — commit NOW and signal")
- **Value**: HIGH — prevents lost work from context overflow

### 3. Workflow Guard
- **Event**: PreToolUse
- **Purpose**: Validate tool calls against scope fence (paths, commands)
- **Timeout**: 3s
- **Output**: Warning if tool targets path outside scope fence
- **Value**: MEDIUM — prevents accidental out-of-scope modifications

### 4. Prompt Guard
- **Event**: UserPromptSubmit
- **Purpose**: Scan handoff content for injection patterns, validate plan structure
- **Timeout**: 5s
- **Output**: Warning if suspicious patterns detected in .claude/handoffs/ references
- **Value**: MEDIUM — defense against prompt injection in plan files

### 5. Check Update
- **Event**: Notification (or periodic via cron)
- **Purpose**: Check for system updates, config changes, new handoffs in queue
- **Timeout**: 10s
- **Output**: Advisory about available updates or queued work
- **Value**: LOW — informational only

## Error Handling
- ALL hooks exit 0 regardless of internal errors (advisory = never block)
- Errors logged to `.claude/logs/hooks/` with timestamp
- If timeout-guard fires, hook is killed and execution continues silently

## Success Criteria
- Hook execution adds < 200ms to tool call latency (p95)
- Context monitor correctly detects <=35% threshold
- No hook ever returns exit code != 0 in production
