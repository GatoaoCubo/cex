---
id: terminology_sweep_2026_04_08
kind: context_doc
title: "Terminology Sweep Report -- capability_summary rename + Portuguese cleanup"
version: 1.0.0
quality: 9.1
pillar: P01
created: 2026-04-08
author: n03_builder
tags: [terminology, rename, sweep, maintenance]
related:
  - bld_collaboration_builder
  - bld_architecture_kind
  - kind-builder
  - _builder-builder
  - bld_knowledge_card_builder
  - bld_collaboration_kind
  - bld_config_builder
  - bld_collaboration_validation_schema
  - bld_architecture_builder
  - bld_collaboration_retriever
---

# Terminology Sweep Report (2026-04-08)

## Part 1: capability_summary rename

| Metric | Value |
|--------|-------|
| Total files renamed | 146 |
| Builder manifests (bld_manifest_*.md) | 124 |
| Python tools updated | 2 (cex_schema_hydrate.py, test_schema_evolution.py) |
| Builder-builder templates | 5 (README, meta_manifest, schema, config, meta_manifest routing) |
| Remaining references | 14 (archive, compiled, nucleus output, retriever_index) |
| New field name | `capabilities` (A2A agent card standard) |
| Old field name | `capability_summary` (non-standard compound) |

### Verification

| Check | Result |
|-------|--------|
| cex_doctor.py | 123 PASS / 0 WARN / 0 FAIL |
| test_schema_evolution.py | 15/15 PASS |
| grep capability_summary | 0 in active code (2 in ROADMAP.md history text) |

### Bonus fix

Fixed `observation_types` in 4 newer builders (citation, context-window-config, multi-modal-config, prompt-cache) -- was `[reference]`, now `[user, feedback, project, reference]`.

---

## Part 2: Portuguese terminology sweep

### Fixed (10 instances in meta templates)

| File | Before | After |
|------|--------|-------|
| bld_meta_manifest_builder.md | "frases", "produz", "ativam", "termos", "naturais", "Manter sincronizado" | "sentences", "produces", "activate", "terms", "natural", "Keep synchronized" |
| bld_manifest_builder.md | "cria outros builders", "gera", "qualquer", "precisa" (L1/L2/L3) | "creates other builders", "generates", "any", "needs" |
| bld_manifest_builder.md | "cria builder", "novo kind precisa builder" (triggers) | "create builder", "new kind needs builder" |
| bld_meta_instructions_builder.md | "Fase de coleta", "Escolha", "reflete" | "Collection phase", "Choose", "reflects" |
| bld_meta_knowledge_builder.md | "vizinhos confusos", "Padrao identico", "Buscar overlaps" | "confusing neighbors", "Pattern identical", "Search overlaps" |
| bld_meta_quality_gates_builder.md | "items de verification ANTES de comecar" | "verification items BEFORE starting" |
| bld_meta_tools_builder.md | "validatar existente", "OBRIGATORIA", "bloqueadas", "resultado final", "vence conflito" | "existing validator", "REQUIRED", "blocked", "final result", "wins on conflict" |
| bld_meta_system_prompt_builder.md | "frases about o that the builder sabe" | "sentences about what the builder knows" |

### Remaining (37 occurrences in 24 files)

These are scattered across individual builder ISOs (not templates). Breakdown:

| Category | Files | Occurrences | Examples |
|----------|-------|-------------|----------|
| _builder-builder meta (other) | 8 | 19 | bld_meta_architecture, bld_meta_collaboration, bld_meta_examples, bld_meta_memory, bld_meta_schema, bld_meta_config, bld_meta_output_template |
| Individual builder manifests | 10 | 12 | handoff, dispatch-rule, schedule, bugloop, rag-source, multi-modal-config, reward-signal, search-tool, system-prompt |
| Individual builder examples | 4 | 4 | golden-test, input-schema, unit-eval, e2e-eval |
| Manifest L1/L2/L3 text | 2 | 2 | bugloop, search-tool |

### Priority for next sweep

1. **High**: 8 remaining _builder-builder meta files (19 occurrences) -- these propagate
2. **Medium**: 10 individual manifests with Portuguese in capabilities text
3. **Low**: 4 example files with Portuguese in comments

## Boundary

Contexto de dominio para hidratar prompts. NAO eh knowledge_card (sem density gate) nem glossary_entry (nao define termo).


## 8F Pipeline Function

Primary function: **INJECT**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_builder]] | downstream | 0.41 |
| [[bld_architecture_kind]] | downstream | 0.38 |
| [[kind-builder]] | downstream | 0.36 |
| [[_builder-builder]] | downstream | 0.35 |
| [[bld_knowledge_card_builder]] | related | 0.34 |
| [[bld_collaboration_kind]] | downstream | 0.31 |
| [[bld_config_builder]] | downstream | 0.31 |
| [[bld_collaboration_validation_schema]] | downstream | 0.28 |
| [[bld_architecture_builder]] | downstream | 0.28 |
| [[bld_collaboration_retriever]] | downstream | 0.28 |
