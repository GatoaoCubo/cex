---
quality: 7.7
id: ontology_cex_vocabulary
kind: knowledge_card
8f: F3_inject
pillar: P01
nucleus: N01
title: CEX Domain Formal Ontology
version: "1.0"
density_score: 0.96
tags: [ontology, vocabulary, cex-core, cross-synthesis, owl, formal-semantics, ubiquitous-language]
created: 2026-04-17
updated: 2026-04-17
sources:
  - .claude/rules/ubiquitous-language.md
  - N01_intelligence/P01_knowledge/kc_intelligence_vocabulary.md
  - _docs/specs/spec_metaphor_dictionary.md
  - .cex/kinds_meta.json
type: ontology
related:
  - n04_competitive_knowledge
  - cex_llm_vocabulary_whitepaper
  - p03_sp_cex_core_identity
  - index
  - spec_n07_bootstrap_context
  - n07_memory_industry_audit
  - taxonomy_completeness_audit
  - spec_cex_system_map
  - p10_entity_cex_system
  - p08_pat_nucleus_fractal
---

## Purpose

Formal ontology of the CEX typed knowledge system. Defines classes, properties, and relationships
in a machine-readable structure. Maps CEX-native terms to OWL/RDF and industry-standard equivalents.

Audience: LLM-to-LLM communication, cross-nucleus vocabulary enforcement, external system integration.

---

## Classes

### Class 1: Kind

| Attribute | Value |
|-----------|-------|
| OWL equivalent | `owl:Class` with URI `cex:Kind` |
| Industry term | Artifact type, Schema type, Resource type |
| CEX definition | Atomic unit of typed knowledge; one of 257 canonical types |
| Instances | 257 (ab_test_config .. workflow_run_crate) |
| Superclass | `cex:Artifact` |
| Registry | `.cex/kinds_meta.json` |

**Kind subclasses by LLM function:**

| Subclass | OWL | LLM Function | Count | Examples |
|----------|-----|-------------|-------|---------|
| ConstraintKind | cex:ConstraintKind | CONSTRAIN (F1) | 49 | chunk_strategy, env_config, embedding_config |
| IdentityKind | cex:IdentityKind | BECOME (F2) | 12 | agent, agent_card, nucleus_def, model_card |
| KnowledgeKind | cex:KnowledgeKind | INJECT (F3) | 45 | knowledge_card, citation, few_shot_example |
| ReasoningKind | cex:ReasoningKind | REASON (F4) | 7 | decision_record, planning_strategy, dispatch_rule |
| ToolKind | cex:ToolKind | CALL (F5) | 30 | mcp_server, browser_tool, cli_tool, webhook |
| OutputKind | cex:OutputKind | PRODUCE (F6) | 35 | landing_page, pitch_deck, press_release |
| GovernanceKind | cex:GovernanceKind | GOVERN (F7) | 70 | quality_gate, guardrail, benchmark, threat_model |
| CollaborationKind | cex:CollaborationKind | COLLABORATE (F8) | 5 | signal, handoff, workflow |

---

### Class 2: Pillar

| Attribute | Value |
|-----------|-------|
| OWL equivalent | `owl:Class` with URI `cex:Pillar` |
| Industry term | Domain, Namespace, Module, Bounded context (DDD) |
| CEX definition | One of 12 domain groupings that cluster kinds by concern |
| Instances | 12 (P01_knowledge .. P12_orchestration) |
| Superclass | `cex:Namespace` |

**Pillar instances:**

| ID | Code | Domain | Industry Analog |
|----|------|--------|----------------|
| P01 | P01_knowledge | Storage, retrieval, KCs | Knowledge Base, Document Store |
| P02 | P02_model | Agent definitions, providers | Model Registry, Agent Framework |
| P03 | P03_prompt | Templates, actions, chains | Prompt Library, LLM Gateway |
| P04 | P04_tools | External capabilities | Tool Registry, Plugin Ecosystem |
| P05 | P05_output | Production artifacts | Content Management, CMS |
| P06 | P06_schema | Data contracts | Schema Registry, API Contract |
| P07 | P07_evals | Quality, scoring, testing | Evaluation Harness, Test Suite |
| P08 | P08_architecture | System structure | Architecture Decision Records |
| P09 | P09_config | Runtime settings | Configuration Management, IaC |
| P10 | P10_memory | State, context, indexing | Memory System, State Store |
| P11 | P11_feedback | Learning, correction | Feedback Loop, RLHF pipeline |
| P12 | P12_orchestration | Workflows, dispatch | Workflow Engine, Orchestrator |

