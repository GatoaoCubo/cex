---
kind: examples
id: bld_examples_workflow_node
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of workflow_node artifacts
quality: 8.8
title: "Examples Workflow Node"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [workflow_node, builder, examples]
tldr: "Golden and anti-examples of workflow_node artifacts"
domain: "workflow_node construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```yaml
kind: workflow_node
type: llm
name: text_generation_node
description: "Generates text using a Hugging Face transformer model"
inputs:
  - name: prompt
    type: string
    description: "Input prompt for text generation"
  - name: temperature
    type: float
    description: "Sampling temperature for model output"
outputs:
  - name: generated_text
    type: string
    description: "Model's generated text response"
configuration:
  model: "HuggingFace/llama-3-8b"
  api_key: "hf_abc123"
  max_tokens: 200
```

## Anti-Example 1: Missing Type Specification
```yaml
kind: workflow_node
name: data_processor
description: "Handles data transformation tasks"
inputs:
  - name: raw_data
    type: any
outputs:
  - name: processed_data
    type: any
```
## Why it fails
No `type` field makes the node ambiguous. A workflow system needs to know if this is an LLM, database, or custom node to enforce proper input/output validation and integration.

## Anti-Example 2: Mixing Node Types
```yaml
kind: workflow_node
type: database
name: user_retriever
description: "Fetches user data from PostgreSQL"
inputs:
  - name: user_id
    type: integer
outputs:
  - name: user_data
    type: object
  - name: llm_summary
    type: string
```
## Why it fails
A database node should only produce database-related outputs. Adding an `llm_summary` output implies this node is also performing LLM processing, violating the single-responsibility principle for workflow nodes.
