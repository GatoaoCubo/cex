---
kind: quality_gate
id: p11_qg_model_provider
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of model_provider artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: Model Provider"
version: "1.0.0"
author: builder_agent
tags: [quality-gate, model-provider, llm-routing, P02, fallback]
tldr: "Quality gate for model_provider artifacts: enforces tiered models, rate limits, fallback chain, and provider authentication fields."
domain: model_provider
created: "2026-04-06"
updated: "2026-04-06"
density_score: 0.87
related:
  - p03_ins_model_provider
  - bld_examples_model_provider
  - p01_kc_model_provider
  - p11_qg_embedder_provider
  - p03_sp_model_provider_builder
  - model-provider-builder
  - p11_qg_model_card
  - bld_knowledge_card_model_provider
  - bld_collaboration_model_provider
  - bld_config_model_provider
---

## Quality Gate

# Gate: Model Provider
## Definition
A `model_provider` is a connection and routing configuration for an LLM API: provider, tiered models (fast/balanced/quality), rate limits (RPM/TPM), fallback chain, and authentication. Infrastructure artifact only — not a tutorial. Gates ensure model IDs are current, rate limits are documented, and fallback chains are complete.
## HARD Gates
All HARD gates must pass. Any single failure sets score to 0 and blocks publish.
| ID  | Check | Failure consequence |
|-----|-------|---------------------|
| H01 | YAML frontmatter parses without error | Artifact unparseable by tooling |
| H02 | `id` matches `^p02_mp_[a-z][a-z0-9_]+$` | Namespace violation — not discoverable |
| H03 | `id` equals filename stem exactly | Brain search failure — id/file mismatch |
| H04 | `kind` == literal string `"model_provider"` | Type integrity failure |
| H05 | `quality` == `null` | Self-scoring violation — pool metric corruption |
| H06 | Required fields present: `id`, `kind`, `pillar`, `version`, `created`, `updated`, `author`, `provider`, `models`, `api_key_env`, `rate_limit_rpm`, `tags`, `tldr` | Incomplete artifact |
| H07 | `provider` matches a known enum (anthropic, openai, google, ollama, groq, mistral, together, other) | Prevents typos that break routing |
| H08 | `models` object has at least `fast` and `quality` keys | Tiered routing requires minimum two tiers |
| H09 | Model IDs in `models` are currently active (not deprecated) | Deprecated models fail at runtime |
| H10 | Body <= 4096 bytes | Exceeds artifact size contract |
## SOFT Scoring
Weights sum to 100%. Each dimension scores 0 or its full weight.
| ID  | Dimension | Weight | Criteria |
|-----|-----------|--------|----------|
| S01 | tldr quality | 1.0 | `tldr` <= 160 chars, names provider + model tier range |
| S02 | Rate limits documented | 1.0 | Both `rate_limit_rpm` and `rate_limit_tpm` present with source |
| S03 | Fallback configured | 1.0 | `fallback` field present with a valid provider name |
| S04 | All three tiers populated | 1.0 | `models.fast`, `models.balanced`, `models.quality` all present |
| S05 | Pricing per tier documented | 1.0 | Body Model Tiers table includes $/1M input and output per model |
| S06 | Retry strategy documented | 1.0 | `max_retries` present; body describes backoff algorithm |
| S07 | Health check configured | 0.5 | `health_check_interval` present |
| S08 | Anti-patterns documented | 1.0 | >= 4 specific anti-patterns with consequences |
| S09 | Nucleus assignment noted | 0.5 | `nucleus_assignment` field maps provider to CEX nuclei |
| S10 | `timeout_seconds` present | 0.5 | Required for request timeout management |
| S11 | `auth_method` documented | 0.5 | Specifies bearer, api-key, oauth, or none |
| S12 | Density >= 0.85 | 1.0 | No filler: "industry-leading", "robust", "comprehensive" |
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool + record in memory |
| >= 8.0 | PUBLISH | Commit to pool |
| >= 7.0 | REVIEW | Acceptable with documented improvement items |
| < 7.0 | REJECT | Revise and resubmit — do not publish |
| 0 (HARD fail) | REJECTED | Fix failing HARD gate(s) first |
## Bypass
Bypasses are logged and expire automatically.
| Field | Value |
|-------|-------|

## Examples

