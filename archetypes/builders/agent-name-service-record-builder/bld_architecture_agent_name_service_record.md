---
kind: architecture
id: bld_architecture_agent_name_service_record
pillar: P08
llm_function: CONSTRAIN
purpose: Component inventory and dependency map for the agent-name-service-record-builder
quality: 9.1
title: "Agent Name Service Record Builder -- Architecture"
version: "1.0.0"
author: wave7_n05
tags: [agent_name_service_record, builder, architecture]
tldr: "13-ISO component map with dependencies and data flow for the ANS registry record builder"
domain: "agent_name_service_record construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

# Agent Name Service Record Builder -- Architecture

> Produces `agent_name_service_record` artifacts: IETF ANS / CNCF AgentDNS registry-records advertising discovery-endpoint URLs, protocol adapters, PKI-cert refs, and capability metadata. Operators: GoDaddy, Salesforce, CNCF.

## Component Inventory (13 ISOs)

| # | ISO file | Kind | Pillar | LLM function | Purpose |
|---|---------|------|--------|-------------|---------|
| 01 | bld_manifest_agent_name_service_record.md | type_builder | P04 | BECOME | Builder identity, capabilities, routing table |
| 02 | bld_instruction_agent_name_service_record.md | instruction | P03 | REASON | 3-phase build process (RESEARCH, COMPOSE, VALIDATE) |
| 03 | bld_system_prompt_agent_name_service_record.md | system_prompt | P03 | BECOME | LLM persona, scope constraints, ALWAYS/NEVER rules |
| 04 | bld_schema_agent_name_service_record.md | schema | P06 | CONSTRAIN | Field definitions, types, validation rules |
| 05 | bld_quality_gate_agent_name_service_record.md | quality_gate | P11 | GOVERN | H01-H08 hard gates, 5D soft scoring |
| 06 | bld_output_template_agent_name_service_record.md | output_template | P05 | PRODUCE | Canonical artifact template with placeholders |
| 07 | bld_examples_agent_name_service_record.md | examples | P07 | GOVERN | 1 golden example (GoDaddy), 2 anti-examples |
| 08 | bld_knowledge_card_agent_name_service_record.md | knowledge_card | P01 | INJECT | IETF ANS domain knowledge, concepts, integrations |
| 09 | bld_architecture_agent_name_service_record.md | architecture | P08 | CONSTRAIN | This file -- component map and dependencies |
| 10 | bld_collaboration_agent_name_service_record.md | collaboration | P12 | COLLABORATE | Crew contracts: receives from / produces for |
| 11 | bld_config_agent_name_service_record.md | config | P09 | CONSTRAIN | Naming conventions, paths, limits, hooks |
| 12 | bld_memory_agent_name_service_record.md | learning_record | P10 | INJECT | Observed patterns, pitfalls, recommendations |
| 13 | bld_tools_agent_name_service_record.md | tools | P04 | CALL | Production tools, validation tools, external references |

## Data Flow

```
[User intent: "register agent X"]
        |
        v
bld_manifest (BECOME)          <-- F2: load builder identity, routing check
        |
        v
bld_instruction (REASON)       <-- F4: Phase 1 RESEARCH checklist
        |
        v
bld_knowledge_card (INJECT)    <-- F3: domain facts, standards, concepts
bld_memory (INJECT)            <-- F3: learned pitfalls, observed patterns
        |
        v
bld_schema (CONSTRAIN)         <-- F1: field validation rules
bld_config (CONSTRAIN)         <-- F1: naming pattern, max_bytes limit
        |
        v
bld_system_prompt (BECOME)     <-- F2: LLM persona injection
        |
        v
bld_output_template (PRODUCE)  <-- F6: fill template with resolved data
        |
        v
bld_quality_gate (GOVERN)      <-- F7: H01-H08 hard gates + 5D scoring
bld_examples (GOVERN)          <-- F7: compare against golden example
        |
        v
bld_tools (CALL)               <-- F5+F8: compile, score, index, signal
bld_collaboration (COLLABORATE) <-- F8: handoff to downstream kinds
        |
        v
[artifact: p04_ans_{slug}.md -- ready for ANS registry submission]
```

## External Dependencies

| Dependency | Kind | Where used | Why |
|-----------|------|-----------|-----|
| agent (P02) | agent | Source agent definition | Resolves agent capabilities for capability_advertisement |
| agent_card (P08) | agent_card | Source deployment spec | Extracts endpoint_url and protocol support |
| secret_config (P09) | secret_config | PKI cert material | Supplies pki_cert_reference value |
| transport_config (P04) | transport_config | Protocol adapter specs | Provides per-protocol endpoint URLs and auth methods |

## Downstream Consumers

| Consumer | Kind | What they use |
|---------|------|--------------|
| search_tool (P04) | search_tool | discovery_endpoint URL -- indexes agent for runtime lookup |
| lifecycle_rule (P12) | lifecycle_rule | lifecycle.expires + renewal_policy -- triggers renewal workflows |
| agent_card (P08) | agent_card | agent_name (ANS name) -- back-reference for the agent's own card |
| workflow (P12) | workflow | registry_id -- references this record in multi-agent workflow specs |

## Pillar Coverage

| Pillar | ISO files in this builder | Role |
|--------|--------------------------|------|
| P01 Knowledge | bld_knowledge_card | Domain injection |
| P03 Prompt | bld_instruction, bld_system_prompt | Reasoning + persona |
| P04 CALL | bld_manifest, bld_tools | Builder identity + tools |
| P05 Output | bld_output_template | Artifact template |
| P06 Schema | bld_schema | Field validation |
| P07 Evaluation | bld_examples | Quality calibration |
| P08 Architecture | bld_architecture | Component map (this file) |
| P09 Config | bld_config | Runtime settings |
| P10 Memory | bld_memory | Learning records |
| P11 Feedback | bld_quality_gate | Hard gates + scoring |
| P12 Orchestration | bld_collaboration | Crew contracts |

## Naming Conventions

| Asset | Pattern | Example |
|-------|---------|---------|
| Builder directory | `agent-name-service-record-builder/` | (this directory) |
| ISO files | `bld_{iso}_{kind}.md` | `bld_manifest_agent_name_service_record.md` |
| Artifact files | `p04_ans_{agent_slug}.md` | `p04_ans_billing_bot_acme.md` |
| Compiled YAML | `p04_ans_{agent_slug}.yaml` | `p04_ans_billing_bot_acme.yaml` |
| Max artifact bytes | 3072 | Per kinds_meta.json entry |
