---
# TEMPLATE: Pipeline Template
# Fill all {{VARIABLES}} before use
# Validate against P12_orchestration/_schema.yaml (kinds.pipeline_template)
# Max 4096 bytes | density_min: 0.85 | quality_min: 8.0

id: p12_pt_{{SCENARIO_SLUG}}
kind: pipeline_template
pillar: P12
title: "Pipeline: {{SCENARIO_HUMAN}}"
scenario: {{SCENARIO}}  # new_feature|new_feature_security|bug_fix_unknown|bug_fix_known|refactoring|perf_opt|infra
stages:
  - role: finder
    model_tier: medium
    optional: false
  # Add stages from canonical sequence for chosen scenario
  # Roles: finder|analyst|architect|planner|coder|refactorer|optimizer|debugger|fixer|devops|documenter|reviewer|tester|researcher|security
  # model_tier: low|medium|high|xhigh
  - role: reviewer
    model_tier: medium
    optional: false
  - role: tester
    model_tier: low
    optional: false
revision_loop:
  max_iterations: 3       # 1-5, default 3
  escalation_target: user # user|nucleus|n07
quality_gates:
  mandatory: [reviewer, tester]
  priority_order: [quality, implementation]  # security>quality>implementation when security stage present
version: 1.0.0
quality: null
tags: [hermes_origin, pipeline, scenario_indexed, {{SCENARIO}}]
upstream_source: "1ilkhamov/opencode-hermes-multiagent"
tldr: "Scenario-indexed agent pipeline recipe with stages, revision loop, and quality gates"
domain: orchestration
density_score: 1.0
updated: "2026-04-22"
---

## Purpose

A pipeline_template is a scenario-indexed agent pipeline recipe for software engineering tasks.
It encodes the OpenCode-Hermes 7-scenario catalog: for each canonical scenario (new_feature,
bug_fix, refactoring, etc.) the template defines the ordered stage sequence, model tier per
stage, revision loop policy, and mandatory quality gates (reviewer + tester). Pipeline templates
are instantiated with a `team_charter` for a specific codebase task, enabling N07 to dispatch
the correct stage sequence without rebuilding the pipeline from scratch each time.

## Scenario

{{SCENARIO_DESCRIPTION}}

## Stage Sequence

| Order | Role | Model Tier | Optional | Notes |
|-------|------|-----------|----------|-------|
| 1 | finder | medium | No | Locate relevant files/functions |
| {{N}} | reviewer | medium | No | Code quality gate |
| {{N+1}} | tester | low | No | Regression gate |

### Canonical Role Definitions

| Role | Responsibility | Typical model_tier | Used in scenarios |
|------|---------------|-------------------|-------------------|
| `finder` | Locate relevant files, functions, modules | medium | All 7 |
| `analyst` | Analyze code structure, dependencies, impact | medium | new_feature, refactoring, perf_opt |
| `architect` | Design solution architecture, component layout | high | new_feature, new_feature_security |
| `planner` | Break solution into implementation steps | medium | new_feature, new_feature_security |
| `coder` | Write new code, implement features | high | new_feature, new_feature_security |
| `refactorer` | Restructure existing code without changing behavior | high | refactoring |
| `optimizer` | Improve performance of existing code | high | perf_opt |
| `debugger` | Diagnose root cause of unknown bugs | medium | bug_fix_unknown |
| `fixer` | Apply targeted fix to known bug | medium | bug_fix_unknown, bug_fix_known |
| `devops` | Infrastructure, CI/CD, deployment config | medium | infra |
| `documenter` | Write/update documentation for changes | low | new_feature, new_feature_security |
| `reviewer` | Code quality review, style, correctness | medium | All 7 (mandatory) |
| `tester` | Regression testing, test authoring | low | All 7 (mandatory) |
| `researcher` | Security research, vulnerability analysis | high | new_feature_security |
| `security` | Security audit, threat modeling | xhigh | new_feature_security |

### Model Tier Reference

| Tier | Cost | Capability | When to use |
|------|------|-----------|-------------|
| `low` | Lowest | Basic tasks, templated work | tester, documenter |
| `medium` | Moderate | Analysis, search, standard coding | finder, analyst, planner, reviewer |
| `high` | High | Complex reasoning, architecture, implementation | architect, coder, refactorer, optimizer |
| `xhigh` | Highest | Security-critical, multi-step reasoning | security audits, threat modeling |

## Revision Loop

Max iterations: 3. Triggered when quality gate fails (reviewer or tester returns FAIL).
Escalates to {{ESCALATION_TARGET}} after max_iterations exceeded.

### Revision Loop Configuration

| Parameter | Type | Range | Default | Description |
|-----------|------|-------|---------|-------------|
| `max_iterations` | integer | 1-5 | 3 | Maximum revision attempts before escalation |
| `escalation_target` | enum | user/nucleus/n07 | user | Who receives unresolved failures |

```
Revision loop flow:
  1. Stage produces output
  2. Quality gate (reviewer/tester) evaluates
  3. IF PASS -> proceed to next stage
  4. IF FAIL -> route back to previous implementation stage
  5. Repeat until PASS or max_iterations exhausted
  6. IF exhausted -> escalate to {{ESCALATION_TARGET}}
```

## Quality Gates

Mandatory: reviewer (code quality check) + tester (regression check).
Priority: {{PRIORITY_ORDER}}.
Gate failure routes back to previous implementation stage (max 3 loops).

### Gate Priority Orders

| Priority order | When | Rationale |
|---------------|------|-----------|
| `[security, quality, implementation]` | Security stage present | Security blocks everything |
| `[quality, implementation]` | Standard pipeline | Quality before feature completeness |
| `[implementation, quality]` | Prototype/spike | Ship fast, refine later |

## Hook Integration

Pipeline templates support pre/post hooks at each stage for cross-cutting concerns:

| Hook point | Fires when | Use case |
|------------|-----------|----------|
| `pre_stage` | Before any stage begins | Load context, validate preconditions |
| `post_stage` | After any stage completes | Log metrics, checkpoint state |
| `on_revision` | Quality gate triggers retry | Adjust parameters, load feedback |
| `on_escalation` | Max iterations exceeded | Notify orchestrator, write signal |
| `on_complete` | Final stage passes all gates | Compile artifacts, send signal |

```yaml
hooks:
  pre_stage:
    - action: load_context
      args: {scope: {{SCENARIO}}}
  post_stage:
    - action: checkpoint
      args: {persist: true}
  on_complete:
    - action: signal
      args: {nucleus: n07, status: complete}
```

## Instantiation

```python
from cex_sdk.pipeline import Pipeline
pl = Pipeline.from_template('p12_pt_{{SCENARIO_SLUG}}.yaml')
result = pl.run(task='{{TASK_DESCRIPTION}}', codebase='{{REPO_PATH}}')
```

## Relationship to Other Kinds

| Kind | Pillar | Relationship |
|------|--------|-------------|
| `crew_template` | P12 | Fixed multi-role team blueprint; pipeline_template is scenario-indexed |
| `team_charter` | P12 | Mission contract that instantiates this template for a specific task |
| `workflow` | P12 | Arbitrary DAG; pipeline_template is a predefined linear recipe |
| `revision_loop_policy` | P11 | Revision loop config can be externalized to this kind |
| `quality_gate` | P11 | Gates referenced by this template are defined as quality_gate artifacts |