# Examples: model-provider-builder
## Golden Example
INPUT: "Configure Anthropic provider for CEX with Max subscription"
OUTPUT:
```yaml
id: p02_mp_anthropic
kind: model_provider
pillar: P02
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "builder_agent"
provider: "anthropic"
api_key_env: "ANTHROPIC_API_KEY"
api_base_url: null
auth_method: "api-key"
models:
  fast: "claude-haiku-3.5"
  balanced: "claude-sonnet-4-6"
  quality: "claude-opus-4-6"
rate_limit_rpm: 4000
rate_limit_tpm: 400000
max_retries: 3
timeout_seconds: 120
fallback: "openai"
health_check_interval: 60
cost_aware: true
nucleus_assignment: [N02, N03, N06, N07]
domain: llm_routing
quality: null
tags: [model-provider, anthropic, claude, multi-tier]
tldr: "Anthropic — claude-haiku/sonnet/opus tiers, 4K RPM (Max), fallback to OpenAI, cost-aware routing"
keywords: [anthropic, claude, llm-routing, fallback]
linked_artifacts:
  primary: null
  related: [p02_mp_openai, p02_mp_google]
data_source: "https://docs.anthropic.com/en/api/rate-limits"
## Boundary
model_provider IS: connection and routing config for Anthropic API (models, rate limits, fallback).
model_provider IS NOT: model_card, embedder_provider, agent, boot_config.
## Provider Matrix
| Parameter | Value | Source |
|-----------|-------|--------|
| Provider | anthropic | https://docs.anthropic.com/en/api |
| API Base | https://api.anthropic.com | https://docs.anthropic.com/en/api |
| Auth Method | api-key (x-api-key header) | https://docs.anthropic.com/en/api/getting-started |
| RPM (Max tier) | 4000 | https://docs.anthropic.com/en/api/rate-limits |
| TPM (Max tier) | 400000 | https://docs.anthropic.com/en/api/rate-limits |
| Timeout | 120s | CEX convention |
## Model Tiers
| Tier | Model ID | Context | $/1M In | $/1M Out | Use Case |
|------|----------|---------|---------|----------|----------|
| fast | claude-haiku-3.5 | 200K | $0.80 | $4.00 | Classification, formatting, simple Q&A |
| balanced | claude-sonnet-4-6 | 200K | $3.00 | $15.00 | Research, analysis, general coding |
| quality | claude-opus-4-6 | 200K | $15.00 | $75.00 | Complex architecture, multi-file refactors |
## Fallback Chain
1. Primary: anthropic (claude-sonnet-4-6)
2. Fallback 1: openai (gpt-4o) — trigger: anthropic 429 or 5xx for > 30s
3. Fallback 2: google (gemini-2.5-pro) — trigger: both anthropic and openai unavailable
4. Circuit breaker: open after 3 consecutive failures, half-open after 60s
## Rate Limit Strategy
- Algorithm: exponential backoff with jitter (base=1s, max=60s)
- Retry: max 3 attempts, then fallback to next provider
- RPM tracking: sliding window per provider
- TPM tracking: token count per response, rolling 60s window
- 429 handling: immediate switch to fallback, mark provider degraded
## Anti-Patterns
1. Using `gpt-4` instead of `gpt-4o-2024-08-06` — unversioned aliases change without notice
2. Setting rate_limit_rpm to provider max without checking account tier — causes 429 cascades
3. No fallback configured — single provider outage takes down entire system
4. Retry without backoff — amplifies rate limit violations, accelerates account throttling
## References
- api: https://docs.anthropic.com/en/api
- rate-limits: https://docs.anthropic.com/en/api/rate-limits
- models: https://docs.anthropic.com/en/docs/about-claude/models
- pricing: https://docs.anthropic.com/en/docs/about-claude/pricing
```
WHY THIS IS GOLDEN:
- Every Provider Matrix row has Source URL (never `-`)
- Model IDs are current and versioned
- Rate limits match specific account tier (Max)
- Fallback chain has clear trigger conditions
- quality: null
- Anti-patterns are concrete with consequences
## Anti-Example
INPUT: "Configure OpenAI provider"
BAD OUTPUT:
```yaml
id: openai_config
kind: provider
provider: OpenAI
api_key: "sk-abc123..."
model: "gpt-4"
rate_limit: "high"
quality: 9.2
OpenAI is one of the leading AI providers. They offer powerful models
for various use cases. Contact sales for enterprise pricing.
```
FAILURES:
1. id: no `p02_mp_` prefix — H02 FAIL
2. kind: "provider" not "model_provider" — H04 FAIL
3. provider: uppercase — H07 FAIL
4. api_key: hardcoded secret — SECURITY VIOLATION
5. model: single unversioned model, no tiers — H08 FAIL
6. rate_limit: string not integer — H09 FAIL
7. quality: self-assigned 9.2 — H05 FAIL
8. No fallback configured — S03 FAIL
9. Body: marketing prose, no Provider Matrix — density FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
