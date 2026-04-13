---
id: atom_31_ml_ontologies
kind: knowledge_card
pillar: P01
domain: ml_ontologies
title: "Machine-Readable ML Ontologies and Taxonomies -- Deep Survey"
version: 1.0.0
quality: 8.8
tags: [ontology, taxonomy, RDF, OWL, JSON-LD, ML, AI, ingestion]
created: 2026-04-13
sources: 6
---

# Machine-Readable ML Ontologies and Taxonomies

## Executive Summary

Six machine-readable sources cover the AI/ML concept space. Three are formal
ontologies (MetaAutoML ML Ontology, ITO, AIO), two are platform taxonomies
(Papers With Code, Hugging Face), and one is a dataset metadata vocabulary
(MLCommons Croissant). A seventh source (W3C ML Schema) provides a lightweight
upper ontology bridging them. Together they offer ~3,000+ distinct ML concepts
in parseable formats (RDF/Turtle, OWL, JSON-LD, JSON). No single source is
complete; each has blind spots the others fill.

---

## 1. MetaAutoML ML Ontology (Hochschule Darmstadt)

| Attribute | Value |
|-----------|-------|
| Source | https://github.com/hochschule-darmstadt/MetaAutoML |
| File | `controller/managers/ontology/ML_Ontology.ttl` |
| Format | RDF/Turtle (SKOS + SHACL) |
| Size | ~700 individuals, ~5,000 triples |
| License | MIT |
| Last update | Active (Jan 2026 paper confirms continued development) |
| Paper | "An Industry-Ready Machine Learning Ontology" (MDPI Applied Sciences, 2026) |

### Top-Level Classes and Instance Counts

| Class | ~Instances | Examples |
|-------|-----------|----------|
| ML_area | 3 | supervised, unsupervised, reinforcement |
| ML_task | 40 | classification, regression, clustering, object detection |
| ML_approach | 120 | random forest, SVM, neural network, gradient boosting |
| Preprocessing_approach | 10 | PCA, kernel approximation, normalization |
| Metric | 120 | accuracy, F1, MSE, AUC-ROC |
| ML_library | 30 | scikit-learn, TensorFlow, PyTorch, XGBoost |
| AutoML_solution | 30 | Auto-sklearn, TPOT, Auto-PyTorch, H2O |
| Configuration_item | 240 | ensemble size, metric selection, approach config |
| Datatype | ~100 | tabular, image, text, time series, audio |

### Strengths

- Directly queryable via SPARQL (query response <100ms, memory <3.5MB)
- Production-proven in MetaAutoML system (AutoML pipeline recommendation)
- Covers the full ML pipeline: data types -> tasks -> algorithms -> libraries -> configs -> metrics
- MIT license allows unrestricted commercial use

### Gaps

- No coverage of deep learning architectures (layers, attention mechanisms)
- No LLM-specific concepts (transformers, fine-tuning, RLHF, prompting)
- No ethical/bias taxonomy
- Limited to classical ML pipeline concepts

### Ingestion Method

```
1. Download: curl -O https://raw.githubusercontent.com/hochschule-darmstadt/MetaAutoML/main/controller/managers/ontology/ML_Ontology.ttl
2. Parse: rdflib (Python) -- load_turtle() -> iterate triples
3. Extract: SPARQL query for all skos:Concept / rdf:type instances
4. Map: ML_task -> CEX kind:knowledge_card (domain=ml_task)
         ML_approach -> CEX kind:knowledge_card (domain=ml_algorithm)
         Metric -> CEX kind:scoring_rubric (domain=ml_metric)
```

---

## 2. Intelligence Task Ontology (ITO)

| Attribute | Value |
|-----------|-------|
| Source | https://github.com/OpenBioLink/ITO |
| Format | OWL (compressed: ITO.owl.zip) + JSON exports |
| Size | 1,100 classes, 1,995 properties, 685,560 edges |
| License | CC-BY-SA 3.0 AT |
| Last update | v1.01 (May 2022) -- NOT actively maintained |
| Paper | "A curated, ontology-based, large-scale knowledge graph of artificial intelligence tasks and benchmarks" (Nature Scientific Data, 2022) |
| SPARQL | No endpoint; use Blazegraph locally |

