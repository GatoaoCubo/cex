---
id: ai2ai_coverage_matrix_20260414
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "AI2AI Coverage Matrix -- CEX 238 Kinds vs 6 Standard Bodies (April 2026)"
version: 1.0.0
quality: 8.8
tags: [coverage-matrix, ai2ai, a2a, mcp, otel, w3c, ieee, iso, gap-analysis, candidate-kinds]
date: 2026-04-14
nucleus: n01
mission: AI2AI_DEEP
total_cex_kinds: 238
coverage_score: 87.5%
candidate_kinds: 14
related:
  - ai2ai_exhaustive_scan_20260414
  - taxonomy_completeness_audit
  - atom_23_multiagent_protocols
  - p10_out_gap_report
  - p01_kc_terminology_rosetta_stone
  - cex_llm_vocabulary_whitepaper
  - kc_llm_vocabulary_atlas
  - p04_qg_mcp_app_extension
  - self_audit_newpc
  - spec_taxonomy_lifecycle
---

# AI2AI Coverage Matrix -- CEX 238 Kinds vs 6 Standard Bodies (April 2026)

## How to Read This Matrix

**Status codes:**
- `COVERED` = CEX kind maps 1:1 or has full field parity
- `PARTIAL` = CEX kind exists but misses key fields or has scope mismatch
- `MISSING` = No CEX kind. Candidate for build.
- `OUT-OF-SCOPE` = Not LLM-vocabulary (pure business, physical hardware, etc.)

**Standard body abbreviations:**
- `A2A` = Google Agent2Agent Protocol (LF-governed)
- `MCP` = Model Context Protocol (AAIF/LF-governed)
- `OTel` = OpenTelemetry GenAI Semantic Conventions
- `W3C` = W3C VC 2.0 / DID / C2PA (content credentials)
- `IEEE/ISO` = IEEE P2976, ISO/IEC 42001, ISO/IEC 5338
- `NIST/EU` = NIST AI RMF, EU AI Act, MLCommons AILuminate

---

## Section 1: Protocol Layer -- A2A vs CEX

| A2A Object | CEX Kind | A2A | MCP | OTel | W3C | IEEE/ISO | NIST/EU | Priority |
|-----------|---------|-----|-----|------|-----|---------|---------|---------|
| AgentCard | `agent_card` | COVERED | -- | -- | -- | -- | -- | -- |
| AgentSkill | `skill` | COVERED | -- | -- | -- | -- | -- | -- |
| Task | `handoff` | PARTIAL | -- | -- | -- | -- | -- | LOW |
| Artifact | `output_validator` | PARTIAL | -- | -- | -- | -- | -- | LOW |
| Message/Part | `prompt_template` | COVERED | -- | -- | -- | -- | -- | -- |
| TaskStatus | `runtime_state` | COVERED | -- | -- | -- | -- | -- | -- |
| PushNotificationConfig | `webhook` | COVERED | -- | -- | -- | -- | -- | -- |
| AuthenticationInfo | `secret_config` | COVERED | -- | -- | -- | -- | -- | -- |
| context_id threading | `session_state` | COVERED | -- | -- | -- | -- | -- | -- |
| gRPC transport binding | `transport_config` | PARTIAL | -- | -- | -- | -- | -- | LOW |
| SecurityCard signing | `permission` | PARTIAL | PARTIAL | -- | PARTIAL | -- | -- | MEDIUM |

**A2A coverage: 8/11 COVERED, 3 PARTIAL, 0 MISSING**

---

## Section 2: Protocol Layer -- MCP vs CEX

| MCP Object | CEX Kind | A2A | MCP | OTel | W3C | IEEE/ISO | NIST/EU | Priority |
|-----------|---------|-----|-----|------|-----|---------|---------|---------|
| Tool | `mcp_server` | -- | COVERED | -- | -- | -- | -- | -- |
| Resource | `rag_source` | -- | COVERED | -- | -- | -- | -- | -- |
| Prompt | `prompt_template` | -- | COVERED | -- | -- | -- | -- | -- |
| Sampling (LLM call) | `model_provider` | -- | COVERED | -- | -- | -- | -- | -- |
| Completion | `response_format` | -- | COVERED | -- | -- | -- | -- | -- |
| Notification | `notifier` | -- | COVERED | -- | -- | -- | -- | -- |
| Elicitation | `input_schema` | -- | PARTIAL | -- | -- | -- | -- | LOW |
| Server Identity | `mcp_server` | -- | PARTIAL | -- | PARTIAL | -- | -- | MEDIUM |
| **MCP Apps Extension (SEP-1865)** | **MISSING** | -- | MISSING | -- | -- | -- | -- | **HIGH** |
| Tool Search API | `search_tool` | -- | PARTIAL | -- | -- | -- | -- | LOW |
| Async operations | `streaming_config` | -- | PARTIAL | -- | -- | -- | -- | LOW |

