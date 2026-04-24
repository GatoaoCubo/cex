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
when_to_use: "Construir multi-agent systems, implementar handoffs entre agentes, ou adicionar guardrails em producao"
keywords: [agent_sdk, handoff, guardrail, tracing, multi_agent]
long_tails:
  - "Como implementar handoffs entre agentes no Claude Agent SDK"
  - "Quais patterns de orquestracao multi-agent existem"
axioms:
  - "NUNCA criar handoffs circulares sem exit condition"
  - "SEMPRE implementar tracing em producao"
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

Agent SDK: framework para agentes em producao. Agent = instructions + tools + model. Orquestracao via handoffs (transfere contexto completo). Guardrails validam input/output. Tracing exporta decisoes para observabilidade.

## Spec

| Componente | Funcao | Detalhe |
|------------|--------|---------|
| Agent | Unidade executora | name + instructions + model + tools + handoffs |
| Handoff | Delegacao | Transfere conversa completa para outro agent |
| Guardrail | Validacao | Input (pre-process) e output (pos-process) |
| Tracing | Observabilidade | Decisoes, tool calls, latencia por step |
| Structured Output | Tipagem | Agent retorna typed object, nao free text |

## Patterns

| Trigger | Action |
|---------|--------|
| Multiplos dominios distintos | Triage: router agent delega para especialistas |
| Tarefas sequenciais dependentes | Pipeline: A -> B -> C com contexto encadeado |
| Tarefas independentes | Parallel: N agents simultaneos |
| Coordenacao complexa | Hierarchical: manager coordena workers |
| Agent retorna dados estruturados | Usar output_type=TypedClass |

## Anti-Patterns

- Handoffs circulares sem exit condition (loop infinito)
- 10+ handoff options num agent (LLM nao consegue escolher)
- Agent user-facing sem guardrails (risco de output inadequado)
- Producao sem tracing (debug cego)
- Agent unico com 20+ tools (usar especialistas)

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
