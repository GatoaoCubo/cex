---
id: p01_kc_cex_function_collaborate
kind: knowledge_card
pillar: P01
title: "CEX Function COLLABORATE — Multi-Agent Coordination and Handoffs"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, llm-function, collaborate, handoff, signal, crew, multi-agent]
tldr: "COLLABORATE coordena agentes via 3 tipos (crew/signal/handoff) — passagem de bastao entre entidades autonomas"
when_to_use: "Entender como agentes coordenam entre si e a fronteira entre COLLABORATE (agente ativo) e CALL (ferramenta passiva)"
keywords: [collaborate, crew, signal, handoff, multi_agent, coordination]
long_tails:
  - "Qual a diferenca entre COLLABORATE e CALL no CEX"
  - "Quais os 3 tipos de coordenacao multi-agente no CEX"
axioms:
  - "SEMPRE usar handoff estruturado (contexto + criterios + formato) ao delegar"
  - "NUNCA tratar coordenacao multi-agente como caso especial de CALL"
linked_artifacts:
  primary: p01_kc_cex_function_govern
  related: [p01_kc_cex_function_call, p01_kc_cex_function_become]
density_score: null
data_source: "https://arxiv.org/abs/2309.07864"
---

## Summary

COLLABORATE coordena comunicacao e trabalho entre agentes autonomos. Com 3 tipos (4% do CEX), eh a menor funcao mas arquiteturalmente critica — como na corrida de revezamento, a passagem do bastao determina o resultado. Fronteira fundamental com CALL: ferramentas (CALL) sao passivas, stateless, sem identidade; agentes (COLLABORATE) tem goals, persona, memoria e autonomia. AutoGen (Microsoft), CrewAI, MetaGPT e CAMEL confirmam: coordenacao multi-agente eh primeiro principio, nao extensao de function calling. COLLABORATE fecha o ciclo do pipeline CEX e conecta de volta a BECOME (novo ciclo).

## Spec

| Tipo | LP | Funcao | Detalhe |
|------|-----|--------|---------|
| crew | P12 | Equipe de agentes | Objetivo+estado compartilhado, coordenacao |
| signal | P12 | Mensagem inter-agente | Status, resultado, completude (async) |
| handoff | P12 | Delegacao formal | Contexto+restricoes+criterios+formato |

crew: equipe com papeis distintos e protocolo de coordenacao.
signal: notificacao assincrona (nao delega, apenas comunica).
handoff: delegacao completa com contexto transferido.
3 diferencas fundamentais entre CALL e COLLABORATE:
Identidade — ferramentas nao tem goals; agentes tem goals e bias.
Estado — ferramentas sao stateless; agentes sao stateful.
Autonomia — ferramentas executam exatamente; agentes interpretam.
ChatDev (Qian 2023): empresa inteira de software com agentes em
papeis profissionais, comunicando via documentos estruturados.
Xi et al. (2023): multi-agent systems como secao separada de tools.
COLLABORATE fecha o pipeline CEX: apos GOVERN, o agente sinaliza
completude ou delega proximo passo, conectando a BECOME (novo ciclo).
AutoGen GroupChat, CrewAI Crew, MetaGPT e CAMEL confirmam:
coordenacao multi-agente eh tipo dedicado, nao function calling.

## Patterns

| Trigger | Action |
|---------|--------|
| Tarefa requer multiplos papeis | crew com objetivo compartilhado |
| Comunicacao assincrona entre agentes | signal (status/resultado) |
| Delegacao de tarefa para outro agente | handoff com contexto completo |
| Resultado parcial para proximo agente | handoff encadeado (pipeline) |
| Sinalizacao de conclusao para orquestrador | signal de completude |
| Multiplos agentes trabalhando em paralelo | crew com coordenacao |
| Ciclo completo finalizado | signal + handoff para BECOME |

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

- Tratar coordenacao como extensao de function calling (sao distintos)
- Handoff sem contexto (agente receptor perde informacao critica)
- Signal sem schema estruturado (parsing fragil)
- Crew sem protocolo de coordenacao (agentes conflitam)
- Delegar para agente quando ferramenta simples basta (overhead)
- Coordenacao sincrona quando assincrona eh suficiente (bottleneck)

## References

- source: https://arxiv.org/abs/2309.07864
- source: https://arxiv.org/abs/2308.00352
- related: p01_kc_cex_function_call
- related: p01_kc_cex_function_govern
- related: p01_kc_cex_function_become
