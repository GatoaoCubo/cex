---
lp: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: every artifact needs rules about WHERE it goes and HOW its named
---

# Config: model_card Production Rules

## Naming
Pattern: `p02_mc_{{provider}}_{{model_slug}}.md`
- provider: lowercase, single word (anthropic, openai, google, meta, mistral, cohere, deepseek)
- model_slug: snake_case, no provider prefix, version-specific
  - opus_4 (not anthropic_opus_4, not opus)
  - gpt_4o (not openai_gpt_4o)
  - gemini_2_5_pro (not google_gemini)
- id MUST equal filename stem (validator checks this)

## File Paths
- Output: `cex/P02_model/examples/p02_mc_{{provider}}_{{slug}}.md`
- Compiled: `cex/P02_model/compiled/p02_mc_{{provider}}_{{slug}}.yaml`
- Research: `cex/.research/model_card/` (intermediate, not committed to pool)

## Size Limits
- Frontmatter: ~800-1200 bytes (26 fields)
- Body: max 3072 bytes (spec_card) or 4096 bytes (comparison_card)
- Total: max 5120 bytes (same as agent type)
- Density: >= 0.85 (higher than KC because pure spec, no narrative)

## Provider Enum
Valid: anthropic, openai, google, meta, mistral, cohere, deepseek, alibaba, ai21, other
If provider not in list: use "other" and add provider name in tags.

## Pricing Convention
- ALWAYS per_1M_tokens (never per_1K, never per_token)
- USD only (convert if provider quotes other currency)
- null for open-weight models (not 0, not "free")
- cache_read/cache_write: null if provider doesn't support caching

## Freshness
- updated field must be within 90 days of current date
- If model deprecated: status = "deprecated", linked_artifacts must point to replacement
- Stale cards (>90d) flagged by lifecycle_rule for review
