---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary and position of runtime_state in the CEX fractal
---

# Architecture: runtime_state in the CEX

## Boundary
runtime_state EH: estado mental variavel que um agente acumula durante runtime — routing decisions, priority shifts, tool preferences.

runtime_state NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| mental_model (P02) | mental_model eh blueprint ESTATICO de design-time. runtime_state eh DINAMICO em runtime. | P02 mental_model |
| session_state (P10) | session_state eh snapshot EFEMERO (reset a cada sessao). runtime_state ACUMULA entre tasks. | P10 session_state |
| learning_record (P10) | learning_record eh registro PERSISTENTE entre sessoes. runtime_state vive durante a sessao atual. | P10 learning_record |
| axiom (P10) | axiom eh regra IMUTAVEL fundamental. runtime_state eh VARIAVEL e adaptavel. | P10 axiom |
| brain_index (P10) | brain_index eh INDICE de busca (BM25, FAISS). runtime_state eh ESTADO mental de decisao. | P10 brain_index |

Regra: "quais routing rules, priorities, e heuristics este agente usa AGORA em runtime?" -> runtime_state.

## Position in State Flow

```text
mental_model (design-time blueprint) -> runtime_state (runtime decisions) -> session_state (ephemeral snapshot)
```

runtime_state is RUNTIME LAYER — accumulates decisions and adaptations during execution.

## Dependency Graph

```text
runtime_state <--initialized_from-- mental_model (P02 provides design-time blueprint)
runtime_state <--informed_by-- learning_record (P10 provides past learnings)
runtime_state --persists_to--> session_state (P10 ephemeral snapshot on save)
runtime_state --queried_by--> brain_index (P10 uses state for search context)
runtime_state --independent-- knowledge_card, signal, permission
```

## Fractal Position
Pillar: P10 (Memory — what the system remembers)
Function: INJECT
Scale: L1 (runtime artifact)
runtime_state is unique in P10 because it bridges design-time identity (P02) and ephemeral snapshots (session_state) — it is the LIVE working memory of an agent.
