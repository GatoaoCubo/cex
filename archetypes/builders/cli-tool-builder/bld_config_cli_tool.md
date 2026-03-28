---
kind: config
id: bld_config_cli_tool
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: cli_tool Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_cli_{tool_slug}.md` | `p04_cli_artifact_validator.md` |
| Builder directory | kebab-case | `cli-tool-builder/` |
| Frontmatter fields | snake_case | `output_format`, `exit_codes` |
| Tool slug | snake_case, lowercase, no hyphens | `artifact_validator`, `index_builder` |
| Command names | snake_case, verb or verb_noun | `validate`, `check_schema`, `build` |
| Flag names | kebab-case with `--` prefix | `--strict`, `--output-format` |

Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.

## File Paths
- Output: `cex/P04_tools/examples/p04_cli_{tool_slug}.md`
- Compiled: `cex/P04_tools/compiled/p04_cli_{tool_slug}.yaml`

## Size Limits (aligned with SCHEMA)
- Body: max 1024 bytes
- Total (frontmatter + body): ~2000 bytes
- Density: >= 0.80 (no filler)

## Output Format Enum

| Value | When to use |
|-------|-------------|
| text | Human-readable default, unstructured |
| json | Machine-parseable, piping to other tools |
| table | Tabular data display (columns, alignment) |
| yaml | Config-like structured output |

## Exit Code Conventions

| Code | Meaning |
|------|---------|
| 0 | Success — operation completed normally |
| 1 | General error — operation failed |
| 2 | Usage error — invalid args/flags |
| 3 | I/O error — file not found, permission denied |
| 126 | Permission denied — cannot execute |
| 127 | Command not found |

Rule: every cli_tool MUST define at least codes 0 and 1.
