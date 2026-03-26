---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: satellite-spec-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any value)
2. Using hyphens in id slug (must be underscores: p08_sat_atlas_codex, not p08_sat_atlas-codex)
3. Making mcps a string instead of list (must be list[string])
4. Writing model as full name "Claude Sonnet 4" instead of identifier "sonnet"
5. Missing boot_sequence entirely (even simple satellites need ordered init steps)
6. Drifting into agent-level detail (individual agent configs belong in P02 agent)
7. Omitting constraints (every satellite has limits — make them explicit)
8. Setting max_concurrent > 3 (BSOD risk on current hardware)
9. Mixing satellite_spec with spawn_config (spec = WHAT, spawn = HOW to launch)
10. Forgetting dispatch_keywords (orchestrator cannot route without keywords)

### Satellite Patterns

| Pattern | When to use | Complexity |
|---------|-------------|-----------|
| Research satellite | Market intel, competitor analysis | Medium (MCP-heavy) |
| Build satellite | Code generation, implementation | High (opus model) |
| Marketing satellite | Copy, content, ads | Medium (sonnet model) |
| Knowledge satellite | Documentation, indexing | Low (sonnet model) |
| Execute satellite | Deploy, test, validate | High (opus + infra MCPs) |
| Monetize satellite | Courses, pricing, funnels | Medium (sonnet model) |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | model selection, MCP completeness, scaling limits |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a satellite_spec, update:
- New common mistake (if encountered)
- New satellite pattern (if discovered)
- Production counter increment
