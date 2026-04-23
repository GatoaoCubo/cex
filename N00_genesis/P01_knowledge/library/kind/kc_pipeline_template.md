---
quality: 8.0
quality: 7.8
id: kc_pipeline_template
kind: knowledge_card
pillar: P01
nucleus: n00
title: "KC: pipeline_template"
version: 1.0
tags: [knowledge_card, pipeline_template, p12, hermes, scenario_indexed, opencode]
density_score: 1.0
upstream_source: "1ilkhamov/opencode-hermes-multiagent"
related:
  - bld_schema_e2e_eval
  - bld_schema_quickstart_guide
  - bld_schema_bugloop
  - bld_schema_voice_pipeline
  - bld_schema_usage_report
  - bld_schema_integration_guide
  - bld_schema_dataset_card
  - bld_schema_reranker_config
  - bld_schema_prompt_optimizer
  - bld_schema_onboarding_flow
updated: "2026-04-22"
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+schema F4=plan F5=scan F6=produce F7=gate F8=save -->

## Definition
A **pipeline_template** is a scenario-indexed agent pipeline recipe that encodes the OpenCode-Hermes 7-scenario software engineering catalog. It defines: which scenario it covers, the ordered stage sequence (roles in execution order), model tier per stage, revision loop policy (max iterations + escalation), and mandatory quality gates (reviewer + tester). Pipeline templates are reusable across codebases; they are instantiated with a team_charter for a specific task.

## Boundary
| Kind | Relation | Difference |
|------|----------|-----------|
| crew_template | Sibling (P12) | crew_template = multi-role TEAM blueprint with topology. pipeline_template = scenario RECIPE with linear stages. |
| workflow | Sibling (P12) | workflow = arbitrary DAG with conditional branches. pipeline_template = predefined linear recipe. |
| workflow_node | Child (P12) | workflow_node = single step. pipeline_template = complete stage sequence. |
| dag | Sibling (P12) | dag = dependency graph without execution. pipeline_template = ordered execution with gates. |

## Schema Summary
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| id | string | yes | ^p12_pt_[a-z][a-z0-9_]+$ |
| kind | string | yes | pipeline_template |
| pillar | string | yes | P12 |
| scenario | enum | yes | 7 canonical values |
| stages | array | yes | ordered, min 2, each with role+model_tier+optional |
| revision_loop | object | yes | max_iterations (1-5) + escalation_target |
| quality_gates | object | yes | mandatory: [reviewer, tester] |
| version | semver | yes | |
| quality | null | yes | Never self-score |

## 7 Canonical Scenarios
| ID | Scenario | Stage Count | Key Additions |
|----|----------|-------------|---------------|
| new_feature | New feature implementation | 8 | architect + planner + documenter |
| new_feature_security | Security-reviewed new feature | 10 | + researcher + security |
| bug_fix_unknown | Bug with unknown root cause | 5 | + debugger |
| bug_fix_known | Bug with known root cause | 4 | minimal sequence |
| refactoring | Code restructuring | 5 | refactorer replaces coder |
| perf_opt | Performance improvement | 5 | optimizer replaces coder |
| infra | Infrastructure/CI changes | 4 | devops replaces coder |

## Model Tier Mapping
| Tier | Roles | LLM Guidance |
|------|-------|-------------|
| xhigh | architect, planner | Highest capability; system-level reasoning |
| high | analyst, coder, refactorer, optimizer, debugger, fixer, devops | Strong reasoning + code generation |
| medium | finder, documenter, reviewer, researcher, security | Standard capability |
| low | tester | Repetitive task; lower cost acceptable |

## Quality Gates (mandatory)
- **reviewer**: Code quality, diff review, style compliance. Routes back to implementation stage on failure.
- **tester**: Regression suite, behavior verification. Routes back to reviewer on pass, escalates on failure loop.
- **Priority order**: security > quality > implementation. Security issues block all other gates.

## Common Usage
```python
# Instantiate canonical bug-fix pipeline
from cex_sdk.pipeline import Pipeline
pl = Pipeline.from_template('p12_pt_bug_fix_unknown.yaml')
result = pl.run(task='Fix null pointer in user auth flow', codebase='src/')
```

## Builder
`archetypes/builders/pipeline-template-builder/`
Sub-agent: `.claude/agents/pipeline-template-builder.md`
Naming: `p12_pt_{{scenario}}.yaml`

## Related KCs
- `kc_crew_template.md` -- team blueprint (complementary kind)
- `kc_workflow.md` -- arbitrary DAG execution
- `kc_workflow_node.md` -- single pipeline step

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_e2e_eval]] | downstream | 0.32 |
| [[bld_schema_quickstart_guide]] | downstream | 0.29 |
| [[bld_schema_bugloop]] | downstream | 0.29 |
| [[bld_schema_voice_pipeline]] | downstream | 0.29 |
| [[bld_schema_usage_report]] | downstream | 0.28 |
| [[bld_schema_integration_guide]] | downstream | 0.28 |
| [[bld_schema_dataset_card]] | downstream | 0.28 |
| [[bld_schema_reranker_config]] | downstream | 0.28 |
| [[bld_schema_prompt_optimizer]] | downstream | 0.28 |
| [[bld_schema_onboarding_flow]] | downstream | 0.28 |
