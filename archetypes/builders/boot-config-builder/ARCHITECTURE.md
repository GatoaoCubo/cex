---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of boot_config in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: boot_config in the CEX

## Boundary
boot_config EH: configuracao de inicializacao de agente por provider — parametros
runtime-specific (model, flags, tools, MCP, permissions, constraints) que transformam
uma definicao generica de agente em instancia executavel num provider concreto.

boot_config NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| agent | agent define QUEM o agente EH; boot_config define COMO ele INICIA | P02 agent |
| model_card | model_card spec do LLM subjacente; boot_config seleciona e configura o modelo | P02 model_card |
| mental_model (P02) | mental_model define routing/decisoes; boot_config define init params | P02 mental_model |
| iso_package | iso_package empacota para distribuir; boot_config configura para executar | P02 iso_package |
| router | router define regras de roteamento; boot_config nao roteia | P02 router |
| fallback_chain | fallback_chain define sequencia de modelos; boot_config seleciona UM modelo | P02 fallback_chain |
| lens | lens eh perspectiva especializada; boot_config eh config tecnica | P02 lens |
| axiom | axiom eh principio imutavel; boot_config eh config editavel por provider | P02 axiom |
| env_config (P09) | env_config define variaveis genericas de ambiente; boot_config eh provider-specific | P09 env_config |
| spawn_config (P12) | spawn_config orquestra spawn de satelites; boot_config configura UM agente | P12 spawn_config |

Regra: "como este agente inicializa neste provider especifico?" -> boot_config.

## Position in Agent Boot Flow

```text
model_card (P02) --> boot_config (P02) --> agent (P02) --> spawn_config (P12)
       |                    |                   |                |
  LLM selection      init params          identity         orchestration
                           |
         system_prompt (P03) + tools (P04) + mcp_config
```

boot_config is INITIALIZATION LAYER — bridges model selection (model_card)
with agent instantiation (agent) on a specific provider runtime.

## Dependency Graph

```text
boot_config <--receives-- model_card (P02) (LLM spec for model selection)
boot_config <--receives-- agent (P02) (identity to bootstrap)
boot_config <--receives-- system_prompt (P03) (persona reference)
boot_config --produces_for--> spawn_config (P12) (runtime parameters)
boot_config --consumed_by--> workflow (P12) (orchestration init)
boot_config --independent-- iso_package, router, fallback_chain, lens
```

## Fractal Position
Pillar: P02 (Model — QUEM o agente EH)
Function: GOVERN (boot_config governs how initialization happens)
Layer: runtime (configures runtime behavior per provider)
Scale: L0 (infrastructure — every deployed agent needs boot configuration)
Unique: only P02 kind scoped to a specific provider runtime.
