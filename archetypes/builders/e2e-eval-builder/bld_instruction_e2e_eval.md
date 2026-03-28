---
kind: instruction
id: bld_instruction_e2e_eval
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for e2e_eval
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce an e2e_eval
## Phase 1: RESEARCH
1. Identify the pipeline to test: name the entry point and the final output, and describe what the pipeline does end-to-end
2. List all stages in execution order — each stage is one agent, model call, or processing step with a defined input and output
3. Define data fixtures: realistic input values that can be used reproducibly across test runs (no random or time-dependent data)
4. Specify the expected output for each stage and for the final result, with enough detail to assert pass or fail
5. Determine environment requirements: which services must be running, which config values must be set, whether a test database is needed
6. Check existing e2e_evals in P07 for coverage gaps — do not duplicate a pipeline already tested; extend or differentiate instead
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints
3. Fill all required and recommended frontmatter fields; set `quality: null` — never self-score
4. Write **Pipeline Flow** section: ordered list of stages, each with agent or step name
5. Write **Data Fixtures** section: concrete input values with realistic, non-trivial content
6. Write **Stage Assertions** section: expected intermediate output per stage — one assertion block per stage
7. Write **Expected Final Output** section: the complete expected result at the pipeline exit point
8. Write **Environment** section: services, configuration keys, test database or fixture store required
9. Write **Cleanup** section: teardown steps to reset state after the test so reruns are not contaminated
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. HARD gates: `id` matches `^p07_e2e_[a-z][a-z0-9_]+$`, `kind` is the literal string `e2e_eval`, `quality` is null, pipeline has at least 2 stages, data fixtures are present, expected final output is defined
3. SOFT gates: score each gate from QUALITY_GATES.md against the artifact
4. Confirm stages form a connected sequence: the output of stage N feeds the input of stage N+1
5. Cross-check: does this test a full pipeline from entry to exit? If it tests a single function or isolated unit it belongs in a `unit_eval`. If it measures performance under load it belongs in a `benchmark`. Assertions must be concrete values, not aspirational descriptions.
6. If score < 8.0: revise in the same pass before outputting
