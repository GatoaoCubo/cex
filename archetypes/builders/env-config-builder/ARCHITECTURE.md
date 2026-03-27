---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of env_config in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: env_config in the CEX

## Boundary
env_config EH: especificacao de variaveis de ambiente genericas do sistema. Define NOMES,
tipos, defaults, validacao, e sensibilidade — nunca valores reais de secrets. Segue
12-Factor App (Factor III): config que varia entre deploys vive em env vars.

env_config NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| boot_config | boot_config eh per-provider (model, temp, system_prompt); env eh generico | P02 boot_config |
| feature_flag | feature_flag eh on/off logico com rollout; env eh variavel de config | P09 feature_flag |
| path_config | path_config eh caminhos do filesystem; env eh variaveis genericas | P09 path_config |
| permission | permission eh controle de acesso (read/write); env eh config do sistema | P09 permission |
| runtime_rule | runtime_rule eh comportamento (timeouts, retries); env eh config values | P09 runtime_rule |

Regra: "quais VARIAVEIS DE AMBIENTE este scope precisa, com que defaults e validacao?" -> env_config.

## Position in Config Flow

```text
env_config (P09) --> boot_config (P02) --> agent (P02) --> runtime
      |                    |
  validation          provider_config
      |
  secret_masking
```

env_config is CONFIGURATION LAYER — foundation that feeds into all runtime components.

## Dependency Graph

```text
env_config --consumed_by--> boot_config (P02) (boot reads env vars at startup)
env_config --consumed_by--> daemon (P04) (daemons read env vars for config)
env_config --consumed_by--> connector (P04) (connectors read API keys from env)
env_config --consumed_by--> client (P04) (clients read base_url, auth from env)
env_config --consumed_by--> mcp_server (P04) (MCP servers read transport config)
env_config <--receives-- guardrail (P11) (security rules for sensitive vars)
env_config --independent-- feature_flag, path_config, runtime_rule, permission
```

## Fractal Position
Pillar: P09 (Config — HOW the system configures)
Function: GOVERN (env_config governs what variables exist and their constraints)
Layer: runtime (env vars are read at runtime)
Scale: L0 (per-scope — one env_config per scope, foundational)
env_config is EXTENSION (not core_24): useful for documenting config but system can run without spec.
