---
id: atom_31_ml_ontologies
kind: knowledge_card
pillar: P01
quality: null
title: "ML Ontologies and Taxonomies"
tags: [ontology, taxonomy, nist, ml-schema, framework-atlas]
date: 2026-04-13
---

# CEX Ontology Ingestion Plan

This document outlines the comprehensive strategy for ingesting and harmonizing multiple knowledge ontologies into the CEX (Concept Exchange) system. The goal is to create a unified, structured knowledge base covering machine learning tasks, algorithms, metrics, datasets, and modern AI concepts.

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
# _tools/cex_ontology_ingest.py
def fetch_source(url, format):
    """Download and cache source data"""
    pass

def parse_ontology(data, format):
    """Convert raw data to list of Concept objects"""
    pass

def deduplicate(concepts, threshold=0.85):
    """Remove duplicate concepts using embeddings"""
    pass

def map_to_cex(concept):
    """Map ontology class to CEX kind + pillar + domain"""
    pass

def generate_kc(concept, mapping):
    """Generate markdown knowledge card artifact"""
    pass

def compile_and_index(artifacts):
    """Update CEX search index"""
    pass
```

---

## Ontology-to-CEX Mapping Strategy

| Ontology Concept Type       | CEX Kind         | CEX Pillar |
|-----------------------------|------------------|------------|
| ML Task / AI Process        | knowledge_card   | P01        |
| Algorithm / Method          | knowledge_card   | P01        |
| DL Architecture             | knowledge_card   | P01        |
| Evaluation Metric           | scoring_rubric   | P07        |
| Dataset Schema              | schema           | P06        |
| Bias / Ethics               | guardrail        | P11        |
| Hyperparameter              | type_def         | P06        |
| Library / Tool              | knowledge_card   | P04        |
| Experiment / Run            | workflow         | P12        |

---

## Risk Management

### High-Risk Items
1. **PWC archive disappearance**  
   - Mitigation: Cache all JSON files locally

2. **Scale (3,000+ KCs)**  
   - Mitigation: Batch generation via `cex_batch.py`

### Medium-Risk Items
1. **Ontology version drift**  
   - Mitigation: Pin versions in `requirements.txt`

2. **Deduplication false positives**  
   - Mitigation: Manual review for >0.90 similarity

---

## Immediate Next Actions

1. **Today**:
   - Cache PWC archive: `git clone https://github.com/paperswithcode/paperswithcode-data`
   - Download MetaAutoML: `wget https://raw.githubusercontent.com/hochschule-darmstadt/MetaAutoML/main/controller/managers/ontology/ML_Ontology.ttl`
   - Fetch ITO: `git clone https://github.com/OpenBioLink/ITO`

2. **Week 1**:
   - Implement `_tools/cex_ontology_ingest.py`
   - Complete Phase 1 (W3C ML Schema)
   - Begin Phase 2 (Task taxonomy)

3. **Week 2**:
   - Complete Phase 3 (Algorithms)
   - Begin Phase 4 (Metrics)

4. **Week 3**:
   - Complete Phase 5 (Datasets)
   - Begin Phase 6 (Modern AI concepts)

---

## Source Repositories

```yaml
sources:
  - name: "MetaAutoML"
    url: "https://github.com/hochschule-darmstadt/MetaAutoML"
    description: "Classical ML algorithm ontology"

  - name: "ITO"
    url: "https://github.com/OpenBioLink/ITO"
    description: "AI process taxonomy"

  - name: "PapersWithCode"
    url: "https://github.com/paperswithcode/paperswithcode-data"
    description: "ML method/task metadata"

  - name: "HuggingFace"
    url: "https://github.com/huggingface"
    description: "NLP pipeline definitions"

  - name: "MLCommons Croissant"
    url: "https://github.com/mlcommons/croissant"
    description: "Dataset metadata standard"

  - name: "W3C ML Schema"
    url: "https://www.w3.org/TR/2021/REC-ml-schema-20211214/"
    description: "Foundational ML ontology"

  - name: "Artificial Intelligence Ontology (AIO)"
    url: "https://github.com/ArtificialIntelligenceOntology/AIO"
    description: "LLM-era concepts"
```

---

## Conclusion

This plan establishes a robust framework for integrating diverse ML knowledge sources into the CEX system. By following this structured approach, we will create a comprehensive, interoperable knowledge base that supports research, development, and ethical AI practices across the ML ecosystem.