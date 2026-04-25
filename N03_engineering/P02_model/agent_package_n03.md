---
id: p02_ap_n03
kind: agent_package
8f: F2_become
pillar: P02
title: "Agent Package -- N03 Engineering Nucleus"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: artifact-construction
quality: 9.1
tags: [agent-package, N03, packaging, deployment, configuration, 8F, opus]
tldr: "Complete packaged configuration for the N03 Engineering nucleus. Bundles identity, model config, capability registry, tool list, boot parameters, and runtime constraints into a deployable agent unit."
density_score: 0.90
updated: "2026-04-17"
related:
  - agent_card_n03
  - p02_nd_n03.md
  - agent_card_engineering_nucleus
  - p03_sp_n03_creation_nucleus
  - p02_agent_creation_nucleus
  - spec_infinite_bootstrap_loop
  - p01_kc_cex_project_overview
  - ctx_cex_new_dev_guide
  - self_audit_n03_builder_20260408
  - agent_card_n07
---

# Agent Package: N03 Engineering Nucleus

## Package Identity

| Field | Value |
|-------|-------|
| package_id | n03_engineering_v1 |
| nucleus | n03 |
| name | N03 Engineering |
| sin_lens | inventive_pride |
| domain | artifact-construction, schema-design, quality-enforcement, system-architecture |
| version | 1.0.0 |
| created | 2026-04-17 |

## Model Configuration

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| model | claude-opus-4-6 | High-effort builds require maximum reasoning |
| context_window | 1_000_000 | Full repo context for architectural decisions |
| temperature | default | Deterministic structure; creativity within constraints |
| max_tokens | 8192 | Sufficient for any single artifact (max ~5120B) |
| thinking_budget | 10000 | Extended reasoning for complex build planning (F4 REASON) |
| fallback_model | claude-sonnet-4-6 | On quota exhaustion |

## Boot Parameters

| Parameter | Value |
|-----------|-------|
| boot_script | boot/n03.ps1 |
| task_file | n03_task.md (repo root) OR .cex/runtime/handoffs/n03_task.md |
| interactive | always (task from file, never CLI args) |
| auto_accept | CEX_AUTO_ACCEPT env var |
| session_id | injected by dispatch.sh at spawn |
| working_dir | repo root (C:/Users/CEX/Documents/GitHub/cex) |

## Capability Registry

Primary capabilities (Inventive Pride domain):

| Capability | Kind | Pillar | Frequency |
|-----------|------|--------|-----------|
| Schema design | input_schema, type_def, interface, enum_def, api_reference, validation_schema | P06 | HIGH |
| Quality governance | scoring_rubric, quality_gate, llm_judge, regression_check | P07 | HIGH |
| Artifact construction | all 300 kinds | all | HIGH |
| Architecture documentation | component_map, invariant, pattern, decision_record, diagram | P08 | MEDIUM |
| Build tooling | code_executor, diff_strategy, cli_tool, code_of_conduct | P04 | MEDIUM |
| Feedback loops | bugloop, self_improvement_loop, quality_gate, guardrail | P11 | MEDIUM |
| Knowledge artifacts | knowledge_card, kc_vocabulary, chunk_strategy | P01 | MEDIUM |
| Prompt engineering | system_prompt, prompt_template, chain, reasoning_strategy | P03 | MEDIUM |
| Workflow design | workflow, dag, checkpoint, dispatch_rule | P12 | LOW |

## Tool Manifest

Tools available to N03 during execution:

| Tool | Path | Used At |
|------|------|---------|
| cex_compile.py | _tools/cex_compile.py | F8, bugloop |
| cex_doctor.py | _tools/cex_doctor.py | F7, bugloop |
| cex_score.py | _tools/cex_score.py | F7 |
| cex_retriever.py | _tools/cex_retriever.py | F3, F5 |
| cex_sanitize.py | _tools/cex_sanitize.py | F8 |
| signal_writer.py | _tools/signal_writer.py | F8 |
| cex_8f_runner.py | cex_sdk/cex_8f_runner.py | primary executor |
| cex_8f_motor.py | cex_sdk/cex_8f_motor.py | F1 intent resolution |
| cex_evolve.py | _tools/cex_evolve.py | self-improvement |
| cex_hygiene.py | _tools/cex_hygiene.py | artifact CRUD |

## Runtime Constraints

| Constraint | Value | Enforced By |
|-----------|-------|-------------|
| Quality floor | 7.0 (warn below 9.0) | quality_gate_n03.md |
| Max retries per artifact | 2 | 8F pipeline |
| Max artifacts per session | 30 | session token budget |
| ASCII-only in code | mandatory | cex_sanitize.py + pre-commit |
| No self-scoring | mandatory | quality_gate H04 |
| Compile on save | mandatory | F8 COLLABORATE |
| Signal on complete | mandatory | F8 COLLABORATE |
| Git commit per wave | mandatory | F8 COLLABORATE |

## Sub-Agent Configuration

N03 can spawn sub-agents for parallel builder execution:

```yaml
sub_agents:
  max_parallel: 5
  isolation: worktree  # each sub-agent in own git worktree
  kinds_supporting_isolation:
    - agent
    - workflow
    - system_prompt
    - landing_page
    - crew_template
  timeout_per_agent: 300s
  session_tracking: true
```

## Deployment Checklist

Pre-deployment verification:
- [ ] boot/n03.ps1 exists and is executable
- [ ] n03_task.md readable at repo root
- [ ] .cex/brand/brand_config.yaml loaded (or gracefully absent for dev repo)
- [ ] N03_engineering/rules/n03-8f-enforcement.md readable
- [ ] archetypes/builders/ accessible (259+ directories)
- [ ] .cex/kinds_meta.json readable (300 kinds)
- [ ] cex_compile.py runnable (python 3.8+)
- [ ] signal_writer.py runnable
- [ ] git configured (username + email)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent_card_n03]] | upstream | 0.35 |
| [[p02_nd_n03.md]] | related | 0.30 |
| [[agent_card_engineering_nucleus]] | related | 0.29 |
| [[p03_sp_n03_creation_nucleus]] | downstream | 0.27 |
| [[p02_agent_creation_nucleus]] | related | 0.27 |
| [[spec_infinite_bootstrap_loop]] | related | 0.25 |
| [[p01_kc_cex_project_overview]] | upstream | 0.25 |
| [[ctx_cex_new_dev_guide]] | related | 0.25 |
| [[self_audit_n03_builder_20260408]] | upstream | 0.24 |
| [[agent_card_n07]] | downstream | 0.24 |
