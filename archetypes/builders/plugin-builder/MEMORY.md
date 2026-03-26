---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: plugin-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any non-null value)
2. Using hyphens in id slug (must be underscores: p04_plug_my_plugin not p04_plug_my-plugin)
3. api_surface_count not matching actual methods in API Surface table (H07 catches this)
4. lifecycle missing on_load or on_unload (both are mandatory minimum)
5. hot_reload: true but lifecycle missing on_config_change (H09 catches this)
6. Confusing plugin (P04, full extension) with hook (P04, single-event interception)
7. No interface contract declared — plugins without contracts are unintegrable
8. Dependencies not declared — implicit dependencies cause silent runtime failures
9. Exposing internal state via API surface — only expose intentional methods
10. Missing config_schema defaults — plugins must work with default configuration
11. No Testing section — plugins need unit tests against mocked host interface
12. Isolation level not declared — security boundary undefined

### Plugin Architecture Patterns
| Pattern | When | Isolation | Priority |
|---------|------|-----------|----------|
| Metrics exporter | Observability | shared | 0-49 |
| Auth provider | Security | privileged | 0-49 |
| Format adapter | Data processing | sandboxed | 50-99 |
| Custom tool | Domain extension | shared | 100-149 |
| Debug inspector | Development | sandboxed | 200+ |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | interface contract design, isolation level selection, dependency resolution, lifecycle completeness |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a plugin artifact, update:
- New common mistake (if encountered)
- New architecture pattern (if discovered)
- Production counter increment
