---
kind: config
id: bld_config_model_provider
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: low
max_turns: 25
disallowed_tools: []
fork_context: inline
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
---
# Config: model_provider Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p02_mp_{provider}.yaml` | `p02_mp_anthropic.yaml` |
| Builder directory | kebab-case | `model-provider-builder/` |
| Frontmatter fields | snake_case | `rate_limit_rpm`, `api_key_env` |
| Provider values | lowercase single word | `anthropic`, `openai`, `google` |
| Model IDs | exact provider identifier | `claude-opus-4-6`, `gpt-4o-2024-08-06` |
Rule: id MUST equal filename stem (validator checks this).
## File Paths
- Output: `cex/P02_model/examples/p02_mp_{provider}.yaml`
- Compiled: `cex/P02_model/compiled/p02_mp_{provider}.yaml`
- Router config: `cex/.cex/config/router_config.yaml` (consumes model_provider)
## Size Limits (aligned with SCHEMA)
- Frontmatter: ~700-1000 bytes (22+ fields)
- Body: max 4096 bytes (excl frontmatter)
- Total: max 5100 bytes
- Density: >= 0.85
## Provider Enum
Valid: anthropic, openai, google, ollama, groq, mistral, together, fireworks, deepseek, other
If provider not in list: use "other" and add provider name in tags.
## Model ID Policy
- ALWAYS use the full versioned model identifier (e.g., `gpt-4o-2024-08-06`, not `gpt-4o`)
- For providers with stable IDs (Anthropic): use current published name
- For Ollama: use `model:tag` format (e.g., `llama3.1:70b`)
- NEVER use deprecated model IDs — check provider deprecation schedule
## Rate Limit Policy
- Document the ACTUAL tier limits for the user's account
- Free tier limits are default when tier is unspecified
- RPM (requests per minute) and TPM (tokens per minute) are separate constraints
- If provider uses different rate limit structure: document in body, set standard fields to null
## Authentication
- NEVER hardcode API keys in artifacts
- ALWAYS use environment variable reference: `api_key_env: "ANTHROPIC_API_KEY"`
- For Ollama/local: `api_key_env: null` (no auth needed)
## Freshness
- updated field must be within 90 days of current date
- Model IDs change frequently — check provider model list on every build
- Rate limits change with account tier upgrades — verify on each update
