---
id: spec_8f_tag_enrichment
kind: constraint_spec
pillar: P06
title: "Spec -- 8F Pipeline Tag Enrichment"
version: 1.0.0
created: 2026-04-24
author: n07_orchestrator
domain: metadata_enrichment
quality_target: 9.0
status: SPEC
scope: cross-cutting
depends_on: null
tags: [spec, 8f, metadata, enrichment, infrastructure]
tldr: "Add 8f field to every artifact frontmatter, mapping each kind to its primary pipeline function."
density_score: 0.95
---

## Problem

- 1054 artifacts have `kind:` in frontmatter but no `8f:` field
- Builder ISOs already have `llm_function:` (3,647 ISOs tagged) but artifacts don't
- No way to query "show me all F7_govern artifacts" or "which pipeline stages are thin"
- New artifacts created by builders don't auto-inherit the 8F tag
- Dataview queries, cex_retriever, and cex_doctor can't filter by pipeline stage

## Vision

Every artifact in the repo carries an `8f:` frontmatter field indicating its primary
pipeline function. Builders auto-tag on creation. Scripts enforce consistency.

```yaml
# BEFORE
kind: knowledge_card
pillar: P01
tags: [index, p01, n00]

# AFTER
kind: knowledge_card
pillar: P01
8f: F3_inject
tags: [index, p01, n00]
```

## Existing State (what we have)

| Layer | Count | Has 8F? |
|-------|-------|---------|
| Builder ISOs (`llm_function:`) | 6,634 | YES (8 canonical + 8 non-canonical) |
| Nucleus artifacts (`kind:`) | 1,054 | NO |
| Builder ISO templates (shared) | 12 per kind | YES (template-level) |
| kinds_meta.json | 300 kinds | NO |

Non-canonical `llm_function` values to normalize:
- CONTEXT (8) -> INJECT
- ORCHESTRATE (2) -> COLLABORATE
- GENERATE (2) -> PRODUCE
- EXECUTE (2) -> CALL
- DEMONSTRATE (2) -> PRODUCE
- TOOL (1) -> CALL
- EVALUATE (1) -> GOVERN
- ACT (1) -> CALL

## Kind-to-8F Mapping (300 kinds -> 8 functions)

### F1 CONSTRAIN (define rules, schemas, boundaries)
ab_test_config, backpressure_policy, batch_config, boot_config, c2pa_manifest,
canary_config, compliance_checklist, compliance_framework, compression_config,
consolidation_policy, constraint_spec, content_filter, context_window_config,
data_contract, data_residency, domain_vocabulary, edit_format, enum_def,
env_config, feature_flag, hibernation_policy, inference_config, input_schema,
interface, invariant, lifecycle_rule, naming_rule, oauth_app_config, path_config,
permission, rate_limit_config, rbac_policy, runtime_rule, safety_policy,
sandbox_config, sandbox_spec, secret_config, spawn_config, sso_config,
streaming_config, tokenizer_config, transport_config, type_def,
usage_quota, vad_config, validation_schema

### F2 BECOME (define identity, persona, model)
agent, agent_card, agent_computer_interface, agent_grounding_record,
agent_name_service_record, agent_package, agent_profile, agents_md,
boot_config, capability_registry, context_file, crew_template, model_architecture,
model_card, model_provider, model_registry, nucleus_def, personality,
role_assignment, system_prompt, user_model

### F3 INJECT (provide knowledge, context, retrieval)
agentic_rag, chunk_strategy, citation, context_doc, dataset_card,
domain_vocabulary, embedder_provider, embedding_config, entity_memory,
episodic_memory, eval_dataset, faq_entry, few_shot_example, glossary_entry,
graph_rag_config, knowledge_card, knowledge_graph, knowledge_index,
memory_architecture, memory_benchmark, memory_scope, memory_summary,
memory_type, ontology, preference_dataset, procedural_memory,
prompt_cache, prospective_memory, rag_source, reranker_config,
retrieval_evaluator, retriever, retriever_config, vector_store,
working_memory

