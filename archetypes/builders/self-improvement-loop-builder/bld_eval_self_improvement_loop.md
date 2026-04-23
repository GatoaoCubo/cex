---
kind: quality_gate
id: p11_qg_self_improvement_loop
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for self_improvement_loop
quality: 9.0
title: "Quality Gate Self Improvement Loop"
version: "1.1.0"
author: n01_hybrid_review4
tags: [self_improvement_loop, builder, quality_gate]
tldr: "Quality gate for self_improvement_loop artifacts: HARD structural checks + SOFT 5D scoring."
domain: "self_improvement_loop construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.86
related:
  - bld_examples_self_improvement_loop
  - p01_qg_agentic_rag
  - p07_qg_trajectory_eval
  - bld_output_template_self_improvement_loop
  - p07_qg_eval_metric
  - p03_sp_self_improvement_loop_builder
  - p05_qg_github_issue_template
  - p11_qg_response_format
  - p08_qg_dual_loop_architecture
  - p11_qg_system_prompt
---

## Quality Gate

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| required_fields_present | 100% | == | frontmatter |
| id_pattern_match | true | == | artifact id |
| loop_stages_count | >=2 | >= | body |
| metrics_section_present | true | == | body |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Syntax errors or missing required fields |
| H02 | ID matches ^p11_sil_[a-z][a-z0-9_]+$ | ID does not match pattern |
| H03 | kind field equals 'self_improvement_loop' | kind is absent or mismatched |
| H04 | loop_stages field present with >= 2 entries | loop_stages missing or has fewer than 2 stages |
| H05 | metrics field present with at least 1 metric | metrics section absent or empty |
| H06 | feedback_sources referenced | No feedback mechanism described |
| H07 | Safety guard or rollback mechanism described | No divergence prevention documented |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D1 | Loop completeness | 0.25 | 1.0 = assess->plan->execute->review stages all present |
| D2 | Metric specificity | 0.20 | 1.0 = metrics are quantifiable and time-bound |
| D3 | Safety guards | 0.20 | 1.0 = rollback + divergence prevention documented |
| D4 | Feedback diversity | 0.20 | 1.0 = >=2 distinct feedback sources |
| D5 | Alignment traceability | 0.15 | 1.0 = loop goals traceable to agent objectives |

## Actions
| Score | Action |
|---|---|
| >=9.5 | GOLDEN |
| >=8.0 | PUBLISH |
| >=7.0 | REVIEW |
| <7.0 | REJECT |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Experimental loop under active research | Research lead | Issue tracker link |
| Legacy system compatibility constraint | Architect | Change control board entry |

## Examples

## Golden Example
```yaml
title: Autonomous Reinforcement Learning System
kind: self_improvement_loop
tools: 
  - TensorFlow
  - Ray
  - Prometheus
body: 
  - Agent deploys a reinforcement learning model in a simulated trading environment.
  - Model generates trades based on real-time market data.
  - Performance metrics (profit, risk ratio) are logged to Prometheus.
  - Every 24 hours, Ray orchestrates a hyperparameter tuning job using Bayesian optimization.
  - New model versions are tested in a staging environment.
  - Top-performing models replace the current version in production.
  - Loop repeats with updated reward functions derived from latest market trends.
```

## Anti-Example 1: No Feedback Mechanism
```yaml
title: Static Model Re-deployment
kind: self_improvement_loop
tools: 
  - TensorFlow
body: 
  - Model trains on historical data once.
  - Every month, same model is re-deployed without new data or evaluation.
  - No metrics collected, no performance comparison.
```
## Why it fails
Lacks any mechanism to compare new vs old performance. No learning occurs—just repeated deployment of the same model.

## Anti-Example 2: Bug-Specific Loop
```yaml
title: Crash Recovery Loop
kind: self_improvement_loop
tools: 
  - Kubernetes
body: 
  - System monitors for container crashes.
  - On crash, restarts container with same configuration.
  - Logs are stored but never analyzed for root causes.
```
## Why it fails
Focuses on immediate recovery rather than systemic improvement. The loop addresses symptoms (crashes) but not underlying issues in the system design or code.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
