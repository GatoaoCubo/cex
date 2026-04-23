---
kind: quality_gate
id: p03_qg_planning_strategy
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for planning_strategy
quality: 9.0
title: "Quality Gate Planning Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [planning_strategy, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for planning_strategy"
domain: "planning_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_examples_planning_strategy
  - bld_instruction_planning_strategy
  - p03_qg_reasoning_strategy
  - p11_qg_safety_policy
  - p05_qg_quickstart_guide
  - p04_qg_search_strategy
  - p03_qg_prompt_technique
  - p12_qg_visual_workflow
  - p07_qg_benchmark_suite
  - p03_sp_planning_strategy_builder
---

## Quality Gate

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| Agent Planning Approach Defined | Yes | Equals | Strategy Document |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML valid | YAML syntax error |
| H02 | ID matches pattern | ID does not match `P[0-9]{2}-[A-Z]{3}` |
| H03 | kind matches | kind ≠ `planning_strategy` |
| H04 | Planning steps defined | Missing step definitions |
| H05 | Alignment with objectives | No objective linkage |
| H06 | Resource allocation | Missing resource details |
| H07 | Risk mitigation | No risk scenarios addressed |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Clarity | 0.15 | 1.0=clear, 0.0=ambiguous |
| D02 | Completeness | 0.15 | 1.0=all steps, 0.0=missing |
| D03 | Alignment | 0.10 | 1.0=fully aligned, 0.0=unrelated |
| D04 | Feasibility | 0.10 | 1.0=realistic, 0.0=unachievable |
| D05 | Risk Coverage | 0.10 | 1.0=all risks, 0.0=none |
| D06 | Resource Allocation | 0.10 | 1.0=optimal, 0.0=missing |
| D07 | Stakeholder Input | 0.10 | 1.0=fully engaged, 0.0=no input |
| D08 | Innovation | 0.10 | 1.0=creative, 0.0=stagnant |

## Actions
| Score | Action |
|---|---|
| GOLDEN (≥9.5) | No action required |
| PUBLISH (≥8.0) | Automated approval |
| REVIEW (≥7.0) | Manual review required |
| REJECT (<7.0) | Reject and request revisions |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Emergency override | CTO | Documented justification |
| Legacy system compatibility | Architect | Change log entry |
| Regulatory change | Compliance Lead | Signed waiver |

## Examples

## Golden Example
```markdown
---
title: "Urban Mobility Expansion Plan"
kind: planning_strategy
author: Urban Planning Team
date: 2023-11-01
---

**Objective**: Optimize city transportation network for 2030.

**Phases**:
1. **Research**: Analyze traffic patterns, population growth, and existing infrastructure gaps.
2. **Design**: Propose hybrid public transit (electric buses + bike lanes) and AI-driven traffic signaling.
3. **Implementation**: Prioritize high-impact zones using phased funding and community feedback loops.
4. **Evaluation**: Use real-time sensors and quarterly audits to adjust strategies.

**Constraints**: 
- Budget: $500M annual cap
- Timeline: 5-year rollout
- Equity: Ensure accessibility in underserved neighborhoods
```

## Anti-Example 1: Confusing with reasoning_strategy
```markdown
---
title: "Prompt-Based Decision Framework"
kind: planning_strategy
author: AI Team
date: 2023-10-15
---

**Steps**:
1. Use "maximize efficiency" prompt for resource allocation.
2. Apply "ethical dilemma" prompt for conflict resolution.
3. Generate options via "scenario simulation" prompt.

**Constraints**: 
- Must use predefined prompts
- No human oversight allowed
```
## Why it fails: 
Mixes planning with prompt-based reasoning. The artifact defines a *reasoning strategy* (prompt usage), not a *planning approach* (strategic framework for execution).

## Anti-Example 2: Treating as workflow
```markdown
---
title: "Project Execution Steps"
kind: planning_strategy
author: Operations
date: 2023-10-20
---

**Tasks**:
1. Collect data from sensors
2. Upload to cloud storage
3. Run ML model on dataset
4. Generate report
5. Send to stakeholders

**Constraints**: 
- Must use Python for data processing
- Reports due by 5 PM daily
```
## Why it fails: 
Describes an *execution workflow* (sequence of tasks), not a *planning strategy* (strategic framework for deciding what to do). It lacks high-level objectives and adaptive planning elements.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
