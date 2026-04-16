---
id: spec_agentic_capabilities_findings
kind: decision_record
pillar: P08
title: Agentic Capabilities Bench — Free Model Selection
version: 1.0
date: 2026-04-15
quality: 9.1
tags: [agentic, free-models, ollama, benchmark, fine-tuning]
density_score: 1.0
---

# Agentic Capabilities — 12-Experiment Bench

## TL;DR

- **llama3.1:8b** (11.67/12) is the agentic base. Only model that passes native tool calling + multi-turn + ReAct loop + code correctness.
- **gemma2:9b** (11.00/12) is the structural base. Fails only native tool calling (E1). Use for single-shot generation.
- **qwen3:14b** (8.00/12) is disqualified for agentic. `<think>` blocks eat budget; loses multi-turn coherence and tool-loop state.

## Methodology

12 experiments across 3 Ollama models via `/api/chat` (temp=0.2, num_predict=600-800). Each probes a distinct agentic capability. Pass = behavioral match, not vibes.

| # | Experiment | What it measures |
|---|---|---|
| E1 | native_tools | Emits `tool_calls` with `tools:` param |
| E2 | react_text | Parses `Action: tool(args)` format |
| E3 | json_mode | Valid JSON with required keys via `format:json` |
| E4 | multiturn | Recalls fact from 3 turns back |
| E5 | fewshot | Few-shot beats zero-shot on strict extraction |
| E6 | selfcritique | Generate -> critique -> improve, adds detail |
| E7 | long_context | Needle in 3K-char haystack |
| E8 | code_correct | Python `fib(n)` passes 4 exec tests |
| E9 | error_recovery | Adapts path after tool error |
| E10 | planning | 5-step numbered decomposition |
| E11 | tool_loop | 3-turn ReAct: list -> read -> done |
| E12 | strict_format | 4 markdown sections in exact order |

## Raw Scores

| Experiment | gemma2:9b | qwen3:14b | llama3.1:8b |
|---|---|---|---|
| E1 native_tools | **0** NO_TOOL | 1.0 | 1.0 |
| E2 react_text | 1.0 | 1.0 | 1.0 |
| E3 json_mode | 1.0 | 1.0 | 1.0 |
| E4 multiturn | 1.0 | **0.7** PARTIAL | 1.0 |
| E5 fewshot | 1.0 | 1.0 | 1.0 |
| E6 selfcritique | 1.0 | 0.33 PARTIAL | **0.67** PARTIAL |
| E7 long_context | 1.0 | 1.0 | 1.0 |
| E8 code_correct | 1.0 | **0** NO_FUNC | 1.0 |
| E9 error_recovery | 1.0 | **0** FAIL | 1.0 |
| E10 planning | 1.0 | 1.0 | 1.0 |
| E11 tool_loop | 1.0 | **0** FAIL | 1.0 |
| E12 strict_format | 1.0 | 1.0 | 1.0 |
| **TOTAL** | **11.00** | **8.00** | **11.67** |

## Capability Matrix (what each model CAN do)

| Capability | gemma2:9b | qwen3:14b | llama3.1:8b |
|---|---|---|---|
| Native `tool_calls` emission | NO | YES | YES |
| ReAct text parsing | YES | YES | YES |
| JSON mode | YES | YES | YES |
| Multi-turn recall | YES | DEGRADED | YES |
| Long context needle | YES | YES | YES |
| Code generation + exec | YES | NO | YES |
| Tool-error recovery | YES | NO | YES |
| Multi-turn ReAct loop | YES | NO | YES |
| Strict markdown format | YES | YES | YES |

## Decision (FINAL, 2026-04-15)

### Single agentic base for ALL 7 nuclei: `llama3.1:8b`

**Rationale**: Tools are the leverage mechanism. An agent without tool calling is a text generator. gemma2:9b CANNOT emit native `tool_calls` (E1 fail, 0%). Even though gemma2:9b won the previous 7-nucleus structural bench 7/7, that bench was single-shot. Once tools enter the equation, llama3.1:8b > gemma2:9b because ReAct text parsing is fragile while native tool calls are robust.

Additionally, grid proof (`LEVERAGE_MAP` mission, 2026-04-15) demonstrated llama3.1:8b running all 6 nuclei interactively with 4 tools (list_dir, read_file, grep, done) on a single RTX 5070 Ti 16GB via Ollama queue.

### Why NOT gemma2:9b anymore

- No native `tool_calls` emission (E1: 0/1.0)
- ReAct text-only is fragile at scale (regex parsing breaks, no OpenAI standard)
- Marginal structural quality advantage does NOT compensate for missing tool loop

### Why NOT qwen3:14b

- `<think>` blocks consume 40-60% of `num_predict` before real output starts
- Multi-turn state gets overwritten by thinking; E4, E11, E9, E8 all fail
- 2.7x slower than llama3.1:8b AND less capable for agentic work

### FT strategy

**v1 (first build)**: ONE shared LoRA over `llama3.1:8b` → `cex-llama3.1:8b-ft:latest`
- Training data: combined FT logs from all 7 nuclei
- Simpler to train, larger dataset, cheaper to serve

**v2 (conditional)**: 7 per-nucleus LoRAs IF measured quality gap > 10% per sin/domain
- N02 Luxúria (marketing voice)
- N05 Operations (code/test precision)
- etc.
- Only train these if v1 LoRA underperforms on domain-specific benchmarks

gemma2:9b is **archived** from roadmap — not retrained, not routed.

## Architecture

```
User intent
    |
    v
N07 Orchestrator (Claude opus-4-6)
    |
    +--> cex_agentic_nucleus.py (llama3.1:8b + LoRA)
    |         |
    |         +--> Tools: list_dir, read_file, grep, done
    |         +--> (to add) cex_retriever, cex_validator, cex_web_fetch, etc.
    |         +--> ReAct loop, max 15 iters
    |         +--> Auto git commit on complete
    |
    +--> Grid dispatcher (_spawn/spawn_grid_ollama.ps1)
              |
              +--> 6 interactive windows, 3x2 positioned
              +--> User can observe + correct in real-time
              +--> Each window runs full 8F via cex_agentic_nucleus.py
```

## Hardware Baseline

- RTX 5070 Ti, 16 GB VRAM, `OLLAMA_NUM_PARALLEL=3`
- llama3.1:8b = 4.9 GB; gemma2:9b = 5.4 GB; qwen3:14b = 9.3 GB
- Wall time (12 experiments): gemma2 = 41s, llama3.1 = 39s, qwen3 = 109s
- qwen3 is ~2.7x slower AND less capable for agentic work

## Next Steps

1. Build `_tools/cex_agentic_nucleus.py` — ReAct loop on llama3.1:8b with per-nucleus tool allowlist
2. Create `.cex/config/nucleus_tools.yaml` — which tools each nucleus (N01-N07) can invoke
3. Update `.cex/config/litellm_config.yaml` — add `llama3.1:8b` as alternate `ollama_agentic` model
4. Capture FT data from agentic runs into `.cex/runtime/ft_data/n0X_agentic.jsonl`

## Source Data

- v1 results: `.cex/runtime/benchmarks/agentic/agentic_capabilities_*.json`
- v2 results: `.cex/runtime/benchmarks/agentic/agentic_capabilities_v2_*.json`
- v1 script: `_tools/test_agentic_capabilities.py`
- v2 script: `_tools/test_agentic_capabilities_v2.py`
