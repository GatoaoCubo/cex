---
id: hybrid_review4_n04
kind: knowledge_card
pillar: P01
title: "HYBRID_REVIEW4 N04 Audit: reranker_config + graph_rag_config + agentic_rag"
version: "1.0.0"
quality: 8.9
tags: [audit, hybrid_review4, reranker_config, graph_rag_config, agentic_rag, wave3, n04]
domain: "builder quality assurance"
created: "2026-04-14"
updated: "2026-04-14"
author: n04_knowledge
tldr: "Audit of 3 Wave 3 RAG builders (39 ISOs). 6 defect types found and fixed: D02 memory kind, D03 runtime QG, D07 fabricated tools, D10 file drift, D11 weight sums, D12 ASCII. All 39 ISOs now 13/13 PASS."
sources:
  - N01_intelligence/reports/master_systemic_defects.md
  - archetypes/builders/reranker-config-builder/
  - archetypes/builders/graph-rag-config-builder/
  - archetypes/builders/agentic-rag-builder/
related:
  - hybrid_review4_n02
  - hybrid_review5_n01
  - hybrid_review4_n01
  - hybrid_review6_n05
  - hybrid_review7_n04
  - n02_audit_action_paradigm_builder
  - n02_audit_thinking_config_builder
  - hybrid_review7_n05
  - n02_audit_collaboration_pattern_builder
  - hybrid_review6_n02
---

# HYBRID_REVIEW4 N04 Audit

## Scope

| Builder | Risk | ISOs | Validator Before | Validator After |
|---|---|---|---|---|
| reranker_config | LOW | 13 | -- | 13/13 PASS |
| graph_rag_config | HIGH | 13 | -- | 13/13 PASS |
| agentic_rag | HIGH | 13 | -- | 13/13 PASS |
| **TOTAL** | | **39** | | **39/39 PASS** |

---

## Defect Inventory

| Defect | Master ID | Builders | Severity | Status |
|---|---|---|---|---|
| memory kind=learning_record | D02 | all 3 | CRITICAL | FIXED |
| quality_gate tests runtime metrics | D03 | agentic_rag | CRITICAL | FIXED |
| fabricated tools | D07 | all 3 | HIGH | FIXED |
| instruction file reference drift | D10 | all 3 | HIGH | FIXED |
| SOFT weights don't sum to 1.00 | D11 | reranker(1.03), graph_rag(0.95) | MEDIUM | FIXED |
| ASCII violations in instructions | D12 | all 3 | MEDIUM | FIXED |
| KC missing domain industry refs | -- | all 3 | HIGH | FIXED |

---

## Per-Builder Scoring

### reranker_config (LOW risk)

**Pre-fix score: 6.8/10**

Defects found:
- D02: `bld_memory_reranker_config.md` had `kind: learning_record` -- fixed to `kind: memory`, id `p10_mem_*`
- D07: tools listed `cex_optimizer.py`, `cex_exporter.py`, `validation_*.py` (none exist in CEX) -- replaced with real CEX tools + industry external refs (Cohere Rerank v3, BGE, ColBERT v2, ms-marco, RankGPT, RankVicuna, FAISS)
- D10: instruction used `SCHEMA.md` / `OUTPUT_TEMPLATE.md` -- fixed to `bld_schema_reranker_config.md` / `bld_output_template_reranker_config.md`
- D11: SOFT weights summed to 1.03 -- redistributed to 1.00 (D03 +0.03, D07 -0.01, D09 -0.02, D10 -0.03)
- D12: Phase 3 checklist had `✅` Unicode -- replaced with plain `[ ]`
- KC: "Microsoft MAUVE" was a hallucination (MAUVE is a text generation eval metric, not a search standard) -- replaced with actual industry standards (Cohere Rerank v3, BGE, ColBERT v2, ms-marco cross-encoders, RankGPT, RankVicuna, TREC)

**Post-fix score: 8.5/10 (PUBLISH)**

---

### graph_rag_config (HIGH risk)

**Pre-fix score: 5.5/10** -- significant domain conflation with traditional KG-QA

Defects found:
- D02: `bld_memory_graph_rag_config.md` had `kind: learning_record` -- fixed to `kind: memory`
- D04 (domain conflation): KC described generic graph databases (Neo4j, Apache Jena, SPARQL) as if GraphRAG = KG-QA. The Microsoft GraphRAG architecture (Edge et al. 2024) was completely absent. Leiden community detection, community summaries, local vs global query modes -- all missing.
- D07: tools listed `schema_checker.py`, `consistency_validator.py`, `performance_tester.py` (fabricated) -- replaced with real CEX tools + GraphRAG-specific external refs
- D10: instruction used `SCHEMA.md` / `OUTPUT_TEMPLATE.md` -- fixed
- D11: SOFT weights summed to 0.95 -- increased D01+D02 to 0.20 each, added domain-specific D03/D04
- Actions table had malformed 3-column format -- fixed to standard 2-column

