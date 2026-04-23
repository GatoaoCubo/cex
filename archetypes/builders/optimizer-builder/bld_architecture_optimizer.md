---
kind: architecture
id: bld_architecture_optimizer
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of optimizer — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Optimizer"
version: "1.0.0"
author: n03_builder
tags: [optimizer, builder, examples]
tldr: "Golden and anti-examples for optimizer construction, demonstrating ideal structure and common pitfalls."
domain: "optimizer construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - optimizer-builder
  - bld_collaboration_optimizer
  - bld_memory_optimizer
  - p11_qg_optimizer
  - p03_sp_optimizer_builder
  - p03_ins_optimizer
  - p01_kc_optimizer
  - bld_output_template_optimizer
  - bld_knowledge_card_optimizer
  - bld_architecture_benchmark
---

# Architecture: optimizer in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, target_metric, direction, etc.) | optimizer-builder | active |
| target_metric | The specific metric being optimized with direction (minimize/maximize) | author | active |
| thresholds | Tripartite levels: trigger (start action), target (goal), critical (escalate) | author | active |
| actions | Ordered list of optimization actions with type, description, and automation flag | author | active |
| baseline | Current measured value with conditions and date of measurement | author | active |
| cost_risk_assessment | Cost of optimization versus benefit, with mitigation plan | author | active |
| monitoring_config | Dashboard, alert rules, and reporting frequency | author | active |
## Dependency Graph
```
benchmark       --produces-->  optimizer  --consumed_by-->  scheduler
quality_gate    --depends-->   optimizer  --signals-->      optimization_event
optimizer       --produces-->  action_execution
```
| From | To | Type | Data |
|------|----|------|------|
| benchmark (P07) | optimizer | data_flow | measured baseline and comparison metrics |
| optimizer | scheduler | consumes | scheduler triggers optimization actions on threshold breach |
| optimizer | action_execution | produces | concrete optimization action dispatched for execution |
| quality_gate (P11) | optimizer | dependency | gate scores may indicate optimization need |
| optimizer | optimization_event (P12) | signals | emitted when threshold crossed or action taken |
| monitoring_config | dashboard | data_flow | feeds metrics to observability system |
## Boundary Table
| optimizer IS | optimizer IS NOT |
|--------------|-----------------|
| A continuous metric-to-action cycle with thresholds | A one-time bug fix cycle (bugloop P11) |
| Defines trigger/target/critical threshold tiers | A passive measurement without action (benchmark P07) |
| Produces automated or manual optimization actions | A pass/fail quality barrier (quality_gate P11) |
| Tracks baseline with measurement conditions | A safety restriction on behavior (guardrail P11) |
| Monitors results and adjusts over iterations | A static configuration parameter (runtime_rule P09) |
| Assesses cost/risk tradeoff before acting | An unbounded optimization without constraints |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Measurement | benchmark, baseline | Establish current performance and measurement conditions |
| Definition | frontmatter, target_metric, thresholds | Specify what to optimize and at what levels |
| Action | actions, cost_risk_assessment | Define what to do when thresholds are crossed |
| Execution | scheduler, action_execution | Trigger and carry out optimization actions |
| Observability | monitoring_config, optimization_event | Track results and report progress |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[optimizer-builder]] | downstream | 0.56 |
| [[bld_collaboration_optimizer]] | downstream | 0.52 |
| [[bld_memory_optimizer]] | downstream | 0.51 |
| [[p11_qg_optimizer]] | downstream | 0.51 |
| [[p03_sp_optimizer_builder]] | upstream | 0.48 |
| [[p03_ins_optimizer]] | upstream | 0.46 |
| [[p01_kc_optimizer]] | downstream | 0.37 |
| [[bld_output_template_optimizer]] | upstream | 0.34 |
| [[bld_knowledge_card_optimizer]] | upstream | 0.31 |
| [[bld_architecture_benchmark]] | sibling | 0.30 |
