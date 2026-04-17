---
kind: examples
id: bld_examples_data_residency
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of data_residency artifacts
quality: 8.8
title: "Examples Data Residency"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [data_residency, builder, examples]
tldr: "Golden and anti-examples of data_residency artifacts"
domain: "data_residency construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```yaml
kind: data_residency
name: eu_gdpr_compliance
labels:
  region: EU
  compliance: GDPR
spec:
  data_storage:
    provider: AWS
    regions: ["eu-west-1", "eu-central-1"]
  data_processing:
    provider: Azure
    regions: ["westeurope", "northeurope"]
  encryption:
    at_rest: AES-256
    in_transit: TLS-1.2
  legal:
    dpa: "https://aws.amazon.com/compliance/gdpr/"
    audit_logs: "https://azure.microsoft.com/en-us/compliance/audit-logs/"
```

## Anti-Example 1: Vague Region Specification
```yaml
kind: data_residency
name: generic_eu_setup
labels:
  region: EU
spec:
  data_storage:
    provider: Google Cloud
    regions: ["EU"]
```
## Why it fails
GDPR requires specific member state locations (e.g., "de" for Germany), not generic "EU" labels. Vague region definitions fail to meet legal requirements for data localization.

## Anti-Example 2: Missing Encryption Requirements
```yaml
kind: data_residency
name: us_compliance
labels:
  region: US
spec:
  data_storage:
    provider: AWS
    regions: ["us-east-1"]
```
## Why it fails
The spec omits encryption standards for data at rest/in transit, which are mandatory for GDPR and regional compliance. Data residency alone is insufficient without proper cryptographic protections.
