---
id: p01_kc_cex_tooling_master
kind: knowledge_card
pillar: P01
title: "CEX Tooling — 23 Python Tools Reference"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: meta-construction
quality: 9.2
tags: [cex, tools, python, reference, 8f-pipeline]
tldr: "Complete reference of all 23 CEX Python tools in _tools/. Organized by function: core pipeline (motor, runner, intent), batch ops (auto, batch, forge, crew), validation (doctor, hooks, score, system_test), lifecycle (compile, index, feedback), scaffolding (init, bootstrap, nucleus_builder, kind_register, materialize), and domain (mission, pipeline, research, flywheel)."
density_score: 0.94
related:
  - p02_agent_builder_nucleus
  - agent_card_n03
  - ctx_cex_new_dev_guide
  - p01_kc_8f_pipeline
  - build
  - skill
  - p06_if_builder_nucleus
  - agent_card_engineering_nucleus
  - p02_agent_creation_nucleus
  - p08_pat_3phase_build_protocol
---

# CEX Tooling — 23 Tools Reference

## Core Pipeline (Build an artifact)

| Tool | Lines | Purpose | Key Functions |
|------|-------|---------|---------------|
| **cex_8f_motor.py** | 400 | Intent parsing → kind resolution | `parse_intent()`, `classify_objects()`, `fan_out()`, `load_builder_map()` |
| **cex_8f_runner.py** | 1386 | Stateful 8F pipeline (F1→F8) | `EightFRunner.run()`, `load_iso()`, `strip_frontmatter()` |
| **cex_intent.py** | 533 | Natural language → governed prompt → LLM execution | `compose_prompt()`, `execute_prompt()`, `run_intent()` |

### 8F Runner Flow

```
Intent → Motor(parse) → Runner(F1-F8) → Artifact(.md) → Compile(.yaml) → Commit
         ↓                ↓
    kind+pillar     F1: load schema
    resolution      F2: load builder identity
                    F3: inject KCs + ISOs
                    F4: LLM reasoning plan
                    F5: tool discovery
                    F6: LLM produces artifact
                    F7: quality gates (6 hard checks + retry)
                    F8: save + compile + index + commit + signal
```

## Batch Operations (Build many artifacts)

| Tool | Lines | Purpose | Key Functions |
|------|-------|---------|---------------|
| **cex_auto.py** | 380 | Autonomous flywheel: scan→plan→execute→learn | `scan_system()`, `generate_plan()`, `run_cycle()` |
| **cex_batch.py** | 183 | Batch from file (1 intent per line) | `parse_intents()`, `run_8f()` |
| **cex_forge.py** | 513 | Seed-based generation with templates | `build_prompt()`, `inject_builder_context()` |
| **cex_crew_runner.py** | 665 | Multi-builder orchestration | `CrewRunner.compose()`, `load_builder_context()` |

## Validation & Quality

| Tool | Lines | Purpose | Key Functions |
|------|-------|---------|---------------|
| **cex_doctor.py** | 500 | Health check (builders, schemas, dirs) | `check_builders()`, `check_schemas()`, reports PASS/WARN/FAIL |
| **cex_hooks.py** | 329 | Git pre-commit validation | `validate_artifact()`, `compile_artifact()`, `run_pre_commit()` |
| **cex_score.py** | 218 | Heuristic quality scoring (5D) | `score_artifact(path)` → `(score, notes)` |
| **cex_system_test.py** | 358 | Full system test (54 checks) | `test_tools()`, `test_builders()`, `test_nuclei()`, `test_quality()` |

### Score Dimensions

```
1. Size (bytes) — content volume
2. Frontmatter — required fields present and valid
3. Sections — header count, structure
4. Density — info per byte (code blocks, tables, lists)
5. Domain signals — kind-specific keywords
```

## Lifecycle (Maintain artifacts)

| Tool | Lines | Purpose | Key Functions |
|------|-------|---------|---------------|
| **cex_compile.py** | 400 | .md → .yaml compilation | `compile_file()`, `compile_all()` |
| **cex_index.py** | 200 | Update registry/index files | `update_index()`, `index_all()` |
| **cex_feedback.py** | 455 | Quality tracking + learning records | `scan_artifacts()`, `analyze()`, `generate_report()` |

## Scaffolding (Create structure)

| Tool | Lines | Purpose | Key Functions |
|------|-------|---------|---------------|
| **cex_init.py** | 694 | Scaffold new CEX project (5 questions) | `interactive_flow()`, `create_nuclei()`, `copy_builders()` |
| **cex_bootstrap.py** | 142 | Sin-driven self-improvement | `run_nucleus_builder()`, `level2_expand()`, `level3_quality_spiral()` |
| **cex_nucleus_builder.py** | 195 | Build complete nucleus (7 artifacts) | `main()` — sequential agent → workflow → tools |
| **cex_kind_register.py** | 181 | Register new kind in taxonomy | `reg_meta()`, `reg_schema()`, `reg_ttt()`, `reg_motor()` |
| **cex_materialize.py** | 180 | Generate sub-agents from kinds_meta | `generate_agent_md()`, `materialize()` |

## Domain (Mission-level operations)

| Tool | Lines | Purpose | Key Functions |
|------|-------|---------|---------------|
| **cex_mission.py** | 271 | Mission executor (goal → tasks → artifacts) | `decompose_mission()`, `execute_task()`, `run_mission()` |
| **cex_pipeline.py** | 740 | 5-stage build engine (CAPTURE→ENVELOPE) | `capture_cli()`, `decompose()`, `hydrate()`, `compile()` |
| **cex_research.py** | 281 | Research helper with source scraping | `build_prompt()`, `build_source_scaffold()`, `list_sources()` |
| **cex_flywheel_worker.py** | 174 | Continuous improvement cycle | `gap_analysis()`, `build_kinds()`, `write_signal()` |

## Usage Patterns

```bash
# Single artifact
python _tools/cex_8f_runner.py "create knowledge_card about pytest" --execute

# Batch
echo "create kc about docker\ncreate kc about fastapi" | python _tools/cex_batch.py -

# Autonomous cycle
python _tools/cex_auto.py cycle --max 10

# Health check
python _tools/cex_doctor.py

# Score artifact
python _tools/cex_score.py path/to/artifact.md

# System test
python _tools/cex_system_test.py

# Register new kind
python _tools/cex_kind_register.py my_kind P01 "A new kind" --boundary 4096
```

## Tool Dependencies

```
cex_8f_runner → cex_8f_motor (intent parsing)
             → cex_intent (LLM execution)
             → cex_compile (F8 auto-compile)
             → cex_hooks (F7 validation)
cex_auto → cex_doctor (scan)
         → cex_8f_runner (execute)
         → cex_score (validate)
cex_batch → cex_8f_runner (per-intent execution)
cex_forge → cex_intent (LLM generation)
cex_crew_runner → cex_8f_runner (per-builder execution)
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_agent_builder_nucleus]] | downstream | 0.47 |
| [[agent_card_n03]] | related | 0.30 |
| [[ctx_cex_new_dev_guide]] | related | 0.27 |
| [[p01_kc_8f_pipeline]] | sibling | 0.27 |
| [[build]] | downstream | 0.24 |
| [[skill]] | downstream | 0.24 |
| [[p06_if_builder_nucleus]] | downstream | 0.24 |
| [[agent_card_engineering_nucleus]] | downstream | 0.24 |
| [[p02_agent_creation_nucleus]] | downstream | 0.24 |
| [[p08_pat_3phase_build_protocol]] | downstream | 0.23 |
