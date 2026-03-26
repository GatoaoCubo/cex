---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: boot-config-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any non-null value)
2. Using hyphens in id slug (must be underscores: p02_boot_claude_code not p02_boot_claude-code)
3. Missing identity object or leaving satellite blank (H07 requires name, role, satellite)
4. Using string for max_tokens ("16384" instead of 16384) — constraints must be numeric
5. Empty tools list (H09 requires at least one tool)
6. Copying constraints from wrong provider (cursor context window != claude context window)
7. Including spawn orchestration logic in boot_config (belongs in spawn_config P12)
8. Omitting constraints rationale in body table (S07 requires value + why)
9. Using placeholder provider name ("AI" or "default") instead of specific provider
10. Body exceeding 2048 bytes — boot_config must be concise

### Provider Reference
| Provider | Context Window | Typical Model | Key MCP |
|----------|---------------|---------------|---------|
| claude_code | 200000 | claude-sonnet-4-6 | brain, firecrawl |
| cursor_ai | 128000 | claude-sonnet-4-6 | none (built-in) |
| codex | 200000 | codex-mini | none |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | provider limits research, identity completeness |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a boot_config, update:
- New common mistake (if encountered)
- New provider reference entry (if new provider)
- Production counter increment
