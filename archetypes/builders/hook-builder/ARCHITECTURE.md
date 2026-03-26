---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of hook in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: hook in the CEX

## Boundary
hook EH: interceptor de evento runtime — codigo executavel que dispara antes ou depois de um
evento do sistema (tool use, session start, prompt submit, stop). O hook INTERCEPTA eventos
pontuais e executa side effects (logging, metrics, validation, context injection).

hook NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| lifecycle_rule | lifecycle_rule DECLARA politicas (archive after 90d); hook EXECUTA codigo em evento | P11 lifecycle_rule |
| daemon | daemon RODA continuamente em background; hook DISPARA uma vez por evento | P04 daemon |
| plugin | plugin EXTENDE o sistema com API completa; hook INTERCEPTA um evento especifico | P04 plugin |
| skill | skill tem FASES estruturadas e workflow; hook eh acao unica em evento | P04 skill |
| signal | signal REPORTA o que aconteceu; hook REAGE a eventos | P12 signal |
| mcp_server | mcp_server EXPOE tools e resources; hook CONSOME eventos internos | P04 mcp_server |
| connector | connector CONECTA a servico externo; hook INTERCEPTA eventos internos | P04 connector |
| cli_tool | cli_tool eh INVOCADO pelo user; hook DISPARA automaticamente em evento | P04 cli_tool |
| scraper | scraper COLETA dados da web; hook PROCESSA eventos locais | P04 scraper |
| client | client CONSOME API externa; hook INTERCEPTA eventos internos | P04 client |
| component | component eh BLOCO composavel de pipeline; hook INTERCEPTA eventos pontuais | P04 component |

Regra: "o que deve acontecer antes/depois deste evento?" -> hook.

## Position in Runtime Flow

```text
event emitted --> conditions check --> hook (P04) --> side effect
                                          |
                                    [pre/post/both]
                                          |
                              signal (P12) <-- hook may emit signal
```

hook is the EVENT INTERCEPTION LAYER — sits between event emission and downstream
processing, executing side effects without modifying the core event flow.

## Dependency Graph

```text
hook <--triggered_by-- agent (P02) (events during execution)
hook <--triggered_by-- workflow (P12) (lifecycle events)
hook <--triggered_by-- spawn_config (P12) (session events)
hook --may_emit--> signal (P12) (report hook execution result)
hook --may_call--> cli_tool (P04) (execute external tool)
hook --independent-- parser, formatter, knowledge_card, model_card
```

## Fractal Position
Pillar: P04 (Tools — WHAT the agent USES)
Function: INTERCEPT (react to system events with side effects)
Layer: runtime (executes per-event, stateless reaction)
Scale: L0 (infrastructure — every event-driven system needs hooks)
