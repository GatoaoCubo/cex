---
id: knowledge_graph_cex_taxonomy
kind: knowledge_graph
8f: F3_inject
pillar: P10
nucleus: N01
title: CEX Taxonomy Knowledge Graph
version: "1.0"
quality: 8.3
density_score: 0.97
tags: [taxonomy, knowledge-graph, cex-core, cross-synthesis, 257-kinds, 12-pillars, 8-nuclei]
created: 2026-04-17
updated: 2026-04-17
source: .cex/kinds_meta.json + N01 artifact scan (VERTICAL_DENSIFICATION W2)
related:
  - bld_knowledge_card_nucleus_def
  - kc_intent_resolution_map
  - spec_mission_100pct_coverage
  - agent_card_n03
  - p03_pc_cex_universal
  - p08_pat_nucleus_fractal
  - p01_kc_cex_project_overview
  - p10_entity_cex_system
  - bld_sp_collaboration_software_project
  - p01_kg_cex_system_architecture
---

## Overview

Knowledge graph of the CEX typed knowledge system. 257 kind-nodes + 12 pillar-nodes + 8 nucleus-nodes = 277 nodes total.
Edge types: `HAS_PILLAR`, `ROUTES_TO`, `GOVERNS` (by LLM function), `CO_OCCURS` (kinds built together).

Representation: adjacency tables + pillar cluster listing. Machine-readable for graph traversal.

---

## Node Index

### Nucleus Nodes (8)

| Node | ID | Role | Sin | Tier |
|------|----|------|-----|------|
| N00 | n00_genesis | Archetype | pre-sin | Sonnet |
| N01 | n01_intelligence | Research | Analytical Envy | Sonnet |
| N02 | n02_marketing | Marketing | Creative Lust | Sonnet |
| N03 | n03_engineering | Build/Create | Inventive Pride | Opus |
| N04 | n04_knowledge | Knowledge/Docs | Knowledge Gluttony | Sonnet |
| N05 | n05_operations | Code/Test/Deploy | Gating Wrath | Sonnet |
| N06 | n06_commercial | Brand/Monetize | Strategic Greed | Sonnet |
| N07 | n07_admin | Orchestration | Orchestrating Sloth | Opus |

### Pillar Nodes (12)

| Node | ID | Domain | Kind Count | Primary Nucleus |
|------|----|--------|-----------|----------------|
| P01 | p01_knowledge | Storage, retrieval, KCs | 28 | N04 |
| P02 | p02_model | Agent definitions, providers | 22 | N03 |
| P03 | p03_prompt | Templates, actions, chains | 20 | N03 |
| P04 | p04_tools | External capabilities | 34 | N05 |
| P05 | p05_output | Production artifacts | 23 | N03 |
| P06 | p06_schema | Data contracts | 8 | N03 |
| P07 | p07_evals | Quality, scoring, testing | 23 | N05 |
| P08 | p08_architecture | System structure | 12 | N03 |
| P09 | p09_config | Runtime settings | 28 | N05 |
| P10 | p10_memory | State, context, indexing | 18 | N04 |
| P11 | p11_feedback | Learning, correction | 26 | N05/N06 |
| P12 | p12_orchestration | Workflows, dispatch | 15 | N07 |

---

## Pillar Clusters (HAS_PILLAR edges)

### P01 Knowledge (28 kinds)
```
agentic_rag, changelog, chunk_strategy, citation, competitive_matrix,
context_doc, dataset_card, discovery_questions, ecommerce_vertical,
edtech_vertical, embedder_provider, embedding_config, faq_entry,
few_shot_example, fintech_vertical, glossary_entry, govtech_vertical,
graph_rag_config, healthcare_vertical, knowledge_card, knowledge_graph,
legal_vertical, ontology, rag_source, repo_map, reranker_config,
retriever_config, vector_store
```

### P02 Model (22 kinds)
```
agent, agent_package, agent_profile, agents_md, axiom, boot_config,
customer_segment, fallback_chain, finetune_config, handoff_protocol,
lens, memory_scope, mental_model, model_architecture, model_card,
model_provider, nucleus_def, rl_algorithm, role_assignment, router,
software_project, training_method
```

### P03 Prompt (20 kinds)
```
action_prompt, chain, churn_prevention_playbook, constraint_spec,
context_window_config, expansion_play, instruction, multimodal_prompt,
planning_strategy, prompt_compiler, prompt_optimizer, prompt_technique,
prompt_template, prompt_version, reasoning_strategy, reasoning_trace,
sales_playbook, system_prompt, tagline, webinar_script
```

### P04 Tools (34 kinds)
```
action_paradigm, agent_name_service_record, api_client, audio_tool,
browser_tool, cli_tool, code_executor, computer_use, daemon, db_connector,
diff_strategy, document_loader, function_def, hook, hook_config,
mcp_app_extension, mcp_server, multi_modal_config, notifier, plugin,
research_pipeline, retriever, sdk_example, search_strategy, search_tool,
skill, social_publisher, stt_provider, supabase_data_layer, toolkit,
tts_provider, vision_tool, voice_pipeline, webhook
```

### P05 Output (23 kinds)
```
analyst_briefing, app_directory_entry, case_study, code_of_conduct,
contributor_guide, course_module, formatter, github_issue_template,
integration_guide, interactive_demo, landing_page, onboarding_flow,
output_validator, parser, partner_listing, pitch_deck, press_release,
pricing_page, product_tour, quickstart_guide, response_format,
streaming_config, user_journey
```

### P06 Schema (8 kinds)
```
api_reference, edit_format, enum_def, input_schema, interface,
type_def, validation_schema, validator
```

### P07 Evals (23 kinds)
```
benchmark, benchmark_suite, bias_audit, cohort_analysis, e2e_eval,
eval_dataset, eval_framework, eval_metric, experiment_tracker,
golden_test, judge_config, llm_evaluation_scenario, llm_judge,
memory_benchmark, red_team_eval, regression_check, reward_model,
scoring_rubric, smoke_eval, trace_config, trajectory_eval, unit_eval,
usage_report
```

### P08 Architecture (12 kinds)
```
agent_card, agent_computer_interface, capability_registry, component_map,
decision_record, diagram, dual_loop_architecture, fhir_agent_capability,
invariant, naming_rule, pattern, supervisor
```

### P09 Config (28 kinds)
```
batch_config, cost_budget, data_residency, effort_profile, env_config,
experiment_config, feature_flag, kubernetes_ai_requirement,
marketplace_app_manifest, oauth_app_config, path_config, permission,
playground_config, prosody_config, quantization_config, rate_limit_config,
rbac_policy, realtime_session, runtime_rule, sandbox_config, sandbox_spec,
secret_config, sso_config, thinking_config, transport_config, usage_quota,
vad_config, white_label_config
```

### P10 Memory (18 kinds)
```
agent_grounding_record, c2pa_manifest, compression_config,
consolidation_policy, entity_memory, knowledge_index, learning_record,
memory_architecture, memory_summary, memory_type, model_registry,
procedural_memory, prompt_cache, runtime_state, session_backend,
session_state, vc_credential, workflow_run_crate
```

### P11 Feedback (26 kinds)
```
ab_test_config, ai_rmf_profile, audit_log, bugloop, compliance_checklist,
compliance_framework, conformity_assessment, content_filter,
content_monetization, enterprise_sla, gpai_technical_doc, guardrail,
hitl_config, incident_report, lifecycle_rule, nps_survey, optimizer,
quality_gate, referral_program, reward_signal, roi_calculator,
safety_hazard_taxonomy, safety_policy, self_improvement_loop,
subscription_tier, threat_model
```

### P12 Orchestration (15 kinds)
```
checkpoint, collaboration_pattern, crew_template, dag, dispatch_rule,
handoff, renewal_workflow, schedule, signal, spawn_config, team_charter,
visual_workflow, workflow, workflow_node, workflow_primitive
```

---

## ROUTES_TO Edges (Kind -> Nucleus)

| Nucleus | Pillar Ownership | Kinds Routed |
|---------|-----------------|-------------|
| N01 | P01 (research subsets) | knowledge_card, competitive_matrix, dataset_card, research_pipeline, discovery_questions, knowledge_graph, ontology |
| N02 | P03 (copy), P05 (campaigns) | tagline, prompt_template, action_prompt, landing_page, press_release, pitch_deck, case_study, course_module |
| N03 | P02, P03, P05, P06, P08 | agent, system_prompt, chain, formatter, parser, interface, type_def, diagram, pattern, decision_record |
| N04 | P01 (full), P10 | agentic_rag, chunk_strategy, embedding_config, rag_source, knowledge_index, entity_memory, memory_summary |
| N05 | P04, P07, P09 | cli_tool, browser_tool, mcp_server, benchmark, eval_framework, env_config, feature_flag, sandbox_config |
| N06 | P11 (monetization), P05 | content_monetization, subscription_tier, roi_calculator, pricing_page, sales_playbook, referral_program |
| N07 | P12 | workflow, dispatch_rule, handoff, signal, schedule, crew_template, team_charter, dag |

---

## GOVERNS Edges (LLM Function -> Kinds)

LLM functions map to 8F pipeline stages. Each kind's `llm_function` field encodes which 8F stage produces it.

