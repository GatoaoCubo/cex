---
id: p01_kc_crewai_patterns
kind: knowledge_card
type: domain
pillar: P01
title: "CrewAI Patterns — Agent, Task, Crew, Process, Memory, Delegation"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: crewai
origin: src_framework_taxonomy
quality: 9.1
tags: [crewai, agent, task, crew, process, delegation, multi-agent]
tldr: "CrewAI orchestrates multi-agent collaboration via Crew(agents, tasks, process) with scoped memory, delegation, and guardrails"
when_to_use: "Building or mapping CrewAI constructs to CEX kinds"
keywords: [crewai, crew, agent, task, process, memory, delegation, flow]
long_tails:
  - "How does CrewAI Agent/Task/Crew map to CEX agent and director kinds"
  - "Which CrewAI concepts map to CEX guardrail and memory_scope kinds"
axioms:
  - "Agent = role + goal + backstory + tools; Task = description + expected_output + agent"
  - "Crew is the director — it composes agents and tasks into a coordinated execution"
linked_artifacts:
  primary: null
  related: [p01_kc_cex_taxonomy, p01_kc_langchain_patterns, p01_kc_dspy_patterns]
feeds_kinds:
  - agent           # Agent (role/goal/backstory), BaseAgent
  - director        # Crew (composes agents + tasks), Process
  - function_def    # BaseTool (custom tools for agents)
  - memory_scope    # Memory, MemoryScope (LLM-inferred scopes)
  - workflow        # Flow (event-driven with built-in state)
  - action_prompt   # Task (specific assignment with expected_output)
  - guardrail       # guardrail param on Task
  - hook            # @before_kickoff, @after_kickoff decorators
  - handoff         # allow_delegation between agents
  - output_validator # TaskOutput (raw/json/pydantic validation)
  - signal          # CrewStreamingOutput (real-time progress)
density_score: 0.92
related:
  - atom_08_crewai
  - bld_knowledge_card_crew_template
  - bld_knowledge_card_role_assignment
  - role-assignment-builder
  - p01_kc_agent
  - crew-template-builder
  - bld_collaboration_agent
  - kc_llm_agent_frameworks
  - cex_llm_vocabulary_whitepaper
  - p01_kc_action_prompt
---

# CrewAI Patterns

## Quick Reference
```yaml
topic: CrewAI Core (crewai)
scope: Multi-agent orchestration, task delegation, scoped memory, flows
source: docs.crewai.com
criticality: high
```

## Key Concepts

| Concept | Module | CEX Kind | Role |
|---------|--------|----------|------|
| `Agent` | `crewai` | agent | Autonomous unit: role + goal + backstory + tools |
| `Task` | `crewai` | action_prompt | Specific assignment with expected_output |
| `Crew` | `crewai` | director | Orchestrates agents + tasks as collaborative group |
| `Process` | `crewai` | director | Execution mode: sequential or hierarchical |
| `Memory` | `crewai` | memory_scope | Unified memory (LLM-inferred scopes) |
| `MemoryScope` | `crewai` | memory_scope | Scoped subtree view of Memory |
| `Flow` | `crewai.flow.flow` | workflow | Event-driven flow with built-in state |
| `BaseTool` | `crewai.tools` | function_def | Base class for custom tools |
| `TaskOutput` | `crewai` | output_validator | Structured result (raw/json/pydantic) |
| `CrewStreamingOutput` | `crewai` | signal | Real-time streaming output chunks |
| `AgentPlanner` | `crewai` | agent | Pre-task planning LLM component |
| `guardrail` param | `crewai.Task` | guardrail | Validation function on task output |
| `allow_delegation` | `crewai.Agent` | handoff | Agent can delegate to peers |
| `@before_kickoff` | `crewai.project` | hook | Pre-execution hook |
| `@after_kickoff` | `crewai.project` | hook | Post-execution hook |
| `@start()` | `crewai.flow.flow` | workflow | Flow entry point |
| `@listen()` | `crewai.flow.flow` | workflow | Flow event listener |

## Patterns

| Trigger | Action |
|---------|--------|
| Define specialist agent | `Agent(role="...", goal="...", backstory="...", tools=[...])` |
| Create task assignment | `Task(description="...", expected_output="...", agent=agent)` |
| Orchestrate team | `Crew(agents=[...], tasks=[...], process=Process.sequential)` |
| Enable delegation | `Agent(allow_delegation=True)` — agent can hand off to peers |
| Add guardrail | `Task(guardrail=my_validator_fn)` — validates before accepting output |
| Structured output | `Task(output_pydantic=MyModel)` — forces Pydantic validation |
| Event-driven flow | `Flow` with `@start()` entry + `@listen()` reactions |
| Hierarchical process | `Crew(process=Process.hierarchical, manager_agent=mgr)` |

## Anti-Patterns

- Omitting `expected_output` on Task — agent has no success criteria
- Using `Process.hierarchical` without `manager_agent` — falls back to default LLM
- Giving all agents `allow_delegation=True` — creates delegation loops
- Ignoring `Memory` — agents lose cross-task context
- Not using `@before_kickoff` for input validation — bad data propagates

## CEX Mapping

```text
[agent + function_def] -> [action_prompt + guardrail] -> [director (Crew + Process)]
    -> [memory_scope] -> [output_validator + signal] -> [handoff / hook]
```

## References

- source: docs.crewai.com/concepts/
- related: p01_kc_cex_taxonomy

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[atom_08_crewai]] | sibling | 0.54 |
| [[bld_knowledge_card_crew_template]] | sibling | 0.39 |
| [[bld_knowledge_card_role_assignment]] | sibling | 0.31 |
| [[role-assignment-builder]] | downstream | 0.31 |
| [[p01_kc_agent]] | sibling | 0.28 |
| [[crew-template-builder]] | downstream | 0.26 |
| [[bld_collaboration_agent]] | downstream | 0.26 |
| [[kc_llm_agent_frameworks]] | sibling | 0.24 |
| [[cex_llm_vocabulary_whitepaper]] | sibling | 0.24 |
| [[p01_kc_action_prompt]] | sibling | 0.23 |
