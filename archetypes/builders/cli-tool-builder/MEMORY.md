---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: cli-tool-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Using hyphens in id slug (must be underscores: p04_cli_validator not p04_cli_code-validator)
2. Setting quality to a number instead of null (H05 rejects any non-null value)
3. commands list not matching ## Commands section names exactly (S03 drift)
4. Missing exit_codes field (required — caller cannot interpret results without it)
5. Omitting output_format (required — consumer needs to know how to parse)
6. Including implementation code in body (this is a spec, not source)
7. Writing command entries without syntax or flags (S04 incomplete)
8. Exceeding 1024 bytes body limit (cli_tool is compact)
9. Confusing cli_tool with daemon (cli_tool terminates, daemon persists)
10. Defining flags with underscores instead of kebab-case (--output_format vs --output-format)

### Effective Patterns
- Command naming: verb or verb_noun in snake_case — `validate`, `check_schema`, `build_index`
- Flag naming: kebab-case with -- prefix — `--strict`, `--output-format`
- commands mirror: write the list in frontmatter FIRST, then expand each in body
- Overview pattern: "{Tool} for {task}. Used by {consumer} via terminal or agent shell."
- Body budget: Overview(80B) + Commands(600B) + Output(150B) + Config(150B) = ~980B

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | id hyphens, commands drift, missing exit_codes |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a cli_tool, update:
- New common mistake (if encountered)
- New effective pattern (if discovered)
- Production counter increment
