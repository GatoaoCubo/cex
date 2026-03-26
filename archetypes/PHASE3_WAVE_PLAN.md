# Phase 3 Wave Plan: 65 Builders in 22 Waves

> Generated: 2026-03-26 | Author: EDISON | Quality: 9.0+
> Source: VARIANCE_ANALYSIS.md, TAXONOMY_LAYERS.yaml, TYPE_TO_TEMPLATE.yaml
> Models: edison (opus), atlas-codex (codex), pytha-gemini (gemini)

---

## Execution Parameters

| Parameter | Value |
|-----------|-------|
| Slots per wave | 3 (edison + atlas-codex + pytha-gemini) |
| Time per wave | ~15-20 min |
| Core 24 first | Yes (Waves 1-7) |
| Extensions after | Yes (Waves 8-22) |
| Grouping | By LP when possible (shared KNOWLEDGE + COLLABORATION) |
| Total types | 65 (69 - 4 done: model_card, knowledge_card, signal, quality_gate) |

## Model Assignment Policy

| Tier | Preferred Model | Rationale |
|------|----------------|-----------|
| COMPLEX | edison (opus) | Deep domain reasoning, persona engineering, multi-section body |
| MEDIUM | atlas-codex (codex) or pytha-gemini (gemini) | Pattern following, template adaptation |
| SIMPLE | pytha-gemini (gemini) or atlas-codex (codex) | Copy+fill variables, minimal creativity |

---

## Phase 3A: Core 24 Types (20 remaining) — Waves 1-7

### Wave 1: P06 Spec Layer (Schema Foundation)
> These define validation contracts used by many other types.

| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | interface | MEDIUM | opus | P06 | No | -- |
| atlas-codex | input_schema | SIMPLE | codex | P06 | Yes | -- |
| pytha-gemini | validator | MEDIUM | gemini | P06 | Yes | -- |

**Why first:** Spec layer types define contracts. Other builders reference them for validation.

---

### Wave 2: P01 Content Layer (Knowledge Foundation)
> Content types that feed into prompts and agents.

| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | context_doc | MEDIUM | opus | P01 | No | -- |
| atlas-codex | rag_source | SIMPLE | codex | P01 | Yes | -- |
| pytha-gemini | glossary_entry | SIMPLE | gemini | P01 | No | -- |

**Why second:** Content layer is independent. All 3 types share P01 KNOWLEDGE and COLLABORATION context.

---

### Wave 3: P01 Content + P03 Prompt Start
> Finish content layer, begin prompt layer with the most complex prompt type.

| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | system_prompt | COMPLEX | opus | P03 | Yes | -- |
| atlas-codex | few_shot_example | SIMPLE | codex | P01 | No | -- |
| pytha-gemini | instruction | MEDIUM | gemini | P03 | Yes | -- |

**Why now:** system_prompt is COMPLEX and foundational (agents depend on it). Pair with simpler types to balance wave time.

---

### Wave 4: P03 Prompt Layer (Complete)
> Remaining prompt types + one runtime config.

| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | action_prompt | COMPLEX | opus | P03 | No | -- |
| atlas-codex | chain | COMPLEX | codex | P03 | No | -- |
| pytha-gemini | spawn_config | SIMPLE | gemini | P12 | No | -- |

**Why group:** action_prompt and chain share P03 KNOWLEDGE. spawn_config is fast filler.

---

### Wave 5: P02+P04 Runtime (Core Agents)
> The two most important runtime types: agent and skill.

| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | agent | COMPLEX | opus | P02 | Yes | system_prompt (W3) |
| atlas-codex | mcp_server | MEDIUM | codex | P04 | Yes | -- |
| pytha-gemini | skill | COMPLEX | gemini | P04 | Yes | -- |

**Why now:** agent depends on system_prompt (W3 done). Skill has template to guide gemini. mcp_server is JSON-structured.

---

### Wave 6: P12 + P07 (Orchestration + Governance)
> Workflow orchestration and evaluation governance.

| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | workflow | COMPLEX | opus | P12 | Yes | signal (done), spawn_config (W4) |
| atlas-codex | golden_test | MEDIUM | codex | P07 | Yes | -- |
| pytha-gemini | scoring_rubric | COMPLEX | gemini | P07 | No | -- |

**Why group:** workflow references signal (done) and spawn_config (W4). golden_test and scoring_rubric share P07 context.

---

### Wave 7: P11 Governance (Complete Core 24)
> Final core types: governance layer.

| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | guardrail | MEDIUM | opus | P11 | No | quality_gate (done) |
| atlas-codex | lifecycle_rule | MEDIUM | codex | P11 | No | -- |
| pytha-gemini | [EMPTY — core complete] | -- | -- | -- | -- | -- |