### What It Covers

- AI tasks hierarchically organized (derived from Papers With Code top-level taxonomy)
- Benchmark results (SOTA scores per task per dataset)
- Performance metrics with values
- Research papers linked to tasks
- Deep inheritance hierarchy (avg depth 1.73)

### Available Files

| File | Content |
|------|---------|
| `ITO.owl.zip` | Full ontology with all benchmark data |
| `ai-process.json` | Curated AI task hierarchy (lightweight) |
| `performance-measure.json` | Performance metrics hierarchy |

### Strengths

- Deepest task taxonomy available (1,100 classes)
- Benchmark results embedded (not just definitions)
- OWL reasoning enables inference over task relationships
- Nature-published, peer-reviewed

### Gaps

- Frozen at May 2022 -- no LLM-era tasks (text-to-image, RLHF, chain-of-thought)
- No algorithm/model architecture taxonomy (only tasks + metrics)
- No dataset metadata vocabulary
- Heavy OWL file; JSON exports lose benchmark data

### Ingestion Method

```
1. Download: curl -LO https://github.com/OpenBioLink/ITO/raw/main/ITO.owl.zip
   + curl -O https://github.com/OpenBioLink/ITO/raw/main/ai-process.json
   + curl -O https://github.com/OpenBioLink/ITO/raw/main/performance-measure.json
2. Parse OWL: owlready2 (Python) -- load ITO.owl -> iterate classes
   Parse JSON: json.load() for lightweight hierarchies
3. Extract: owl:Class hierarchy -> flatten to {id, label, parent, depth}
4. Map: AI process classes -> CEX kind:knowledge_card (domain=ml_task)
         Performance measures -> CEX kind:scoring_rubric
```

---

## 3. Papers With Code (PWC) -- ARCHIVED

| Attribute | Value |
|-----------|-------|
| Source | https://github.com/paperswithcode/paperswithcode-data |
| Format | JSON (daily-regenerated snapshots, now frozen) |
| Size | ~56K papers, ~3K tasks, ~16 areas, ~9,327 benchmarks, 665+ methods |
| License | CC-BY-SA 4.0 |
| Status | **SHUT DOWN July 25, 2025** by Meta. Domain redirects to Hugging Face. |
| API | `paperswithcode-client` Python package (v0.3.1) -- **defunct** |
| Archive | GitHub repo still has last data snapshots |

### What Was Covered

| Entity | Count | Description |
|--------|-------|-------------|
| Papers | ~56K | With abstracts and code links |
| Tasks | ~3K | Hierarchical (16 top-level areas) |
| Methods | ~665 | Algorithm implementations |
| Datasets | thousands | Linked to benchmarks |
| Evaluation tables | ~9,327 | SOTA leaderboards |

### Top-Level Areas (16)

Computer Vision (665 methods), NLP (119), Graphs (104), Reinforcement Learning (88),
Sequential (53), Audio (35), Adversarial (28), Robots (20), Music (18), Speech (16),
Computer Code (14), Reasoning (14), Knowledge Base (12), Playing Games (10), Time Series (8), Medical (6).

### Data Files Available (frozen)

| File | Format | Content |
|------|--------|---------|
| `papers-with-abstracts.json.gz` | JSON | All papers |
| `links-between-papers-and-code.json.gz` | JSON | Paper-to-repo links |
| `evaluation-tables.json.gz` | JSON | SOTA benchmarks |
| `methods.json.gz` | JSON | ML methods |
| `datasets.json.gz` | JSON | Dataset metadata |

### Strengths

- Largest curated ML task taxonomy (3K tasks)
- Benchmark data with actual SOTA scores
- Well-structured JSON, easy to parse
- Community-curated over many years

### Gaps

- **DEAD** -- no updates since July 2025
- API defunct; only static archive remains
- Methods taxonomy is shallow (665 entries, no architecture details)
- No formal ontology (just JSON, no OWL/RDF reasoning)

