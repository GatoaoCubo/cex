---
kind: config
id: bld_config_function_def
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: function_def Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_fn_{function_slug}.md` | `p04_fn_search_web.md` |
| Compiled files | `p04_fn_{function_slug}.json` | `p04_fn_search_web.json` |
| Builder directory | kebab-case | `function_def-builder/` |
| Frontmatter fields | snake_case | `max_results`, `provider_compat` |
| Function slug | snake_case, lowercase, no hyphens | `search_web`, `get_weather` |
| Function name | snake_case, verb_noun | `search_web`, `create_ticket` |
| Parameter names | snake_case | `max_results`, `language_code` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P04_tools/examples/p04_fn_{function_slug}.md`
- Compiled: `cex/P04_tools/compiled/p04_fn_{function_slug}.json`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~4000 bytes
- Density: >= 0.80 (no filler)
## Parameter Type Enum
| Type | JSON Schema | When to use |
|------|------------|-------------|
| string | "type": "string" | Text input, IDs, names |
| number | "type": "number" | Decimal values, scores |
| integer | "type": "integer" | Counts, indices, limits |
| boolean | "type": "boolean" | Flags, toggles |
| array | "type": "array" | Lists of values |
| object | "type": "object" | Nested structures |
## Provider Compatibility
| Provider | Strict Mode | Nested Objects | Enum Support |
|----------|-------------|---------------|-------------|
| OpenAI | yes (strict: true) | yes (2 levels) | yes |
| Anthropic | no | yes (2 levels) | yes |
| Gemini | no | yes (limited) | yes |
| Bedrock | no | yes (2 levels) | yes |
Rule: keep nesting <= 2 levels for maximum compatibility.