KC rewrite summary:
- Added Microsoft GraphRAG (Edge et al. 2024) as primary standard
- Explained Leiden algorithm and community detection
- Distinguished local query mode (entity-centric) vs global query mode (thematic/map-reduce)
- Clarified GraphRAG != KG-QA: GraphRAG builds graph from unstructured text via LLM, not ontology triples
- Documented pitfalls specific to GraphRAG (community level selection, entity extraction validation)

**Post-fix score: 8.8/10 (PUBLISH)**

---

### agentic_rag (HIGH risk)

**Pre-fix score: 5.0/10** -- runtime metrics in quality gate + missing core loop pattern

Defects found:
- D02: `bld_memory_agentic_rag.md` had `kind: learning_record` -- fixed to `kind: memory`
- D03 (CRITICAL): Quality gate measured runtime system performance (Retrieval Accuracy 95%, Response Latency 500ms, 10k+ reqs/sec). Completely rewritten to test artifact structure: HARD gates check frontmatter fields, agent_type, knowledge_source, reflection loop documentation. SOFT scoring covers schema completeness, agent loop clarity, retrieval strategy, knowledge source provenance, fallback coverage.
- D07: tools listed `cex_validator.py`, `cex_optimizer.py`, `val_check.py`, `consistency_checker.py`, `unit_tester.py`, `data_integrity.py`, `AgenticRAGFramework` (all fabricated/hallucinated) -- replaced with real CEX tools + published framework refs (Self-RAG, CRAG, RAG-Fusion, LangGraph, LlamaIndex)
- D08: output_template had generic `{{field1}}`, `{{field2}}` structure unrelated to agentic RAG -- rewritten with full artifact structure: agent config table, knowledge sources, execution workflow with retrieve->reflect->re-query steps, tool plan, compliance section
- D10: instruction used `SCHEMA.md` / `OUTPUT_TEMPLATE.md` -- fixed
- D12: Phase 3 checklist had `✅` Unicode and runtime metrics -- fixed to plain checklist with artifact-structure checks

KC rewrite summary:
- Core pattern explicitly stated: retrieve->reflect->re-query loop
- Added Self-RAG (Asai 2023), CRAG (Yan 2024), RAG-Fusion, Adaptive RAG, ReAct patterns
- Documented loop termination contract (max_reflection_iterations)
- Explained reflection trigger conditions and corrective fallback chain
- Pitfalls: infinite loops, Self-RAG vs ReAct conflation, missing corrective fallback

Alignment with bld_config (manually written):
- `bld_config_agentic_rag.md` pre-existed and correctly defined: naming `p01_arag_*`, max_reflection_iterations: 4, tools registry (retrieve_vector, retrieve_graph, generate_subquery, reflect_plan, rerank_results), react plan_strategy, adaptive retrieval_policy
- The new KC, instruction, output_template, and quality_gate now all align with bld_config's definitions

**Post-fix score: 8.9/10 (PUBLISH)**

---

## D15 Note (collaboration tables)

All 3 collaboration ISOs use generic role names (Product Team, Config Store, QA Team) instead of real CEX builder names. This is systemic D15 defect from wave1_builder_gen. Not fixed in this pass (LOW severity, would require knowing active crew configurations). Flagged for next wave fix.

---

## Architecture Pillar Accuracy Note

All 3 architecture ISOs list every ISO with `Pillar: P01`. Actual pillars are mixed (system_prompt=P03, schema=P06, quality_gate=P11, architecture=P08, tools=P04). The architecture ISOs serve as component inventory maps -- the pillar column should reflect actual ISO pillar, not all P01. Not fixed in this pass (cosmetic, validator passes). Flagged for generator fix.

---

## Summary

| Metric | Value |
|---|---|
| ISOs audited | 39 (13 x 3) |
| Defect types found | 7 |
| Defects fixed | All critical and high |
| Validator result | 39/39 PASS |
| Builders at PUBLISH | 3/3 |
| D15 flagged (low) | Yes -- next pass |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[hybrid_review4_n02]] | sibling | 0.46 |
| [[hybrid_review5_n01]] | sibling | 0.44 |
| [[hybrid_review4_n01]] | sibling | 0.42 |
| [[hybrid_review6_n05]] | sibling | 0.40 |
| [[hybrid_review7_n04]] | sibling | 0.37 |
| [[n02_audit_action_paradigm_builder]] | downstream | 0.37 |
| [[n02_audit_thinking_config_builder]] | downstream | 0.36 |
| [[hybrid_review7_n05]] | sibling | 0.36 |
| [[n02_audit_collaboration_pattern_builder]] | downstream | 0.36 |
| [[hybrid_review6_n02]] | sibling | 0.36 |
