# FRACTAL_FILL Wave Plan (codex/GPT builder)

447 artifacts across 6 waves x 8 nuclei. Applicability-filtered scope.

## Wave schedule

| Wave | Pillars | Artifacts | Purpose |
|---|---|---:|---|
| W1_FOUNDATIONS | P06+P09 | 67 | schemas + config |
| W2_KNOWLEDGE | P01+P10 | 69 | knowledge + memory |
| W3_AGENT_LAYER | P02+P03 | 103 | agents + prompts |
| W4_EXECUTION | P04+P05 | 88 | tools + output |
| W5_META | P08+P07 | 59 | architecture + quality |
| W6_SELF_IMPROVE | P11+P12 | 61 | feedback + orchestration |
| **TOTAL** | **all 12** | **447** | |

## Dispatch strategy

- 6 nuclei parallel per sub-wave (grid-codex max).
- Wave 1a: N01-N06. Wave 1b: N00+N07 (archetype+admin).
- Between waves: N07 verifies deliverables, commits, compiles, doctor check, archives handoffs.
- Codex no-autocommit: N07 runs `git add && git commit` after each nucleus signals done.

## W1_FOUNDATIONS  (P06+P09)

| Nucleus | Count | Kinds |
|---|---:|---|
| N00_genesis | 9 | enum_def, input_schema, type_def, validator, env_config, path_config, permission, rate_limit_config, secret_config |
| N01_intelligence | 9 | enum_def, input_schema, type_def, validator, env_config, path_config, permission, rate_limit_config, secret_config |
| N02_marketing | 7 | enum_def, type_def, validator, path_config, permission, rate_limit_config, secret_config |
| N03_engineering | 8 | enum_def, type_def, validator, env_config, path_config, permission, rate_limit_config, secret_config |
| N04_knowledge | 9 | enum_def, input_schema, type_def, validator, env_config, path_config, permission, rate_limit_config, secret_config |
| N05_operations | 8 | enum_def, type_def, env_config, feature_flag, path_config, permission, rate_limit_config, secret_config |
| N06_commercial | 8 | enum_def, type_def, validator, env_config, path_config, permission, rate_limit_config, secret_config |
| N07_admin | 9 | enum_def, input_schema, type_def, validator, env_config, path_config, permission, rate_limit_config, secret_config |

## W2_KNOWLEDGE  (P01+P10)

| Nucleus | Count | Kinds |
|---|---:|---|
| N00_genesis | 11 | chunk_strategy, embedder_provider, few_shot_example, knowledge_card, retriever_config, vector_store, entity_memory, knowledge_index, learning_record, memory_summary, runtime_state |
| N01_intelligence | 11 | chunk_strategy, citation, competitive_matrix, embedder_provider, few_shot_example, ontology, retriever_config, vector_store, entity_memory, memory_summary, runtime_state |
| N02_marketing | 8 | chunk_strategy, embedder_provider, few_shot_example, retriever_config, vector_store, entity_memory, knowledge_index, runtime_state |
| N03_engineering | 8 | chunk_strategy, embedder_provider, retriever_config, vector_store, entity_memory, knowledge_index, memory_summary, runtime_state |
| N04_knowledge | 5 | embedder_provider, knowledge_graph, vector_store, learning_record, runtime_state |
| N05_operations | 9 | chunk_strategy, embedder_provider, few_shot_example, retriever_config, vector_store, entity_memory, knowledge_index, learning_record, memory_summary |
| N06_commercial | 8 | chunk_strategy, embedder_provider, few_shot_example, retriever_config, vector_store, entity_memory, knowledge_index, runtime_state |
| N07_admin | 9 | chunk_strategy, embedder_provider, few_shot_example, retriever_config, vector_store, knowledge_index, learning_record, memory_summary, runtime_state |

## W3_AGENT_LAYER  (P02+P03)

| Nucleus | Count | Kinds |
|---|---:|---|
| N00_genesis | 15 | agent, agent_package, axiom, handoff_protocol, mental_model, model_provider, nucleus_def, router, action_prompt, constraint_spec, context_window_config, prompt_compiler, prompt_template, reasoning_trace, system_prompt |
| N01_intelligence | 12 | agent_package, axiom, handoff_protocol, mental_model, model_provider, nucleus_def, router, action_prompt, constraint_spec, context_window_config, prompt_compiler, reasoning_trace |
| N02_marketing | 13 | agent_package, axiom, handoff_protocol, mental_model, model_provider, nucleus_def, router, constraint_spec, context_window_config, multimodal_prompt, prompt_compiler, reasoning_trace, tagline |
| N03_engineering | 10 | agent_package, handoff_protocol, model_provider, nucleus_def, router, action_prompt, constraint_spec, context_window_config, prompt_compiler, reasoning_trace |
| N04_knowledge | 13 | agent_package, axiom, handoff_protocol, mental_model, model_provider, nucleus_def, router, action_prompt, constraint_spec, context_window_config, prompt_compiler, prompt_template, reasoning_trace |
| N05_operations | 13 | agent_package, axiom, handoff_protocol, mental_model, model_provider, nucleus_def, router, action_prompt, constraint_spec, context_window_config, prompt_compiler, prompt_template, reasoning_trace |
| N06_commercial | 13 | agent_package, customer_segment, handoff_protocol, model_provider, nucleus_def, router, action_prompt, constraint_spec, context_window_config, expansion_play, prompt_compiler, reasoning_trace, sales_playbook |
| N07_admin | 14 | agent_package, axiom, handoff_protocol, mental_model, model_provider, nucleus_def, role_assignment, router, action_prompt, constraint_spec, context_window_config, prompt_compiler, prompt_template, reasoning_trace |

