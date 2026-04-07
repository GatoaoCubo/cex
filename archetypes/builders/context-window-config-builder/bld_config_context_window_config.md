---
kind: config
id: bld_config_context_window_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 20
disallowed_tools: []
fork_context: fork
hooks:
  pre_build: null
  post_build: null
permission_scope: nucleus
---
# Config: context_window_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p03_cwc_{model_slug}.yaml` | `p03_cwc_opus_rag_heavy.yaml` |
| Builder directory | kebab-case | `context-window-config-builder/` |
| Frontmatter fields | snake_case | `total_tokens`, `overflow_strategy` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `P03_prompt/examples/p03_cwc_{model}.yaml`
- Compiled: `P03_prompt/compiled/p03_cwc_{model}.yaml`
## Size Limits
- Total file: max 2048 bytes
- tldr: <= 160 chars
## Budget Validation Rules
- sum(all_budgets) + output_reserve <= total_tokens
- output_reserve >= 2000 (absolute minimum)
- Default split: system=10%, examples=15%, context=40%, query=5%, output=30%
- RAG-heavy: context gets 50%+, examples reduced
- Few-shot-heavy: examples get 25%+, context reduced
