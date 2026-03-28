---
kind: collaboration
id: bld_collaboration_unit_eval
pillar: P07
llm_function: COLLABORATE
purpose: How unit-eval-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: unit-eval-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "does this agent or prompt produce correct output for this specific input?"
I write isolated unit tests with input, expected_output, and assertions mapped to quality gates. I do NOT handle pipeline-level tests (e2e-eval-builder), quick sanity checks (smoke-eval-builder), or quality calibration against golden examples (golden-test-builder).

## Crew Compositions

### Crew: "Agent Build + Test"
```
  1. system-prompt-builder -> "builds the agent identity and rules being tested"
  2. unit-eval-builder -> "writes unit evals: input/expected_output/assertions per capability"
  3. validator-builder -> "adds pre-commit checks that unit eval artifacts are structurally valid"
```

### Crew: "Test Suite"
```
  1. unit-eval-builder -> "verifies individual agent/prompt correctness with assertions"
  2. smoke-eval-builder -> "runs quick sanity checks on the same targets"
  3. e2e-eval-builder -> "tests the full pipeline composed of agents unit-eval verified"
```

## Handoff Protocol

### I Receive
- seeds: target agent or prompt artifact id, capability list to cover, quality gates to assert against
- optional: golden_test reference for expected_output, setup/teardown requirements, edge case inputs

### I Produce
- unit_eval artifact (YAML, input + expected_output + assertions, max 80 lines per eval)
- committed to: `cex/P07_evals/examples/p07_ue_{target_slug}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- scoring-rubric-builder: provides evaluation criteria dimensions for assertion mapping
- golden-test-builder: provides reference outputs to use as expected_output in assertions

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| golden-test-builder | uses unit_evals to validate golden candidate quality before promotion |
| e2e-eval-builder | composes unit_evals into pipeline-level integration tests |
| smoke-eval-builder | derives quick sanity checks from unit_eval assertion sets |
