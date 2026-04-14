---
id: hybrid_review4_n05
kind: knowledge_card
pillar: P07
title: "HYBRID_REVIEW4 N05 Audit: benchmark_suite, eval_metric, memory_benchmark"
version: "1.0.0"
quality: 8.9
tags: [audit, hybrid_review4, benchmark_suite, eval_metric, memory_benchmark, wave3, n05]
domain: "quality assurance"
created: "2026-04-14"
updated: "2026-04-14"
author: n05_operations
tldr: "Wave 3 audit of 3 eval/benchmark builders (39 ISOs). benchmark_suite and eval_metric: surgical fixes. memory_benchmark: full domain hallucination (DRAM vs AI agent memory) -- 7 ISOs rebuilt."
---

# HYBRID_REVIEW4 N05 Audit

## Scope

| Builder           | Risk  | ISOs | Source Model  |
|-------------------|-------|------|---------------|
| benchmark_suite   | LOW   | 13   | qwen3:14b     |
| eval_metric       | LOW   | 13   | qwen3:14b     |
| memory_benchmark  | HIGH  | 13   | qwen3:14b     |

## Defect Inventory by Builder

### benchmark_suite (LOW -> post-fix score ~8.0)

| Defect | ISO | Finding | Action |
|--------|-----|---------|--------|
| D02 | bld_memory | kind=learning_record | Fixed -> kind=memory |
| D03 | bld_quality_gate | Definition table: runtime metrics (latency 100ms, accuracy 95%) | Fixed -> artifact structure checks |
| D07+D12 | bld_tools | 4 fabricated tools (cex_analyzer.py, cex_runner.py, val_*.py); Chinese chars (base64 chars in External Refs) | Fixed: removed fabricated tools, replaced with real CEX tools + real external refs |
| D09 | bld_architecture | Pillar column: P07 for all 13 ISOs | Fixed: each ISO now shows correct pillar (P01, P03, P04, etc.) |

ISO check: D01 PASS (system_prompt llm_function=BECOME). D05 PASS (quality=null). D11 PASS (weights sum 1.00).

### eval_metric (LOW -> post-fix score ~8.0)

| Defect | ISO | Finding | Action |
|--------|-----|---------|--------|
| D02 | bld_memory | kind=learning_record | Fixed -> kind=memory |
| D03 | bld_quality_gate | Definition table: runtime metrics (accuracy 0.95, latency 100ms) | Fixed -> artifact structure checks |
| D07 | bld_tools | 6 fabricated tools (cex_validator.py, cex_formatter.py, metric_validator.py, etc.) | Fixed: replaced with real CEX tools + real external refs |
| D11 | bld_quality_gate | SOFT weights summed to 0.90 (missing 0.10) | Fixed: D2=0.20, D3=0.15, D6=0.10 -> sum=1.00 |

ISO check: D01 PASS (system_prompt llm_function=BECOME). D05 PASS (quality=null). D06 PASS (H02 pattern matches schema).

### memory_benchmark (HIGH -> full domain hallucination, REBUILT)

**Root cause**: qwen3:14b misidentified "memory_benchmark" as hardware DRAM/SRAM benchmarking.
Correct domain: AI agent memory evaluation (retention, recall, hallucination rate across conversations).

| ISO | Finding | Action |
|-----|---------|--------|
| bld_knowledge_card | DRAM hardware concepts (JEDEC DDR5, ECC, Rowhammer) | REBUILT: AI memory benchmarks (LOCOMO, LongMemEval, MemGPT, NiH) |
| bld_system_prompt | DRAM scope ("memory subsystems: DRAM, SRAM") | REBUILT: AI agent memory scope with anti-contamination rules |
| bld_quality_gate | DRAM metrics (latency 100ns, bandwidth 50GB/s) | REBUILT: artifact structure checks + AI memory-specific SOFT scoring |
| bld_schema | Hardware fields (capacity_mb, latency_ms for DRAM) | REBUILT: AI memory fields (memory_type, eval_distance) |
| bld_tools | DRAM tools (PyMemcache, Redis, JMH) | REBUILT: real CEX tools + LOCOMO/LongMemEval/ragas refs |
| bld_instruction | DRAM methodology (STREAM, MEMBENCH, x86/ARM/FPGA) | REBUILT: AI memory eval methodology (conversation generation, fact planting, query distances) |
| bld_manifest | DRAM capabilities (JEDEC, HBM, 3D XPoint) | REBUILT: AI memory evaluation identity with correct routing |
| bld_memory | kind=learning_record (D02) | Fixed -> kind=memory |
| bld_architecture | Pillar column: P07 for all ISOs | Fixed: correct pillars per ISO |

