---
id: spec_vllm_lora_hotswap
kind: spec
title: "vLLM LoRA Hot-Swap Architecture"
version: 1.0.0
quality: 9.0
tags: [vllm, lora, inference, wsl2, cuda, architecture]
pillar: P08
created: 2026-04-13
density_score: 1.0
---

# vLLM LoRA Hot-Swap Architecture

## Overview

This spec defines how CEX runs local inference with **one base model** and
**seven LoRA adapters** (one per nucleus) using vLLM inside WSL2 with CUDA
passthrough. The key insight: LoRA adapters share the base model weights,
so 7 specialized nuclei cost only ~1% more VRAM than a single model.

## Architecture

```
 Windows 11 (Host)
 +-------------------------------------------------------------+
 |                                                               |
 |  CEX Nuclei (N01-N07)                                        |
 |    |                                                          |
 |    v                                                          |
 |  LiteLLM Proxy (:4000)                                       |
 |    | model="cex-n03" -> route to vLLM with LoRA              |
 |    | model="anthropic/opus" -> route to Anthropic API         |
 |    |                                                          |
 |    v                                                          |
 |  WSL2 (Ubuntu 24.04)                                          |
 |  +-----------------------------------------------------------+|
 |  |                                                           ||
 |  |  vLLM Server (:8000, OpenAI-compatible API)               ||
 |  |  +-------------------------------------------------------+||
 |  |  |                                                       |||
 |  |  |  Base Model (gemma-3-27b-it or qwen3-14b)             |||
 |  |  |  ~14GB VRAM (AWQ 4-bit) or ~10GB (qwen3-14b 4-bit)   |||
 |  |  |                                                       |||
 |  |  |  LoRA Adapter Pool:                                   |||
 |  |  |  +--------------------------------------------------+ |||
 |  |  |  | cex-n01 (research)    ~50MB  rank-64  |          | |||
 |  |  |  | cex-n02 (marketing)   ~50MB  rank-64  |          | |||
 |  |  |  | cex-n03 (builder)     ~50MB  rank-64  | HOT      | |||
 |  |  |  | cex-n04 (knowledge)   ~50MB  rank-64  | SWAP     | |||
 |  |  |  | cex-n05 (operations)  ~50MB  rank-64  | PER      | |||
 |  |  |  | cex-n06 (commercial)  ~50MB  rank-64  | REQUEST  | |||
 |  |  |  | cex-n07 (orchestrator)~50MB  rank-64  |          | |||
 |  |  |  +--------------------------------------------------+ |||
 |  |  |                                                       |||
 |  |  |  Total VRAM: base(14GB) + lora_pool(~350MB) = ~14.3GB|||
 |  |  +-------------------------------------------------------+||
 |  |                                                           ||
 |  |  NVIDIA CUDA (passthrough from Windows driver)            ||
 |  +-----------------------------------------------------------+|
 |                                                               |
 |  RTX 5070 Ti (16GB VRAM, Blackwell SM_120)                   |
 +-------------------------------------------------------------+
```

## How LoRA Hot-Swap Works

### The Problem

Without LoRA, running 7 specialized models requires 7x VRAM (7 * 14GB = 98GB).
Ollama can swap models but must unload/reload the entire model per switch
(~10-30 seconds cold swap, serial only).

### The Solution

LoRA (Low-Rank Adaptation) adds small adapter matrices on top of frozen base
weights. vLLM loads ALL adapters into VRAM simultaneously alongside the base
model. Per-request, the adapter is selected by the `model` parameter:

```
POST /v1/chat/completions
{
  "model": "cex-n03",     <-- selects LoRA adapter for N03
  "messages": [...]
}
```

### Request Flow

```
  Nucleus N03 sends request
        |
        v
  LiteLLM (:4000)
  - Matches model="cex-n03" in litellm_config.yaml
  - Routes to: openai/cex-n03 at http://localhost:8000
        |
        v
  vLLM (:8000)
  - Receives model="cex-n03"
  - Looks up LoRA module: cex-n03 -> /mnt/c/.../cex-n03-qlora/
  - Runs inference: base_model_weights + cex-n03_lora_weights
  - Returns completion
        |
        v
  Nucleus N03 receives response
```

### Concurrency (the key advantage)

vLLM uses **continuous batching** (industry: iteration-level scheduling).
Multiple requests from different nuclei are batched in a single forward pass:

```
  Time -->
  
  Ollama (serial):
  |==N01==|==N03==|==N05==|==N02==|  (4 requests = 4x latency)
  
  vLLM (batched):
  |==N01+N03+N05+N02==|             (4 requests = ~1.2x latency)
```

