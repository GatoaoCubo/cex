---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: knowledge-card-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from validation)
1. Setting quality to a number (must be null — H05 rejects any value)
2. Using hyphens in id slug (must be underscores: p01_kc_topic_name)
3. Writing bullets > 80 chars (S10 fails — break into sub-bullets)
4. Including internal paths like records/ or .claude/ (H09 fails)
5. Using filler phrases ("this document", "in summary") in body (S09)
6. Self-referencing in tldr ("this kc describes...") instead of direct fact
7. Forgetting axioms field (S18 — must be ALWAYS/NEVER actionable rules)
8. Tags as comma-separated string instead of YAML list (H07 fails)
9. Body under 200 bytes (H08 — need >= 4 sections with >= 3 lines each)
10. Author set to STELLA (H10 — STELLA orchestrates, never authors)

### Template Discrepancy (important)
The legacy template (tpl_knowledge_card.md) shows `quality: {{QUALITY_8_TO_10}}`.
validate_kc.py v2.0 enforces `quality: null` (H05). The VALIDATOR is truth.
Always set quality: null. Scoring is done externally after production.

### Density Boosters
- Replace prose paragraphs with bullet lists
- Replace descriptions with comparison tables
- Add code blocks (yaml, text diagrams, command examples)
- Remove transition sentences ("as we can see", "it is worth noting")
- Each bullet should contain exactly one fact

### Production Counter
| Metric | Value |
|--------|-------|
| Cards produced | 0 (builder just created) |
| Avg quality | — |
| Common friction | density threshold, bullet length |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a knowledge_card, update:
- New common mistake (if encountered)
- New density technique (if discovered)
- Production counter increment
