---
id: p01_kc_cex_function_collaborate
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Function COLLABORATE — Multi-Agent Coordination and Handoffs"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, llm-function, collaborate, handoff, signal, crew, multi-agent]
tldr: "COLLABORATE coordinates agents via 3 types (crew/signal/handoff) — baton pass between autonomous entities"
when_to_use: "Understand how agents coordinate with each other and the boundary between COLLABORATE (active agent) and CALL (passive tool)"
keywords: [collaborate, crew, signal, handoff, multi_agent, coordination]
long_tails:
  - "What is the difference between COLLABORATE and CALL in CEX"
  - "What are the 3 multi-agent coordination types in CEX"
axioms:
  - "ALWAYS use structured handoff (context + criteria + format) when delegating"
  - "NEVER treat multi-agent coordination as a special case of CALL"
linked_artifacts:
  primary: p01_kc_cex_function_govern
  related: [p01_kc_cex_function_call, p01_kc_cex_function_become]
density_score: null
data_source: "https://arxiv.org/abs/2309.07864"
related:
  - p01_kc_cex_lp12_orchestration
  - p01_kc_cex_llm_function_concept
  - bld_collaboration_handoff_protocol
  - p01_kc_lp12_orchestration
  - handoff-protocol-builder
  - handoff-builder
  - bld_collaboration_handoff
  - p01_kc_cex_pipeline_execution
  - signal-builder
  - bld_collaboration_signal
---

## Summary

COLLABORATE coordinates communication and work between autonomous agents. With 3 types (4% of CEX), it is the smallest function but architecturally critical — like in a relay race, the baton pass determines the result. Fundamental boundary with CALL: tools (CALL) are passive, stateless, without identity; agents (COLLABORATE) have goals, persona, memory, and autonomy. AutoGen (Microsoft), CrewAI, MetaGPT, and CAMEL confirm: multi-agent coordination is a first principle, not an extension of function calling. COLLABORATE closes the CEX pipeline cycle and connects back to BECOME (new cycle).

## Spec

| Type | LP | Function | Detail |
|------|-----|----------|--------|
| crew | P12 | Agent team | Shared objective+state, coordination |
| signal | P12 | Inter-agent message | Status, result, completion (async) |
| handoff | P12 | Formal delegation | Context+constraints+criteria+format |

crew: team with distinct roles and coordination protocol.
signal: asynchronous notification (does not delegate, only communicates).
handoff: complete delegation with transferred context.
3 fundamental differences between CALL and COLLABORATE:
Identity — tools have no goals; agents have goals and bias.
State — tools are stateless; agents are stateful.
Autonomy — tools execute exactly; agents interpret.
ChatDev (Qian 2023): entire software company with agents in
professional roles, communicating via structured documents.
Xi et al. (2023): multi-agent systems as a section separate from tools.
COLLABORATE closes the CEX pipeline: after GOVERN, the agent signals
completion or delegates next step, connecting to BECOME (new cycle).
AutoGen GroupChat, CrewAI Crew, MetaGPT, and CAMEL confirm:
multi-agent coordination is a dedicated type, not function calling.

## Patterns

| Trigger | Action |
|---------|--------|
| Task requires multiple roles | crew with shared objective |
| Asynchronous communication between agents | signal (status/result) |
| Task delegation to another agent | handoff with complete context |
| Partial result for next agent | chained handoff (pipeline) |
| Completion signaling to orchestrator | completion signal |
| Multiple agents working in parallel | crew with coordination |
| Full cycle completed | signal + handoff to BECOME |

## Code

<!-- lang: python | purpose: multi-agent collaboration patterns -->
```python
# handoff: delegacao formal com contexto completo
handoff = Handoff(
    from_agent="stella", to_agent="edison",
    context={"task": "Build KC", "seeds": ["cex", "produce"]},
    criteria={"quality": ">= 9.0", "format": "meta_kc"},
)
edison.execute(handoff)  # contexto transferido, nao perdido

# signal: notificacao assincrona de completude
signal = Signal(agent="edison", status="complete", score=9.2)
stella.receive(signal)  # orquestrador decide proximo passo

# crew: equipe com papeis e coordenacao
crew = Crew(agents=[shaka, lily, edison], goal="Launch product")
crew.run(protocol="parallel")  # cada agente com papel distinto
```

## Anti-Patterns

- Treating coordination as extension of function calling (they are distinct)
- Handoff without context (receiving agent loses critical information)
- Signal without structured schema (fragile parsing)
- Crew without coordination protocol (agents conflict)
- Delegating to agent when simple tool suffices (overhead)
- Synchronous coordination when asynchronous is sufficient (bottleneck)

## References

- source: https://arxiv.org/abs/2309.07864
- source: https://arxiv.org/abs/2308.00352
- related: p01_kc_cex_function_call
- related: p01_kc_cex_function_govern
- related: p01_kc_cex_function_become

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_lp12_orchestration]] | sibling | 0.44 |
| [[p01_kc_cex_llm_function_concept]] | sibling | 0.31 |
| [[bld_collaboration_handoff_protocol]] | downstream | 0.30 |
| [[p01_kc_lp12_orchestration]] | sibling | 0.26 |
| [[handoff-protocol-builder]] | downstream | 0.25 |
| [[handoff-builder]] | downstream | 0.25 |
| [[bld_collaboration_handoff]] | downstream | 0.25 |
| [[p01_kc_cex_pipeline_execution]] | sibling | 0.25 |
| [[signal-builder]] | downstream | 0.25 |
| [[bld_collaboration_signal]] | downstream | 0.23 |
