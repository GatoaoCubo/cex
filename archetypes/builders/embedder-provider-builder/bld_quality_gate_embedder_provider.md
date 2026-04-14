---
id: p11_qg_embedder_provider
kind: quality_gate
pillar: P11
title: "Gate: Embedder Provider"
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: builder_agent
domain: embedder_provider
quality: 9.0
tags: [quality-gate, embedder-provider, embedding, P01, dimensions]
tldr: "Quality gate for embedder_provider artifacts: enforces dimensions, normalization, max_tokens, and provider authentication fields."
density_score: 0.87
llm_function: GOVERN
---
# Gate: Embedder Provider
## Definition
An `embedder_provider` is a connection configuration for an embedding model: provider, model ID, dimensions, normalization, batch size, and authentication. Infrastructure artifact only — not a tutorial. Gates ensure dimension correctness, normalization explicitness, and traceability to official documentation.
## HARD Gates
All HARD gates must pass. Any single failure sets score to 0 and blocks publish.
| ID  | Check | Failure consequence |
|-----|-------|---------------------|
| H01 | YAML frontmatter parses without error | Artifact unparseable by tooling |
| H02 | `id` matches `^p01_emb_[a-z][a-z0-9_]+$` | Namespace violation — not discoverable |
| H03 | `id` equals filename stem exactly | Brain search failure — id/file mismatch |
| H04 | `kind` == literal string `"embedder_provider"` | Type integrity failure |
| H05 | `quality` == `null` | Self-scoring violation — pool metric corruption |
| H06 | Required fields present: `id`, `kind`, `pillar`, `version`, `created`, `updated`, `author`, `provider`, `model`, `dimensions`, `max_tokens`, `normalize`, `tags`, `tldr` | Incomplete artifact |
| H07 | `provider` matches a known enum (openai, cohere, voyage, jina, nomic, local, huggingface, other) | Prevents typos that break integration |
| H08 | `dimensions` is a positive integer matching official model spec | Wrong dimensions corrupt entire vector index |
| H09 | `normalize` is boolean (true/false), not string | Distance metric mismatch if ambiguous |
| H10 | Body <= 4096 bytes | Exceeds artifact size contract |
## SOFT Scoring
Weights sum to 100%. Each dimension scores 0 or its full weight.
| ID  | Dimension | Weight | Criteria |
|-----|-----------|--------|----------|
| S01 | tldr quality | 1.0 | `tldr` <= 160 chars, names provider + model + primary dimension |
| S02 | Pricing documented | 1.0 | `pricing.per_1m_tokens` present; `null` for local models |
| S03 | MTEB score referenced | 1.0 | At least one MTEB benchmark score (retrieval or STS) cited |
| S04 | Batch size documented | 1.0 | `batch_size` present with provider rate limit source |
| S05 | Matryoshka flag set | 0.5 | `matryoshka` boolean present if model supports MRL |
| S06 | Distance metric specified | 1.0 | `distance_metric` present with rationale |
| S07 | Integration code snippet | 1.0 | Body contains SDK initialization example |
| S08 | Anti-patterns documented | 1.0 | >= 4 specific anti-patterns with consequences |
| S09 | Dimension tradeoff table | 1.0 | If matryoshka: comparison of native vs reduced dimensions |
| S10 | `api_key_env` present | 0.5 | Environment variable name for authentication |
| S11 | `max_tokens` matches provider docs | 0.5 | Verified against official API limits |
| S12 | Density >= 0.85 | 1.0 | No filler: "powerful", "state-of-the-art", "best-in-class" |
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