## W4_EXECUTION  (P04+P05)

| Nucleus | Count | Kinds |
|---|---:|---|
| N00_genesis | 11 | browser_tool, code_executor, document_loader, function_def, hook, mcp_server, retriever, search_tool, toolkit, output_validator, response_format |
| N01_intelligence | 12 | browser_tool, document_loader, function_def, hook, mcp_server, research_pipeline, retriever, search_tool, toolkit, analyst_briefing, output_validator, response_format |
| N02_marketing | 13 | browser_tool, document_loader, function_def, hook, mcp_server, retriever, search_tool, social_publisher, toolkit, landing_page, onboarding_flow, press_release, response_format |
| N03_engineering | 10 | browser_tool, code_executor, document_loader, hook, mcp_server, retriever, search_tool, skill, toolkit, output_validator |
| N04_knowledge | 11 | browser_tool, code_executor, document_loader, function_def, hook, mcp_server, retriever, search_tool, toolkit, output_validator, response_format |
| N05_operations | 10 | browser_tool, code_executor, document_loader, function_def, hook, mcp_server, retriever, search_tool, toolkit, response_format |
| N06_commercial | 10 | browser_tool, document_loader, hook, mcp_server, retriever, search_tool, toolkit, output_validator, pricing_page, response_format |
| N07_admin | 11 | browser_tool, code_executor, document_loader, function_def, hook, mcp_server, retriever, search_tool, toolkit, output_validator, response_format |

## W5_META  (P08+P07)

| Nucleus | Count | Kinds |
|---|---:|---|
| N00_genesis | 8 | decision_record, invariant, pattern, eval_dataset, golden_test, llm_judge, scoring_rubric, unit_eval |
| N01_intelligence | 6 | decision_record, invariant, pattern, golden_test, llm_judge, unit_eval |
| N02_marketing | 7 | decision_record, invariant, pattern, eval_dataset, golden_test, llm_judge, unit_eval |
| N03_engineering | 6 | decision_record, invariant, eval_dataset, golden_test, llm_judge, unit_eval |
| N04_knowledge | 7 | decision_record, invariant, pattern, eval_dataset, golden_test, llm_judge, unit_eval |
| N05_operations | 10 | decision_record, invariant, pattern, e2e_eval, eval_dataset, golden_test, llm_judge, scoring_rubric, smoke_eval, unit_eval |
| N06_commercial | 6 | decision_record, invariant, eval_dataset, golden_test, llm_judge, unit_eval |
| N07_admin | 9 | capability_registry, decision_record, invariant, pattern, eval_dataset, golden_test, llm_judge, scoring_rubric, unit_eval |

## W6_SELF_IMPROVE  (P11+P12)

| Nucleus | Count | Kinds |
|---|---:|---|
| N00_genesis | 10 | guardrail, lifecycle_rule, quality_gate, reward_signal, checkpoint, handoff, signal, spawn_config, workflow, workflow_primitive |
| N01_intelligence | 7 | guardrail, lifecycle_rule, checkpoint, handoff, signal, spawn_config, workflow_primitive |
| N02_marketing | 7 | guardrail, lifecycle_rule, checkpoint, handoff, signal, spawn_config, workflow_primitive |
| N03_engineering | 4 | lifecycle_rule, reward_signal, checkpoint, workflow_primitive |
| N04_knowledge | 6 | guardrail, lifecycle_rule, checkpoint, handoff, signal, workflow_primitive |
| N05_operations | 8 | guardrail, incident_report, lifecycle_rule, reward_signal, checkpoint, handoff, signal, workflow_primitive |
| N06_commercial | 12 | content_monetization, guardrail, lifecycle_rule, nps_survey, referral_program, roi_calculator, subscription_tier, checkpoint, handoff, signal, spawn_config, workflow_primitive |
| N07_admin | 7 | guardrail, lifecycle_rule, checkpoint, crew_template, schedule, team_charter, workflow_primitive |

