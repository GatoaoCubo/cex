---
id: spec_local_model_per_nucleus
kind: decision_record
pillar: P08
title: Best Local Model per CEX Nucleus (Free Mode)
version: 1.0.0
quality: 9.0
tags: [ollama, benchmark, routing, nuclei, free-mode]
created: 2026-04-15
density_score: 1.0
---

# Best Local Model per Nucleus (measured, not guessed)

## Hardware baseline

RTX 5070 Ti, 16 GB VRAM. Models that overflow VRAM (>14 GB resident) thrash via CPU offload (prior memory: gemma4:26b at 10.1 eff TPS — disqualified for grid).

## Candidates benchmarked (2026-04-15)

| Model | Size | Family | Quant | Fits 16GB | Thinking mode |
|-------|------|--------|-------|-----------|---------------|
| qwen3:8b | 5.2 GB | Qwen3 | Q4_K_M | yes | yes (`<think>`) |
| qwen3:14b | 9.3 GB | Qwen3 | Q4_K_M | yes | yes (`<think>`) |
| llama3.1:8b | ~4.7 GB | Llama 3 | Q4 | yes | no |
| gemma4:26b | 18.0 GB | Gemma | Q4_K_M | NO (overflow) | no |

Bench: `_tools/bench_nucleus_models.py` — one domain prompt per nucleus (N01–N07), 800 tokens max, temp 0.2, measured wall + TPS + structural adherence + content byte count.

## Per-nucleus winners (measured)

| Nucleus | Task signature | Winner | Wall (s) | Rationale |
|---------|----------------|--------|----------|-----------|
| N01 research | Analyze competitor claim with sections | llama3.1:8b | 5.7 | 2× faster; adequate structural quality |
| N02 marketing | Landing-page hero copy | llama3.1:8b | 5.0 | Fastest; 672 B output vs 346 B (qwen3:8b) |
| N03 build | YAML frontmatter scaffold | **qwen3:14b** | 11.6 | **Only model producing raw `---` frontmatter (llama wraps in ```yml)** |
| N04 knowledge | Explain TF-IDF with citations | **qwen3:14b** | 12.7 | **Cites Sparck-Jones 1972; llama skips citations entirely** |
| N05 ops | Shell one-liner with flag explanation | llama3.1:8b | 6.0 | **qwen3:8b FAILED (0 bytes, thinking-budget consumed output)** |
| N06 commercial | 3-tier pricing table | llama3.1:8b | 6.2 | Produces proper markdown table; 1411 B content |
| N07 orchestrate | 3-wave dispatch plan | llama3.1:8b | 6.8 | Longer structured plans (1664 B vs 735 B for qwen3:14b) |

## Why not qwen3 everywhere

Qwen3 is a thinking model — it emits `<think>...</think>` blocks before the actual answer. Under a constrained `max_tokens`, the thinking block can consume the entire budget and return zero user-visible content. N05 benchmark: qwen3:8b produced **0 bytes of usable output** on the ops prompt at 800 max_tokens.

llama3.1:8b has no thinking overhead — every generated token contributes to visible output. On 5 of 7 nuclei this yields both speed and byte-count wins.

## Why qwen3:14b still wins N03 and N04

Frontmatter fidelity (N03): CEX compiler requires `---\n...\n---\n` blocks. llama3.1:8b wraps YAML in triple-backtick fences (```yml ... ```) — invalid frontmatter. qwen3:14b produces the raw `---` block every time. No post-processing needed.

Citation recall (N04): On "explain TF-IDF" qwen3:14b named Karen Sparck-Jones and cited her 1972 paper (real reference, title paraphrased slightly). llama3.1:8b followed the fallback instruction ("classical IR technique") and omitted the citation. For KCs we want named references — qwen wins, even if titles need human verification.

## Fabrication risk reminder

Both qwen3:14b and llama3.1:8b will fabricate under pressure to fill an "Evidence" section. Prior A/B (`.cex/runtime/out/kc_litellm_free_first.md`) showed qwen3:14b inventing 5 data points when producing a full KC. This is NOT a model-pick issue — it is a **genre** issue. Any free model producing a `knowledge_card` or `decision_record` needs human review before commit.

Router rule (`_tools/cex_router_v2.py`): when task signature is `production_kc` and Anthropic credit > 0, use Claude Opus. Otherwise use `ollama/qwen3:14b + human review` and mark explicitly.

## Updated config

`.cex/config/litellm_config.yaml` now maps:

```yaml
cex-n01, n02, n05, n06, n07 -> ollama/llama3.1:8b   # speed + adequate quality
cex-n03, n04               -> ollama/qwen3:14b      # fidelity-critical
```

Previous mapping (all qwen3) still works but is 2–3× slower for 5/7 nuclei and FAILS for N05.

## Estimated grid wall (serialized, single GPU)

| Mapping | 6-nucleus SMOKE grid | Notes |
|---------|----------------------|-------|
| Old (all qwen3) | 227 s | measured 2026-04-15 round 3 |
| New (5 llama + 2 qwen) | ~55 s | projected: 5×6 + 2×12 |

~4× speedup on grid mode for the same hardware.

## Future candidates (not yet tested)

- `phi-4:14b` (Microsoft reasoning, fits 16 GB)
- `deepseek-r1:8b` (reasoning distilled, thinking model — likely same budget issue as qwen)
- `mistral:7b` (older but fast baseline)
- `qwen2.5-coder:7b` (candidate for N05 ops)

Add to bench with: `python _tools/bench_nucleus_models.py --models "qwen3:14b,llama3.1:8b,phi-4:14b"`.
