---
kind: knowledge_card
id: bld_knowledge_card_few_shot_example
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for few_shot_example production — format-teaching I/O pairs
sources: Brown et al. 2020 (GPT-3), Anthropic prompt engineering, in-context learning research
quality: 9.1
title: "Knowledge Card Few Shot Example"
version: "1.0.0"
author: n03_builder
tags: [few_shot_example, builder, examples]
tldr: "Golden and anti-examples for few shot example construction, demonstrating ideal structure and common pitfalls."
domain: "few shot example construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_architecture_few_shot_example
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

# Domain Knowledge: few_shot_example
## Executive Summary
Few-shot examples are input/output pairs that teach LLMs format and quality through in-context demonstration. 1-3 examples dramatically improve task performance (Brown et al. 2020) — the LLM pattern-matches example structure. A mediocre prompt with a golden example outperforms an excellent prompt with no example. Few-shot examples differ from golden tests (quality evaluation with scoring) and unit evals (assertion-based correctness testing).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P01 (knowledge) |
| Max size | 1024 bytes per example |
| Quality gates | 7 HARD + 7 SOFT |
| Quantity rule | 1 golden + 1 anti per builder (sufficient) |
| Max examples | 3 golden + 3 anti (context budget limit) |
| Purpose | Teach FORMAT, not evaluate QUALITY |
## Patterns
- **Golden example structure**: three layers
| Layer | Content | Rule |
|-------|---------|------|
| Frontmatter | Every schema field with realistic value | Missing field = LLM learns to omit it |
| Dense body | Concrete domain content, no filler | Every sentence carries information |
| WHY GOLDEN | Maps each quality gate to example | Bridge between example and schema |
- **Anti-example structure**: deliberately violates schema to teach what NOT to produce
| Layer | Content | Rule |
|-------|---------|------|
| Wrong frontmatter | Missing fields, wrong prefix, self-scored quality | Shows specific violations |
| Generic body | Filler language, no domain content | "You are a helpful assistant" |
| FAILURES | Numbered list of violated gates | Gate code + FAIL for each |
- **Bridge pattern**: SCHEMA defines fields → EXAMPLE demonstrates them → GATES validate them
- **Density test**: if replacing a sentence with "blah blah" and example seems complete, that sentence is filler
- **Input specificity**: golden input names concrete artifacts; anti input is vague and generic
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Abstract output ("good response") | LLM learns vagueness, not format |
| Vague input ("write something") | No domain anchor; any output seems valid |
| Self-scored quality field | Must be null; self-scoring teaches wrong pattern |
| Body > 1024 bytes | Exceeds context budget; compress |
| Missing gate references in WHY | Bridge between example and schema is broken |
| >3 golden examples | Diminishing returns; wastes context window |
## Application
1. Read target type's SCHEMA.md: know every required field and gate
2. Write golden: specific input + fully-formatted output + WHY GOLDEN mapping all gates
3. Write anti: vague input + deliberately wrong output + FAILURES listing violated gates
4. Verify bridge: every schema field appears in golden; every HARD gate referenced
5. Density check: every sentence in body carries information; no filler
6. Validate: <= 1024 bytes per example, quality: null, realistic domain values
## References
- Brown et al. 2020: "Language Models are Few-Shot Learners" (GPT-3)
- Anthropic: prompt engineering — in-context example design
- Min et al. 2022: "Rethinking the Role of Demonstrations in In-Context Learning"
- Liu et al. 2022: few-shot example selection and ordering effects
