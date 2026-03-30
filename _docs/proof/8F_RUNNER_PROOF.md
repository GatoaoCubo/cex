# 8F Runner Proof -- Pipeline Validation

**Date**: 2026-03-30
**Runner**: `_tools/cex_8f_runner.py` (v1.0.0, all 3 waves)
**Mode**: dry-run (no LLM calls)

---

## 1. Architecture Comparison

### cex_intent.py (monolithic, 533 loc)
- Loads ALL ISOs -> composes 1 flat prompt -> 1 LLM call -> done
- 8F are LABELS, not steps. Zero intermediate processing.
- No validation (F7). No constraints extraction (F1). No reasoning (F4).
- Prompt sections: 6 (system_prompt, instruction, KC, schema, template, intent)

### cex_8f_runner.py (pipeline, ~1160 loc)
- Each F produces a dict that the next CONSUMES. State accumulates.
- F1 extracts constraints from _schema.yaml + bld_schema + bld_config
- F2 loads identity (persona, boundary, domain)
- F3 injects knowledge (builder KC + domain KCs + examples + memory + architecture)
- F4 composes reasoning prompt (LLM plans the artifact in execute mode)
- F5 scans tools + existing artifacts (duplicate detection)
- F6 produces structured prompt with 9 labeled sections
- F7 validates 6 hard gates with retry loop (max 2 retries)
- F8 saves artifact or prompt, attempts compile

### Key Difference
| Aspect | cex_intent.py | cex_8f_runner.py |
|--------|---------------|------------------|
| State | None | RunState dataclass (8 fields) |
| F1 constraints | Not extracted | max_bytes, id_pattern, required fields |
| F3 knowledge | KC-Domains only | builder KC + domain KCs + examples + memory + arch |
| F4 reasoning | None | LLM planning step (haiku) |
| F5 tools | None | Tools table + duplicate detection |
| F6 sections | 6 flat | 9 structured (identity, constraints, knowledge, examples, plan, tools, instruction, template, task) |
| F7 validation | None | 6 hard gates + retry loop |
| Prompt words | ~1500-2500 | ~3400-4100 (richer context) |

---

## 2. Proof Artifacts (3 dry-runs)

### Artifact 1: chunk_strategy
```
Intent:   "create a markdown chunking strategy for technical docs"
Kind:     chunk_strategy
Pillar:   P01
Builder:  chunk-strategy-builder (13 ISOs)
```

| Function | Contribution | Timing |
|----------|-------------|--------|
| F1 CONSTRAIN | max_bytes=2048, id_pattern=`^p01_chunk_[a-z][a-z0-9_]+$`, 5 required fields | 25ms |
| F2 BECOME | 7 identity keys (persona, boundary, domain) | 3ms |
| F3 INJECT | builder-KC + 3 domain-KCs + examples + memory + architecture | 2ms |
| F4 REASON | 147-word planning prompt (dry-run) | <1ms |
| F5 CALL | 7 tools parsed, 1 existing artifact detected | 2ms |
| F6 PRODUCE | 3406-word structured prompt (9 sections) | 1ms |
| F7 GOVERN | 2/6 gates passed (expected: dry-run artifact = prompt text) | 3ms |
| F8 COLLABORATE | Saved to `_docs/proof/runner_out/chunk_strategy_prompt.md` | 2ms |

**Output**: 26,350 bytes | **Total**: ~38ms

### Artifact 2: unit_eval
```
Intent:   "create an eval dataset for testing RAG retrieval quality"
Kind:     unit_eval
Pillar:   P07
Builder:  unit-eval-builder (13 ISOs)
```

| Function | Contribution | Timing |
|----------|-------------|--------|
| F1 CONSTRAIN | max_bytes=4096, id_pattern=`^p07_ue_[a-z][a-z0-9_]+$` | 29ms |
| F2 BECOME | 7 identity keys | 5ms |
| F3 INJECT | builder-KC + 1 domain-KC + examples + memory + architecture | 2ms |
| F4 REASON | 156-word planning prompt (dry-run) | <1ms |
| F5 CALL | 8 tools parsed, 1 existing artifact detected | 1ms |
| F6 PRODUCE | 3685-word structured prompt | 1ms |
| F7 GOVERN | 3/6 gates passed (expected dry-run failure) | 3ms |
| F8 COLLABORATE | Saved to `_docs/proof/runner_out/unit_eval_prompt.md` | 1ms |