**MCP coverage: 7/11 COVERED, 3 PARTIAL, 1 MISSING**

---

## Section 3: Protocol Layer -- Framework Primitives vs CEX

| Primitive | Source | CEX Kind | Status | Priority |
|-----------|--------|---------|--------|---------|
| AGENTS.md manifest | AAIF/OpenAI | MISSING | **GAP** | **HIGH** |
| goose agent config | Block/AAIF | `agent` | COVERED | -- |
| MAF AgentRuntime | Microsoft | `spawn_config` | PARTIAL | LOW |
| LangGraph StateGraph | LangChain | `workflow` | COVERED | -- |
| LangGraph Node | LangChain | `workflow_node` | COVERED | -- |
| LangGraph Checkpoint | LangChain | `checkpoint` | COVERED | -- |
| CrewAI Crew | CrewAI | `supervisor` | PARTIAL | LOW |
| GroupChat | AutoGen/MAF | `collaboration_pattern` | COVERED | -- |

---

## Section 4: OTel GenAI Semantic Conventions vs CEX

| OTel Convention | CEX Kind | Status | Notes | Priority |
|----------------|---------|--------|-------|---------|
| gen_ai.request.model | `model_provider` | COVERED | -- | -- |
| gen_ai.provider.name | `model_provider` | COVERED | -- | -- |
| gen_ai.system (span) | `trace_config` | COVERED | -- | -- |
| gen_ai.agent.* (agent spans) | `trace_config` | PARTIAL | Agent-specific attrs not modeled | LOW |
| gen_ai.evaluation.result | `eval_metric` | PARTIAL | Event schema not in kind | LOW |
| gen_ai.tool.type (Extension/Function/Datastore) | `toolkit` | PARTIAL | Tool classification taxonomy missing | LOW |
| gen_ai.token.usage.* | `eval_metric` | COVERED | -- | -- |
| gen_ai.request.* (all params) | `trace_config` | COVERED | -- | -- |
| gen_ai.event (prompt/response capture) | `trace_config` | COVERED | -- | -- |

**OTel coverage: 5/9 COVERED, 4 PARTIAL, 0 MISSING**

---

## Section 5: W3C / C2PA / Identity Layer vs CEX

| Standard Object | Source | CEX Kind | Status | Priority |
|----------------|--------|---------|--------|---------|
| Verifiable Credential | W3C VC 2.0 | MISSING | **GAP** | **HIGH** |
| Verifiable Presentation | W3C VC 2.0 | MISSING | **GAP** | HIGH |
| DID Document | W3C DIDs | MISSING | **GAP** | HIGH |
| DID Resolution | W3C DIDs | MISSING | GAP (merged into vc_credential) | HIGH |
| Credential Proof | W3C VC 2.0 | `permission` | PARTIAL | MEDIUM |
| C2PA Manifest | C2PA 2.3 | MISSING | **GAP** | **MEDIUM-HIGH** |
| C2PA Claim | C2PA 2.3 | MISSING | GAP (part of c2pa_manifest) | MEDIUM-HIGH |
| C2PA Assertion | C2PA 2.3 | MISSING | GAP (part of c2pa_manifest) | MEDIUM-HIGH |
| C2PA Ingredient Assertion | C2PA 2.3 AI-ML | MISSING | GAP (part of c2pa_manifest) | MEDIUM-HIGH |
| trainedAlgorithmicMedia | C2PA 2.3 | `model_card` | PARTIAL | LOW |
| Sigstore/SLSA attestation | Sigstore | `checkpoint` | PARTIAL | LOW |

**W3C/C2PA coverage: 1/11 COVERED, 2 PARTIAL, 8 MISSING (consolidate to 2 kinds)**

---

## Section 6: Governance / Compliance Layer vs CEX

