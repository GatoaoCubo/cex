---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: spawn-config-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any value)
2. Using hyphens in id slug (must be underscores: p12_spawn_solo not p12_spawn-solo)
3. Missing baseline flags (--dangerously-skip-permissions, --no-chrome)
4. Including task instructions in spawn_config (belongs in handoff)
5. Using uppercase satellite name (must be lowercase: shaka not SHAKA)
6. Setting timeout too low for task type (research needs >= 1800s)
7. Forgetting -p flag (causes workspace trust prompt hang in automation)
8. Using --mcp-config with absolute paths (hangs in PS->cmd chain)

### Satellite Timeout Reference

| Satellite | Typical Task | Recommended Timeout |
|-----------|-------------|-------------------|
| shaka | Research | 1800s (30min) |
| lily | Marketing copy | 1200s (20min) |
| edison | Build/code | 2700s (45min) |
| pytha | Knowledge | 1200s (20min) |
| atlas | Deploy/test | 900s (15min) |
| york | Monetize | 1200s (20min) |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | flag combinations, timeout sizing, mode selection |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a spawn_config, update:
- New common mistake (if encountered)
- New timeout reference (if discovered)
- Production counter increment
