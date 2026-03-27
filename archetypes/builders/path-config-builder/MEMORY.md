---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: path-config-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Using hyphens in id slug (must be underscores: p09_path_data_pipeline not p09_path_data-pipeline)
2. Setting quality to a number instead of null (H05 rejects any non-null value)
3. paths list not matching ## Path Catalog names exactly (S03 drift)
4. Including user-specific absolute paths like /home/john or C:\Users\John (H08 — use {{HOME}})
5. Confusing path_config with env_config (paths are filesystem locations, env is variables)
6. Using backslashes in path templates (always forward slashes, resolve at runtime)
7. Missing ## Directory Hierarchy section (required, shows tree structure)
8. Not specifying platform compatibility for each path
9. Vague scope like "files" instead of concrete "data_pipeline" or "global"
10. Missing ## Platform Notes even for "all" platform (section required, state cross-platform rules)

### Path Type Patterns
| Scope | Typical Paths | Platform |
|-------|--------------|----------|
| global | base_dir, config_dir, log_dir, temp_dir | all |
| service | base_dir, data_dir, output_dir, cache_dir | all |
| satellite | work_dir, handoff_dir, signal_dir | all |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | platform differences, expandable vars, hierarchy depth |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a path_config, update:
- New common mistake (if encountered)
- New path type pattern (if discovered)
- Production counter increment
