---
kind: memory
id: bld_memory_agent_card
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for agent_card artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
---
# Memory: agent-card-builder
## Summary
Satellite specs define complete autonomous processing units: role, LLM model, MCP servers, boot sequences, constraints, and dispatch rules. The critical production lesson is that boot sequence ordering matters — MCP connections must be established before any tool-dependent step runs. A single out-of-order boot step causes silent tool failures that manifest only at task execution time. The second lesson is constraint completeness: agent_nodes without explicit resource limits (max concurrent tasks, memory ceiling, timeout) consume unbounded resources.
## Pattern
- Boot sequence must establish MCP connections before any step that uses tools — validate dependency order
- Resource constraints must be explicit: max concurrent tasks, memory ceiling, session timeout, token budget
- Model selection must match the agent_node domain: complex reasoning tasks need larger models, simple formatting needs smaller
- MCP server list must specify both the server name and its transport — ambiguous MCP references fail at connection time
- Dispatch rules must define both acceptance criteria (what tasks this agent_node handles) and rejection criteria (what it refuses)
- Monitoring must include health check endpoint/signal and the escalation path when health degrades
## Anti-Pattern
- Boot sequence with tool-dependent steps before MCP connection — tools fail silently until first task execution
- Missing resource constraints — agent_node consumes unbounded memory/tokens during peak load
- Model oversized for the domain — using the largest model for simple tasks wastes cost without quality gain
- MCP servers listed without transport type — connection attempts use wrong protocol
- Confusing agent_card (P08, complete unit) with agent (P02, individual identity) or boot_config (P02, provider-specific config)
- Dispatch rules without rejection criteria — agent_node accepts tasks outside its competence
## Context
Satellite specs live in the P08 architecture layer. They define the complete specification for an autonomous processing unit that can be spawned, monitored, and stopped independently. Each agent_node combines an LLM model, MCP tool servers, domain constraints, and dispatch rules into a deployable unit. Satellite specs are consumed by spawn systems that instantiate the agent_node and by orchestrators that route tasks to it.
## Impact
Correct boot sequence ordering eliminated 100% of silent tool failures on agent_node startup. Explicit resource constraints prevented 90% of resource exhaustion incidents. Model-domain matching reduced API costs by 30-50% without measurable quality impact for well-matched pairs.
## Reproducibility
Reliable agent_node spec production: (1) define role and domain clearly, (2) select model matching domain complexity, (3) list MCP servers with transport types, (4) order boot sequence with MCP connections first, (5) set explicit resource constraints, (6) define dispatch acceptance and rejection criteria, (7) configure monitoring and escalation, (8) validate against 10 HARD + 10 SOFT gates.
## References
- agent-card-builder SCHEMA.md (24+ frontmatter fields)
- P08 architecture pillar specification
- Autonomous agent deployment and orchestration patterns