---

### Class 3: Nucleus

| Attribute | Value |
|-----------|-------|
| OWL equivalent | `owl:Class` with URI `cex:Nucleus` |
| Industry term | Agent, Microservice, Bounded Context, Department |
| CEX definition | Operational LLM agent specializing in one domain; runs 8F pipeline |
| Instances | 8 (N00_genesis .. N07_admin) |
| Superclass | `cex:Agent` |

**Nucleus instances:**

| ID | Code | Domain | Sin | Industry Analog |
|----|------|--------|-----|----------------|
| N00 | N00_genesis | Archetype | pre-sin | Template, Seed, Prototype |
| N01 | N01_intelligence | Research | Analytical Envy | Research Analyst, Data Scientist |
| N02 | N02_marketing | Marketing | Creative Lust | Content Strategist, Copywriter |
| N03 | N03_engineering | Build | Inventive Pride | Software Engineer, Builder |
| N04 | N04_knowledge | Knowledge | Knowledge Gluttony | Knowledge Engineer, Librarian |
| N05 | N05_operations | Operations | Gating Wrath | DevOps, QA Engineer |
| N06 | N06_commercial | Commercial | Strategic Greed | Sales Engineer, Revenue Strategist |
| N07 | N07_admin | Orchestration | Orchestrating Sloth | Tech Lead, Architect, PM |

---

### Class 4: Pipeline

| Attribute | Value |
|-----------|-------|
| OWL equivalent | `owl:Class` with URI `cex:Pipeline` |
| Industry term | Processing pipeline, Execution graph, Workflow |
| CEX definition | The 8F reasoning protocol (F1-F8) applied to every task by every nucleus |
| Instances | 1 canonical (8F); plus per-kind variants |
| Superclass | `cex:Process` |

**Pipeline stages as sub-properties:**

| Stage | OWL Property | Industry Term | Description |
|-------|-------------|--------------|-------------|
| F1 | cex:hasConstraint | Intent resolution, Schema binding | Resolve kind/pillar/schema |
| F2 | cex:hasIdentity | Role adoption, Persona loading | Load builder ISOs + sin lens |
| F3 | cex:hasContext | Context assembly, RAG injection | Load KCs, examples, brand, memory |
| F4 | cex:hasReasoning | Planning, Deliberation | Plan sections, approach, GDP if subjective |
| F5 | cex:hasTools | Tool use, Action execution | Execute tools, fetch references |
| F6 | cex:hasOutput | Generation, Inference | Produce artifact with frontmatter + body |
| F7 | cex:hasGovernance | Validation, Quality gate | Score, gate, retry if below threshold |
| F8 | cex:hasCollaboration | Commit, Signal, Handoff | Save, compile, commit, signal |

---

### Class 5: LLMFunction

| Attribute | Value |
|-----------|-------|
| OWL equivalent | `owl:Class` with URI `cex:LLMFunction` |
| Industry term | Cognitive function, Task type, Skill category |
| CEX definition | One of 8 cognitive functions a kind primarily exercises |
| Instances | 8 (CONSTRAIN, BECOME, INJECT, REASON, CALL, PRODUCE, GOVERN, COLLABORATE) |
| Superclass | `cex:Capability` |

---

## Properties

### Data Properties

| Property | OWL Type | Domain | Range | CEX Field | Industry Term |
|----------|----------|--------|-------|-----------|--------------|
| cex:hasQuality | owl:DatatypeProperty | Kind instance | xsd:float [0-10] | quality | Quality score, Evaluation score |
| cex:hasDensity | owl:DatatypeProperty | Kind instance | xsd:float [0-1] | density_score | Information density, Compression ratio |
| cex:hasMaxBytes | owl:DatatypeProperty | Kind class | xsd:integer | max_bytes | Size budget, Token budget |
| cex:hasPillarCode | owl:DatatypeProperty | Pillar | xsd:string | P01..P12 | Namespace code, Module ID |
| cex:hasVersion | owl:DatatypeProperty | Kind instance | xsd:string | version | Schema version, Artifact version |
| cex:hasStatus | owl:DatatypeProperty | Kind class | xsd:string | status | Lifecycle status (stable/experimental/deprecated) |
| cex:hasNamingPattern | owl:DatatypeProperty | Kind class | xsd:string | naming | File naming convention |
| cex:isCore | owl:DatatypeProperty | Kind class | xsd:boolean | core | Core/non-core designation |

---

## Relationships (Object Properties)

