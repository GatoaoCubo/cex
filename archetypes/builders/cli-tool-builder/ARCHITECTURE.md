---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of cli_tool in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: cli_tool in the CEX

## Boundary
cli_tool EH: ferramenta de linha de comando que executa uma tarefa pontual e termina.
Recebe input via args/flags/stdin, produz output via stdout/stderr, retorna exit code.
Cada command tem syntax + flags + args. cli_tool EXECUTA e TERMINA, nunca persiste.

cli_tool NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| skill | skill eh habilidade com fases e trigger; cli_tool eh execucao pontual sem fases | P04 skill |
| daemon | daemon persiste em background; cli_tool executa e termina | P04 daemon |
| plugin | plugin eh extensao plugavel ao sistema; cli_tool eh executavel independente | P04 plugin |
| mcp_server | mcp_server expoe tools via MCP protocol; cli_tool eh invocado diretamente | P04 mcp_server |
| client | client consome API via HTTP; cli_tool opera via terminal/shell | P04 client |
| connector | connector integra servico bidirecional; cli_tool eh unidirecional (in->out) | P04 connector |
| scraper | scraper extrai dados web; cli_tool processa input local | P04 scraper |
| hook | hook eh gatilho pre/post evento; cli_tool eh invocado explicitamente | P04 hook |
| component | component eh bloco composavel de pipeline; cli_tool eh executavel standalone | P04 component |

Regra: "quem executa via terminal, processa args, e termina com exit code?" -> cli_tool.

## Position in Agent Tool Flow

```text
agent (P02) --> hook (P04) --> cli_tool (P04) --> filesystem/stdout
                   |                |
              skill (P04)      exit_code + output
                   |
              daemon (P04)
```

cli_tool is EXECUTION LAYER — atomic operations invoked by agents or hooks.

## Dependency Graph

```text
cli_tool <--receives-- env_config (P09) (env vars, config file paths)
cli_tool <--receives-- path_config (P09) (binary location, PATH setup)
cli_tool <--receives-- guardrail (P11) (execution constraints, timeouts)
cli_tool --consumed_by--> agent (P02) (agent invokes tool via shell)
cli_tool --consumed_by--> hook (P04) (hooks invoke tool on events)
cli_tool --independent-- mcp_server, client, connector, scraper, daemon
```

## Fractal Position
Pillar: P04 (Tools — what the agent USES)
Function: CALL (agent invokes tool at runtime)
Layer: runtime (executes during agent session)
Scale: L2 (per-task — one tool per specific operation)
cli_tool is EXTENSION (not core_24): useful but not required for bootstrapping.
