---
id: p07_qg_builder_construction
kind: quality_gate
pillar: P07
title: "Quality Gate — N03 Builder Output"
version: 2.0.0
created: 2026-04-07
updated: 2026-04-07
author: builder_agent
domain: construction
quality: 8.9
tags: [quality-gate, builder, N03, validation, 8F, frontmatter]
tldr: "Quality gate for N03 builder output — 8 checkpoints from frontmatter validity to compilation sync."
gate_count: 8
pass_threshold: 8.0
reject_action: rebuild
density_score: 0.94
linked_artifacts:
  primary: "N03_builder/agents/agent_builder.md"
  related:
    - N03_builder/prompts/system_prompt_builder.md
    - N03_builder/schemas/artifact_schema_builder.md
---

# Quality Gate — N03 Builder Output

## Purpose

Every artifact produced by N03 must pass these 8 checkpoints before being accepted.
The builder does NOT assign quality scores — peer review handles scoring.
The builder DOES enforce structural, syntactic, and pipeline compliance.

## Checkpoints

### Gate 1: Frontmatter Validity
- **Check**: YAML frontmatter parses without errors
- **Tool**: `python -c "import yaml; yaml.safe_load(open(path)...)"` or pre-commit hook
- **Fail action**: Fix YAML syntax immediately
- **Severity**: BLOCKER

### Gate 2: Required Fields Present
- **Check**: All fields required by kind schema are present in frontmatter
- **Required universal**: `id`, `kind`, `pillar`, `title`, `version`, `created`, `updated`, `author`, `quality`, `tags`, `tldr`
- **Tool**: `cex_hooks.py` pre-validation
- **Fail action**: Add missing fields
- **Severity**: BLOCKER

### Gate 3: Quality Field is Null
- **Check**: `quality: null` — never a number, never a string
- **Tool**: grep + manual check
- **Fail action**: Reset to `quality: null`
- **Severity**: BLOCKER

### Gate 4: Schema Compliance
- **Check**: Frontmatter matches `P{pillar}_*/_schema.yaml` constraints
- **Tool**: `cex_hooks.py` schema validation
- **Fail action**: Adjust fields to match schema
- **Severity**: CRITICAL

### Gate 5: Body Structure
- **Check**: Body follows kind's output format (from ISO `07_output_format.md`)
- **Check**: Body stays under kind's `max_bytes` limit
- **Tool**: Manual review against ISO template
- **Fail action**: Restructure body
- **Severity**: MAJOR

### Gate 6: 8F Pipeline Complete
- **Check**: All 8 steps executed (no skipped steps)
- **Check**: 8F trace included in builder output
- **Tool**: Builder self-check (trace log)
- **Fail action**: Re-execute from skipped step
- **Severity**: BLOCKER

### Gate 7: Compilation Sync
- **Check**: `.yaml` exists alongside `.md` in compiled directory
- **Check**: `.yaml` content matches `.md` frontmatter
- **Tool**: `cex_compile.py {path}` + diff
- **Fail action**: Re-compile
- **Severity**: CRITICAL

### Gate 8: Commit Convention
- **Check**: Commit message starts with `[N03]`
- **Check**: Only scoped files are staged (no stray changes)
- **Tool**: Git pre-commit hook
- **Fail action**: Amend commit message
- **Severity**: MAJOR

## Quality Tiers (assigned by peer review, NOT builder)

| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Reference example — archive as golden |
| PUBLISH | >= 8.0 | Standard publication — accepted |
| REVIEW | >= 7.0 | Needs revision — return with feedback |
| REJECT | < 7.0 | Redo from scratch — full rebuild |

## Pass/Fail Summary

- **PASS**: All 8 gates pass → artifact accepted, signal complete
- **FAIL**: Any BLOCKER fails → artifact blocked, fix required before signal
- **WARN**: MAJOR or CRITICAL fails → artifact accepted with noted issues

## References

- Schema validation: N03_builder/schemas/artifact_schema_builder.md
- Agent definition: N03_builder/agents/agent_builder.md
- Quality tools: `_tools/cex_hooks.py`, `_tools/cex_score.py`
