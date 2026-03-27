---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of session_state in the CEX fractal
pattern: every builder must know where its output fits and what it connects to
---

# Architecture: session_state in the CEX

## Boundary
`session_state` EH: snapshot efemero de sessao de um agente, capturando estado
momentaneo de execucao, consumo de recursos, e pontos de recovery.

`session_state` NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|--------------|
| runtime_state | runtime_state persiste entre sessoes e acumula decisoes de routing | P10 runtime_state |
| learning_record | learning_record acumula aprendizado (padroes, anti-padroes, scores) ao longo do tempo | P10 learning_record |
| brain_index | brain_index configura indice de busca (BM25, FAISS), nao captura estado de sessao | P10 brain_index |
| axiom | axiom eh regra fundamental imutavel, nao estado efemero | P10 axiom |
| mental_model | mental_model define routing/decisoes persistentes de um agente | P10 mental_model |

Regra:
- "qual o estado desta sessao agora?" -> `session_state`
- "qual estado persiste entre sessoes?" -> `runtime_state`
- "o que o agente aprendeu?" -> `learning_record`

## Position in Runtime Flow

```text
agent boot -> session start -> session_state snapshots -> session end -> learning_record extraction
```

`session_state` sits during active execution, between boot and learning extraction.
It is observation, not accumulation.

## Dependency Graph

```text
session_state <--receives-- (none — built independently from current session context)
session_state --produces_for--> learning_record (P10) — post-session extraction
session_state --produces_for--> runtime_state (P10) — may update persistent state
session_state --produces_for--> signal (P12) — status events reference session data

session_state --independent-- brain_index (P10)
session_state --independent-- axiom (P10)
session_state --independent-- workflow (P05)
session_state --independent-- dispatch_rule (P06)

monitors/STELLA --> consumes --> session_state
recovery_tools  --> consumes --> session_state
```

## Fractal Position
Pillar: P10 (Memory - "what it remembers")
Function: INJECT
Scale: L0 runtime snapshot
Ephemeral capture artifact in P10: shorter-lived than runtime_state, simpler than learning_record.

session_state is SNAPSHOT LAYER — ephemeral execution state only.
