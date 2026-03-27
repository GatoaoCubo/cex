---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of feature_flag in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: feature_flag in the CEX

## Boundary
feature_flag EH: definicao de toggle on/off para features com rollout gradual. Controla
SE uma feature esta ativa, PARA QUEM, e COM QUE estrategia de rollout. Segue feature
toggle patterns (Fowler 2017): release, experiment, ops, permission.

feature_flag NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| env_config | env_config eh variavel generica de config; feature_flag eh logica on/off | P09 env_config |
| permission | permission controla QUEM acessa recursos; feature_flag controla SE feature existe | P09 permission |
| path_config | path_config define caminhos de filesystem; feature_flag eh toggle logico | P09 path_config |
| runtime_rule | runtime_rule define comportamento tecnico (timeouts); feature_flag eh toggle de feature | P09 runtime_rule |
| boot_config | boot_config eh per-provider (model, temp); feature_flag eh toggle generico | P02 boot_config |

Regra: "esta FEATURE deve estar ON ou OFF, para quem, com que rollout?" -> feature_flag.

## Position in Config Flow

```text
feature_flag (P09) --> agent (P02) --> runtime decision
       |
  rollout_evaluation --> targeting
       |
  kill_switch --> emergency_off
```

feature_flag is RUNTIME TOGGLE — evaluated at decision points during execution.

## Dependency Graph

```text
feature_flag --consumed_by--> agent (P02) (agents check flags before enabling features)
feature_flag --consumed_by--> router (P02) (routers check flags for A/B routing)
feature_flag --consumed_by--> skill (P04) (skills check flags for optional phases)
feature_flag <--receives-- guardrail (P11) (safety rules for flag behavior)
feature_flag --independent-- env_config, path_config, runtime_rule, permission
```

## Fractal Position
Pillar: P09 (Config — HOW the system configures)
Function: GOVERN (feature_flag governs whether features are active)
Layer: runtime (flags evaluated at runtime decision points)
Scale: L0 (per-feature — one flag per feature, granular)
feature_flag is EXTENSION (not core_24): system runs without flags, but flags enable safe deployments.
