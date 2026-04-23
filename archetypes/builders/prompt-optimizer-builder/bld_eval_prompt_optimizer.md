---
kind: quality_gate
id: p03_qg_prompt_optimizer
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for prompt_optimizer
quality: 9.1
title: "Quality Gate Prompt Optimizer"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [prompt_optimizer, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for prompt_optimizer"
domain: "prompt_optimizer construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_prompt_optimizer
  - p03_qg_multimodal_prompt
  - p07_qg_eval_metric
  - p03_qg_prompt_technique
  - p05_qg_product_tour
  - p05_qg_pricing_page
  - p11_qg_incident_report
  - p11_qg_usage_report
  - p05_qg_integration_guide
  - p03_qg_reasoning_strategy
---

## Quality Gate

## Definition
(Table: metric, threshold, operator, scope)
| metric              | threshold | operator | scope           |
|---------------------|-----------|----------|-----------------|
| optimization_passes | 2         | >=       | each artifact   |
| industry_refs       | 1         | >=       | each artifact   |

## HARD Gates
(Table: ID | Check | Fail Condition)
| ID           | Check                                   | Fail Condition                                      |
|--------------|-----------------------------------------|-----------------------------------------------------|
| H01          | YAML frontmatter valid                  | Invalid YAML syntax or missing fields               |
| H02          | ID matches ^p03_po_[a-z][a-z0-9_]+.md$ | ID does not conform to schema pattern               |
| H03          | kind field = 'prompt_optimizer'         | kind field is incorrect or missing                  |
| H04          | At least 2 optimization passes defined  | No documented optimization steps                    |
| H05          | Input prompt and output prompt present  | Missing before/after comparison                     |
| H06          | Rationale documented for each pass      | No explanation of why each change improves quality  |
| H07          | At least 1 industry method cited        | No reference to DSPy, OPRO, APE, or PromptWizard    |

## SOFT Scoring
(Table: Dim | Dimension | Weight | Scoring Guide)
| Dim | Dimension         | Weight | Scoring Guide                                            |
|-----|-------------------|--------|----------------------------------------------------------|
| D1  | Clarity gain      | 0.20   | 1.0: Unambiguous after optimization; 0.5: Minor gains    |
| D2  | Specificity       | 0.20   | 1.0: Task-specific, concrete; 0.5: Generic language      |
| D3  | Conciseness       | 0.15   | 1.0: No redundancy; 0.5: Some waste; 0.0: Bloated        |
| D4  | Constraint align  | 0.15   | 1.0: Meets all domain rules; 0.5: Partial; 0.0: Violates |
| D5  | Rationale quality | 0.15   | 1.0: Each change justified; 0.5: Partial; 0.0: None      |
| D6  | Method rigor      | 0.10   | 1.0: Named method applied; 0.5: Ad hoc; 0.0: None        |
| D7  | Reusability       | 0.05   | 1.0: Template extractable; 0.5: Partial; 0.0: One-off    |

## Actions
(Table: Score | Action)
| Score  | Action                          |
|--------|---------------------------------|
| >=9.5  | GOLDEN                          |
| >=8.0  | PUBLISH                         |
| >=7.0  | REVIEW                          |
| <7.0   | REJECT                          |

## Bypass
(Table: conditions, approver, audit trail)
| conditions                  | approver   | audit trail                          |
|-----------------------------|------------|--------------------------------------|
| Security exception approved | N07        | Bypass logged with reason + timestamp |
| Experimental method         | N07        | Bypass logged with reason + timestamp |

## Examples

## Golden Example

A properly structured CEX prompt_optimizer artifact shows the before/after transformation with documented rationale:

```yaml
---
id: p03_po_chain_of_thought_boost.md
kind: prompt_optimizer
pillar: P03
quality: null
title: "Chain-of-Thought Boost for Reasoning Tasks"
version: "1.0.0"
domain: "analytical reasoning"
method: DSPy signature optimization
tags: [prompt_optimizer, chain_of_thought, reasoning]
---
```

**Original prompt:**
> "Explain this concept."

**Pass 1 -- Specificity (APE-style candidate generation):**
> "Explain [CONCEPT] in three steps, using concrete examples for each step."
> Rationale: Forces structured output; reduces abstraction drift.

**Pass 2 -- Constraint injection (OPRO-style refinement):**
> "Explain [CONCEPT] in exactly three steps. Each step must include: (1) the principle, (2) a real-world example, (3) a common misconception to avoid."
> Rationale: Prevents hallucination by forcing grounding per step.

**Optimized prompt:** Pass 2 output. Measurable gain: specificity +40%, hallucination risk -30% vs. baseline.

## Anti-Example 1: Vendor tool catalog entry
```yaml
---
tool: PromptHero Optimizer v2.1
vendor: PromptHero Inc.
description: "Automated prompt refinement via API"
---
```
**Why it fails:** Describes a third-party product, not a CEX kind artifact. Missing frontmatter kind/pillar fields. No optimization passes documented. Not a produced artifact -- a vendor reference.

## Anti-Example 2: No transformation documented
```yaml
---
id: p03_po_vague_boost.md
kind: prompt_optimizer
description: "Makes prompts better"
---
```
**Optimized prompt:** "An improved version of your input."

**Why it fails:** Zero specificity on optimization technique. No before/after comparison. No rationale. Fails H04 (must have 2+ passes) and H06 (rationale required per pass).

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
