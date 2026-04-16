---
kind: schema
id: bld_schema_workflow_node
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for workflow_node artifacts
quality: 9.2
title: "Schema Workflow Node"
version: "1.1.0"
author: n03_hybrid_review4
tags: [workflow_node, builder, schema]
tldr: "Schema for a single node inside a workflow DAG -- aligned with LangGraph StateGraph, Prefect task, Temporal activity, Dagster op, Airflow operator canonical patterns."
domain: "workflow_node construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.92
---

## Frontmatter Fields

### Required

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string | yes | -- | Must match ID Pattern below |
| kind | string | yes | "workflow_node" | Must equal "workflow_node" |
| pillar | string | yes | "P12" | Must equal "P12" |
| title | string | yes | -- | Descriptive human-readable name |
| version | string | yes | "1.0.0" | Semantic version |
| created | date | yes | -- | ISO 8601 date |
| updated | date | yes | -- | ISO 8601 date |
| author | string | yes | -- | Creator identifier |
| domain | string | yes | -- | Node domain (e.g., "agent", "data", "llm") |
| quality | null | yes | null | NEVER self-score; peer review assigns |
| tags | array | yes | [] | Keywords |
| tldr | string | yes | -- | One-sentence summary |
| node_type | enum | yes | -- | One of: agent, tool, router, condition, parallel, start, end, human |
| input_schema | string | yes | -- | Type name or JSON-Schema ref for inputs (LangGraph state key or typed in/out) |
| output_schema | string | yes | -- | Type name or JSON-Schema ref for outputs |
| next_nodes | array | yes | [] | List of downstream node ids; for router/condition use objects {condition, target} |
| retry_policy | object | yes | {max_attempts: 1, backoff: "none"} | max_attempts, backoff (none/linear/exponential), retry_on |
| timeout_s | integer | yes | 60 | Hard timeout in seconds |

### Recommended

| Field | Type | Notes |
|-------|------|-------|
| state_update | string | Keys this node writes to shared state (LangGraph StateGraph pattern) |
| trigger_rule | enum | Airflow-style: all_success, all_failed, all_done, one_success, one_failed, none_failed, always |
| cache_key | string | Prefect-style cache key expression for memoized execution |
| heartbeat_s | integer | Temporal-style heartbeat interval for long activities |
| required_resources | array | Dagster-style resource_defs keys |
| description | string | Free-form explanation |

## ID Pattern

Regex: `^p12_wn_[a-z][a-z0-9_]+\.md$`

Examples: `p12_wn_classify_intent.md`, `p12_wn_router_by_confidence.md`

## Body Structure (required sections)

1. **Overview** -- purpose, role in parent workflow, upstream/downstream context.
2. **Inputs** -- each input: name, type, required/optional, source node.
3. **Outputs** -- each output: name, type, consumers.
4. **Execution** -- stepwise logic; tool/model invocations; state transitions.
5. **Edges** (or **Next Nodes**) -- transitions with condition expressions for router/condition types.
6. **Failure Modes** -- retry behavior, compensation, fallback edge.

## Constraints

- node_type is an enum; no free-form values.
- For node_type == "router" or "condition", next_nodes MUST be an array of {condition, target} objects.
- For node_type == "parallel", next_nodes is the fan-out list; a corresponding join/end node must exist.
- retry_policy.max_attempts >= 1; backoff must be one of {none, linear, exponential}.
- timeout_s must be > 0 and <= 3600 (1 hour) unless heartbeat_s is set.
- File size must not exceed 4096 bytes.
- quality is assigned by peer review; it is always null at authoring time.
