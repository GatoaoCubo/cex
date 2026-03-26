---
lp: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: knowledge-card-builder

## Accumulated Patterns (update after each production)

### Quality Score Distribution (from 63+ real examples)
| Tier | Count | Common traits |
|------|-------|---------------|
| GOLDEN (9.5+) | ~5 | Dense tables, code flows, zero filler |
| PUBLISH (8.0+) | ~40 | Good structure, minor density gaps |
| ACCEPTABLE (7.0+) | ~10 | Missing keywords or thin sections |
| NEEDS_WORK (<7.0) | ~8 | Filler, missing fields, broad topics |

### Common Mistakes (learned from production + validate_kc.py)
1. Setting quality to a number instead of null (H05 instant fail)
2. Using string tags ("tag1, tag2") instead of list [tag1, tag2]
3. Bullets exceeding 80 chars — split or rephrase
4. Sections with < 3 lines flagged as "thin" (S08)
5. Filler phrases surviving from source material copy-paste
6. Self-referencing in tldr ("This KC covers..." -> just state the fact)
7. Topic too broad — "Python" not atomic, "Python GIL mechanics" is
8. Missing linked_artifacts when related KCs clearly exist
9. Internal paths leaking into body (records/, .claude/)
10. Duplicate sentences (Jaccard >= 0.85) from copy-paste sections

### Density Boosters (proven techniques)
| Technique | Density gain | Example |
|-----------|-------------|---------|
| Prose -> table | +0.15 | 3 paragraphs -> 1 table |
| Paragraph -> bullets | +0.10 | 5-line paragraph -> 5 bullets |
| Add code block | +0.05 | Text flow -> ASCII diagram |
| Cut filler phrases | +0.08 | "It should be noted that" -> delete |
| Shorten bullets to 80ch | +0.03 | Forces concision |

### Production Counter
| Metric | Value |
|--------|-------|
| Cards in examples/ | 63+ |
| Avg quality | ~8.2 (estimated from validator runs) |
| Common friction | broad topics, filler from sources |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a knowledge_card, update:
- New common mistake (if encountered)
- New density technique (if discovered)
- Production counter increment
