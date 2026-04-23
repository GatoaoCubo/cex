---
kind: quality_gate
id: p09_qg_playground_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for playground_config
quality: 9.0
title: "Quality Gate Playground Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [playground_config, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for playground_config"
domain: "playground_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_playground_config
  - p01_qg_reranker_config
  - p11_qg_audit_log
  - p01_qg_graph_rag_config
  - p09_qg_marketplace_app_manifest
  - p09_qg_sandbox_spec
  - p07_qg_cohort_analysis
  - bld_instruction_playground_config
  - bld_examples_eval_framework
  - p04_qg_stt_provider
---

## Quality Gate

## Definition
| metric         | threshold                          | operator | scope  |
|----------------|------------------------------------|----------|--------|
| schema_id      | ^p09_pg_[a-z][a-z0-9_]+.yaml$     | matches  | H02    |

## HARD Gates
| ID  | Check                  | Fail Condition                                  |
|-----|------------------------|-------------------------------------------------|
| H01 | YAML frontmatter valid | Missing or invalid YAML frontmatter             |
| H02 | ID matches pattern     | ID does not match ^p09_pg_[a-z][a-z0-9_]+.yaml$|
| H03 | kind field matches     | kind ≠ 'playground_config'                      |
| H04 | Required fields exist  | Missing 'name', 'description', or 'access_control'|
| H05 | Timeout defined        | timeout < 1s or > 72h                           |
| H06 | Resource limits valid  | CPU/memory limits exceed 80% of system capacity |
| H07 | Audit logs enabled     | audit_logs not set to 'enabled'                 |

## SOFT Scoring
| Dim | Dimension           | Weight | Scoring Guide                                  |
|-----|---------------------|--------|------------------------------------------------|
| D01 | Configuration completeness | 0.15 | 100% required fields present                   |
| D02 | Security controls    | 0.20 | 100% access control + encryption              |
| D03 | Usability            | 0.10 | Interactive features functional               |
| D04 | Documentation        | 0.15 | 100% API/usage guides complete                |
| D05 | Performance          | 0.10 | Latency < 500ms, error rate < 1%              |
| D06 | Compliance           | 0.10 | Meets data privacy and audit standards        |
| D07 | Scalability          | 0.10 | Supports 1000+ concurrent users               |
| D08 | Auditability         | 0.10 | Full traceability of user actions             |

## Actions
| Score   | Action                        |
|---------|-------------------------------|
| ≥9.5    | Automate deployment           |
| ≥8.0    | Schedule review               |
| ≥7.0    | Manual QA verification        |
| <7.0    | Reject and request revisions  |

## Bypass
| conditions                          | approver | audit trail         |
|------------------------------------|----------|---------------------|
| Urgent production fix required     | CISO     | Escalation log      |

## Examples

## Golden Example
```markdown
---
title: "AI Model Playground Config"
description: "Config for evaluating LLMs in a collaborative research environment"
vendor: "Hugging Face"
version: "2.1"
parameters:
  model: "google/flan-t5-xl"
  max_tokens: 2048
  rate_limit: 100
  logging: true
  evaluation_metrics: ["accuracy", "latency", "hallucination"]
---

### Overview
Configures a collaborative evaluation environment for large language models with real-time metrics.

### Setup
- Requires Hugging Face Spaces API key
- Uses Google Cloud for model hosting
- Integrates with AWS for data storage

### Usage
1. Load model from Hugging Face Model Hub
2. Enable interactive evaluation with Jupyter widgets
3. Collect metrics via Prometheus exporter

### Security
- Role-based access control (RBAC)
- Data anonymization pipeline
- Session expiration after 2 hours

### Evaluation
- Compare against baseline models
- Track user feedback via form submission
- Export results to BigQuery
```

## Anti-Example 1: Missing Evaluation Metrics
```markdown
---
title: "Incomplete Playground Config"
description: "Basic config without evaluation parameters"
vendor: "ExampleCo"
version: "0.5"
parameters:
  model: "meta/llama-2"
  max_tokens: 512
---
```
## Why it fails
Lacks essential evaluation metrics and security parameters required for proper product evaluation. Missing metrics makes it impossible to measure model performance, and no security settings expose the playground to misuse.

## Anti-Example 2: Sandbox Configuration
```markdown
---
title: "Misconfigured Playground"
description: "Includes sandbox isolation parameters"
vendor: "SomeCorp"
version: "1.0"
parameters:
  model: "openai/gpt-3.5"
  container_image: "nginx:latest"
  network_policy: "deny-all"
---
```
## Why it fails
Includes sandbox-specific isolation parameters (container_image, network_policy) that violate the playground spec. Playground configs should focus on interactive evaluation, not system isolation. This conflates playground with sandbox specifications.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
