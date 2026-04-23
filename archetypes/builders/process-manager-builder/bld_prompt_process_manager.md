---
quality: 7.8
id: bld_instruction_process_manager
kind: instruction
pillar: P12
title: "Process Manager Builder -- Instruction"
version: 1.0.0
quality: 7.3
tags: [builder, process_manager, instruction]
llm_function: REASON
author: builder
density_score: 0.8
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_instruction_hook
  - bld_instruction_golden_test
  - p03_ins_lifecycle_rule
  - bld_instruction_input_schema
  - bld_instruction_instruction
  - bld_instruction_action_prompt
  - bld_instruction_cli_tool
  - bld_instruction_context_doc
  - bld_memory_runtime_state
  - bld_instruction_chain
---
# Instructions: How to Produce a process_manager
## Phase 1: RESEARCH
1. Identify the business process being coordinated -- what multi-step operation spans multiple services or aggregates?
2. Define the correlation key: what identifier ties all events/commands in one process instance together?
3. Map events received: what domain events does this process manager subscribe to?
4. Map commands issued: for each received event, what command is dispatched and to whom?
5. Design state machine: what are the states, transitions, and terminal states (success + failure)?
6. Define timeout strategy: what happens if a step does not complete within SLA?
7. Define compensation: how does the process roll back if a step fails?
## Phase 2: COMPOSE
1. Read bld_schema_process_manager.md -- source of truth for required fields
2. Fill frontmatter: id pattern p12_pm_{slug}, kind: process_manager, quality: null
3. Write Correlation section: how process instances are identified and tracked
4. Write States section: state machine with all states and allowed transitions
5. Write Event Routing table: event -> state transition + command dispatched
6. Write Commands section: each command issued with target and payload
7. Write Timeout section: per-state timeouts and timeout actions
8. Write Compensation section: failure path with rollback commands
## Phase 3: VALIDATE
1. HARD gates: id matches `p12_pm_[a-z][a-z0-9_]+`, kind == process_manager, quality == null
2. Correlation key defined, state machine has start state and terminal states
3. Every event in routing table has a command dispatched
4. Timeout and compensation actions defined
5. If score < 8.0: revise before outputting


## Prompt Construction Checklist

- Verify prompt follows target kind's instruction template
- Validate variable placeholders use standard naming convention
- Cross-reference with chain dependencies for context completeness
- Test prompt with sample input before publishing

## Prompt Pattern

```yaml
# Prompt validation
template_match: true
variables_valid: true
chain_refs_checked: true
sample_tested: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_prompt_optimizer.py --check
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_hook]] | sibling | 0.29 |
| [[bld_instruction_golden_test]] | sibling | 0.28 |
| [[p03_ins_lifecycle_rule]] | sibling | 0.28 |
| [[bld_instruction_input_schema]] | sibling | 0.28 |
| [[bld_instruction_instruction]] | sibling | 0.27 |
| [[bld_instruction_action_prompt]] | sibling | 0.26 |
| [[bld_instruction_cli_tool]] | sibling | 0.26 |
| [[bld_instruction_context_doc]] | sibling | 0.25 |
| [[bld_memory_runtime_state]] | upstream | 0.24 |
| [[bld_instruction_chain]] | sibling | 0.24 |