**Core 24 complete after Wave 7.** 20 types in 7 waves = ~2h wall time.

---

## Phase 3B: Extensions (45 types) — Waves 8-22

### Wave 8: P02 Extensions (Model Layer)
| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | iso_package | COMPLEX | opus | P02 | Yes | agent (W5) |
| atlas-codex | boot_config | MEDIUM | codex | P02 | Yes | model_card (done) |
| pytha-gemini | mental_model_P02 | MEDIUM | gemini | P02 | No | -- |

---

### Wave 9: P02 Extensions + P01 Extensions
| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | satellite_spec | COMPLEX | opus | P08 | Yes | agent (W5) |
| atlas-codex | lens | SIMPLE | codex | P02 | No | -- |
| pytha-gemini | embedding_config | SIMPLE | gemini | P01 | No | -- |

---

### Wave 10: P02 Runtime Extensions
| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | router | SIMPLE | opus | P02 | No | agent (W5) |
| atlas-codex | fallback_chain | SIMPLE | codex | P02 | No | model_card (done) |
| pytha-gemini | axiom | SIMPLE | gemini | P10 | No | -- |

---

### Wave 11: P04 Tools Extensions (Batch 1)
| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | plugin | MEDIUM | opus | P04 | No | skill (W5) |
| atlas-codex | hook | SIMPLE | codex | P04 | No | -- |
| pytha-gemini | scraper | MEDIUM | gemini | P04 | No | -- |

---

### Wave 12: P04 Tools Extensions (Batch 2)
| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | client | SIMPLE | opus | P04 | No | -- |
| atlas-codex | connector | SIMPLE | codex | P04 | No | -- |
| pytha-gemini | daemon | SIMPLE | gemini | P04 | No | -- |

---

### Wave 13: P04 Tools + P05 Output
| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | cli_tool | SIMPLE | opus | P04 | No | -- |
| atlas-codex | output_schema_P05 | MEDIUM | codex | P05 | Yes | -- |
| pytha-gemini | parser | MEDIUM | gemini | P05 | No | -- |

---

### Wave 14: P05 Output Extensions
| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | formatter | MEDIUM | opus | P05 | No | -- |
| atlas-codex | naming_rule | SIMPLE | codex | P05 | No | -- |
| pytha-gemini | output_schema_P06 | SIMPLE | gemini | P06 | No | -- |

---

### Wave 15: P06 Schema Extensions
| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | type_def | SIMPLE | opus | P06 | No | -- |
| atlas-codex | [SKIP — P06 core done] | -- | -- | -- | -- | -- |
| pytha-gemini | [SKIP — P06 core done] | -- | -- | -- | -- | -- |

**Note:** Only 1 P06 extension remains. Merge with Wave 14 or run solo.

---

### Wave 15 (revised): P06 + P07 Evals
| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | e2e_eval | COMPLEX | opus | P07 | Yes | -- |
| atlas-codex | type_def | SIMPLE | codex | P06 | No | -- |
| pytha-gemini | unit_eval | MEDIUM | gemini | P07 | Yes | -- |

---

### Wave 16: P07 Evals Extensions
| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | benchmark | COMPLEX | opus | P07 | No | -- |
| atlas-codex | smoke_eval | MEDIUM | codex | P07 | No | -- |
| pytha-gemini | [SKIP — P07 done] | -- | -- | -- | -- | -- |

---

### Wave 16 (revised): P07 + P08 Architecture
| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | benchmark | COMPLEX | opus | P07 | No | -- |
| atlas-codex | smoke_eval | MEDIUM | codex | P07 | No | -- |
| pytha-gemini | pattern | MEDIUM | gemini | P08 | Yes | -- |

---

### Wave 17: P08 Architecture Extensions
| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | law | MEDIUM | opus | P08 | No | -- |
| atlas-codex | component_map | MEDIUM | codex | P08 | No | -- |
| pytha-gemini | diagram | MEDIUM | gemini | P08 | No | -- |

---

### Wave 18: P09 Config Extensions
| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | env_config | MEDIUM | opus | P09 | Yes | -- |
| atlas-codex | feature_flag | SIMPLE | codex | P09 | Yes | -- |
| pytha-gemini | path_config | SIMPLE | gemini | P09 | No | -- |

---

### Wave 19: P09 Config + P10 Memory
| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | runtime_rule | SIMPLE | opus | P09 | No | -- |
| atlas-codex | permission | SIMPLE | codex | P09 | No | -- |
| pytha-gemini | brain_index | MEDIUM | gemini | P10 | No | -- |

---

### Wave 20: P10 Memory Extensions
| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | mental_model_P10 | MEDIUM | opus | P10 | Yes | -- |
| atlas-codex | learning_record | SIMPLE | codex | P10 | Yes | -- |
| pytha-gemini | session_state | SIMPLE | gemini | P10 | Yes | -- |