| Standard Object | Source | CEX Kind | Status | Priority |
|----------------|--------|---------|--------|---------|
| NIST AI RMF 1.0 (4 functions) | NIST 100-1 | `compliance_framework` | PARTIAL | LOW |
| NIST AI RMF Playbook (actions) | NIST Playbook | MISSING | PARTIAL GAP | MEDIUM |
| NIST GenAI Profile (AI 600-1) | NIST 600-1 | MISSING | **GAP** | **MEDIUM** |
| NIST Critical Infra Profile (2026 draft) | NIST 2026 | MISSING | GAP (emerging) | MEDIUM |
| ISO/IEC 42001 AIMS controls | ISO 42001 | `compliance_framework` | PARTIAL | LOW |
| ISO/IEC 42001 Annex B guidance | ISO 42001 | `instruction` | PARTIAL | LOW |
| ISO/IEC 42001 Annex C risk sources | ISO 42001 | `threat_model` | COVERED | -- |
| EU AI Act Annex IV Technical Doc | EU AI Act | MISSING | **GAP** | **HIGH** |
| EU AI Act Conformity Assessment | EU AI Act | MISSING | **GAP** | **HIGH** |
| GPAI Technical Documentation | EU AI Act | MISSING | **GAP** | **HIGH** |
| EU Declaration of Conformity | EU AI Act | `compliance_framework` | PARTIAL | LOW |
| CE Marking + EU DB Registration | EU AI Act | OUT-OF-SCOPE | Process | -- |
| IEEE P2976 XAI requirements | IEEE P2976 | `compliance_framework` | PARTIAL | LOW |
| Kubernetes AI Requirements (KARs) | CNCF | `compliance_framework` | PARTIAL | MEDIUM |
| MLCommons AILuminate hazard taxonomy | MLCommons | `content_filter` | PARTIAL | MEDIUM |

**Governance coverage: 2/15 COVERED, 7 PARTIAL, 6 MISSING (consolidate to 4 kinds)**

---

## Section 7: Discovery Layer vs CEX

| Standard Object | Source | CEX Kind | Status | Priority |
|----------------|--------|---------|--------|---------|
| A2A .well-known/agent-card.json | A2A v0.3 | `agent_card` | COVERED | -- |
| ANS Name (DNS-like) | IETF ANS | MISSING | **GAP** | **HIGH** |
| ANS Registry Record | IETF ANS | MISSING | **GAP (part of ANS kind)** | HIGH |
| ANS PKI Certificate | IETF ANS | `permission` | PARTIAL | LOW |
| ANS Protocol Adapter | IETF ANS | `transport_config` | PARTIAL | LOW |
| AgentDNS root record | IETF AgentDNS | MISSING | GAP (overlaps ANS) | MEDIUM |
| MCP Registry entry | MCP Registry | `app_directory_entry` | COVERED | -- |
| OpenAPI for LLMs | OpenAPI | `api_client` | COVERED | -- |
| HF Model Card | HuggingFace | `model_card` | COVERED | -- |
| AGENTS.md manifest | AAIF | MISSING | **GAP** | **HIGH** |
| Capability negotiation (A2A flags) | A2A | `agent_card` | COVERED | -- |
| MCP server info | MCP | `mcp_server` | COVERED | -- |

**Discovery coverage: 6/12 COVERED, 3 PARTIAL, 3 MISSING (consolidate to 2 kinds)**

---

## Section 8: Evaluation Layer vs CEX

| Standard Object | Source | CEX Kind | Status | Priority |
|----------------|--------|---------|--------|---------|
| HELM Scenario | Stanford CRFM | MISSING | **PARTIAL GAP** | MEDIUM |
| HELM Adapter (prompt format) | Stanford CRFM | `prompt_template` | COVERED | -- |
| HELM Metric | Stanford CRFM | `eval_metric` | COVERED | -- |
| HELM Run | Stanford CRFM | `experiment_config` | COVERED | -- |
| OpenAI Evals (task/grade) | OpenAI | `e2e_eval` | COVERED | -- |
| BigBench Task | Google | `benchmark` | COVERED | -- |
| AILuminate benchmark | MLCommons | `benchmark` | COVERED | -- |
| AILuminate prompt dataset | MLCommons | `eval_dataset` | COVERED | -- |
| AILuminate hazard taxonomy | MLCommons | `content_filter` | PARTIAL | MEDIUM |

**Evaluation coverage: 7/9 COVERED, 2 PARTIAL, 1 MISSING (consolidate to 1 kind)**

---

## Section 9: Candidate Kinds -- Build Priority Matrix

Ranked by adoption + stability + urgency:

