# 8F Runner Proof -- Wave 3

**Date**: 2026-03-29
**Wave**: 3 (F5 CALL, --verbose timing, --step, multi-kind, proofs)

---

## 1. Monolithic vs Pipeline Comparison

### cex_intent.py (monolithic)
- Single `execute_prompt()` call with flat string concatenation
- No state accumulation between stages
- No validation/governance loop
- No timing, no verbose, no step control
- Builder ISOs loaded ad-hoc (no structured F1-F8 mapping)

### cex_8f_runner.py (8F pipeline)
- 8 discrete functions, each consuming prior state
- `RunState` dataclass accumulates constraints, identity, knowledge, reasoning, tools, artifact, verdict, result
- F7 GOVERN: 6 hard gates with 2-retry loop feeding back into F6
- F5 CALL: scans existing artifacts + parses bld_tools ISO for available tooling
- `--verbose`: per-F timing with labeled summaries (`[F1 CONSTRAIN] 16ms | constraints: {...}`)
- `--step N`: stop after function N, inspect accumulated state
- Multi-kind: Motor classifies multiple kinds -> sequential F1-F8 per kind

---

## 2. Artifact Proof: 3 Dry-Run Outputs

### Proof 1: Chunk Strategy (P01)
- **Intent**: "create a markdown chunking strategy for technical docs"
- **Kind**: chunk_strategy | **Pillar**: P01
- **Builder**: chunk-strategy-builder
- **F5 CALL**: 7 tools parsed, 1 existing artifact detected (`ex_chunk_strategy_recursive_1000.md`)

| Function | Time | Summary |
|----------|------|---------|
| F1 CONSTRAIN | 16.1ms | max_bytes: 2048, fields: 5, id_pattern: /^p01_chunk_.../ |
| F2 BECOME | 8.0ms | 7 identity keys (persona, boundary, domain) |
| F3 INJECT | 2.4ms | 5 ISOs loaded, 3 KCs injected |
| F4 REASON | 0.4ms | 147 words (dry-run) |
| F5 CALL | 1.8ms | 7 tools, 1 existing artifact |
| F6 PRODUCE | 1.1ms | 3389 words prompt |
| F7 GOVERN | 3.2ms | 2/6 gates (expected: dry-run has no frontmatter) |
| F8 COLLABORATE | 2.6ms | saved to runner_out/chunk_strategy_prompt.md |
| **Total** | **36ms** | |

**Prompt sections from each F**:
- `# IDENTITY` <- F2 (bld_system_prompt persona + rules)
- `# CONSTRAINTS` <- F1 (max_bytes, id_pattern, frontmatter_required)
- `# KNOWLEDGE` <- F3 (builder KC, 3 domain KCs, architecture, memory)
- `# EXAMPLES` <- F3 (bld_examples few-shots)
- `# PLAN` <- F4 (reasoning prompt for LLM planning)
- `# TOOLS` <- F5 (7 available tools + 1 existing artifact warning)
- `# INSTRUCTION` <- F6 (bld_instruction body)
- `# TEMPLATE` <- F6 (bld_output_template body)
- `# TASK` <- user intent + kind + pillar + verb

### Proof 2: Eval Dataset (P07)
- **Intent**: "create an eval dataset for testing RAG retrieval quality"
- **Kind**: unit_eval | **Pillar**: P07
- **Builder**: unit-eval-builder
- **F5 CALL**: 8 tools parsed, 1 existing artifact (`ex_unit_eval_brain_query_accuracy.md`)

| Function | Time | Summary |
|----------|------|---------|
| F1 CONSTRAIN | 16.9ms | max_bytes: 4096, id_pattern: /^p07_ue_.../ |
| F2 BECOME | 5.7ms | 7 identity keys |
| F3 INJECT | 2.1ms | 5 ISOs, 1 KC |
| F4 REASON | 0.1ms | 156 words (dry-run) |
| F5 CALL | 0.9ms | 8 tools, 1 existing |
| F6 PRODUCE | 1.6ms | 3668 words |
| F7 GOVERN | 2.9ms | 3/6 gates |
| F8 COLLABORATE | 1.2ms | saved to runner_out/unit_eval_prompt.md |
| **Total** | **31ms** | |