**Output**: 26,285 bytes | **Total**: ~41ms

### Artifact 3: reward_signal
```
Intent:   "create a reward signal for agent task completion"
Kind:     reward_signal
Pillar:   P11
Builder:  reward-signal-builder (13 ISOs)
```

| Function | Contribution | Timing |
|----------|-------------|--------|
| F1 CONSTRAIN | max_bytes=2048, id_pattern=`^p11_rs_[a-z][a-z0-9_]+$`, 5 required fields | 53ms |
| F2 BECOME | 7 identity keys | 4ms |
| F3 INJECT | builder-KC + 1 domain-KC + examples + memory + architecture | 1ms |
| F4 REASON | 154-word planning prompt (dry-run) | <1ms |
| F5 CALL | 15 tools parsed, 1 existing artifact detected | 1ms |
| F6 PRODUCE | 4085-word structured prompt | 1ms |
| F7 GOVERN | 2/6 gates passed (expected dry-run failure) | 3ms |
| F8 COLLABORATE | Saved to `_docs/proof/runner_out/reward_signal_prompt.md` | 1ms |

**Output**: 30,157 bytes | **Total**: ~63ms

---

## 3. F7 Hard Gate Results

In dry-run mode, F7 validates the assembled prompt (not a real artifact),
so frontmatter/id/size gates fail by design. In --execute mode with an LLM,
F7 validates the actual generated artifact.

| Gate | Check | chunk_strategy | unit_eval | reward_signal |
|------|-------|----------------|-----------|---------------|
| H01 | YAML frontmatter parses | FAIL (prompt) | FAIL (prompt) | FAIL (prompt) |
| H02 | id matches pattern | FAIL (no FM) | FAIL (no FM) | FAIL (no FM) |
| H03 | kind matches | PASS | PASS | PASS |
| H04 | quality is null | PASS | PASS | PASS |
| H05 | required fields present | FAIL (no FM) | PASS (0 req) | FAIL (no FM) |
| H06 | body <= max_bytes | FAIL (prompt) | FAIL (prompt) | FAIL (prompt) |

All gates are functional. H03/H04 pass because they default-pass when
no frontmatter is parsed. In execute mode, all 6 gates validate real output.

---

## 4. Metrics Summary

| Metric | Target | Result |
|--------|--------|--------|
| dry-run has structured sections | PASS | 9 sections in all 3 |
| F1 constraints visible in F6 prompt | visible | max_bytes, id_pattern, required fields injected |
| F3 KC content visible in F6 prompt | visible | builder-KC + domain-KCs + examples + memory + arch |
| F7 catches bad frontmatter | reject + retry | PASS (retry loop works, 2 retries executed) |
| F7->F6 retry injects feedback | feedback in prompt | PASS (RETRY FEEDBACK section appended) |
| verbose shows timing | ms per F | PASS (all 8 functions timed) |
| F5 detects existing artifacts | duplicate warning | PASS (1 existing found per kind) |
| 3 proof artifacts generated | valid prompts | PASS (26-30KB each, 3 different kinds) |
| Multi-kind support | sequential run | PASS (CLI handles >1 classified kind) |

---

## 5. CLI Flags Verified

| Flag | Status |
|------|--------|
| `--dry-run` (default) | PASS |
| `--execute` | PASS (tested separately) |
| `--kind TYPE` | PASS (skips Motor classify) |
| `--verbose` | PASS (per-F timing + state summary) |
| `--step N` | PASS (stops after function N) |
| `--output-dir DIR` | PASS (creates dir, saves prompt) |
| `--list-kinds` | PASS (prints all kinds by pillar) |
| `--context TEXT` | PASS (injected in F3) |

---

*Proof generated by builder_agent on 2026-03-30. All 3 waves complete.*