### Alternatives Post-Shutdown

| Alternative | URL | Status |
|-------------|-----|--------|
| SOTAPapers | sotapapers.com | Community rebuild from PWC data |
| ScholarWiki | scholarwiki.ai | Partial PWC clone |
| HF Trending | huggingface.co/papers | Paper discovery only, no benchmarks |
| CodeSOTA | codesota.com | Independent benchmark tracking |

### Ingestion Method

```
1. Download: from HF datasets hub (paperswithcode/paperswithcode-data)
   or direct JSON from GitHub releases
2. Parse: json.load() each .json.gz file
3. Extract: tasks -> hierarchical tree (area -> task -> subtask)
            methods -> flat list with paper links
            evaluations -> task x dataset x metric x score
4. Map: PWC tasks -> CEX kind:knowledge_card (domain=ml_task)
         PWC methods -> CEX kind:knowledge_card (domain=ml_method)
         PWC evaluations -> CEX kind:benchmark
```

---

## 4. Hugging Face Task Taxonomy

| Attribute | Value |
|-----------|-------|
| Source | https://github.com/huggingface/huggingface.js/blob/main/packages/tasks/src/pipelines.ts |
| Docs | https://huggingface.co/docs/hub/models-tasks |
| Format | TypeScript source (parseable) + API queryable |
| Size | ~75 pipeline_tag types across 7 categories |
| License | Apache 2.0 (huggingface.js repo) |
| Status | **ACTIVE** -- maintained, new tasks added regularly |

### Complete Task List by Category

**NLP (15+)**
text-classification, token-classification, table-question-answering,
question-answering, zero-shot-classification, translation, summarization,
feature-extraction, text-generation, fill-mask, sentence-similarity,
table-to-text, multiple-choice, text-ranking, text-retrieval

**Audio (6)**
text-to-speech, text-to-audio, automatic-speech-recognition,
audio-to-audio, audio-classification, voice-activity-detection

**Computer Vision (18)**
depth-estimation, image-classification, object-detection,
image-segmentation, text-to-image, image-to-text, image-to-image,
image-to-video, unconditional-image-generation, video-classification,
zero-shot-image-classification, mask-generation, zero-shot-object-detection,
text-to-3d, image-to-3d, image-feature-extraction, keypoint-detection,
video-to-video

**Multimodal (9)**
audio-text-to-text, image-text-to-text, image-text-to-image,
image-text-to-video, visual-question-answering, document-question-answering,
video-text-to-text, visual-document-retrieval, any-to-any

**Tabular (3)**
tabular-classification, tabular-regression, time-series-forecasting

**Reinforcement Learning (2)**
reinforcement-learning, robotics

**Other (2)**
graph-ml, other

### Strengths

- De facto industry standard for model discovery (500K+ models tagged)
- Actively maintained; new modalities added (3D, video, any-to-any)
- Queryable via HF Hub API: `huggingface_hub.list_models(pipeline_tag="text-generation")`
- Coarse-grained by design -- stable, not prone to taxonomy bloat

### Gaps

- Only ~75 tasks -- deliberately coarse (no subtasks like "named entity recognition on biomedical text")
- No algorithm/architecture taxonomy (no "transformer", "CNN", "diffusion model")
- No metrics or benchmark data
- No formal ontology (TypeScript enum, not RDF/OWL)

### Ingestion Method

```
1. API: pip install huggingface_hub
   from huggingface_hub import HfApi
   api = HfApi()
   # Get all unique pipeline tags
   tags = api.get_model_tags()  # includes pipeline_tag list
2. Alternate: parse pipelines.ts from huggingface.js repo
3. Map: HF pipeline_tag -> CEX kind:knowledge_card (domain=ml_task)
         Each tag also maps to input/output schema -> CEX kind:input_schema
```

---

## 5. MLCommons Croissant

