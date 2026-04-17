---
kind: architecture
id: bld_architecture_search_strategy
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of search_strategy -- inventory, dependencies
quality: 9.0
title: "Architecture Search Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [search_strategy, builder, architecture]
tldr: "Component map of search_strategy -- inventory, dependencies"
domain: "search_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Component Inventory
| ISO | llm_function | Purpose | Status |
|-----|-------------|---------|--------|
| bld_manifest_search_strategy | BECOME | Builder identity: inference-time compute allocation specialist | Production |
| bld_system_prompt_search_strategy | BECOME | Persona: compute orchestration engineer | Production |
| bld_instruction_search_strategy | REASON | 3-phase production (Research/Compose/Validate) | Production |
| bld_schema_search_strategy | CONSTRAIN | Schema: id pattern ^p04_ss_*, strategy_type enum | Production |
| bld_quality_gate_search_strategy | GOVERN | HARD gates (H01-H08) + SOFT scoring (D01-D10) | Production |
| bld_output_template_search_strategy | PRODUCE | Frontmatter + body structure for search_strategy artifact | Production |
| bld_examples_search_strategy | INJECT | Golden (Dynamic Resource Allocation) + 2 anti-examples | Production |
| bld_knowledge_card_search_strategy | INJECT | Domain KC: MLPerf, edge AI, Kubernetes, cost modeling | Production |
| bld_tools_search_strategy | CALL | Elasticsearch, LangChain, compute simulator | Production |
| bld_collaboration_search_strategy | COLLABORATE | Crew: upstream retriever, downstream inference engine | Production |
| bld_config_search_strategy | CONSTRAIN | Naming: p04_ss_{{name}}.md, max_bytes=4096 | Production |
| bld_memory_search_strategy | INJECT | Learning record: 20% latency reduction via query profiling | Production |
| bld_architecture_search_strategy | CONSTRAIN | This file -- component map and ISO dependencies | Production |

## Dependencies
| From | To | Type |
|------|----|------|
| bld_instruction | bld_schema | Reads schema before compose phase |
| bld_instruction | bld_output_template | Fills template at F6 PRODUCE |
| bld_system_prompt | bld_manifest | Derives compute-specialist persona |
| bld_quality_gate | bld_schema | H02 enforces schema ID pattern ^p04_ss_* |
| bld_examples | bld_knowledge_card | Examples demonstrate MLPerf compute allocation patterns |
| retriever-builder | search_strategy-builder | Retriever defines query load that search_strategy allocates |

## Architectural Position
search_strategy-builder occupies P04 (Tools pillar) in the CEX taxonomy. It produces inference-time compute allocation strategies: how CPU/GPU/memory resources are assigned to query execution based on complexity, load, and latency SLAs. Upstream: retriever (query patterns), reasoning_strategy (compute requirements). Downstream: runtime_rule, rate_limit_config (enforce allocation).
