---
kind: instruction
id: bld_instruction_rate_limit_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for rate_limit_config
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Rate Limit Config"
version: "1.0.0"
author: n03_builder
tags: [rate_limit_config, builder, examples]
tldr: "Golden and anti-examples for rate limit config construction, demonstrating ideal structure and common pitfalls."
domain: "rate limit config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Instructions: How to Produce a rate_limit_config

This ISO encodes a rate limit policy -- throttle bounds, quota windows, and backoff behavior.
## Phase 1: RESEARCH
1. Identify the provider (anthropic, openai, litellm, azure_openai, google_vertex)
2. Identify the tier (free, build, scale, enterprise, or provider-specific tier name)
3. Look up RPM and TPM from provider documentation for that exact tier
4. Record RPD (requests per day) if provider enforces a daily cap
5. Record concurrent limit (max parallel in-flight requests) if documented
6. Determine retry_after: check provider 429 response headers or docs (typically 1–60s)
7. Identify any per-model overrides (some providers have separate limits per model)
8. Get monthly budget target from user or use team default
9. Check for existing rate_limit_config artifacts to avoid duplicates
10. Confirm provider slug for id: snake_case, lowercase, no hyphens
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Set id: `p09_rl_{provider_slug}` — verify it matches `^p09_rl_[a-z][a-z0-9_]+$`
5. Write Overview section: provider name, tier, primary use case (1–2 sentences)
6. Write Limits section: table with RPM, TPM, RPD, concurrent and their values
7. Write Tier section: tier name, what it includes, upgrade path to next tier
8. Write Budget section: budget_usd, alert_threshold as percent, overage policy
9. Add model_overrides if provider enforces per-model limits
10. Verify body <= 1024 bytes (count: Overview ~80 + Limits ~250 + Tier ~150 + Budget ~150 = ~630)
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `^p09_rl_[a-z][a-z0-9_]+$`
4. Confirm kind == rate_limit_config
5. Confirm rpm and tpm are positive integers (not strings, not zero, not negative)
6. Confirm all four body sections present: Overview, Limits, Tier, Budget
7. Confirm tags list contains "rate_limit_config" and >= 3 items total
8. Confirm quality: null (never a numeric value)
9. Cross-check: are limits real provider values, not placeholder text?
10. Cross-check: does this belong in rate_limit_config vs runtime_rule (retry logic) vs env_config (generic vars)?
11. Score against SOFT gates in QUALITY_GATES.md
12. Revise if score < 8.0 before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify rate
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | rate limit config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
