---
id: atom_31_ml_ontologies
kind: knowledge_card
pillar: P01
quality: 9.0
title: "ML Ontologies and Taxonomies"
tags: [ontology, taxonomy, nist, ml-schema, framework-atlas]
date: 2026-04-13
related:
  - bld_instruction_benchmark_suite
  - dataset-card-builder
  - p03_sp_dataset_card_builder
  - p01_gl_taxonomy
  - bld_tools_ontology
  - p01_kc_dataset_card
  - bld_collaboration_ontology
  - ontology-builder
  - eval-dataset-builder
  - kc_ontology
---

# CEX Ontology Ingestion Plan

This document outlines the comprehensive strategy for ingesting and harmonizing multiple knowledge ontologies into the CEX (Concept Exchange) system. The goal is to create a unified, structured knowledge base covering machine learning tasks, algorithms, metrics, datasets, and modern AI concepts.

## Boundary

This artifact defines the **process** for mapping external ML ontologies into CEX knowledge cards. It is **not** a technical specification for the ontologies themselves, nor a final implementation of the CEX system. It focuses solely on the **ingestion methodology**, not the ontologies' content or the CEX system's architecture.

## Related Kinds

- **schema**: Dataset metadata is mapped to `schema` for structured data definitions  
- **guardrail**: Ethical AI concepts are integrated as `guardrail` for compliance tracking  
- **workflow**: Experiment/run concepts are linked to `workflow` for reproducibility  
- **type_def**: Hyperparameter definitions are captured as `type_def` for standardization  
- **knowledge_card**: All algorithm/task/metric concepts are represented as `knowledge_card` for discoverability  

## Executive Summary

The CEX system will integrate data from **7+ authoritative sources**, including:
- **MetaAutoML** (classical ML algorithms)
- **ITO** (AI process taxonomy)
- **PapersWithCode** (method/task metadata)
- **HuggingFace** (NLP pipelines)
- **MLCommons Croissant** (dataset metadata)
- **W3C ML Schema** (foundational ontology)
- **Artificial Intelligence Ontology (AIO)** (LLM-era concepts)

The result will be a **3,000+ concept knowledge base** with:
- Hierarchical task taxonomy
- Algorithm/architecture definitions
- Evaluation metrics
- Dataset metadata schema
- Ethical AI guardrails

## Phase Plan

### Phase 1: Foundation Layer (Week 1)
**Goal**: Establish ontology backbone from W3C ML Schema

**Key Deliverables**:
- 25 foundational `knowledge_card` concepts
- Ontology alignment with CEX pillars
- Schema for future concept mapping

**Tools**:
- `rdflib` for RDF parsing
- `owlready2` for OWL processing

**Output**: `P01_knowledge/library/ml/` directory with foundational concepts

---

### Phase 2: Task Taxonomy (Weeks 1-2)
**Goal**: Build comprehensive ML task hierarchy

**Sources**:
- ITO (1,100+ AI process classes)
- PWC (3,000+ tasks)
- HuggingFace (75 pipeline tags)

**Strategy**:
- Use **Levenshtein distance + BERT embeddings** for deduplication
- Create **3-level hierarchy**:
  1. HF pipeline tags (top-level)
  2. ITO mid-level classes
  3. PWC task leaves

**Output**: ~2,000 deduplicated task `knowledge_card`s

---

### Phase 3: Algorithm & Architecture Taxonomy (Week 2)
**Goal**: Cover classical ML and deep learning

**Sources**:
- MetaAutoML (120 algorithms)
- AIO (DL architectures)
- PWC (665 methods)

**Mapping**:
- Classical ML: MetaAutoML + ML-Schema `Algorithm` class
- DL architectures: AIO Networks/Layers branches

**Output**: ~500 algorithm/architecture `knowledge_card`s

---

### Phase 4: Metrics & Evaluation (Weeks 2-3)
**Goal**: Create comprehensive evaluation library

**Sources**:
- MetaAutoML (120 metrics)
- ITO (1,995 performance properties)
- ML-Schema (EvaluationMeasure)

**Categorization**:
- Classification / Regression / Generation / Ranking
- Include **computation formulas** where available

**Output**: ~200 `scoring_rubric` concepts

---

### Phase 5: Dataset Vocabulary (Week 3)
**Goal**: Adopt MLCommons Croissant as dataset metadata standard

**Mapping**:
- `cr:Dataset` → `knowledge_card` (dataset domain)
- `cr:RecordSet` → `schema` (data structure)
- `cr:Field` → `type_def` (data type)

