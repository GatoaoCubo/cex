# CEX LLM Pipeline — As 8 Funcoes Fundamentais

**Status**: LEI | **Versao**: 1.0.0 | **Data**: 2026-03-26

---

## O Que Eh Isso

TODO sistema LLM — de um prompt simples a um satellite completo —
executa as mesmas 8 funcoes na mesma ordem. A diferenca entre um
prompt e um agente nao eh de natureza. Eh de COMPLETUDE.

```
INPUT
  |
  v
1. BECOME      — Quem eu sou? (identidade, persona, regras)
  |
  v
2. INJECT      — O que eu sei? (contexto, knowledge, RAG)
  |
  v
3. REASON      — Como penso? (CoT, ReAct, planning)
  |
  v
4. CALL        — Que tools uso? (APIs, MCPs, CLIs)
  |
  v
5. PRODUCE     — O que gero? (texto, codigo, dados)
  |
  v
6. CONSTRAIN   — Esta no formato? (schema, grammar, template)
  |
  v
7. GOVERN      — Passou no quality gate? (eval, benchmark, score)
  |
  v
8. COLLABORATE — Quem recebe? (signal, handoff, next agent)
  |
  v
OUTPUT
```

---

## As 8 Funcoes

| # | Funcao | Verbo | O Que Faz | Types Exemplo | % do CEX |
|---|--------|-------|-----------|---------------|----------|
| 1 | **BECOME** | Ser | Configura identidade antes de tudo | agent, system_prompt, persona, mental_model | 8% (6 tipos) |
| 2 | **INJECT** | Saber | Fornece contexto e conhecimento | knowledge_card, rag_source, few_shot, context_doc | 21% (16 tipos) |
| 3 | **REASON** | Pensar | Raciocina, planeja, decompoe | chain_of_thought, react, planner, router | 9% (7 tipos) |
| 4 | **CALL** | Fazer | Invoca ferramentas externas | skill, mcp_server, cli_tool, connector | 10% (8 tipos) |
| 5 | **PRODUCE** | Gerar | Produz output final | completion, chain, workflow, meta_prompt | 6% (5 tipos) |
| 6 | **CONSTRAIN** | Restringir | Valida contra schemas e regras | grammar, law, guardrail, template | 14% (11 tipos) |
| 7 | **GOVERN** | Avaliar | Quality gates, evals, feedback | quality_gate, benchmark, scoring_rubric | 28% (22 tipos) |
| 8 | **COLLABORATE** | Coordenar | Sinaliza, delega, proximo agente | crew, signal, handoff | 4% (3 tipos) |

**Total**: 78 kinds distribuidos em 8 funcoes.

---

## Niveis de Completude

| Sistema | Funcoes Executadas | Exemplo |
|---------|-------------------|---------|
| Prompt simples | 1-2 (BECOME implicito + PRODUCE) | ChatGPT vanilla |
| Prompt + RAG | 1-3 (+ INJECT) | Perplexity |
| Agente | 4-5 (+ REASON + CALL) | CrewAI agent |
| Agente + QA | 6-7 (+ CONSTRAIN + GOVERN) | Agente com evals |
| Satellite completo | 8/8 (pipeline full) | CEX satellite |

---

## Relacao com os 12 pillars

As 8 funcoes sao o que o LLM FAZ (pipeline de execucao).
Os 12 pillars sao como ORGANIZAMOS os artefatos (filesystem).

| Funcao | pillars que alimentam |
|--------|-------------------|
| BECOME | P02 Model, P03 Prompt |
| INJECT | P01 Knowledge, P10 Memory |
| REASON | P03 Prompt |
| CALL | P04 Tools |
| PRODUCE | P03 Prompt, P05 Output |
| CONSTRAIN | P06 Schema, P08 Architecture |
| GOVERN | P07 Evals, P09 Config, P11 Feedback |
| COLLABORATE | P12 Orchestration |

Os 12 pillars cobrem os 8 funcoes. Nenhum pillar eh orfao.

---

## Regras Inviolaveis

1. BECOME antes de tudo (identidade precede contexto)
2. INJECT antes de REASON (contexto precede raciocinio)
3. REASON antes de CALL (planejamento precede acao)
4. PRODUCE antes de CONSTRAIN (gerar antes de validar)
5. GOVERN antes de COLLABORATE (qualidade antes de propagar)
6. NUNCA tratar funcoes como pastas (sao pipeline, nao categorias)
7. NUNCA pular GOVERN (sem quality gate = degradacao silenciosa)
8. A diferenca entre sistemas eh COMPLETUDE, nao natureza

---

## KCs Detalhados (1 por funcao)

| Funcao | KC | Path |
|--------|----|------|
| BECOME | p01_kc_cex_function_become | P01_knowledge/examples/ |
| INJECT | p01_kc_cex_function_inject | P01_knowledge/examples/ |
| REASON | p01_kc_cex_function_reason | P01_knowledge/examples/ |
| CALL | p01_kc_cex_function_call | P01_knowledge/examples/ |
| PRODUCE | p01_kc_cex_function_produce | P01_knowledge/examples/ |
| CONSTRAIN | p01_kc_cex_function_constrain | P01_knowledge/examples/ |
| GOVERN | p01_kc_cex_function_govern | P01_knowledge/examples/ |
| COLLABORATE | p01_kc_cex_function_collaborate | P01_knowledge/examples/ |

---

## Origem

Descoberta empirica. Hipotese inicial: 6 funcoes. Expandiu para 8
quando REASON e COLLABORATE apareceram com artefatos dedicados em
12/12 frameworks auditados (DSPy, LangChain, CrewAI, AutoGen,
Haystack, LlamaIndex, Guidance, Instructor, Outlines, LMQL, LangGraph,
Semantic Kernel).

Cobertura: 91% dos artefatos da industria (70% direto + 21% parcial).

---

*LLM_PIPELINE.md — Lei do CEX. As 8 funcoes sao o DNA de todo sistema LLM.*