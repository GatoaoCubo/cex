---
kind: norms
id: bld_norms
pillar: P08
quality: 9.2
title: "Norms"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Builder Norms (inject in every builder handoff)

## Mandatory Rules (learned from deep review)

1. **MANIFEST.md parent**: set `parent: null` — never reference [PLANNED] builders
2. **TOOLS.md brain_query**: mark as `CONDITIONAL` not `ACTIVE` — add `[MCP]` tag
3. **INSTRUCTIONS.md brain_query**: write `brain_query [IF MCP]` — not all runtimes have MCP
4. **ARCHITECTURE.md**: MUST include `## Dependency Graph` with `-->` arrows showing receives/produces_for/independent
5. **EXAMPLES.md**: golden must have 19+ fields. Anti-example must list 8+ numbered FAILURES with gate refs
6. **OUTPUT_TEMPLATE.md**: NO instructions inside template (no "repeat for N"). Only `{{vars}}` and structure
7. **SCHEMA.md**: every required field MUST appear in OUTPUT_TEMPLATE.md — zero drift allowed

## Quality Floor

1. HARD gates: all must pass (YAML parses, id pattern, kind literal, quality null, required fields)
2. SOFT gates: score >= 8.0 minimum
3. Density: >= 0.80 (no filler phrases)
4. Max 4KB per builder spec

## Deep Review Learnings (Waves 3-4)

8. **INSTRUCTIONS.md steps**: each numbered step = ONE action (no "and", "then", compound verbs)
9. **ARCHITECTURE.md boundary**: MUST list ALL sibling kinds in same pillar as "NOT" rows
10. **SCHEMA.md flags/enums**: use GENERIC values, not runtime-specific (no --dangerously-skip-permissions)
11. **EXAMPLES.md golden IDs**: use CEX-universal patterns, minimize framework-specific director names
12. **COLLABORATION.md cross-refs**: if builder A refs builder B, builder B MUST ref builder A

## Universal Schema Rules (v1.0)

13. **MANIFEST.md keywords**: 4-8 terms in frontmatter, extracted from ## Routing body
14. **MANIFEST.md triggers**: 2-4 natural language phrases in frontmatter
15. **MANIFEST.md capabilities**: >= 50 chars, 3 layers (L1=what, L2=how, L3=when)
16. **MEMORY.md memory_scope**: must be user | project | local (default: project)
17. **MEMORY.md observation_types**: must be [user, feedback, project, reference] — never alter
18. **MEMORY.md observation**: each observation MUST have type: field matching one of 4 types
19. **CONFIG.md effort**: must be low | medium | high | max (default: medium)
20. **CONFIG.md max_turns**: integer 1-100 (default: 25)
21. **CONFIG.md disallowed_tools**: list of blocked tools (empty list = all allowed)
22. **CONFIG.md permission_scope**: must be nucleus | pillar | global | restricted (default: nucleus)
23. **TOOLS.md Tool Permissions**: ## Tool Permissions section required with ALLOWED/DENIED/EFFECTIVE

## Metadata

```yaml
id: bld_norms
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-norms.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `norms` |
| Pillar |  |
| Domain | CEX system |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
