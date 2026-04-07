# Phase 3 Wave Plan v2.0: Build + Review Pipeline

**Updated**: 2026-03-26 | **Strategy**: Opus builds, Codex+Gemini review
**Status**: ACTIVE

---

## Pipeline Architecture

| Role | Model | Agent_group | Task |
|------|-------|-----------|------|
| BUILD | Claude/Opus | edison | Construct 3 builders/wave (13 ISO) |
| REVIEW | Codex/GPT-5.4 | edison-codex | Review all 3 (5-point checklist) |
| DEEP REVIEW | Gemini/2.5-pro | edison-gemini | Deep review 1 builder (full cross-check) |

**Why**: Opus 8.5 (aligned). Codex 7.0 (drift). Gemini failed build 3x but can review.

## Review Checklist

1. SCHEMA completeness: defines ALL fields?
2. TEMPLATE alignment: uses ALL SCHEMA fields?
3. EXAMPLE validity: golden passes ALL HARD gates?
4. CONFIG consistency: naming matches SCHEMA?
5. Vocabulary: kind/pillar (not type/lp)?

---

## Done (5/78)

| Kind | Pillar | Built By | Score |
|------|--------|----------|-------|
| model_card | P02 | opus | 9.0 |
| knowledge_card | P01 | opus | 9.0 |
| signal | P12 | opus | 9.0 |
| quality_gate | P11 | opus | 9.0 |
| validator | P06 | opus | 9.0 |

---

## Phase 3A: Core 24 (19 remaining)

### Wave 1: P06 Spec + P01 Content [x]
| Kind | Tier | Pillar |
|------|------|--------|
| interface | MEDIUM | P06 |
| input_schema | SIMPLE | P06 |
| glossary_entry | SIMPLE | P01 |

### Wave 2: P01 Content [x]
| Kind | Tier | Pillar |
|------|------|--------|
| context_doc | MEDIUM | P01 |
| rag_source | SIMPLE | P01 |
| few_shot_example | SIMPLE | P01 |

### Wave 3: P03 Prompt Start [x]
| Kind | Tier | Pillar |
|------|------|--------|
| system_prompt | COMPLEX | P03 |
| instruction | MEDIUM | P03 |
| action_prompt | COMPLEX | P03 |

### Wave 4: P03+P12 [x]
| Kind | Tier | Pillar |
|------|------|--------|
| chain | COMPLEX | P03 |
| spawn_config | SIMPLE | P12 |
| workflow | COMPLEX | P12 |

### Wave 5: P02+P04 Core Agents [x]
| Kind | Tier | Pillar |
|------|------|--------|
| agent | COMPLEX | P02 |
| skill | COMPLEX | P04 |
| mcp_server | MEDIUM | P04 |

### Wave 6: P07+P11 Governance [x]
| Kind | Tier | Pillar |
|------|------|--------|
| golden_test | MEDIUM | P07 |
| scoring_rubric | COMPLEX | P07 |
| guardrail | MEDIUM | P11 |

### Wave 7: P11 Final Core [x]
| Kind | Tier | Pillar |
|------|------|--------|
| lifecycle_rule | MEDIUM | P11 |

**Core 24 complete after Wave 7.**

---

## Phase 3B: Extensions (53 remaining)

### Wave 8: P02 Model [x]
agent_package (COMPLEX), boot_config (MEDIUM), mental_model (MEDIUM)

### Wave 9: P02+P08 [x]
lens (SIMPLE), agent_card (COMPLEX), embedding_config (SIMPLE)

### Wave 10: P02+P10 [ ]
router (MEDIUM), fallback_chain (MEDIUM), axiom (SIMPLE)

### Wave 11: P08 Architecture [ ]
pattern (MEDIUM), law (SIMPLE), diagram (SIMPLE)

### Wave 12: P08+P03 [ ]
component_map (MEDIUM), prompt_template (MEDIUM), meta_prompt (COMPLEX)

### Wave 13: P03 Advanced [ ]
chain_of_thought (COMPLEX), react (COMPLEX), planner (COMPLEX)

### Wave 14: P05 Output [ ]
response_format (MEDIUM), parser (MEDIUM), formatter (SIMPLE)

### Wave 15: P05+P06 [ ]
naming_rule (SIMPLE), type_def (MEDIUM), validation_schema (MEDIUM)

### Wave 16: P06+P04 [ ]
artifact_blueprint (MEDIUM), grammar (COMPLEX), hook (MEDIUM)

### Wave 17: P04 Tools [ ]
plugin (MEDIUM), client (MEDIUM), cli_tool (SIMPLE)

### Wave 18: P04 Advanced [ ]
scraper (MEDIUM), connector (MEDIUM), daemon (COMPLEX)

### Wave 19: P04+P07 [ ]
component (MEDIUM), unit_eval (MEDIUM), smoke_eval (SIMPLE)

### Wave 20: P07+P09 [ ]
e2e_eval (COMPLEX), benchmark (MEDIUM), env_config (SIMPLE)

### Wave 21: P09 Config [ ]
path_config (SIMPLE), feature_flag (SIMPLE), runtime_rule (MEDIUM)

### Wave 22: P09+P10 [ ]
permission (MEDIUM), runtime_state (MEDIUM), knowledge_index (MEDIUM)

### Wave 23: P10+P11 [ ]
learning_record (SIMPLE), session_state (SIMPLE), bugloop (MEDIUM)

### Wave 24: P11+P12 [ ]
optimizer (MEDIUM), dag (COMPLEX), handoff (MEDIUM)

### Wave 25: P12 Final [ ]
dispatch_rule (MEDIUM), crew (COMPLEX)

---

## Totals

| Phase | Waves | Builders | Status |
|-------|-------|----------|--------|
| Done | 0-9 | 30 | COMPLETE |
| 3A Core | 1-7 | 24 | COMPLETE |
| 3B Ext | 8-25 | 53 | 6/53 DONE |
| Total | 25 | 77 | 30/77 (39%) |

**Time**: ~25 waves x 20min build + review overlap = ~9h effective

---
*v2.0 | Build: Opus | Review: Codex+Gemini | 2026-03-26*