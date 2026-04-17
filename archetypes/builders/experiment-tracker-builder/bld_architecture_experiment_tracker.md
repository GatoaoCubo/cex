---
kind: architecture
id: bld_architecture_experiment_tracker
pillar: P08
llm_function: CONSTRAIN
purpose: 13-ISO component map of the experiment-tracker-builder
quality: 9.1
title: "Architecture Experiment Tracker"
version: "1.1.0"
author: n03_hybrid_review3
tags: [experiment_tracker, builder, architecture]
tldr: "13-ISO builder structure (manifest, system_prompt, instruction, schema, output_template, quality_gate, tools, examples, config, memory, knowledge_card, architecture, collaboration)"
domain: "experiment_tracker construction"
created: "2026-04-13"
updated: "2026-04-14"
density_score: 0.90
---

## Component Inventory (the 13 ISOs)
| # | ISO File | Kind | Pillar | LLM Function | Role |
| :-- | :--- | :--- | :--- | :--- | :--- |
| 1 | bld_manifest_experiment_tracker.md | type_builder | P07 | BECOME | Identity, capabilities, routing |
| 2 | bld_system_prompt_experiment_tracker.md | system_prompt | P03 | BECOME | Persona + scope + quality rules |
| 3 | bld_instruction_experiment_tracker.md | instruction | P03 | REASON | FRAME -> INSTRUMENT -> EXECUTE -> GOVERN phases |
| 4 | bld_schema_experiment_tracker.md | schema | P06 | CONSTRAIN | Frontmatter fields, ID regex, body structure |
| 5 | bld_output_template_experiment_tracker.md | output_template | P05 | PRODUCE | Body skeleton (objective, hypothesis, params, results) |
| 6 | bld_quality_gate_experiment_tracker.md | quality_gate | P11 | GOVERN | HARD H01-H07 + SOFT D1-D9 (weights=1.00) |
| 7 | bld_tools_experiment_tracker.md | tools | P04 | CALL | Real cex_* + MLflow/W&B/Neptune backends |
| 8 | bld_examples_experiment_tracker.md | examples | P07 | GOVERN | Gold-standard exemplars |
| 9 | bld_config_experiment_tracker.md | config | P09 | CONSTRAIN | Runtime settings, retention |
| 10 | bld_memory_experiment_tracker.md | memory | P10 | INJECT | Retrieved context per F3 |
| 11 | bld_knowledge_card_experiment_tracker.md | knowledge_card | P01 | INJECT | Domain knowledge card |
| 12 | bld_architecture_experiment_tracker.md | architecture | P08 | CONSTRAIN | This file |
| 13 | bld_collaboration_experiment_tracker.md | collaboration | P12 | COLLABORATE | Handoff to N05 (ops), N01 (analysis) |

## ISO Dependencies
| From | To | Type |
| :--- | :--- | :--- |
| system_prompt | manifest | identity inheritance |
| instruction | schema | phases produce schema-valid fields |
| output_template | schema | placeholders -> fields |
| quality_gate | schema | HARD gates check schema fields |
| tools | instruction | backends called per phase |
| examples | output_template | filled runs |

## Architectural Position
The experiment-tracker-builder produces experiment_tracker artifacts (pillar P07, `p07_et_*.md`). Artifacts map cleanly onto MLflow runs, W&B runs, Neptune experiments, Comet ML experiments. Consumed by N01 (meta-analysis), N05 (ops reproducibility), N07 (orchestration of sweeps).

## Pipeline Mapping
| 8F | Uses ISO |
| :--- | :--- |
| F1 CONSTRAIN | schema, architecture |
| F2 BECOME | manifest, system_prompt |
| F3 INJECT | knowledge_card, memory |
| F4 REASON | instruction |
| F5 CALL | tools |
| F6 PRODUCE | output_template, examples |
| F7 GOVERN | quality_gate |
| F8 COLLABORATE | collaboration |
