---
kind: quality_gate
id: p12_qg_workflow_node
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for workflow_node ARTIFACTS (not runtime)
quality: 9.0
title: "Quality Gate Workflow Node"
version: "1.1.0"
author: n03_hybrid_review4
tags: [workflow_node, builder, quality_gate]
tldr: "Tests the workflow_node artifact structure (frontmatter + body sections), not runtime behavior."
domain: "workflow_node construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - bld_examples_workflow_node
  - bld_output_template_workflow_node
  - bld_examples_workflow_primitive
  - bld_schema_workflow_node
  - p11_qg_function_def
  - bld_output_template_workflow_primitive
  - p07_qg_eval_framework
  - p11_qg_response_format
  - workflow-node-builder
  - atom_12_dify
---

## Quality Gate

## Definition

| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| ID pattern match | ^p12_wn_[a-z][a-z0-9_]+\.md$ | matches | frontmatter.id |
| Max bytes | 4096 | <= | file size |
| Required sections | 5 | >= | body |
| Edge declaration present | 1 | >= | body: Edges/Transitions |

## HARD Gates

| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | Valid YAML frontmatter | YAML parse error or missing frontmatter |
| H02 | ID matches ^p12_wn_[a-z][a-z0-9_]+\.md$ | ID does not match pattern |
| H03 | kind == "workflow_node" | kind field missing or != "workflow_node" |
| H04 | pillar == "P12" | pillar != "P12" |
| H05 | quality == null | quality self-scored (must be null) |
| H06 | node_type in enum | node_type not in [agent, tool, router, condition, parallel, start, end, human] |
| H07 | Body contains "## Inputs" and "## Outputs" sections | Either section missing |
| H08 | Body contains "## Edges" or "## Next Nodes" section | No transition declaration |
| H09 | state_schema reference or input/output types declared | Missing type contract |

## SOFT Scoring

| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D1 | Schema compliance | 0.25 | All required frontmatter fields present with correct types |
| D2 | Edge/transition clarity | 0.20 | Next-node routing explicit (conditional vs unconditional edges named) |
| D3 | Contract rigor | 0.20 | Input/output types declared, state_schema referenced |
| D4 | Industry alignment | 0.20 | Uses LangGraph/Prefect/Temporal/Dagster/Airflow terminology correctly |
| D5 | Documentation density | 0.15 | tldr + description + example invocation present |

Weight check: 0.25 + 0.20 + 0.20 + 0.20 + 0.15 = 1.00

## Actions

| Score | Action |
|-------|--------|
| GOLDEN (>= 9.5) | Auto-approve, promote to examples library |
| PUBLISH (>= 8.0) | Approve as-is |
| REVIEW (>= 7.0) | Peer review required before publish |
| REJECT (< 7.0) | Rework; fix all HARD failures and re-submit |

## Bypass

| Conditions | Approver | Audit Trail |
|------------|----------|-------------|
| Emergency hotfix to existing node | Pillar owner (P12) | Log bypass with reason + version diff in git commit |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
