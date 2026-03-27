---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of runtime_rule in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: runtime_rule in the CEX

## Boundary
runtime_rule EH: regra de comportamento tecnico em runtime — timeouts, retries, rate limits,
circuit breakers, concurrency limits. Define PARAMETROS NUMERICOS CONCRETOS com unidades.
Segue stability patterns de Michael Nygard (Release It! 2007).

runtime_rule NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| lifecycle_rule | lifecycle_rule gerencia ciclo de vida de artifacts (archive, promote); runtime_rule governa operacoes | P11 lifecycle_rule |
| law | law eh inviolavel e permanente; runtime_rule eh configuravel e ajustavel | P08 law |
| guardrail | guardrail eh safety boundary (previne dano); runtime_rule eh parametro operacional | P11 guardrail |
| env_config | env_config define variaveis genericas; runtime_rule define comportamento numerico | P09 env_config |
| feature_flag | feature_flag eh toggle on/off logico; runtime_rule eh parametro numerico | P09 feature_flag |
| path_config | path_config define caminhos de filesystem; runtime_rule define comportamento | P09 path_config |
| permission | permission controla acesso (read/write); runtime_rule define limites operacionais | P09 permission |

Regra: "quais TIMEOUTS, RETRIES e LIMITES governam esta operacao em runtime?" -> runtime_rule.

## Position in Config Flow

```text
runtime_rule (P09) --> agent (P02) --> runtime behavior
       |                    |
  threshold_eval       operation_exec
       |
  fallback_trigger --> error_handling
```

runtime_rule is OPERATIONAL BEHAVIOR LAYER — applied at every operation boundary.

## Dependency Graph

```text
runtime_rule --consumed_by--> agent (P02) (agents apply timeout/retry rules)
runtime_rule --consumed_by--> connector (P04) (connectors use retry + timeout)
runtime_rule --consumed_by--> client (P04) (clients enforce rate limits)
runtime_rule --consumed_by--> daemon (P04) (daemons respect concurrency limits)
runtime_rule --consumed_by--> skill (P04) (skills apply per-phase timeouts)
runtime_rule <--receives-- guardrail (P11) (safety rules constrain max values)
runtime_rule --independent-- env_config, path_config, feature_flag, permission
```

## Fractal Position
Pillar: P09 (Config — HOW the system configures)
Function: GOVERN (runtime_rule governs operational behavior boundaries)
Layer: runtime (rules evaluated at every operation boundary)
Scale: L0 (per-operation — one rule per operation type, granular)
runtime_rule is EXTENSION (not core_24): system can run with defaults, but explicit rules prevent incidents.