| Attribute | Value |
|-----------|-------|
| Source | https://github.com/mlcommons/croissant |
| Spec | https://docs.mlcommons.org/croissant/docs/croissant-spec.html |
| Format | JSON-LD (extends schema.org) |
| Namespace | `http://mlcommons.org/croissant/` (prefix: `cr`) |
| Version | 1.0 (March 2024) |
| License | Apache 2.0 |
| Status | **ACTIVE** -- adopted by HF, Google Dataset Search, Kaggle |

### Vocabulary Classes

| Class | Purpose |
|-------|---------|
| Dataset (schema.org) | Root entity, extended with ML properties |
| cr:FileObject | Individual files in a dataset |
| cr:FileSet | Homogeneous file collections |
| cr:RecordSet | Structured data records |
| cr:Field | Individual data elements |
| cr:DataSource | Extraction + transformation spec |

### ML-Specific Extensions

| Term | Type | Description |
|------|------|-------------|
| cr:Split | Property | train/validation/test divisions |
| cr:Label | Property | Annotation labels |
| cr:BoundingBox | Class | Spatial annotations |
| cr:SegmentationMask | Class | Pixel-level annotations |
| cr:isLiveDataset | Property | Dataset update frequency |
| cr:citeAs | Property | Citation format |

### RAI (Responsible AI) Extension

Separate vocabulary at `http://mlcommons.org/croissant/RAI/1.0` covering:
data lifecycle, labeling practices, participatory design, AI safety,
fairness evaluation, traceability, regulatory compliance.

### Strengths

- Industry standard for dataset metadata (HF, Google, Kaggle all support it)
- JSON-LD = machine-readable + human-readable
- Bridges schema.org (web discovery) and ML (training pipelines)
- Python library: `pip install mlcroissant`

### Gaps

- Dataset metadata ONLY -- no tasks, algorithms, models, or metrics
- Small vocabulary (~15 classes/properties)
- No task taxonomy or benchmark coverage
- RAI extension is separate and still maturing

### Ingestion Method

```
1. Install: pip install mlcroissant
2. Parse any Croissant JSON-LD:
   import mlcroissant as mlc
   dataset = mlc.Dataset("path/to/croissant.json")
   records = dataset.records("record_set_name")
3. For vocabulary itself:
   Fetch JSON-LD context from namespace URL
   Parse with json-ld library (pyld)
4. Map: Croissant Dataset -> CEX kind:knowledge_card (domain=dataset)
         Croissant RecordSet -> CEX kind:schema (domain=data_schema)
         Croissant RAI terms -> CEX kind:guardrail
```

---

## 6. W3C ML Schema (mls)

| Attribute | Value |
|-----------|-------|
| Source | https://www.w3.org/ns/mls |
| Spec | http://ml-schema.github.io/documentation/ML%20Schema.html |
| Format | RDF/Turtle (OWL-compatible) |
| Namespace | `http://www.w3.org/ns/mls#` |
| Size | 25 classes, 13 properties |
| License | W3C Community Group (open) |
| Status | **CLOSED** (W3C group closed Dec 2023). Spec is stable but unmaintained. |
| Paper | "ML-Schema: Exposing the Semantics of ML with Schemas and Ontologies" (2018) |

### All 25 Classes

| Class | Description |
|-------|-------------|
| Algorithm | Abstract algorithm definition |
| Data | Base data entity |
| Dataset | Subclass of Data |
| Feature | Subclass of Data |
| DataCharacteristic | Statistical measures of data |
| DatasetCharacteristic | Dataset-level characteristics |
| FeatureCharacteristic | Feature-level characteristics |
| EvaluationMeasure | Metrics (accuracy, F1, etc.) |
| EvaluationProcedure | Cross-validation, holdout, etc. |
| EvaluationSpecification | Measure + procedure combined |
| Experiment | Collection of runs |
| Study | Collection of experiments |
| HyperParameter | Prior parameter of an implementation |
| HyperParameterSetting | Parameter + value binding |
| Implementation | Executable ML algorithm |
| ImplementationCharacteristic | Implementation qualities |
| InformationEntity | Base class |
| Model | Trained model artifact |
| ModelCharacteristic | Model qualities |
| ModelEvaluation | Evaluation results |
| Process | Base process class |
| Quality | Base quality class |
| Run | Single execution of an implementation |
| Software | Implemented programs/scripts |
| Task | Formal process description (inputs/outputs) |

