---
kind: tools
id: bld_tools_model_registry
pillar: P04
llm_function: CALL
purpose: Tools available for model_registry production
quality: null
title: "Tools Model Registry"
version: "1.0.0"
author: wave1_builder_gen
tags: [model_registry, builder, tools]
tldr: "Tools available for model_registry production"
domain: "model_registry construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Production Tools
| Tool | Purpose | When |
| :--- | :--- | :--- |
| cex_compile.py | Bundles model artifacts | Post-training |
| cex_score.py | Computes performance metrics | Post-compilation |
| cex_retriever.py | Fetches models from registry | Inference |
| cex_doctor.py | Checks registry integrity | Maintenance |
| cex_deploy.py | Promotes models to production | Deployment |

## Validation Tools
| Tool | Purpose | When |
| :--- | :--- | :--- |
| val_schema.py | Validates metadata format | Pre-registration |
| val_drift.py | Detects model drift | Monitoring |
| val_security.py | Scans for vulnerabilities | Pre-deployment |

## External References
* MLflow
* DVC
* Kubernetes
