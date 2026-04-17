---
kind: examples
id: bld_examples_marketplace_app_manifest
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of marketplace_app_manifest artifacts
quality: 8.8
title: "Examples Marketplace App Manifest"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [marketplace_app_manifest, builder, examples]
tldr: "Golden and anti-examples of marketplace_app_manifest artifacts"
domain: "marketplace_app_manifest construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```markdown
---
name: "Anthropic Claude Integration"
description: "Seamless integration with Anthropic's Claude API for advanced text generation and reasoning."
vendor: "Anthropic"
version: "1.2.0"
permissions:
  - "api_access:claude"
  - "data_usage:training"
pricing:
  - tier: "Free"
    limit: "1000 tokens/month"
  - tier: "Pro"
    price: "$0.0001/token"
    limit: "unlimited"
metadata:
  compatibility: ["Claude", "LangChain"]
  model: "Claude 3"
  license: "Apache 2.0"
```

## Anti-Example 1: Missing Required Fields
```markdown
---
name: "HuggingFace Model"
description: "A HuggingFace model for NLP tasks"
vendor: "HuggingFace"
version: "0.1.0"
metadata:
  model: "bert-base-uncased"
```
## Why it fails
Missing required `permissions` and `pricing` sections. All marketplace manifests must define access controls and monetization terms.

## Anti-Example 2: Invalid Permissions
```markdown
---
name: "LangChain Plugin"
description: "LangChain integration for RAG workflows"
vendor: "LangChain Inc"
version: "2.0.0"
permissions:
  - "full_system_access"
pricing:
  - tier: "Enterprise"
    price: "$5000/month"
```
## Why it fails
"full_system_access" is an invalid permission scope. Permissions must be specific and granular (e.g., "api_access:specific_endpoint"). The example also lacks metadata compatibility information required for marketplace listings.
