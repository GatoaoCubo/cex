---
kind: schema
id: bld_schema_reasoning_trace
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for reasoning_trace - SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
quality: 9.1
title: "Schema Reasoning Trace"
version: "1.0.0"
author: n03_builder
tags: [reasoning_trace, builder, examples]
tldr: "Golden and anti-examples for reasoning trace construction, demonstrating ideal structure and common pitfalls."
domain: "reasoning trace construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_reasoning_trace_builder
  - bld_knowledge_card_reasoning_trace
  - bld_examples_reasoning_trace
  - p11_qg_reasoning_trace
  - p03_sp_reasoning_trace_builder
  - bld_output_template_reasoning_trace
  - bld_memory_reasoning_trace
  - bld_config_reasoning_trace
  - p01_kc_reasoning_trace
  - bld_schema_reranker_config
---

# Schema: reasoning_trace
## Artifact Identity
| Field | Value |
|-------|-------|
| Pillar | `P03` |
| Type | literal `reasoning_trace` |
| Machine format | `yaml` |
| Naming | `p03_rt_{agent}_{timestamp}.yaml` |
| Max bytes | 8192 |
## Required Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| agent | string, non-empty, lowercase slug preferred | YES | - | agent or agent_group whose reasoning is recorded |
| intent | string, non-empty | YES | - | decision question or goal being reasoned about |
| steps | list[step_object], non-empty, >= 2 entries | YES | - | ordered chain of reasoning steps |
| conclusion | string, non-empty | YES | - | final decision summary referencing strongest evidence |
| confidence | number, `0.0 <= x <= 1.0` | YES | - | overall confidence — geometric mean of step confidences |
| timestamp | string, ISO 8601 datetime | YES | - | when the reasoning occurred |
## Step Object Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| step | integer, >= 1 | YES | - | sequential step number |
| thought | string, non-empty | YES | - | what the agent considered at this point |
| evidence | string, non-empty | YES | - | concrete data supporting or refuting the thought |
| confidence | number, `0.0 <= x <= 1.0` | YES | - | confidence for this specific step |
## Optional Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| alternatives_rejected | list[alt_object] | NO (strongly recommended) | omitted | rejected paths with reasons |
| duration_ms | integer, >= 0 | NO | omitted | total reasoning time in milliseconds |
| context | string | NO | omitted | additional context that informed the decision |
| trigger | string | NO | omitted | what initiated the reasoning (instruction ID, user request) |
| tags | list[string] | NO | omitted | classification tags for trace indexing |
## Alternative Object Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| alternative | string, non-empty | YES | - | description of the rejected option |
| reason | string, non-empty | YES | - | evidence-based reason for rejection |
## Semantic Rules
1. One trace describes one decision chain from one agent
2. Steps must be in chronological/logical order (step 1 before step 2)
3. Each step MUST have non-empty thought AND evidence — thought without evidence is assertion
4. Confidence 0.0-0.3 = low (flag for review), 0.3-0.7 = medium, 0.7-1.0 = high
5. A step with no concrete evidence gets confidence capped at 0.3
6. Overall confidence is geometric mean of step confidences (penalizes weak links)
7. Traces are immutable once emitted — corrections produce a new trace
8. `alternatives_rejected` is technically optional but traces without it have lower audit value
## Boundary Rules
`reasoning_trace` IS:
- structured decision audit record
- step-evidence-confidence chain for one agent's reasoning
- human-readable YAML for auditability
`reasoning_trace` IS NOT:
- `instruction`: no execution directives, no phase definitions, no action items
- `system_prompt`: no agent identity, no persona, no rules
- `workflow_primitive`: no step graph, no conditions, no loops
- `signal`: no atomic event notification, no fire-and-forget status
## Canonical Minimal Example
```yaml
agent: research-agent
intent: select embedding model for P01 retriever
steps:
  - step: 1
    thought: OpenAI ada-002 is widely used and well-documented
    evidence: "benchmark: 63.4% on MTEB, 8191 token limit, $0.0001/1K tokens"
    confidence: 0.8
  - step: 2
    thought: Cohere embed-v3 offers better multilingual support
    evidence: "benchmark: 66.1% on MTEB, 512 token limit, requires API key rotation"
    confidence: 0.7
  - step: 3
    thought: ada-002 token limit is sufficient for our chunk size (512 tokens)
    evidence: "current chunk_size=512 in P01 embedding_config"
    confidence: 0.9
conclusion: "Selected ada-002 — sufficient token limit for our chunks, lower cost, better documentation"
alternatives_rejected:
  - alternative: Cohere embed-v3
    reason: "Higher MTEB score but 512 token limit creates truncation risk with our chunk strategy"
confidence: 0.79
timestamp: "2026-04-06T14:30:00-03:00"
duration_ms: 4500
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_reasoning_trace_builder]] | upstream | 0.58 |
| [[bld_knowledge_card_reasoning_trace]] | upstream | 0.53 |
| [[bld_examples_reasoning_trace]] | downstream | 0.48 |
| [[p11_qg_reasoning_trace]] | downstream | 0.46 |
| [[p03_sp_reasoning_trace_builder]] | upstream | 0.46 |
| [[bld_output_template_reasoning_trace]] | upstream | 0.43 |
| [[bld_memory_reasoning_trace]] | downstream | 0.41 |
| [[bld_config_reasoning_trace]] | downstream | 0.40 |
| [[p01_kc_reasoning_trace]] | upstream | 0.40 |
| [[bld_schema_reranker_config]] | sibling | 0.38 |
