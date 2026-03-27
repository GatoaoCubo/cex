---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary and position of permission in the CEX fractal
---

# Architecture: permission in the CEX

## Boundary
permission EH: regra de controle de acesso que define quem pode ler/escrever/executar recursos.

permission NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| env_config | env_config define VARIAVEIS de ambiente. permission define ACESSO a recursos. | P09 env_config |
| path_config | path_config define CAMINHOS do filesystem. permission define quem pode ACESSAR caminhos. | P09 path_config |
| feature_flag | feature_flag liga/desliga FEATURES. permission controla quem pode ACESSAR. | P09 feature_flag |
| runtime_rule | runtime_rule define TIMEOUTS e retries. permission define READ/WRITE/EXECUTE. | P09 runtime_rule |
| guardrail | guardrail previne DANO (safety). permission controla ACESSO (who can do what). | P11 guardrail |
| law | law define regra OPERACIONAL arquitetural. permission define regra de ACESSO granular. | P08 law |

Regra: "quem pode ler/escrever/executar este recurso?" -> permission.

## Position in Access Flow

```text
law (operational rule) -> guardrail (safety boundary) -> permission (access control) -> runtime check (enforcement)
```

permission is ACCESS LAYER — controls who can read/write/execute specific resources.

## Dependency Graph

```text
permission <--constrained_by-- law (P08 provides operational principles)
permission <--complemented_by-- guardrail (P11 provides safety boundaries)
permission --enforced_by--> hook (P04 implements access checks)
permission --audited_by--> quality_gate (P11 tracks compliance)
permission --configures--> env_config (P09 may restrict env access)
permission --independent-- knowledge_card, signal, scoring_rubric
```

## Fractal Position
Pillar: P09 (Config — how to configure)
Function: GOVERN
Scale: L0 (governance artifact)
permission is unique in P09 because it is in the GOVERNANCE layer (not runtime) — it restricts access rather than configuring behavior.
