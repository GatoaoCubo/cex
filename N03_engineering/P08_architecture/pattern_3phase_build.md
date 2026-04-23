---
id: p08_pat_3phase_build_protocol
kind: pattern
pillar: P08
title: 3-Phase Build Protocol -- Pre-Flight / Execute / Synthesize
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.1
tags: [pattern, protocol, 3-phase, execution, workflow]
tldr: Every build follows three phases -- validate intent (30s), execute with full autonomy (5-30min), synthesize results (1min). No shortcuts.
density_score: 0.91
related:
  - bld_instruction_kind
  - p03_sp_n03_creation_nucleus
  - p01_kc_8f_pipeline
  - skill
  - tpl_instruction
  - bld_tools_kind
  - bld_architecture_kind
  - p08_pat_construction_triad
  - ctx_cex_new_dev_guide
  - p03_sp_builder_nucleus
---

# 3-Phase Build Protocol

Proven across 700+ builds. Applies to single artifacts AND grid batches.

## Phase 1: Pre-Flight (30 seconds)

**Purpose**: Validate intent BEFORE committing resources.

| Step | Action | Output |
|------|--------|--------|
| 1.1 | Parse intent into {verb, object, kind, domain} | Structured spec |
| 1.2 | Check constraints: does the kind exist? Is the pillar correct? | Boolean |
| 1.3 | Search for existing artifacts (Template-First pattern) | Match list |
| 1.4 | Load builder ISOs for the target kind | 13 ISO files |
| 1.5 | If interactive: ask 1 clarifying question (max) | Refinement |
| 1.6 | If headless: proceed with defaults | Auto-resolve |

**Gate**: If kind is unresolvable or pillar mismatch, STOP. Do not guess.

### Pre-Flight Checklist

```
[ ] Kind resolved in kinds_meta.json?
[ ] Builder exists in archetypes/builders/{kind}-builder/?
[ ] Target pillar directory exists in nucleus?
[ ] No duplicate artifact at target path?
[ ] Schema loaded for target pillar?
```

## Phase 2: Autonomous Execution (5-30 minutes)

**Purpose**: Build with full autonomy. Zero interruptions.

| Step | Action | Maps to 8F |
|------|--------|------------|
| 2.1 | Load constraints (schema + config) | F1 CONSTRAIN |
| 2.2 | Load identity (system prompt + mental model) | F2 BECOME |
| 2.3 | Inject knowledge (KCs + builder ISOs + examples) | F3 INJECT |
| 2.4 | Reason and plan the approach | F4 REASON |
| 2.5 | Identify available tools | F5 CALL |
| 2.6 | Generate artifact content | F6 PRODUCE |
| 2.7 | Validate against quality gates | F7 GOVERN |
| 2.8 | If F7 fails: retry F6-F7 (max 2 attempts) | F6-F7 loop |
| 2.9 | Save, compile, index, signal | F8 COLLABORATE |

**Gate**: F7 must pass (score >= 8.0) before F8. No exceptions.

### Autonomy Rules

- Do NOT ask questions during Phase 2
- Do NOT skip validation steps
- Do NOT save artifacts below 7.0
- DO retry failed validations (max 2)
- DO commit immediately after save
- DO write completion signal

## Phase 3: Synthesis (1 minute)

**Purpose**: Report what was built, how good it is, what comes next.

### If quality >= 8.0 (Full Report):

```
## Build Report
- Artifact: {path}
- Kind: {kind} | Pillar: {pillar}
- Quality: {score}/10
- Key decisions: {list}
- Gaps found: {list or "none"}
- Suggested next: {list}
```

### If quality < 8.0 (Brief + Retry Plan):

```
## Build Incomplete
- Artifact: {path} (DRAFT)
- Quality: {score}/10 -- below threshold
- Failures: {which gates failed}
- Retry plan: {what to change}
```

## Phase Timing

| Phase | Interactive | Headless (Grid) |
|-------|-------------|-----------------|
| Pre-Flight | 30s (1 question) | 5s (auto-resolve) |
| Execute | 5-30min | 5-30min (same quality) |
| Synthesis | 1min (full report) | 10s (signal only) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_kind]] | upstream | 0.31 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.30 |
| [[p01_kc_8f_pipeline]] | upstream | 0.30 |
| [[skill]] | related | 0.29 |
| [[tpl_instruction]] | upstream | 0.28 |
| [[bld_tools_kind]] | upstream | 0.28 |
| [[bld_architecture_kind]] | related | 0.28 |
| [[p08_pat_construction_triad]] | sibling | 0.28 |
| [[ctx_cex_new_dev_guide]] | related | 0.26 |
| [[p03_sp_builder_nucleus]] | upstream | 0.26 |
