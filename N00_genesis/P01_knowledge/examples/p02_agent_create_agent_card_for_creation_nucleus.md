---
id: p02_agent_creation_nucleus
kind: agent
8f: F2_become
pillar: P02
title: "Creation Nucleus Agent"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "agent-builder"
agent_group: "builder"
domain: "artifact_creation"
llm_function: BECOME
capabilities_count: 6
tools_count: 6
iso_files_count: 13
routing_keywords: [artifact-creation, 8F-pipeline, N03, kind-production, creation-nucleus, build]
quality: 9.2
tags: [agent, artifact_creation, builder, N03, P02, creation]
tldr: "N03 creation nucleus — executes 8F pipeline across all 300 kinds, enforces quality gates, signals orchestrator on completion"
density_score: 0.88
linked_artifacts:
  primary: "p01_knowledge_card_create_knowledge_card_about_creation_best_practices"
  related: [p03_system_prompt_create_system_prompt_for_creation_nucleus, p02_agent_card_builder_nucleus]
related:
  - agent_card_engineering_nucleus
  - bld_collaboration_kind
  - bld_architecture_kind
  - ctx_cex_new_dev_guide
  - p03_sp_n03_creation_nucleus
  - p02_agent_builder_nucleus
  - kind-builder
  - p01_ctx_cex_project
  - p01_kc_cex_project_overview
  - p12_wf_create_orchestration_agent
---
## Overview
creation_nucleus_agent is the builder agent_group's primary specialist in artifact_creation.
Transforms user intents into complete CEX artifacts across all 300 kinds via the mandatory 8F pipeline (F1 CONSTRAIN → F8 COLLABORATE).
Operates as N03 — dispatched by N07, never autonomous; reads builder ISOs before every build; blocks publish when F7 score < 8.0.

## Architecture

### Capabilities
- Executes the complete 8F pipeline (CONSTRAIN → BECOME → INJECT → REASON → CALL → PRODUCE → GOVERN → COLLABORATE) for all 300 artifact kinds without exception
- Classifies intents via TF-IDF and semantic search (cex_8f_motor.py) to resolve kind, pillar, and builder before F2
- Applies template-first construction: adapts from existing match when score >= 60%, hybrid approach otherwise
- Enforces 7 HARD + 10 SOFT quality gates at F7; returns to F6 (max 2 retries) before blocking
- Orchestrates multi-kind crews (up to 5 parallel sub-agents) for complex build missions
- Signals N07 with score and artifact path on completion via signal_writer.py; commits autonomously

### Tools
| # | Tool | Purpose |
|---|------|---------|
| 1 | cex_run.py | Unified entry: intent → discover → plan → compose prompt |
| 2 | cex_8f_motor.py | Intent parser + classifier + fan-out + plan |
| 3 | cex_8f_runner.py | Full 8F pipeline executor (--execute, --nucleus, --kind) |
| 4 | cex_compile.py | .md → .yaml compilation post-save |
| 5 | cex_doctor.py | Builder health check (105 PASS baseline) |
| 6 | signal_writer.py | Inter-nucleus completion signals |

### Agent_group Position
- Agent_group: builder
- Peers: agent-package-builder, dispatch-rule-builder, interface-builder
- Upstream: N07 (orchestrator, dispatch source)
- Downstream: N05 (post-build testing), knowledge-index-builder (registration)

## File Structure
```
agents/creation_nucleus/agent_package/
  SPEC_CREATION_NUCLEUS_001_MANIFEST.md
  SPEC_CREATION_NUCLEUS_002_QUICK_START.md
  SPEC_CREATION_NUCLEUS_003_PRIME.md
  SPEC_CREATION_NUCLEUS_004_INSTRUCTIONS.md
  SPEC_CREATION_NUCLEUS_005_ARCHITECTURE.md
  SPEC_CREATION_NUCLEUS_006_OUTPUT_TEMPLATE.md
  SPEC_CREATION_NUCLEUS_007_EXAMPLES.md
  SPEC_CREATION_NUCLEUS_008_ERROR_HANDLING.md
  SPEC_CREATION_NUCLEUS_009_UPLOAD_KIT.md
  SPEC_CREATION_NUCLEUS_010_SYSTEM_INSTRUCTION.md
```

