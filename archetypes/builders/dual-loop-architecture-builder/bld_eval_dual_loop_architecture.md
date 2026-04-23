---
kind: quality_gate
id: p08_qg_dual_loop_architecture
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for dual_loop_architecture
quality: 9.0
title: "Quality Gate Dual Loop Architecture"
version: "1.0.0"
author: wave1_builder_gen
tags: [dual_loop_architecture, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for dual_loop_architecture"
domain: "dual_loop_architecture construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_examples_dual_loop_architecture
  - bld_knowledge_card_dual_loop_architecture
  - bld_collaboration_dual_loop_architecture
  - p03_sp_dual_loop_architecture_builder
  - dual-loop-architecture-builder
  - bld_instruction_dual_loop_architecture
  - kc_dual_loop_architecture
  - p10_lr_dual_loop_architecture_builder
  - bld_tools_dual_loop_architecture
  - bld_architecture_dual_loop_architecture
---

## Quality Gate

## Definition

This ISO applies to the dual loop pattern, coordinating an outer orchestrator with one or more inner worker loops.
| Metric | Threshold | Operator | Scope |
|---|---|---|---|
| Dual-loop architecture compliance | 100% | Equals | System-wide |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML valid | Invalid YAML syntax |
| H02 | ID matches pattern | ID does not match `P08-XX-XXX` |
| H03 | Kind matches | Kind does not equal `dual_loop_architecture` |
| H04 | Outer/inner loop separation | No clear separation of concerns |
| H05 | Communication protocol | Missing secure inter-loop messaging |
| H06 | Error handling | No fallback in outer loop on inner failure |
| H07 | Scalability | Inner loop cannot scale independently |
| H08 | Security isolation | Shared resources between loops |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Architecture clarity | 0.15 | 1.0 = fully documented |
| D02 | Loop separation | 0.20 | 1.0 = strict isolation |
| D03 | Communication efficiency | 0.15 | 1.0 = low latency, high reliability |
| D04 | Error resilience | 0.15 | 1.0 = full redundancy |
| D05 | Scalability | 0.10 | 1.0 = linear scaling |
| D06 | Security | 0.10 | 1.0 = zero cross-loop vulnerabilities |
| D07 | Documentation | 0.10 | 1.0 = complete API/flow diagrams |
| D08 | Maintainability | 0.15 | 1.0 = modular, testable components |

## Actions
| Score | Action |
|---|---|
| >=9.5 | GOLDEN: Auto-approve, deploy to production |
| >=8.0 | PUBLISH: Deploy to staging, notify team |
| >=7.0 | REVIEW: Manual review required |
| <7.0 | REJECT: Block deployment, fix required |

## Bypass
| Conditions | Approver | Audit Trail |
|---|---|---|
| Legacy system migration | CTO | Change request + risk assessment |
| Urgent security fix | Security lead | Emergency ticket + post-mortem |
| Experimental feature | Lead architect | Prototype approval + test logs |

## Examples

## Golden Example

This ISO applies to the dual loop pattern, coordinating an outer orchestrator with one or more inner worker loops.
```yaml
title: Autonomous Vehicle Control System
kind: dual_loop_architecture
description: >-
  Outer loop handles route planning; inner loop manages real-time steering/throttle.
  Feedback ensures alignment between high-level goals and low-level execution.
outer_loop:
  - name: Path Planner
    inputs: [destination, map, traffic data]
    outputs: [desired trajectory]
inner_loop:
  - name: Vehicle Controller
    inputs: [trajectory, sensor data]
    outputs: [steering, throttle, brake]
feedback:
  - from: Vehicle Controller
    to: Path Planner
    metric: deviation from trajectory
```

## Anti-Example 1: Linear Workflow Misinterpretation
```yaml
title: Misinterpreted Workflow
kind: dual_loop_architecture
description: >-
  "Outer loop" processes data sequentially, then passes to "inner loop" for final output.
outer_loop:
  - name: Data Processor
    inputs: [raw data]
    outputs: [processed data]
inner_loop:
  - name: Finalizer
    inputs: [processed data]
    outputs: [result]
```
## Why it fails
Lacks bidirectional feedback and real-time adjustment. Treats loops as sequential stages, violating dual-loop control's core principle of continuous interaction between high-level planning and low-level execution.

## Anti-Example 2: Merged Loop Architecture
```yaml
title: Monolithic Controller
kind: dual_loop_architecture
description: >-
  Single agent handles both planning and execution without clear separation.
agent:
  - name: Unified Controller
    inputs: [goals, sensor data]
    outputs: [actions]
```
## Why it fails
Blurs separation between strategic planning (outer loop) and tactical execution (inner loop). Loses modularity and fails to enable independent optimization of each control layer, making system adaptation and debugging difficult.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