| Relationship | OWL Property | Domain | Range | Cardinality | Industry Term |
|-------------|-------------|--------|-------|-------------|--------------|
| belongsToPillar | cex:belongsToPillar | Kind | Pillar | many-to-one | has_module, has_namespace |
| routesToNucleus | cex:routesToNucleus | Kind | Nucleus | many-to-many | assignedTo, ownedBy |
| governedBy | cex:governedBy | Kind instance | Pipeline stage | many-to-one | executedBy, processedBy |
| producedBy | cex:producedBy | Kind instance | Nucleus | many-to-one | createdBy, authoredBy |
| requires | cex:requires | Kind class | Kind class | many-to-many | dependsOn, imports |
| coOccursWith | cex:coOccursWith | Kind class | Kind class | many-to-many | frequentlyPairedWith |
| hasBuilder | cex:hasBuilder | Kind class | Builder | one-to-one | hasFactory, hasConstructor |
| compilesWith | cex:compilesWith | Kind instance | Compiled artifact | one-to-one | compiledTo, derivedAs |

---

## Axioms

### Covering Axiom
Every Kind instance belongs to exactly one Pillar:
```
Kind subClassOf (belongsToPillar exactly 1 Pillar)
```

### Domain Routing Axiom
Every Kind instance routes to at least one Nucleus:
```
Kind subClassOf (routesToNucleus min 1 Nucleus)
```

### Quality Floor Axiom
Published Kind instances (non-null quality) must satisfy the 8.0 floor:
```
KindInstance and (hasQuality some xsd:float) -> hasQuality >= 8.0
```

### 8F Completeness Axiom
Every Kind class maps to exactly one LLMFunction:
```
Kind subClassOf (governedBy exactly 1 LLMFunction)
```

### Builder Axiom
Every Kind class has exactly one Builder agent:
```
Kind subClassOf (hasBuilder exactly 1 Builder)
```

---

## CEX-to-Industry Mapping

| CEX Term | Industry Term | Standard | Notes |
|----------|--------------|----------|-------|
| kind | artifact type | OWL Class, JSON Schema | 257 canonical types |
| pillar | domain / bounded context | DDD Bounded Context, OWL Namespace | 12 pillars |
| nucleus | agent / microservice | A2A Agent, OWL Individual | 8 nuclei |
| 8F pipeline | processing pipeline | BPMN Process, OWL Workflow | F1-F8 |
| quality | evaluation score | HELM metric, OpenAI Evals score | 0-10 scale |
| density_score | information density | TF-IDF density, compression ratio | 0-1 scale |
| frontmatter | metadata header | YAML front matter, JSON-LD header | standard CEX format |
| signal | completion event | A2A Task signal, BPMN End Event | F8 COLLABORATE |
| handoff | context transfer | A2A Message, FIPA ACL performative | inter-nucleus |
| builder | artifact factory | Factory pattern, Builder pattern (GoF) | 259 builders |
| ISO | builder component | Interface, Module, Mixin | 13 per kind |
| GDP | co-pilot protocol | Human-in-the-loop, Decision support | subjective decisions |
| sin lens | optimization bias | Objective function, Reward function | nucleus identity |
| archetype | template / prototype | OOP prototype, N00 genesis | N00 is the archetype |
| KC | knowledge card | Knowledge Base entry, Fact | typed knowledge unit |
| intent resolution | intent resolution | NLU intent, Semantic routing | F1 CONSTRAIN |

---

## Graph Summary

| Dimension | Count |
|-----------|-------|
| Classes | 5 (Kind, Pillar, Nucleus, Pipeline, LLMFunction) |
| Kind subclasses | 8 (by LLM function) |
| Data properties | 8 |
| Object properties / relationships | 8 |
| Axioms | 5 |
| Kind instances | 257 |
| Pillar instances | 12 |
| Nucleus instances | 8 |
| CEX-to-Industry mappings | 16 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n04_competitive_knowledge]] | related | 0.28 |
| [[cex_llm_vocabulary_whitepaper]] | sibling | 0.27 |
| [[p03_sp_cex_core_identity]] | downstream | 0.26 |
| [[index]] | downstream | 0.26 |
| [[spec_n07_bootstrap_context]] | related | 0.25 |
| [[n07_memory_industry_audit]] | downstream | 0.25 |
| [[taxonomy_completeness_audit]] | sibling | 0.25 |
| [[spec_cex_system_map]] | related | 0.24 |
| [[p10_entity_cex_system]] | downstream | 0.24 |
| [[p08_pat_nucleus_fractal]] | downstream | 0.23 |
