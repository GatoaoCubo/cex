---
mission: HYBRID_REVIEW3
nucleus: n05
wave: review
created: 2026-04-13
model: claude-opus-4-6
source_model: gemma4:26b (Wave 2 ML kinds)
---

# N05 -- Audit quantization_config (13 ISOs)

## Your kind
1. quantization_config -- archetypes/builders/quantization-config-builder/ (13 ISOs)

## Pre-flight check

```bash
ls archetypes/builders/quantization-config-builder/ | grep -c bld_
```
Should return 13. If < 13, Wave 2 incomplete -- wait for gemma4 signal.

## Review protocol

### Step 1: Load systemic defects reference
Read `N01_intelligence/reports/master_systemic_defects.md` first.
N05 is Operations -- you own runtime correctness, deploy validity, and config accuracy.
Focus especially on: D03 (quality_gate tests runtime not artifacts), D05 (quality non-null),
D06 (H02 ID pattern drift), D07 (fabricated tools), D08 (bare placeholders), D11 (soft weights).

### Step 2: Per-ISO audit (5D scoring)

Open all 13 ISOs and score:
- D1 Structural completeness (all bld_* files present, no blank required fields, correct naming)
- D2 Domain accuracy (quantization = model compression, inference optimization -- not data compression)
- D3 Density (>= 0.85)
- D4 CEX compliance (8F integration, quality: null in bld_schema, llm_function: BECOME)
- D5 Industry alignment (terminology matches GPTQ, AWQ, llama.cpp, GGUF below)

**Score thresholds:**
- >= 8.0: leave
- 6.0-7.9: surgical fix
- < 6.0: rebuild

### Step 3: Industry citations to verify

**quantization_config:**
- GPTQ (Frantar et al.): layer-wise quantization, Hessian approximation, group_size, desc_act, damp_percent
- AWQ (Lin et al.): activation-aware weight quantization, zero-point, scale search
- GGUF (llama.cpp / ggerganov): format spec, Q4_K_M / Q8_0 naming, metadata section
- GGML: legacy format (GGUF supersedes it -- check for stale references)
- bitsandbytes (Dettmers): int8 LLM.int8(), int4 nf4/fp4, double quantization
- AutoGPTQ / AutoAWQ: Python API for running GPTQ/AWQ
- ONNX INT8: per-channel vs per-tensor quantization
- Key fields: quant_type (GPTQ|AWQ|GGUF|int8|int4), bits (2|3|4|8), group_size, calibration_dataset, target_device

**What the ISOs must cover correctly:**
- bld_schema: quant_type, bits, group_size, calibration_dataset, target_device, accuracy_drop fields
- bld_instruction: how to select quantization method based on hardware + latency + accuracy requirements
- bld_system_prompt: llm_function=BECOME (not INJECT)
- bld_quality_gate: should test artifact structure (schema fields present), NOT runtime inference speed
- bld_tools: real CEX tools, not fabricated quantize() Python calls

### Step 4: Known gemma4 contamination to detect

1. D01: bld_system_prompt llm_function=INJECT instead of BECOME
2. D03: bld_quality_gate tests inference latency or model size at runtime -- should test artifact completeness
3. D04: Data compression domain (ZIP, zlib, deflate) contaminating LLM quantization content
4. D06: H02 gate checks ID pattern "p09_qc_*" but naming convention is actually different
5. D07: bld_tools references torch.quantize_dynamic() or llama_cpp.quantize() -- not CEX tools
6. D08: output_template has bare {{quant_method}}, {{bits}} without guidance
7. D11: SOFT gate weights in bld_quality_gate do not sum to 1.00

### Step 5: Fix or rebuild

For D03: rewrite bld_quality_gate to validate artifact structure, not runtime behavior.
For D11: sum the SOFT weights and redistribute to exactly 1.00.
For D01: change llm_function: INJECT -> llm_function: BECOME.

### Step 6: Validate

```bash
python _tools/cex_wave_validator.py --scope archetypes/builders/quantization-config-builder/
```
All gates must pass before commit.

### Step 7: Write audit report

`N05_operations/audits/hybrid_review3_n05.md`

Frontmatter:
```yaml
---
id: hybrid_review3_n05
kind: knowledge_card
pillar: P01
title: "HYBRID_REVIEW3 Audit: quantization_config (N05)"
version: 1.0.0
quality: null
tags: [audit, hybrid_review3, quantization_config, gemma4, wave2]
domain: ML ops quality assurance
created: "2026-04-13"
---
```

Report sections:
1. Scope (13 ISOs examined)
2. Defects found by category (D01-D15)
3. Fixes applied per ISO
4. ISOs rebuilt
5. Final 5D scores
6. Validator output summary

## Context (pre-loaded)

- Master defects: `N01_intelligence/reports/master_systemic_defects.md`
- Gold standard builder: `archetypes/builders/knowledge-card-builder/`
- Prior N05 audit: `N05_operations/audits/hybrid_review2_n05.md`
- Config kinds reference: `P09_config/` (env_config, rate_limit_config -- similar structure)

## Commit

```bash
git add archetypes/builders/quantization-config-builder/ \
        N05_operations/audits/hybrid_review3_n05.md
git commit -m "[N05] HYBRID_REVIEW3: audit+fix quantization_config (13 ISOs)"
```

## ON COMPLETION

```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n05', 'complete', 9.0)"
```
