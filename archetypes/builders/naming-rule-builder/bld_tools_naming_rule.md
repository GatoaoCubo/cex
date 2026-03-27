---
pillar: P04
llm_function: CALL
kind: tools
domain: naming_rule
version: 1.0.0
---

# Tools — Naming Rule Builder

## Tool Registry

| Tool | Status | Tag | Purpose |
|------|--------|-----|---------|
| brain_query | CONDITIONAL | [MCP] | Discover existing naming rules and related conventions |
| Read | ACTIVE | [FILE] | Read existing naming rule files for scope overlap check |
| Grep | ACTIVE | [FILE] | Search for naming patterns in existing artifacts |
| Glob | ACTIVE | [FILE] | List existing naming rule files in pool directories |

## brain_query [IF MCP]

**Activation**: Only when Brain MCP is available in the current session.

```
brain_query("naming rule {scope_slug}")
brain_query("p05 nr {keyword}")
brain_query("naming convention {domain}")
```

**Expected return**: Existing naming rule artifacts, related conventions, pillar assignments.

**Fallback (MCP unavailable)**: Use Grep to search `records/pool/` for `kind: naming_rule` entries.

## Read [ACTIVE]

Use to load existing naming rule artifacts for scope comparison:

```
Read: records/pool/{pillar}/{id}.md
Read: archetypes/builders/naming-rule-builder/SCHEMA.md
Read: archetypes/builders/naming-rule-builder/OUTPUT_TEMPLATE.md
```

## Grep [ACTIVE]

Search for naming rule patterns in the codebase:

```
Grep: pattern="kind: naming_rule" path=records/pool/
Grep: pattern="^id: p05_nr_" path=records/pool/
Grep: pattern="{scope_keyword}" path=records/pool/
```

## Glob [ACTIVE]

List existing naming rules for scope overlap detection:

```
Glob: pattern="records/pool/**/p05_nr_*.md"
Glob: pattern="archetypes/builders/naming-rule-builder/*.md"
```

## Data Sources

| Source | Content | When to Use |
|--------|---------|-------------|
| `records/pool/` | Existing naming rule artifacts | Always — check before creating |
| `SCHEMA.md` | Field definitions and constraints | Always — source of truth |
| `OUTPUT_TEMPLATE.md` | Output structure | Always — derive final artifact |
| `KNOWLEDGE.md` | Industry naming standards | When establishing case style or pattern base |
