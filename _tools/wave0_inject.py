"""Wave 0: Inject 52 new kinds into kinds_meta.json."""
import json
import sys

META = ".cex/kinds_meta.json"

NEW_KINDS = {
    "threat_model": {
        "pillar": "P11", "llm_function": "GOVERN", "naming": "p11_tm_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "Structured hazard/risk assessment for AI systems",
        "boundary": "Threat/risk assessment. NOT safety_policy (governance rules) nor guardrail (runtime filter)."
    },
    "safety_policy": {
        "pillar": "P11", "llm_function": "CONSTRAIN", "naming": "p11_sp_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "Organizational AI safety governance rules",
        "boundary": "Safety governance rules. NOT threat_model (risk assessment) nor compliance_framework (regulatory mapping)."
    },
    "content_filter": {
        "pillar": "P11", "llm_function": "GOVERN", "naming": "p11_cf_{{name}}.md", "max_bytes": 4096,
        "core": False, "description": "Input/output content filtering pipeline config",
        "boundary": "Content filtering pipeline. NOT guardrail (broad safety constraint) nor output_validator (schema check)."
    },
    "bias_audit": {
        "pillar": "P07", "llm_function": "GOVERN", "naming": "p07_ba_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "Fairness evaluation methodology and results",
        "boundary": "Fairness evaluation. NOT benchmark (general perf) nor eval_metric (single metric def)."
    },
    "compliance_framework": {
        "pillar": "P11", "llm_function": "CONSTRAIN", "naming": "p11_cfw_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "Regulatory mapping and attestation for AI systems",
        "boundary": "Regulatory compliance mapping. NOT safety_policy (org rules) nor threat_model (risk assessment)."
    },
    "incident_report": {
        "pillar": "P11", "llm_function": "GOVERN", "naming": "p11_ir_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "AI incident documentation and post-mortem",
        "boundary": "Incident post-mortem. NOT bugloop (auto-fix) nor learning_record (generic learning)."
    },
    "voice_pipeline": {
        "pillar": "P04", "llm_function": "CALL", "naming": "p04_vp_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "End-to-end voice agent architecture definition",
        "boundary": "Voice pipeline architecture. NOT tts_provider (single provider) nor stt_provider (single provider)."
    },
    "realtime_session": {
        "pillar": "P09", "llm_function": "CALL", "naming": "p09_rs_{{name}}.md", "max_bytes": 4096,
        "core": False, "description": "Live bidirectional session configuration",
        "boundary": "Realtime session config. NOT transport_config (network layer) nor voice_pipeline (full architecture)."
    },
    "vad_config": {
        "pillar": "P09", "llm_function": "CONSTRAIN", "naming": "p09_vad_{{name}}.yaml", "max_bytes": 2048,
        "core": False, "description": "Voice activity detection settings",
        "boundary": "VAD settings only. NOT voice_pipeline (full arch) nor stt_provider (transcription)."
    },
    "tts_provider": {
        "pillar": "P04", "llm_function": "CALL", "naming": "p04_tts_{{name}}.md", "max_bytes": 4096,
        "core": False, "description": "Text-to-speech provider integration",
        "boundary": "TTS provider integration. NOT voice_pipeline (full arch) nor prosody_config (voice personality)."
    },
    "stt_provider": {
        "pillar": "P04", "llm_function": "CALL", "naming": "p04_stt_{{name}}.md", "max_bytes": 4096,
        "core": False, "description": "Speech-to-text provider integration",
        "boundary": "STT provider integration. NOT voice_pipeline (full arch) nor vad_config (detection settings)."
    },
    "prosody_config": {
        "pillar": "P09", "llm_function": "CONSTRAIN", "naming": "p09_prs_{{name}}.yaml", "max_bytes": 2048,
        "core": False, "description": "Voice personality and emotion settings",
        "boundary": "Prosody/emotion settings. NOT tts_provider (provider integration) nor agent_profile (agent persona)."
    },
    "transport_config": {
        "pillar": "P09", "llm_function": "CONSTRAIN", "naming": "p09_tc_{{name}}.yaml", "max_bytes": 2048,
        "core": False, "description": "Network transport layer for realtime communication",
        "boundary": "Transport layer config. NOT realtime_session (session lifecycle) nor streaming_config (LLM streaming)."
    },
    "edit_format": {
        "pillar": "P06", "llm_function": "CONSTRAIN", "naming": "p06_ef_{{name}}.md", "max_bytes": 4096,
        "core": False, "description": "LLM-to-host file change format specification",
        "boundary": "Edit format spec. NOT diff_strategy (matching algo) nor formatter (output formatting)."
    },
    "sandbox_config": {
        "pillar": "P09", "llm_function": "CONSTRAIN", "naming": "p09_sb_{{name}}.yaml", "max_bytes": 2048,
        "core": False, "description": "Isolated code execution environment config",
        "boundary": "Sandbox/isolation config. NOT env_config (environment vars) nor code_executor (execution logic)."
    },
    "repo_map": {
        "pillar": "P01", "llm_function": "INJECT", "naming": "p01_rm_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "Codebase context extraction strategy",
        "boundary": "Repo context map. NOT component_map (system architecture) nor knowledge_index (search index)."
    },
    "diff_strategy": {
        "pillar": "P04", "llm_function": "CALL", "naming": "p04_ds_{{name}}.md", "max_bytes": 4096,
        "core": False, "description": "Change application and matching algorithm",
        "boundary": "Diff matching strategy. NOT edit_format (format spec) nor parser (generic parsing)."
    },
    "agent_computer_interface": {
        "pillar": "P08", "llm_function": "CALL", "naming": "p08_aci_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "GUI/terminal interaction protocol for agents",
        "boundary": "Agent-computer interface. NOT browser_tool (web automation) nor computer_use (screen control)."
    },
    "reasoning_strategy": {
        "pillar": "P03", "llm_function": "REASON", "naming": "p03_rs_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "Prompting technique for structured reasoning",
        "boundary": "Reasoning technique. NOT prompt_technique (generic prompt pattern) nor thinking_config (budget settings)."
    },
    "rl_algorithm": {
        "pillar": "P02", "llm_function": "BECOME", "naming": "p02_rla_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "Reinforcement learning training algorithm definition",
        "boundary": "RL algorithm def. NOT training_method (broader training) nor reward_model (reward function)."
    },
    "reward_model": {
        "pillar": "P07", "llm_function": "GOVERN", "naming": "p07_rwm_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "Process/outcome reward model configuration",
        "boundary": "Reward model config. NOT rl_algorithm (training algo) nor scoring_rubric (human eval rubric)."
    },
    "search_strategy": {
        "pillar": "P04", "llm_function": "CALL", "naming": "p04_ss_{{name}}.md", "max_bytes": 4096,
        "core": False, "description": "Inference-time compute allocation strategy",
        "boundary": "Search/inference strategy. NOT reasoning_strategy (prompt technique) nor retriever (document retrieval)."
    },
    "thinking_config": {
        "pillar": "P09", "llm_function": "CONSTRAIN", "naming": "p09_thk_{{name}}.yaml", "max_bytes": 2048,
        "core": False, "description": "Extended thinking and budget token settings",
        "boundary": "Thinking budget config. NOT reasoning_strategy (technique) nor context_window_config (token limits)."
    },
    "training_method": {
        "pillar": "P02", "llm_function": "BECOME", "naming": "p02_trm_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "Model training/adaptation technique definition",
        "boundary": "Training technique. NOT rl_algorithm (RL-specific) nor finetune_config (runtime fine-tune settings)."
    },
    "model_architecture": {
        "pillar": "P02", "llm_function": "BECOME", "naming": "p02_ma_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "Neural network architecture definition",
        "boundary": "Architecture definition. NOT model_card (deployment spec) nor model_provider (API integration)."
    },
    "dataset_card": {
        "pillar": "P01", "llm_function": "INJECT", "naming": "p01_dc_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "Structured dataset documentation",
        "boundary": "Dataset documentation. NOT eval_dataset (eval-specific data) nor knowledge_card (general knowledge)."
    },
    "model_registry": {
        "pillar": "P10", "llm_function": "GOVERN", "naming": "p10_mr_{{name}}.md", "max_bytes": 4096,
        "core": False, "description": "Model versioning and artifact tracking",
        "boundary": "Model registry. NOT model_card (single model spec) nor checkpoint (training snapshot)."
    },
    "experiment_tracker": {
        "pillar": "P07", "llm_function": "GOVERN", "naming": "p07_et_{{name}}.md", "max_bytes": 4096,
        "core": False, "description": "Experiment configuration and results tracking",
        "boundary": "Experiment tracking. NOT benchmark (evaluation suite) nor experiment_config (single experiment settings)."
    },
    "quantization_config": {
        "pillar": "P09", "llm_function": "CONSTRAIN", "naming": "p09_qc_{{name}}.yaml", "max_bytes": 2048,
        "core": False, "description": "Model quantization and compression settings",
        "boundary": "Quantization settings. NOT compression_config (context compression) nor model_architecture (full arch)."
    },
    "benchmark_suite": {
        "pillar": "P07", "llm_function": "GOVERN", "naming": "p07_bs_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "Composite benchmark definition with multiple tasks",
        "boundary": "Benchmark suite. NOT benchmark (single benchmark) nor eval_framework (evaluation tooling)."
    },
    "judge_config": {
        "pillar": "P07", "llm_function": "GOVERN", "naming": "p07_jc_{{name}}.md", "max_bytes": 4096,
        "core": False, "description": "LLM judge configuration for automated evaluation",
        "boundary": "Judge config. NOT llm_judge (judge instance) nor scoring_rubric (human rubric)."
    },
    "eval_metric": {
        "pillar": "P07", "llm_function": "GOVERN", "naming": "p07_em_{{name}}.md", "max_bytes": 4096,
        "core": False, "description": "Individual evaluation metric definition",
        "boundary": "Single metric def. NOT benchmark_suite (composite) nor scoring_rubric (qualitative rubric)."
    },
    "eval_framework": {
        "pillar": "P07", "llm_function": "GOVERN", "naming": "p07_efw_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "End-to-end evaluation framework integration",
        "boundary": "Eval framework. NOT benchmark_suite (benchmark collection) nor eval_metric (single metric)."
    },
    "trajectory_eval": {
        "pillar": "P07", "llm_function": "GOVERN", "naming": "p07_te_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "Agent trajectory evaluation methodology",
        "boundary": "Trajectory evaluation. NOT benchmark (static eval) nor e2e_eval (end-to-end test)."
    },
    "reranker_config": {
        "pillar": "P01", "llm_function": "INJECT", "naming": "p01_rr_{{name}}.yaml", "max_bytes": 2048,
        "core": False, "description": "Retrieval reranking model and strategy config",
        "boundary": "Reranker config. NOT retriever_config (first-stage retrieval) nor retriever (retrieval logic)."
    },
    "graph_rag_config": {
        "pillar": "P01", "llm_function": "INJECT", "naming": "p01_grc_{{name}}.yaml", "max_bytes": 4096,
        "core": False, "description": "Graph-based RAG architecture configuration",
        "boundary": "Graph RAG config. NOT knowledge_graph (graph instance) nor rag_source (document source)."
    },
    "agentic_rag": {
        "pillar": "P01", "llm_function": "INJECT", "naming": "p01_ar_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "Agent-driven retrieval augmented generation pattern",
        "boundary": "Agentic RAG pattern. NOT retriever (simple retrieval) nor agent (agent definition)."
    },
    "memory_architecture": {
        "pillar": "P10", "llm_function": "INJECT", "naming": "p10_marc_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "Complete memory system architecture design",
        "boundary": "Memory system design. NOT memory_type (single type) nor memory_scope (access scope)."
    },
    "procedural_memory": {
        "pillar": "P10", "llm_function": "INJECT", "naming": "p10_pm_{{name}}.md", "max_bytes": 4096,
        "core": False, "description": "Skill and procedure storage/retrieval system",
        "boundary": "Procedural memory. NOT entity_memory (entity facts) nor knowledge_card (declarative knowledge)."
    },
    "consolidation_policy": {
        "pillar": "P10", "llm_function": "GOVERN", "naming": "p10_cp_{{name}}.md", "max_bytes": 4096,
        "core": False, "description": "Memory lifecycle management policy",
        "boundary": "Memory lifecycle policy. NOT memory_scope (access rules) nor compression_config (token compression)."
    },
    "memory_benchmark": {
        "pillar": "P07", "llm_function": "GOVERN", "naming": "p07_mb_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "Memory system quality evaluation suite",
        "boundary": "Memory eval suite. NOT benchmark_suite (general benchmarks) nor memory_architecture (system design)."
    },
    "agent_profile": {
        "pillar": "P02", "llm_function": "BECOME", "naming": "p02_ap_{{name}}.md", "max_bytes": 4096,
        "core": False, "description": "Agent persona and identity construction method",
        "boundary": "Agent persona construction. NOT agent (full agent def) nor system_prompt (how agent speaks)."
    },
    "planning_strategy": {
        "pillar": "P03", "llm_function": "REASON", "naming": "p03_ps_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "Agent planning approach definition",
        "boundary": "Planning approach. NOT reasoning_strategy (prompt reasoning) nor workflow (execution flow)."
    },
    "action_paradigm": {
        "pillar": "P04", "llm_function": "CALL", "naming": "p04_act_{{name}}.md", "max_bytes": 4096,
        "core": False, "description": "How agents execute actions in environments",
        "boundary": "Action execution paradigm. NOT agent_computer_interface (specific protocol) nor cli_tool (CLI wrapper)."
    },
    "collaboration_pattern": {
        "pillar": "P12", "llm_function": "COLLABORATE", "naming": "p12_collab_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "Multi-agent coordination topology",
        "boundary": "Coordination pattern. NOT workflow (execution sequence) nor handoff_protocol (handoff rules)."
    },
    "dual_loop_architecture": {
        "pillar": "P08", "llm_function": "REASON", "naming": "p08_dl_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "Outer/inner loop agent control architecture",
        "boundary": "Dual-loop control. NOT workflow (linear flow) nor collaboration_pattern (multi-agent topology)."
    },
    "workflow_node": {
        "pillar": "P12", "llm_function": "PRODUCE", "naming": "p12_wn_{{name}}.md", "max_bytes": 4096,
        "core": False, "description": "Typed node in visual/programmatic workflow",
        "boundary": "Workflow node type. NOT workflow (full workflow) nor visual_workflow (GUI editor config)."
    },
    "visual_workflow": {
        "pillar": "P12", "llm_function": "PRODUCE", "naming": "p12_vw_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "GUI-based workflow editor configuration",
        "boundary": "Visual workflow editor. NOT workflow (code-defined) nor dag (directed acyclic graph)."
    },
    "prompt_technique": {
        "pillar": "P03", "llm_function": "INJECT", "naming": "p03_pt_{{name}}.md", "max_bytes": 4096,
        "core": False, "description": "Specific prompting method or pattern",
        "boundary": "Prompt technique. NOT prompt_template (reusable template) nor reasoning_strategy (reasoning-specific)."
    },
    "prompt_optimizer": {
        "pillar": "P03", "llm_function": "GOVERN", "naming": "p03_po_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "Automated prompt improvement and compilation tool",
        "boundary": "Prompt optimizer. NOT prompt_compiler (CEX internal) nor optimizer (general optimization)."
    },
    "multimodal_prompt": {
        "pillar": "P03", "llm_function": "INJECT", "naming": "p03_mmp_{{name}}.md", "max_bytes": 4096,
        "core": False, "description": "Cross-modal prompt pattern for vision/audio/text",
        "boundary": "Multimodal prompt. NOT prompt_technique (text-only) nor multi_modal_config (model settings)."
    },
    "self_improvement_loop": {
        "pillar": "P11", "llm_function": "GOVERN", "naming": "p11_sil_{{name}}.md", "max_bytes": 5120,
        "core": False, "description": "Agent/system self-evolution mechanism",
        "boundary": "Self-improvement loop. NOT bugloop (bug-specific) nor learning_record (passive learning)."
    },
}


def main():
    with open(META, "r", encoding="utf-8") as f:
        data = json.load(f)

    before = len(data)
    added = 0
    skipped = 0

    for kind, entry in NEW_KINDS.items():
        if kind in data:
            print(f"[SKIP] {kind} already exists")
            skipped += 1
        else:
            data[kind] = entry
            added += 1

    data = dict(sorted(data.items()))

    with open(META, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"\n[OK] Before: {before} kinds")
    print(f"[OK] Added: {added} new kinds")
    print(f"[OK] Skipped: {skipped} (already existed)")
    print(f"[OK] Total: {len(data)} kinds")
    return 0


if __name__ == "__main__":
    sys.exit(main())
