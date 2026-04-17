---
mission: KIND_GAP_AUDIT
nucleus: n01
wave: M1
created: 2026-04-17
priority: HIGH
effort: opus
---

# N01 KIND_GAP_AUDIT M1: DDD Ubiquitous Language x CEX Kind Coverage

## CONTEXT

CEX has 257 kinds across 12 pillars. A "kind" is the atomic artifact type in the typed
knowledge system. The governing philosophy: **Ubiquitous Language** (Eric Evans, DDD):
> "Build a common, rigorous language shared between developers and domain users, grounded in
> the Domain Model. Rigorous because software does not tolerate ambiguity."

CEX is a domain model for AI/LLM agent infrastructure. Every concept in the AI enterprise
domain that is unambiguous, reusable, and requires a typed representation should be a kind.

The question: **What is missing from CEX's 257 kinds, viewed through the DDD UL lens?**

## CURRENT 257 KINDS

ab_test_config, action_paradigm, action_prompt, agent, agent_card,
agent_computer_interface, agent_grounding_record, agent_name_service_record,
agent_package, agent_profile, agentic_rag, agents_md, ai_rmf_profile,
analyst_briefing, api_client, api_reference, app_directory_entry, audio_tool,
audit_log, axiom, batch_config, benchmark, benchmark_suite, bias_audit,
boot_config, browser_tool, bugloop, c2pa_manifest, capability_registry,
case_study, chain, changelog, checkpoint, chunk_strategy, churn_prevention_playbook,
citation, cli_tool, code_executor, code_of_conduct, cohort_analysis,
collaboration_pattern, competitive_matrix, compliance_checklist, compliance_framework,
component_map, compression_config, computer_use, conformity_assessment,
consolidation_policy, constraint_spec, content_filter, content_monetization,
context_doc, context_window_config, contributor_guide, cost_budget,
course_module, crew_template, customer_segment, daemon, dag, data_residency,
dataset_card, db_connector, decision_record, diagram, diff_strategy,
discovery_questions, dispatch_rule, document_loader, dual_loop_architecture,
e2e_eval, ecommerce_vertical, edit_format, edtech_vertical, effort_profile,
embedder_provider, embedding_config, enterprise_sla, entity_memory,
enum_def, env_config, eval_dataset, eval_framework, eval_metric,
expansion_play, experiment_config, experiment_tracker, fallback_chain,
faq_entry, feature_flag, few_shot_example, fhir_agent_capability,
finetune_config, fintech_vertical, formatter, function_def, github_issue_template,
glossary_entry, golden_test, govtech_vertical, gpai_technical_doc, graph_rag_config,
guardrail, handoff, handoff_protocol, healthcare_vertical, hitl_config, hook,
hook_config, incident_report, input_schema, instruction, integration_guide,
interactive_demo, interface, invariant, judge_config, knowledge_card,
knowledge_graph, knowledge_index, kubernetes_ai_requirement, landing_page, lens,
learning_record, legal_vertical, lifecycle_rule, llm_evaluation_scenario, llm_judge,
marketplace_app_manifest, mcp_app_extension, mcp_server, memory_architecture,
memory_benchmark, memory_scope, memory_summary, memory_type, mental_model,
model_architecture, model_card, model_provider, model_registry, multi_modal_config,
multimodal_prompt, naming_rule, notifier, nps_survey, nucleus_def, oauth_app_config,
onboarding_flow, ontology, optimizer, output_validator, parser, partner_listing,
path_config, pattern, permission, pitch_deck, planning_strategy, playground_config,
plugin, press_release, pricing_page, procedural_memory, product_tour, prompt_cache,
prompt_compiler, prompt_optimizer, prompt_technique, prompt_template, prompt_version,
prosody_config, quality_gate, quantization_config, quickstart_guide, rag_source,
rate_limit_config, rbac_policy, realtime_session, reasoning_strategy, reasoning_trace,
red_team_eval, referral_program, regression_check, renewal_workflow, repo_map,
reranker_config, research_pipeline, response_format, retriever, retriever_config,
reward_model, reward_signal, rl_algorithm, roi_calculator, role_assignment,
router, runtime_rule, runtime_state, safety_hazard_taxonomy, safety_policy,
sales_playbook, sandbox_config, sandbox_spec, schedule, scoring_rubric, sdk_example,
search_strategy, search_tool, secret_config, self_improvement_loop, session_backend,
session_state, signal, skill, smoke_eval, social_publisher, software_project,
spawn_config, sso_config, streaming_config, stt_provider, subscription_tier,
supabase_data_layer, supervisor, system_prompt, tagline, team_charter,
thinking_config, threat_model, toolkit, trace_config, training_method,
trajectory_eval, transport_config, tts_provider, type_def, unit_eval, usage_quota,
usage_report, user_journey, vad_config, validation_schema, validator,
vc_credential, vector_store, vision_tool, visual_workflow, voice_pipeline,
webhook, webinar_script, white_label_config, workflow, workflow_node,
workflow_primitive, workflow_run_crate

