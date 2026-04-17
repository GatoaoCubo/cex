---
kind: instruction
id: bld_instruction_eval_dataset
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for eval_dataset
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Eval Dataset"
version: "1.0.0"
author: n03_builder
tags: [eval_dataset, builder, examples]
tldr: "Golden and anti-examples for eval dataset construction, demonstrating ideal structure and common pitfalls."
domain: "eval dataset construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Instructions: How to Produce an eval_dataset
## Phase 1: RESEARCH
1. Identify the LLM behavior the dataset evaluates (QA, summarization, classification, tool use, reasoning, etc.)
2. Define the schema: what fields appear in each test case (minimum: input, expected_output)
3. Determine optional metadata fields: difficulty, category, language, source_id, tags
4. Decide on splits: eval-only (test: 1.0) is default unless training use is confirmed
5. Estimate size: how many cases exist now, what is the target size, what is the growth cadence
6. Identify source: human-curated, synthetic (LLM-generated), scraped, adversarial, or hybrid
7. Choose target framework: Braintrust, LangSmith, DeepEval, HuggingFace, or costm
8. Check for existing eval_dataset artifacts to avoid duplicates
9. Confirm dataset slug for id: snake_case, lowercase, no hyphens
10. Confirm this is a COLLECTION (not a single golden_test, not a benchmark, not a scoring_rubric)

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write Overview section: what behavior is evaluated, who uses the dataset, primary use case
5. Write Schema section: define each field (input, expected_output, metadata) with type and description
6. Write Splits section: table of train/test/val percentages with rationale; verify they sum to 1.0
7. Write Integration section: framework adapter pattern, loading code snippet, version migration notes
8. Verify body <= 4096 bytes
9. Verify id matches `^p07_ds_[a-z][a-z0-9_]+$`
10. Verify schema_fields list in frontmatter matches ## Schema section field names exactly

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p07_ds_` prefix pattern
4. Confirm kind == eval_dataset
5. Confirm schema_fields includes both input and expected_output
6. Confirm splits values sum to 1.0 (check float arithmetic)
7. Confirm size is a positive integer
8. HARD gates: frontmatter valid, id pattern, required fields present, splits sum, schema_fields complete
9. SOFT gates: score against QUALITY_GATES.md (framework specified, source declared, versioning defined)
10. Cross-check: is this a collection of cases (eval_dataset) or a single reference case (golden_test)?
    Is this measuring performance (benchmark)? Is this defining criteria (scoring_rubric)?
    If any cross-check fails, redirect to the correct builder with explanation.
11. Revise if score < 8.0 before outputting
