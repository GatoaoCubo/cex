---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of daemon in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: daemon in the CEX

## Boundary
daemon EH: processo background persistente que executa continuamente ou em schedule.
Tem lifecycle proprio (start, run, restart, shutdown), responde a signals, escreve PID,
e eh monitorado por health checks. Daemon PERSISTE, nunca executa e sai imediatamente.

daemon NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| hook | hook dispara UMA VEZ por evento (pre/post); daemon roda continuamente | P04 hook |
| cli_tool | cli_tool executa e termina; daemon persiste em background | P04 cli_tool |
| skill | skill eh invocavel sob demanda com fases; daemon roda independente | P04 skill |
| workflow | workflow orquestra multiplos steps; daemon executa uma concern unica | P12 workflow |
| connector | connector define spec de integracao; daemon eh lifecycle de processo | P04 connector |
| plugin | plugin eh extensao plugavel; daemon eh processo independente | P04 plugin |
| mcp_server | mcp_server expoe tools via MCP; daemon eh processo generico | P04 mcp_server |
| client | client consome API pontualmente; daemon roda background | P04 client |
| component | component eh bloco composavel; daemon eh processo autonomo | P04 component |

Regra: "quem RODA em background PERSISTENTEMENTE com restart e signal handling?" -> daemon.

## Position in Process Lifecycle

```text
env_config (P09) --> daemon (P04) --> signal (P12)
                        |                 |
                   health_check      monitoring
                        |
                   restart_policy
```

daemon is PROCESS LAYER — persistent background execution with self-management.

## Dependency Graph

```text
daemon <--receives-- env_config (P09) (config vars, paths, secrets)
daemon <--receives-- runtime_rule (P09) (timeouts, resource limits)
daemon <--receives-- guardrail (P11) (safety boundaries, circuit breakers)
daemon --produces--> signal (P12) (heartbeat, completion, error signals)
daemon --consumed_by--> workflow (P12) (workflows may depend on daemon being alive)
daemon --may_wrap--> connector (P04) (daemon runs connector sync loop)
daemon --may_wrap--> client (P04) (daemon polls API via client)
daemon --independent-- hook, skill, cli_tool, plugin, scraper
```

## Fractal Position
Pillar: P04 (Tools — what the agent USES)
Function: GOVERN (daemon governs its own lifecycle)
Layer: runtime (executes persistently during system lifetime)
Scale: L1 (per-system — daemons are infrastructure-level)
daemon is EXTENSION (not core_24): persistent process management, useful but not required for bootstrap.
