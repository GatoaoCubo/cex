---
id: p01_kc_engineering_vocabulary
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Knowledge Card -- Engineering Vocabulary (N03 Controlled)"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: artifact-construction
quality: 9.2
tags: [knowledge-card, vocabulary, N03, controlled-vocabulary, engineering, 8F, ubiquitous-language]
tldr: "N03's controlled vocabulary KC. 22 canonical engineering terms with definitions, CEX applications, anti-patterns, and industry sources. Loaded at F2b SPEAK to enforce ubiquitous language in all N03 outputs."
density_score: 0.92
updated: "2026-04-17"
related:
  - p03_sp_n03_creation_nucleus
  - bld_collaboration_quality_gate
  - agent_card_n03
  - p03_sp_engineering_nucleus
  - p02_agent_creation_nucleus
  - agent_card_engineering_nucleus
  - bld_collaboration_validation_schema
  - p03_sp_kind_builder
  - bld_collaboration_golden_test
  - ctx_cex_new_dev_guide
---

# Knowledge Card: Engineering Vocabulary (N03 Controlled)

## Purpose

This is N03's LANGUAGE MODEL -- the terms it thinks and speaks in.
Loaded at **F2b SPEAK** before every F3-F8 execution.
Zero tolerance for vocabulary drift once this KC is loaded.

## Canonical Terms

| Term | Industry Definition | CEX Application | Anti-Pattern |
|------|-------------------|-----------------|-------------|
| contract_first_design | Define the API/schema before implementation (Bertrand Meyer, 1988) | P06 artifacts before F6 PRODUCE; input_schema before builder | Building artifacts without a type contract |
| interface_segregation | No client should depend on methods it does not use (SOLID-I) | interface_builder_protocol.md: builders expose ONLY their contract | Omnibus interfaces with unused methods |
| type_safety | Operations only apply to appropriate types; enforced statically or at runtime | type_def_cex_types.md: typed Kind, Pillar, Nucleus | Passing kind names as raw strings without validation |
| schema_validation | Verify data conforms to a defined structure before processing | validation_schema_artifact.md: L1 hard gates + L2 soft gates | Assuming frontmatter is valid without parsing |
| invariant | A property that always holds true regardless of program state (Hoare, 1969) | invariant_n03.md: 18 system properties that never break | Treating invariants as guidelines or best practices |
| idempotency | Applying an operation multiple times has same effect as once (REST semantics) | F8 COLLABORATE: compiling same artifact twice = same .yaml | Build scripts that fail if run twice |
| dependency_inversion | Depend on abstractions, not concretions (SOLID-D) | Builders depend on builder protocol interface, not specific nucleus | Hard-coding claude-opus as executor instead of routing via interface |
| separation_of_concerns | Each component addresses a single concern (Dijkstra, 1974) | P06 (contracts) separate from P07 (evaluation) separate from P11 (feedback) | quality_gate that also writes artifacts |
| technical_debt | Cost of future rework from choosing easy solution now (Ward Cunningham, 1992) | Artifacts with quality < 7.0 that ship; accumulate in cex_evolve.py queue | Ignoring WARN signals in quality gate |
| refactoring | Restructuring code without changing external behavior (Fowler, 1999) | MIGRATE verb: schema migration without changing artifact content | Rewriting artifact content during version bump |
| test_pyramid | Unit > Integration > E2E (broad base, narrow top) (Mike Cohn) | golden_test (unit) -> cex_doctor (integration) -> cex_system_test (E2E) | Only running E2E tests; skipping golden tests |
| coverage_target | Minimum % of code/artifacts validated by tests | N03 quality gate: all P06 artifacts pass compile before commit | Shipping without compile check |
| cyclomatic_complexity | Number of linearly independent paths through code (McCabe, 1976) | Artifact section depth: no more than 3 levels of nesting | Deep nested YAML with 5+ indent levels |
| design_pattern | Reusable solution to common software design problem (GoF, 1994) | Construction Triad (Template-First / Hybrid / Fresh) is N03's build pattern | Solving the same builder selection problem differently each time |
| anti_pattern | Common response to recurring problem that is ineffective or counterproductive | Self-scoring (quality != null), placeholder text, invented kinds | Treating anti-patterns as optional guidelines |
| architectural_decision_record | Document capturing why an architectural decision was made (Michael Nygard, 2011) | decision_record artifacts in P08; permanent record of WHY, not just WHAT | Changing architecture without documenting rationale |
| convention_over_configuration | Sensible defaults reduce need for explicit configuration (Rails principle) | CEX: kind -> pillar -> directory follows convention; no config needed | Requiring explicit directory for every artifact |
| ubiquitous_language | Shared vocabulary between domain experts and developers (DDD, Evans 2003) | kc_{domain}_vocabulary.md per nucleus; all LLM-to-LLM comms use canonical terms | Using "research card" instead of knowledge_card |
| bounded_context | Explicit boundary within which a model applies consistently (DDD) | N03 boundary: artifact construction, schema, quality enforcement. N07 boundary: orchestration | N03 building orchestration artifacts (out of bounded context) |
| aggregate_root | Cluster of domain objects treated as a unit for data changes (DDD) | Kind+Pillar+Builder is the aggregate root for artifact construction | Treating kind, pillar, builder as independent entities |
| regression | Defect introduced by a change that previously worked correctly | regression_check_n03.md: quality drop >= 0.5 from baseline | Accepting quality drops as "normal variation" |
| density_score | Ratio of structured content (tables+code+lists) to total body bytes | frontmatter field; target >= 0.85; computed by cex_score.py | Using prose paragraphs when a table would serve |