**Ethics Integration**:
- Import RAI vocabulary as 10 `guardrail` concepts

**Output**: Dataset metadata schema + ethical guardrails

---

### Phase 6: Modern AI Concepts (Weeks 3-4)
**Goal**: Capture LLM-era concepts from AIO

**Focus Areas**:
- Transformer variants (BERT, GPT, etc.)
- Attention mechanisms
- Fine-tuning strategies (LoRA, QLoRA)
- Prompt engineering
- AI bias types

**Output**: ~300 modern AI `knowledge_card`s

---

## Technical Implementation

### Tools & Dependencies

```python
# Core dependencies
pip install rdflib        # RDF/Turtle parsing
pip install owlready2     # OWL ontology loading
pip install mlcroissant   # Croissant JSON-LD
pip install huggingface_hub  # HF API
pip install pyld          # JSON-LD processing
pip install scikit-learn  # Deduplication
pip install transformers  # BERT embeddings
```

### Unified Ingestion Pipeline

```python
# Core dependencies
pip install rdflib        # RDF/Turtle parsing
pip install owlready2     # OWL ontology loading
pip install mlcroissant   # Croissant JSON-LD
pip install huggingface_hub  # HF API
pip install pyld          # JSON-LD processing
pip install scikit-learn  # Deduplication
pip install transformers  # BERT embeddings
```

## Ontology-to-CEX Mapping Strategy

| Ontology Concept       | CEX Kind         | Mapping Notes                          |
|------------------------|------------------|----------------------------------------|
| ML Task Definitions    | knowledge_card   | Mapped from PWC and ITO hierarchies    |
| Algorithm Specifications | knowledge_card | From MetaAutoML and AIO              |
| Evaluation Metrics     | scoring_rubric   | Derived from MetaAutoML and ITO      |
| Dataset Metadata       | schema           | Aligned with MLCommons Croissant     |
| Ethical Constraints    | guardrail        | Integrated from RAI vocabulary       |
| Hyperparameter Types   | type_def         | Extracted from ML-Schema and AIO     |
| NLP Pipeline Templates | knowledge_card   | From HuggingFace definitions         |

---

## Conclusion

This plan establishes a robust framework for integrating diverse ML knowledge sources into the CEX system. By following this structured approach, we will create a comprehensive, interoperable knowledge base that supports research, development, and ethical AI practices across the ML ecosystem.

---

## Deep Implementation: MetaAutoML Ontology

