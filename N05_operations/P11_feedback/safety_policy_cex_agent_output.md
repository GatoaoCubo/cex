---
quality: 8.9
quality: 8.4
id: p11_sp_cex_agent_output
kind: safety_policy
8f: F1_constrain
pillar: P11
title: "Safety Policy: CEX Agent Output Guardrails"
version: "1.0.0"
author: "n05_operations"
created: "2026-04-19"
updated: "2026-04-19"
domain: "agent_output_safety"
tags: [safety_policy, agent_output, guardrails, operations]
tldr: "Guardrails for CEX agent output: no hallucinated scores, no data leaks, no fabricated evidence, no unsafe code execution."
risk_level: "High"
compliance_frameworks: [eu_ai_act_2024, nist_ai_rmf, anthropic_usage_policy]
enforcement_mechanisms: [block, flag, log, escalate]
harm_taxonomy_sources: [cex_quality_system, anthropic_hhh, owasp_llm_top10]
related:
  - p03_sp_n03_creation_nucleus
  - p11_qg_orchestration_artifacts
  - ctx_cex_new_dev_guide
  - p01_ctx_cex_project
  - p03_sp_cex_core_identity
  - p12_wf_orchestration_pipeline
  - p12_sig_builder_nucleus
  - skill
  - agent_card_engineering_nucleus
  - p11_qg_creation_artifacts
density_score: 1.0
---

## 1. Purpose and Scope

**Purpose**: Governs all output produced by CEX nuclei (N01-N07) to prevent hallucinated quality scores, fabricated evidence, data leakage, and unsafe autonomous actions.

**Applies to**: All 8 nuclei (N00-N07), all 4 runtimes (Claude, Codex, Gemini, Ollama), all artifact kinds (300 kinds).

**Out of scope**: Input validation (see input_schema artifacts), infrastructure security (see threat_model_n05.md), brand voice compliance (see N06 policies).

## 2. Harm Category Table

| Category | Source | Threshold | Action | Basis |
|----------|--------|-----------|--------|-------|
| Hallucinated quality score | CEX quality system | Any non-null quality in self-produced artifact | BLOCK | 8F rule: quality: null always; peer-review assigns |
| Fabricated evidence | CEX quality system | Citation to nonexistent file/KC/artifact | BLOCK | F3c GROUND: all sources must be verifiable |
| Data leakage | OWASP LLM Top 10 (LLM06) | API keys, credentials, .env contents in output | BLOCK | Pre-commit hook + this policy |
| Prompt injection in artifact | OWASP LLM Top 10 (LLM01) | Injected instructions in artifact body targeting downstream consumers | FLAG | Downstream nuclei consume artifacts as context |
| Unsafe code execution | Anthropic usage policy | rm -rf, DROP TABLE, force-push without user confirmation | BLOCK | N07 autonomous lifecycle: confirm destructive actions |
| Score inflation | CEX quality system | Nucleus self-scores above 8.0 or claims golden status | BLOCK | cex_score.py --apply is the only valid scorer |
| Phantom artifact reference | CEX quality system | References artifact path that does not exist on disk | FLAG | F5 CALL: verify artifact existence before citing |
| Ollama fabricated signals | Empirical (2026-04-15) | Signal file written without actual artifact production | BLOCK | Multi-runtime verification rule: verify deliverables before trusting signal |

## 3. Enforcement Actions

| Action | Behavior | SLA | Audit Record |
|--------|----------|-----|--------------|
| BLOCK | Artifact rejected; not saved to disk; nucleus must retry via F6 | Immediate | Log: category, nucleus, artifact_id, timestamp |
| FLAG | Artifact saved but marked for human review in consolidation | Next consolidation cycle | Flagged in cex_doctor.py output |
| LOG | Artifact saved normally; event recorded for trend analysis | None | Append to .cex/runtime/audit/safety_events.jsonl |
| ESCALATE | Artifact blocked; N07 notified; user prompted for decision | Within current session | Full context dump to .cex/runtime/signals/ |

## 4. Detection Rules

| Rule ID | Category | Detection Method | Automation |
|---------|----------|-----------------|-----------|
| SR01 | Hallucinated score | Frontmatter parse: quality field != null in self-produced artifact | cex_hooks.py pre-commit |
| SR02 | Fabricated evidence | F3c GROUND: check file existence for every cited path | cex_doctor.py --refs |
| SR03 | Data leakage | Regex scan for API key patterns, env var dumps, credential strings | cex_sanitize.py --check |
| SR04 | Prompt injection | Scan artifact body for instruction-like patterns targeting LLM consumers | Manual review at consolidation |
| SR05 | Unsafe code | Scan bash/powershell commands for destructive patterns without confirmation | cex_hooks.py pre-tool-use |
| SR06 | Score inflation | Cross-check: did the scoring nucleus also produce the artifact? | cex_score.py --validate-scorer |
| SR07 | Phantom reference | Glob check: does every path in artifact body resolve to a real file? | cex_doctor.py --refs |
| SR08 | Ollama fake signal | Compare signal timestamp vs git log: did artifact commit precede signal? | cex_signal_watch.py --verify |

## 5. Incident Response Protocol

**Critical** (data leakage, unsafe code execution):
1. BLOCK immediately
2. Halt nucleus process (taskkill /F /PID /T)
3. Scan last 10 commits from nucleus for similar violations
4. Notify user with full context
5. Do NOT auto-retry; require explicit user approval

**High** (hallucinated scores, fabricated evidence, Ollama fake signals):
1. BLOCK artifact
2. Log violation with nucleus ID and artifact path
3. Re-dispatch with explicit instruction to avoid violation
4. If repeat offense (>2 in session): halt nucleus, notify user

**Medium** (prompt injection, phantom references):
1. FLAG artifact
2. Queue for human review at consolidation
3. Auto-fix if possible (remove phantom refs, strip injected instructions)

## 6. Runtime-Specific Considerations

| Runtime | Known Risk | Mitigation |
|---------|-----------|-----------|
| Claude | Low risk; follows instructions reliably | Standard policy enforcement |
| Codex | Exits without committing; may leave partial artifacts | N07 verifies + commits (feedback_codex_no_autocommit) |
| Gemini | May hallucinate file paths; cannot git | N07 commits for Gemini; verify all paths |
| Ollama | Fabricates KC evidence; fake-signals completion | Verify deliverables + commit before trusting signal (feedback_multiruntime_verification) |

## 7. Review and Update Protocol

- Review trigger: (a) new harm category discovered in production, (b) new runtime added, (c) quarterly scheduled review
- Owner: N05 Operations
- Approval: N07 Orchestrator review
- Version history: maintained in git, semantic versioning

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.28 |
| [[p11_qg_orchestration_artifacts]] | related | 0.27 |
| [[ctx_cex_new_dev_guide]] | related | 0.26 |
| [[p01_ctx_cex_project]] | upstream | 0.25 |
| [[p03_sp_cex_core_identity]] | upstream | 0.24 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.23 |
| [[p12_sig_builder_nucleus]] | downstream | 0.23 |
| [[skill]] | upstream | 0.23 |
| [[agent_card_engineering_nucleus]] | upstream | 0.23 |
| [[p11_qg_creation_artifacts]] | related | 0.22 |
