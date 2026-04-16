---
id: plan_wave3_v2
kind: decision_record
pillar: P08
title: Wave 3 dispatch plan with gen_v2
version: 2.0.0
quality: 9.1
tags: [wave3, planning, v2, gen_v2, hardening]
created: 2026-04-13
nucleus: n06
mission: GEN_V2_HARDENING
density_score: 1.0
---

# Wave 3 Plan (v2)

## Prerequisites

- [ ] Wave 2 complete (18 kinds x 13 ISOs = 234 artifacts committed)
- [ ] HYBRID_REVIEW_2 complete (N07 consolidated Wave 2 audit)
- [ ] `wave1_builder_gen_v2.py` present at `_tools/` (N02 deliverable -- BLOCK if missing)
- [ ] `cex_wave_validator.py` installed as pre-commit hook (N05 deliverable -- BLOCK if missing)
- [ ] Ollama running: `curl http://localhost:11434/api/tags` returns gemma4:26b
- [ ] No orphan aider/ollama processes competing for VRAM
- [ ] Disk space > 5 GB free (234 ISOs x ~4 KB avg = ~1 MB; headroom for logs)
- [ ] Claude quota checked: `python _tools/cex_quota_check.py --all --cache`

## gen_v2 Integration Points

> NOTE (2026-04-13): `wave1_builder_gen_v2.py` was not yet present when this plan was written.
> N02 is responsible for producing it. The items below describe EXPECTED improvements from v1.
> Update this section once gen_v2 is available and verified.

| v1 Weakness | v2 Expected Fix | Impact |
|-------------|-----------------|--------|
| `validate_iso_body()` absent -- short/empty ISOs pass undetected | Body length + section count check | Prevents hollow artifacts |
| BECOME persona identical across kinds (no domain sin lens) | Kind-specific persona injection from kinds_meta.json `boundary` field | Higher domain specificity |
| No retry on quality failure | Re-prompt with feedback if body < threshold | Reduces HYBRID_REVIEW rework |
| Single prompt per ISO regardless of ISO type | ISO-type-specific prompt templates | Better schema/instruction/examples ISOs |
| No `--validator` flag in wave_pipeline.py | Pass `--generator` and `--validator` to wave_pipeline.py | End-to-end validated pipeline |

**Before launching Wave 3**: confirm gen_v2 passes:
```bash
python _tools/wave1_builder_gen_v2.py --kind benchmark_suite --dry-run
python _tools/cex_wave_validator.py --check archetypes/builders/benchmark-suite-builder/
```

## Kinds (18)

| # | Kind | Domain | Pillar | Nucleus | Risk | Domain Notes |
|---|------|--------|--------|---------|------|-------------|
| 1 | benchmark_suite | Eval | P07 | N05 | LOW | MLPerf, HELM, BIG-Bench well-documented. Strong training signal. |
| 2 | judge_config | Eval | P07 | N05 | MEDIUM | LLM-as-judge patterns evolving. MT-Bench, Chatbot Arena as refs. |
| 3 | eval_metric | Eval | P07 | N05 | LOW | BLEU/ROUGE/F1/NDCG established. Gemma4 likely strong here. |
| 4 | eval_framework | Eval | P07 | N05 | MEDIUM | Eleuther, OpenAI Evals, HELM differ significantly in schema. |
| 5 | trajectory_eval | Eval | P07 | N05 | HIGH | Very new (2024-2025). Sparse training data. High hallucination risk. |
| 6 | reranker_config | RAG | P01 | N04 | LOW | Cohere Rerank, cross-encoder, ColBERT well-documented. |
| 7 | graph_rag_config | RAG | P01 | N04 | HIGH | MS GraphRAG (2024). Few standardized patterns. Divergent configs. |
| 8 | agentic_rag | RAG | P01 | N04 | HIGH | Rapidly evolving. Corrective RAG, Self-RAG, RAG-Fusion all differ. |
| 9 | memory_architecture | Memory | P10 | N04 | MEDIUM | MemGPT/Letta, Zep, mem0 have divergent schemas. |
| 10 | procedural_memory | Memory | P10 | N04 | MEDIUM | Less documented than semantic. Skill-library patterns emerging. |
| 11 | consolidation_policy | Memory | P10 | N04 | MEDIUM | Novel in agent memory. Few production references. |
| 12 | memory_benchmark | Memory | P07/P10 | N04 | HIGH | Barely standardized (LOCOMO, MemGPT evals). Gemma4 likely to hallucinate. |
| 13 | prompt_technique | Prompt | P03 | N03 | LOW | CoT, ReAct, ToT, SC well-documented. Strong training signal. |
| 14 | prompt_optimizer | Prompt | P03 | N03 | MEDIUM | DSPy (Stanford) primary ref. OPRO, APE as alternatives. |
| 15 | multimodal_prompt | Prompt | P03 | N03 | MEDIUM | GPT-4V, Claude 3, Gemini patterns emerging but not unified. |
| 16 | workflow_node | Workflow | P12 | N03 | LOW | LangGraph, Prefect, Temporal all well-documented node primitives. |
| 17 | visual_workflow | Workflow | P12 | N03 | MEDIUM | Mermaid + LangGraph visual overlap. Less standardized schema. |
| 18 | self_improvement_loop | Self | P11 | N03 | HIGH | Cutting-edge (2024-2025). AlphaCode 2, DSPy self-improvement sparse. |

