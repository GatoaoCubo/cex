---
id: p01_kc_claude_agent_sdk_patterns
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Claude Agent SDK — Handoffs, Guardrails, Tracing, Structured Output"
version: 2.0.0
created: 2026-02-23
updated: 2026-03-25
author: builder_agent
domain: architecture
quality: 9.1
tags: [agent-sdk, multi-agent, handoffs, guardrails, orchestration, claude]
tldr: "Agent SDK: agent(instructions+tools+model) + handoffs(triage/pipeline/parallel) + guardrails(input/output) + tracing + structured output"
when_to_use: "Build multi-agent systems, implement handoffs between agents, or add guardrails in production"
keywords: [agent_sdk, handoff, guardrail, tracing, multi_agent]
long_tails:
  - "How to implement handoffs between agents in the Claude Agent SDK"
  - "What multi-agent orchestration patterns exist"
axioms:
  - "NEVER create circular handoffs without exit condition"
  - "ALWAYS implement tracing in production"
linked_artifacts:
  primary: p01_kc_mcp_tool_infrastructure
  related: [p01_kc_context_parallelization]
density_score: null
data_source: "https://github.com/anthropics/anthropic-cookbook"
related:
  - p01_kc_agent
  - bld_collaboration_agent
  - agent-builder
  - atom_03_openai_agents_sdk
  - bld_architecture_agent
  - bld_knowledge_card_agent
  - p03_pt_sdk_agent_builder
  - p03_ins_mental_model
  - p01_kc_handoff_protocol
  - bld_instruction_agent
---

## Summary

Agent SDK: framework for agents in production. Agent = instructions + tools + model. Orchestration via handoffs (transfers complete context). Guardrails validate input/output. Tracing exports decisions for observability.

## Spec

| Component | Function | Detail |
|-----------|----------|--------|
| Agent | Executor unit | name + instructions + model + tools + handoffs |
| Handoff | Delegation | Transfers complete conversation to another agent |
| Guardrail | Validation | Input (pre-process) and output (post-process) |
| Tracing | Observability | Decisions, tool calls, latency per step |
| Structured Output | Typing | Agent returns typed object, not free text |

## Patterns

| Trigger | Action |
|---------|--------|
| Multiple distinct domains | Triage: router agent delegates to specialists |
| Sequential dependent tasks | Pipeline: A -> B -> C with chained context |
| Independent tasks | Parallel: N simultaneous agents |
| Complex coordination | Hierarchical: manager coordinates workers |
| Agent returns structured data | Use output_type=TypedClass |

## Anti-Patterns

- Circular handoffs without exit condition (infinite loop)
- 10+ handoff options in one agent (LLM cannot choose)
- User-facing agent without guardrails (risk of inadequate output)
- Production without tracing (blind debug)
- Single agent with 20+ tools (use specialists)

## Code

<!-- lang: python | purpose: multi-agent handoff pattern -->
```python
stella = Agent(name="stella", instructions="Orchestrate", handoffs=[shaka, edison])
shaka = Agent(name="shaka", instructions="Research", tools=[web_search, scrape])
edison = Agent(name="edison", instructions="Build", tools=[write_code, test])
```

<!-- lang: python | purpose: structured output -->
```python
agent = Agent(name="extractor", output_type=ProductData)
result = agent.run("Extract product info from this listing")
# result.name, result.price, result.category — typed, not free text
```


<!-- lang: python | purpose: input guardrail -->
```python
@input_guardrail
def check_pii(input: str) -> GuardrailResult:
    if contains_pii(input): return GuardrailResult(block=True, reason="PII detected")
    return GuardrailResult(block=False)

agent = Agent(name="safe", input_guardrails=[check_pii])
```
## References

- external: https://github.com/anthropics/anthropic-cookbook
- external: https://docs.anthropic.com/en/docs/agents-and-tools
- deepens: p01_kc_mcp_tool_infrastructure (tool scaling patterns)
- deepens: p01_kc_context_parallelization (token reduction via workers)
- deepens: /skill agent_orchestration (como orquestrar — a ser criada)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_agent]] | sibling | 0.39 |
| [[bld_collaboration_agent]] | downstream | 0.38 |
| [[agent-builder]] | downstream | 0.36 |
| [[atom_03_openai_agents_sdk]] | sibling | 0.35 |
| [[bld_architecture_agent]] | downstream | 0.32 |
| [[bld_knowledge_card_agent]] | sibling | 0.29 |
| [[p03_pt_sdk_agent_builder]] | downstream | 0.26 |
| [[p03_ins_mental_model]] | downstream | 0.26 |
| [[p01_kc_handoff_protocol]] | sibling | 0.25 |
| [[bld_instruction_agent]] | downstream | 0.25 |
