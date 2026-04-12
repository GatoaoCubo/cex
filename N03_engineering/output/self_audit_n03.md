---
id: self_audit_n03_builder_20260408
kind: knowledge_card
pillar: P01
title: "N03 Builder Self-Audit -- Agent Definitions & Builder Capabilities"
version: 1.0.0
created: 2026-04-08
author: n03_builder
mission: CLAUDE_NATIVE
quality: 9.0
tags: [audit, n03, builder, agents, claude-code, self-audit]
tldr: "125 agent defs cover all 123 kinds. 0 PI refs. 118/125 have generic placeholder tldr. Model routing is flat sonnet -- complex kinds should use opus."
density_score: 0.91
---

# N03 Builder Self-Audit

## Executive Summary

| Metric | Value | Status |
|--------|-------|--------|
| Agent definitions | 125 files | OK |
| Kinds in registry | 123 kinds | OK |
| Kind-to-agent coverage | 123/123 (100%) | PASS |
| Extra agents | 2 (kind-builder, validator) | Expected |
| PI references in agents | 0 | PASS |
| PI references in shared ISOs | 0 | PASS |
| Generic placeholder tldr | 118/125 (94%) | FAIL |
| Flat model routing (all sonnet) | 118/125 (94%) | NEEDS REVIEW |

## 1. Agent Coverage Analysis

### 1:1 Kind-to-Builder Mapping

Every kind in `.cex/kinds_meta.json` has a corresponding `.claude/agents/{kind}-builder.md`.
Naming convention: underscore in kind (`action_prompt`) maps to hyphen in agent (`action-prompt-builder.md`).

**Extra agents (not tied to a specific kind):**

| Agent | Purpose |
|-------|---------|
| `kind-builder.md` | Generic/meta builder -- builds any kind by dynamically loading ISOs |
| `validator.md` | Read-only validation agent (uses `disallowedTools: Write, Edit`) |

### Missing Builders: None

All 123 kinds have a dedicated builder agent definition. No gaps.

## 2. PI Reference Sweep

| Scope | Files Searched | PI Matches |
|-------|---------------|------------|
| `.claude/agents/` | 125 | 0 |
| `archetypes/builders/_shared/` | all | 0 |

Both scopes are fully clean of PI wrapper references. No remediation needed.

## 3. Quality Issues Found

### 3.1 Generic Placeholder tldr (CRITICAL)

**118 of 125** agent definitions contain this identical, incorrect tldr:

```yaml
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
```

This is a copy-paste artifact from `cex_materialize.py` -- the tldr describes an examples document, not a builder agent. Each builder should have a kind-specific tldr matching its `description` field.

**Impact**: Low (tldr is metadata, not loaded into builder reasoning). But violates density principle -- every field should carry signal.

**Fix**: Batch update via `cex_materialize.py` regeneration, pulling tldr from each builder's `bld_manifest_{kind}.md`.

### 3.2 Flat Model Routing

118/125 agent definitions use `model: sonnet`. This is a reasonable cost-optimization default, but some kinds require deeper reasoning:

| Kind Category | Suggested Model | Reason |
|---------------|----------------|--------|
| Architecture kinds (component_map, interface, dag) | opus | Multi-system reasoning |
| Evaluation kinds (e2e_eval, benchmark, llm_judge) | opus | Complex rubric construction |
| Orchestration kinds (workflow, supervisor, dispatch_rule) | opus | Cross-nucleus dependency planning |
| Simple data kinds (enum_def, env_config, path_config) | haiku | Structural, low reasoning load |
| All others | sonnet | Good balance of cost and quality |

**Impact**: Medium. Complex kinds built with sonnet may not hit 9.0 quality floor consistently.

**Fix**: Add a `model_override` map in `cex_materialize.py` keyed by kind complexity tier.

### 3.3 Agent Tool References

Agent definitions correctly use Claude Code native format:
- `tools: Read, Write, Edit, Bash, Glob, Grep` for builders
- `disallowedTools: Write, Edit` for validator (read-only enforcement)

No agent references PI subagent mechanisms. The `Agent` tool's `subagent_type` parameter in Claude Code system prompt correctly maps to these agent definition names.

## 4. Claude Code Native Features -- Unused Opportunities

| Feature | Current State | Opportunity |
|---------|--------------|-------------|
| `isolation: "worktree"` | Not used | Parallel artifact builds could use worktrees to avoid git conflicts |
| `model` field per-agent | Flat sonnet | Tiered routing (see 3.2 above) |
| Agent `run_in_background` | Not referenced in defs | Builders could signal async completion |
| Agents inline JSON | Not used | Alternative to file-based agent defs for one-shot builds |
| Custom `allowedTools` | Broad (6 tools for all) | Some builders don't need Bash (pure content kinds) |

### Recommended Improvements (priority order)

1. **Fix generic tldr** across 118 agent defs (batch, low risk)
2. **Tiered model routing** for complex vs simple kinds (medium effort, high impact)
3. **Restrict tools** per builder -- pure content builders don't need Bash (low effort, cleaner security)
4. **Worktree isolation** for parallel grid builds (requires dispatch.sh changes)

## 5. Files Modified in This Audit

| File | Change | Task |
|------|--------|------|
| `N03_builder/orchestration/spawn_config_builder.md` | `pi` -> `claude` (3 refs) | Task 1 |
| `N04_knowledge/orchestration/spawn_config_knowledge.md` | `pi` -> `claude` (1 ref) | Task 1 |
| `N07_admin/orchestration/spawn_config_admin.md` | `pi + claude` -> `claude` (1 ref) | Task 1 |
| `.claude/rules/n07-autonomous-lifecycle.md` | `pi` -> `claude` (3 refs) | Task 4 |
| `N03_engineering/output/self_audit_n03.md` | Created (this file) | Task 5 |

## 6. Spawn Config PI Cleanup Summary

| File | Before | After |
|------|--------|-------|
| N03 spawn_config line 13 | `pi CLI with claude opus-4-6` | `claude CLI with opus-4-6` |
| N03 spawn_config line 35 | `cli: pi` | `cli: claude` |
| N03 spawn_config line 54 | `pi --model opus-4-6` | `claude --model opus-4-6` |
| N04 spawn_config line 31 | `pi --model opus-4-6` | `claude --model opus-4-6` |
| N07 spawn_config line 29 | `pi + claude` | `claude` |
| N07 lifecycle rule lines 109-111 | `pi (pi runtime)` x3 | `claude (Claude Code runtime)` x3 |
