---
id: bld_instruction_data_contract
kind: instruction
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for data_contract
version: 1.0.0
quality: null
tags: [data_contract, builder, instruction]
title: "Instruction Data Contract Builder"
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