### Key Properties (13)

achieves, definedOn, defines, executes, hasHyperParameter, hasInput,
hasOutput, hasPart, hasQuality, hasValue, implements, realizes, specifiedBy

### Strengths

- Upper ontology for ML experiment tracking (OpenML, EXPO compatible)
- W3C-backed standard namespace
- Clean separation: Algorithm vs Implementation vs Model vs Run
- Small, stable, well-defined -- good as a backbone

### Gaps

- Only 25 classes -- too abstract for direct use
- No specific algorithms, tasks, or metrics defined (just the schema)
- Unmaintained since Dec 2023
- No LLM, deep learning, or modern ML concepts

### Ingestion Method

```
1. Download: curl -O https://raw.githubusercontent.com/ML-Schema/core/master/MLSchema.ttl
2. Parse: rdflib -> load_turtle()
3. Use as: upper ontology backbone for CEX's ML taxonomy
   Map mls:Algorithm -> parent class for MetaAutoML ML_approach instances
   Map mls:Task -> parent class for ITO/PWC task hierarchies
   Map mls:Model -> parent class for HF model cards
```

---

## 7. Artificial Intelligence Ontology (AIO) -- Bonus Source

| Attribute | Value |
|-----------|-------|
| Source | https://github.com/berkeleybop/artificial-intelligence-ontology |
| BioPortal | https://bioportal.bioontology.org/ontologies/AIO |
| Format | OWL, OBO, JSON |
| Branches | 6: Networks, Layers, Functions, LLMs, Preprocessing, Bias |
| License | CC-BY 4.0 |
| Last update | v2024-11-08 |
| Paper | "The Artificial Intelligence Ontology: LLM-Assisted Construction of AI Concept Hierarchies" (Applied Ontology, 2024) |

### Unique Value

AIO is the ONLY ontology that covers:
- Deep learning architectures (layers, attention, transformers)
- LLM-specific concepts (fine-tuning, prompting, RLHF)
- Bias and ethical AI taxonomy
- Built with LLM assistance (Claude 3 Sonnet + GPT-4)

### Strengths

- Modern (2024) -- includes LLM-era concepts no other ontology has
- OBO Foundry principles (formal definitions, upper-level alignment)
- Multiple serializations (OWL for reasoning, OBO for bio-tools, JSON for web)
- Actively maintained (8 releases)

### Gaps

- No benchmark data or SOTA scores
- No dataset metadata
- Focused on architecture/methodology, not tasks or metrics
- Relatively new, less battle-tested than ITO or ML Ontology

### Ingestion Method

```
1. Download: curl -LO https://raw.githubusercontent.com/berkeleybop/artificial-intelligence-ontology/main/aio.json
   (or aio.owl for full OWL)
2. Parse JSON: json.load() -> iterate classes
   Parse OWL: owlready2 -> load aio.owl
3. Map: AIO Network classes -> CEX kind:knowledge_card (domain=dl_architecture)
         AIO Layer classes -> CEX kind:knowledge_card (domain=dl_layer)
         AIO Bias classes -> CEX kind:guardrail (domain=ai_bias)
```

---

## Coverage Matrix

| Concept Domain | MetaAutoML | ITO | PWC | HF | Croissant | ML-Schema | AIO |
|---------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ML Tasks | ++ | +++ | +++ | ++ | - | + | + |
| Algorithms/Methods | +++ | - | ++ | - | - | + | + |
| DL Architectures | - | - | + | - | - | - | +++ |
| LLM Concepts | - | - | - | + | - | - | +++ |
| Metrics/Evaluation | +++ | ++ | +++ | - | - | ++ | - |
| Datasets | + | + | ++ | + | +++ | ++ | - |
| Libraries/Tools | +++ | - | + | + | - | + | - |
| Experiment Tracking | - | - | - | - | - | +++ | - |
| Ethical AI/Bias | - | - | - | - | + | - | +++ |
| Hyperparameters | +++ | - | - | - | - | +++ | - |
| Preprocessing | ++ | - | - | - | + | - | ++ |
| AutoML | +++ | - | - | - | - | - | - |

