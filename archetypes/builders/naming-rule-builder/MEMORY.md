---
pillar: P10
llm_function: INJECT
kind: memory
domain: naming_rule
version: 1.0.0
---

# Memory — Naming Rule Builder

## Common Mistakes

1. **Self-assigning quality** — Setting `quality: 8.0` at creation. Must always be `null`. Quality is assigned post-review by a separate reviewer pass.
2. **Plain-text pattern** — Writing `pattern: "starts with p01_kc_"` instead of a regex. Pattern must be a valid, machine-testable regex string.
3. **Wrong kind value** — Using `naming_convention`, `naming_schema`, or `convention` instead of the fixed value `naming_rule`.
4. **Hyphens in scope slug** — Using `p05_nr_knowledge-card` instead of `p05_nr_knowledge_card`. Scope slug must be snake_case (underscores only).
5. **Missing pillar prefix in ID** — Writing `nr_knowledge_card` instead of `p05_nr_knowledge_card`. The `p05_` prefix is mandatory and encodes the pillar.
6. **Invalid case_style enum value** — Using `lowercase`, `uppercase`, `sentence_case`, or any value not in the allowed enum. Only: snake_case, kebab-case, camelCase, PascalCase, UPPER_SNAKE.
7. **Missing collision_strategy** — Leaving collision_strategy blank or writing `null`. Every naming rule must define a collision resolution strategy; `null` is not a valid value.

## Naming Pattern Catalog

| Scope | Pattern | Prefix | Separator | Case Style |
|-------|---------|--------|-----------|-----------|
| knowledge_card | `^p01_kc_[a-z][a-z0-9_]+\.md$` | `p01_kc_` | `_` | snake_case |
| model_card | `^p02_mc_[a-z][a-z0-9_]+\.md$` | `p02_mc_` | `_` | snake_case |
| naming_rule | `^p05_nr_[a-z][a-z0-9_]+\.md$` | `p05_nr_` | `_` | snake_case |
| signal | `^p12_sig_[a-z][a-z0-9_]+\.json$` | `p12_sig_` | `_` | snake_case |
| builder_dir | `^[a-z][a-z0-9]+-[a-z][a-z0-9-]+-builder$` | none | `-` | kebab-case |
| agent_readme | `^[a-z][a-z0-9-]+/README\.md$` | none | `-` | kebab-case |

## Regex Cheat Sheet

| Pattern Fragment | Matches |
|-----------------|---------|
| `^p05_nr_` | literal start: pillar+kind prefix |
| `[a-z][a-z0-9_]+` | slug: starts with letter, then alphanumeric+underscore |
| `[a-z][a-z0-9-]+` | slug: starts with letter, then alphanumeric+hyphen |
| `\\.md$` | literal `.md` at end of string |
| `\\.json$` | literal `.json` at end of string |
| `_v[0-9]+` | version suffix: `_v1`, `_v12` |
| `_[0-9]{8}` | date suffix: `_20260326` |
| `_[0-9]{3}` | sequence suffix: `_001`, `_042` |

## Production Counter

| Stat | Value |
|------|-------|
| naming_rule artifacts produced | 0 (bootstrap) |
| Common failure mode | plain-text pattern (not regex) |
| Avg time to produce | ~8 min (3-phase protocol) |
| Quality floor | 7.0 (experimental); 8.0 (pool-eligible) |
