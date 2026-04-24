---
id: p04_ct_n03_build
kind: cli_tool
8f: F5_call
pillar: P04
title: "CLI Tool -- N03 Build Interface (cex_build)"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: artifact-construction
quality: 9.1
tags: [cli-tool, N03, build, interface, cex-build, 8F, dispatch]
tldr: "CLI interface contract for cex_build.py -- N03's primary build entry point. Documents all flags, subcommands, exit codes, and integration with the 8F pipeline. Used by N07 dispatch and direct human invocation."
density_score: 0.91
updated: "2026-04-17"
related:
  - p02_agent_creation_nucleus
  - agent_card_engineering_nucleus
  - ctx_cex_new_dev_guide
  - build
  - p01_kc_cex_project_overview
  - p03_sp_n03_creation_nucleus
  - p12_wf_create_orchestration_agent
  - p06_if_builder_nucleus
  - bld_collaboration_kind
  - p01_ctx_cex_project
---

# CLI Tool: N03 Build Interface (cex_build)

## Overview

`cex_build.py` is N03's primary CLI. It accepts a build contract, executes the full
8F pipeline, and outputs a structured result. All N07 dispatches to N03 route through
this interface or its equivalent cex_8f_runner.py.

## Base Command

```bash
python cex_sdk/cex_8f_runner.py [OPTIONS]
# Alias: python _tools/cex_build.py [OPTIONS]  (if installed)
```

## Subcommands

| Subcommand | Purpose |
|-----------|---------|
| `build` | Execute full 8F pipeline (default) |
| `validate` | Run F7 GOVERN only (no F6, no F8) |
| `dry-run` | Execute F1-F5, print plan, stop before F6 |
| `improve` | Run self-improvement loop on target artifact |
| `batch` | Process list of intents from file |

## Options (build subcommand)

| Flag | Short | Type | Default | Description |
|------|-------|------|---------|-------------|
| `--intent` | `-i` | string | required* | Natural language build request |
| `--kind` | `-k` | string | resolved | Explicit kind override |
| `--pillar` | `-p` | string | derived | Pillar override |
| `--verb` | `-v` | enum | CREATE | BUILD_ACTION verb |
| `--quality-target` | `-q` | float | 9.0 | Minimum quality score |
| `--domain` | `-d` | string | null | Domain for context injection |
| `--output-dir` | `-o` | path | derived | Override output directory |
| `--model` | `-m` | enum | opus | Model tier: haiku/sonnet/opus |
| `--dry-run` | | bool | false | Simulate; print plan only |
| `--no-compile` | | bool | false | Skip cex_compile.py after save |
| `--no-signal` | | bool | false | Skip signal_writer.py |
| `--force` | `-f` | bool | false | Overwrite existing artifact |
| `--nucleus` | `-n` | enum | n03 | Executing nucleus ID |

*`--intent` OR `--kind` required; both may be specified.

## Exit Codes

| Code | Meaning | Action |
|------|---------|--------|
| 0 | Build complete; all gates passed | N07 proceeds to next wave |
| 1 | Build failed; artifact not saved | N07 checks failure signal |
| 2 | Validation error; bad input contract | N07 corrects dispatch params |
| 3 | Compile error; artifact saved but invalid YAML | N07 triggers bugloop |
| 4 | Quality gate failed after 2 retries | N07 escalation required |
| 5 | Token budget exhausted | N07 pauses dispatch |

## Usage Examples

### Minimal build
```bash
python cex_sdk/cex_8f_runner.py -i "create a system prompt for the research agent"
```

### Explicit kind + quality target
```bash
python cex_sdk/cex_8f_runner.py \
  --kind knowledge_card \
  --verb CREATE \
  --domain "embedding strategies" \
  --quality-target 9.5 \
  --nucleus n03
```

### Validate existing artifact (no write)
```bash
python cex_sdk/cex_8f_runner.py validate \
  --kind scoring_rubric \
  N03_engineering/P07_evals/scoring_rubric_n03.md
```

### Batch build from file
```bash
python cex_sdk/cex_8f_runner.py batch \
  --file .cex/runtime/handoffs/batch_n03_w1.txt \
  --nucleus n03 \
  --quality-target 9.0
```

### Dry run (print plan, no write)
```bash
python cex_sdk/cex_8f_runner.py --dry-run \
  -i "create an input schema for the build contract" \
  --kind input_schema
```

## stdout Format (machine-parseable)

```
=== 8F PIPELINE ===
F1 CONSTRAIN: kind=input_schema, pillar=P06, max=3072B
F2 BECOME: input-schema-builder loaded (13 ISOs)
F2b SPEAK: vocabulary loaded (20 terms). Drift prevention: active.
F3 INJECT: kc_input_schema.md + 2 examples. Match: 72%
F4 REASON: 5 sections, approach=template (adapt from match)
F5 CALL: compile+doctor+index ready. 3 similar found.
F6 PRODUCE: 2,840 bytes, 5 sections, density=0.91
F7 GOVERN: Score pending. Gates: 7/7. 12LP: 12/12
F8 COLLABORATE: saved N03_engineering/P06_schema/input_schema_build_contract.md. Compiled. Committed.
===================
EXIT: 0
```

## Integration with N07 Dispatch

N07 writes handoff to `.cex/runtime/handoffs/n03_task.md`.
N03 reads handoff on boot. Handoff contains structured CLI arguments:

```yaml
# Handoff excerpt
cli_args:
  kind: input_schema
  verb: CREATE
  quality_target: 9.0
  nucleus: n03
  compile: true
  signal: true
```

N03 boot script: `boot/n03.ps1` reads task file, constructs CLI call, executes.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_agent_creation_nucleus]] | upstream | 0.40 |
| [[agent_card_engineering_nucleus]] | upstream | 0.40 |
| [[ctx_cex_new_dev_guide]] | related | 0.34 |
| [[build]] | downstream | 0.31 |
| [[p01_kc_cex_project_overview]] | upstream | 0.29 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.29 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.28 |
| [[p06_if_builder_nucleus]] | downstream | 0.28 |
| [[bld_collaboration_kind]] | downstream | 0.28 |
| [[p01_ctx_cex_project]] | upstream | 0.27 |
