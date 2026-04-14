---
mission: HYBRID_REVIEW3
nucleus: n02
wave: review
created: 2026-04-13
model: claude-opus-4-6
source_model: gemma4:26b (Wave 2 ML kinds)
---

# N02 -- Audit model_architecture (13 ISOs)

## Your kind
1. model_architecture -- archetypes/builders/model-architecture-builder/ (13 ISOs)

## Pre-flight check

```bash
ls archetypes/builders/model-architecture-builder/ | grep -c bld_
```
Should return 13. If < 13, Wave 2 incomplete -- wait for gemma4 signal.

## Review protocol

### Step 1: Load systemic defects reference
Read `N01_intelligence/reports/master_systemic_defects.md` first.
Focus on D01 (system_prompt llm_function), D04 (domain hallucination), D07 (fabricated tools),
D08 (bare placeholders), D09 (generic architecture content).

### Step 2: Per-ISO audit

Open all 13 ISOs in model-architecture-builder/ and score 5D:
- D1 Structural completeness (frontmatter, required fields, no blanks)
- D2 Domain accuracy (content is about neural net architectures, not generic software)
- D3 Density (>= 0.85, no padding)
- D4 CEX compliance (8F references, correct llm_function: BECOME for bld_system_prompt)
- D5 Industry alignment (terminology matches authoritative sources below)

**Score thresholds:**
- >= 8.0: leave as-is
- 6.0-7.9: surgical fix in place
- < 6.0: full rebuild

### Step 3: Industry citations to verify

**model_architecture:**
- Transformer (Vaswani et al., "Attention Is All You Need"): self-attention, multi-head, positional encoding
- Mixture of Experts (MoE): sparse gating, expert routing, capacity factor
- Mamba (state space model): selective SSM, linear recurrence, hardware-aware algorithm
- RWKV: linear attention, recurrent vs parallel mode
- Llama architecture: RMS Norm, RoPE, grouped-query attention (GQA), SwiGLU
- Attention variants: MHA, MQA, GQA, FlashAttention, sliding window attention
- Model families: GPT-2, GPT-NeoX, Falcon, Mistral, Phi, Gemma, Qwen

**What the ISOs must cover correctly:**
- bld_schema: architecture_type, attention_mechanism, parameter_count, context_length fields
- bld_instruction: how to document an architecture (not how to train one -- that is training_method)
- bld_system_prompt: llm_function=BECOME (N02 role), NOT INJECT
- bld_examples: should show real architecture cards (e.g., llama3 or mistral) not synthetic ones
- bld_tools: should reference cex_compile.py, cex_doctor.py -- not fabricated tools

### Step 4: Known gemma4 contamination to detect

1. D01: bld_system_prompt llm_function=INJECT instead of BECOME
2. D04: Financial/trading domain contamination (model_architecture should cover neural nets, not portfolio models)
3. D07: Fake tools in bld_tools (validate vs actual _tools/ directory contents)
4. D08: Bare {{placeholders}} in output_template without field-level descriptions
5. D09: bld_architecture describes generic software architecture (microservices, APIs) not the 13-ISO builder structure
6. D05: quality fields with non-null defaults in bld_schema

### Step 5: Fix or rebuild

Surgical fixes: edit in place, note in audit.
Rebuilds: follow the model-architecture-builder ISOs as spec, run 8F.

### Step 6: Validate

```bash
python _tools/cex_wave_validator.py --scope archetypes/builders/model-architecture-builder/
```
Fix any failures before committing.

### Step 7: Write audit report

`N02_marketing/audits/hybrid_review3_n02.md` -- model_architecture audit + master summary

Frontmatter:
```yaml
---
id: hybrid_review3_n02
kind: knowledge_card
pillar: P01
title: "HYBRID_REVIEW3 Audit: model_architecture (N02)"
version: 1.0.0
quality: null
tags: [audit, hybrid_review3, model_architecture, gemma4, wave2]
domain: ML architecture quality assurance
created: "2026-04-13"
---
```

Include: defects found vs D01-D15, fixes applied, ISOs rebuilt, final score per ISO.

## Context (pre-loaded)

- Master defects: `N01_intelligence/reports/master_systemic_defects.md`
- Gold standard builder: `archetypes/builders/knowledge-card-builder/`
- Prior audit: `N02_marketing/audits/hybrid_review2_n02.md`
- Note: model_architecture was previously diff_strategy (renamed) -- check for stale references to old kind name

## Commit

```bash
git add archetypes/builders/model-architecture-builder/ \
        N02_marketing/audits/hybrid_review3_n02.md
git commit -m "[N02] HYBRID_REVIEW3: audit+fix model_architecture (13 ISOs)"
```

## ON COMPLETION

```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n02', 'complete', 9.0)"
```