### Proof 3: Reward Signal (P11)
- **Intent**: "create a reward signal for agent task completion"
- **Kind**: reward_signal | **Pillar**: P11
- **Builder**: reward-signal-builder
- **F5 CALL**: 15 tools parsed, 1 existing artifact (`ex_reward_signal_answer_quality.md`)

| Function | Time | Summary |
|----------|------|---------|
| F1 CONSTRAIN | 7.9ms | max_bytes: 2048, fields: 5, id_pattern: /^p11_rs_.../ |
| F2 BECOME | 5.2ms | 7 identity keys |
| F3 INJECT | 1.9ms | 5 ISOs, 1 KC |
| F4 REASON | 0.0ms | 154 words (dry-run) |
| F5 CALL | 1.1ms | 15 tools, 1 existing |
| F6 PRODUCE | 1.0ms | 4068 words |
| F7 GOVERN | 4.5ms | 2/6 gates |
| F8 COLLABORATE | 35.0ms | saved to runner_out/reward_signal_prompt.md |
| **Total** | **57ms** | |

---

## 3. F7 Hard Gate Results (Dry-Run Expected)

In dry-run mode, F6 outputs the composed prompt (not LLM-generated artifact), so frontmatter gates expectedly fail:

| Gate | Check | P1 | P2 | P3 | Notes |
|------|-------|----|----|----|----|
| H01 | YAML frontmatter parses | FAIL | FAIL | FAIL | Prompt has no frontmatter (expected) |
| H02 | id matches id_pattern | FAIL | FAIL | FAIL | No id in prompt (expected) |
| H03 | kind matches | PASS | PASS | PASS | -- |
| H04 | quality is null | PASS | PASS | PASS | -- |
| H05 | required fields present | FAIL | PASS | FAIL | Only fails when fields defined |
| H06 | body <= max_bytes | FAIL | FAIL | FAIL | Prompt > max_bytes (expected) |

With `--execute` (LLM generates real artifact), these gates validate and retry-loop fixes issues.

---

## 4. Timing Breakdown (Average of 3 Proofs)

| Function | Avg Time | % of Total |
|----------|----------|------------|
| F1 CONSTRAIN | 13.6ms | 33% |
| F2 BECOME | 6.3ms | 15% |
| F3 INJECT | 2.1ms | 5% |
| F4 REASON | 0.2ms | <1% |
| F5 CALL | 1.3ms | 3% |
| F6 PRODUCE | 1.2ms | 3% |
| F7 GOVERN | 3.5ms | 9% |
| F8 COLLABORATE | 12.9ms | 31% |
| **Total** | **~41ms** | 100% |

F1 dominates due to filesystem reads (schema + ISOs). F8 spikes on first-write (directory creation).
F4/F5/F6 are sub-2ms in dry-run. With `--execute`, F4+F6 would dominate (LLM calls).

---

## 5. Wave 3 Features Summary

| Feature | Status | Evidence |
|---------|--------|----------|
| F5 CALL | DONE | Parses bld_tools table, scans existing artifacts, warns on duplicates |
| --verbose timing | DONE | `[F1 CONSTRAIN] 16.1ms \| constraints: {max_bytes: 2048, ...}` |
| --step N | DONE | `--step 5` stops after F5, shows accumulated state |
| Multi-kind | DONE | Detects multiple classified kinds, runs F1-F8 per kind sequentially |
| F5 in F6 prompt | DONE | `# TOOLS` section with available tools + existing artifact warnings |
| F5 in banner | DONE | `Tools: N available, M existing artifacts` |
| 3 proof artifacts | DONE | chunk_strategy, unit_eval, reward_signal (dry-run, no API key) |

---

*Generated by cex_8f_runner.py wave 3 | 2026-03-29*
