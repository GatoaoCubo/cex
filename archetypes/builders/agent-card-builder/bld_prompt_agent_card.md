---
id: p03_ins_agent_card_builder
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Agent_group Spec Builder Instructions
target: agent-card-builder agent
phases_count: 4
prerequisites:
  - Agent_group name is defined (non-empty string, kebab-case)
  - Primary domain or responsibility is stated
  - At least one tool or MCP server is identified
  - Target LLM model family is known (e.g. opus, sonnet, haiku)
validation_method: checklist
domain: agent_card
quality: 9.0
tags: [instruction, agent-card, architecture, P08]
idempotent: true
atomic: false
rollback: Delete generated agent_card file and restart from Phase 1
dependencies: []
logging: true
tldr: Build a complete agent_card covering role, model, MCPs, boot sequence, constraints, dispatch rules, and scaling.
density_score: 0.91
llm_function: REASON
related:
  - bld_collaboration_agent_card
  - bld_knowledge_card_agent_card
  - bld_memory_agent_card
  - agent-card-builder
  - p11_qg_agent-card
  - bld_architecture_agent_card
  - p03_sp_agent_card_builder
  - p01_kc_agent_card
  - p12_wf_stella_dispatch
  - bld_collaboration_model_card
---
## Context
The agent-card-builder produces `agent_card` artifacts — complete architectural
specifications for an autonomous agent agent_group. A agent_card defines everything needed
to instantiate, operate, and monitor a agent_group: its role, model, MCP servers, boot sequence,
constraints, dispatch rules, and scaling configuration.
**Input contract**:
- `{{agent_group_name}}`: kebab-case identifier (e.g. `research-sat`, `build-sat`)
- `{{domain}}`: primary operational domain (e.g. `web_research`, `code_generation`)
- `{{model}}`: LLM model identifier (e.g. `claude-opus-4`, `claude-sonnet-4`)
- `{{tools_list}}`: comma-separated list of MCP servers or built-in tools
- `{{constraints_raw}}`: free-text description of operational boundaries
**Output contract**: A single `agent_card` YAML file with 24+ frontmatter fields,
a narrative identity section, and structured subsections for boot sequence, dispatch rules,
constraints, and monitoring.
**Boundaries**:
- Handles full agent_group architecture only.
- Individual agent identity belongs in a separate agent artifact.
- Per-provider boot configuration belongs in a boot_config artifact.
- Reusable operation patterns belong in pattern artifacts.
## Phases
### Phase 1: Analyze Role and Boundary
**Primary action**: Define the agent_group's operational role and establish what it does
versus what it explicitly does not do.
```
INPUT: agent_group_name, domain, constraints_raw
1. Express the agent_group's single primary function:
   role_statement = "{{agent_group_name}} is responsible for [ONE THING]"
   Reject vague roles like "general purpose" or "multi-domain"
2. Map the NOT-domain boundary:
   for each adjacent domain in [research, build, execute, monitor, orchestrate, store]:
     if domain != agent_group's primary domain:
       add to NOT_HANDLES list with brief reason
   Minimum 2 entries required.
3. Determine LLM function type:
   if agent_group makes decisions     -> BECOME
   if agent_group calls external tools -> CALL
   if agent_group coordinates others  -> COLLABORATE
   if agent_group injects context     -> INJECT
4. Extract capability_keywords (5-10 terms) from domain description.
OUTPUT: role_statement, not_handles[], llm_function, capability_keywords[]
```
Verification: `role_statement` is one sentence. `not_handles` has >= 2 entries.
### Phase 2: Specify Model and Tools
**Primary action**: Select and document the model configuration and MCP server bindings.
```
INPUT: model, tools_list, role_statement
1. Model specification:
   model_config = {
     id: {{model}},
     context_window: lookup by family (opus=200k, sonnet=200k, haiku=200k),
     temperature: 0.3 for deterministic tasks | 0.7 for creative tasks,
     max_tokens: sized to expected output
   }
2. MCP server binding for each tool in tools_list:
   mcp_entry = {
     name: tool_name,
     transport: "stdio" | "http",
     required: true | false,
     fallback: null | alternative_tool
   }
3. Boot sequence (ordered list):
   boot_steps = [
     "load system prompt",
     "initialize MCP connections",
     "verify tool availability",
     "load domain context",
     "ready"
   ]
   Add agent-cardific steps between generic ones.
   Assign estimated duration in seconds to each step.
4. boot_time_seconds = sum(step durations)
OUTPUT: model_config{}, mcp_bindings[], boot_sequence[], boot_time_seconds
```
Verification: each MCP entry has `transport` and `required` fields.
`boot_sequence` has >= 4 steps.
### Phase 3: Define Dispatch and Constraints
**Primary action**: Specify how the agent_group receives work, what it accepts or rejects,
and its operational limits.
```
INPUT: constraints_raw, capability_keywords[], role_statement
1. Dispatch rules:
   dispatch = {
     triggers: [keywords that route tasks here],  # >= 3 required
     input_format: "handoff_file" | "inline_prompt" | "both",
     max_prompt_chars: 200 if inline else null,
     priority: "normal" | "high" | "low"
   }
2. Constraint extraction from constraints_raw:
   hard_constraints = []   # things the agent_group MUST NEVER do
   soft_constraints = []   # things the agent_group SHOULD prefer
   for each sentence in constraints_raw:
     if NEVER/MUST NOT/FORBIDDEN -> hard_constraint
     if PREFER/AVOID/MINIMIZE    -> soft_constraint
3. Scaling configuration:
   scaling = {
     max_parallel_instances: 1 | 2 | 3,
     shared_resources: [resources that conflict if parallel],
     cooldown_seconds: wait time between sequential runs
   }
4. Monitoring spec:
   monitoring = {
     signal_on_complete: true,
     signal_on_error: true,
     heartbeat_interval_seconds: null | integer,
     log_level: "info" | "debug" | "error"
   }
OUTPUT: dispatch{}, hard_constraints[], soft_constraints[], scaling{}, monitoring{}
```
Verification: `dispatch.triggers` has >= 3 keywords. `hard_constraints` is non-empty.
### Phase 4: Assemble and Validate Artifact
**Primary action**: Combine all phase outputs into the final agent_card YAML and run
quality gates.
```
INPUT: all outputs from Phases 1-3
1. Assemble frontmatter with 24+ required fields (id, kind, pillar, version,
   created, domain, model, llm_function, boot_time_seconds, context_window,


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_agent_card]] | downstream | 0.46 |
| [[bld_knowledge_card_agent_card]] | upstream | 0.46 |
| [[bld_memory_agent_card]] | downstream | 0.45 |
| [[agent-card-builder]] | downstream | 0.44 |
| [[p11_qg_agent-card]] | downstream | 0.39 |
| [[bld_architecture_agent_card]] | downstream | 0.37 |
| [[p03_sp_agent_card_builder]] | related | 0.35 |
| [[p01_kc_agent_card]] | downstream | 0.32 |
| [[p12_wf_stella_dispatch]] | downstream | 0.31 |
| [[bld_collaboration_model_card]] | upstream | 0.30 |
