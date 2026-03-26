---
lp: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: model_card Production Rules

## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p02_mc_{provider}_{slug}.md` | `p02_mc_google_gemini_2_5_pro.md` |
| Builder directory | kebab-case | `model-card-builder/` |
| Frontmatter fields | snake_case | `context_window`, `max_output` |
| Provider values | lowercase single word | `anthropic`, `openai`, `google` |
| Model slug | snake_case, no provider prefix | `opus_4`, `gpt_4o`, `gemini_2_5_pro` |

Rule: id MUST equal filename stem (validator checks this).

## File Paths
- Output: `cex/P02_model/examples/p02_mc_{provider}_{slug}.md`
- Compiled: `cex/P02_model/compiled/p02_mc_{provider}_{slug}.yaml`

## Size Limits (aligned with SCHEMA)
- Frontmatter: ~800-1200 bytes (26 fields)
- Body: max 4096 bytes (excl frontmatter)
- Total: max 5300 bytes
- Density: >= 0.85

## Provider Enum (same as SCHEMA)
Valid: anthropic, openai, google, meta, mistral, cohere, deepseek, alibaba, ai21, other
If provider not in list: use "other" and add provider name in tags.

## Pricing Policy (aligned with SCHEMA)
- Frontmatter: BASE TIER only (lowest published standard API price)
- If tiered: document higher tiers in body Specifications table
- ALWAYS per_1M_tokens, USD only
- open-weight: null (not 0, not "free")
- commercial free tier: 0.00 (not null)
- cache_write: null if provider has no symmetric cache write price

## Freshness
- updated field must be within 90 days of current date
- If model deprecated: status = "deprecated", linked_artifacts must point to replacement
- Stale cards (>90d) flagged by lifecycle_rule for review