### F4 REASON (plan, decide, analyze)
analyst_briefing, axiom, bounded_context, case_study, cohort_analysis,
competitive_matrix, component_map, context_map, decision_record,
diagram, discovery_questions, mental_model, pattern, planning_strategy,
reasoning_strategy, reasoning_trace, threat_model, aggregate_root,
domain_event, value_object

### F5 CALL (invoke tools, external capabilities)
api_client, api_reference, audio_tool, browser_tool, cli_tool,
code_executor, computer_use, db_connector, document_loader,
marketplace_app_manifest, mcp_app_extension, mcp_server,
messaging_gateway, notifier, openapi_spec, plugin, research_pipeline,
search_strategy, search_tool, session_backend, toolkit, vision_tool,
voice_pipeline, webhook

### F6 PRODUCE (generate output, content, prompts)
action_paradigm, action_prompt, chain, course_module, curation_nudge,
diff_strategy, distillation_config, finetune_config, formatter,
function_def, interactive_demo, landing_page, multimodal_prompt,
multi_modal_config, output_validator, parser, pitch_deck,
playground_config, press_release, product_tour, prompt_compiler,
prompt_optimizer, prompt_technique, prompt_template, prompt_version,
prosody_config, quantization_config, query_optimizer, realtime_session,
response_format, sdk_example, social_publisher, stt_provider,
synthetic_data_config, tagline, training_method, tts_provider,
visual_workflow, webinar_script

### F7 GOVERN (evaluate, score, gate, correct)
ai_rmf_profile, benchmark, benchmark_suite, bias_audit, bugloop,
conformity_assessment, constitutional_rule, drift_detector, e2e_eval,
eval_framework, eval_metric, experiment_config, experiment_tracker,
golden_test, gpai_technical_doc, guardrail, judge_config,
kubernetes_ai_requirement, learning_record, lineage_record,
llm_evaluation_scenario, llm_judge, quality_gate, red_team_eval,
regression_check, reward_model, reward_signal, rl_algorithm,
safety_hazard_taxonomy, scoring_rubric, self_improvement_loop,
smoke_eval, trajectory_eval, unit_eval

### F8 COLLABORATE (orchestrate, coordinate, deploy)
alert_rule, app_directory_entry, audit_log, changelog, checkpoint,
circuit_breaker, collaboration_pattern, dag, daemon, deployment_manifest,
dispatch_rule, dual_loop_architecture, event_schema, event_stream,
expansion_play, fallback_chain, github_issue_template, handoff,
handoff_protocol, hook, hook_config, incident_report, optimizer,
partner_listing, pipeline_template, process_manager, retry_policy,
router, runtime_state, saga, schedule, session_state, signal,
slo_definition, software_project, state_machine, supervisor,
team_charter, trace_config, vc_credential, workflow, workflow_node,
workflow_primitive, workflow_run_crate

### Cross-cutting (kind serves multiple 8F functions equally)
code_of_conduct, contributor_guide, instruction, integration_guide,
quickstart_guide, repo_map, skill, validator, white_label_config,
lens

### Verticals (domain-specific constraint + knowledge bundles)
ecommerce_vertical -> F1, edtech_vertical -> F1, fintech_vertical -> F1,
fhir_agent_capability -> F1, govtech_vertical -> F1,
healthcare_vertical -> F1, legal_vertical -> F1

### GTM/Commercial (produce + collaborate)
churn_prevention_playbook -> F6, competitive_matrix -> F4,
content_monetization -> F6, customer_segment -> F4,
effort_profile -> F4, enterprise_sla -> F8, expansion_play -> F8,
cost_budget -> F1, nps_survey -> F7, onboarding_flow -> F6,
pricing_page -> F6, referral_program -> F6, renewal_workflow -> F8,
roi_calculator -> F6, sales_playbook -> F6, subscription_tier -> F1,
usage_report -> F7, user_journey -> F4, supabase_data_layer -> F5

