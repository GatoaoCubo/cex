---
id: p08_cm_n03
kind: component_map
pillar: P08
title: "Component Map -- N03 Engineering System"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: artifact-construction
quality: 9.1
tags: [component-map, N03, architecture, dependencies, 8F, builders, system]
tldr: "Dependency map of all N03 engineering system components: builders (259), SDK tools (78), quality infrastructure, schema layer, and runtime artifacts. Shows how components compose to produce the 8F pipeline execution."
density_score: 0.92
updated: "2026-04-17"
---

# Component Map: N03 Engineering System

## System Overview

N03's engineering system is a layered composition of builders, tools, schemas, and protocols.
This map shows dependencies, not just inventory. Understanding the dependency graph prevents
build failures from missing prerequisites and enables confident refactoring.

## Layer 0: Identity (Sin Lens Layer)

```
N03_engineering/P02_model/agent_engineering.md
  |-- nucleus_def_n03.md          (machine-readable identity)
  |-- agent_card_n03.md           (deployment card)
  `-- agent_package_n03.md        (packaged configuration)

N03_engineering/rules/n03-8f-enforcement.md
  |-- Enforces: 8F mandatory for all builds
  `-- Source: .claude/rules/8f-reasoning.md
```

## Layer 1: Schema Foundation (P06)

The schema layer is the CONTRACT layer. All other layers depend on it.

```
P06_schema/
  |-- input_schema_build_contract.md   <- BUILD ENTRY POINT CONTRACT
  |-- validation_schema_artifact.md    <- OUTPUT VALIDATION CONTRACT
  |-- type_def_cex_types.md            <- TYPE SYSTEM (Kind, Pillar, Nucleus, Quality...)
  |-- interface_builder_protocol.md    <- BUILDER BILATERAL CONTRACT
  |-- enum_def_build_actions.md        <- CONSTANTS (BUILD_ACTION, PILLAR, NUCLEUS...)
  `-- api_reference_8f_pipeline.md     <- F1-F8 CALLABLE INTERFACE

Dependencies: none (foundation layer)
Depended on by: ALL other layers
```

## Layer 2: Builder Runtime (archetypes/)

The builders are the execution engine. 259 builders, each with 13 ISOs.

```
archetypes/builders/
  {kind}-builder/                    (259 directories)
    |-- bld_manifest_{kind}.md       (F1: kind constraints)
    |-- bld_instruction_{kind}.md    (F4: production instructions)
    |-- bld_system_prompt_{kind}.md  (F2: builder identity)
    |-- bld_schema_{kind}.md         (F1: validation schema)
    |-- bld_template_{kind}.md       (F6: output template)
    |-- bld_quality_gates_{kind}.md  (F7: quality gates)
    |-- bld_examples_{kind}.md       (F3: positive examples)
    |-- bld_anti_examples_{kind}.md  (F3: anti-examples)
    |-- bld_knowledge_{kind}.md      (F3: domain knowledge)
    |-- bld_prompt_cache_{kind}.md   (F5: cached context)
    |-- bld_compiler_{kind}.md       (F8: compilation rules)
    |-- bld_scorer_{kind}.md         (F7: scoring rubric)
    `-- bld_memory_{kind}.md         (F3b: memory injection)

Dependencies: P06 schema layer (contracts), N00_genesis (archetypes)
```

## Layer 3: SDK Motor (cex_sdk/)

Python tools that execute the pipeline and manage artifacts.

```
cex_sdk/
  |-- cex_8f_motor.py          (intent -> kind -> plan; 1385L)
  |-- cex_8f_runner.py         (full 8F execution; F1->F8)
  |-- cex_compile.py           (.md -> .yaml; post-F8)
  |-- cex_doctor.py            (artifact health scan)
  |-- cex_retriever.py         (TF-IDF similarity; F3 INJECT)
  |-- cex_score.py             (5D scoring; F7 GOVERN)
  |-- cex_hooks.py             (pre-commit validation)
  |-- signal_writer.py         (F8 signal write)
  |-- cex_sanitize.py          (ASCII compliance)
  `-- cex_query.py             (TF-IDF builder discovery)

Dependencies: P06 type_def, enum_def; .cex/kinds_meta.json
```

## Layer 4: Quality Infrastructure (P07 + P11)

```
P07_evals/
  |-- scoring_rubric_n03.md    (5D scoring model)
  |-- llm_judge_n03.md         (L3 semantic evaluation)
  |-- regression_check_n03.md  (drift detection)
  `-- golden_test_n03.md       (expected output tests)

P11_feedback/
  |-- quality_gate_n03.md      (H01-H07 hard gates + 12LP)
  |-- bugloop_n03.md           (autonomous error correction)
  `-- self_improvement_loop_n03.md  (quality flywheel)

Dependencies: P06 validation_schema; cex_sdk motor+score
Depended on by: every F7 GOVERN call
```

## Layer 5: Knowledge Base (P01)

```
P01_knowledge/
  |-- kc_8f_pipeline_implementation.md  (8F implementation details)
  |-- kc_construction_laws.md           (build quality laws)
  |-- kc_cex_tooling_master.md          (tool reference)
  |-- kc_engineering_vocabulary.md      (controlled vocabulary KC)
  `-- [+ 10 more KCs]

N00_genesis/P01_knowledge/library/kind/
  |-- kc_{kind}.md  (424 kind KCs; loaded at F3 INJECT)

Dependencies: none (base layer)
Depended on by: F3 INJECT in every 8F run
```

## Dependency Flow (Build Request -> Artifact)

```
User/N07 intent
    |
    v
cex_8f_motor.py (intent -> kind + plan)
    |
    v [F1 CONSTRAIN]
.cex/kinds_meta.json + P06 type_def + P06 enum_def
    |
    v [F2 BECOME]
archetypes/builders/{kind}-builder/ (13 ISOs)
    |
    v [F3 INJECT]
P01_knowledge/kc_{kind}.md + examples + brand_config
    |
    v [F6 PRODUCE]
draft artifact (frontmatter + body)
    |
    v [F7 GOVERN]
P11_feedback/quality_gate_n03.md -> P07_evals/scoring_rubric_n03.md
    |
    v [F8 COLLABORATE]
N03_engineering/P{xx}/{kind}_{name}.md (saved artifact)
    |
    cex_compile.py -> compiled/.yaml
    signal_writer.py -> .cex/runtime/signals/
    git commit
```

## Component Count Summary

| Layer | Component Type | Count |
|-------|---------------|-------|
| L0 | Identity artifacts | 3 |
| L1 | Schema contracts | 6+ |
| L2 | Builder ISOs (13 per builder) | 259 builders x 13 = 3367 |
| L3 | SDK Python tools | 78 |
| L4 | Quality infrastructure artifacts | 7 |
| L5 | Knowledge cards | 424+ |
| Runtime | Handoffs, signals, PIDs | variable |
