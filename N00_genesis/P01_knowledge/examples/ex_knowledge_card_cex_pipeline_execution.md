---
id: p01_kc_cex_pipeline_execution
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Pipeline Execution — The 8-Function Sequence From Input to Output"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.0
tags: [cex, pipeline, execution, 8-functions, boot-sequence, llm-processing]
tldr: "Pipeline of 8 functions (BECOME-INJECT-REASON-CALL-PRODUCE-CONSTRAIN-GOVERN-COLLABORATE) is the actual processing of every LLM system"
when_to_use: "Understand the complete execution sequence of an LLM agent or agent_group from input to output"
keywords: [pipeline, execution, 8-functions, boot-sequence, processing]
long_tails:
  - "What is the execution sequence of an LLM agent from input to output"
  - "How does the boot sequence of an agent_group organization work"
axioms:
  - "ALWAYS execute functions in the order BECOME-INJECT-REASON-CALL-PRODUCE-CONSTRAIN-GOVERN-COLLABORATE"
  - "NEVER skip BECOME (identity precedes everything)"
linked_artifacts:
  primary: p01_kc_cex_function_become
  related: [p01_kc_cex_agent_group_concept, p01_kc_cex_cortex_enterprise]
density_score: null
data_source: "https://arxiv.org/abs/2308.00352"
related:
  - p01_kc_cex_llm_function_concept
  - p01_kc_cex_function_become
  - p01_kc_cex_function_produce
  - spec_seed_words
  - p01_kc_cex_lp03_prompt
  - p01_kc_cex_agent_group_concept
  - p01_kc_cex_function_call
  - p01_kc_cex_taxonomy
  - p01_kc_cex_learning_package_concept
  - bld_architecture_dataset_card
---

## Summary

Every LLM system executes the same 8 functions in the same logical order. A simple prompt executes 1-2 (implicit BECOME + PRODUCE). An agent executes 4-5. An agent_group with complete lifecycle executes all 8. The difference between prompt and agent_group is not in nature — it is in completeness. The boot sequence of a Cortex Enterprise is itself an instantiation of these 8 functions.

## Spec

| # | Function | What it does | Boot Equivalent |
|---|----------|-------------|-----------------|
| 1 | BECOME | Configure identity, persona, role | Load PRIME.md + mental_model.yaml |
| 2 | INJECT | Provide context, data, knowledge | Index KC pool via Brain MCP |
| 3 | REASON | Plan, decompose, decide strategy | Read task, decompose into sub-tasks |
| 4 | CALL | Use external tools, APIs, MCPs | brain_query() + connect MCPs |
| 5 | PRODUCE | Generate output: code, KCs, copy, deploy | Execute agent teams per agent_group |
| 6 | CONSTRAIN | Validate against schemas, format output | Validate types, apply templates |
| 7 | GOVERN | Evaluate quality, test, benchmark | Quality gate >= 7.0, pre-commit hooks |
| 8 | COLLABORATE | Signal, commit, dispatch next | Signal file + git commit + next task |

## Patterns

| Trigger | Action |
|---------|--------|
| Simple prompt without agent | Executes BECOME (implicit) + PRODUCE |
| Agent with tools | Adds INJECT + REASON + CALL to pipeline |
| Complete agent_group | Executes all 8 functions in sequence |
| Cortex Enterprise boot | Instantiates the 8 functions as boot sequence |
| GOVERN failure (score < 7.0) | Retry loop: REASON-PRODUCE-CONSTRAIN-GOVERN |

## Anti-Patterns

- Skipping BECOME (generates output without identity, inconsistent)
- INJECT before BECOME (context without role = noise)
- PRODUCE without REASON (output without planning = garbage)
- GOVERN absent (no quality gate = silent degradation)
- COLLABORATE without GOVERN (propagates errors to next in pipeline)

## Code

<!-- lang: python | purpose: 8-function pipeline execution -->
```python
pipeline = [
    ("BECOME",      load_prime, load_mental_model),
    ("INJECT",      index_pool, load_routing_table),
    ("REASON",      read_task, decompose_subtasks),
    ("CALL",        brain_query, connect_mcps),
    ("PRODUCE",     run_agent_teams, generate_artifacts),
    ("CONSTRAIN",   validate_schema, apply_templates),
    ("GOVERN",      quality_gate, run_tests),
    ("COLLABORATE", write_signal, git_commit),
]
for name, *steps in pipeline:
    for step in steps:
        step()  # each function executes in order
# Prompt: executes BECOME(implicit) + PRODUCE only
# Agent: adds INJECT + REASON + CALL
# Agent_group: all 8 functions, full lifecycle
```

## References

- source: https://arxiv.org/abs/2308.00352
- source: https://arxiv.org/abs/2303.17760
- related: p01_kc_cex_function_become
- related: p01_kc_cex_agent_group_concept
- related: p01_kc_cex_cortex_enterprise

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_llm_function_concept]] | sibling | 0.62 |
| [[p01_kc_cex_function_become]] | sibling | 0.31 |
| [[p01_kc_cex_function_produce]] | sibling | 0.30 |
| [[spec_seed_words]] | related | 0.28 |
| [[p01_kc_cex_lp03_prompt]] | sibling | 0.25 |
| [[p01_kc_cex_agent_group_concept]] | sibling | 0.25 |
| [[p01_kc_cex_function_call]] | sibling | 0.25 |
| [[p01_kc_cex_taxonomy]] | sibling | 0.24 |
| [[p01_kc_cex_learning_package_concept]] | sibling | 0.24 |
| [[bld_architecture_dataset_card]] | downstream | 0.24 |