**Risk summary**: LOW=5 (28%) | MEDIUM=7 (39%) | HIGH=6 (33%)
**Implication**: HIGH-risk kinds need post-generation manual spot-check before HYBRID_REVIEW_3.

## ETA Calculation

| Factor | Value | Source |
|--------|-------|--------|
| Model | gemma4:26b | RTX 5070 Ti, VRAM 14.6 GB |
| Base rate | 35 TPS (effective) | Wave 2 benchmark, validated |
| ISO avg tokens | 800 | Wave 1 empirical avg |
| Per-ISO time | ~23 s | 800 / 35 TPS |
| Total ISOs | 234 | 18 kinds x 13 ISOs |
| Raw generation time | ~90 min | 234 x 23 s |
| Validation overhead (v2) | +15% | cex_wave_validator.py per-ISO check |
| Retry overhead (HIGH-risk) | +5% | ~6 kinds with 1-2 retries avg |
| **Total ETA** | **~107 min** | ~1h47min from launch |

> Baseline vs plan_wave3_prep.md: original ETA was 3h40min using 58s/ISO.
> v2 pipeline runs gemma4 at 35 TPS (validated) vs the 58s/ISO estimate -- 2x faster.
> The 104-107 min estimate is credible if Ollama has no competing processes.

## Risk Matrix

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| gemma4 hallucination on HIGH-risk domains (trajectory_eval, graph_rag, self_improvement_loop) | HIGH | Hollow/wrong ISOs | Validator catches empty sections; HYBRID_REVIEW_3 audits semantics |
| Ollama OOM with competing processes (aider, qwen3) | MEDIUM | Generation crash mid-wave | Pre-flight: `Get-Process aider,ollama | Stop-Process -Force`; check free VRAM |
| wave1_builder_gen_v2.py not ready when Wave 2 completes | MEDIUM | Wave 3 blocked | Hard gate: check file exists before dispatch; fallback to gen_v1 with manual validation |
| cex_wave_validator.py pre-commit hook blocks legitimate edge cases | LOW | Pipeline stall | `--bypass` flag with audit log; investigate before disabling |
| HYBRID_REVIEW_2 incomplete when Wave 2 finishes | MEDIUM | Missing quality data to calibrate thresholds | Use Wave 1 empirical avg (7.55/ISO) as proxy; update thresholds post-HYBRID_REVIEW_2 |
| Disk or context window overflow mid-wave | LOW | Partial run | wave_pipeline.py resumes from last committed kind; safe to re-run |
| memory_benchmark ISOs fail schema validation (cross-pillar P07/P10) | MEDIUM | Schema mismatch in kinds_meta.json | Pre-check: verify memory_benchmark entry in .cex/kinds_meta.json before launch |
| gemma4 CPU offload if VRAM fragmented | LOW | TPS drops from 35 to ~10 | Monitor: `nvidia-smi` during first kind; kill + restart Ollama if TPS < 20 |

## Quality Gates (v2)

> v2 adds gates 2-3 vs the original Wave 3 prep plan.

