---
kind: quality_gate
id: p11_qg_model_architecture
pillar: P11
llm_function: GOVERN
quality: 9.0
title: "Quality Gate: model_architecture"
version: "1.0.0"
author: n02_hybrid_review3
tags: [model_architecture, quality_gate, builder, P11]
tldr: "Gates ensuring model_architecture artifacts contain complete layer specs, accurate neural net content, and all required frontmatter."
domain: "model_architecture construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.91
purpose: Quality gate with HARD and SOFT scoring for model_architecture
related:
  - p11_qg_agent_computer_interface
  - p02_qg_training_method
  - bld_instruction_model_architecture
  - p11_qg_knowledge_card
  - p11_qg_input_schema
  - p11_qg_quality_gate
  - bld_examples_model_architecture
  - bld_output_template_model_architecture
  - p11_qg_chunk_strategy
  - p11_qg_handoff
---

## Quality Gate

# Quality Gate: model_architecture

## Definition

| Field | Value |
|-------|-------|
| metric | weighted soft score + all hard gates pass |
| threshold | 8.0 to publish; 9.0 for pool; 9.5 for golden |
| operator | AND (all hard) + weighted average (soft) |
| scope | any artifact with `kind: model_architecture` |

## HARD Gates

All must pass. Any failure = immediate reject.

| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error on any field |
| H02 | ID matches `^p02_ma_[a-z][a-z0-9_]+$` | Uppercase, wrong prefix, or non-alphanumeric chars |
| H03 | ID equals filename stem | id: p02_ma_llama_7b in file p02_ma_gpt2.md |
| H04 | kind equals literal `model_architecture` | Any other kind value |
| H05 | quality field is null | Any non-null value (self-scoring forbidden) |
| H06 | All required fields present | Missing: architecture_type, parameter_count, domain, tldr, tags |
| H07 | architecture_type from allowed enum | Not one of: transformer, cnn, rnn, mlp, diffusion, graph, hybrid |
| H08 | parameter_count is explicit | null, "TBD", "unknown", or empty string |
| H09 | File size <= 4096 bytes body | Body exceeds 4KB limit |
| H10 | Layer Structure table has >= 3 rows | Missing section or fewer than 3 data rows |

## SOFT Scoring

Total weights sum to 1.0.

| ID | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|----|-----------|--------|--------|-------|-------|
| S01 | Layer structure completeness | 1.0 | Ordered table with layer type, count, hidden dim, and notes | Table present but missing dim or count | No table or < 3 rows |
| S02 | Connectivity pattern | 1.0 | Explicit table: attention type, residual connections, pooling | Pattern mentioned in prose but not tabular | Missing entirely |
| S03 | Parameter profile breakdown | 1.0 | Component-level breakdown summing to total (embeddings, attention, FFN) | Total only, no breakdown | Missing or vague |
| S04 | Compute profile | 1.0 | Both FLOPs and memory specified with units (e.g., 3.5T FLOPs, 14GB fp16) | One of FLOPs or memory, not both | Missing or "varies" |
| S05 | Training considerations | 1.0 | Concrete recommendations: optimizer, LR schedule, init strategy | Generic advice without specifics | Missing section |
| S06 | Domain accuracy | 1.0 | Content covers neural net architecture (layers, weights, activations) -- no finance/trading contamination | Mostly accurate with minor tangents | Financial, portfolio, or trading content present |
| S07 | Architecture novelty | 0.5 | Overview section explains design goal and difference vs prior work | Mentions novelty vaguely | No differentiation from prior work |
| S08 | Boundary disambiguation | 0.5 | Explicitly notes what this is NOT (finetune_config, model_card, training_method) | Partially disambiguated | No boundary stated |

**Score = sum(pts * weight) / sum(max_pts * weight) * 10**

## Actions

| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Publish as authoritative architecture reference |
| >= 9.0 | Pool | Publish to P02 architecture pool |
| >= 8.0 | Skilled | Publish with quality: null (peer review pending) |
| >= 6.0 | Fix | Return for revision with gate report |
| < 6.0 | Reject | Full rebuild required |

## Bypass

| Field | Value |
|-------|-------|
| Conditions | Novel unreleased architecture where parameter details are not yet public (e.g., day-of release) |
| Approver | N01 Intelligence with citation to official source |
| Bypass duration | 30 days -- recheck when details are published |

## Examples

# Examples: model_architecture Artifacts

## Example 1: Causal Decoder (LLaMA-style)
```yaml
---
id: p02_ma_llama_style_7b
kind: model_architecture
pillar: P02
title: "LLaMA-style 7B Causal Decoder"
architecture_type: transformer
parameter_count: "7B"
domain: NLP
quality: null
---
## Layer Structure
| # | Layer Type | Count | Hidden Dim | Heads | Notes |
|---|-----------|-------|-----------|-------|-------|
| 1 | Token Embedding | 1 | 4096 | - | vocab=32000 |
| 2 | RMSNorm | 32 | 4096 | - | pre-norm |
| 3 | Grouped Query Attention | 32 | 4096 | 32/8 | GQA |
| 4 | FFN (SwiGLU) | 32 | 11008 | - | gated activation |
## Parameter Profile
| Component | Params |
|-----------|--------|
| Embeddings | 131M |
| Attention | 2.1B |
| FFN | 4.5B |
| Norms + biases | 50M |
| Total | ~7B |
```

## Example 2: Vision Transformer (ViT-B)
```yaml
---
id: p02_ma_vit_base
kind: model_architecture
pillar: P02
title: "Vision Transformer ViT-B/16"
architecture_type: transformer
parameter_count: "86M"
domain: vision
quality: null
---
## Layer Structure
| Layer | Count | Dim | Notes |
|-------|-------|-----|-------|
| Patch Embedding | 1 | 768 | 16x16 patches |
| CLS Token | 1 | 768 | prepended |
| Position Embedding | 1 | 768 | learned |
| Transformer Encoder | 12 | 768 | 12 heads |
| MLP Head | 1 | num_classes | linear probe |
```

## Anti-Pattern: Incomplete Layer Table
```yaml
---
id: p02_ma_incomplete
kind: model_architecture
pillar: P02
title: "Some Transformer"
architecture_type: transformer
parameter_count: "unknown"
quality: 9.0
---
## Architecture
A transformer model with some layers.
```
### Why it fails
- `parameter_count: unknown` violates required specificity
- No Layer Structure table (required section)
- `quality: 9.0` -- never self-score, always null
- Prose instead of structured tables

## Pattern Recognition
| Anti-Pattern | Why Wrong | Correct Approach |
|-------------|-----------|-----------------|
| quality not null | Self-scoring | Set quality: null always |
| Missing layer table | Vague spec | Add ordered layer table |
| No param count | Incomplete | Specify count (e.g., "7B", "340M") |
| Prose only | Low density | Use tables for structure |
| Wrong architecture_type | Routing failure | Use exact enum value |

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
