#!/usr/bin/env python3
# -*- coding: ascii -*-
"""gen_deps_patch.py -- Generate depends_on patch for 231 kinds missing deps."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KINDS_META = ROOT / ".cex" / "kinds_meta.json"
OUTPUT = ROOT / ".cex" / "kind_deps_patch.json"

with open(KINDS_META, encoding="utf-8") as f:
    meta = json.load(f)

ALL = set(meta.keys())
have_deps = {k for k, v in meta.items() if v.get("depends_on")}
missing = sorted(ALL - have_deps)


def d(*deps):
    return [x for x in deps if x in ALL]


PATCHES = {
    # P01 Knowledge
    "changelog": d("knowledge_card", "learning_record"),
    "chunk_strategy": d("embedding_config"),
    "citation": d("knowledge_card"),
    "competitive_matrix": d("knowledge_card", "customer_segment"),
    "context_doc": d("knowledge_card"),
    "discovery_questions": d("customer_segment", "knowledge_card"),
    "domain_vocabulary": d("glossary_entry", "ontology"),
    "ecommerce_vertical": d("customer_segment", "knowledge_card"),
    "edtech_vertical": d("customer_segment", "knowledge_card"),
    "embedder_provider": d("embedding_config"),
    "embedding_config": d("vector_store"),
    "faq_entry": d("knowledge_card"),
    "few_shot_example": d("prompt_template"),
    "fintech_vertical": d("customer_segment", "knowledge_card"),
    "glossary_entry": d("knowledge_card"),
    "govtech_vertical": d("customer_segment", "knowledge_card"),
    "graph_rag_config": d("rag_source", "embedding_config", "vector_store"),
    "healthcare_vertical": d("customer_segment", "knowledge_card"),
    "knowledge_card": d("citation"),
    "legal_vertical": d("customer_segment", "knowledge_card"),
    "repo_map": d("knowledge_card", "context_doc"),
    "reranker_config": d("retriever_config", "embedding_config"),
    "vector_store": d("embedding_config"),
    # P02 Model
    "agent_package": d("agent", "agent_card"),
    "agent_profile": d("agent", "agent_card"),
    "agents_md": d("agent", "agent_card"),
    "axiom": d("mental_model"),
    "boot_config": d("env_config", "secret_config"),
    "customer_segment": d("knowledge_card"),
    "finetune_config": d("training_method", "eval_dataset"),
    "handoff_protocol": d("agent_card", "dispatch_rule"),
    "lens": d("mental_model"),
    "memory_scope": d("entity_memory", "session_state"),
    "mental_model": d("knowledge_card"),
    "model_architecture": d("model_card", "model_provider"),
    "model_card": d("model_provider"),
    "model_provider": d("env_config", "secret_config"),
    "nucleus_de": d("agent", "system_prompt", "agent_card"),
    "rl_algorithm": d("reward_model", "training_method"),
    "role_assignment": d("agent_card", "capability_registry"),
    "router": d("model_provider", "fallback_chain"),
    "software_project": d("agent_card", "context_doc"),
    "training_method": d("eval_dataset", "scoring_rubric"),
    # P03 Prompt
    "action_prompt": d("prompt_template"),
    "context_window_config": d("prompt_template"),
    "instruction": d("prompt_template"),
    "multimodal_prompt": d("prompt_template"),
    "planning_strategy": d("prompt_template", "reasoning_strategy"),
    "prompt_compiler": d("prompt_template", "prompt_version"),
    "prompt_optimizer": d("prompt_template", "scoring_rubric"),
    "prompt_technique": d("prompt_template"),
    "prompt_template": d("system_prompt"),
    "prompt_version": d("prompt_template"),
    "reasoning_strategy": d("prompt_template", "mental_model"),
    "reasoning_trace": d("reasoning_strategy"),
    "sales_playbook": d("customer_segment", "prompt_template"),
    "system_prompt": d("boot_config"),
    "tagline": d("prompt_template"),
    "webinar_script": d("prompt_template", "knowledge_card"),
    # P04 Tools
    "action_paradigm": d("function_de", "skill"),
    "agent_name_service_record": d("agent_card"),
    "api_client": d("env_config", "secret_config"),
    "audio_tool": d("toolkit"),
    "cli_tool": d("function_de"),
    "code_executor": d("env_config"),
    "computer_use": d("browser_tool", "vision_tool"),
    "daemon": d("env_config", "boot_config"),
    "db_connector": d("env_config", "secret_config"),
    "diff_strategy": d("function_de"),
    "document_loader": d("parser", "api_client"),
    "function_de": d("type_de"),
    "hook": d("function_de"),
    "hook_config": d("hook", "env_config"),
    "mcp_app_extension": d("mcp_server", "api_client"),
    "multi_modal_config": d("toolkit"),
    "notifier": d("webhook", "api_client"),
    "plugin": d("function_de", "toolkit"),
    "retriever": d("retriever_config", "vector_store"),
    "sdk_example": d("api_client", "function_de"),
    "search_strategy": d("retriever_config"),
    "search_tool": d("retriever_config", "api_client"),
    "skill": d("function_de"),
    "social_publisher": d("api_client", "prompt_template"),
    "stt_provider": d("api_client"),
    "supabase_data_layer": d("db_connector", "env_config"),
    "toolkit": d("function_de"),
    "tts_provider": d("api_client"),
    "vision_tool": d("api_client"),
    "webhook": d("api_client", "env_config"),
    # P05 Output
    "analyst_briefing": d("knowledge_card", "scoring_rubric"),
    "app_directory_entry": d("agent_card", "knowledge_card"),
    "case_study": d("knowledge_card", "customer_segment"),
    "code_of_conduct": d("knowledge_card"),
    "contributor_guide": d("knowledge_card", "context_doc"),
    "course_module": d("knowledge_card", "scoring_rubric"),
    "formatter": d("type_de"),
    "github_issue_template": d("knowledge_card"),
    "integration_guide": d("api_reference", "knowledge_card"),
    "interactive_demo": d("landing_page"),
    "landing_page": d("prompt_template"),
    "onboarding_flow": d("user_journey", "knowledge_card"),
    "output_validator": d("validation_schema"),
    "parser": d("formatter", "type_de"),
    "partner_listing": d("knowledge_card", "agent_card"),
    "pitch_deck": d("knowledge_card", "customer_segment"),
    "press_release": d("knowledge_card"),
    "pricing_page": d("subscription_tier", "customer_segment"),
    "product_tour": d("user_journey", "knowledge_card"),
    "quickstart_guide": d("knowledge_card", "context_doc"),
    "response_format": d("formatter", "type_de"),
    "streaming_config": d("transport_config"),
    "user_journey": d("customer_segment", "knowledge_card"),
    # P06 Schema
    "api_reference": d("api_client", "input_schema"),
    "edit_format": d("formatter", "type_de"),
    "enum_de": d("type_de"),
    "event_schema": d("type_de", "domain_event"),
    "input_schema": d("type_de"),
    "interface": d("input_schema", "output_validator"),
    "type_de": [],  # foundational
    "validation_schema": [],  # foundational
    "validator": d("validation_schema", "quality_gate"),
    # P07 Evals
    "benchmark_suite": d("benchmark", "eval_dataset", "scoring_rubric"),
    "bias_audit": d("eval_dataset", "scoring_rubric"),
    "cohort_analysis": d("eval_dataset", "customer_segment"),
    "e2e_eval": d("quality_gate", "scoring_rubric"),
    "eval_framework": d("eval_metric", "scoring_rubric"),
    "eval_metric": d("scoring_rubric"),
    "experiment_tracker": d("experiment_config", "eval_metric"),
    "golden_test": d("eval_dataset", "scoring_rubric"),
    "llm_evaluation_scenario": d("eval_dataset", "scoring_rubric", "llm_judge"),
    "memory_benchmark": d("benchmark", "entity_memory"),
    "regression_check": d("quality_gate", "eval_metric"),
    "reward_model": d("scoring_rubric", "reward_signal"),
    "scoring_rubric": d("quality_gate"),
    "smoke_eval": d("quality_gate"),
    "trace_config": d("env_config"),
    "trajectory_eval": d("eval_dataset", "scoring_rubric"),
    "unit_eval": d("scoring_rubric"),
    "usage_report": d("eval_metric", "knowledge_card"),
    # P08 Architecture
    "agent_computer_interface": d("agent_card", "computer_use"),
    "bounded_context": d("domain_vocabulary", "context_map"),
    "capability_registry": d("agent_card"),
    "component_map": d("agent_card", "knowledge_card"),
    "context_map": d("knowledge_card", "component_map"),
    "decision_record": d("knowledge_card"),
    "diagram": d("component_map"),
    "dual_loop_architecture": d("workflow", "agent_card"),
    "fhir_agent_capability": d("agent_card", "api_client"),
    "naming_rule": d("knowledge_card"),
    "pattern": d("knowledge_card"),
    "supervisor": d("agent", "agent_card"),
    # P09 Config
    "alert_rule": d("trace_config", "env_config"),
    "backpressure_policy": d("rate_limit_config"),
    "batch_config": d("env_config"),
    "cost_budget": d("env_config", "usage_quota"),
    "data_residency": d("env_config", "secret_config"),
    "effort_profile": d("env_config"),
    "env_config": [],  # foundational
    "experiment_config": d("env_config", "feature_flag"),
    "feature_flag": d("env_config"),
    "kubernetes_ai_requirement": d("deployment_manifest", "env_config"),
    "marketplace_app_manifest": d("agent_card", "env_config"),
    "oauth_app_config": d("secret_config", "env_config"),
    "path_config": d("env_config"),
    "permission": d("rbac_policy"),
    "playground_config": d("env_config", "sandbox_spec"),
    "prosody_config": d("env_config"),
    "quantization_config": d("model_card", "env_config"),
    "rate_limit_config": d("env_config"),
    "rbac_policy": d("env_config"),
    "retry_policy": d("env_config"),
    "runtime_rule": d("env_config"),
    "sandbox_spec": d("env_config"),
    "secret_config": [],  # foundational
    "sso_config": d("oauth_app_config", "secret_config"),
    "thinking_config": d("env_config"),
    "transport_config": d("env_config"),
    "usage_quota": d("rate_limit_config", "env_config"),
    "vad_config": d("env_config"),
    "white_label_config": d("env_config"),
    # P10 Memory
    "agent_grounding_record": d("entity_memory", "knowledge_index"),
    "c2pa_manifest": d("knowledge_card"),
    "compression_config": d("entity_memory", "memory_summary"),
    "consolidation_policy": d("entity_memory", "knowledge_index"),
    "episodic_memory": d("entity_memory"),
    "memory_architecture": d("entity_memory", "knowledge_index"),
    "memory_type": d("entity_memory"),
    "model_registry": d("model_card", "model_provider"),
    "procedural_memory": d("entity_memory"),
    "prospective_memory": d("entity_memory"),
    "runtime_state": d("session_state", "entity_memory"),
    "session_backend": d("entity_memory", "env_config"),
    "vc_credential": d("knowledge_card"),
    "workflow_run_crate": d("workflow", "knowledge_card"),
    "working_memory": d("entity_memory"),
    # P11 Feedback
    "ai_rmf_profile": d("safety_policy", "guardrail"),
    "audit_log": d("env_config", "knowledge_card"),
    "compliance_checklist": d("quality_gate", "knowledge_card"),
    "compliance_framework": d("compliance_checklist", "constitutional_rule"),
    "conformity_assessment": d("compliance_framework", "eval_metric"),
    "content_filter": d("guardrail"),
    "content_monetization": d("customer_segment", "subscription_tier"),
    "drift_detector": d("eval_metric", "regression_check"),
    "enterprise_sla": d("quality_gate", "env_config"),
    "gpai_technical_doc": d("ai_rmf_profile", "knowledge_card"),
    "hitl_config": d("quality_gate", "workflow"),
    "incident_report": d("audit_log", "knowledge_card"),
    "lifecycle_rule": d("env_config", "workflow"),
    "nps_survey": d("customer_segment", "knowledge_card"),
    "optimizer": d("eval_metric", "quality_gate"),
    "preference_dataset": d("eval_dataset", "customer_segment"),
    "referral_program": d("customer_segment", "knowledge_card"),
    "reward_signal": d("eval_metric"),
    "roi_calculator": d("customer_segment", "eval_metric"),
    "safety_hazard_taxonomy": d("safety_policy", "knowledge_card"),
    "safety_policy": d("guardrail", "constitutional_rule"),
    "self_improvement_loop": d("quality_gate", "reward_signal"),
    "subscription_tier": d("customer_segment"),
    "threat_model": d("safety_policy", "knowledge_card"),
    # P12 Orchestration
    "checkpoint": d("workflow"),
    "collaboration_pattern": d("workflow", "agent_card"),
    "dispatch_rule": d("workflow"),
    "domain_event": d("event_schema"),
    "handof": d("agent_card", "dispatch_rule"),
    "pipeline_template": d("workflow", "dispatch_rule"),
    "schedule": d("workflow"),
    "signal": d("workflow"),
    "spawn_config": d("agent", "env_config"),
    "state_machine": d("workflow", "dispatch_rule"),
    "visual_workflow": d("workflow", "diagram"),
    "workflow_node": d("workflow"),
}

valid_patches = {}
for kind in missing:
    if kind in PATCHES:
        valid_patches[kind] = PATCHES[kind]
    else:
        valid_patches[kind] = []

covered = len([k for k, v in valid_patches.items() if v])
no_deps = len([k for k, v in valid_patches.items() if not v])
uncovered = [k for k in missing if k not in PATCHES]

print(f"Patched: {len(valid_patches)} kinds")
print(f"With deps: {covered}")
print(f"Foundational (no deps): {no_deps}")
if uncovered:
    print(f"Uncovered ({len(uncovered)}):", uncovered)

output = {
    "schema": "kind_deps_patch/v1",
    "generated_by": "N07 FULL_COVERAGE W1 in-session",
    "kind_count": len(valid_patches),
    "with_deps": covered,
    "foundational": no_deps,
    "patches": valid_patches,
}
with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2)
print(f"[OK] {OUTPUT} written")
