---
kind: knowledge_card
id: bld_knowledge_card_eval_dataset
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for eval_dataset production — curated test case collection specification
sources: Braintrust docs, LangSmith docs, DeepEval docs, HuggingFace datasets, academic ML eval practices
---

# Domain Knowledge: eval_dataset
## Executive Summary
Eval datasets are structured collections of test cases used to measure LLM behavior systematically. Each case has an input, an expected output (ground truth), and optional metadata. Datasets declare their schema, size, and splits upfront. They are COLLECTIONS — not single cases (golden_test), not performance benchmarks (benchmark), and not evaluation rubrics (scoring_rubric).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P07 (Evals) |
| llm_function | GOVERN |
| Minimum schema | input + expected_output |
| Splits | train / test / val (must sum to 1.0) |
| Size unit | integer count of test cases |
| Version | semver — schema changes = minor bump, data changes = patch |
| Machine format | yaml |
## Framework Patterns
### Braintrust Dataset
```python
from braintrust import Braintrust
project = Braintrust().projects.create(name="my-project")
dataset = project.datasets.create(name="p07_ds_my_dataset")
dataset.insert({"input": "...", "expected": "...", "metadata": {}})
```
- Uses `expected` (not `expected_output`) as the ground truth field
- Supports `metadata` dict for arbitrary case-level annotations
- Dataset versioning via insert/fetch cycles with pinned experiment IDs

### LangSmith Dataset
```python
from langsmith import Client
client = Client()
dataset = client.create_dataset("p07_ds_my_dataset")
client.create_example(inputs={"query": "..."}, outputs={"answer": "..."}, dataset_id=dataset.id)
```
- Uses `inputs` dict and `outputs` dict (nested, not flat)
- Supports `source_run_id` for tracing case origin
- Dataset sharing via workspace permissions

### DeepEval EvaluationDataset
```python
from deepeval.dataset import EvaluationDataset, Golden
golden = Golden(input="...", actual_output="...", expected_output="...", context=[])
dataset = EvaluationDataset(goldens=[golden])
dataset.push(alias="p07_ds_my_dataset")
```
- Uses `Golden` as the test case unit (confusingly named — not the same as CEX golden_test)
- Requires `actual_output` field (populated at eval time, not at dataset creation)
- `context` list for RAG-specific evaluations

### HuggingFace datasets
```python
from datasets import Dataset
data = {"input": [...], "expected_output": [...], "metadata": [...]}
ds = Dataset.from_dict(data)
ds.push_to_hub("org/p07_ds_my_dataset")
```
- Columnar format — each field is a list, not per-row dict
- Supports `train`/`test`/`validation` splits via `DatasetDict`
- Arrow-backed for large-scale datasets (millions of cases)

## Split Strategies
| Strategy | train | test | val | When to use |
|----------|-------|------|-----|-------------|
| Eval-only | 0.0 | 1.0 | 0.0 | Pure evaluation, no training use |
| Standard ML | 0.7 | 0.2 | 0.1 | Training + evaluation |
| Heavy eval | 0.0 | 0.8 | 0.2 | Evaluation focus with held-out validation |
| Balanced | 0.6 | 0.2 | 0.2 | Equal emphasis on val and test |

## Schema Field Types
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| input | string or dict | YES | The prompt or query sent to the LLM |
| expected_output | string or list | YES | Ground truth answer or reference |
| metadata | dict | REC | Tags, difficulty, category, source_id |
| context | list[string] | OPT | Retrieved chunks for RAG evals |
| tags | list[string] | OPT | Case-level labels for filtering |
| difficulty | enum | OPT | easy, medium, hard |
| source_id | string | OPT | Traceability to origin case |

## Versioning Strategy
- `1.0.0` → initial release
- `1.1.0` → new schema field added (backward-compatible)
- `2.0.0` → breaking schema change (field renamed or removed)
- `1.0.1` → data correction (same schema, corrected cases)
Rule: never reuse a dataset ID for a different schema. Bump minor version for additive changes.

## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Missing expected_output | Cannot compute automated metrics (BLEU, exact match, LLM-as-judge) |
| Splits that do not sum to 1.0 | Reproducibility breaks; train/test overlap or gap |
| No schema declaration | Consumers cannot load data without reading source code |
| Actual data rows in artifact body | Artifact bloats; data belongs in registry, not spec |
| Confusing dataset with benchmark | Benchmark measures performance; dataset is the input collection |
| Single case called a "dataset" | Single exemplary case is golden_test (P07), not eval_dataset |
| No versioning strategy | Schema drift causes silent downstream failures |

## Application
1. Define purpose: what LLM behavior does this dataset evaluate?
2. Design schema: input fields, ground truth field, metadata fields
3. Declare splits: use eval-only (test: 1.0) unless training use is confirmed
4. Specify size: how many cases now, what is the growth target
5. Choose framework: Braintrust (experiment tracking), LangSmith (trace-linked), DeepEval (metric suites), HuggingFace (large scale)
6. Set versioning: semver with schema-change rules
7. Validate: schema_fields has input + expected_output, splits sum to 1.0, quality: null

## References
- Braintrust: braintrustdata.com/docs/guides/datasets
- LangSmith: docs.smith.langchain.com/evaluation/datasets
- DeepEval: docs.confident-ai.com/docs/evaluation-datasets
- HuggingFace: huggingface.co/docs/datasets