## Cross-Nucleus Shared Terms (DO NOT REDEFINE)

These terms are defined in N00_genesis and must not be redefined in this KC:
- `8F pipeline` (F1-F8): canonical reasoning protocol (.claude/rules/8f-reasoning.md)
- `kind`: atomic artifact type from the 257-kind taxonomy (.cex/kinds_meta.json)
- `pillar`: P01-P12 domain grouping (N00_genesis/P{01-12}_*/_schema.yaml)
- `nucleus`: N00-N07 operational agent (N0X_*/P08_architecture/nucleus_def_n0X.md)
- `quality_gate`: F7 GOVERN validation (quality_gate_n03.md)
- `signal`: F8 COLLABORATE completion notification (signal_writer.py)
- `builder`: 1 of 259 specialized agents in archetypes/builders/

## Trigger Phrases -> Combo Activation

| User says | N03 activates |
|-----------|--------------|
| "define contracts" / "schema first" | COMBO B: Schema Foundation (P06 all 6 kinds) |
| "quality check" / "validate artifact" | COMBO C: Quality Engine (scoring_rubric + llm_judge + regression_check) |
| "how is this structured" / "architecture" | COMBO D: Architecture Blueprint (component_map + invariant + pattern) |
| "build pipeline" / "workflow for" | COMBO E: Pipeline Orchestration (workflow + dag + checkpoint) |
| "run the builder" / "create artifact" | COMBO A: Builder Stack (agent + system_prompt + quality_gate) |

## Source Hierarchy

When a term conflict occurs, resolve in this order:
1. p03_pc_cex_universal.md (prompt_compiler -- 300 kinds, highest authority)
2. spec_metaphor_dictionary.md (Industry term column)
3. N00_genesis/P01_knowledge/kc_*.md (canonical N00 definitions)
4. This file (N03 domain extensions)
5. types_meta.json (kind names only)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_n03_creation_nucleus]] | downstream | 0.27 |
| [[bld_collaboration_quality_gate]] | downstream | 0.25 |
| [[agent_card_n03]] | related | 0.24 |
| [[p03_sp_engineering_nucleus]] | downstream | 0.23 |
| [[p02_agent_creation_nucleus]] | downstream | 0.22 |
| [[agent_card_engineering_nucleus]] | downstream | 0.22 |
| [[bld_collaboration_validation_schema]] | downstream | 0.21 |
| [[p03_sp_kind_builder]] | downstream | 0.21 |
| [[bld_collaboration_golden_test]] | downstream | 0.20 |
| [[ctx_cex_new_dev_guide]] | related | 0.20 |