With `--max-num-seqs 6`, vLLM processes up to 6 nucleus requests simultaneously.
Each request can use a different LoRA adapter. The base model weights are shared.

## VRAM Budget

### RTX 5070 Ti (16GB)

| Component | VRAM | Notes |
|-----------|------|-------|
| Base model (gemma-3-27b AWQ 4-bit) | ~14.0 GB | Quantized weights |
| 7 LoRA adapters (rank-64 each) | ~0.35 GB | 7 * ~50MB |
| KV cache (6 concurrent seqs) | ~1.0 GB | Depends on max_model_len |
| CUDA overhead | ~0.3 GB | Driver, context |
| **Total** | **~15.65 GB** | Fits in 16GB |

### Fallback: Qwen3-14B (more headroom)

| Component | VRAM | Notes |
|-----------|------|-------|
| Base model (qwen3-14b AWQ 4-bit) | ~8.0 GB | Smaller model |
| 7 LoRA adapters (rank-64 each) | ~0.25 GB | Smaller layers |
| KV cache (6 concurrent seqs) | ~1.5 GB | More room for longer context |
| CUDA overhead | ~0.3 GB | Driver, context |
| **Total** | **~10.05 GB** | 6GB headroom |

### Tuning `--gpu-memory-utilization`

| Setting | Behavior |
|---------|----------|
| 0.90 (default) | Uses 14.4GB of 16GB. Safe for gemma-3-27b. |
| 0.85 | Uses 13.6GB. Safer, less KV cache. |
| 0.95 | Uses 15.2GB. Maximum throughput, risk of OOM on long seqs. |

## LoRA Adapter Training

### Training Stack

```
Dataset:       _data/ft/ft_n0X.jsonl (per-nucleus training data)
Framework:     Unsloth (4-bit QLoRA, 2x faster than HF PEFT)
Base model:    google/gemma-3-27b-it (or Qwen/Qwen3-14B)
Output:        _data/ft/adapters/cex-n0X-qlora/
  |-- adapter_config.json
  |-- adapter_model.safetensors
```

### Training Parameters (recommended)

| Parameter | Value | Why |
|-----------|-------|-----|
| LoRA rank | 64 | Enough capacity for domain specialization |
| LoRA alpha | 128 | 2x rank (standard ratio) |
| Target modules | q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj | Full attention + FFN |
| Learning rate | 2e-4 | Standard for QLoRA |
| Epochs | 3-5 | Per-nucleus dataset is small (~500 examples) |
| Max seq len | 4096 | Covers most CEX artifacts |
| Quantization | 4-bit NF4 | Fits training on 16GB |

### Adapter Directory Structure

```
_data/ft/adapters/
  cex-n01-qlora/
    adapter_config.json        # LoRA config (rank, alpha, target_modules)
    adapter_model.safetensors  # Trained weights (~50MB)
  cex-n02-qlora/
    ...
  cex-n03-qlora/
    ...
  (one directory per nucleus)
```

## Performance Comparison

### Ollama (current) vs vLLM (target)

| Dimension | Ollama | vLLM |
|-----------|--------|------|
| Concurrency | 1 (serial) | 6 (batched) |
| Model switching | 10-30s cold swap | 0ms (LoRA hot-swap) |
| Throughput (tok/s) | ~30-40 | ~120-200 (batched) |
| API compatibility | OpenAI-like | Full OpenAI |
| LoRA support | Modelfile ADAPTER | Native --enable-lora |
| Memory efficiency | 1 model at a time | 1 base + N adapters |
| Platform | Native Windows | WSL2 (CUDA passthrough) |
| Continuous batching | No | Yes |
| PagedAttention | No | Yes (memory-efficient KV cache) |
| Speculative decoding | No | Yes (future) |

### Latency Estimates (RTX 5070 Ti)

| Scenario | Ollama | vLLM |
|----------|--------|------|
| 1 request, 500 tokens | ~12s | ~8s |
| 6 concurrent, 500 tokens each | ~72s (serial) | ~15s (batched) |
| Model switch (N01 -> N03) | ~15s | 0ms |
| Full grid (6 nuclei) | ~5min | ~30s |

## LiteLLM Integration

### litellm_config.yaml additions

```yaml
# vLLM local backend (add after existing entries)
model_list:
  # --- vLLM base model (no LoRA) ---
  - model_name: cex-local-base
    litellm_params:
      model: openai/base
      api_base: http://localhost:8000/v1
      api_key: dummy  # vLLM does not require auth

  # --- vLLM with per-nucleus LoRA ---
  - model_name: cex-n01-local
    litellm_params:
      model: openai/cex-n01
      api_base: http://localhost:8000/v1
      api_key: dummy

  - model_name: cex-n03-local
    litellm_params:
      model: openai/cex-n03
      api_base: http://localhost:8000/v1
      api_key: dummy

  # ... (one entry per nucleus with trained LoRA)
```

