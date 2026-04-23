---
kind: quality_gate
id: p04_qg_search_strategy
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for search_strategy
quality: 9.0
title: "Quality Gate Search Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [search_strategy, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for search_strategy"
domain: "search_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_examples_search_strategy
  - bld_architecture_search_strategy
  - p10_lr_search_strategy_builder
  - bld_output_template_search_strategy
  - search-strategy-builder
  - p03_sp_search_strategy_builder
  - p01_qg_reranker_config
  - p03_qg_planning_strategy
  - bld_knowledge_card_search_strategy
  - kc_search_strategy
---

## Quality Gate

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| Compute Allocation Efficiency | 90% | ≥ | All inference nodes |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML valid | Invalid YAML syntax |
| H02 | ID matches pattern | ID does not match `^p04_ss_[a-zA-Z0-9_-]+$` |
| H03 | kind matches | kind ≠ `search_strategy` |
| H04 | Resource limits defined | Missing CPU/RAM limits |
| H05 | Strategy validity | Strategy not in `static`, `dynamic`, or `adaptive` |
| H06 | Versioning present | No version field in metadata |
| H07 | Documentation included | Missing user-facing documentation |
| H08 | Performance threshold | Latency > 500ms under load |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Strategy clarity | 0.15 | Clear objective and constraints |
| D02 | Resource optimization | 0.12 | Efficient use of compute resources |
| D03 | Scalability | 0.10 | Handles 10x load increase |
| D04 | Error handling | 0.08 | Graceful fallback on failure |
| D05 | Documentation | 0.15 | Complete and actionable |
| D06 | Versioning | 0.08 | Semantic versioning compliant |
| D07 | Performance | 0.12 | Meets SLA under stress |
| D08 | Compliance | 0.10 | Adheres to security/privacy policies |
| D09 | Innovation | 0.08 | Novel approach to allocation |
| D10 | Maintainability | 0.02 | Easy to update/monitor |

## Actions
| Score | Action |
|---|---|
| ≥9.5 | Automatically approve and deploy |
| ≥8.0 | Schedule for review by domain experts |
| ≥7.0 | Request changes and resubmit |
| <7.0 | Reject and require redesign |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Critical production issue | CTO | Bypass logged with justification |

## Examples

## Golden Example
```markdown
---
title: "Dynamic Resource Allocation for Query Complexity"
author: "AI Systems Team"
date: "2023-10-01"
keywords: search_strategy, compute_allocation, inference_optimization
---

**Strategy**: Allocate compute resources based on query complexity during inference.  
**Implementation**:  
1. Preprocess queries to estimate complexity (e.g., length, entity count).  
2. Use a tiered compute budget:  
   - Low complexity: 1 GPU core, 2 threads.  
   - Medium: 2 GPU cores, 4 threads.  
   - High: 4 GPU cores, 8 threads.  
3. Monitor latency and adjust budgets dynamically using feedback loops.  
**Parameters**: `max_threads`, `gpu_cores_per_tier`, `latency_threshold`.  
**Benefits**: Balances speed and accuracy, adapts to workload variations.
```

## Anti-Example 1: Confusing with Reasoning Strategy
```markdown
---
title: "Prompt-Based Compute Allocation"
author: "Novice Developer"
date: "2023-09-15"
keywords: reasoning_strategy, prompt_tuning
---

**Strategy**: Use prompts like "Use more compute" to influence model behavior.  
**Implementation**:  
- Insert instruction: "Allocate maximum resources for this query."  
**Parameters**: None.  
**Benefits**: "Simplifies" resource management through natural language.
```
## Why it fails: This is a reasoning_strategy (prompt technique), not a search_strategy. It relies on model interpretation of text, not explicit compute allocation logic.

## Anti-Example 2: Vague Allocation Rules
```markdown
---
title: "Generic Compute Strategy"
author: "Unspecified"
date: "2023-08-20"
keywords: search_strategy
---

**Strategy**: "Use more resources when needed."  
**Implementation**:  
- "Sometimes increase GPU usage."  
**Parameters**: None.  
**Benefits**: "Flexible" approach.
```
## Why it fails: No actionable rules or metrics for determining "need." Lacks parameters, tiers, or feedback mechanisms, making it unimplementable.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
