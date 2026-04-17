---
id: p03_ins_model_provider
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: instruction-builder
title: Model Provider Builder Execution Protocol
target: model-provider-builder agent
phases_count: 4
prerequisites:
  - LLM provider and account tier are identified
  - Provider API documentation is accessible (models, rate limits, pricing)
  - The provider is not already configured in the P02 examples directory
validation_method: checklist
domain: model_provider
quality: 9.1
tags: [instruction, model-provider, P02, llm-routing, fallback, rate-limit]
idempotent: true
atomic: false
rollback: "Discard generated artifact; no router configuration is modified"
dependencies: []
logging: true
tldr: Configure an LLM provider's connection parameters, tiered models, rate limits, and fallback chain from official sources into a complete model_provider artifact.
density_score: 0.91
llm_function: REASON
---
## Context
The model-provider-builder produces `model_provider` artifacts (P02) — LLM provider connection and routing configurations. Configs specify the provider API, authentication, tiered model selection, rate limits, fallback chains, retry logic, and health tracking. A model_provider is a connection/routing config, not a model_card (technical LLM spec), not an embedder_provider (embedding config), and not a boot_config (agent startup).
**Inputs:**
- `$provider (required) - string - "One of: anthropic, openai, google, ollama, groq, mistral, together, other"`
- `$tier (optional) - string - "Account tier: free, pro, team, enterprise — affects rate limits"`
- `$nucleus_assignment (optional) - string - "Which CEX nucleus this provider serves (N01-N07)"`
- `$fallback_provider (optional) - string - "Provider to fall back to when primary is unavailable"`
**Output:** A single `model_provider` artifact with 22+ frontmatter fields and 6 body sections: Boundary, Provider Matrix, Model Tiers, Fallback Chain, Rate Limit Strategy, Anti-Patterns. Body <= 4096 bytes.
## Phases
### Phase 1: Research
**Action:** Gather all provider connection specifications from official sources.
1. Identify the provider: API name, authentication method, base URL.
2. Locate official documentation:
   - Models page (available models, latest versions)
   - Rate limits page (RPM, TPM per account tier)
   - Pricing page (per-token costs for each model)
   - API reference (endpoints, headers, request format)
   - Status page (uptime, incident history)
3. Extract all schema fields:
   - `api_key_env`: environment variable for authentication
   - `api_base_url`: base URL for API requests (null if standard)
   - `models.fast`: cheapest/fastest model ID
   - `models.balanced`: mid-tier model ID
   - `models.quality`: most capable model ID
   - `rate_limit_rpm`: requests per minute for account tier
   - `rate_limit_tpm`: tokens per minute for account tier
   - `max_retries`: retry count with backoff
   - `timeout_seconds`: request timeout
   - `fallback`: fallback provider name
4. Rule: if a rate limit is unavailable, set to `null` — never estimate.
5. Check for existing model_provider artifacts for the same provider.
**Verification:** Every model ID is currently active (not deprecated). Rate limits match documented tier.
### Phase 2: Compose
**Action:** Write all frontmatter fields and body sections within the 4096-byte body limit.
1. Read SCHEMA — source of truth for all fields.
2. Read OUTPUT_TEMPLATE — fill every `{{var}}`.
3. Fill frontmatter: all required fields (`quality: null` mandatory).
4. Write `## Boundary` section — what a model_provider IS and IS NOT.
5. Write `## Provider Matrix` table:
   | Parameter | Value | Source |
   |-----------|-------|--------|
   Rows: provider, api_base_url, auth_method, api_key_env, rate_limit_rpm, rate_limit_tpm, timeout.
6. Write `## Model Tiers` table:
   | Tier | Model ID | Context | $/1M In | $/1M Out | Use Case |
   |------|----------|---------|---------|----------|----------|
   Rows: fast, balanced, quality.
7. Write `## Fallback Chain` — ordered list of fallback providers with conditions.
8. Write `## Rate Limit Strategy` — backoff algorithm, retry logic, circuit breaker.
9. Write `## Anti-Patterns` — >= 4 common mistakes.
10. Write `## References` — >= 1 official URL.
**Verification:** Every Provider Matrix row has Source URL. Model IDs are current. Body <= 4096 bytes.
### Phase 3: Validate
**Action:** Run all 10 HARD gates. Fix any failure before output.
| Gate | Check |
|------|-------|
| H01 | YAML frontmatter parses without error |
| H02 | `id` matches `^p02_mp_[a-z][a-z0-9_]+$` |
| H03 | `id` equals filename stem exactly |
| H04 | `kind` == literal string `"model_provider"` |
| H05 | `quality` == `null` |
| H06 | Required fields present: `id`, `kind`, `pillar`, `provider`, `models`, `api_key_env`, `rate_limit_rpm`, `tags`, `tldr` |
| H07 | `provider` matches a known enum value |
| H08 | `models` object has at least `fast` and `quality` keys with valid model IDs |
| H09 | `rate_limit_rpm` is a positive integer or null |
| H10 | Body <= 4096 bytes |
Score all SOFT gates. If soft score < 8.0, revise in the same pass.
### Phase 4: Deliver
**Action:** Save, compile, commit, signal.
1. Save artifact to `P02_model/examples/p02_mp_{provider}.yaml`
2. Compile: `python _tools/cex_compile.py {path}`
3. Git commit with descriptive message
4. Signal: `write_signal('n03', 'complete', {score})`
