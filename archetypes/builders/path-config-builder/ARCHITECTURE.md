---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of path_config in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: path_config in the CEX

## Boundary
path_config EH: especificacao de caminhos do sistema de arquivos para um scope. Define NOMES
de paths, tipos (dir/file), plataforma, defaults, hierarquia de diretorios — nunca paths
absolutos usuario-especificos. Segue XDG Base Directory conventions.

path_config NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| env_config | env_config define variaveis genericas; path_config define caminhos de filesystem | P09 env_config |
| permission | permission controla QUEM acessa; path_config define ONDE ficam arquivos | P09 permission |
| feature_flag | feature_flag eh toggle on/off logico; path_config eh localizacao fisica | P09 feature_flag |
| runtime_rule | runtime_rule define comportamento (timeouts); path_config define localizacao | P09 runtime_rule |
| boot_config | boot_config eh per-provider (model, temp); path_config eh generico | P02 boot_config |

Regra: "quais CAMINHOS de filesystem este scope precisa, em quais plataformas?" -> path_config.

## Position in Config Flow

```text
path_config (P09) --> boot_config (P02) --> agent (P02) --> runtime
      |                    |
  dir_hierarchy       provider_config
      |
  platform_resolve
```

path_config is CONFIGURATION LAYER — defines filesystem structure before runtime starts.

## Dependency Graph

```text
path_config --consumed_by--> boot_config (P02) (boot reads paths for data/config dirs)
path_config --consumed_by--> daemon (P04) (daemons need log_dir, pid file paths)
path_config --consumed_by--> spawn_config (P12) (spawn reads work dirs for satellites)
path_config <--receives-- guardrail (P11) (security rules for path access)
path_config --independent-- env_config, feature_flag, runtime_rule, permission
```

## Fractal Position
Pillar: P09 (Config — HOW the system configures)
Function: GOVERN (path_config governs where files live and directory structure)
Layer: runtime (paths resolved at runtime)
Scale: L0 (per-scope — one path_config per scope, foundational)
path_config is CORE: system needs defined paths to function.