### Fallback Chain (updated)

```
cex-n03:
  1. anthropic/claude-opus-4-6      (cloud, best quality)
  2. gemini/gemini-2.5-flash         (cloud, fast fallback)
  3. openai/cex-n03 @ localhost:8000  (local, vLLM + LoRA)
  4. ollama/qwen3:14b                 (local, no LoRA)
```

The vLLM entry slots in as a local fallback: better than raw Ollama (batched
+ LoRA), cheaper than cloud (zero cost), but lower quality than Opus/Sonnet.

## Deployment Topology

### Development (single machine)

```
  Windows 11 (RTX 5070 Ti 16GB)
  +-- LiteLLM (:4000)  -- routes all traffic
  +-- vLLM/WSL2 (:8000) -- local inference
  +-- Ollama (:11434)   -- fallback / other models
  +-- Claude Code       -- N07 orchestrator
```

### Future: Multi-GPU / Remote

```
  Windows 11 (orchestrator)            Linux Server (inference)
  +-- LiteLLM (:4000) ---- SSH -----> +-- vLLM (:8000)
  +-- Claude Code                      +-- 2x RTX 4090 (48GB total)
                                       +-- tensor parallel across GPUs
```

vLLM supports `--tensor-parallel-size N` for multi-GPU inference.
The API remains identical; only the base URL in litellm_config changes.

## Operational Procedures

### Start Server

```powershell
# Default (gemma-3-27b, port 8000, LoRA enabled)
powershell -File boot/vllm_server.ps1

# Qwen3 fallback (smaller, no HF token needed)
powershell -File boot/vllm_server.ps1 -Model "Qwen/Qwen3-14B" -MaxModelLen 32768

# No LoRA (base model only)
powershell -File boot/vllm_server.ps1 -NoLoRA
```

### Health Check

```bash
# List served models
curl http://localhost:8000/v1/models

# Test base model
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"base","messages":[{"role":"user","content":"hello"}],"max_tokens":50}'

# Test LoRA adapter
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"cex-n03","messages":[{"role":"user","content":"hello"}],"max_tokens":50}'
```

### Monitor GPU

```powershell
# From Windows (works for both host and WSL processes)
nvidia-smi

# Continuous monitoring
nvidia-smi -l 5
```

### Stop Server

```
Ctrl+C in the vllm_server.ps1 terminal (sends SIGTERM to vLLM inside WSL)
```

## Known Limitations

| Limitation | Impact | Workaround |
|------------|--------|------------|
| WSL2 overhead | ~5-10% latency vs native Linux | Negligible for LLM inference |
| 16GB VRAM ceiling | gemma-3-27b barely fits | Use Qwen3-14B or quantize aggressively |
| LoRA rank limit | rank-64 max at 16GB | Sufficient for domain specialization |
| No multi-GPU | Single GPU only | Future: remote vLLM on multi-GPU server |
| First load slow | Model download + load ~5min | Cached after first run |
| Blackwell SM_120 | vLLM/PyTorch CUDA support may lag | Use CUDA 12.8+, latest vLLM nightly |

## Dependencies

| Component | Version | Source |
|-----------|---------|--------|
| WSL2 | Latest | `wsl --install` |
| Ubuntu | 24.04 LTS | WSL distribution |
| CUDA Toolkit | 12.8 | NVIDIA apt repo (inside WSL) |
| NVIDIA Driver | 560+ | nvidia.com (Windows only) |
| Python | 3.12 | deadsnakes PPA |
| vLLM | latest | pip install vllm |
| PyTorch | 2.5+ | vLLM dependency |
| LiteLLM | latest | pip install litellm (Windows) |

## Related Files

| File | Purpose |
|------|---------|
| `boot/vllm_setup.ps1` | One-time WSL2 + CUDA + vLLM installation |
| `boot/vllm_server.ps1` | Start vLLM server with LoRA adapters |
| `boot/litellm_proxy.ps1` | LiteLLM routing proxy (upstream of vLLM) |
| `boot/ollama_nucleus.ps1` | Ollama-based inference (fallback) |
| `.cex/config/litellm_config.yaml` | LiteLLM routing configuration |
| `_data/ft/ft_n0X.jsonl` | Per-nucleus training data |
| `_data/ft/adapters/cex-n0X-qlora/` | Trained LoRA adapter weights |
| `_data/ft/adapters/cex-n0X.Modelfile` | Ollama adapter config (legacy) |
