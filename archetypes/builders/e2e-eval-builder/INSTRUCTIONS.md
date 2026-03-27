---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for e2e_eval
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce an e2e_eval

## Phase 1: RESEARCH
1. Identify the pipeline to test (which agents/stages in which order)
2. Find existing e2e_evals for the same pipeline (search P07_evals/)
3. Map all stages and their intermediate outputs
4. Identify data fixtures needed for reproducibility
5. Check brain_query [IF MCP] for duplicate e2e_evals

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill following SCHEMA constraints
3. Fill frontmatter: all required + recommended fields (quality: null)
4. Define stages list in execution order
5. Write Input section: the pipeline entry point data
6. Write Expected Output section: the final pipeline result
7. Write Stages section: each stage with input/output/assertion
8. Specify data_fixtures for reproducible test data
9. Define environment requirements
10. Write cleanup procedure for post-test state reset

## Phase 3: VALIDATE
1. Check against QUALITY_GATES.md (this builder's own gates)
2. HARD: id format, kind, pillar, quality==null, stages non-empty
3. SOFT: data_fixtures present, cleanup defined, environment specified
4. Verify: stages form a connected pipeline (output_n feeds input_n+1)
5. If score < 8.0: revise before outputting
