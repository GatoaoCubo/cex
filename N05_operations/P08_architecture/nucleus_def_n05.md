---
id: p02_nd_n05.md
kind: nucleus_def
8f: F2_become
pillar: P02
nucleus_id: N05
role: operations
sin_lens: "Gating Wrath"
cli_binding: claude
model_tier: sonnet
model_specific: claude-sonnet-4-6
context_tokens: 200000
boot_script: boot/n05.ps1
agent_card_path: N05_operations/agent_card_n05.md
pillars_owned:
  - P04
  - P07
  - P09
  - P11
crew_templates_exposed:
  - incident_response
  - release_gate
  - perf_audit
domain_agents:
  - agent_tester
  - agent_deployer
  - agent_reviewer
fallback_cli: codex
title: "Nucleus Def N05"
version: "1.0.0"
author: n07_crewwiring
domain: "ops, testing, CI/CD, quality gates, tools"
quality: 8.9
tags: [nucleus_def, n05, operations, composable]
tldr: "N05 is the operations nucleus: tests, deploys, CI/CD, quality gates, tools. Owns nucleus_def authoring."
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.88
related:
  - kc_nucleus_def
  - p02_nd_n03.md
  - p02_nd_n02.md
  - p02_nd_n01.md
  - p02_nd_n06.md
  - bld_examples_nucleus_def
  - p02_nd_n04.md
  - p02_nd_n07.md
  - self_audit_n05_codex_2026_04_15
  - bld_knowledge_card_nucleus_def
---

## Identity

| Field | Value |
|-------|-------|
| Nucleus ID | N05 |
| Role | operations |
| Sin Lens | Gating Wrath |
| CLI Binding | claude |
| Model Tier | sonnet |
| Model | claude-sonnet-4-6 |
| Context | 200K tokens |
| Boot Script | `boot/n05.ps1` |
| Agent Card | `N05_operations/agent_card_n05.md` |

## Pillars Owned

| Pillar | Domain | Sample Kinds |
|--------|--------|--------------|
| P04 | tools | mcp_server, api_client, webhook, cli_tool |
| P07 | evaluation | scoring_rubric, benchmark, smoke_eval, llm_judge |
| P09 | config | env_config, secret_config, rate_limit_config |
| P11 | feedback | quality_gate, bugloop, regression_check |

## Crew Templates Exposed

| Template | Role in Crew | Inputs | Outputs |
|----------|--------------|--------|---------|
| incident_response | oncall | alert | postmortem + fix PR |
| release_gate | qa_reviewer | release candidate | pass/fail verdict |
| perf_audit | perf_engineer | benchmark target | perf report |

## Domain Agents

| Agent | Purpose | Path |
|-------|---------|------|
| agent_tester | Test generation + execution | `N05_operations/P02_model/` |
| agent_deployer | Deploy automation | `N05_operations/P02_model/` |
| agent_reviewer | Code review | `N05_operations/P02_model/` |

## Boot Contract

- Boot file: `boot/n05.ps1`
- Task source: `.cex/runtime/handoffs/n05_task.md`
- Signal: `write_signal('n05', 'complete', {score})`

## Composability

| Direction | Nucleus | What Flows |
|-----------|---------|-----------|
| outbound | all | quality gates + CI results |
| outbound | N07 | health reports |
| inbound | N03 | code to test |
| inbound | N02 | landing pages to deploy |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_nucleus_def]] | upstream | 0.47 |
| [[p02_nd_n03.md]] | sibling | 0.45 |
| [[p02_nd_n02.md]] | sibling | 0.44 |
| [[p02_nd_n01.md]] | sibling | 0.44 |
| [[p02_nd_n06.md]] | sibling | 0.39 |
| [[bld_examples_nucleus_def]] | downstream | 0.39 |
| [[p02_nd_n04.md]] | sibling | 0.38 |
| [[p02_nd_n07.md]] | sibling | 0.35 |
| [[self_audit_n05_codex_2026_04_15]] | downstream | 0.34 |
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.34 |