## Artifacts

### Wave 1: Foundation (3 artifacts, N07+N05)

| Action | Path | Kind | Nucleus | Notes |
|--------|------|------|---------|-------|
| CREATE | `.cex/config/kind_8f_mapping.yaml` | config | N07 | 300 kinds -> 8F function map |
| CREATE | `_tools/cex_8f_tagger.py` | cli_tool | N05 | Bulk tagger: read mapping, scan .md, inject `8f:` field |
| CREATE | `_tools/cex_8f_normalizer.py` | cli_tool | N05 | Normalize non-canonical `llm_function` values in ISOs |

### Wave 2: Enrichment (bulk operation, N05)

| Action | Path | Kind | Nucleus | Notes |
|--------|------|------|---------|-------|
| MODIFY | `N0*_*/P*_*/*.md` (~1054 files) | mixed | N05 | Add `8f: F{N}_{function}` after `kind:` line |
| MODIFY | `archetypes/builders/*/bld_*.md` (~20 ISOs) | mixed | N05 | Normalize non-canonical llm_function values |

### Wave 3: Enforcement (4 artifacts, N03+N05)

| Action | Path | Kind | Nucleus | Notes |
|--------|------|------|---------|-------|
| MODIFY | `_tools/cex_hooks.py` | cli_tool | N05 | Add 8F tag validation to pre-commit |
| MODIFY | `archetypes/builders/_shared/` | template | N03 | Update shared output templates to include `8f:` field |
| MODIFY | `.cex/kinds_meta.json` | config | N05 | Add `primary_8f` field to each kind entry |
| CREATE | `_docs/specs/kind_8f_reference.md` | context_doc | N04 | Human-readable 8F mapping reference |

## Decisions

| Decision | Value | Source |
|----------|-------|--------|
| Field name | `8f` (short, greppable) | LLM-optimal |
| Field format | `F{N}_{function}` (e.g., `F3_inject`) | Machine + human readable |
| Placement | After `kind:` line in frontmatter | Logical grouping |
| Cross-cutting kinds | Tagged with primary function | Simplicity over precision |
| Scope | cex-lab first, push to public after review | User decision |

## Acceptance Criteria

- [ ] All 300 kinds mapped in `kind_8f_mapping.yaml`
- [ ] Tagger script handles: add new, skip existing, dry-run mode
- [ ] ~1054 artifacts have `8f:` field in frontmatter
- [ ] Non-canonical `llm_function` values normalized (20 ISOs)
- [ ] `kinds_meta.json` enriched with `primary_8f` per kind
- [ ] Pre-commit hook validates 8F tag on new artifacts
- [ ] Shared builder templates include `8f:` in output
- [ ] `python _tools/cex_doctor.py` passes after enrichment
- [ ] Dataview query `FROM #F7_govern` returns results

## Estimated Impact

| Metric | Before | After |
|--------|--------|-------|
| Artifacts with 8F metadata | 0 | ~1054 |
| ISOs with canonical llm_function | 6,614 | 6,634 |
| kinds_meta.json with primary_8f | 0 | 300 |
| Queryable pipeline dimensions | 3 (kind, pillar, nucleus) | 4 (+8F) |
| Builder auto-tag coverage | 0% | 100% |

## Risk

| Risk | Mitigation |
|------|------------|
| Wrong kind->8F mapping | ~30 ambiguous kinds; use primary function, flag in reference doc |
| Frontmatter corruption | Dry-run first; git diff review before commit |
| Large git diff | Single atomic commit per wave; easy to revert |
| We're in cex-lab | Zero risk to public; push only after validation |

## Execution

```
/grid spec_8f_tag_enrichment
  Wave 1: N07 writes mapping + N05 writes scripts (parallel)
  Wave 2: N05 runs bulk tagger (sequential, after W1)
  Wave 3: N03+N05 update builders + hooks (parallel, after W2)
```

Estimated: ~30 min for scripts, ~5 min for bulk run, ~15 min for enforcement.
