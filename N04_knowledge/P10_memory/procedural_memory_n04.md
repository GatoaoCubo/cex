---
id: p10_pm_n04_knowledge
kind: procedural_memory
8f: F3_inject
pillar: P10
nucleus: n04
title: "Procedural Memory -- N04 Standard Operating Procedures"
version: "1.0.0"
quality: 9.1
tags: [procedural_memory, n04, sop, rag, knowledge_card, indexing, P10]
domain: knowledge management
status: active
created: "2026-04-17"
updated: "2026-04-17"
author: n04_knowledge
tldr: "N04 task procedure memory: step-by-step SOPs for the most common operations -- KC creation, RAG corpus ingestion, retrieval debugging, memory consolidation, taxonomy extension, and artifact quality review."
density_score: null
related:
  - bld_collaboration_kind
  - kind-builder
  - bld_architecture_kind
  - self_audit_n04_codex_2026_04_15
  - p11_qg_knowledge
  - agent_card_n04
  - n04_rag_pipeline_memory
  - bld_instruction_kind
  - agent_card_engineering_nucleus
  - bld_tools_kind
---

# Procedural Memory: N04 Standard Operating Procedures

## About This File

This is N04's procedural memory layer -- how N04 DOES things, not what it knows.
Loaded at every session start. When a new procedure is learned, it is appended here.

---

## SOP-01: Knowledge Card Creation

**Trigger**: user says "document this", "create a KC", or new concept discovered

1. Check if KC already exists: `python _tools/cex_retriever.py --query "{concept}" --top-k 3`
2. If exists (similarity >= 0.90): update existing KC, do not duplicate
3. If new: load builder ISO `archetypes/builders/knowledge-card-builder/`
4. Run F1 CONSTRAIN: kind=knowledge_card, pillar=P01, nucleus=n04
5. Run F2 BECOME: knowledge-card-builder (13 ISOs)
6. Run F3 INJECT: load domain KCs, examples from P01_knowledge/
7. Draft KC with: id, kind, pillar, nucleus, title, version, quality: null, tags, domain, tldr
8. Body: Definition > Industry Context > CEX Application > Cross-references > Properties table
9. Run F7 GOVERN: quality gate (min 7/7 HARD gates)
10. Save to `N04_knowledge/P01_knowledge/kc_{name}.md`
11. Compile: `python _tools/cex_compile.py N04_knowledge/P01_knowledge/kc_{name}.md`
12. Index auto-triggered by post-compile hook

---

## SOP-02: RAG Corpus Ingestion (New Source)

**Trigger**: new document type, external source, or large batch ingestion

1. Load `document_loader_n04.md` (P04) for source type config
2. Determine document type per `type_def_document_types.md` (P06)
3. Apply chunking strategy per `chunk_strategy_knowledge.md` (P01)
   - PDF/web: 512-token sliding, 128-token overlap
   - Code: function-level chunks
   - KCs: whole document
4. Embed: text-embedding-3-small (1536 dim)
5. Upsert to pgvector: `api_reference_rag_apis.md` -> `upsert_document` endpoint
6. Verify: query the just-ingested content with `match_documents`
7. Log ingestion: append to `workflow_rag_ingestion.md` (P12) run log

---

## SOP-03: Retrieval Debugging

**Trigger**: retrieval returns wrong results, misses obvious answer, or low scores

1. Check query against `input_schema_knowledge_query.md` (P06) -- is it valid?
2. Test dense-only mode: `cex_retriever.py --mode dense --query "{query}"`
3. Test sparse-only mode: `cex_retriever.py --mode sparse --query "{query}"`
4. Compare scores -- if dense wins but still low: check embedding quality
5. Try query expansion: add `--expand` flag (HyDE)
6. Reduce score_threshold from 0.65 to 0.55
7. Check if content is indexed: `cex_doctor.py --check-index`
8. If not indexed: run `cex_compile.py --all` then reindex
9. Log findings in `P07_evals/hybrid_review_n04.md`

---

## SOP-04: Memory Consolidation (Manual Trigger)

**Trigger**: after large mission, session_memory growth > 50 entries, or `/consolidate` command

1. Run: `python _tools/cex_memory_update.py --prune --decay`
2. Extract session learnings: `python _tools/cex_memory_select.py --session`
3. Update learning record: `N04_knowledge/P11_feedback/learning_record_n04.md`
4. Deduplication check: `python _tools/cex_retriever.py --deduplicate --threshold 0.95`
5. For each near-duplicate pair: merge per `consolidation_policy_n04.md` rules
6. Run: `python _tools/cex_compile.py --all`
7. Commit: `git add N04_knowledge/ && git commit -m "[N04] memory consolidation: {summary}"`

---

## SOP-05: Taxonomy Extension (Adding New Kind)

**Trigger**: encounter a concept that has no existing kind in 257-kind taxonomy

1. Check: is this concept 80% covered by an existing kind? (use cex_retriever)
2. If yes: document as sub-variant in existing KC, do not create new kind
3. If no: create proposal in `N04_knowledge/P01_knowledge/kc_{new_kind}.md`
4. Frontmatter flag: `status: proposed`
5. Signal N07: "N04 proposes new kind: {kind_name}" via write_signal
6. N07 decides: accept (update kinds_meta.json) or reject (redirect to existing kind)
7. If accepted: trigger builder bootstrap (`cex_materialize.py --kind {name}`)

---

## SOP-06: Artifact Quality Review

**Trigger**: N07 dispatches quality review task, or artifact quality score < 8.0

1. Load artifact: read full content
2. Check frontmatter completeness: all required fields present, quality: null
3. Run quality gate from `P07_evals/quality_gate_knowledge.md`
4. Score body: density >= 0.85? structured data > prose? cross-references present?
5. Apply scoring rubric from `P07_evals/scoring_rubric_knowledge.md`
6. If score >= 8.5: mark for peer review, append to review queue
7. If score 7.0-8.4: flag improvements, optionally rewrite weak sections
8. If score < 7.0: full rewrite required, reload builder ISOs
9. Log review in `P07_evals/hybrid_review_n04.md`

---

## SOP-07: Responding to N07 Dispatch

**Trigger**: handoff file written to `.cex/runtime/handoffs/` or `n04_task.md`

1. Read handoff immediately (first action)
2. Parse: mission, nucleus, wave, priority, kind list, paths
3. Load relevant builder ISOs (F2 BECOME)
4. Run 8F pipeline: F1 -> F8
5. Build all specified artifacts
6. Compile: `python _tools/cex_compile.py --all`
7. Signal: `python -c "from _tools.signal_writer import write_signal; write_signal('n04', 'complete', 9.0)"`
8. Commit: `git add N04_knowledge/ && git commit -m "[N04] {mission}: {summary}"`

---

## Procedure Update Log

| Date | Procedure | Change |
|------|-----------|--------|
| 2026-04-17 | SOP-01 to SOP-07 | Initial creation (SELF_ASSEMBLY W1) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_kind]] | downstream | 0.32 |
| [[kind-builder]] | upstream | 0.28 |
| [[bld_architecture_kind]] | upstream | 0.26 |
| [[self_audit_n04_codex_2026_04_15]] | upstream | 0.26 |
| [[p11_qg_knowledge]] | downstream | 0.24 |
| [[agent_card_n04]] | upstream | 0.24 |
| [[n04_rag_pipeline_memory]] | related | 0.24 |
| [[bld_instruction_kind]] | upstream | 0.24 |
| [[agent_card_engineering_nucleus]] | upstream | 0.24 |
| [[bld_tools_kind]] | upstream | 0.23 |