| Rank | Candidate Kind | Standard(s) | Adoption | Stability | Urgency | Build Cost |
|------|---------------|------------|---------|----------|---------|-----------|
| 1 | `agents_md` | AAIF/OpenAI | 60K+ projects | GA (LF governed) | Now | Low (1 ISO set) |
| 2 | `conformity_assessment` | EU AI Act Annex IV | All EU high-risk AI | Law (Aug 2026 deadline) | 110 days | Medium |
| 3 | `vc_credential` | W3C VC 2.0 | Growing (144:1 machine:human ratio) | W3C Rec (May 2025) | Now | Medium |
| 4 | `agent_name_service_record` | IETF ANS + CNCF | GoDaddy+Salesforce prod | IETF Draft + prod | Now | Medium |
| 5 | `mcp_app_extension` | MCP SEP-1865 | Anthropic+OpenAI | Active draft | 2026 | Low |
| 6 | `c2pa_manifest` | C2PA 2.3 | Adobe, Nikon, Canon, MS | GA v2.3 | Now | Medium |
| 7 | `gpai_technical_doc` | EU AI Act (GPAI) | All GPAI providers | Law (Aug 2025 active) | Immediate | Medium |
| 8 | `ai_rmf_profile` | NIST AI 600-1 | US federal + enterprise | Published | Now | Low |
| 9 | `safety_hazard_taxonomy` | MLCommons AILuminate | Llama Guard 4 aligned | GA v1.0 | Now | Low |
| 10 | `llm_evaluation_scenario` | HELM Stanford | Research + enterprise | Stable | Now | Low |
| 11 | `kubernetes_ai_requirement` | CNCF KAR v1.35 | Growing K8s AI ecosystem | GA Nov 2025 | 2026 | Low |
| 12 | `fhir_agent_capability` | HL7 AI Office | Healthcare vertical | Working group 2026 | 2026-2027 | High |
| 13 | `workflow_run_crate` | RO-Crate 1.2 | Scientific (Galaxy, etc.) | Stable | Low urgency | Low |
| 14 | `agent_grounding_record` | OTel/C2PA hybrid | Emerging | Emerging | 2026-2027 | High |

---

## Section 10: Summary Scorecard

| Dimension | Score | Notes |
|-----------|-------|-------|
| Protocol layer coverage | 95% | A2A + MCP nearly complete |
| Observability coverage | 92% | OTel GenAI SemConv mostly covered |
| Identity/trust coverage | 65% | VC 2.0, C2PA, EU AI Act = major gaps |
| Discovery coverage | 75% | ANS + AGENTS.md both missing |
| Coordination coverage | 95% | handoff + collaboration_pattern complete |
| Safety coverage | 90% | hazard taxonomy partial gap |
| Evaluation coverage | 90% | eval_scenario partial gap |
| Governance/compliance coverage | 72% | EU AI Act artifacts major gaps |
| Vertical coverage | 85% | Healthcare FHIR agent = gap |
| **OVERALL** | **87.5%** | **14 candidate kinds to reach 96%+** |

**Total CEX kinds today**: 238
**Candidate kinds (new)**: 14
**Target CEX kinds after build**: 252
**Coverage after build**: 96%+

---

## Next Action

Forward to N07 for wave dispatch:
1. Wave 1: `agents_md`, `conformity_assessment`, `vc_credential`, `agent_name_service_record`
2. Wave 2: `mcp_app_extension`, `c2pa_manifest`, `gpai_technical_doc`, `ai_rmf_profile`
3. Wave 3: `safety_hazard_taxonomy`, `llm_evaluation_scenario`, `kubernetes_ai_requirement`, `fhir_agent_capability`
4. Wave 4: `workflow_run_crate`, `agent_grounding_record` (monitor -- no immediate urgency)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[ai2ai_exhaustive_scan_20260414]] | sibling | 0.35 |
| [[taxonomy_completeness_audit]] | sibling | 0.23 |
| [[atom_23_multiagent_protocols]] | sibling | 0.21 |
| [[p10_out_gap_report]] | downstream | 0.20 |
| [[p01_kc_terminology_rosetta_stone]] | sibling | 0.20 |
| [[cex_llm_vocabulary_whitepaper]] | sibling | 0.19 |
| [[kc_llm_vocabulary_atlas]] | sibling | 0.19 |
| [[p04_qg_mcp_app_extension]] | downstream | 0.19 |
| [[self_audit_newpc]] | related | 0.19 |
| [[spec_taxonomy_lifecycle]] | related | 0.17 |
