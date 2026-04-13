---
id: atom_31_ml_ontologies
kind: knowledge_card
pillar: P01
quality: 9.0
title: "ML Ontologies and Taxonomies"
tags: [ontology, taxonomy, nist, ml-schema, framework-atlas]
date: 2026-04-13
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