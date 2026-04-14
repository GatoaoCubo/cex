---
id: p11_qg_model_provider
kind: quality_gate
pillar: P11
title: "Gate: Model Provider"
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: builder_agent
domain: model_provider
quality: 9.0
tags: [quality-gate, model-provider, llm-routing, P02, fallback]
tldr: "Quality gate for model_provider artifacts: enforces tiered models, rate limits, fallback chain, and provider authentication fields."
density_score: 0.87
llm_function: GOVERN
---
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