Legend: `+++` = deep coverage, `++` = good, `+` = partial, `-` = absent

---

## Ingestion Plan for CEX

### Phase 1: Foundation Layer (Week 1)

**Goal**: Establish upper ontology backbone from W3C ML Schema

```
Source: W3C ML Schema (25 classes)
Action: Download MLSchema.ttl
        Parse with rdflib
        Create CEX kind:knowledge_card for each class
        These become PARENT concepts for all other sources
Output: 25 foundational KCs in P01_knowledge/library/ml/
```

### Phase 2: Task Taxonomy (Week 1-2)

**Goal**: Build comprehensive ML task hierarchy

```
Source 1: ITO ai-process.json (1,100 task classes)
Source 2: PWC tasks from archived JSON (~3,000 tasks)
Source 3: HF pipeline_tags (75 coarse tasks)
Action: Parse all three sources
        Merge: HF tags as top-level categories
               ITO classes as mid-level taxonomy
               PWC tasks as leaf nodes
        Deduplicate using label similarity (Levenshtein + embedding)
        Map each unique task to CEX kind:knowledge_card
Output: ~2,000 deduplicated task KCs with hierarchy
```

### Phase 3: Algorithm and Architecture Taxonomy (Week 2)

**Goal**: Cover both classical ML and deep learning

```
Source 1: MetaAutoML ML_approach instances (120 algorithms)
Source 2: AIO Network + Layer branches (architecture concepts)
Source 3: PWC methods (665 methods)
Action: MetaAutoML for classical ML (RF, SVM, etc.)
        AIO for deep learning (transformers, attention, CNN architectures)
        PWC methods for additional coverage
        Merge with ML-Schema Algorithm as parent class
Output: ~500 algorithm/architecture KCs
```

### Phase 4: Metrics and Evaluation (Week 2-3)

**Goal**: Comprehensive evaluation metric library

```
Source 1: MetaAutoML Metric instances (120 metrics)
Source 2: ITO performance-measure.json (1,995 properties)
Source 3: ML-Schema EvaluationMeasure/Procedure classes
Action: Parse metrics from all sources
        Categorize: classification / regression / generation / ranking
        Include computation formulas where available
Output: ~200 metric KCs mapped to CEX kind:scoring_rubric
```

### Phase 5: Dataset Vocabulary (Week 3)

**Goal**: Dataset metadata standard for CEX

```
Source: MLCommons Croissant vocabulary
Action: Adopt Croissant JSON-LD as CEX dataset metadata format
        Map Croissant classes to CEX kinds:
          cr:Dataset -> kind:knowledge_card (domain=dataset)
          cr:RecordSet -> kind:schema
          cr:Field -> kind:type_def
        Import RAI vocabulary for guardrail kinds
Output: Dataset metadata schema + 10 guardrail KCs from RAI vocab
```

### Phase 6: Modern AI Concepts (Week 3-4)

**Goal**: LLM-era concepts not in older ontologies

```
Source: AIO (Networks, Layers, Functions, LLMs, Bias branches)
Action: Parse aio.json for all classes
        Focus on unique AIO concepts:
          - Transformer variants
          - Attention mechanisms
          - Fine-tuning strategies (LoRA, QLoRA, RLHF)
          - Prompt engineering concepts
          - AI bias types
Output: ~300 modern AI KCs filling the gap no other source covers
```

### Technical Stack for Ingestion

