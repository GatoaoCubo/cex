---
kind: architecture
id: bld_architecture_few_shot_example
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of few_shot_example — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Few Shot Example"
version: "1.0.0"
author: n03_builder
tags: [few_shot_example, builder, examples]
tldr: "Golden and anti-examples for few shot example construction, demonstrating ideal structure and common pitfalls."
domain: "few shot example construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_few_shot_example
  - bld_model_few_shot_example
  - bld_prompt_few_shot_example
  - bld_schema_few_shot_example
  - bld_memory_few_shot_example
  - bld_feedback_few_shot_example
  - bld_eval_few_shot_example
  - bld_tools_few_shot_example
  - bld_output_few_shot_example
  - bld_config_few_shot_example
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| input_text | Realistic task request that mimics a real user or system prompt | few_shot_example | required |
| output_text | Ideal response demonstrating the target format exactly | few_shot_example | required |
| domain | Subject area the example belongs to; scopes the learning signal | few_shot_example | required |
| difficulty | Calibration level: easy, medium, or hard | few_shot_example | required |
| format_target | The specific format being taught (JSON, YAML, Markdown, table, etc.) | few_shot_example | required |
| edge_case_flag | Whether this example covers a boundary or unusual condition | few_shot_example | optional |
| byte_budget | Size constraint (max 1024 bytes); keeps context injection cost low | few_shot_example | required |
## Dependency Graph
```
knowledge_card (P01) --produces--> few_shot_example
schema (P06)         --depends-->  few_shot_example
few_shot_example     --produces--> system_prompt (P03)
few_shot_example     --produces--> action_prompt (P03)
golden_test (P07)    --depends-->  few_shot_example
```
| From | To | Type | Data |
|------|----|------|------|
| knowledge_card (P01) | few_shot_example | produces | domain facts and concepts to exemplify |
| schema (P06) | few_shot_example | depends | format constraints the output must conform to |
| few_shot_example | system_prompt (P03) | produces | injected input/output pair for format teaching |
| few_shot_example | action_prompt (P03) | produces | task demonstration injected into action context |
| golden_test (P07) | few_shot_example | depends | uses exemplary pairs as quality reference anchors |
## Boundary Table
| few_shot_example IS | few_shot_example IS NOT |
|---------------------|-------------------------|
| An input/output pair that teaches format by demonstration | An artifact with a scoring rubric or quality grade (that is golden_test) |
| Evaluated externally; quality is null in the artifact itself | A prompt template with `{{variables}}` for reuse |
| Subject to a byte budget (max 1024 bytes) | Background domain knowledge without an input/output pair |
| A teaching unit — shows HOW to format a response | A test assertion that checks correctness (that is unit_eval) |
| Domain-scoped and difficulty-calibrated | An orchestration step or workflow instruction |
| Stateless — no execution context, just a static pair | A context document explaining system background |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| Source | knowledge_card (P01), schema (P06) | Provide domain facts and format constraints to exemplify |
| Content | input_text, output_text | The core teaching pair — request and ideal response |
| Metadata | domain, difficulty, format_target, edge_case_flag | Classify the example for selection and calibration |
| Budget | byte_budget | Enforce size constraint for cost-effective context injection |
| Injection | system_prompt (P03), action_prompt (P03) | Consume the pair as format-teaching context |
| Evaluation | golden_test (P07) | Use exemplary pairs as quality calibration anchors (external) |
