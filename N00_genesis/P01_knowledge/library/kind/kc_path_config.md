---
id: p01_kc_path_config
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P09
title: "Path Config — Deep Knowledge for path_config"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: commercial_agent
domain: path_config
quality: 9.1
tags: [path_config, P09, GOVERN, kind-kc]
tldr: "path_config is the versioned YAML map of named filesystem paths for a bounded scope — anchored to a base_dir, with explicit readonly declarations to prevent accidental overwrites."
when_to_use: "Building, reviewing, or reasoning about path_config artifacts"
keywords: [filesystem_paths, path_aliases, directory_config]
feeds_kinds: [path_config]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - bld_examples_path_config
  - p03_ins_path_config
  - p11_qg_path_config
  - path-config-builder
  - bld_architecture_path_config
  - bld_knowledge_card_path_config
  - bld_collaboration_path_config
  - bld_memory_path_config
  - bld_schema_path_config
  - p03_sp_path_config_builder
---

# Path Config

## Spec
```yaml
kind: path_config
pillar: P09
llm_function: GOVERN
max_bytes: 3072
naming: p09_path_{{scope}}.yaml
core: true
```

## What It Is
A path_config is an authoritative YAML map of named filesystem paths within a bounded scope — all anchored relative to a base_dir, with explicit readonly lists. It is NOT an env_config (which covers generic configuration variables), NOT a permission (which governs access control logic beyond read/write on paths).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `LANGCHAIN_CACHE_DIR`, `persist_directory` | Cache and vectorstore path configuration |
| LlamaIndex | `LLAMA_INDEX_CACHE_DIR`, `StorageContext` paths | Index storage locations, docstore paths |
| CrewAI | Knowledge source file paths | File paths for knowledge base sources |
| DSPy | Cache paths + compiled output dirs | `.dspy_cache`, compiled program output paths |
| Haystack | `DocumentStore` paths, pipeline YAML paths | Storage locations and serialization paths |
| OpenAI | N/A | Cloud-only API; no filesystem paths |
| Anthropic | N/A | API-only; local paths used in `bash_20250124` tool |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| scope | string | required | system/agent_group/service — tighter = clearer ownership |
| base_dir | path | required | Root anchor — all other paths relative to this |
| paths | map[key, path] | required | Named aliases — more = easier reference, more maintenance |
| readonly | list[str] | [] | Explicit read-only paths — missing = accidental overwrites |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Base anchor | All paths relative to base_dir | `base_dir: C:/Users/PC/Documents/GitHub/cex` |
| Role separation | Read-only source vs writable output paths | `readonly: [P01_knowledge/templates/]` |
| Env interpolation | Paths use env var substitution | `${organization_ROOT}/records/pool/` |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Hardcoded absolute paths | `C:/Users/PC/` breaks on any other machine | Always use `base_dir` + relative paths |
| No readonly declaration | All paths writable = accidental template overwrites | Explicitly mark all source/template paths readonly |
| God path config | One config for all 7 agent_groups + system | Scope per agent_group or service; system config for shared dirs |

## Integration Graph
```
env_config, permission --> [path_config] --> agent_card, law, runtime_rule
                                  |
                             naming_rule, component_map, secret_config
```

## Decision Tree
- IF path points to a credential file THEN secret_config handles it
- IF path availability determines feature THEN feature_flag + path_config
- IF path used by exactly 1 agent_group THEN agent_group-scoped path config
- DEFAULT: system path_config for shared directories, agent_group path_config for local

## Quality Criteria
- GOOD: scope, base_dir, paths map, readonly list all present
- GREAT: env var interpolation supported, path existence validation rule, migration guide
- FAIL: hardcoded user-specific paths, no readonly declaration, missing base_dir anchor

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_path_config]] | upstream | 0.45 |
| [[p03_ins_path_config]] | upstream | 0.44 |
| [[p11_qg_path_config]] | downstream | 0.42 |
| [[path-config-builder]] | related | 0.42 |
| [[bld_architecture_path_config]] | upstream | 0.41 |
| [[bld_knowledge_card_path_config]] | sibling | 0.41 |
| [[bld_collaboration_path_config]] | related | 0.40 |
| [[bld_memory_path_config]] | downstream | 0.37 |
| [[bld_schema_path_config]] | upstream | 0.36 |
| [[p03_sp_path_config_builder]] | upstream | 0.31 |