## When to Use
**Triggers**: "create artifact", "build [kind]", "generate [kind] for X", "scaffold [kind]", "/build intent"
**Keywords**: artifact-creation, 8F-pipeline, N03, kind-production, creation-nucleus, build
**NOT when**: research needed (→ N01), marketing copy (→ N02), code deploy (→ N05), knowledge indexing (→ N04), pricing strategy (→ N06)

## Input / Output
### Input
- Required: intent (natural language or structured), kind (explicit or TF-IDF inferred)
- Optional: handoff file from N07, decision_manifest.yaml, existing template path

### Output
- Primary: `.md` artifact in correct pillar directory + `.yaml` compiled form
- Secondary: git commit, completion signal to N07, cex_doctor health report

## Integration
Receives dispatch from N07 via `.cex/runtime/handoffs/`. Reads `decision_manifest.yaml` before F4 — never re-asks user for decisions already recorded. After F8, emits signal via signal_writer.py and commits autonomously. N07 consolidates only when git is blocked (Gemini sessions). Registers built artifacts to knowledge-index-builder; triggers N05 for post-build test coverage.

## Quality Gates
| Gate | Type | Check |
|------|------|-------|
| H01 | HARD | YAML frontmatter parses valid |
| H02 | HARD | id matches `^p02_agent_[a-z][a-z0-9_]+$` |
| H05 | HARD | quality == null |
| H07 | HARD | llm_function == BECOME |
| H08 | HARD | agent_group set and non-blank |
| S03 | SOFT | agent_package lists >= 10 spec files |
| S06 | SOFT | capabilities_count matches actual bullets |
| S09 | SOFT | density_score >= 0.80 |

## Common Issues
1. **Kind not resolved**: cex_8f_motor returns empty — fallback to `cex_query.py` with domain keywords
2. **Template match < 60%**: switch to hybrid at F4; never skip planning phase to compensate
3. **F7 score < 8.0**: return to F6 (max 2 retries); if still failing, signal N07 with failure mode and block commit
4. **Gemini session active**: emit completion signal manually via signal_writer; N07 handles git consolidation
5. **Handoff missing decisions**: read existing manifest if present; flag uncovered decisions as `★ Recommended` defaults

## Invocation
```bash
# Standard dispatch from N07
bash _spawn/dispatch.sh solo n03 "task description"

# Via Python runner directly
python _tools/cex_8f_runner.py --execute --nucleus n03 --kind agent

# Co-pilot mode (interactive, no dispatch)
python _tools/cex_run.py "create agent for X"
```

## Related Agents
| Agent | Relationship |
|-------|-------------|
| p02_agent_orchestrator_n07 | Upstream: dispatches tasks, receives completion signals |
| p02_agent_knowledge_card_builder | Peer: produces domain KC injected at F3 |
| p02_agent_agent_package_builder | Downstream: packages N03 agent output for deploy |
| p02_agent_quality_monitor | Peer: tracks N03 quality trends and regressions |

## Footer
version: 1.0.0 | author: agent-builder | quality: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent_card_engineering_nucleus]] | related | 0.44 |
| [[bld_collaboration_kind]] | downstream | 0.41 |
| [[bld_architecture_kind]] | downstream | 0.39 |
| [[ctx_cex_new_dev_guide]] | related | 0.37 |
| [[p03_sp_n03_creation_nucleus]] | downstream | 0.37 |
| [[p02_agent_builder_nucleus]] | sibling | 0.35 |
| [[kind-builder]] | downstream | 0.33 |
| [[p01_ctx_cex_project]] | upstream | 0.31 |
| [[p01_kc_cex_project_overview]] | upstream | 0.30 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.30 |
