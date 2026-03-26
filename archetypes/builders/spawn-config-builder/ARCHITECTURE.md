---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of spawn_config in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: spawn_config in the CEX

## Boundary
spawn_config EH: configuracao declarativa de como spawnar um satelite — modo, flags, model, timeout, MCP profile. Consumido por PowerShell spawn scripts.

spawn_config NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| boot_config | boot_config eh inicializacao per-provider (temperature, tokens) | P02 boot_config |
| env_config | env_config sao variaveis de ambiente (API keys, paths) | P09 env_config |
| handoff | handoff eh instrucao de tarefa com context+commit | P12 handoff |
| signal | signal eh evento de completion/error emitido por satelite | P12 signal |
| workflow | workflow eh orquestracao multi-step de agentes | P12 workflow |

Regra: "como spawnar este satelite com quais flags e timeout?" -> spawn_config.

## Position in Dispatch Flow

```text
dispatch_rule (P12) --> handoff (P12) --> spawn_config (P12) --> PowerShell script
                                                                      |
                                                               satellite spawned
                                                                      |
                                                               signal (P12)
```

spawn_config is INFRASTRUCTURE LAYER — bridges orchestration decisions to runtime execution.

## Dependency Graph

```text
spawn_config <--receives-- dispatch_rule (P12) (which satellite to spawn)
spawn_config <--receives-- handoff (P12) (task reference for prompt)
spawn_config --consumed_by--> spawn_solo.ps1 / spawn_grid.ps1 (execution)
spawn_config --independent-- signal, workflow, chain, system_prompt
```

## Fractal Position
Pillar: P12 (Orchestration — how it COORDINATES)
Function: GOVERN (defines rules for satellite spawning)
Scale: L0 (core 24 — every satellite spawn needs configuration)
spawn_config is the EXECUTION BRIDGE: 3 spawn scripts + 7 satellites depend on it.
