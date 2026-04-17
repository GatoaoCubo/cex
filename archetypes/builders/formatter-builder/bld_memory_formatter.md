---
id: p10_lr_formatter_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "Formatters that omit locale for numeric output produce wrong decimal separators (1.000 vs 1,000 depending on locale). Missing null handling in transformation rules causes runtime crashes when optional fields are absent. Escaping mismatches — using HTML escaping rules for a JSON target or vice versa — corrupt output silently. rule_count field not matching the actual count of rules in the Formatting Rules table is caught by schema validator H07. Formatters that include extraction or validation logic grow unbounded and become unmaintainable."
pattern: "Every rule in the Formatting Rules table specifies: input type, transformation applied, output example, and null behavior. Locale is declared at artifact level for number and date rules. Escaping strategy matches the target format: HTML uses entity encoding, JSON uses backslash escaping, markdown uses backslash for special chars. Null input must produce a documented fallback output, never a runtime error. Extraction belongs in parser (P05); validation belongs in validator (P06)."
evidence: "8 formatter artifacts built. Formatters with explicit null handling had zero runtime crashes on opti..."
confidence: 0.75
outcome: SUCCESS
domain: formatter
tags: [formatter, locale_aware, escaping, null_handling, transformation_rules, output_format]
tldr: "Declare locale for numeric/date rules; match escaping to target format; every rule documents null behavior."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
keywords: [formatter, locale, escaping, null_handling, transformation, rule_count, target_format, currency, date_format]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Formatter"
density_score: 0.90
llm_function: INJECT
---
## Summary
A formatter defines how data is transformed into a presentation format. It is not a parser (which extracts data) and not a validator (which checks data). Its core deliverable is a table of transformation rules where each rule specifies the input type, the transformation applied, the output shape, and what happens when input is null.
## Pattern
1. Declare `locale` at the artifact level for any artifact that formats numbers, currencies, or dates.
2. The Formatting Rules table has four columns per rule: `input_type`, `transform`, `output_example`, `null_behavior`.
3. Escaping strategy must match the target format: HTML uses entity encoding (`&amp;`, `&lt;`); JSON uses backslash sequences; markdown escapes with backslash for `*`, `_`, `[`, `]`.
4. Every rule documents `null_behavior` explicitly — either a fallback string (`"—"`, `"N/A"`) or omit-the-field semantics.
5. `rule_count` in frontmatter must match the exact number of rows in the Formatting Rules table.
6. Currency formatting in pt-BR: `R$ {value:,.2f}` with decimal/thousands swapped (`swap_decimal: true`).
7. Date formatting: use strftime codes; document which timezone is assumed.
8. Truncation rules must specify the byte/char limit and the suffix appended (`"..."`, `" [truncated]"`).
## Anti-Pattern
1. Omitting `locale` for number or date formatters — `1.000,00` (pt-BR) and `1,000.00` (en-US) are different values.
2. Applying HTML entity escaping to a JSON target — produces malformed JSON with `&amp;` literal strings.
3. Missing null handling in any rule — optional fields absent at runtime cause crashes or empty output.
4. Including extraction logic (`"parse price from HTML string"`) — that is a parser (P05), not a formatter.
5. Including validation logic (`"check if price is positive"`) — that is a validator (P06), not a formatter.
6. `rule_count` not matching the actual rule count — caught by schema validator H07 on every build.
## Context
Applies when: transforming structured data into a human-readable or machine-readable output format.

## Builder Context

This ISO operates within the `formatter-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Reference

```yaml
id: p10_lr_formatter_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_formatter_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | formatter |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |
