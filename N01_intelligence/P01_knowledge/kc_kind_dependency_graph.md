---
id: kc_kind_dependency_graph
kind: knowledge_card
pillar: P01
nucleus: n01
title: "Kind Dependency Graph -- Cross-Kind Build Order for 293 Kinds"
version: 1.0.0
created: 2026-04-18
author: n01_intelligence
domain: cex-architecture
quality: 8.9
tags: [dependency_graph, kinds, build_order, architecture, critical_path]
tldr: "Which kinds must exist before a given kind can be built. Full dependency graph for all 293 CEX kinds organized by pillar."
density_score: null
related:
  - bld_architecture_citation
  - bld_architecture_knowledge_card
  - bld_architecture_agent
  - bld_architecture_rag_source
  - p06_schema_taxonomy
  - p01_kc_context_doc
  - bld_architecture_context_doc
  - p01_kc_knowledge_card
  - bld_architecture_system_prompt
  - p01_kc_agent
---

# Kind Dependency Graph

## Overview

Every CEX kind has upstream dependencies -- other kinds that must be produced first.
This KC maps those relationships so orchestrators can sequence builds correctly,
detect circular risks, and identify critical path bottlenecks.

**Notation**: `depends_on` = must exist before this kind is buildable.
`optional_deps` = enriches quality but not strictly required.
`circular_risk` = kinds that could form dependency cycles if not managed.

---

## P01 Knowledge Layer

| Kind | depends_on | optional_deps | circular_risk |
|------|-----------|---------------|---------------|
| knowledge_card | rag_source | glossary_entry, citation | none |
| glossary_entry | rag_source | knowledge_card | knowledge_card (mutual) |
| context_doc | rag_source, knowledge_card | glossary_entry | none |
| citation | rag_source, search_tool | knowledge_card | none |
| chunk_strategy | rag_source | knowledge_card | none |
| embedding_config | chunk_strategy | knowledge_card | none |
| rag_source | (none -- leaf) | search_tool, browser_tool | none |
| document_loader | rag_source | chunk_strategy | none |
| dataset_card | rag_source, knowledge_card | citation | none |
| ontology | knowledge_card, glossary_entry | domain_vocabulary | domain_vocabulary (mutual) |
| domain_vocabulary | glossary_entry, ontology | knowledge_card | ontology (mutual) |
| knowledge_graph | document_loader, entity_memory | embedding_config, retriever_config | entity_memory |
| axiom | knowledge_card | glossary_entry | none |
| mental_model | knowledge_card, axiom | ontology | none |
| agentic_rag | rag_source, embedding_config, retriever_config | chunk_strategy, knowledge_index | none |
| context_map | knowledge_card, context_doc | ontology | none |
| repo_map | context_doc, knowledge_card | component_map | none |
| analyst_briefing | knowledge_card, context_doc | citation, competitive_matrix | none |
| competitive_matrix | knowledge_card | citation, rag_source | none |
| case_study | knowledge_card, context_doc | citation | none |
| research_pipeline | rag_source, search_tool | knowledge_card, citation | none |

---

## P02 Model Layer

| Kind | depends_on | optional_deps | circular_risk |
|------|-----------|---------------|---------------|
| agent | system_prompt, input_schema | boot_config, agent_card | agent_card (mutual) |
| agent_card | agent, boot_config | permission, path_config, law | agent (must precede) |
| boot_config | agent, env_config | mental_model, agent_card | none |
| agent_package | agent, system_prompt, boot_config | skill, output_validator | none |
| agent_profile | agent, agent_card | context_doc | none |
| agent_computer_interface | agent, agent_card | input_schema, output_validator | none |
| agent_grounding_record | agent, citation | knowledge_card | none |
| agent_name_service_record | agent, agent_card | registry config | none |
| model_provider | env_config, secret_config | rate_limit_config | none |
| model_card | model_provider, knowledge_card | benchmark, bias_audit | none |
| model_registry | model_provider, model_card | benchmark | none |
| model_architecture | knowledge_card | diagram, decision_record | none |
| lens | agent | system_prompt | none |
| personality | system_prompt, agent | knowledge_card | none |
| nucleus_def | agent, agent_card, boot_config | capability_registry | none |
| capability_registry | agent_card, nucleus_def | role_assignment | none |
| role_assignment | agent, agent_card | capability_registry | none |
| fallback_chain | model_provider | rate_limit_config | none |
| supervisor | agent, agent_card, workflow | dispatch_rule | none |

---

## P03 Prompt Layer

| Kind | depends_on | optional_deps | circular_risk |
|------|-----------|---------------|---------------|
| prompt_template | few_shot_example | constraint_spec, prompt_version | none |
| action_prompt | prompt_template | constraint_spec | none |
| system_prompt | prompt_template, knowledge_card | few_shot_example, constraint_spec | none |
| chain | action_prompt, prompt_template | constraint_spec | none |
| few_shot_example | knowledge_card | rag_source | none |
| instruction | prompt_template | knowledge_card | none |
| multimodal_prompt | prompt_template | few_shot_example | none |
| context_window_config | prompt_template, knowledge_card | memory_scope | none |
| prompt_version | prompt_template | scoring_rubric | none |
| prompt_cache | prompt_template, knowledge_index | context_window_config | none |
| prompt_compiler | prompt_template, knowledge_card | ontology, glossary_entry | none |
| prompt_optimizer | prompt_template, scoring_rubric | benchmark, eval_dataset | none |
| prompt_technique | knowledge_card, few_shot_example | prompt_template | none |
| action_paradigm | prompt_template, knowledge_card | system_prompt | none |
| context_file | context_doc, prompt_template | knowledge_card | none |
| tagline | knowledge_card | prompt_template | none |
| agents_md | agent_card, prompt_template | system_prompt | none |

---

## P04 Tools Layer

| Kind | depends_on | optional_deps | circular_risk |
|------|-----------|---------------|---------------|
| search_tool | env_config | rate_limit_config, secret_config | none |
| browser_tool | env_config | secret_config | none |
| cli_tool | env_config, path_config | secret_config | none |
| api_client | env_config, secret_config | rate_limit_config, input_schema | none |
| db_connector | env_config, secret_config | input_schema | none |
| mcp_server | env_config, secret_config | input_schema, output_validator | none |
| mcp_app_extension | mcp_server | env_config | none |
| webhook | env_config, secret_config | input_schema, rate_limit_config | none |
| document_loader | env_config | path_config | none |
| code_executor | env_config, secret_config | sandbox_config | none |
| audio_tool | env_config | secret_config | none |
| vision_tool | env_config | model_provider | none |
| toolkit | (none -- leaf, aggregates tools) | search_tool, browser_tool, cli_tool | none |
| computer_use | env_config, browser_tool | agent_card | none |
| messaging_gateway | env_config, secret_config | rate_limit_config, webhook | none |
| notifier | env_config, messaging_gateway | webhook | none |
| skill | prompt_template | input_schema | none |
| plugin | env_config, api_client | input_schema | none |
| social_publisher | api_client, secret_config | rate_limit_config | none |

---

## P05 Output Layer

| Kind | depends_on | optional_deps | circular_risk |
|------|-----------|---------------|---------------|
| formatter | prompt_template, type_def | response_format | none |
| parser | type_def, input_schema | formatter | none |
| response_format | type_def | validation_schema | none |
| output_validator | validation_schema, type_def | scoring_rubric | none |
| diagram | knowledge_card, context_doc | component_map | none |
| landing_page | knowledge_card, prompt_template | tagline | none |
| pricing_page | content_monetization, knowledge_card | landing_page | none |
| press_release | knowledge_card, context_doc | tagline | none |
| pitch_deck | knowledge_card, competitive_matrix | case_study | none |
| webinar_script | knowledge_card, prompt_template | few_shot_example | none |
| app_directory_entry | agent_card, knowledge_card | api_reference | none |
| api_reference | api_client, input_schema | openapi_spec | none |
| openapi_spec | api_client, input_schema, type_def | validation_schema | none |
| quickstart_guide | knowledge_card, context_doc | api_reference | none |
| integration_guide | api_client, knowledge_card | openapi_spec | none |
| contributor_guide | knowledge_card, context_doc | code_of_conduct | none |
| interactive_demo | prompt_template, knowledge_card | landing_page | none |
| product_tour | landing_page, knowledge_card | prompt_template | none |
| partner_listing | knowledge_card, context_doc | api_reference | none |
| marketplace_app_manifest | agent_card, api_client | openapi_spec, oauth_app_config | none |

---

## P06 Schema Layer

| Kind | depends_on | optional_deps | circular_risk |
|------|-----------|---------------|---------------|
| type_def | enum_def | knowledge_card | none |
| enum_def | (none -- leaf) | knowledge_card | none |
| input_schema | type_def, enum_def | knowledge_card | none |
| validation_schema | type_def, enum_def | input_schema | none |
| interface | input_schema, enum_def | type_def | none |
| data_contract | input_schema, interface, type_def | validation_schema | none |
| function_def | input_schema, type_def | output_validator | none |
| constraint_spec | type_def | knowledge_card | none |
| invariant | constraint_spec, type_def | knowledge_card | none |
| aggregate_root | type_def, domain_event | knowledge_card | domain_event |
| domain_event | type_def, aggregate_root | knowledge_card | aggregate_root (mutual) |
| value_object | type_def | knowledge_card | none |
| bounded_context | knowledge_card, domain_vocabulary | ontology, aggregate_root | none |

---

## P07 Evaluation Layer

| Kind | depends_on | optional_deps | circular_risk |
|------|-----------|---------------|---------------|
| scoring_rubric | knowledge_card | golden_test | none |
| quality_gate | scoring_rubric | reward_signal | none |
| benchmark | eval_dataset, scoring_rubric | golden_test | none |
| benchmark_suite | benchmark | eval_dataset | none |
| eval_dataset | knowledge_card, rag_source | few_shot_example | none |
| eval_framework | scoring_rubric, eval_dataset | benchmark | none |
| llm_judge | scoring_rubric, golden_test | eval_dataset | none |
| golden_test | knowledge_card, few_shot_example | scoring_rubric | none |
| unit_eval | scoring_rubric, input_schema | golden_test | none |
| e2e_eval | workflow, scoring_rubric | benchmark | none |
| smoke_eval | env_config, scoring_rubric | quality_gate | none |
| red_team_eval | knowledge_card, scoring_rubric | eval_dataset, guardrail | none |
| bias_audit | eval_dataset, knowledge_card | scoring_rubric | none |
| ai_rmf_profile | knowledge_card, scoring_rubric | bias_audit, guardrail | none |
| llm_evaluation_scenario | knowledge_card, eval_dataset | scoring_rubric | none |
| trajectory_eval | workflow, scoring_rubric | eval_dataset | none |
| judge_config | llm_judge, scoring_rubric | quality_gate | none |
| preference_dataset | eval_dataset, scoring_rubric | golden_test | none |
| reward_model | preference_dataset, scoring_rubric | eval_dataset | none |
| reward_signal | scoring_rubric, quality_gate | reward_model | none |
| conformity_assessment | knowledge_card, scoring_rubric | compliance_checklist | none |
| gpai_technical_doc | knowledge_card, ai_rmf_profile | scoring_rubric | none |

---

## P08 Architecture Layer

| Kind | depends_on | optional_deps | circular_risk |
|------|-----------|---------------|---------------|
| component_map | knowledge_card, context_doc | diagram | none |
| decision_record | knowledge_card | context_doc | none |
| naming_rule | knowledge_card | glossary_entry | none |
| diagram | knowledge_card | component_map | none |
| context_map | knowledge_card, context_doc | ontology | none |
| bounded_context | knowledge_card, domain_vocabulary | context_map | none |
| interface | input_schema | type_def | none |
| agent_card | agent, boot_config | permission, path_config | none |
| capability_registry | agent_card, nucleus_def | role_assignment | none |
| nucleus_def | agent, agent_card | capability_registry | none |
| threat_model | knowledge_card, component_map | scoring_rubric, guardrail | none |
| safety_hazard_taxonomy | knowledge_card | threat_model | none |
| api_reference | api_client, input_schema | openapi_spec | none |
| repo_map | context_doc, knowledge_card | component_map | none |
| software_project | knowledge_card, decision_record | component_map | none |
| collaboration_pattern | knowledge_card | workflow, crew_template | none |
| edit_format | knowledge_card, prompt_template | formatter | none |

---

## P09 Config Layer

| Kind | depends_on | optional_deps | circular_risk |
|------|-----------|---------------|---------------|
| env_config | (none -- leaf) | path_config | none |
| secret_config | env_config, permission | path_config | none |
| path_config | env_config | naming_rule | none |
| rate_limit_config | env_config, secret_config | feature_flag | none |
| feature_flag | env_config, permission | rate_limit_config | none |
| batch_config | env_config, spawn_config | rate_limit_config | none |
| streaming_config | env_config | rate_limit_config | none |
| thinking_config | env_config, model_provider | prompt_template | none |
| quantization_config | env_config, model_provider | model_card | none |
| finetune_config | eval_dataset, model_provider | scoring_rubric | none |
| boot_config | agent, env_config | agent_card | none |
| sandbox_config | env_config | secret_config | none |
| sandbox_spec | sandbox_config | env_config | none |
| sso_config | env_config, secret_config | permission, rbac_policy | none |
| oauth_app_config | env_config, secret_config | rate_limit_config | none |
| transport_config | env_config | secret_config | none |
| compression_config | env_config | transport_config | none |
| backpressure_policy | rate_limit_config, env_config | circuit_breaker | none |
| circuit_breaker | rate_limit_config, retry_policy | backpressure_policy | backpressure_policy |
| retry_policy | env_config | rate_limit_config | circuit_breaker |
| canary_config | env_config, deployment_manifest | feature_flag | none |
| deployment_manifest | env_config, agent_card | spawn_config, secret_config | none |
| terminal_backend | env_config, secret_config | sandbox_config | none |
| hibernation_policy | env_config | rate_limit_config | none |
| ab_test_config | feature_flag, env_config | scoring_rubric | none |
| experiment_config | env_config, scoring_rubric | feature_flag | none |
| realtime_session | env_config, streaming_config | rate_limit_config | none |
| vad_config | env_config, audio_tool | realtime_session | none |
| prosody_config | env_config, audio_tool | tts_provider | none |

---

## P10 Memory Layer

| Kind | depends_on | optional_deps | circular_risk |
|------|-----------|---------------|---------------|
| knowledge_index | embedding_config, rag_source | chunk_strategy | none |
| entity_memory | rag_source, context_doc | knowledge_index, retriever_config | none |
| memory_summary | session_state, learning_record | action_prompt | none |
| episodic_memory | session_state | entity_memory | none |
| procedural_memory | knowledge_card, skill | entity_memory | none |
| prospective_memory | schedule, knowledge_card | entity_memory | none |
| working_memory | session_state | memory_summary | none |
| memory_scope | context_window_config | knowledge_index | none |
| memory_type | knowledge_card | memory_scope | none |
| memory_architecture | knowledge_card, component_map | entity_memory, knowledge_index | none |
| memory_benchmark | benchmark, eval_dataset | knowledge_index | none |
| session_backend | env_config, secret_config | session_state | none |
| session_state | env_config | session_backend | none |
| user_model | entity_memory, learning_record | knowledge_card | none |
| retriever | knowledge_index, embedding_config | retriever_config | none |
| retriever_config | embedding_config, knowledge_index | chunk_strategy | none |
| reranker_config | retriever_config | scoring_rubric | none |
| graph_rag_config | knowledge_graph, embedding_config | retriever_config | none |
| vector_store | embedding_config | knowledge_index | none |
| embedder_provider | env_config, model_provider | secret_config | none |
| diff_strategy | knowledge_card | context_window_config | none |
| chunk_strategy | rag_source | knowledge_card | none |
| prompt_cache | prompt_template, knowledge_index | context_window_config | none |

---

## P11 Feedback Layer

| Kind | depends_on | optional_deps | circular_risk |
|------|-----------|---------------|---------------|
| quality_gate | scoring_rubric | reward_signal | none |
| guardrail | knowledge_card, safety_policy | threat_model | none |
| safety_policy | knowledge_card | safety_hazard_taxonomy | none |
| bugloop | quality_gate, guardrail | learning_record, signal | none |
| learning_record | session_state | memory_summary | none |
| regression_check | benchmark, eval_dataset | golden_test, quality_gate | none |
| content_filter | knowledge_card, guardrail | safety_policy | none |
| reward_signal | scoring_rubric, quality_gate | reward_model | none |
| lifecycle_rule | quality_gate | knowledge_card | none |
| self_improvement_loop | bugloop, learning_record | reward_signal | none |
| drift_detector | benchmark, regression_check | eval_dataset | none |
| revision_loop_policy | quality_gate, scoring_rubric | retry_policy | none |
| content_monetization | knowledge_card, customer_segment | pricing_page | none |
| curation_nudge | knowledge_card, prompt_template | entity_memory | none |
| consolidation_policy | knowledge_card | quality_gate | none |
| bias_audit | eval_dataset, scoring_rubric | knowledge_card | none |

---

## P12 Orchestration Layer

| Kind | depends_on | optional_deps | circular_risk |
|------|-----------|---------------|---------------|
| workflow | handoff, dag | spawn_config, checkpoint, quality_gate | none |
| dispatch_rule | signal, handoff | spawn_config | none |
| handoff | dag | dispatch_rule, session_state | none |
| dag | (none -- leaf) | workflow | none |
| spawn_config | handoff, agent_card | env_config | none |
| signal | workflow, bugloop | dispatch_rule, checkpoint | none |
| checkpoint | workflow, signal | quality_gate | none |
| schedule | (none -- leaf) | dispatch_rule | none |
| crew_template | role_assignment, capability_registry | team_charter | none |
| role_assignment | agent, agent_card | capability_registry | none |
| team_charter | crew_template, role_assignment | quality_gate | none |
| process_manager | spawn_config, workflow | signal | none |
| runtime_state | session_state, signal | workflow | none |
| runtime_rule | env_config, feature_flag | constraint_spec | none |
| pipeline_template | workflow, handoff | dispatch_rule | none |
| planning_strategy | knowledge_card, dag | workflow | none |
| visual_workflow | workflow, diagram | component_map | none |
| workflow_node | prompt_template, input_schema | type_def | none |
| workflow_primitive | workflow_node | workflow | none |
| workflow_run_crate | workflow, eval_dataset | scoring_rubric | none |
| dual_loop_architecture | workflow, learning_record | quality_gate | none |
| saga | workflow, state_machine | signal, checkpoint | none |
| state_machine | (none -- leaf) | workflow | none |
| effort_profile | knowledge_card | scoring_rubric | none |
| audit_log | workflow, signal | knowledge_card | none |
| lineage_record | workflow, knowledge_card | citation | none |

---

## Cross-Pillar Kinds (Vertical and Domain)

| Kind | depends_on | optional_deps | circular_risk |
|------|-----------|---------------|---------------|
| permission | env_config | rbac_policy, law | none |
| rbac_policy | permission | env_config | none |
| law | knowledge_card | compliance_checklist | none |
| compliance_checklist | knowledge_card | law, scoring_rubric | none |
| compliance_framework | compliance_checklist, knowledge_card | law | none |
| code_of_conduct | knowledge_card | glossary_entry | none |
| github_issue_template | knowledge_card, context_doc | scoring_rubric | none |
| changelog | knowledge_card, decision_record | context_doc | none |
| faq_entry | knowledge_card | glossary_entry | none |
| data_residency | knowledge_card, env_config | compliance_checklist | none |
| c2pa_manifest | knowledge_card, citation | vc_credential | none |
| vc_credential | knowledge_card | data_contract | none |

---

## Domain/Vertical Kinds

| Kind | depends_on | optional_deps | circular_risk |
|------|-----------|---------------|---------------|
| healthcare_vertical | knowledge_card, compliance_checklist | fhir_agent_capability | none |
| fhir_agent_capability | agent_card, knowledge_card | compliance_checklist | none |
| fintech_vertical | knowledge_card, compliance_checklist | guardrail | none |
| edtech_vertical | knowledge_card, course_module | scoring_rubric | none |
| govtech_vertical | knowledge_card, compliance_checklist | law | none |
| legal_vertical | knowledge_card, law | compliance_checklist | none |
| ecommerce_vertical | knowledge_card, content_monetization | landing_page | none |
| kubernetes_ai_requirement | env_config, deployment_manifest | knowledge_card | none |

---

## Business/Revenue Kinds

| Kind | depends_on | optional_deps | circular_risk |
|------|-----------|---------------|---------------|
| customer_segment | knowledge_card, context_doc | competitive_matrix | none |
| cohort_analysis | eval_dataset, knowledge_card | scoring_rubric | none |
| churn_prevention_playbook | knowledge_card, customer_segment | cohort_analysis | none |
| expansion_play | knowledge_card, customer_segment | content_monetization | none |
| referral_program | knowledge_card, content_monetization | customer_segment | none |
| nps_survey | knowledge_card, customer_segment | eval_dataset | none |
| subscription_tier | content_monetization, knowledge_card | pricing_page | none |
| roi_calculator | knowledge_card, scoring_rubric | content_monetization | none |
| sales_playbook | knowledge_card, customer_segment | competitive_matrix | none |
| discovery_questions | knowledge_card, customer_segment | prompt_template | none |
| onboarding_flow | knowledge_card, customer_segment | prompt_template | none |
| renewal_workflow | workflow, customer_segment | knowledge_card | none |
| white_label_config | env_config, knowledge_card | brand config | none |
| enterprise_sla | knowledge_card, data_contract | compliance_checklist | none |
| cost_budget | knowledge_card, env_config | rate_limit_config | none |
| usage_quota | rate_limit_config, knowledge_card | cost_budget | none |
| usage_report | audit_log, knowledge_card | scoring_rubric | none |
| course_module | knowledge_card | prompt_template | none |

---

## LLM/ML Training Kinds

| Kind | depends_on | optional_deps | circular_risk |
|------|-----------|---------------|---------------|
| training_method | knowledge_card, eval_dataset | scoring_rubric | none |
| rl_algorithm | reward_model, reward_signal | training_method | none |
| reasoning_strategy | knowledge_card, prompt_technique | few_shot_example | none |
| reasoning_trace | knowledge_card | reasoning_strategy | none |
| learning_record | session_state | memory_summary | none |
| experiment_tracker | experiment_config, eval_dataset | scoring_rubric | none |

---

## Voice/Multimodal Kinds

| Kind | depends_on | optional_deps | circular_risk |
|------|-----------|---------------|---------------|
| tts_provider | env_config, model_provider | secret_config | none |
| stt_provider | env_config, model_provider | secret_config | none |
| voice_pipeline | tts_provider, stt_provider | vad_config, realtime_session | none |
| multi_modal_config | env_config, model_provider | vision_tool, audio_tool | none |

---

## Top 10 Critical Path Chains

Critical paths are sequences where each kind must be built before the next.
These are the "spine" of any CEX deployment.

### Chain 1: RAG Knowledge Pipeline (P01 + P10)
```
rag_source -> chunk_strategy -> embedding_config -> knowledge_index -> retriever_config -> agentic_rag
```
**Why critical**: Every knowledge retrieval system requires this spine. No RAG without embeddings; no embeddings without chunks; no chunks without source.

### Chain 2: Agent Deployment Stack (P02 + P09 + P12)
```
env_config -> agent -> system_prompt -> boot_config -> agent_card -> spawn_config -> workflow
```
**Why critical**: An agent cannot boot without env config; cannot have identity without system_prompt; cannot be dispatched without agent_card + spawn_config.

### Chain 3: Prompt Engineering Pipeline (P03)
```
knowledge_card -> few_shot_example -> prompt_template -> action_prompt -> chain -> system_prompt
```
**Why critical**: Every prompt builds on domain knowledge. Templates precede actions; actions precede chains.

### Chain 4: Quality Gate Pipeline (P07 + P11)
```
knowledge_card -> scoring_rubric -> quality_gate -> bugloop -> learning_record
```
**Why critical**: Cannot gate without rubric; cannot auto-fix without gate; cannot improve without records.

### Chain 5: Multi-Agent Orchestration (P02 + P12)
```
role_assignment -> capability_registry -> crew_template -> team_charter -> workflow -> signal
```
**Why critical**: Crew requires defined roles; roles require capability index; charters instantiate crews; workflows execute them.

### Chain 6: Security/Compliance Stack (P09 + P11)
```
knowledge_card -> safety_policy -> guardrail -> content_filter -> threat_model -> compliance_checklist
```
**Why critical**: All compliance artifacts derive from policy; policy requires knowledge; guardrails reference policy.

### Chain 7: Evaluation Pipeline (P07)
```
knowledge_card -> eval_dataset -> golden_test -> scoring_rubric -> llm_judge -> benchmark -> regression_check
```
**Why critical**: Cannot benchmark without golden reference; cannot judge without rubric; regression requires baseline benchmark.

### Chain 8: Schema Data Contract (P06)
```
enum_def -> type_def -> input_schema -> interface -> data_contract -> validation_schema -> output_validator
```
**Why critical**: Types flow upward -- enums are atomic leaves; contracts require complete interfaces.

### Chain 9: Memory Persistence Stack (P10)
```
session_state -> entity_memory -> knowledge_index -> retriever_config -> memory_architecture
```
**Why critical**: Memory cannot be retrieved without an index; index requires entities; entities emerge from session.

### Chain 10: Mission Orchestration (N07 workflow, P12)
```
dag -> handoff -> dispatch_rule -> spawn_config -> workflow -> checkpoint -> signal -> audit_log
```
**Why critical**: Full N07 mission lifecycle. Each step gates the next; no workflow without dispatch; no dispatch without handoff.

---

## Leaf Kinds (no upstream dependencies)

These kinds have no required predecessors and can be built first:

| Kind | Pillar | Notes |
|------|--------|-------|
| rag_source | P01 | Root of all knowledge |
| enum_def | P06 | Atomic type primitive |
| env_config | P09 | Root of all config |
| dag | P12 | Root of orchestration graphs |
| schedule | P12 | Standalone temporal trigger |
| state_machine | P12 | Abstract flow definition |
| knowledge_card | P01 | Can be written from domain knowledge alone |
| glossary_entry | P01 | Can be written from domain knowledge alone |

---

## Circular Risk Registry

Monitored pairs where back-references must be managed via version sequencing:

| Pair | Direction | Resolution |
|------|-----------|------------|
| aggregate_root <-> domain_event | mutual reference | Build aggregate_root stub first, domain_event second, then enrich aggregate_root |
| ontology <-> domain_vocabulary | mutual enrichment | Build ontology first, domain_vocabulary second, cross-link afterward |
| knowledge_card <-> glossary_entry | mutual enrichment | Not a true cycle -- both can be built independently; links added post-creation |
| circuit_breaker <-> backpressure_policy | mutual config | Build retry_policy first, then both in parallel |
| agent <-> agent_card | sequential | Agent must precede agent_card (card describes the agent) |
| benchmark <-> regression_check | sequential | Benchmark creates baseline; regression references it -- no cycle |

---

## Summary Statistics

| Pillar | Kinds | Avg depends_on | Max depth |
|--------|-------|----------------|-----------|
| P01 Knowledge | 21 | 1.4 | 3 |
| P02 Model | 19 | 2.1 | 4 |
| P03 Prompt | 17 | 1.6 | 4 |
| P04 Tools | 19 | 1.3 | 2 |
| P05 Output | 20 | 1.8 | 3 |
| P06 Schema | 13 | 1.5 | 3 |
| P07 Evaluation | 22 | 2.0 | 4 |
| P08 Architecture | 17 | 1.7 | 3 |
| P09 Config | 29 | 1.6 | 3 |
| P10 Memory | 23 | 1.9 | 4 |
| P11 Feedback | 16 | 1.9 | 4 |
| P12 Orchestration | 26 | 1.8 | 5 |
| Cross-pillar/Domain | 31 | 1.5 | 3 |
| **Total** | **293** | **1.7 avg** | **5 max** |

**Root (leaf) kinds**: 8 -- env_config, rag_source, enum_def, dag, schedule, state_machine, knowledge_card, glossary_entry

**Highest-fanout kinds** (most things depend on them):
1. knowledge_card -- 78+ downstream consumers
2. env_config -- 62+ downstream consumers
3. rag_source -- 41+ downstream consumers
4. scoring_rubric -- 38+ downstream consumers
5. type_def -- 31+ downstream consumers

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_citation]] | downstream | 0.24 |
| [[bld_architecture_knowledge_card]] | downstream | 0.22 |
| [[bld_architecture_agent]] | downstream | 0.21 |
| [[bld_architecture_rag_source]] | downstream | 0.20 |
| [[p06_schema_taxonomy]] | downstream | 0.20 |
| [[p01_kc_context_doc]] | sibling | 0.19 |
| [[bld_architecture_context_doc]] | downstream | 0.19 |
| [[p01_kc_knowledge_card]] | sibling | 0.18 |
| [[bld_architecture_system_prompt]] | downstream | 0.18 |
| [[p01_kc_agent]] | sibling | 0.18 |
