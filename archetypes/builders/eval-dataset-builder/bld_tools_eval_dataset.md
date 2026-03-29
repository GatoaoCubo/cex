---
kind: tools
id: bld_tools_eval_dataset
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for eval_dataset production
---

# Tools: eval-dataset-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing eval_dataset artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |

## Framework SDKs
| SDK | Install | Primary Use |
|-----|---------|-------------|
| braintrust | `pip install braintrust` | Dataset CRUD, experiment linking |
| langsmith | `pip install langsmith` | Dataset + trace-linked evaluation |
| deepeval | `pip install deepeval` | EvaluationDataset with metric suites |
| datasets (HuggingFace) | `pip install datasets` | Large-scale columnar datasets, Hub push |

## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P07_evals/_schema.yaml | Field definitions, eval_dataset kind |
| CEX Examples | P07_evals/examples/ | Real eval_dataset artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P07_eval_dataset |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |

## Framework Loading Patterns
### Braintrust
```python
import braintrust
dataset = braintrust.load_dataset("project-name", "dataset-name")
for case in dataset:
    result = my_model(case["input"])
    # compare to case["expected"]
```

### LangSmith
```python
from langsmith import Client
client = Client()
examples = list(client.list_examples(dataset_name="p07_ds_my_dataset"))
```

### DeepEval
```python
from deepeval.dataset import EvaluationDataset
dataset = EvaluationDataset()
dataset.pull(alias="p07_ds_my_dataset")
```

### HuggingFace
```python
from datasets import load_dataset
ds = load_dataset("org/p07_ds_my_dataset", split="test")
```

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern matches `p07_ds_`, splits
sum to 1.0, schema_fields includes input + expected_output, body <= 4096 bytes,
quality == null, no actual data rows in body.
