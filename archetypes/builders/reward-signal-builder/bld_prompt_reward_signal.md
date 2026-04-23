---
kind: instruction
id: bld_instruction_reward_signal
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for reward_signal
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Reward Signal"
version: "1.0.0"
author: n03_builder
tags: [reward_signal, builder, examples]
tldr: "Golden and anti-examples for reward signal construction, demonstrating ideal structure and common pitfalls."
domain: "reward signal construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_llm_judge
  - p03_sp_reward_signal_builder
  - bld_instruction_output_validator
  - p11_qg_reward_signal
  - bld_instruction_retriever_config
  - bld_instruction_memory_scope
  - bld_instruction_chunk_strategy
  - bld_instruction_prompt_version
  - bld_instruction_handoff_protocol
  - bld_instruction_constraint_spec
---

# Instructions: How to Produce a reward_signal
## Phase 1: RESEARCH
1. Identify the domain and what quality dimension the signal must measure (helpfulness, factual accuracy, tone, safety, etc.)
2. Determine signal_type: scalar if a single judge score suffices; preference if training RLHF from pairs; critique if Constitutional AI cycle; comparative if ranking N outputs; implicit if mining behavioral signals
3. Choose scale: 0-1 for normalized probability-like scores; 0-10 for human rubric alignment; binary for pass/fail proxies; -1_to_1 for directional signals
4. Identify which model (or human annotator) will produce the reward and confirm it is reliable for this domain (avoid verbosity bias, positional bias)
5. Decompose quality into >= 2 weighted criteria — list each dimension, its weight, and a concrete low/high example
6. Set baseline: research P20 of human-rated outputs for this domain or use 0.7 for normalized scales as default starting point; justify the choice
7. Determine frequency: per_turn for interactive agents; per_task for multi-step workflows; per_session for session-level quality; on_demand for human spot-checks
8. Determine aggregation: mean for stable signals; weighted_mean when criteria have unequal importance; min for safety (weakest link); last for recency-weighted signals
9. Identify the application loop: RLHF (reward model training), DPO (preference dataset), filtering (training data curation), monitoring (production alerting)
10. Check for existing reward_signal artifacts to avoid duplicates; confirm slug is snake_case, no hyphens
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write Overview section: what quality dimension this signal measures, who consumes it, and what improvement loop it feeds (2-4 sentences)
5. Write Signal Design section: type with justification, scale with semantic meaning at low/high, model with reliability rationale, computation method step-by-step, frequency, aggregation
6. Write Criteria section: table with dimension, weight, low-score example, high-score example; weights must sum to 1.0; minimum 2 dimensions; note baseline and what happens below it
7. Write Application section: improvement loop name, consumer, cadence, how scores are collected and applied
8. Verify body <= 2048 bytes
9. Verify id matches `^p11_rs_[a-z][a-z0-9_]+$`
10. Verify baseline is within declared scale range
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p11_rs_` prefix
4. Confirm kind == reward_signal
5. Confirm signal_type is one of the five valid enum values
6. Confirm baseline is within scale range (H08 — hardest gate to catch)
7. Confirm tags includes "reward_signal"
8. Confirm all 4 body sections present: Overview, Signal Design, Criteria, Application
9. SOFT gates: score against QUALITY_GATES.md
10. Cross-check: is this truly a continuous score (not binary pass/fail = quality_gate)? Is it measuring quality (not defining criteria taxonomy = scoring_rubric)? Does it have an improvement loop consumer?
11. Revise if score < 8.0 before outputting


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_llm_judge]] | sibling | 0.46 |
| [[p03_sp_reward_signal_builder]] | downstream | 0.44 |
| [[bld_instruction_output_validator]] | sibling | 0.41 |
| [[p11_qg_reward_signal]] | downstream | 0.41 |
| [[bld_instruction_retriever_config]] | sibling | 0.40 |
| [[bld_instruction_memory_scope]] | sibling | 0.40 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.39 |
| [[bld_instruction_prompt_version]] | sibling | 0.38 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.38 |
| [[bld_instruction_constraint_spec]] | sibling | 0.38 |