---

### Wave 21: P11 Feedback Extensions
| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | bugloop | MEDIUM | opus | P11 | Yes | quality_gate (done) |
| atlas-codex | lifecycle_rule | MEDIUM | codex | P11 | No | -- |
| pytha-gemini | optimizer | MEDIUM | gemini | P11 | No | -- |

**Note:** lifecycle_rule appears in both Wave 7 (core) and here. If completed in W7, replace with next unbuilt type.

---

### Wave 22: P12 Orchestration Extensions
| Slot | Type | Tier | Model | LP | Has Template | Depends On |
|------|------|------|-------|-----|-------------|------------|
| edison | dag | COMPLEX | opus | P12 | No | workflow (W6) |
| atlas-codex | handoff | MEDIUM | codex | P12 | Yes | -- |
| pytha-gemini | dispatch_rule | SIMPLE | gemini | P12 | No | -- |

---

## Execution Summary

### Phase 3A (Core 24)
| Wave | Types | Time Est. | Cumulative |
|------|-------|-----------|------------|
| W1 | interface, input_schema, validator | 15 min | 15 min |
| W2 | context_doc, rag_source, glossary_entry | 15 min | 30 min |
| W3 | system_prompt, few_shot_example, instruction | 20 min | 50 min |
| W4 | action_prompt, chain, spawn_config | 20 min | 1h10 |
| W5 | agent, mcp_server, skill | 20 min | 1h30 |
| W6 | workflow, golden_test, scoring_rubric | 20 min | 1h50 |
| W7 | guardrail, lifecycle_rule, [empty] | 15 min | 2h05 |
| **Subtotal** | **20 types** | — | **~2h** |

### Phase 3B (Extensions)
| Wave | Types | Time Est. | Cumulative |
|------|-------|-----------|------------|
| W8 | iso_package, boot_config, mental_model_P02 | 18 min | 2h23 |
| W9 | satellite_spec, lens, embedding_config | 15 min | 2h38 |
| W10 | router, fallback_chain, axiom | 12 min | 2h50 |
| W11 | plugin, hook, scraper | 15 min | 3h05 |
| W12 | client, connector, daemon | 10 min | 3h15 |
| W13 | cli_tool, output_schema_P05, parser | 12 min | 3h27 |
| W14 | formatter, naming_rule, output_schema_P06 | 12 min | 3h39 |
| W15 | e2e_eval, type_def, unit_eval | 18 min | 3h57 |
| W16 | benchmark, smoke_eval, pattern | 18 min | 4h15 |
| W17 | law, component_map, diagram | 15 min | 4h30 |
| W18 | env_config, feature_flag, path_config | 12 min | 4h42 |
| W19 | runtime_rule, permission, brain_index | 12 min | 4h54 |
| W20 | mental_model_P10, learning_record, session_state | 12 min | 5h06 |
| W21 | bugloop, lifecycle_rule, optimizer | 15 min | 5h21 |
| W22 | dag, handoff, dispatch_rule | 15 min | 5h36 |
| **Subtotal** | **45 types** | — | **~3h30** |

### Grand Total

| Metric | Value |
|--------|-------|
| Total waves | 22 |
| Total types | 65 |
| Total builders (13 files each) | 65 x 13 = **845 files** |
| Estimated wall time | **~5.5 hours** |
| SIMPLE types | 25 (38%) |
| MEDIUM types | 27 (42%) |
| COMPLEX types | 13 (20%) |
| Types with template | 26 (40%) |
| Types without template (GAP) | 39 (60%) |

### Critical Path

```
W1 (P06 spec) ─┬─ W2 (P01 content) ─── W3 (P03 prompt start)
                │                         │
                │                         ├─ W4 (P03 prompt complete)
                │                         │
                └─────────────────────────├─ W5 (P02+P04 runtime) ─── W6 (P12+P07)
                                          │
                                          └─ W7 (P11 governance) ─── CORE COMPLETE
                                                    │
                                                    └─ W8-W22 (extensions, all parallel-safe)
```

### Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| COMPLEX type takes >25 min | Let it run; other 2 slots finish first, monitor |
| Gemini struggles with COMPLEX | Only 2 COMPLEX assigned to gemini (skill, scoring_rubric) — both have templates |
| Git lock contention | 3 parallel slots confirmed safe (CBTEST 2026-03-05) |
| _schema.yaml missing fields | Builder inherits from nearest existing builder as reference |
| No template for 39 types | Use 4 existing builders as structural reference, author from _schema.yaml |

---

*Phase 3 ready for execution. Run with `spawn_grid.ps1 -mission PHASE3 -mode continuous -interactive`*
