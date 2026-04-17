---
kind: quality_gate
id: p11_qg_model_architecture
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for model_architecture
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
---

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
