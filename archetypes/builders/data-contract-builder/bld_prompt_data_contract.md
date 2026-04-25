---
quality: 7.8
id: bld_instruction_data_contract
kind: instruction
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for data_contract
version: 1.0.0
quality: 7.3
tags: [data_contract, builder, instruction]
title: "Instruction Data Contract Builder"
author: builder
tldr: "Step-by-step production process for data_contract"
density_score: 0.83
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_instruction_input_schema
  - bld_instruction_golden_test
  - bld_instruction_instruction
  - bld_instruction_action_prompt
  - bld_instruction_interface
  - bld_instruction_memory_scope
  - bld_instruction_output_validator
  - bld_instruction_kind
  - bld_instruction_retriever_config
  - bld_instruction_handoff_protocol
---
# Instructions: How to Produce a data_contract
## Phase 1: IDENTIFY
1. Name producer system and consumer system (teams or services)
2. Identify the data entity being exchanged (Event, Record, API response)
3. Determine transport: REST, event bus, file, database view, gRPC
4. List all fields with types -- producer is source of truth for schema
5. Confirm this needs a formal contract (crossing team/system boundary)
## Phase 2: COMPOSE
1. Read bld_schema_data_contract.md for required fields
2. Set id: dc_{producer}_{consumer}_{entity} (snake_case)
3. Fill producer_system and consumer_system
4. Define schema section: all fields with type, nullable, description
5. Define SLA section: freshness_sla, availability_sla, latency_p99
6. Set contract_version (semver) and effective_date
7. Set quality: null -- never self-score
## Phase 3: VALIDATE
1. HARD gates:
   - id follows pattern dc_{prod}_{cons}_{entity}
   - kind == data_contract
   - quality == null
   - producer_system and consumer_system both present
   - schema section with >= 1 typed field
   - at least one SLA field (freshness OR availability)
2. SOFT gates:
   - all schema fields have types and nullable flag
   - SLA includes numeric thresholds (not vague "fast" or "available")
   - backward_compatible field set (true/false)
   - breaking_change_policy documented


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
| [[bld_instruction_input_schema]] | sibling | 0.34 |
| [[bld_instruction_golden_test]] | sibling | 0.26 |
| [[bld_instruction_instruction]] | sibling | 0.26 |
| [[bld_instruction_action_prompt]] | sibling | 0.26 |
| [[bld_instruction_interface]] | sibling | 0.25 |
| [[bld_instruction_memory_scope]] | sibling | 0.24 |
| [[bld_instruction_output_validator]] | sibling | 0.24 |
| [[bld_instruction_kind]] | sibling | 0.24 |
| [[bld_instruction_retriever_config]] | sibling | 0.23 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.23 |
