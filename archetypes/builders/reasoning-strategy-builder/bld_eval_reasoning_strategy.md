---
kind: quality_gate
id: p03_qg_reasoning_strategy
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for reasoning_strategy
quality: 9.0
title: "Quality Gate Reasoning Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [reasoning_strategy, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for reasoning_strategy"
domain: "reasoning_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_examples_reasoning_strategy
  - bld_instruction_reasoning_strategy
  - kc_reasoning_strategy
  - bld_output_template_reasoning_strategy
  - p03_sp_reasoning_strategy_builder
  - bld_knowledge_card_reasoning_strategy
  - reasoning-strategy-builder
  - bld_architecture_reasoning_strategy
  - p05_qg_quickstart_guide
  - bld_instruction_chain
---

## Quality Gate

## Definition

This ISO selects a reasoning strategy (e.g. chain-of-thought) and the conditions under which it applies.
| metric | threshold | operator | scope |
|---|---|---|---|
| Structured Reasoning Completeness | 90% | ≥ | All reasoning steps |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML valid | Invalid YAML syntax |
| H02 | ID matches pattern | ID does not match `^p03_rs_[a-zA-Z0-9]+$` |
| H03 | kind matches | `reasoning_strategy` not specified |
| H04 | Required fields present | Missing `prompt_template` or `validation_rules` |
| H05 | Valid reasoning steps | Steps not aligned with P03 pillar |
| H06 | Consistency | Contradictory logic in reasoning chain |
| H07 | Language | Non-English content detected |
| H08 | Example validity | Example outputs fail validation |
| H09 | Output format | Non-structured output format |
| H10 | Performance | >5s latency in reasoning simulation |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Clarity | 0.15 | 1.0=unambiguous, 0.0=obscure |
| D02 | Coherence | 0.15 | 1.0=logical flow, 0.0=incoherent |
| D03 | Completeness | 0.15 | 1.0=all steps covered, 0.0=missing |
| D04 | Logical Flow | 0.12 | 1.0=valid inference, 0.0=invalid |
| D05 | Example Relevance | 0.10 | 1.0=aligned use case, 0.0=irrelevant |
| D06 | Output Format | 0.10 | 1.0=strictly structured, 0.0=unstructured |
| D07 | Performance | 0.10 | 1.0=≤2s latency, 0.0=>5s |
| D08 | Language | 0.08 | 1.0=English, 0.0=non-English |

## Actions
| Score | Action |
|---|---|
| ≥9.5 | GOLDEN: Deploy immediately |
| ≥8.0 | PUBLISH: Release to production |
| ≥7.0 | REVIEW: Peer review required |
| <7.0 | REJECT: Requires major revisions |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Urgent production need | CTO | Requires written justification and audit log |

## Examples

## Golden Example

This ISO selects a reasoning strategy (e.g. chain-of-thought) and the conditions under which it applies.
```markdown
---
name: "Structured Deduction Chain"
description: "Breaks down complex problems into logical steps with explicit validation"
type: reasoning_strategy
boundary: reasoning_technique
example: "For mathematical proofs, use 'Assume X → Derive Y → Validate Z'"
---

**Phases:**
1. **Premise Mapping** - List all given facts and constraints
2. **Hypothesis Generation** - Propose 3+ possible conclusions
3. **Logical Validation** - Test each hypothesis against premises
4. **Contradiction Check** - Identify and resolve inconsistencies
5. **Conclusion Synthesis** - Select best-supported outcome

**Validation Criteria:**
- Each step must reference prior premises
- All assumptions must be explicitly stated
- Contradictions must be resolved before finalizing
```

## Anti-Example 1: Vague Instructions
```markdown
---
name: "Just Think Harder"
description: "Encourages deep thinking without structure"
type: reasoning_strategy
---

**Steps:**
1. Think about the problem
2. Consider different angles
3. Come to a conclusion
```
## Why it fails
Lacks specific methodology, validation criteria, and actionable steps. The open-ended nature makes it impossible to evaluate reasoning quality or ensure consistency.

## Anti-Example 2: Prompt Technique Confusion
```markdown
---
name: "Roleplay Reasoning"
description: "Asks AI to act as a specific expert"
type: reasoning_strategy
---

**Instructions:**
"Imagine you're a quantum physicist. Explain this concept."
```
## Why it fails
Confuses reasoning strategy with prompt technique. Focuses on roleplaying rather than structuring the reasoning process itself. Doesn't provide methodology for validating conclusions or tracking logical flow.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
