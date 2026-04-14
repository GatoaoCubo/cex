---
kind: architecture
id: bld_architecture_dispatch_rule
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of dispatch_rule — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Dispatch Rule"
version: "1.0.0"
author: n03_builder
tags: [dispatch_rule, builder, examples]
tldr: "Golden and anti-examples for dispatch rule construction, demonstrating ideal structure and common pitfalls."
domain: "dispatch rule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| scope | Domain identifier this rule covers: string key (e.g. `research`, `build`) | dispatch-rule-builder | required |
| keywords | List of trigger terms (PT and EN) that activate this rule | dispatch-rule-builder | required |
| target_agent_group | Which execution target receives matched tasks | dispatch-rule-builder | required |
| model | LLM model assigned to the target agent_group | dispatch-rule-builder | required |
| priority | Integer rank for conflict resolution when multiple rules match | dispatch-rule-builder | required |
| confidence_threshold | Minimum match confidence to fire this rule (0.0–1.0) | dispatch-rule-builder | required |
| fallback_agent_group | Backup target when primary agent_group is unavailable | dispatch-rule-builder | required |
| conditions | Optional AND-gated conditions beyond keyword match | dispatch-rule-builder | optional |
| routing_strategy | Match algorithm: keyword_match, semantic, regex | dispatch-rule-builder | optional |
| metadata | Rule id, version, author, pillar, created date | dispatch-rule-builder | required |
## Dependency Graph
```
task_input --triggers--> dispatch_rule (keywords in input matched against rule)
dispatch_rule --selects--> target_agent_group (routes task to correct executor)
dispatch_rule --precedes--> handoff (P12) (rule selects who; handoff instructs what)
dispatch_rule --precedes--> spawn_config (P12) (rule selects; config defines launch params)
signal (P12) --informs--> dispatch_rule (completion signals may update priority weights)
orchestrator --consumes--> dispatch_rule (orchestrator, spawn_grid read rules at routing time)
router (P02) --independent-- dispatch_rule (P02 router does multi-step model routing, DR does agent_group routing)
workflow (P12) --independent-- dispatch_rule (workflow sequences steps, DR routes incoming tasks)
```
| From | To | Type | Data |
|------|----|------|------|
| task_input | dispatch_rule | data_flow | raw task text matched against keywords/conditions |
| dispatch_rule | target_agent_group | data_flow | routing decision: which agent_group + model |
| dispatch_rule | handoff | produces | selected agent_group receives handoff instructions |
| dispatch_rule | spawn_config | produces | launch parameters for selected agent_group |
| signal | dispatch_rule | signals | completion feedback may influence priority |
| orchestrator | dispatch_rule | consumes | reads rules to route incoming work |
## Boundary Table
| dispatch_rule IS | dispatch_rule IS NOT |
|-----------------|----------------------|
| A routing policy: maps task keywords to execution targets | A handoff — handoff provides full task context and instructions |
| Decides WHO receives a task before execution begins | A signal — signal reports what just happened at runtime |
| A static, versioned, machine-readable policy record | A workflow — workflow sequences steps with dependencies |
| Includes priority for conflict resolution between rules | A dag — dag models dependency structure between tasks |
| Includes fallback for agent_group unavailability | A spawn_config — spawn_config configures how processes are launched |
| Supports confidence_threshold for ambiguous matches | A crew — crew defines multi-agent coordination protocols |
| Covers one domain scope per file | A router (P02) — P02 router does complex task-to-model routing with context |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Match | keywords, conditions, routing_strategy | Define what triggers this rule to activate |
| Decision | scope, target_agent_group, model, priority | Specify who receives the task and with what model |
| Resilience | confidence_threshold, fallback_agent_group | Handle low-confidence matches and unavailable targets |