```python
# Dependencies
pip install rdflib        # RDF/Turtle + SPARQL
pip install owlready2     # OWL ontology loading
pip install mlcroissant   # Croissant JSON-LD
pip install huggingface_hub  # HF API
pip install pyld          # JSON-LD processing

# Unified ingestion pipeline
# _tools/cex_ontology_ingest.py (to be built)
#
# 1. fetch_source(url, format) -> raw data
# 2. parse_ontology(data, format) -> list[Concept]
# 3. deduplicate(concepts, threshold=0.85) -> list[Concept]
# 4. map_to_cex(concept) -> kind + pillar + domain
# 5. generate_kc(concept, mapping) -> markdown artifact
# 6. compile_and_index(artifacts) -> updated search index
```

### Mapping Strategy: Ontology Class -> CEX Kind

| Ontology Concept Type | CEX Kind | CEX Pillar |
|----------------------|----------|------------|
| ML Task / AI Process | knowledge_card | P01 |
| Algorithm / Method | knowledge_card | P01 |
| DL Architecture | knowledge_card | P01 |
| Evaluation Metric | scoring_rubric | P07 |
| Dataset Schema | schema | P06 |
| Bias / Ethics | guardrail | P11 |
| Hyperparameter | type_def | P06 |
| Library / Tool | knowledge_card | P04 |
| Experiment / Run | workflow | P12 |

---

## Risk Assessment

| Risk | Severity | Mitigation |
|------|----------|------------|
| PWC archive goes offline | HIGH | Download and cache all JSON files NOW |
| ITO frozen at 2022 | MEDIUM | Supplement with AIO + HF for modern tasks |
| Ontology version drift | LOW | Pin versions, track upstream releases |
| Deduplication false positives | MEDIUM | Manual review of merged concepts >0.90 similarity |
| Scale (3,000+ KCs to generate) | HIGH | Batch generation via cex_batch.py, phased rollout |
| Format incompatibility | LOW | rdflib + owlready2 handle all formats |

---

## Immediate Next Actions

1. **TODAY**: Download and cache PWC archive (at risk of disappearing)
2. **TODAY**: Download MetaAutoML ML_Ontology.ttl + ITO JSON exports + AIO aio.json
3. **WEEK 1**: Build `_tools/cex_ontology_ingest.py` parser
4. **WEEK 1**: Phase 1 (ML Schema backbone) + Phase 2 (task taxonomy)
5. **WEEK 2**: Phase 3 (algorithms) + Phase 4 (metrics)
6. **WEEK 3**: Phase 5 (Croissant) + Phase 6 (AIO modern concepts)

---

## Source URLs for Programmatic Download

```yaml
metaautoml:
  ttl: https://raw.githubusercontent.com/hochschule-darmstadt/MetaAutoML/main/controller/managers/ontology/ML_Ontology.ttl
  format: turtle
  parser: rdflib

ito:
  owl: https://github.com/OpenBioLink/ITO/raw/main/ITO.owl.zip
  tasks_json: https://github.com/OpenBioLink/ITO/raw/main/ai-process.json
  metrics_json: https://github.com/OpenBioLink/ITO/raw/main/performance-measure.json
  format: owl+json
  parser: owlready2 + json

pwc_archive:
  repo: https://github.com/paperswithcode/paperswithcode-data
  datasets_hub: https://huggingface.co/datasets/paperswithcode
  format: json.gz
  parser: json

huggingface:
  pipelines_ts: https://raw.githubusercontent.com/huggingface/huggingface.js/main/packages/tasks/src/pipelines.ts
  api: huggingface_hub.HfApi().get_model_tags()
  format: typescript + api
  parser: regex + huggingface_hub

croissant:
  spec: https://docs.mlcommons.org/croissant/docs/croissant-spec.html
  context: http://mlcommons.org/croissant/1.0
  python: mlcroissant
  format: json-ld
  parser: mlcroissant + pyld

ml_schema:
  ttl: https://raw.githubusercontent.com/ML-Schema/core/master/MLSchema.ttl
  namespace: http://www.w3.org/ns/mls
  format: turtle
  parser: rdflib

aio:
  json: https://raw.githubusercontent.com/berkeleybop/artificial-intelligence-ontology/main/aio.json
  owl: https://raw.githubusercontent.com/berkeleybop/artificial-intelligence-ontology/main/aio.owl
  format: json+owl
  parser: json + owlready2
```
