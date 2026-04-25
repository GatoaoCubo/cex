---
id: n00_mentor_context
kind: context_doc
8f: F3_inject
pillar: P01
nucleus: n00
title: "CEX Universal Vocabulary -- Mentor Context"
version: "2.0.0"
author: n07_orchestrator
quality: 9.1
tags: [mentor, vocabulary, taxonomy, 8f, pillars, kinds, nuclei, archetype]
tldr: "Pre-compiled reference for /mentor: 8F pipeline + 12 pillars + 300 kinds + 8 nuclei."
domain: "CEX system"
created: "2026-04-17"
updated: "2026-04-24"
density_score: 0.95
related:
  - p01_kc_cex_project_overview
  - agent_card_engineering_nucleus
  - agent_card_n04
  - bld_collaboration_kind
  - agent_card_n03
  - skill
  - spec_cex_system_map
  - ctx_cex_new_dev_guide
  - spec_mission_100pct_coverage
  - p03_sp_n03_creation_nucleus
---

# CEX Universal Vocabulary

Pre-compiled context for the `/mentor` command. This document is the single
source for structural questions about CEX's typed knowledge system.

---

## Section 1: The 8F Pipeline

Every task in CEX -- build, research, analyze, deploy, price -- follows 8 functions in sequence.

| Function | Name | What it does | Key action |
|----------|------|-------------|------------|
| F1 | CONSTRAIN | Resolve kind, pillar, schema from user intent | Read `kinds_meta.json` + `_schema.yaml` |
| F2 | BECOME | Load builder identity (12 ISOs per kind) | Read `archetypes/builders/{kind}-builder/` |
| F3 | INJECT | Assemble context: KCs, examples, brand, memory, similar artifacts | Read `P01_knowledge/library/kind/kc_{kind}.md` |
| F3b | PERSIST | (optional) Declare new knowledge to save | Entity memory, fact updates, learning records |
| F3c | GROUND | (optional) Record source provenance | Path, confidence score, freshness |
| F4 | REASON | Plan approach, sections, density target | GDP if subjective; autonomous if technical |
| F5 | CALL | Use tools for enrichment | Compile, doctor, index, retriever |
| F6 | PRODUCE | Generate complete artifact with frontmatter + body | Follow builder instructions, density >= 0.85 |
| F7 | GOVERN | Validate quality gates (H01-H07), score (D1-D5) | Target 9.0+; retry if < 8.0 (max 2) |
| F7b | LEARN | (optional) Capture feedback signals | Reward signals, regression checks |
| F8 | COLLABORATE | Save, compile, commit, signal | `cex_compile.py` + `git commit` + `signal_writer` |

**Key rule**: 8F is mandatory for ALL tasks, not just builds. Research, analysis,
documentation, pricing -- everything flows through 8F.

---

## Section 2: The 12 Pillars

| Code | Name | Domain | Kind count | Primary nuclei |
|------|------|--------|-----------|----------------|
| P01 | Knowledge | Storage, retrieval, KCs, RAG, verticals | 32 | N01, N04 |
| P02 | Model | Agents, providers, personas, training | 24 | N02, N03 |
| P03 | Prompt | Templates, chains, system prompts, reasoning | 21 | N02, N03 |
| P04 | Tools | External capabilities: CLI, MCP, browser, API | 36 | N05 |
| P05 | Output | Production artifacts: pages, decks, guides | 23 | N03, N06 |
| P06 | Schema | Data contracts: types, validation, interfaces, DDD | 13 | N03 |
| P07 | Evaluation | Quality, scoring, benchmarks, testing | 25 | N05 |
| P08 | Architecture | System structure: diagrams, decisions, cards, DDD | 14 | N03 |
| P09 | Config | Runtime settings: env, secrets, flags, quotas, resilience | 39 | N05 |
| P10 | Memory | State, context, indexing, provenance | 22 | N04 |
| P11 | Feedback | Learning, correction, compliance, monetization, safety | 31 | N03, N06 |
| P12 | Orchestration | Workflows, dispatch, scheduling, crews, DDD events | 20 | N07 |

**Total: 300 kinds across 12 pillars.**

---

## Section 3: All 300 Kinds

### P01 Knowledge (32 kinds)

| Kind | Purpose |
|------|---------|
| agentic_rag | Agent-driven retrieval augmented generation pattern |
| changelog | Product changelog entry with semver, features, fixes, breaking changes |
| chunk_strategy | Chunking strategy for document ingestion |
| citation | Structured source attribution with provenance, URL, date, reliability |
| competitive_matrix | Competitive feature matrix for sales battle cards |
| context_doc | Domain context document |
| dataset_card | Structured dataset documentation |
| discovery_questions | MEDDIC/BANT discovery question bank per buyer persona |
| domain_vocabulary | Governed registry of canonical terms for a bounded context |
| ecommerce_vertical | eCommerce industry vertical template |
| edtech_vertical | Education/EdTech industry vertical template |
| embedder_provider | Text embedding provider for vector search |
| embedding_config | Embedding model configuration |
| faq_entry | FAQ entry with question, canonical answer, related links |
| few_shot_example | Input/output example for prompts |
| fintech_vertical | Fintech industry vertical template |
| glossary_entry | Term definition |
| govtech_vertical | Government/govtech industry vertical template |
| graph_rag_config | Graph-based RAG architecture configuration |
| healthcare_vertical | Healthcare industry vertical template |
| knowledge_card | Atomic searchable fact (density > 0.8) |
| knowledge_graph | Graph-based knowledge schema with entities and relations |
| legal_vertical | Legal industry vertical template |
| lineage_record | Provenance chain documenting artifact derivation and curation |
| ontology | Formal taxonomy and ontology definitions |
| query_optimizer | Query rewriting, expansion, and multi-hop decomposition for RAG |
| rag_source | External indexable source |
| repo_map | Codebase context extraction strategy |
| reranker_config | Retrieval reranking model and strategy config |
| retriever_config | Retrieval configuration (top_k, hybrid, reranker) |
| synthetic_data_config | Synthetic training data generation pipeline configuration |
| vector_store | Vector database backend for similarity search |

### P02 Model (24 kinds)

| Kind | Purpose |
|------|---------|
| agent | Agent definition (persona + capabilities) |
| agent_package | Portable AI agent package (ISO format) |
| agent_profile | Agent persona and identity construction |
| agents_md | AGENTS.md project-root manifest |
| axiom | Fundamental immutable principle |
| boot_config | Boot configuration per provider |
| customer_segment | Customer segment/ICP definition |
| distillation_config | Teacher-student model compression and knowledge distillation setup |
| fallback_chain | Fallback sequence (model A > B > C) |
| finetune_config | Fine-tuning job configuration |
| handoff_protocol | Agent-to-agent transfer protocol |
| lens | Specialized domain perspective |
| memory_scope | Agent memory configuration |
| mental_model | Agent mental model (routing, decisions) |
| model_architecture | Neural network architecture definition |
| model_card | LLM spec (pricing, context, capabilities) |
| model_provider | LLM provider adapter (Claude, GPT, Gemini, Ollama) |
| nucleus_def | Formal CEX nucleus definition (N00-N07) |
| personality | Hot-swap persona applied to an agent at runtime |
| rl_algorithm | Reinforcement learning algorithm definition |
| role_assignment | Role-to-agent binding with responsibilities |
| router | Routing rule (task > agent group) |
| software_project | Complete software project definition |
| training_method | Model training/adaptation technique |

### P03 Prompt (21 kinds)

| Kind | Purpose |
|------|---------|
| action_prompt | Task prompt sent by human/orchestrator |
| chain | Chained prompt sequence (output A -> input B) |
| churn_prevention_playbook | Churn prevention with signal detection and intervention |
| constraint_spec | Constrained generation rules |
| context_file | Project-scoped instruction file auto-injected into context |
| context_window_config | Token budget allocation and overflow rules |
| expansion_play | Account expansion play: upsell/cross-sell |
| instruction | Step-by-step execution instructions |
| multimodal_prompt | Cross-modal prompt (vision/audio/text) |
| planning_strategy | Agent planning approach definition |
| prompt_compiler | Intent-to-artifact transmutation rules |
| prompt_optimizer | Automated prompt improvement tool |
| prompt_technique | Specific prompting method or pattern |
| prompt_template | Reusable template with {{vars}} |
| prompt_version | Versioned prompt snapshot |
| reasoning_strategy | Structured reasoning technique |
| reasoning_trace | Chain-of-thought with confidence scores |
| sales_playbook | Sales playbook with personas and objection handling |
| system_prompt | System prompt defining agent identity |
| tagline | Short brand phrase (taglines, slogans, headlines) |
| webinar_script | Webinar script with segments and speaker notes |

### P04 Tools (36 kinds)

| Kind | Purpose |
|------|---------|
| action_paradigm | How agents execute actions in environments |
| agent_name_service_record | Agent discovery registry record |
| api_client | Typed REST/GraphQL/gRPC API client |
| audio_tool | Speech-to-text, TTS, audio analysis |
| browser_tool | Browser automation: DOM, navigation, screenshots |
| cli_tool | CLI tool |
| code_executor | Sandboxed runtime for code execution |
| computer_use | Screen/keyboard/mouse control by LLM |
| daemon | Background process |
| db_connector | Database connector (SQL, GraphQL, REST-to-DB) |
| diff_strategy | Change application and matching algorithm |
| document_loader | File ingestion + chunking (PDF, HTML, CSV) |
| event_stream | Real-time ordered sequence of domain events for subscribers |
| function_def | LLM-callable function definition (JSON Schema) |
| hook | Pre/post processing hook |
| hook_config | Hook lifecycle configuration |
| mcp_app_extension | MCP Apps Extension (SEP-1865) |
| mcp_server | MCP server (tools + resources) |
| messaging_gateway | Unified multi-platform messaging transport abstraction |
| multi_modal_config | Multi-modal input format and routing rules |
| notifier | Push notification delivery (email, SMS, Slack) |
| plugin | Pluggable extension |
| research_pipeline | 7-stage research engine |
| retriever | Vector/keyword/hybrid search (RAG core) |
| sdk_example | SDK code example per language |
| search_strategy | Inference-time compute allocation |
| search_tool | Web, semantic, or hybrid search |
| skill | Reusable capability with trigger + phases |
| social_publisher | Auto-publishing agent (social media) |
| stt_provider | Speech-to-text provider |
| supabase_data_layer | Supabase data layer (tables, RLS, edge functions) |
| toolkit | Collection of callable tools with JSON Schema |
| tts_provider | Text-to-speech provider |
| vision_tool | Image analysis, OCR, screenshot interpretation |
| voice_pipeline | End-to-end voice agent architecture |
| webhook | HTTP event-driven endpoint (inbound/outbound) |

### P05 Output (23 kinds)

| Kind | Purpose |
|------|---------|
| analyst_briefing | Analyst briefing deck (Gartner/Forrester/IDC) |
| app_directory_entry | App directory entry for discovery |
| case_study | Customer case study (challenge/solution/outcome) |
| code_of_conduct | Community code of conduct |
| contributor_guide | CONTRIBUTING.md spec |
| course_module | Online course module with assessments |
| formatter | Output formatter (json, md, yaml) |
| github_issue_template | GitHub issue template (bug/feature/question) |
| integration_guide | Deep integration guide for partners |
| interactive_demo | Interactive product demo script |
| landing_page | Production-ready landing page (12 sections, responsive) |
| onboarding_flow | User onboarding with activation milestones |
| output_validator | Post-LLM output validation |
| parser | Output data extractor |
| partner_listing | Partner directory listing |
| pitch_deck | Sales pitch deck (problem/solution/traction/ask) |
| press_release | Press release (AP-style) |
| pricing_page | Pricing page with tier comparison |
| product_tour | In-app product tour walkthrough |
| quickstart_guide | Quickstart guide (under 5 minutes) |
| response_format | LLM response format definition |
| streaming_config | SSE/WebSocket streaming configuration |
| user_journey | End-to-end user journey map |

### P06 Schema (13 kinds)

| Kind | Purpose |
|------|---------|
| aggregate_root | DDD entry point entity enforcing domain invariants |
| api_reference | API reference doc (endpoints, params, auth) |
| data_contract | Schema-level agreement between data producer and consumer |
| edit_format | LLM-to-host file change format |
| enum_def | Reusable enumeration |
| event_schema | AsyncAPI/CloudEvents schema for event payloads |
| input_schema | Input contract |
| interface | Agent-to-agent integration contract |
| openapi_spec | Machine-readable API contract (OpenAPI 3.x) |
| type_def | Custom type definition |
| validation_schema | Post-generation validation contract |
| validator | Validation rule (pre-commit, quality gate) |
| value_object | Immutable typed value without identity |

### P07 Evaluation (25 kinds)

| Kind | Purpose |
|------|---------|
| benchmark | Performance measurement (latency, cost, quality) |
| benchmark_suite | Composite benchmark with multiple tasks |
| bias_audit | Fairness evaluation methodology |
| cohort_analysis | Cohort analysis for retention/LTV |
| curriculum_config | Training data ordering, difficulty scheduling, adaptive pacing |
| e2e_eval | End-to-end pipeline test |
| eval_dataset | Test case collection |
| eval_framework | Evaluation framework integration |
| eval_metric | Individual evaluation metric |
| experiment_tracker | Experiment config and results tracking |
| golden_test | Reference test case (quality 9.5+) |
| judge_config | LLM judge configuration |
| llm_evaluation_scenario | HELM evaluation scenario |
| llm_judge | LLM-as-Judge configuration |
| memory_benchmark | Memory system quality evaluation |
| red_team_eval | Adversarial test |
| regression_check | Baseline comparison |
| retrieval_evaluator | RAG-specific IR evaluation (MRR, NDCG, precision@k) |
| reward_model | Process/outcome reward model config |
| scoring_rubric | Evaluation criterion (5D, 12LP, custom) |
| smoke_eval | Quick sanity test (< 30s) |
| trace_config | Trace/span config for observability |
| trajectory_eval | Agent trajectory evaluation |
| unit_eval | Agent/prompt unit test |
| usage_report | Usage analytics report for billing |

### P08 Architecture (14 kinds)

| Kind | Purpose |
|------|---------|
| agent_card | Deployment spec for autonomous agent |
| agent_computer_interface | GUI/terminal interaction protocol |
| bounded_context | DDD boundary within which a domain model applies |
| capability_registry | Searchable catalog of all available agents |
| component_map | Component connectivity map |
| context_map | DDD diagram of bounded context relationships |
| decision_record | ADR: context, decision, consequences |
| diagram | Architecture diagram (ASCII or Mermaid) |
| dual_loop_architecture | Outer/inner loop agent control |
| fhir_agent_capability | HL7 FHIR R5 AI agent capability declaration |
| invariant | Inviolable operational law |
| naming_rule | Naming convention rule |
| pattern | Reusable pattern (e.g., continuous batching) |
| supervisor | Crew orchestrator for multiple builders |

### P09 Config (39 kinds)

| Kind | Purpose |
|------|---------|
| alert_rule | Observable threshold that triggers notification or response |
| backpressure_policy | Policy for when downstream cannot keep up with upstream |
| batch_config | Async batch processing config |
| canary_config | Gradual traffic rollout with automatic rollback triggers |
| circuit_breaker | Auto-disable failing dependencies with recovery cooldown |
| cost_budget | Token budget and spend tracking |
| data_residency | GDPR regional compliance config |
| deployment_manifest | Specification of artifacts to deploy and deployment config |
| effort_profile | Thinking level config for builder execution |
| env_config | Environment variables |
| experiment_config | A/B test and prompt experiment config |
| feature_flag | Feature flag (on/off, gradual rollout) |
| hibernation_policy | Policy for hibernating idle serverless workloads |
| inference_config | Inference-time parameters (temperature, top_p, sampling) |
| kubernetes_ai_requirement | CNCF Kubernetes AI Requirement (KAR) |
| marketplace_app_manifest | Marketplace app manifest (Claude/LangChain/HF) |
| oauth_app_config | OAuth2/PKCE app config |
| path_config | System paths |
| permission | Permission rule (read/write/execute) |
| playground_config | Interactive evaluation sandbox config |
| prosody_config | Voice personality and emotion settings |
| quantization_config | Model quantization and compression |
| rate_limit_config | Rate limiting (RPM, TPM, budget) |
| rbac_policy | Role-based access control for multi-tenant |
| realtime_session | Live bidirectional session config |
| retry_policy | Backoff, jitter, and budget config for retrying failed ops |
| runtime_rule | Runtime rule (timeouts, retries, limits) |
| sandbox_config | Isolated code execution environment |
| sandbox_spec | Enterprise pilot sandbox spec |
| secret_config | Secret management |
| slo_definition | Service level objective with target threshold and error budget |
| sso_config | SSO/SAML/OIDC identity provider config |
| terminal_backend | Abstract execution backend selectable at runtime |
| thinking_config | Extended thinking and budget tokens |
| tokenizer_config | BPE/sentencepiece/tiktoken tokenizer parameters |
| transport_config | Network transport for realtime communication |
| usage_quota | Usage quota and fair-use enforcement |
| vad_config | Voice activity detection settings |
| white_label_config | White-label/reseller configuration |

