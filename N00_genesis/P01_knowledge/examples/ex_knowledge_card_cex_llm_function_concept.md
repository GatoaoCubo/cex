---
id: p01_kc_cex_llm_function_concept
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX LLM Functions — 8 Pipeline Stages from BECOME to COLLABORATE"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, llm-function, pipeline, execution-sequence, become-collaborate]
tldr: "8 LLM functions (BECOME to COLLABORATE) describe the real execution pipeline -- sequence, not categories"
when_to_use: "Understand how LLMs process artifacts and why the sequence matters"
keywords: [llm-function, pipeline, execution-stages, become, collaborate]
long_tails:
  - "What are the 8 functions an LLM executes in each interaction"
  - "What is the difference between LLM function and artifact category"
axioms:
  - "ALWAYS respect the sequence BECOME before INJECT"
  - "NEVER treat functions as static file categories"
linked_artifacts:
  primary: p01_kc_cex_taxonomy
  related: [p01_kc_cex_function_become, p01_kc_cex_function_inject]
density_score: null
data_source: "https://arxiv.org/abs/2308.00352"
related:
  - p01_kc_cex_pipeline_execution
  - p01_kc_cex_lp03_prompt
  - p01_kc_cex_function_become
  - p01_kc_cex_taxonomy
  - p01_kc_cex_function_produce
  - bld_architecture_dataset_card
  - bld_architecture_webinar_script
  - spec_seed_words
  - bld_architecture_experiment_tracker
  - p01_kc_cex_function_collaborate
---

## Summary

LLM function is what the model DOES with an artifact, not what the artifact IS. The 8 functions (BECOME, INJECT, REASON, CALL, PRODUCE, CONSTRAIN, GOVERN, COLLABORATE) form the real execution pipeline of any LLM system. A simple prompt executes 1-2 functions. An agent executes 4-5. An agent_group with complete lifecycle executes all 8. The difference is one of completeness, not nature.

## Spec

| Function | Stage | What It Does | Example Types |
|----------|-------|-------------|---------------|
| BECOME | 1 | Configures identity and role | agent, persona, system_prompt |
| INJECT | 2 | Loads context and knowledge | knowledge_card, memory, embedding |
| REASON | 3 | Reasons and decomposes | chain_of_thought, planner, react |
| CALL | 4 | Uses external tools | tool, mcp_server, api_call |
| PRODUCE | 5 | Generates output artifacts | code, copy, report |
| CONSTRAIN | 6 | Validates against schemas | schema, template, output_format |
| GOVERN | 7 | Applies quality gates | quality_gate, benchmark, lifecycle |
| COLLABORATE | 8 | Coordinates with other agents | handoff, signal, shared_state |

Complete pipeline: INPUT -> BECOME -> INJECT -> REASON -> CALL -> PRODUCE -> CONSTRAIN -> GOVERN -> COLLABORATE -> OUTPUT.

Functions 1-2 configure. Functions 3-5 execute. Functions 6-8 validate and communicate. Empirical discovery: initial hypothesis of 6 functions expanded to 8 upon finding that REASON and COLLABORATE had dedicated artifacts in all analyzed frameworks.

## Patterns

| Trigger | Action |
|---------|--------|
| Agent without defined identity | BECOME with system_prompt + mental_model |
| Response without relevant context | Verify if INJECT loaded knowledge |
| Output with inconsistent format | Add CONSTRAIN with explicit schema |
| Multi-agent system without coordination | Implement COLLABORATE with signals |
| Opaque reasoning in critical decisions | Activate REASON with chain_of_thought |

## Code

<!-- lang: python | purpose: LLM function pipeline sequence -->
```python
PIPELINE = [
    "BECOME",      # 1. identidade
    "INJECT",      # 2. contexto
    "REASON",      # 3. raciocinio
    "CALL",        # 4. ferramentas
    "PRODUCE",     # 5. geracao
    "CONSTRAIN",   # 6. validacao
    "GOVERN",      # 7. quality gates
    "COLLABORATE", # 8. coordenacao
]
# prompt simples: BECOME(implicit) + PRODUCE
# agente: BECOME + INJECT + REASON + CALL + PRODUCE
# agent_group: todas as 8 funcoes
```

## Anti-Patterns

- Skipping BECOME and sending input directly (no identity)
- Confusing INJECT with BECOME (context vs identity)
- Executing CALL before REASON (action without planning)
- PRODUCE without CONSTRAIN (output without format contract)
- Treating functions as filesystem folder categories

## References

- source: https://arxiv.org/abs/2308.00352
- source: https://arxiv.org/abs/2303.17760
- related: p01_kc_cex_function_become
- related: p01_kc_cex_function_inject

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_pipeline_execution]] | sibling | 0.68 |
| [[p01_kc_cex_lp03_prompt]] | sibling | 0.34 |
| [[p01_kc_cex_function_become]] | sibling | 0.34 |
| [[p01_kc_cex_taxonomy]] | sibling | 0.33 |
| [[p01_kc_cex_function_produce]] | sibling | 0.31 |
| [[bld_architecture_dataset_card]] | downstream | 0.31 |
| [[bld_architecture_webinar_script]] | downstream | 0.29 |
| [[spec_seed_words]] | related | 0.28 |
| [[bld_architecture_experiment_tracker]] | downstream | 0.28 |
| [[p01_kc_cex_function_collaborate]] | sibling | 0.28 |
