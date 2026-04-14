---
id: p11_qg_model_card
kind: quality_gate
pillar: P11
title: "Gate: Model Card"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder_agent
domain: model_card
quality: 9.0
tags: [quality-gate, model-card, llm-spec, P02, provider]
tldr: "Quality gate for model_card artifacts: enforces provider, context window, pricing, and capabilities fields."
density_score: 0.85
llm_function: GOVERN
---
# Gate: Model Card
## Definition
A `model_card` is a technical spec for a language model: provider, context window, pricing in $/1M tokens, and boolean capability flags. Reference artifact only — not a tutorial. Gates ensure traceability to official sources, comparable pricing, and freshness within 90 days.
## HARD Gates
All HARD gates must pass. Any single failure sets score to 0 and blocks publish.
| ID  | Check | Failure consequence |
|-----|-------|---------------------|
| H01 | YAML frontmatter parses without error | Artifact unparseable by tooling |
| H02 | `id` matches `^p02_mc_[a-z][a-z0-9_]+$` | Namespace violation — not discoverable |
| H03 | `id` equals filename stem exactly | Brain search failure — id/file mismatch |
| H04 | `kind` == literal string `"model_card"` | Type integrity failure |
| H05 | `quality` == `null` | Self-scoring violation — pool metric corruption |
| H06 | Required fields present and non-empty: `id`, `kind`, `pillar`, `version`, `created`, `updated`, `author`, `provider`, `model_name`, `context_window`, `pricing`, `capabilities`, `tags`, `tldr` | Incomplete artifact |
| H07 | `provider` matches a known provider enum (Anthropic, OpenAI, Google, Meta, Mistral, Cohere, or documented costm) | Prevents typos that break routing |
| H08 | `context_window` is a positive integer | Core spec field — must be exact |
| H09 | `pricing` field present with at least `input` and `output` keys (numeric $/1M tokens, or `null` for open-weight) | Non-comparable pricing blocks cost analysis |
| H10 | `capabilities` field is a map of boolean flags | Capability claims require verifiable binary form |
## SOFT Scoring
Weights sum to 100%. Each dimension scores 0 or its full weight.
| ID  | Dimension | Weight | Criteria |
|-----|-----------|--------|----------|
| S01 | tldr quality | 1.0 | `tldr` <= 160 chars, names provider + model + primary use case |
| S02 | Pricing normalized to $/1M tokens | 1.0 | Both `input` and `output` prices in $/1M tokens; `null` for open-weight |
| S03 | Capabilities list complete | 1.0 | Flags: vision, audio, function_calling, streaming, fine_tuning, json_mode, code, reasoning |
| S04 | Benchmarks referenced | 1.0 | >= 1 public benchmark (MMLU, HumanEval, MATH) with score and date |
| S05 | Limitations documented | 1.0 | >= 2 specific limitations: context degradation, refusal patterns, knowledge cutoff |
| S06 | `tags` includes `"model-card"` | 0.5 | Minimum tag for routing |
| S07 | Use-case recommendations present | 1.0 | >= 3 recommended use cases and >= 1 not-recommended |
| S08 | API endpoint documented | 0.5 | Names the model identifier string used in API calls |
| S09 | Comparison to alternatives noted | 0.5 | >= 1 comparable model named with key difference stated |
| S10 | Version and spec date accurate | 1.0 | `updated` within 90 days; `data_source` is a live URL |
| S11 | `max_output` field present and positive integer | 0.5 | Required for prompt budget calculations |
| S12 | Density >= 0.85 | 1.0 | No narrative: "great for", "one of the best", "in summary" |
| S13 | `linked_artifacts` field present | 0.5 | Lists related model cards, lenses, or routing rules |
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
