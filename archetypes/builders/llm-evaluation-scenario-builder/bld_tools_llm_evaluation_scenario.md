---
kind: tools
id: bld_tools_llm_evaluation_scenario
pillar: P04
llm_function: CALL
purpose: Tools available for llm_evaluation_scenario production
quality: 8.9
title: "Tools LLM Evaluation Scenario"
version: "1.0.0"
author: n06_wave7
tags: [llm_evaluation_scenario, builder, tools, helm]
tldr: "Tools available for llm_evaluation_scenario production"
domain: "llm_evaluation_scenario construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_knowledge_card_llm_evaluation_scenario
  - llm-evaluation-scenario-builder
  - p03_sp_llm_evaluation_scenario_builder
  - bld_instruction_llm_evaluation_scenario
  - p07_qg_llm_evaluation_scenario
  - bld_collaboration_llm_evaluation_scenario
  - bld_schema_llm_evaluation_scenario
  - bld_tools_eval_framework
  - bld_knowledge_card_eval_framework
  - p10_lr_llm_evaluation_scenario_builder
---

## Production Tools
| Tool                 | Purpose                                    | When                        |
|----------------------|--------------------------------------------|-----------------------------|
| cex_compile.py       | Compile scenario YAML from Markdown        | After F6 PRODUCE            |
| cex_score.py         | Peer-review quality scoring                | F7 GOVERN                   |
| cex_retriever.py     | Find similar existing scenarios            | F3 INJECT / duplicate check |
| cex_doctor.py        | Builder health diagnostics                 | Pre-build validation        |
| cex_validator.py     | Schema compliance check (H01-H08 gates)    | F7 GOVERN                   |
| cex_query.py         | TF-IDF discovery of related eval kinds     | F5 CALL                     |

## Validation Tools
| Tool                   | Purpose                                 | When                     |
|------------------------|-----------------------------------------|--------------------------|
| helm_validate.py       | HELM-spec compliance (canonical check)  | Post-compose             |
| canonicalization_test  | Verify normalization function on 10 samples | Before F8 COLLABORATE |
| dataset_license_check  | Validate upstream dataset license       | Phase 1 RESEARCH         |
| token_cost_estimate    | Compute prompt + completion token budget | Phase 2 COMPOSE         |

## External References
- HELM Python library: `github.com/stanford-crfm/helm` (scenario runner, adapter, metrics)
- IBM fms-fmeval: `github.com/foundation-model-stack/fms-fmeval` (enterprise extensions)
- HELM leaderboard API: `crfm.stanford.edu/helm/latest/` (scenario registry, run results)
- MLCommons AILuminate runner: compatible HELM runner for safety scenarios
- BigBench data loader: 204-task JSON format, compatible with HELM adapter

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_llm_evaluation_scenario]] | upstream | 0.58 |
| [[llm-evaluation-scenario-builder]] | downstream | 0.44 |
| [[p03_sp_llm_evaluation_scenario_builder]] | upstream | 0.39 |
| [[bld_instruction_llm_evaluation_scenario]] | upstream | 0.39 |
| [[p07_qg_llm_evaluation_scenario]] | downstream | 0.32 |
| [[bld_collaboration_llm_evaluation_scenario]] | downstream | 0.31 |
| [[bld_schema_llm_evaluation_scenario]] | downstream | 0.29 |
| [[bld_tools_eval_framework]] | sibling | 0.27 |
| [[bld_knowledge_card_eval_framework]] | upstream | 0.26 |
| [[p10_lr_llm_evaluation_scenario_builder]] | downstream | 0.24 |
