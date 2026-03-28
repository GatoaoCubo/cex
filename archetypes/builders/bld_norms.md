---
kind: norms
id: bld_norms
---

# Builder Norms (inject in every builder handoff)

## Mandatory Rules (learned from deep review)

1. **MANIFEST.md parent**: set `parent: null` — never reference [PLANNED] builders
2. **TOOLS.md brain_query**: mark as `CONDITIONAL` not `ACTIVE` — add `[MCP]` tag
3. **INSTRUCTIONS.md brain_query**: write `brain_query [IF MCP]` — not all runtimes have MCP
4. **ARCHITECTURE.md**: MUST include `## Dependency Graph` with `-->` arrows showing receives/produces_for/independent
5. **EXAMPLES.md**: golden must have 19+ fields. Anti-example must list 8+ numbered FAILURES with gate refs
6. **OUTPUT_TEMPLATE.md**: NO instructions inside template (no "repeat for N"). Only {{vars}} and structure
7. **SCHEMA.md**: every required field MUST appear in OUTPUT_TEMPLATE.md — zero drift allowed

## Quality Floor

- HARD gates: all must pass (YAML parses, id pattern, kind literal, quality null, required fields)
- SOFT gates: score >= 8.0 minimum
- Density: >= 0.80 (no filler phrases)
- Max 4KB per ISO file

## Deep Review Learnings (Waves 3-4)

8. **INSTRUCTIONS.md steps**: each numbered step = ONE action (no "and", "then", compound verbs)
9. **ARCHITECTURE.md boundary**: MUST list ALL sibling kinds in same pillar as "NAO EH" rows
10. **SCHEMA.md flags/enums**: use GENERIC values, not runtime-specific (no --dangerously-skip-permissions)
11. **EXAMPLES.md golden IDs**: use CEX-universal patterns, minimize CODEXA-specific satellite names
12. **COLLABORATION.md cross-refs**: if builder A refs builder B, builder B MUST ref builder A
