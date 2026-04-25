# GLOSSARY: 68 Artifact Types x 12 Pillars

---

## CORE (weight 1.0)

### P01 Knowledge (6 types)
- knowledge_card: searchable atomic fact (max 2KB)
- rag_source: indexable external source
- glossary_entry: term definition
- context_doc: domain context
- embedding_config: embedding configuration
- few_shot_example: example for prompt

### P02 Model (7 types)
- agent: agent definition (persona + capabilities)
- lens: specialized perspective on a domain
- boot_config: initialization configuration
- mental_model: agent mental map
- model_card: LLM specification
- router: routing rule
- fallback_chain: fallback sequence

### P03 Prompt (5 types)
- system_prompt: system prompt
- action_prompt: specific action prompt
- prompt_template: template with {{vars}}
- instruction: operational instruction
- chain: prompt sequence

### P04 Tools (9 types)
- mcp_server: MCP server
- hook: pre/post processing hook
- skill: reusable skill
- plugin: pluggable extension
- client: API client
- cli_tool: CLI tool
- scraper: data extractor
- connector: service connector
- daemon: background process

---

## QUALITY (weight 0.8)

### P05 Output (4 types)
- output_schema: output format
- parser: output data extractor
- formatter: output formatter
- naming_rule: naming convention

### P06 Schema (5 types)
- input_schema: input contract
- output_schema: output contract
- type_def: custom type definition
- validator: validation rule
- interface: integration contract

### P07 Evals (6 types)
- unit_eval: agent unit test
- smoke_eval: quick sanity test
- e2e_eval: end-to-end test
- benchmark: performance measurement
- golden_test: reference test case (9.5+)
- scoring_rubric: evaluation criteria

### P11 Feedback (5 types)
- quality_gate: quality barrier
- bugloop: automated fix cycle
- lifecycle_rule: lifecycle rule
- guardrail: safety constraint
- optimizer: process optimizer

---

## SCALE (weight 0.6)

### P08 Architecture (5 types)
- agent_card: agent group specification
- pattern: reusable pattern
- law: operational law
- diagram: architecture diagram
- component_map: component map

### P09 Config (5 types)
- env_config: environment variables
- path_config: system paths
- permission: permission rule
- feature_flag: feature flag
- runtime_rule: runtime rule

### P10 Memory (5 types)
- mental_model: persistent mental model
- knowledge_index: search index
- learning_record: learning record
- session_state: session state
- axiom: fundamental rule

### P12 Orchestration (6 types)
- workflow: workflow
- dag: directed acyclic dependency graph
- spawn_config: spawn configuration
- signal: inter-agent communication signal
- handoff: handoff instruction
- dispatch_rule: dispatch rule

---

TOTAL: 68 fixed CORE types + _custom/ per pillar
Promotion: used 10x + quality > 8.0 = becomes CORE

---
*GLOSSARY v1.0 | 2026-03-22*