## TASK

Run 8F. Produce kc_kind_gap_analysis.md.

### Research dimensions:

**DDD Strategic Design (Evans + Vernon):**
- Bounded Context, Context Map, Shared Kernel, Anti-Corruption Layer,
  Open Host Service, Published Language, Conformist, Customer-Supplier
- Ubiquitous Language Registry as a governed artifact
- Domain Vision Statement, Highlighted Core
- Event Storming outputs: Domain Event, Command, Policy, Read Model, External System
- Subdomains: Core, Supporting, Generic

**DDD Tactical Design:**
- Aggregate, Aggregate Root, Entity, Value Object
- Domain Service, Application Service
- Repository, Factory, Specification patterns
- Saga / Process Manager, Domain Notification

**AI/LLM Infrastructure gaps vs 257 kinds:**
- Observability: span_config, metric_definition, alert_rule, slo_definition
- Data governance: lineage_record, provenance_chain, consent_record, data_contract
- Training pipeline: training_run, eval_checkpoint, hyperparameter_config, ablation_study
- Safety/alignment: constitutional_rule, preference_dataset, sycophancy_spec
- Agent economics: token_cost_model, compute_budget (vs cost_budget)
- Multi-agent coordination: consensus_protocol, voting_scheme, arbitration_rule
- Versioning: artifact_version, migration_script, schema_evolution, deprecation_policy
- Real-time: event_stream, pub_sub_config, queue_config, backpressure_policy
- Graph: knowledge_triple, inference_rule
- MCP ecosystem: mcp_tool_manifest, mcp_capability_schema

**CEX meta-system gaps:**
- domain_vocabulary (kc_{domain}_vocabulary as a registered kind?)
- wave_config, builder_iso, quality_threshold
- deployment_manifest, rollback_plan, canary_config

### F6 PRODUCE

Write `N01_intelligence/P01_knowledge/kc_kind_gap_analysis.md`:

```yaml
---
id: kc_kind_gap_analysis
kind: knowledge_card
pillar: P01
nucleus: n01
domain: taxonomy-audit
quality: null
---
```

Required sections:
1. **DDD Coverage Map** (table: DDD_concept | closest_CEX_kind | gap: COVERED/PARTIAL/MISSING)
2. **Top 20 Gap Candidates** -- each with: name | pillar | definition | reuse_score
3. **Anti-gap Analysis** -- overloaded kinds (one kind covering 3+ DDD concepts)
4. **10 Recommended New Kinds** with pillar, rationale, and example use case
5. **domain_vocabulary as a kind?** -- yes/no with reasoning

### F8 COLLABORATE
```bash
git add N01_intelligence/
git commit -m "[N01] KIND_GAP_AUDIT M1: DDD UL x 257 CEX kinds coverage map"
python -c "from _tools.signal_writer import write_signal; write_signal('n01', 'kind_gap_complete', 9.0)"
```

## COMPLETION CRITERIA
- [ ] kc_kind_gap_analysis.md written (min 4KB, quality: null)
- [ ] DDD coverage map table (min 15 rows)
- [ ] Top 20 gap candidates listed with pillar
- [ ] 10 recommended new kinds
- [ ] git commit [N01] KIND_GAP_AUDIT M1
- [ ] signal sent: n01 -> kind_gap_complete
