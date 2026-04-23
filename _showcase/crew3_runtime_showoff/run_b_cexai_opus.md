---
id: p02_agent_customer_support_triage
kind: agent
pillar: P02
title: "Customer Support Triage Agent"
showcase_id: showcase_agent_customer_support_triage
version: "1.0.0"
created: "2026-04-22"
updated: "2026-04-22"
author: "n03_builder"
agent_group: "support-engine"
domain: "customer_support_triage"
llm_function: BECOME
capabilities_count: 6
tools_count: 8
iso_files_count: 10
routing_keywords: [customer-support, triage, rag-retrieval, escalation, multi-language, helpdesk]
quality: 8.8
tags: [agent, customer-support, triage, rag, escalation, multi-language, P02]
tldr: "Triages inbound support tickets via RAG KB lookup, scores urgency, routes to tier-1/2/human, and responds in 12+ languages"
density_score: 0.91
thinking_budget: medium
linked_artifacts:
  primary: "p02_agent_customer_support_triage"
  related:
    - p01_kc_agent
    - bld_schema_agent
    - bld_architecture_agent
    - p02_agent_petshop_crm
    - p11_qg_agent
    - bld_knowledge_card_agent
    - p10_lr_agent-builder
    - bld_output_template_agent
    - bld_instruction_agent
    - bld_schema_retriever_config
---

## Overview

`customer-support-triage` is a support-engine specialist in `customer_support_triage`.
Classifies tickets by intent + urgency, retrieves KB candidates via RAG, auto-resolves
T0 cases, escalates T1-T3 per rules, and replies in the caller's detected locale (12+).

## Capabilities

- Classifies ticket intent (billing/tech/account/abuse/general) via LLM + regex
- Retrieves top-K KB candidates from RAG with confidence scoring
- Scores urgency P0-P3 using signal matrix (SLA class, churn risk, keywords)
- Routes to resolution tier T0-T3 per escalation rules
- Generates locale-detected responses in 12+ languages
- Logs every decision with trace ID for audit trail

## Tools

| # | Tool | Purpose |
|---|------|---------|
| 1 | `rag_retriever` [MCP] | Semantic + BM25 KB search, top-K with confidence |
| 2 | `intent_classifier` | LLM+regex intent (billing/tech/account/abuse/general) |
| 3 | `urgency_scorer` | Signal-matrix P0-P3 (SLA class, churn risk, keywords) |
| 4 | `translation_gateway` [API] | DeepL/LibreTranslate for 12+ locales |
| 5 | `escalation_router` | Rules engine: tier routing by confidence + urgency |
| 6 | `ticket_writer` [MCP] | Create/update helpdesk tickets (Zendesk/Freshdesk) |
| 7 | `audit_logger` | Decision trace to .cex/runtime/ with trace ID |
| 8 | `language_detector` | Locale detection (langdetect/fastText) |

## Agent_group Position

Agent_group: `support-engine` | Upstream: n07_orchestrator, inbound webhook |
Downstream: human_agent_queue, tier2_specialist_agent, audit_pipeline

## File Structure

```
agents/customer_support_triage/agent_package/
  SPEC_CST_001_MANIFEST.md        SPEC_CST_006_OUTPUT_TEMPLATE.md
  SPEC_CST_002_QUICK_START.md     SPEC_CST_007_EXAMPLES.md
  SPEC_CST_003_PRIME.md           SPEC_CST_008_ERROR_HANDLING.md
  SPEC_CST_004_INSTRUCTIONS.md    SPEC_CST_009_UPLOAD_KIT.md
  SPEC_CST_005_ARCHITECTURE.md    SPEC_CST_010_SYSTEM_INSTRUCTION.md
```

## Routing

Triggers: "triage support ticket", "classify inbound request", "escalate to human"
NOT when: billing refund execution (finance-engine), code debugging (N05), sales (N06)

## Escalation Rules

| Tier | Trigger | Action | SLA |
|------|---------|--------|-----|
| T0 Auto | confidence >= 0.85 + urgency <= P2 | RAG response, close | 2 min |
| T1 Review | confidence 0.60-0.84 OR urgency P1 | Draft + human queue | 15 min |
| T2 Specialist | confidence < 0.60 OR urgency P0 | Specialist + manager alert | 1 hr |
| T3 Human | abuse/legal/data-breach keywords | Incident protocol | 5 min |
| Fallback | RAG 0 results | Acknowledge + queue T2 | 30 min |

## RAG Config

| Parameter | Value |
|-----------|-------|
| retriever | rag_retriever MCP -- semantic + BM25 hybrid |
| top_k | 5, confidence >= 0.60 |
| chunk_strategy | 512-token sliding window, 10% overlap |
| reranker | cross-encoder bge-reranker-base (post top-K) |
| index_sources | KB articles + resolved tickets + FAQ (nightly) |
| fallback | BM25 if semantic < 0.40 |

## Multi-Language Support

| Group | Locales | Detection | Response |
|-------|---------|-----------|---------|
| Primary (native) | en | built-in | native LLM generation |
| Latin script | pt-BR, es, fr, de, it, nl | langdetect | translation_gateway |
| CJK | ja, zh-CN, ko | fastText | translation_gateway |
| RTL | ar | fastText | translation_gateway + RTL flag |
| Devanagari | hi | fastText | translation_gateway |

## Input / Output

IN (required): `ticket_body`, `ticket_id`, `customer_id`
IN (optional): `sla_class` (standard/premium/enterprise), `channel` (email/chat/api)
OUT: `resolution_tier` (T0-T3), `response_draft` (locale), `urgency_score` (P0-P3),
     `decision_trace` (dict), `detected_locale` (ISO 639-1)

## Quality Gates

HARD (all must pass): H01 YAML valid | H02 id=`^p02_agent_` | H03 id==stem |
H04 kind=="agent" | H05 quality==null | H06 10 fields | H07 llm_function==BECOME |
H08 agent_group set.
SOFT: S03 agent_package>=10 files | S06 capabilities_count(6)==body(6) |
S09 density>=0.80 | S10 no filler phrases.

## Common Issues

| Issue | Fix |
|-------|-----|
| RAG confidence < 0.60 | Run N04 KB enrichment pipeline |
| Wrong locale on short text | Fallback to Accept-Language header |
| T1 escalation loop | Default sla_class="standard" if absent |
| Audit log missing | Log async; never block resolution path |

## Related Artifacts

| Artifact | Rel | Score |
|----------|-----|-------|
| [[p01_kc_agent]] | upstream | 0.61 |
| [[bld_schema_agent]] | schema | 0.59 |
| [[bld_architecture_agent]] | arch | 0.54 |
| [[bld_schema_retriever_config]] | rag-sibling | 0.52 |
| [[p11_qg_agent]] | quality-gate | 0.49 |
| [[bld_knowledge_card_agent]] | domain-kc | 0.48 |
| [[p10_lr_agent-builder]] | memory | 0.46 |
| [[bld_output_template_agent]] | template | 0.43 |
| [[bld_instruction_agent]] | build-proc | 0.41 |
| [[p02_agent_petshop_crm]] | sibling | 0.38 |

---
version: 1.0.0 | author: n03_builder | quality: null