| LLM Function | 8F Stage | Kind Count | Sample Kinds |
|-------------|----------|-----------|-------------|
| CONSTRAIN | F1 | 49 | agents_md, api_reference, chunk_strategy, embedding_config, env_config |
| INJECT | F3 | 45 | action_prompt, agentic_rag, citation, few_shot_example, knowledge_card |
| BECOME | F2 | 12 | agent, agent_card, agent_package, model_card, nucleus_def, role_assignment |
| CALL | F5 | 30 | api_client, browser_tool, cli_tool, mcp_server, retriever, webhook |
| PRODUCE | F6 | 35 | analyst_briefing, landing_page, pitch_deck, press_release, tagline |
| GOVERN | F7 | 70 | ab_test_config, benchmark, guardrail, quality_gate, scoring_rubric |
| REASON | F4 | 7 | decision_record, dispatch_rule, planning_strategy, reasoning_strategy |
| COLLABORATE | F8 | 5 | collaboration_pattern, handoff, handoff_protocol, signal, workflow |

---

## CO_OCCURS Edges (Kinds Commonly Built Together)

Derived from CEX build patterns and pillar co-residence:

| Kind A | Kind B | Co-occurrence Pattern |
|--------|--------|----------------------|
| agent | agent_card | agent identity + deployment spec |
| agent | system_prompt | agent + its operational prompt |
| rag_source | embedding_config | RAG stack: source + embedder |
| rag_source | retriever_config | RAG stack: source + retriever |
| embedding_config | reranker_config | retrieval pipeline pair |
| prompt_template | few_shot_example | prompt + examples |
| eval_framework | scoring_rubric | eval system pair |
| eval_framework | llm_judge | judge-based eval pair |
| crew_template | role_assignment | crew + role bindings |
| crew_template | team_charter | crew + mission contract |
| workflow | dag | workflow + execution graph |
| workflow | dispatch_rule | workflow + routing logic |
| system_prompt | guardrail | agent safety pair |
| quality_gate | regression_check | quality enforcement pair |
| learning_record | reward_signal | feedback loop pair |
| model_provider | fallback_chain | reliability pair |
| trace_config | audit_log | observability pair |
| finetune_config | eval_dataset | fine-tuning pair |
| knowledge_card | ontology | knowledge structure pair |
| knowledge_graph | knowledge_index | graph + index pair |

---

## Dependency Graph (REQUIRES Edges)

Kinds that logically require other kinds to function:

| Kind | Requires | Reason |
|------|----------|--------|
| agentic_rag | rag_source, embedding_config | RAG needs source + embedder |
| graph_rag_config | knowledge_graph, retriever_config | graph RAG needs graph + retriever |
| benchmark_suite | benchmark, eval_metric | suite wraps benchmarks |
| eval_framework | eval_metric, scoring_rubric | framework needs metrics |
| crew_template | role_assignment, team_charter | crew needs roles + charter |
| workflow | dispatch_rule, signal | workflow needs routing + completion |
| fallback_chain | model_provider, router | fallback needs providers |
| finetune_config | dataset_card, eval_dataset | fine-tune needs data |
| agent | agent_card, system_prompt | agent needs identity + prompt |
| knowledge_index | knowledge_card, chunk_strategy | index needs docs + chunking |
| prompt_cache | prompt_template, context_window_config | cache needs template + window |
| self_improvement_loop | learning_record, reward_signal, quality_gate | loop needs all 3 |
| supervisor | agent, dispatch_rule | supervisor orchestrates agents |
| dual_loop_architecture | workflow, self_improvement_loop | dual loop needs both loops |

---

## Graph Statistics

| Metric | Value |
|--------|-------|
| Total nodes | 277 (300 kinds + 12 pillars + 8 nuclei) |
| HAS_PILLAR edges | 257 (one per kind) |
| ROUTES_TO edges | 257 (one per kind, via pillar) |
| GOVERNS edges | 253 (kinds with known llm_function) |
| CO_OCCURS edges | 20 (manually curated high-value pairs) |
| REQUIRES edges | 14 (dependency relationships) |
| Total edges | ~800 |
| Avg edges per kind-node | ~3.1 |
| Most connected pillar | P04 Tools (34 kinds) |
| Most connected nucleus | N03 Engineering (~80 kinds routed) |
| Densest cluster | P11 Feedback + P07 Evals (quality enforcement) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.37 |
| [[kc_intent_resolution_map]] | upstream | 0.34 |
| [[spec_mission_100pct_coverage]] | upstream | 0.33 |
| [[agent_card_n03]] | upstream | 0.33 |
| [[p03_pc_cex_universal]] | upstream | 0.33 |
| [[p08_pat_nucleus_fractal]] | upstream | 0.31 |
| [[p01_kc_cex_project_overview]] | upstream | 0.31 |
| [[p10_entity_cex_system]] | related | 0.28 |
| [[bld_sp_collaboration_software_project]] | downstream | 0.28 |
| [[p01_kg_cex_system_architecture]] | sibling | 0.27 |
