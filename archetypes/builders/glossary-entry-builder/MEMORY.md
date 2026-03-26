---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: glossary-entry-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any value)
2. Using hyphens in id slug (must be underscores: p01_gl_quality_gate, not p01_gl_quality-gate)
3. Definition exceeding 3 lines (must be concise — deep analysis goes in knowledge_card)
4. Writing synonyms as a string instead of list (must be list[string])
5. Empty synonyms list (must have at least 1 synonym)
6. Capitalizing term field when not a proper noun (use lowercase)
7. Including operational steps in definition (that is instruction P03)
8. Drifting into knowledge_card depth — adding sections, research, density scoring

### Glossary Patterns

| Pattern | When to use | Definition style |
|---------|-------------|-----------------|
| Technical term | System-specific concept | Concrete + 1 example |
| Abbreviation | Short form in use | Expand + define |
| Cross-pillar | Term used in multiple contexts | Define + disambiguate |
| Industry standard | Well-known concept | CEX-specific meaning |
| Internal jargon | Team-specific term | Plain language definition |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | definition length, depth vs breadth |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a glossary_entry, update:
- New common mistake (if encountered)
- New glossary pattern (if discovered)
- Production counter increment