### P10 Memory (22 kinds)

| Kind | Purpose |
|------|---------|
| agent_grounding_record | Per-inference provenance record |
| c2pa_manifest | C2PA content credential for AI-generated media |
| compression_config | Context compression config for tool outputs |
| consolidation_policy | Memory lifecycle management policy |
| entity_memory | Entity-level memory |
| episodic_memory | Long-term store of past interactions indexed by episode |
| knowledge_index | Search index (BM25, FAISS config) |
| learning_record | Learning record (what worked/failed) |
| memory_architecture | Complete memory system design |
| memory_summary | Compressed memory summary |
| memory_type | Memory classification by source and decay |
| model_registry | Model versioning and artifact tracking |
| procedural_memory | Skill and procedure storage/retrieval |
| prompt_cache | Cached prompt TTL and eviction config |
| prospective_memory | Scheduled future actions and reminders for agents |
| runtime_state | Per-session runtime state |
| session_backend | Per-user session state persistence |
| session_state | Session state (ephemeral, snapshot) |
| user_model | Cross-session model of user preferences and working style |
| vc_credential | W3C Verifiable Credential for AI agent identity |
| workflow_run_crate | RO-Crate workflow execution provenance |
| working_memory | Short-term context store for a single active task |

### P11 Feedback (31 kinds)

| Kind | Purpose |
|------|---------|
| ab_test_config | A/B test experiment for conversion optimization |
| ai_rmf_profile | NIST AI RMF profile (GOVERN/MAP/MEASURE/MANAGE) |
| audit_log | Immutable audit log for SOC2 Type II |
| bugloop | Automatic correction loop (detect > fix > verify) |
| compliance_checklist | SOC2, GDPR, HIPAA, EU AI Act checklist |
| compliance_framework | Regulatory mapping and attestation |
| conformity_assessment | EU AI Act Annex IV conformity assessment |
| constitutional_rule | Absolute behavioral constraint that cannot be overridden |
| content_filter | Input/output content filtering pipeline |
| content_monetization | Content monetization pipeline config |
| curation_nudge | Periodic prompt to persist knowledge to durable memory |
| drift_detector | Monitor for distribution shift in model inputs/outputs |
| enterprise_sla | Enterprise SLA (uptime, latency, support) |
| gpai_technical_doc | EU AI Act GPAI technical documentation |
| guardrail | Safety restriction / safety boundary |
| hitl_config | Human-in-the-loop approval flow |
| incident_report | AI incident documentation and post-mortem |
| lifecycle_rule | Lifecycle rule (freshness, archive, promote) |
| nps_survey | NPS survey configuration |
| optimizer | Process optimizer (metric > action) |
| preference_dataset | Human-labeled preference pairs for RLHF/DPO training |
| quality_gate | Quality barrier (pass/fail with score) |
| referral_program | Referral program with viral coefficient |
| revision_loop_policy | Policy governing max revision iterations and escalation |
| reward_signal | Continuous quality signal |
| roi_calculator | ROI calculator with TCO comparison |
| safety_hazard_taxonomy | MLCommons hazard taxonomy (12 categories) |
| safety_policy | AI safety governance rules |
| self_improvement_loop | Agent self-evolution mechanism |
| subscription_tier | SaaS subscription tier (pricing + features) |
| threat_model | Structured hazard/risk assessment |

### P12 Orchestration (20 kinds)

| Kind | Purpose |
|------|---------|
| checkpoint | Workflow state snapshot |
| collaboration_pattern | Multi-agent coordination topology |
| crew_template | Reusable crew blueprint (roles, process, memory) |
| dag | Acyclic dependency graph |
| dispatch_rule | Dispatch rule (keyword > agent group) |
| domain_event | Immutable record of something significant in the domain |
| handoff | Handoff instruction (task + context + commit) |
| pipeline_template | Scenario-indexed agent pipeline recipe |
| process_manager | Event-driven coordinator for multi-step processes |
| renewal_workflow | Renewal workflow with stages and escalation |
| saga | Long-running distributed transaction with compensating actions |
| schedule | Temporal trigger for workflows |
| signal | Inter-agent signal (complete, error, progress) |
| spawn_config | Spawn configuration (solo, grid, continuous) |
| state_machine | Formal finite state machine with states and transitions |
| team_charter | Mission contract for a crew instance |
| visual_workflow | GUI-based workflow editor config |
| workflow | Workflow (sequential/parallel steps) |
| workflow_node | Typed node in visual/programmatic workflow |
| workflow_primitive | Workflow execution primitive (Step, Parallel, Loop) |

