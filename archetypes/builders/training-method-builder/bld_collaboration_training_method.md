---
kind: collaboration
id: bld_collaboration_training_method
pillar: P12
llm_function: COLLABORATE
quality: 9.1
title: "Collaboration Training Method"
version: "1.0.0"
author: n05_builder
tags: [training_method, collaboration, P12, builder]
tldr: "Collaboration patterns for training-method-builder: upstream/downstream dependencies and crew integration."
domain: "training_method construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.86
---

# Collaboration: training-method-builder

## Upstream Dependencies (What I Need)
| Artifact | From | When |
|----------|------|------|
| model_architecture | P02 / N03 | To understand target model structure |
| knowledge_card (domain) | P01 / N04 | Domain-specific training conventions |
| dataset documentation | P01 / N04 | Dataset format, size, preprocessing |

## Downstream Products (What I Produce)
| Artifact | To | Purpose |
|----------|-----|---------|
| training_method | P02 | Paradigm specification for model training |
| Informs finetune_config | P02 / N03 | Concrete job uses this paradigm |
| Informs model_card | P02 / N04 | Model docs reference training approach |

## Crew Roles
| Nucleus | Role | Interaction |
|---------|------|------------|
| N03 Builder | Creates the artifact | Receives handoff with training domain + model type |
| N01 Intelligence | Provides research context | Feeds training trends, dataset benchmarks |
| N04 Knowledge | Provides domain KCs | Injects learning paradigm conventions |
| N05 Operations | Validates and deploys | Runs doctor + hooks on final artifact |

## Handoff Format
When N07 dispatches to N03 for a training_method build:
```
Build: training_method for [domain]
Kind: training_method
Pillar: P02
Context:
  - Model architecture: [link or description]
  - Target task: [classification/generation/alignment/etc.]
  - Compute budget: [available hardware]
  - Dataset: [source and format]
Read: archetypes/builders/training-method-builder/ (all 13 ISOs)
Output: P02_model/training_methods/p02_tm_[domain].md
```

## Signal Protocol
After completion:
```python
from _tools.signal_writer import write_signal
write_signal('n03', 'complete', 9.0)
```