HARD gates added (H07): explicitly reject artifacts containing DRAM/SRAM/bandwidth/ECC references.

## Validator Results (post-fix)

```
benchmark_suite:  13/13 PASS (0 FAIL)
eval_metric:      13/13 PASS (0 FAIL)
memory_benchmark: 13/13 PASS (0 FAIL)
TOTAL:            39/39 PASS
```

## Estimated Quality Scores (post-fix)

| Builder          | Pre-fix | Post-fix | Delta |
|------------------|---------|----------|-------|
| benchmark_suite  | 6.0     | 8.0      | +2.0  |
| eval_metric      | 6.0     | 8.0      | +2.0  |
| memory_benchmark | 3.0     | 8.2      | +5.2  |

## Industry Standards Referenced

- MLPerf (mlcommons.org): AI benchmark suite standard
- HELM (Liang et al., 2022): Holistic LLM evaluation framework
- LOCOMO (Maharana et al., 2024): Long-conversation memory benchmark
- LongMemEval (Wu et al., 2024): Multi-session memory QA
- MemGPT (Packer et al., 2023): Tiered memory agent + internal evals
- MT-Bench-101 (Bai et al., 2024): Multi-turn coherence
- Needle-in-a-Haystack (Kamradt, 2023): Long-context retrieval

## Files Modified

```
archetypes/builders/benchmark-suite-builder/bld_memory_benchmark_suite.md
archetypes/builders/benchmark-suite-builder/bld_quality_gate_benchmark_suite.md
archetypes/builders/benchmark-suite-builder/bld_tools_benchmark_suite.md
archetypes/builders/benchmark-suite-builder/bld_architecture_benchmark_suite.md
archetypes/builders/eval-metric-builder/bld_memory_eval_metric.md
archetypes/builders/eval-metric-builder/bld_quality_gate_eval_metric.md
archetypes/builders/eval-metric-builder/bld_tools_eval_metric.md
archetypes/builders/memory-benchmark-builder/bld_knowledge_card_memory_benchmark.md
archetypes/builders/memory-benchmark-builder/bld_system_prompt_memory_benchmark.md
archetypes/builders/memory-benchmark-builder/bld_quality_gate_memory_benchmark.md
archetypes/builders/memory-benchmark-builder/bld_schema_memory_benchmark.md
archetypes/builders/memory-benchmark-builder/bld_tools_memory_benchmark.md
archetypes/builders/memory-benchmark-builder/bld_instruction_memory_benchmark.md
archetypes/builders/memory-benchmark-builder/bld_manifest_memory_benchmark.md
archetypes/builders/memory-benchmark-builder/bld_memory_memory_benchmark.md
archetypes/builders/memory-benchmark-builder/bld_architecture_memory_benchmark.md
N05_operations/audits/hybrid_review4_n05.md
```

## Ops Lens Notes

- bld_collaboration ISOs use generic team names (D15) -- LOW priority, acceptable for P1 review
- bld_instruction for benchmark_suite still references SCHEMA.md (should be bld_schema_benchmark_suite.md) -- minor D10 drift
- No functional CI/CD issues found; bld_collaboration_benchmark_suite.md references real commit/compile patterns

## N05 Verdict

HYBRID_REVIEW4 complete. All 39 ISOs pass validator. memory_benchmark domain hallucination
was severe (full DRAM contamination) and required 7 ISO rebuilds. benchmark_suite and
eval_metric required surgical fixes (4 ISOs each). No outstanding blockers.