---

## Section 4: Builder Structure

Each kind has a builder at `archetypes/builders/{kind}-builder/` with 12 ISOs:

| ISO | File pattern | 8F stage | Purpose |
|-----|-------------|----------|---------|
| 1 | `bld_manifest_{kind}.md` | F2 BECOME | Builder identity and capabilities |
| 2 | `bld_instruction_{kind}.md` | F6 PRODUCE | Step-by-step build instructions |
| 3 | `bld_prompt_{kind}.md` | F3 INJECT | System prompt for the builder agent |
| 4 | `bld_scoring_{kind}.md` | F7 GOVERN | Quality scoring criteria |
| 5 | `bld_template_{kind}.md` | F6 PRODUCE | Output template with placeholders |
| 6 | `bld_examples_{kind}.md` | F7 GOVERN | Golden + anti examples |
| 7 | `bld_knowledge_card_{kind}.md` | F3 INJECT | Domain knowledge for the kind |
| 8 | `bld_schema_{kind}.md` | F1 CONSTRAIN | Frontmatter schema definition |
| 9 | `bld_quality_gate_{kind}.md` | F7 GOVERN | Hard gates (H01-H07) |
| 10 | `bld_architecture_{kind}.md` | F1 CONSTRAIN | Structural constraints and patterns |
| 11 | `bld_feedback_{kind}.md` | F7 GOVERN | Feedback loops and improvement signals |
| 12 | `bld_orchestration_{kind}.md` | F8 COLLABORATE | Cross-builder coordination rules |

**Build command**: `python _tools/cex_8f_runner.py "intent" --kind {kind} --execute`

**301 builders** exist today (300 kind-specific + 2 meta-builders).

---

## Section 5: The 8 Nuclei

| Nucleus | Role | Sin lens | Model | When to use |
|---------|------|----------|-------|-------------|
| N00 | Genesis | (archetype -- no sin) | -- | Template for new nuclei; /mentor source |
| N01 | Intelligence | Analytical Envy | Opus | Research, analysis, competitive intel |
| N02 | Marketing | Creative Lust | Opus | Copy, campaigns, content, brand voice |
| N03 | Engineering | Inventive Pride | Opus | Build artifacts, code, architecture |
| N04 | Knowledge | Knowledge Gluttony | Opus | Documentation, RAG, knowledge cards |
| N05 | Operations | Gating Wrath | Opus | Testing, deployment, CI/CD, tooling |
| N06 | Commercial | Strategic Greed | Opus | Pricing, sales, monetization, funnels |
| N07 | Orchestrator | Orchestrating Sloth | Opus | Dispatch, wave planning, mission control |

**Routing heuristic**: if the task is about WHAT to build, route to the domain nucleus.
If it is about HOW to build, route to N03. If it is about TESTING, route to N05.
If it is about SELLING, route to N06. If it crosses domains, N07 orchestrates.

---

## Quick Reference

| Stat | Value |
|------|-------|
| Total kinds | 300 |
| Total pillars | 12 (P01-P12) |
| Total nuclei | 8 (N00-N07) |
| Total builders | 302 |
| ISOs per builder | 12 |
| Total ISOs | 3,647 |
| Pipeline steps | 8 (F1-F8) + 3 sub-steps (F3b, F3c, F7b) |
| Quality floor | 8.0 |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_project_overview]] | related | 0.36 |
| [[agent_card_engineering_nucleus]] | downstream | 0.35 |
| [[agent_card_n04]] | sibling | 0.34 |
| [[bld_collaboration_kind]] | downstream | 0.33 |
| [[agent_card_n03]] | sibling | 0.33 |
| [[skill]] | downstream | 0.32 |
| [[spec_cex_system_map]] | sibling | 0.31 |
| [[ctx_cex_new_dev_guide]] | sibling | 0.31 |
| [[spec_mission_100pct_coverage]] | downstream | 0.31 |
| [[p03_sp_n03_creation_nucleus]] | downstream | 0.31 |
