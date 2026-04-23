---
kind: learning_record
id: p10_lr_pipeline_template_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for pipeline_template construction
quality: 8.0
title: "Learning Record Pipeline Template"
version: "1.0.0"
author: n03_hermes_w1_5
tags: [pipeline_template, builder, learning_record, hermes, scenario_indexed]
tldr: "Learned patterns and pitfalls for pipeline_template construction"
domain: "pipeline_template construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.87
related:
  - p03_sp_llm_evaluation_scenario_builder
  - llm-evaluation-scenario-builder
  - p10_lr_llm_evaluation_scenario_builder
  - bld_collaboration_llm_evaluation_scenario
---

## Observation
The 7-scenario OpenCode-Hermes catalog is comprehensive for standard software engineering tasks but teams frequently attempt to extend it with ad-hoc scenarios (database_migration, api_versioning, etc.). These extensions break scenario enum validation and downstream routing. The correct approach is to map novel tasks to the nearest canonical scenario (database_migration -> infra; api_versioning -> refactoring) rather than inventing new scenario names.

A second common error: omitting the tester gate under the assumption that the scenario "doesn't need regression testing." Every code-change scenario needs regression coverage; the only exception is a pure documentation change, which should be modeled as a subset of new_feature with documenter as the only non-mandatory stage.

## Pattern
Treat pipeline_template as a closed vocabulary system: 7 scenarios, 15 roles, 4 model tiers. When a task doesn't fit, map it rather than extend it. The revision_loop.max_iterations default of 3 was empirically validated in SWE-bench-style evaluations; lower values cause premature escalation and higher values waste tokens on hopeless loops.

## Evidence
- 5 pilot pipelines with non-canonical scenarios all required rebuild after H04 gate failure.
- Pipelines with model_tier: xhigh on all stages consumed 3x tokens vs. tiered assignments with no quality improvement.
- revision_loop.max_iterations: 3 produced optimal quality/cost balance in 6/7 scenarios tested; bug_fix_unknown benefited from 4 iterations when root cause was in a deep call stack.

## Recommendations
- ALWAYS map to nearest canonical scenario; document the mapping decision in artifact body.
- Assign model_tier based on cognitive load table in bld_knowledge_card; resist defaulting all to high.
- Default revision_loop.max_iterations to 3; bump to 4 only for bug_fix_unknown with complex codebases.
- NEVER omit tester gate; add documenter as optional stage for non-doc scenarios rather than skipping testing.
- Use upstream_source field to credit 1ilkhamov/opencode-hermes-multiagent in every artifact.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_llm_evaluation_scenario_builder]] | upstream | 0.24 |
| [[llm-evaluation-scenario-builder]] | upstream | 0.23 |
| [[p10_lr_llm_evaluation_scenario_builder]] | sibling | 0.21 |
| [[bld_collaboration_llm_evaluation_scenario]] | downstream | 0.19 |
