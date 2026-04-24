---
id: component_map_n05
kind: component_map
8f: F4_reason
pillar: P08
nucleus: n05
title: "N05 Operations -- Component Map"
version: 1.0.0
created: 2026-04-18
author: n07_admin
domain: operations-ci-architecture
quality: 8.7
tags: [component_map, n05, operations, ci_cd, testing, architecture]
tldr: "Internal component map of N05 Operations nucleus: quality gates, test runners, CI/CD pipeline, config management, MCP servers, and inter-nucleus data flows."
density_score: null
related:
  - agent_card_n03
  - p01_kc_git_hooks_ci
  - kc_intent_resolution_map
  - leverage_map_v2_n05_verify
  - agent_card_n05
  - p12_wf_create_orchestration_agent
  - self_audit_n05_20260408
  - p04_hook_pre_commit_qa
  - self_audit_n05_codex_2026_04_15
  - p01_kc_cex_project_overview
---

# N05 Operations -- Component Map

## System Overview

N05 is the code quality, CI/CD, and infrastructure nucleus. Its primary function
is enforcing correctness, managing runtime config, and deploying artifacts.
All work flows through 8F: CONSTRAIN kind/pillar -> BECOME gatekeeper
-> INJECT test KCs -> REASON over quality gaps -> CALL test runners
-> PRODUCE quality_gate/env_config -> GOVERN ruthlessly -> COLLABORATE.

**Sin Lens**: Gating Wrath -- merciless at the quality gate. Breaks what must break.
Zero tolerance for untested, unconfigured, or undocumented production artifacts.

---

## Artifact Inventory

| Pillar | Count | Primary Kinds |
|--------|------:|---------------|
| P01 Knowledge | 20 | knowledge_card, rag_source, context_doc |
| P02 Model | 5 | agent, boot_config, nucleus_def |
| P03 Prompt | 6 | system_prompt, prompt_template, context_file |
| P04 Tools | 8 | mcp_server, cli_tool, webhook, browser_tool |
| P05 Output | 30 | integration_guide, quickstart, api_reference |
| P06 Schema | 13 | input_schema, validation_schema, openapi_spec |
| P07 Evals | 19 | quality_gate, smoke_eval, e2e_eval, benchmark |
| P08 Architecture | 7 | component_map, decision_record, naming_rule, supervisor |
| P09 Config | 17 | env_config, rate_limit_config, sandbox_config, hibernation_policy |
| P10 Memory | 9 | entity_memory, session_state, prompt_cache |
| P11 Feedback | 11 | bugloop, regression_check, learning_record, guardrail |
| P12 Orchestration | 7 | workflow, schedule, pipeline_template |

**Total: 156 artifacts**

---

## Internal Components

### C1 -- Quality Gate Stack
```
F7 GOVERN trigger
  |
  v
[C1.1] Structural check  -- frontmatter, naming, file size
  |
  v
[C1.2] Rubric scoring    -- 5D: content, structure, density, completeness, coherence
  |
  v
[C1.3] LLM judge         -- cex_score.py --hybrid (when L1+L2 >= 8.5)
  |
  v
[C1.4] Quality gate      -- PASS (>= 8.0) or FAIL (re-run F6)
  |
  v
cex_hooks.py             -- pre-commit validation on staged artifacts
```

### C2 -- CI/CD Pipeline
```
git push / PR
  |
  v
.github/workflows/
  |-- claude_learn.yml   -- @.claude learn comment loop
  |-- ci.yml             -- build + test + lint
  |
  v
cex_hooks_native.py      -- session-start / post-tool-use / stop hooks
  |
  v
cex_flywheel_audit.py    -- 109-check doc-vs-practice audit
```

### C3 -- Config Management
```
.cex/config/
  |-- nucleus_models.yaml    -- provider + model per nucleus
  |-- router_config.yaml     -- routing rules
  |-- rate_limits.yaml       -- concurrent limits
  |
  v
cex_router.py                -- multi-provider routing (L1/L2/L3)
cex_quota_check.py           -- provider health + quota
```

### C4 -- MCP Server Registry
```
.mcp.json (root)
  |
  +-- per-nucleus overlays
  |
  v
N05/P04/mcp_*.md             -- mcp_server kind artifacts
  |
  v
uvx mcp-server-{name}        -- runtime processes
```

### C5 -- F3b Auto-Persist Hook
```
cex_hooks_native.py stop()
  |
  +-- write_signal()
  +-- _persist_from_signal()  -- F3b: scan last commit -> entity extraction
  |
  v
cex_memory_update.py --observation "{entities from commit}"
```

---

## Data Flows

| Source | -> | N05 | -> | Destination |
|--------|----|----|-----|-------------|
| N03 built artifact | -> | quality_gate | -> | PASS/FAIL signal |
| N07 handoff | -> | test dispatch | -> | smoke_eval / e2e_eval |
| N05 env_config | -> | provision | -> | All nuclei env vars |
| N05 signal | -> | F8 COLLABORATE | -> | N07 consolidation |
| git commit | -> | pre-commit hook | -> | cex_hooks.py validation |

---

## Key Tools

| Tool | Function |
|------|----------|
| `cex_hooks.py` | Pre/post validation + git hook |
| `cex_hooks_native.py` | Native Claude hooks (session/tool/stop) |
| `cex_score.py` | 3-layer hybrid scoring |
| `cex_doctor.py` | Builder integrity (294 builders) |
| `cex_flywheel_audit.py` | 109-check system audit |
| `cex_system_test.py` | 54-test full validation |
| `cex_quota_check.py` | Provider health + quota |

---

## Gaps (from SELF_AUDIT)

| Gap | Severity | Status |
|-----|----------|--------|
| component_map missing until this file | MEDIUM | RESOLVED |
| P09 Config: only env_config had builder | HIGH | 9 new builders added in BOOTSTRAP_SELF_W1 |
| F3b auto-persist not triggered per-run | HIGH | WIRED in cex_hooks_native.py stop() |
| No handoff_ack protocol | MEDIUM | Spec written; cex_handoff_ack.py pending |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent_card_n03]] | upstream | 0.31 |
| [[p01_kc_git_hooks_ci]] | upstream | 0.30 |
| [[kc_intent_resolution_map]] | upstream | 0.30 |
| [[leverage_map_v2_n05_verify]] | downstream | 0.29 |
| [[agent_card_n05]] | upstream | 0.29 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.26 |
| [[self_audit_n05_20260408]] | upstream | 0.26 |
| [[p04_hook_pre_commit_qa]] | upstream | 0.26 |
| [[self_audit_n05_codex_2026_04_15]] | upstream | 0.26 |
| [[p01_kc_cex_project_overview]] | upstream | 0.26 |
