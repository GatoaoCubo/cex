---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: validator-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any value)
2. Using hyphens in id slug (must be underscores: p06_val_kc_quality, not p06_val_kc-quality)
3. Writing conditions as a string instead of list[object] (must be structured triples)
4. Using severity "critical" or "fatal" (only error/warning/info allowed)
5. Writing auto_fix as a string ("yes"/"maybe") instead of boolean (true/false)
6. Forgetting the target field in conditions (defaults to frontmatter but should be explicit)
7. Writing error_message as "Invalid" or "Error" (must be actionable — tell HOW to fix)
8. Drifting into scoring territory — adding weights or numeric scores (that is quality_gate P11)

### Validation Rule Patterns

| Pattern | When to use | Severity |
|---------|-------------|----------|
| Null check | Field must be null (e.g., quality) | error |
| Enum check | Field must be in allowed list | error |
| Regex match | Field must match pattern (e.g., id prefix) | error |
| Type check | Field must be correct type (list, object, string) | error |
| Range check | Numeric field within bounds | warning |
| Existence check | Required field must be present | error |
| Length check | String/list length constraints | warning |
| Format check | Date format, semver format | warning |
| No-filler check | Body must not contain filler phrases | info |
| Cross-field check | Two fields must be consistent | error |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | severity classification, conditions structure |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a validator, update:
- New common mistake (if encountered)
- New validation rule pattern (if discovered)
- Production counter increment
