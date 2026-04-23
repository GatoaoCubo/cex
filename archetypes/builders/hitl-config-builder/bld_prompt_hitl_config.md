---
kind: instruction
id: bld_instruction_hitl_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for hitl_config
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Hitl Config"
version: "1.0.0"
author: n03_builder
tags: [hitl_config, builder, instruction, P11]
tldr: "3-phase build process for hitl_config: research workflow + compose gate spec + validate all HARD gates."
domain: "hitl_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - p11_qg_hitl_config
  - bld_knowledge_card_hitl_config
  - bld_instruction_output_validator
  - p03_sp_hitl_config_builder
  - bld_instruction_context_doc
  - p01_kc_hitl_config
  - bld_instruction_retriever_config
  - bld_instruction_memory_scope
  - bld_instruction_handoff_protocol
  - bld_instruction_chunk_strategy
---

# Instructions: How to Produce a hitl_config
## Phase 1: RESEARCH
1. Identify the workflow: what AI process outputs are being reviewed? (e.g., content generation, code review, medical diagnosis support)
2. Determine WHY human review is needed: regulatory requirement, high stakes, model uncertainty, edge case domain
3. Define the review_trigger condition precisely: what score, flag, or output property routes to human? (confidence threshold, domain label, toxicity score, output category)
4. Identify the reviewer population: who has the expertise to judge this output? Map to roles (L1: generalist, L2: domain expert, L3: senior/legal/admin)
5. Determine approval_flow type: binary (simple accept/reject), edit (reviewer modifies output), or score (reviewer rates quality numerically)
6. Set realistic timeout_seconds based on SLA requirements and reviewer availability (default: 3600 for async, 300 for real-time)
7. Choose fallback_action: reject (safe for high-risk), accept_with_flag (low-risk with audit), retry (model can be re-run)
8. Check existing hitl_configs in P11/examples/ for the same workflow -- do not duplicate a gate that already covers this scope
## Phase 2: COMPOSE
1. Read SCHEMA.md -- source of truth for all fields
2. Read OUTPUT_TEMPLATE.md -- fill the template following SCHEMA constraints
3. Fill all required frontmatter fields; set `quality: null` -- never self-score
4. Write **Overview** section: what workflow, why human judgment is required, who is affected downstream
5. Write **Review Trigger** section: exact condition(s) as evaluable expressions; include threshold values; note what data the condition reads
6. Write **Escalation Chain** section: table with columns level, role, SLA (minutes), contact channel, escalation condition
7. Write **Approval Flow** section: which flow type (binary/edit/score), what each reviewer action means, how approved/rejected outputs are handled downstream
8. Write **Timeout and Fallback** section: timeout_seconds value, which escalation level it applies to, fallback_action and justification for why that fallback is appropriate for this risk level
9. Add optional **Priority Rules** section if high-risk outputs need fast-lane routing to senior reviewers
10. Add optional **Feedback Loop** section if review decisions should feed back to model training
11. Confirm body <= 3072 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md -- verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm `id` matches `^p11_hitl_[a-z][a-z0-9_]+$`
4. Confirm escalation_chain list has >= 2 roles
5. Confirm approval_flow is one of: binary, edit, score
6. Confirm fallback_action is one of: reject, accept_with_flag, retry
7. Confirm timeout_seconds > 0
8. Confirm no reviewer SLA is longer than timeout_seconds (escalation chain must fit within timeout)
9. Confirm review_trigger is a precise, evaluable condition -- not vague prose
10. Confirm `quality` is null
11. Confirm body <= 3072 bytes
12. Cross-check: does this require human judgment? If it can be fully automated, it belongs in `guardrail` (automated block) or `quality_gate` (automated score). hitl_config is ONLY for cases where human decision is required.
13. If score < 8.0: revise in the same pass before outputting


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_hitl_config]] | downstream | 0.41 |
| [[bld_knowledge_card_hitl_config]] | upstream | 0.39 |
| [[bld_instruction_output_validator]] | sibling | 0.39 |
| [[p03_sp_hitl_config_builder]] | related | 0.39 |
| [[bld_instruction_context_doc]] | sibling | 0.38 |
| [[p01_kc_hitl_config]] | downstream | 0.38 |
| [[bld_instruction_retriever_config]] | sibling | 0.37 |
| [[bld_instruction_memory_scope]] | sibling | 0.37 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.37 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.36 |
