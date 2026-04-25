---
quality: 8.4
quality: 7.8
id: kind_tool_dependency_matrix
kind: knowledge_card
pillar: P01
nucleus: N03
domain: security-routing
title: Kind Tool Dependency Matrix -- 300 kinds x 2 routing flags
version: 1.0.0
created: 2026-04-20
author: n03_builder
tags: [security, routing, kinds, preflight, mcp, open-source]
related: _docs/security/mcp_access_matrix.md
spec: _docs/specs/spec_preflight_expansion_smart_routing.md
density_score: 0.98
updated: "2026-04-22"
---

# Kind Tool Dependency Matrix

Maps all 293 CEX kinds to their routing requirements.
Used by: cex_router_v2.py, cex_preflight.py, cex_kind_classifier.py.

## Field Definitions

| Field | Values | Meaning |
|-------|--------|---------|
| requires_external_context | true/false | Kind benefits from web search, GitHub data, or external sources. N07 runs preflight MCP gather before dispatch. |
| requires_live_tools | true/false | Kind needs MCP at RUNTIME (not pre-compilable). Routes to Claude-only. |

## Routing Logic

```
requires_live_tools=true        --> route: claude-only (live MCP access required)
requires_external_context=true  --> route: any runtime (N07 pre-compiles via MCP before dispatch)
both false                      --> route: any runtime (structural generation, no external context)
```

## Summary Stats

- Total kinds: 293
- requires_external_context=true: 74 (25%)
- requires_live_tools=true: 5 (5 kinds, Claude-only routing)
- Both false: 300 kinds (structural generation, any runtime)

## Live-Tools Kinds (Claude-only routing)

These 5 kinds require live MCP tool access at runtime. Pre-flight cannot substitute.

| Kind | Pillar | Why live tools required |
|------|--------|------------------------|
| browser_tool | P04 | Needs live browser session for web automation |
| computer_use | P04 | Needs live screen capture and control |
| db_connector | P04 | Needs live database connection to validate schema/queries |
| interactive_demo | P05 | Needs live browser rendering to verify UI state |
| mcp_server | P04 | Needs live MCP protocol connection to test server responses |

## Full Classification Matrix (300 kinds)