**Source**: [ML_Ontology.ttl](https://github.com/hochschule-darmstadt/MetaAutoML/blob/main/controller/managers/ontology/ML_Ontology.ttl) — MIT license, Hochschule Darmstadt  
**Paper**: [An Industry-Ready Machine Learning Ontology (MDPI Applied Sciences 2026)](https://www.mdpi.com/2076-3417/16/2/843)

### Individual Count (Exact)

| Class | Count | Notes |
|-------|-------|-------|
| `ML_task` | 48 | Classification, regression, clustering, etc. |
| `ML_approach` | 134 | Algorithms + neural network architectures |
| `Metric` | 127 | Accuracy, F1, AUC, MAE, RMSE, etc. |
| `Preprocessing_approach` | 6 | PCA, kernel approximation, scaling, etc. |
| `ML_library` | 26 | scikit-learn, PyTorch, TensorFlow, etc. |
| `AutoML_solution` | 43 | AutoSklearn, FLAML, TPOT, etc. |
| **TOTAL** | **384** | **Across 6 primary entity types** |

### Technical Stack

- Format: RDF/Turtle (`.ttl`), generated from `ML_Ontology.xlsx`
- Standards: RDF/RDFS + SPARQL + SKOS + SHACL (no OWL named individuals)
- Instance pattern: `:[resource-name] a :[Class]` (not `owl:NamedIndividual`)
- ~5,000 RDF triples total
- Query performance: <100ms for complex SPARQL, <3.5 MB memory

### SPARQL Ingestion Pattern

```sparql
PREFIX : <http://example.org/ml-ontology#>
SELECT ?task ?label WHERE {
  ?task a :ML_task ;
        rdfs:label ?label .
}
```

### CEX Mapping

| MetaAutoML Class | CEX Kind | Target Pillar |
|------------------|----------|---------------|
| `ML_task` | `knowledge_card` | P01 |
| `ML_approach` | `knowledge_card` | P01 |
| `Metric` | `scoring_rubric` | P07 |
| `Preprocessing_approach` | `knowledge_card` | P01 |
| `ML_library` | `knowledge_card` | P01 |
| `AutoML_solution` | `knowledge_card` | P01 |

---

## Deep Implementation: AIO LLM-Era Branch

**Source**: [berkeleybop/artificial-intelligence-ontology](https://github.com/berkeleybop/artificial-intelligence-ontology) — Lawrence Berkeley National Lab  
**Paper**: [Joachimiak et al. 2024, arXiv:2404.03044](https://arxiv.org/abs/2404.03044)  
**Latest release**: v2024-11-08

### Scale

- **442 classes** total
- **439 synonyms** (cross-terminology mapping)
- **513 subclass-of** relationships
- 7 bridge mappings to BFO/IAO/OBI upper ontologies

### Eight Top-Level Branches

| Branch | Domain | LLM-assisted? |
|--------|--------|---------------|
| Bias | Fairness / ethical AI types | Partially |
| Layer | Neural network layer types | YES |
| Machine Learning Task | Task taxonomy | Partially |
| Mathematical Function | Activation functions | YES |
| Model | Model architecture classes | YES |
| Network | Full network architectures | YES |
| Preprocessing | Data prep methods | YES |
| Training Strategy | Fine-tuning, LoRA, RLHF | YES |

LLM branches (Layer, Mathematical Function, Model, Network, Training Strategy) were constructed with Claude 3 Sonnet + GPT-4 + ROBOT-helper chatbot.

### LLM/Transformer Sub-Hierarchy (Model branch)

```
AIO:Model
  AIO:LanguageModel
    AIO:TransformerLanguageModel
      AIO:TransformerLLM           <- GPT-4, Claude, Llama, etc.
        AIO:InstructionTunedLLM
        AIO:RLHF_LLM
    AIO:RNN_LanguageModel
  AIO:VisionLanguageModel           <- multimodal
  AIO:DiffusionModel
```

Transformer definition in AIO: "uses the transformer architecture based on multi-head attention mechanisms allowing it to contextualize tokens within a context window."

### Fine-Tuning Concepts (Training Strategy branch)

| AIO Term | Industry Term | CEX Kind |
|----------|--------------|----------|
| `AIO:LoRATraining` | Low-Rank Adaptation | `knowledge_card` |
| `AIO:QLoRATraining` | Quantized LoRA | `knowledge_card` |
| `AIO:InstructionTuning` | Supervised Fine-Tuning | `knowledge_card` |
| `AIO:RLHF` | Reinforcement Learning from Human Feedback | `knowledge_card` |
| `AIO:PromptTuning` | Soft prompt optimization | `knowledge_card` |

### Ingestion Note

AIO is OWL-based. Load with `owlready2` or query via BioPortal SPARQL endpoint. The `aio-full.owl` release includes imports; `aio-base.owl` is standalone.

```python
from owlready2 import get_ontology
aio = get_ontology("https://github.com/berkeleybop/artificial-intelligence-ontology/releases/latest/download/aio.owl").load()
llm_classes = list(aio.TransformerLLM.subclasses())
```

---

## Deep Implementation: Papers With Code Post-Shutdown Archive

**Shutdown date**: July 24-25, 2025 (Meta sunset, no prior notice)  
**Announcement**: Julien Chaumond (HuggingFace co-founder), July 25, 2025

### Archive Access Points

| Resource | URL | Coverage |
|----------|-----|----------|
| Internet Archive snapshot | `https://web.archive.org/web/20250630093841/https://paperswithcode.com/sota` | SOTA leaderboards as of 2025-06-30 |
| GitHub data repo | `https://github.com/paperswithcode/paperswithcode-data` | Structured JSON datasets |
| HuggingFace datasets | `huggingface.co/datasets/paperswithcode/*` | Papers, code links, eval tables, methods |

### Available Dataset Files (GitHub/HuggingFace)

| File | Content | Format |
|------|---------|--------|
| papers-with-abstracts | ~300K papers with abstracts | JSON + sota-extractor |
| links-between-papers-and-code | Paper-to-repo mappings | JSON |
| evaluation-tables | Benchmark results | JSON |
| methods | Research methodology | JSON |
| datasets | Referenced datasets | JSON |

License: **CC-BY-SA 4.0** — reusable with attribution.

### Coverage Gap

| Metric | Papers With Code (pre-shutdown) | HuggingFace Trending (successor) |
|--------|--------------------------------|----------------------------------|
| SOTA tasks tracked | 3,000-5,000 | ~40 |
| Benchmark leaderboards | Full | Minimal |
| Code-paper linking | ~300K papers | Trending only |

### Active Alternatives (2025-2026)

| Platform | URL | Strength |
|----------|-----|----------|
| CodeSOTA | `codesota.com` | Fresh SOTA benchmarks, independent |
| PapersWithCodePlus | Community | Open-source PWC replacement |
| CatalyzeX | `catalyzex.com` | Code-for-paper search |
| OpenCodePapers | Community | Community maintained |
| ResearchLit | — | Search-based paper-code linking |

### CEX Ingestion Note

Use the `paperswithcode-data` GitHub repo + HuggingFace datasets for bulk offline ingestion. The `evaluation-tables` JSON is the highest-value artifact: it contains benchmark results mapping method names to scores on standard datasets. Map `method` -> `knowledge_card`, `evaluation_table` row -> `scoring_rubric`.

---

## Deep Implementation: W3C ML Schema Classes and Properties

**Namespace**: `http://www.w3.org/ns/mls#`  
**Spec**: [ml-schema.github.io/documentation](http://ml-schema.github.io/documentation/ML%20Schema.html)  
**Status**: W3C Community Group Report (not a W3C Standard)

### Full Class Inventory (25 Classes)

#### Information Entities (11)

| Class | Definition | CEX Kind |
|-------|-----------|----------|
| `mls:Algorithm` | The algorithm regardless of software implementation | `knowledge_card` |
| `mls:Data` | Entities composed of data examples at various granularity levels | `schema` |
| `mls:Dataset` | Subclass of Data; a specific collection | `knowledge_card` |
| `mls:Feature` | Subclass of Data; a column/attribute | `type_def` |
| `mls:EvaluationMeasure` | A metric to assess model performance | `scoring_rubric` |
| `mls:EvaluationProcedure` | Technique to evaluate ML models (e.g. cross-validation) | `knowledge_card` |
| `mls:EvaluationSpecification` | Combines procedures and measures | `scoring_rubric` |
| `mls:HyperParameter` | Prior parameter set before implementation execution | `type_def` |
| `mls:HyperParameterSetting` | Connection between hyperparameter and assigned value | `type_def` |
| `mls:Implementation` | Executable implementation of algorithms/workflows | `knowledge_card` |
| `mls:Model` | Generalization of training data for prediction | `knowledge_card` |

#### Quality / Characteristic Classes (5)

| Class | Definition | CEX Kind |
|-------|-----------|----------|
| `mls:DataCharacteristic` | Distinguishing quality of data (statistical, geometric) | `knowledge_card` |
| `mls:DatasetCharacteristic` | Subclass of DataCharacteristic | `knowledge_card` |
| `mls:FeatureCharacteristic` | Properties distinguishing features | `type_def` |
| `mls:ModelCharacteristic` | Distinguishing model quality (interpretability, complexity) | `knowledge_card` |
| `mls:ImplementationCharacteristic` | Qualities of executable implementations | `knowledge_card` |

#### Process Classes (4)

| Class | Definition | CEX Kind |
|-------|-----------|----------|
| `mls:Process` | Base class for procedural entities | `workflow` |
| `mls:Run` | Execution of an implementation on a machine | `workflow` |
| `mls:Experiment` | Collection of runs | `workflow` |
| `mls:Study` | Collection of runs for analysis | `knowledge_card` |

#### Remaining Classes (5)

| Class | Definition | CEX Kind |
|-------|-----------|----------|
| `mls:Task` | Formal description of a process to be completed | `knowledge_card` |
| `mls:ModelEvaluation` | Performance measure value paired with its specification | `scoring_rubric` |
| `mls:Software` | Computer programs with implementations | `knowledge_card` |
| `mls:InformationEntity` | Top-level parent for information concepts | *(abstract)* |
| `mls:Quality` | Top-level parent for characteristics | *(abstract)* |

### Object Properties (12)

| Property | Domain | Range | Semantics |
|----------|--------|-------|-----------|
| `mls:achieves` | Run | Task | Run solves a task |
| `mls:definedOn` | Task | Data / EvaluationSpecification | Task has data context |
| `mls:defines` | EvaluationSpecification | Task | inverse of definedOn |
| `mls:executes` | Run | Implementation | Run executes code |
| `mls:hasHyperParameter` | Implementation | HyperParameter | Code has params |
| `mls:hasInput` | Run | Data / HyperParameterSetting | Input data + settings |
| `mls:hasOutput` | Run | Model / ModelEvaluation | Output model + metrics |
| `mls:hasPart` | Various | Various | Part-whole |
| `mls:hasQuality` | Data/Implementation/Model | Characteristics | Quality annotation |
| `mls:implements` | Implementation | Algorithm | Code implements algo |
| `mls:realizes` | Run | Task | *(deprecated, use achieves)* |
| `mls:specifiedBy` | HyperParameterSetting / ModelEvaluation | HyperParameter / EvaluationMeasure | Specification link |

### Data Properties (1) + Annotation Properties (7)

| Property | Type | Purpose |
|----------|------|---------|
| `mls:hasValue` | Data | Literal value assignment |
| `dcterms:description` | Annotation | Description |
| `dcterms:hasVersion` | Annotation | Version string |
| `dcterms:issued` | Annotation | Issue date |
| `dcterms:modified` | Annotation | Modified date |
| `skos:note` | Annotation | Notes |
| `dcterms:publisher` | Annotation | Publisher |
| `dcterms:title` | Annotation | Title |

### Three-Layer Architecture

```
Layer 1 (Specification)   — Task, Algorithm, EvaluationMeasure, EvaluationProcedure
Layer 2 (Implementation)  — Implementation, HyperParameter, HyperParameterSetting, Software
Layer 3 (Application)     — Run, Experiment, Study, Model, ModelEvaluation
```

---

## Ontology Ingestion Priority Matrix

Ranked by: (a) data volume, (b) CEX coverage gap, (c) implementation complexity, (d) maintenance risk.

| Priority | Ontology | Volume | Complexity | Coverage Gap | First Action |
|----------|----------|--------|------------|--------------|--------------|
| **P1** | MetaAutoML | 384 individuals | Low | Algorithms + Metrics | `git clone` + `rdflib` parse |
| **P2** | W3C ML Schema | 25 classes, 12 props | Low | Foundational schema | `pip install rdflib` + fetch namespace |
| **P3** | AIO | 442 classes | Medium | LLM/DL architectures | `owlready2` + `aio-base.owl` |
| **P4** | PWC archive | ~300K papers | High | Task/benchmark intel | HuggingFace datasets API |
| **P5** | HuggingFace tasks | 75 pipeline tags | Low | NLP task taxonomy | `huggingface_hub` API |
| **P6** | ITO | 1,100+ classes | High | Process taxonomy | OWL download + parse |
| **P7** | MLCommons Croissant | JSON-LD | Medium | Dataset metadata | `pip install mlcroissant` |

### Minimum Viable Ingestion (Phase 1 only)

```python
# Estimated effort: 1 developer-day
# Output: ~600 CEX knowledge_card drafts

import rdflib

# 1. MetaAutoML (384 individuals -> knowledge_cards + scoring_rubrics)
g = rdflib.Graph()
g.parse("https://raw.githubusercontent.com/hochschule-darmstadt/MetaAutoML/main/controller/managers/ontology/ML_Ontology.ttl", format="turtle")

# 2. W3C ML Schema (25 classes -> schema backbone)
g2 = rdflib.Graph()
g2.parse("https://www.w3.org/ns/mls", format="xml")

# 3. Query tasks
tasks = list(g.subjects(rdflib.RDF.type, rdflib.URIRef("http://example.org/ml-ontology#ML_task")))
```

### Risk Register

| Risk | Ontology | Mitigation |
|------|----------|-----------|
| PWC SOTA data gap (40 vs 5K tasks) | PWC successor | Use Internet Archive + CodeSOTA |
| AIO version drift (fast-moving LLM space) | AIO | Pin to v2024-11-08, quarterly review |
| MetaAutoML XLSX -> TTL pipeline break | MetaAutoML | Cache raw TTL, parse offline |
| W3C Community Group status (not W3C Standard) | ML Schema | Treat as stable reference, not normative |
| ITO 1,100 classes -> deduplication effort | ITO | Phase 2+ only, BERT embeddings required |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_benchmark_suite]] | downstream | 0.22 |
| [[dataset-card-builder]] | related | 0.22 |
| [[p03_sp_dataset_card_builder]] | downstream | 0.21 |
| [[p01_gl_taxonomy]] | related | 0.21 |
| [[bld_tools_ontology]] | downstream | 0.21 |
| [[p01_kc_dataset_card]] | sibling | 0.21 |
| [[bld_collaboration_ontology]] | downstream | 0.20 |
| [[ontology-builder]] | related | 0.20 |
| [[eval-dataset-builder]] | downstream | 0.20 |
| [[kc_ontology]] | sibling | 0.19 |
