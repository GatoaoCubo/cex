---
kind: instruction
id: bld_instruction_llm_judge
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for llm_judge
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Llm Judge"
version: "1.0.0"
author: n03_builder
tags: [llm_judge, builder, examples]
tldr: "Golden and anti-examples for llm judge construction, demonstrating ideal structure and common pitfalls."
domain: "llm judge construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_llm_judge_builder
  - p11_qg_llm_judge
  - bld_instruction_reward_signal
  - bld_instruction_output_validator
  - bld_instruction_retriever_config
  - bld_instruction_memory_scope
  - bld_instruction_chunk_strategy
  - bld_instruction_eval_dataset
  - bld_instruction_context_doc
  - bld_instruction_handoff_protocol
---

# Instructions: How to Produce a llm_judge
## Phase 1: RESEARCH
1. Identify what is being evaluated: RAG responses, code quality, dialogue, summarization, classification, etc.
2. Determine the evaluation context: reference-based (ground truth available) or reference-free
3. Select judge_model: choose a frontier model from a different family than the evaluated model to avoid self-enhancement bias
4. Define criteria: list 1-5 independent quality dimensions (e.g. faithfulness, relevance, coherence, completeness, safety)
5. Confirm criteria are non-overlapping: each dimension must measure ONE thing; overlap = double-penalization
6. Choose scale type: binary (pass/fail gates), likert 1-5 (general quality), 1-10 (fine-grained), continuous 0.0-1.0 (Braintrust)
7. Write scale anchors: define what the minimum, midpoint, and maximum scores mean concretely
8. Identify framework: Braintrust, DeepEval, RAGAS, Promptfoo, OpenAI Evals, or costm
9. Check for existing llm_judge artifacts in pool to avoid duplicates
10. Confirm artifact slug for id: snake_case, lowercase, no hyphens
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Set judge_model: concrete identifier (e.g. "gpt-4o", "claude-3-5-sonnet-20241022")
5. Write criteria list in frontmatter: exact names that match ## Criteria sections in body
6. Write scale block: type, min, max, anchors map with at least 3 anchor points
7. Write Overview section: what the judge evaluates, use case, reference-based or free
8. Write Criteria section: for each criterion, definition + what high score looks like + what low score looks like
9. Write Scale section: scale type, anchor labels with concrete examples of what each score means
10. Write Few-Shot Examples section: minimum 2 examples (1 high, 1 low) each with input, score, and rationale
11. Set chain_of_thought: true (default); document reason if false
12. Set temperature: 0.0 for reproducibility; document reason if higher
13. Set aggregation method if multi-criteria: mean, min, max, or weighted_sum
14. Verify body <= 2048 bytes
15. Verify id matches `^p07_judge_[a-z][a-z0-9_]+$`
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p07_judge_` prefix pattern
4. Confirm kind == llm_judge
5. Confirm judge_model is a concrete model identifier (not a placeholder)
6. Confirm criteria list in frontmatter matches ## Criteria section names exactly
7. Confirm scale has min, max, and anchor labels
8. Confirm at least 2 few_shot examples with scores within declared scale range
9. HARD gates: frontmatter valid, id pattern, judge_model present, criteria offined, scale declared
10. SOFT gates: score against QUALITY_GATES.md
11. Cross-check boundaries: has judge_model? (if no -> scoring_rubric, not llm_judge). Blocks pipeline? (if yes -> quality_gate P11). Measures comparative performance? (if yes -> benchmark). Formula-based? (if yes -> metric).
12. Revise if score < 8.0 before outputting


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_llm_judge_builder]] | downstream | 0.46 |
| [[p11_qg_llm_judge]] | downstream | 0.44 |
| [[bld_instruction_reward_signal]] | sibling | 0.43 |
| [[bld_instruction_output_validator]] | sibling | 0.40 |
| [[bld_instruction_retriever_config]] | sibling | 0.39 |
| [[bld_instruction_memory_scope]] | sibling | 0.39 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.39 |
| [[bld_instruction_eval_dataset]] | sibling | 0.38 |
| [[bld_instruction_context_doc]] | sibling | 0.38 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.38 |