| Kind | Pillar | ext_ctx | live_tools | Description |
|------|--------|---------|------------|-------------|
| ab_test_config | P11 | no | no | A/B test experiment configuration for conversion optimizatio |
| action_paradigm | P04 | no | no | How agents execute actions in environments |
| action_prompt | P03 | no | no | Task prompt sent by human/orchestrator to the agent |
| agent | P02 | no | no | Agent definition (persona + capabilities) |
| agent_card | P08 | no | no | Deployment spec for autonomous agent  identity, model, tools |
| agent_computer_interface | P08 | no | no | GUI/terminal interaction protocol for agents |
| agent_grounding_record | P10 | no | no | Per-inference provenance record: tool calls, RAG chunks, mod |
| agent_name_service_record | P04 | no | no | IETF ANS + CNCF AgentDNS registry record for agent discovery |
| agent_package | P02 | no | no | Portable AI agent package (ISO format) -- self-contained, LL |
| agent_profile | P02 | no | no | Agent persona and identity construction method |
| agentic_rag | P01 | no | no | Agent-driven retrieval augmented generation pattern |
| agents_md | P02 | no | no | AAIF/OpenAI AGENTS.md project-root manifest: setup/test/lint |
| aggregate_root | P06 | no | no | DDD entry point entity that enforces domain invariants and c |
| ai_rmf_profile | P11 | YES | no | NIST AI RMF profile artifact -- 4 functions (GOVERN/MAP/MEAS |
| alert_rule | P09 | no | no | Observable threshold condition that triggers a notification  |
| analyst_briefing | P05 | YES | no | Gartner/Forrester/IDC analyst briefing deck with positioning |
| api_client | P04 | no | no | Typed REST/GraphQL/gRPC API client |
| api_reference | P06 | no | no | API reference doc with endpoints, params, responses, auth, e |
| app_directory_entry | P05 | YES | no | App directory entry for FREE-tier discovery: tagline, screen |
| audio_tool | P04 | no | no | Speech-to-text, text-to-speech, audio analysis |
| audit_log | P11 | no | no | Immutable audit log configuration for SOC2 Type II complianc |
| axiom | P02 | no | no | Principio fundamental imutavel  parte da identidade profunda |
| backpressure_policy | P09 | no | no | Policy defining how a system responds when downstream consum |
| batch_config | P09 | no | no | Async batch processing config for bulk API operations (OpenA |
| benchmark | P07 | YES | no | Performance measurement (latency, cost, quality) |
| benchmark_suite | P07 | YES | no | Composite benchmark definition with multiple tasks |
| bias_audit | P07 | YES | no | Fairness evaluation methodology and results |
| boot_config | P02 | no | no | Boot configuration per provider |
| bounded_context | P08 | no | no | Explicit boundary within which a domain model applies, with  |
| browser_tool | P04 | no | YES | Browser automation: DOM parsing, navigation, interaction, sc |
| bugloop | P11 | no | no | Automatic correction loop (detect > fix > verify) |
| c2pa_manifest | P10 | no | no | C2PA 2.3 content credential for AI-generated media: claim, a |
| canary_config | P09 | no | no | Gradual traffic rollout configuration for safe deployment wi |
| capability_registry | P08 | no | no | Searchable catalog of all agents available to crews. Indexes |
| case_study | P05 | YES | no | Customer case study with challenge/solution/outcome/quote na |
| chain | P03 | no | no | Chained prompt sequence (output A -> input B) |
| changelog | P01 | no | no | Product changelog entry with semver, features, fixes, breaki |
| checkpoint | P12 | no | no | Workflow state snapshot |
| chunk_strategy | P01 | no | no | Chunking strategy |
| churn_prevention_playbook | P03 | YES | no | Churn prevention playbook: signal detection, intervention tr |
| circuit_breaker | P09 | no | no | Resilience pattern that auto-disables failing dependencies a |
| citation | P01 | YES | no | Structured source attribution with provenance, URL, date, an |
| cli_tool | P04 | no | no | Ferramenta CLI |
| code_executor | P04 | no | no | Sandboxed runtime for code execution (Docker, E2B, Jupyter) |
| code_of_conduct | P05 | no | no | Community code of conduct (Contributor Covenant pattern) wit |
| cohort_analysis | P07 | YES | no | Cohort analysis spec for retention measurement and LTV model |
| collaboration_pattern | P12 | no | no | Multi-agent coordination topology |
| competitive_matrix | P01 | YES | no | Competitive feature matrix for sales battle cards and procur |
| compliance_checklist | P11 | YES | no | Compliance checklist for SOC2, GDPR, HIPAA, EU AI Act audits |
| compliance_framework | P11 | YES | no | Regulatory mapping and attestation for AI systems |
| component_map | P08 | no | no | Component map (what connects to what) |
| compression_config | P10 | no | no | Context compression configuration for tool outputs |
| computer_use | P04 | no | YES | Screen, keyboard, and mouse control by LLM (Anthropic, brows |
| conformity_assessment | P11 | YES | no | EU AI Act Annex IV conformity assessment for high-risk AI sy |
| consolidation_policy | P10 | no | no | Memory lifecycle management policy |
| constitutional_rule | P11 | no | no | Absolute behavioral constraint for an agent that cannot be o |
| constraint_spec | P03 | no | no | Constrained generation rules |
| content_filter | P11 | no | no | Input/output content filtering pipeline config |
| content_monetization | P11 | YES | no | Config-driven content monetization pipeline  PARSE>PRICING>C |
| context_doc | P01 | no | no | Domain context |
| context_file | P03 | no | no | Project-scoped instruction file auto-injected into context |
| context_map | P08 | no | no | DDD diagram of relationships and integration patterns betwee |
| context_window_config | P03 | no | no | Token budget allocation, priority tiers, and overflow rules  |
| contributor_guide | P05 | no | no | OSS CONTRIBUTING.md spec: dev setup, PR flow, coding standar |
| cost_budget | P09 | YES | no | Token budget allocation, spend tracking, cost alerts per pro |
| course_module | P05 | YES | no | Online course module with learning objectives and assessment |
| crew_template | P12 | no | no | CrewAI/AutoGen-style reusable crew blueprint (roles, process |
| curation_nudge | P11 | no | no | Periodic prompt to persist knowledge to durable memory |
| customer_segment | P02 | YES | no | Customer segment/ICP definition artifact with firmographics  |
| daemon | P04 | no | no | Processo background |
| dag | P12 | no | no | Acyclic dependency graph |
| data_contract | P06 | no | no | Schema-level agreement between a data producer and consumer  |
| data_residency | P09 | YES | no | Data residency configuration for GDPR and regional complianc |
| dataset_card | P01 | YES | no | Structured dataset documentation |
| db_connector | P04 | no | YES | Structured database connector (SQL, GraphQL, REST-to-DB) |
| decision_record | P08 | no | no | ADR: contexto, decisao, consequencias |
| deployment_manifest | P09 | no | no | Specification of what artifacts to deploy, where to deploy t |
| diagram | P08 | no | no | Architecture diagram (ASCII or Mermaid) |
| diff_strategy | P04 | no | no | Change application and matching algorithm |
| discovery_questions | P01 | YES | no | MEDDIC/BANT discovery question bank per buyer persona and de |
| dispatch_rule | P12 | no | no | Dispatch rule (keyword > agent_group) |
| document_loader | P04 | no | no | Ingere arquivos e converte em chunks (PDF, HTML, CSV, etc) |
| domain_event | P12 | no | no | Immutable record of something significant that happened in t |
| domain_vocabulary | P01 | no | no | Governed registry of canonical terms for a bounded context,  |
| drift_detector | P11 | no | no | Monitor that detects distribution shift in model inputs, out |
| dual_loop_architecture | P08 | no | no | Outer/inner loop agent control architecture |
| e2e_eval | P07 | no | no | Teste end-to-end (pipeline completo) |
| ecommerce_vertical | P01 | YES | no | eCommerce industry vertical: cart/checkout, PCI-DSS, recomme |
| edit_format | P06 | no | no | LLM-to-host file change format specification |
| edtech_vertical | P01 | YES | no | Education/EdTech industry vertical: FERPA, COPPA, LMS integr |
| effort_profile | P09 | no | no | Effort and thinking level configuration for builder executio |
| embedder_provider | P01 | no | no | Text embedding provider for vector search |
| embedding_config | P01 | no | no | Embedding model configuration |
| enterprise_sla | P11 | YES | no | Enterprise SLA template with uptime, latency, support commit |
| entity_memory | P10 | no | no | Memoria sobre entidades |
| enum_def | P06 | no | no | Enumeracao reutilizavel |
| env_config | P09 | no | no | Environment variables |
| episodic_memory | P10 | no | no | Long-term store of past interactions indexed by episode for  |
| eval_dataset | P07 | YES | no | Test case collection |
| eval_framework | P07 | no | no | End-to-end evaluation framework integration |
| eval_metric | P07 | no | no | Individual evaluation metric definition |
| event_schema | P06 | no | no | AsyncAPI / CloudEvents schema for event payloads defining st |
| event_stream | P04 | no | no | Configuration for a real-time ordered sequence of domain eve |
| expansion_play | P03 | YES | no | Account expansion play: upsell triggers, cross-sell map, NRR |
| experiment_config | P09 | no | no | A/B test and prompt experiment configuration with variants,  |
| experiment_tracker | P07 | no | no | Experiment configuration and results tracking |
| fallback_chain | P02 | no | no | Fallback sequence (model A > B > C) |
| faq_entry | P01 | YES | no | FAQ entry with question, canonical answer, related links, su |
| feature_flag | P09 | no | no | Feature flag (on/off, gradual rollout) |
| few_shot_example | P01 | no | no | Exemplo input/output pra prompt |
| fhir_agent_capability | P08 | YES | no | HL7 FHIR R5 AI agent capability declaration: SMART on FHIR s |
| finetune_config | P02 | YES | no | Fine-tuning job configuration: dataset, base model, adapter  |
| fintech_vertical | P01 | YES | no | Fintech industry vertical: SOC2+PCI-DSS, KYC/AML, fraud dete |
| formatter | P05 | no | no | Output formatter (json, md, yaml) |
| function_def | P04 | no | no | LLM-callable function definition (JSON Schema tool) |
| github_issue_template | P05 | no | no | GitHub issue template (bug/feature/question) with required f |
| glossary_entry | P01 | YES | no | Term definition |
| golden_test | P07 | no | no | Reference test case (quality 9.5+) |
| govtech_vertical | P01 | YES | no | Government/govtech industry vertical: FedRAMP, FISMA, GSA, C |
| gpai_technical_doc | P11 | YES | no | EU AI Act GPAI technical documentation (Annex IV / Article 5 |
| graph_rag_config | P01 | no | no | Graph-based RAG architecture configuration |
| guardrail | P11 | no | no | Safety restriction (safety boundary) |
| handoff | P12 | no | no | Handoff instruction (task + context + commit) |
| handoff_protocol | P02 | no | no | Agent-to-agent transfer protocol |
| healthcare_vertical | P01 | YES | no | Healthcare industry vertical: HIPAA, HL7/FHIR, PHI handling, |
| hibernation_policy | P09 | no | no | Policy for hibernating idle serverless workloads to save cos |
| hitl_config | P11 | no | no | Human-in-the-loop approval flow configuration: review trigge |
| hook | P04 | no | no | Pre/post processing hook |
| hook_config | P04 | no | no | Hook lifecycle configuration for builder execution |
| incident_report | P11 | YES | no | AI incident documentation and post-mortem |
| input_schema | P06 | no | no | Input contract |
| instruction | P03 | no | no | Step-by-step execution instructions for agents or pipelines |
| integration_guide | P05 | YES | no | Deep integration guide for platform partners and paid-tier o |
| interactive_demo | P05 | no | YES | Interactive product demo script with guided-tour steps and t |
| interface | P06 | no | no | Agent-to-agent integration contract |
| invariant | P08 | no | no | Lei operacional (inviolavel) |
| judge_config | P07 | no | no | LLM judge configuration for automated evaluation |
| knowledge_card | P01 | YES | no | Fato atomico pesquisavel (densidade > 0.8) |
| knowledge_graph | P01 | YES | no | Graph-based knowledge schema with entity types, relation typ |
| knowledge_index | P10 | no | no | Search index (BM25, FAISS config) |
| kubernetes_ai_requirement | P09 | YES | no | CNCF Kubernetes AI Requirement (KAR) conformance artifact: G |
| landing_page | P05 | YES | no | Complete production-ready landing page with 12 sections, res |
| learning_record | P10 | YES | no | Learning record (what worked/failed) |
| legal_vertical | P01 | YES | no | Legal industry vertical: privilege, billable hour, contract  |
| lens | P02 | no | no | Perspectiva especializada sobre dominio |
| lifecycle_rule | P11 | no | no | Lifecycle rule (freshness, archive, promote) |
| lineage_record | P01 | YES | no | Provenance chain documenting how a knowledge artifact was de |
| llm_evaluation_scenario | P07 | no | no | HELM Stanford CRFM evaluation scenario: task instances, metr |
| llm_judge | P07 | no | no | Config LLM-as-Judge |
| marketplace_app_manifest | P09 | YES | no | Marketplace app manifest spec for Claude/LangChain/HuggingFa |
| mcp_app_extension | P04 | no | no | MCP Apps Extension (SEP-1865): app manifest, install/launch/ |
| mcp_server | P04 | no | YES | Servidor MCP (tools + resources) |
| memory_architecture | P10 | no | no | Complete memory system architecture design |
| memory_benchmark | P07 | no | no | Memory system quality evaluation suite |
| memory_scope | P02 | no | no | Agent memory configuration |
| memory_summary | P10 | no | no | Compressed memory summary |
| memory_type | P10 | no | no | Classification of persistent memory by source, confidence, a |
| mental_model | P02 | no | no | Agent mental model (routing, decisions) |
| messaging_gateway | P04 | no | no | Unified multi-platform messaging transport abstraction |
| model_architecture | P02 | no | no | Neural network architecture definition |
| model_card | P02 | YES | no | LLM spec in use (pricing, context, capabilities) |
| model_provider | P02 | no | no | LLM provider adapter (Claude, GPT, Gemini, Ollama, OpenRoute |
| model_registry | P10 | YES | no | Model versioning and artifact tracking |
| multi_modal_config | P04 | no | no | Input format, resolution, encoding, and routing rules for mu |
| multimodal_prompt | P03 | no | no | Cross-modal prompt pattern for vision/audio/text |
| naming_rule | P08 | no | no | Naming rule |
| notifier | P04 | no | no | Push notification delivery (email, SMS, Slack, Discord) |
| nps_survey | P11 | YES | no | NPS survey config: question, scale, follow-up, segmentation, |
| nucleus_def | P02 | no | no | Formal definition of a CEX nucleus (N00-N07). Fields: nucleu |
| oauth_app_config | P09 | no | no | OAuth2/PKCE app config for partner integrations: scopes, red |
| onboarding_flow | P05 | no | no | User onboarding flow with activation milestones and aha-mome |
| ontology | P01 | YES | no | Formal taxonomy and ontology definitions (OWL, SKOS, schema. |
| openapi_spec | P06 | no | no | Machine-readable API contract following OpenAPI Specificatio |
| optimizer | P11 | no | no | Process optimizer (metric > action) |
| output_validator | P05 | no | no | Validacao pos-LLM |
| parser | P05 | no | no | Output data extractor |
| partner_listing | P05 | YES | no | Partner directory listing for SI/reseller channels with tier |
| path_config | P09 | no | no | System paths |
| pattern | P08 | no | no | Pattern reutilizavel (ex: continuous batching) |
| permission | P09 | no | no | Permission rule (read/write/execute) |
| personality | P02 | no | no | Hot-swap persona applied to an agent at runtime |
| pipeline_template | P12 | no | no | Scenario-indexed agent pipeline recipe (new-feature, bug-fix |
| pitch_deck | P05 | YES | no | Sales pitch deck with problem/solution/traction/ask slide st |
| planning_strategy | P03 | no | no | Agent planning approach definition |
| playground_config | P09 | no | no | Playground/sandbox config for interactive product evaluation |
| plugin | P04 | no | no | Extensao plugavel |
| preference_dataset | P11 | YES | no | Curated dataset of human-labeled preference pairs used for R |
| press_release | P05 | YES | no | Press release with AP-style headline, dateline, lede, quotes |
| pricing_page | P05 | YES | no | Pricing page artifact with tier comparison and conversion co |
| procedural_memory | P10 | no | no | Skill and procedure storage/retrieval system |
| process_manager | P12 | no | no | Event-driven coordinator for multi-step processes that route |
| product_tour | P05 | YES | no | In-app product tour walkthrough with step/tooltip/trigger sp |
| prompt_cache | P10 | no | no | TTL, eviction, and invalidation config for cached LLM prompt |
| prompt_compiler | P03 | no | no | Intent-to-artifact transmutation rules. Compiles vague user  |
| prompt_optimizer | P03 | no | no | Automated prompt improvement and compilation tool |
| prompt_technique | P03 | no | no | Specific prompting method or pattern |
| prompt_template | P03 | no | no | Reusable template with {{vars}} to generate prompts |
| prompt_version | P03 | no | no | Versioned prompt snapshot |
| prosody_config | P09 | no | no | Voice personality and emotion settings |
| prospective_memory | P10 | no | no | Scheduled future actions and reminders that an agent must ex |
| quality_gate | P11 | no | no | Quality barrier (pass/fail with score) |
| quantization_config | P09 | no | no | Model quantization and compression settings |
| quickstart_guide | P05 | YES | no | Quickstart guide artifact for product/API onboarding in unde |
| rag_source | P01 | no | no | Fonte externa indexavel |
| rate_limit_config | P09 | no | no | Rate limiting: RPM, TPM, budget |
| rbac_policy | P09 | no | no | Role-based access control policy for multi-tenant isolation |
| realtime_session | P09 | no | no | Live bidirectional session configuration |
| reasoning_strategy | P03 | no | no | Prompting technique for structured reasoning |
| reasoning_trace | P03 | no | no | Structured chain-of-thought reasoning with confidence scores |
| red_team_eval | P07 | YES | no | Teste adversarial |
| referral_program | P11 | YES | no | Referral program design with viral coefficient and reward st |
| regression_check | P07 | no | no | Comparacao contra baseline |
| renewal_workflow | P12 | no | no | Renewal workflow with stages, owners, automation, escalation |
| repo_map | P01 | no | no | Codebase context extraction strategy |
| reranker_config | P01 | no | no | Retrieval reranking model and strategy config |
| research_pipeline | P04 | YES | no | 7-stage research engine: INTENT>PLAN>RETRIEVE>RESOLVE>SCORE> |
| response_format | P05 | no | no | LLM response format (how the agent responds) |
| retriever | P04 | no | no | Busca vetorial/keyword/hibrida sobre store local (RAG core) |
| retriever_config | P01 | no | no | Retrieval configuration (top_k, hybrid, reranker) |
| retry_policy | P09 | no | no | Backoff, jitter, and budget configuration for retrying faile |
| revision_loop_policy | P11 | no | no | Policy governing max revision iterations and escalation prio |
| reward_model | P07 | no | no | Process/outcome reward model configuration |
| reward_signal | P11 | no | no | Continuous quality signal |
| rl_algorithm | P02 | no | no | Reinforcement learning training algorithm definition |
| roi_calculator | P11 | YES | no | ROI calculator spec with inputs, formulas, TCO comparison fo |
| role_assignment | P02 | no | no | CrewAI Agent-style binding: role -> agent + responsibilities |
| router | P02 | no | no | Routing rule (task > agent_group) |
| runtime_rule | P09 | no | no | Runtime rule (timeouts, retries, limits) |
| runtime_state | P10 | no | no | Estado mental variavel por sessao (routing, decisoes em runt |
| safety_hazard_taxonomy | P11 | YES | no | MLCommons AILuminate / Llama Guard hazard taxonomy -- 12 haz |
| safety_policy | P11 | YES | no | Organizational AI safety governance rules |
| saga | P12 | no | no | Long-running distributed transaction composed of local steps |
| sales_playbook | P03 | YES | no | Sales playbook with personas, discovery flow, objection hand |
| sandbox_config | P09 | no | no | Isolated code execution environment config |
| sandbox_spec | P09 | no | no | Isolated sandbox environment spec for enterprise pilot procu |
| schedule | P12 | no | no | Trigger temporal que inicia workflow |
| scoring_rubric | P07 | no | no | Evaluation criterion (5D, 12LP, custom) |
| sdk_example | P04 | YES | no | SDK code example showing canonical integration patterns per  |
| search_strategy | P04 | no | no | Inference-time compute allocation strategy |
| search_tool | P04 | no | no | Busca web, semantica ou hibrida (Tavily, Serper, Perplexity) |
| secret_config | P09 | no | no | Secret management |
| self_improvement_loop | P11 | no | no | Agent/system self-evolution mechanism |
| session_backend | P10 | no | no | Per-user session state persistence backend |
| session_state | P10 | no | no | Session state (ephemeral, snapshot) |
| signal | P12 | no | no | Inter-agent signal (complete, error, progress) |
| skill | P04 | no | no | Reusable capability with trigger + phases (AgentSkills.io /  |
| slo_definition | P09 | no | no | Measurable service level objective with target threshold and |
| smoke_eval | P07 | no | no | Quick sanity test (< 30s) |
| social_publisher | P04 | YES | no | Automatic publishing agent: LOAD>FETCH>SELECT>GENERATE>OPTIM |
| software_project | P02 | no | no | Complete software project definition  architecture, dependen |
| spawn_config | P12 | no | no | Spawn configuration (solo, grid, continuous) |
| sso_config | P09 | no | no | SSO/SAML/OIDC identity provider integration configuration |
| state_machine | P12 | no | no | Formal finite state machine with states, transitions, guards |
| streaming_config | P05 | no | no | SSE, WebSocket, and chunked response streaming configuration |
| stt_provider | P04 | no | no | Speech-to-text provider integration |
| subscription_tier | P11 | YES | no | SaaS subscription tier definition with pricing and feature m |
| supabase_data_layer | P04 | no | no | Supabase-specific data layer  tables, RLS policies, edge fun |
| supervisor | P08 | no | no | Crew orchestrator that composes and coordinates multiple bui |
| system_prompt | P03 | no | no | System prompt that defines agent identity and rules |
| tagline | P03 | YES | no | Short memorable phrase capturing brand essence  taglines, sl |
| team_charter | P12 | no | no | Mission contract for a specific crew instance. Bridges GDP d |
| terminal_backend | P09 | no | no | Abstract execution backend selectable at runtime |
| thinking_config | P09 | no | no | Extended thinking and budget token settings |
| threat_model | P11 | YES | no | Structured hazard/risk assessment for AI systems |
| toolkit | P04 | no | no | Collection of callable tools with auto JSON Schema |
| trace_config | P07 | no | no | Trace/span configuration for 8F pipeline observability |
| training_method | P02 | YES | no | Model training/adaptation technique definition |
| trajectory_eval | P07 | no | no | Agent trajectory evaluation methodology |
| transport_config | P09 | no | no | Network transport layer for realtime communication |
| tts_provider | P04 | no | no | Text-to-speech provider integration |
| type_def | P06 | no | no | Custom type definition |
| unit_eval | P07 | no | no | Agent/prompt unit test |
| usage_quota | P09 | no | no | Usage quota and fair-use enforcement configuration |
| usage_report | P07 | YES | no | Usage analytics report spec for billing and CFO dashboards |
| user_journey | P05 | YES | no | End-to-end user journey map from awareness to conversion |
| user_model | P10 | YES | no | Cross-session dialectic model of the user -- preferences, wo |
| vad_config | P09 | no | no | Voice activity detection settings |
| validation_schema | P06 | no | no | Post-generation validation contract (system applies, LLM doe |
| validator | P06 | no | no | Validation rule (pre-commit, quality gate) |
| value_object | P06 | no | no | Immutable typed value without identity, defined entirely by  |
| vc_credential | P10 | YES | no | W3C Verifiable Credential 2.0 for AI agent identity, provena |
| vector_store | P01 | no | no | Vector database backend for similarity search |
| vision_tool | P04 | no | no | Image analysis, OCR, screenshot interpretation |
| visual_workflow | P12 | no | no | GUI-based workflow editor configuration |
| voice_pipeline | P04 | no | no | End-to-end voice agent architecture definition |
| webhook | P04 | no | no | Endpoint HTTP event-driven inbound/outbound |
| webinar_script | P03 | YES | no | Webinar script with intro/agenda/segments/Q&A/CTA + speaker  |
| white_label_config | P09 | YES | no | White-label/reseller configuration for branded deployments |
| workflow | P12 | no | no | Workflow (sequential/parallel steps) |
| workflow_node | P12 | no | no | Typed node in visual/programmatic workflow |
| workflow_primitive | P12 | no | no | Workflow execution primitive (Step, Parallel, Loop, Conditio |
| workflow_run_crate | P10 | no | no | RO-Crate 1.2 Workflow Run Crate: scientific workflow executi |
| working_memory | P10 | no | no | Short-term context store for a single active task, cleared a |

## Heuristic Basis

Classification follows spec_preflight_expansion_smart_routing.md DP5:

| Pattern | requires_external_context | Reasoning |
|---------|---------------------------|-----------|
| Knowledge cards, research kinds | YES | Need citations, external sources, market data |
| Vertical kinds (edtech, fintech, healthcare, etc.) | YES | Market data, regulatory requirements |
| Compliance, legal, regulatory | YES | Current law and standard text required |
| Landing pages, pitch decks, sales materials | YES | Competitor and market context |
| Benchmarks, case studies, audits | YES | External performance data points |
| Config, schema, type definitions | no | Internal structure only |
| Agent, prompt, workflow | no | Internal orchestration |
| Memory, state, evaluation tooling | no | Internal tooling |
| Security operations, monitoring | no | Internal constraints |
