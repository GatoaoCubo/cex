---
kind: output_template
id: bld_output_template_model_architecture
pillar: P05
llm_function: PRODUCE
quality: 9.1
title: "Output Template Model Architecture"
version: "1.0.0"
author: n05_builder
tags: [model_architecture, output_template, P05, builder]
tldr: "Canonical output template for model_architecture artifacts with all required sections."
domain: "model_architecture construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
---

# Output Template: model_architecture

```markdown
---
id: p02_ma_{{family}}_{{scale}}
kind: model_architecture
pillar: P02
title: "{{Family}} {{Scale}} Architecture"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{author}}"
domain: "{{NLP|vision|audio|multimodal|RL}}"
architecture_type: "{{transformer|cnn|rnn|mlp|diffusion|graph|hybrid}}"
parameter_count: "{{e.g. 7B, 340M, 1.5B}}"
quality: null
tags: [model_architecture, {{domain}}, {{architecture_type}}]
tldr: "{{One-sentence description of architecture}}"
---

# Architecture: {{Family}} {{Scale}}

## Overview
| Attribute | Value |
|-----------|-------|
| Design Goal | {{primary objective}} |
| Novelty | {{vs. prior work}} |
| Input | {{text/image/audio/multimodal}} |
| Output | {{text/embedding/logits/image}} |
| Framework | {{pytorch/jax/tensorflow}} |

## Layer Structure
| # | Layer Type | Count | Hidden Dim | Notes |
|---|-----------|-------|-----------|-------|
| 1 | {{layer}} | {{n}} | {{dim}} | {{notes}} |

## Connectivity Pattern
| Component | Pattern | Notes |
|-----------|---------|-------|
| {{component}} | {{sequential/residual/attention}} | {{details}} |

## Parameter Profile
| Component | Params | % of Total |
|-----------|--------|-----------|
| {{component}} | {{count}} | {{pct}}% |
| **Total** | **{{total}}** | **100%** |

## Compute Profile
| Metric | Value | Notes |
|--------|-------|-------|
| Inference FLOPs | {{e.g. 3.5T}} | Per forward pass |
| Peak Memory | {{e.g. 14GB}} | fp16 inference |
| Throughput | {{tokens/s}} | On A100 |
| Context Length | {{tokens}} | Max sequence |

## Training Considerations
| Aspect | Recommendation |
|--------|---------------|
| Initialization | {{e.g. Kaiming, Xavier}} |
| Optimizer | {{AdamW lr=1e-4 wd=0.1}} |
| LR Schedule | {{cosine with warmup}} |
| Batch Size | {{e.g. 2048 tokens}} |
```
