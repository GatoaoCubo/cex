---
id: p03_rt_n03_builder_agent_20260406
kind: reasoning_trace
pillar: P03
title: "Example — Reasoning Trace: 8F Pipeline Build Decision"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
agent: n03-agent-builder
intent: "create sales agent for SaaS onboarding"
conclusion: "Build agent kind with 4 tools, consultative persona, sonnet tier"
confidence: 0.87
duration_ms: 3400
domain: reasoning_trace
quality: 9.1
tags: [reasoning-trace, chain-of-thought, 8f, audit, decision]
tldr: "Reasoning trace from N03 building a sales agent — 5 steps, rejected template clone and generic agent, chose hybrid approach with 0.87 confidence."
when_to_use: "Auditing agent decisions, debugging low-quality outputs, or training from past reasoning"
keywords: [reasoning, trace, chain-of-thought, decision, audit, confidence]
density_score: null
related:
  - p03_ins_reasoning_trace_builder
  - bld_knowledge_card_reasoning_trace
  - bld_schema_reasoning_trace
  - p01_kc_reasoning_trace
  - bld_output_template_reasoning_trace
  - bld_examples_reasoning_trace
  - p03_sp_reasoning_trace_builder
  - bld_collaboration_reasoning_trace
  - p01_kc_agent
  - p11_qg_reasoning_trace
---

# Reasoning Trace: Sales Agent Build (N03)

## Context
| Field | Value |
|-------|-------|
| Agent | n03-agent-builder |
| Intent | "create sales agent for SaaS onboarding" |
| Trigger | User request via /build |
| Model | claude-opus-4-6 |
| Timestamp | 2026-04-06T14:30:00-03:00 |

## Steps
### Step 1: Kind Resolution (F1)
| Field | Value |
|-------|-------|
| Thought | Intent mentions "agent" — resolve to kind=agent, pillar=P02 |
| Evidence | Motor matched "create" verb + "agent" object → kind=agent (confidence 0.95) |
| Confidence | 0.95 |
| Duration | 120ms |

### Step 2: Template Match (F3)
| Field | Value |
|-------|-------|
| Thought | Search for similar agents — sales/onboarding domain |
| Evidence | cex_retriever found ex_agent_customer_support.md (72% match), ex_agent_research.md (41% match) |
| Confidence | 0.72 |
| Duration | 450ms |
| Decision | 72% >= 60% threshold → use Template-First approach, adapt customer_support agent |

### Step 3: Approach Selection (F4)
| Field | Value |
|-------|-------|
| Thought | Template match is good but not exact — need hybrid approach |
| Evidence | customer_support agent has tools: search, email, CRM. Sales needs: CRM, calendar, proposal_gen, pipeline_tracker |
| Alternatives considered | (a) Pure template clone — rejected: 3/4 tools different. (b) Fresh build — rejected: structure matches 72%. (c) Hybrid — accepted: keep structure, swap tools |
| Confidence | 0.85 |
| Duration | 800ms |

### Step 4: Tool Selection (F5)
| Field | Value |
|-------|-------|
| Thought | Sales agent needs CRM access, scheduling, and proposal generation |
| Evidence | bld_tools_agent.md lists recommended tools for sales domain. 4 tools selected. |
| Tools selected | crm_lookup, calendar_book, proposal_generate, pipeline_update |
| Confidence | 0.90 |
| Duration | 200ms |

### Step 5: Persona and Tier (F4 continued)
| Field | Value |
|-------|-------|
| Thought | Sales persona should be consultative, not pushy. Tier: sonnet (balanced cost/quality) |
| Evidence | Brand config tone=professional, decision_manifest specifies "helpful, not aggressive" |
| Confidence | 0.88 |
| Duration | 300ms |

## Conclusion
| Field | Value |
|-------|-------|
| Decision | Build agent kind with hybrid approach (adapt customer_support template) |
| Persona | Consultative sales assistant, professional tone |
| Tools | 4 tools: crm_lookup, calendar_book, proposal_generate, pipeline_update |
| Model tier | balanced (sonnet) |
| Overall confidence | 0.87 |
| Total duration | 3,400ms |

## Alternatives Rejected
| Alternative | Reason | Confidence if chosen |
|------------|--------|---------------------|
| Pure template clone | 3/4 tools different, would need heavy post-edit | 0.45 |
| Fresh build from scratch | Wastes 72% structural match | 0.60 |
| Generic agent (no specialization) | Fails brand alignment requirement | 0.30 |

## Boundary
reasoning_trace IS: structured record of step-by-step reasoning with evidence and confidence per step.
reasoning_trace IS NOT: a trace config (observability rules), a quality gate (pass/fail), or the final artifact output.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_reasoning_trace_builder]] | related | 0.39 |
| [[bld_knowledge_card_reasoning_trace]] | upstream | 0.37 |
| [[bld_schema_reasoning_trace]] | downstream | 0.36 |
| [[p01_kc_reasoning_trace]] | related | 0.35 |
| [[bld_output_template_reasoning_trace]] | downstream | 0.35 |
| [[bld_examples_reasoning_trace]] | downstream | 0.34 |
| [[p03_sp_reasoning_trace_builder]] | related | 0.33 |
| [[bld_collaboration_reasoning_trace]] | upstream | 0.32 |
| [[p01_kc_agent]] | upstream | 0.31 |
| [[p11_qg_reasoning_trace]] | downstream | 0.30 |