| Gate | Stage | Tool | Pass Criteria | Action on Fail |
|------|-------|------|---------------|---------------|
| 1. Kind registry | Pre-generation | `kinds_meta.json` lookup | Kind has valid pillar, llm_function, description | Block; add entry first |
| 2. Body validation (NEW) | Post-generation, in generator | `validate_iso_body()` in gen_v2 | Body > 300 chars, has >= 3 markdown sections | Re-prompt with feedback (max 2 retries) |
| 3. Pre-commit hook (NEW) | Pre-commit | `cex_wave_validator.py --staged` | Frontmatter valid + body density >= 0.7 | Fix or --bypass with log |
| 4. Doctor check | Post-commit | `cex_doctor.py` | All ISOs for wave pass health check | Flag kind for manual review |
| 5. Semantic audit | Post-wave | HYBRID_REVIEW_3 (6 Claude nuclei) | Quality >= 8.0 per ISO avg | Rebuild failing ISOs via /evolve |

## Launch Command

> Requires gen_v2 and cex_wave_validator.py to be installed.

```bash
nohup python _tools/wave_pipeline.py \
    --start-wave 3 \
    --generator _tools/wave1_builder_gen_v2.py \
    --validator _tools/cex_wave_validator.py \
    > .cex/runtime/wave3_gemma.log 2>&1 & disown
```

**Fallback** (if gen_v2 not ready -- use v1 without validator):
```bash
nohup python _tools/wave_pipeline.py --start-wave 3 > .cex/runtime/wave3_gemma.log 2>&1 & disown
```

Monitor:
```bash
tail -f .cex/runtime/wave3_gemma.log
# or
python _tools/wave_pipeline.py --status
```

## Dispatch Checklist (N07 executes in order)

1. [ ] Wave 2 complete: `python _tools/wave_pipeline.py --dry-run` shows Wave 2 = 18/18
2. [ ] HYBRID_REVIEW_2 consolidated: check git log for "[N07] HYBRID_REVIEW2 consolidation"
3. [ ] gen_v2 present: `ls _tools/wave1_builder_gen_v2.py` -- if missing, dispatch N02 first
4. [ ] Validator installed: `ls _tools/cex_wave_validator.py` -- if missing, dispatch N05 first
5. [ ] Validator as pre-commit hook: `cat .git/hooks/pre-commit | grep cex_wave_validator`
6. [ ] Claude quota: `python _tools/cex_quota_check.py --all --cache`
7. [ ] Ollama live: `curl -s http://localhost:11434/api/tags | python -c "import sys,json; m=[x['name'] for x in json.load(sys.stdin)['models']]; print('OK' if 'gemma4:26b' in m else 'MISS')"`
8. [ ] No orphan processes: `Get-CimInstance Win32_Process -Filter "Name='aider.exe'" | Measure-Object | Select Count`
9. [ ] Disk space: `(Get-PSDrive C).Free / 1GB` -- must be > 5 GB
10. [ ] Execute launch command (v2 if gen_v2 ready, fallback if not)
11. [ ] Monitor log every 15 min: `tail -100 .cex/runtime/wave3_gemma.log`
12. [ ] After complete: `python _tools/cex_doctor.py` -- all 234 ISOs pass

## Post-Wave-3 Actions

1. HYBRID_REVIEW_3: dispatch 6 Claude nuclei to audit 234 Wave 3 ISOs
2. Apply /evolve to any ISO below 8.0 (target: 0 below 7.0)
3. Update `.cex/kinds_meta.json` if new domains discovered during build
4. Regenerate FT dataset: handled automatically by wave_pipeline.py
5. Final commit: tag as `wave3-complete`

## Quality Calibration from Wave 1

> Wave 2 quality report not yet available (N04 pending). Using Wave 1 as proxy.

| Metric | Wave 1 (qwen3:14b) | Wave 3 Target (gemma4:26b) |
|--------|--------------------|-----------------------------|
| Avg ISO quality | 7.55 | 8.5+ |
| Domain hallucination rate | ~75% of kinds had >= 1 wrong domain | < 10% with validator |
| Hollow ISOs (< 300 chars) | ~5% | 0% (gate 2 blocks) |
| Schema compliance | ~85% | 98%+ (gate 3 enforces) |

> Update this table once wave2_quality_report.md is available from N04.
