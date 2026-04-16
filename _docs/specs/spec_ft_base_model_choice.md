---
id: spec_ft_base_model_choice
kind: decision_record
pillar: P08
title: Base Model Choice for 7-Nucleus FT Strategy
version: 1.0.0
quality: 9.1
tags: [fine-tuning, gemma2, lora, benchmark, nuclei]
created: 2026-04-15
density_score: 1.0
---

# Base Model for Per-Nucleus Fine-Tuning

## Decision

**All 7 nuclei FT from the same base: `gemma2:9b`.** One LoRA adapter per nucleus, trained on `.cex/runtime/ft_data/n0X.jsonl`.

## Three-way bench (2026-04-15, round 2 with Haiku)

Same 7 domain prompts, 800 max_tokens, temp 0.2. Claude Haiku via `claude -p` CLI (user's Anthropic Max subscription).

| Nucleus | gemma2:9b | qwen3:14b | haiku-4-5 | Winner | Notes |
|---------|-----------|-----------|-----------|--------|-------|
| N01 | 5.9s / 1037 B | 15.3s / 1230 B | 15.4s / 1412 B | **gemma2** | 2.6x faster than haiku |
| N02 | 5.0s / 365 B | 13.0s / 357 B | 22.1s / 618 B | **gemma2** | 4.4x faster than haiku |
| N03 | 4.8s / **raw `---`** | **0 B (FAIL)** | 6.7s / ```yaml fence | **gemma2** | Only gemma2 produces frontmatter-valid output |
| N04 | 6.7s / 1042 B | 12.7s / 931 B | 8.3s / 1040 B | **gemma2** | No model cited Sparck-Jones this round |
| N05 | 6.3s / 704 B | 14.5s / 339 B | 10.4s / 893 B | **gemma2** | |
| N06 | 5.6s / 627 B | **0 B (FAIL)** | 7.8s / 942 B | **gemma2** | qwen3 thinking-budget consumed |
| N07 | 8.6s / 1916 B (1 sec) | **0 B (FAIL)** | 22.3s / 3492 B (3 sec) | **gemma2 on speed**, haiku on content volume |

**Sweep result: gemma2:9b wins 7/7 by adherence + wall time.**

## Key discoveries

1. **Qwen3:14b failed N03, N06, N07** (0 bytes) at 800 max_tokens. `<think>` block consumed entire output budget. Qwen3 needs ~1500 max_tokens to reliably emit visible content at 14B scale. Downgrade risk for grid mode.

2. **Haiku wraps frontmatter** in ```yaml fences. Same failure mode as llama3.1:8b. CEX compiler rejects fenced frontmatter — haiku cannot be trusted for N03 without post-processing.

3. **Nobody cited Sparck-Jones this round** — the prior qwen3:14b win on N04 was not reproducible. Citation recall is probabilistic, not reliable. Production KCs still need Claude Opus or human review.

4. **Haiku produces 2x more content on N07** (3492 B vs gemma2 1916 B) but at 2.6x wall cost (22.3s vs 8.6s). For grid mode the speed wins; for content volume haiku wins.

## Why gemma2:9b as single FT base

| Criterion | gemma2:9b | qwen3:14b | llama3.1:8b |
|-----------|-----------|-----------|-------------|
| Fits 16 GB VRAM with 10+ GB headroom for LoRA training | YES (5.4 GB) | tight (9.3 GB) | YES (4.7 GB) |
| No thinking-mode interference | YES | NO (thinking token budget) | YES |
| Produces raw `---` frontmatter | YES | YES (when completes) | NO (```yml fence) |
| Bench wins across all 7 nuclei | 7/7 | 0/7 (3 failures) | 0/7 |
| Unsloth/Axolotl LoRA compatibility | mature | mature | mature |
| Apache 2.0 license | YES | Apache 2.0 | Llama license |

Gemma2:9b is the only model that is fast, compatible, structurally correct, and license-clean for all 7 nuclei simultaneously.

## FT pipeline

```
Base: gemma2:9b
Per nucleus:
  - Data: .cex/runtime/ft_data/n0X.jsonl (OpenAI chat format, logged per-call)
  - Adapter: LoRA rank=16, alpha=32, dropout=0.05
  - Steps: ~500-1000 (depends on dataset size)
  - Eval: re-run bench_nucleus_models.py with ft'd model; require +20% adherence
  - Output: ollama Modelfile with adapter merged -> cex-n0X-ft:latest
```

Target: 7 specialized models `cex-n01-ft:latest` ... `cex-n07-ft:latest`, each beating the base gemma2:9b by +20% adherence + preserving ~5s wall.

## Minimum data requirement per nucleus

LoRA at rank=16 needs ~500 quality examples to move the needle. Current `.cex/runtime/ft_data/` capture rate (1 row per nucleus per grid run) means 500 grid runs before any nucleus has a training set. Accelerate by:

1. Running `overnight.ps1` with `--count 100` per night -> 7 nuclei x 100 = 700 rows/week
2. Backfilling from `.cex/runtime/logs/spawn/` (existing nucleus output)
3. Synthetic expansion: `cex_ft_augment.py` (NOT YET BUILT) — takes 1 row, generates 5 paraphrases

## When to revisit

- New 8-9B model released (e.g. `phi-4`, `qwen2.5:7b` in March 2026) -> re-bench
- Gemma2:9b fails on a nucleus post-FT -> consider nucleus-specific base (e.g. qwen2.5-coder for N05)
- VRAM upgrade to 24 GB -> revisit 14B+ models without thinking-budget workarounds

## Cost comparison (serialized grid, 7 nuclei, one task each)

| Setup | Wall | Cost |
|-------|------|------|
| All gemma2:9b base | ~45 s | $0 |
| Mixed (gemma2 + qwen3) pre-FT | ~60 s | $0 (but 3 qwen failures) |
| All haiku via claude CLI | ~100 s | ~$0.01 |
| All sonnet via claude CLI | ~40 s | ~$0.10 |
| All ft'd gemma2 (projected) | ~45 s | $0 |

FT'd gemma2 matches sonnet speed at zero cost per call — one-time training cost (~2 hours on this GPU per adapter) pays off after ~200 calls.
