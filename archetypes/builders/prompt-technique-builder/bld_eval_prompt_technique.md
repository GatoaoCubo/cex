---
kind: quality_gate
id: p03_qg_prompt_technique
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for prompt_technique
quality: 9.1
title: "Quality Gate Prompt Technique"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [prompt_technique, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for prompt_technique"
domain: "prompt_technique construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_prompt_technique
  - p07_qg_eval_metric
  - p11_qg_usage_report
  - p03_qg_multimodal_prompt
  - p05_qg_product_tour
  - p05_qg_pricing_page
  - p05_qg_integration_guide
  - p05_qg_user_journey
  - p03_qg_prompt_optimizer
  - p02_qg_customer_segment
---

## Quality Gate

## Definition  
(Table: metric, threshold, operator, scope)  
| metric         | threshold              | operator | scope                  |  
|----------------|------------------------|----------|------------------------|  
| Prompt Pattern | ^p03_pt_[a-z][a-z0-9_]+.md$ | matches  | Schema ID (H02)        |  

## HARD Gates  
(Table: ID | Check | Fail Condition)  
| ID      | Check                          | Fail Condition                                      |  
|---------|--------------------------------|-----------------------------------------------------|  
| H01     | YAML frontmatter valid         | Invalid YAML syntax or missing required fields      |  
| H02     | ID matches pattern             | ID does not match ^p03_pt_[a-z][a-z0-9_]+.md$      |  
| H03     | kind field matches 'prompt_technique' | kind field is not 'prompt_technique'              |  
| H04     | Prompt technique is unique     | Duplicate technique ID or name detected             |  
| H05     | Description is non-empty       | Description field is missing or blank               |  
| H06     | No harmful patterns detected   | Contains banned keywords or unsafe templates        |  
| H07     | Example usage provided         | No example usage or example is incomplete           |  

## SOFT Scoring  
(Table: Dim | Dimension | Weight | Scoring Guide)  
| Dim | Dimension         | Weight | Scoring Guide                                                                 |  
|-----|-------------------|--------|-------------------------------------------------------------------------------|  
| D1  | Clarity           | 0.15   | Clear, concise, and actionable (1.0) vs. vague (0.0)                         |  
| D2  | Originality       | 0.15   | Novel approach (1.0) vs. derivative or generic (0.0)                         |  
| D3  | Alignment         | 0.15   | Fully aligns with CEX guidelines (1.0) vs. partial or no alignment (0.0)     |  
| D4  | Safety            | 0.15   | No risks identified (1.0) vs. moderate/high risks (0.0)                      |  
| D5  | Formatting        | 0.10   | Adheres to schema (1.0) vs. formatting errors (0.0)                          |  
| D6  | Example Quality   | 0.15   | Realistic, complete example (1.0) vs. placeholder or missing (0.0)           |  
| D7  | Adaptability      | 0.15   | Works across use cases (1.0) vs. limited scope (0.0)                         |  

## Actions  
(Table: Score | Action)  
| Score      | Action                          |  
|------------|---------------------------------|  
| GOLDEN     | Auto-publish and archive        |  
| PUBLISH    | Manual review by domain expert  |  
| REVIEW     | Flag for stakeholder feedback   |  
| REJECT     | Reject and require rework       |  

## Bypass  
(Table: conditions, approver, audit trail)  
| conditions                          | approver         | audit trail                          |  
|-----------------------------------|------------------|--------------------------------------|  
| Exception for experimental use    | Senior Engineer  | Note in audit trail with justification |

## Examples

## Golden Example
```yaml
name: "Chain-of-Thought with Self-Consistency"
kind: prompt_technique
vendor: Anthropic
model: Claude 3.5
version: 1.0
body: |
  1. Frame the problem as a multi-step reasoning task
  2. Generate 3 independent solutions using separate reasoning paths
  3. Compare results and select the most consistent answer
  4. Use explicit markers like [Reasoning 1], [Reasoning 2] for clarity
  Example: "Solve this math problem by showing three different solution paths, then choose the most consistent answer."
```

## Anti-Example 1: Template Confusion
```yaml
name: "Generic Question Template"
kind: prompt_technique
vendor: OpenAI
model: GPT-4
version: 0.1
body: |
  "Please answer the following question: [Question here]. Provide a detailed explanation."
```
## Why it fails
This is a reusable template (prompt_template), not a specific prompting method. It lacks the structural pattern that defines a true prompt_technique.

## Anti-Example 2: Vague Instructions
```yaml
name: "Unstructured Thinking"
kind: prompt_technique
vendor: Google
model: Gemini Pro
version: 1.0
body: |
  "Think deeply about this and give a thorough answer."
```
## Why it fails
The instruction is too vague to qualify as a technique. It doesn't define a specific pattern or method for structuring the prompt, making it non-reproducible.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
