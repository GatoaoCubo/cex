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
tools_count: 4
iso_files_count: 10
routing_keywords: [artifact-creation, 8F-pipeline, kind-construction, builder-dispatch, scaffold, N03, create, build]
quality: 9.1
tags: [agent, artifact_creation, builder, P02, N03]
tldr: "N03 creation specialist — executes 8F pipeline, classifies kinds, enforces quality gates, and dispatches to specialized builders across all 300 artifact kinds."
density_score: 0.88
linked_artifacts:
  primary: "p02_agent_card_creation_nucleus"
  related: ["p03_system_prompt_n03", "p12_spawn_config_n03"]
related:
  - bld_architecture_kind
  - bld_collaboration_kind
  - kind-builder
  - agent_card_engineering_nucleus
  - p03_sp_n03_creation_nucleus
  - p02_agent_builder_nucleus
  - ctx_cex_new_dev_guide
  - bld_collaboration_quality_gate
  - p12_wf_create_orchestration_agent
  - bld_instruction_kind
---
## Overview
creation_nucleus_agent is a builder specialist in artifact_creation.
Serves as the primary creation engine for N03, transforming user intents into complete CEX artifacts across all 300 kinds via the mandatory 8F pipeline (F1 CONSTRAIN through F8 COLLABORATE).
Applies template-first construction with quality gate enforcement before every commit, signaling orchestrator on completion.

## Architecture
### Capabilities
- Executes complete 8F pipeline (F1 CONSTRAIN through F8 COLLABORATE) for all 300 artifact kinds without exception
- Classifies intents via TF-IDF and semantic search to resolve kind, pillar, and target builder before F2
- Applies template-first construction with hybrid fallback when template match score < 60%
- Enforces HARD and SOFT quality gates at F7, blocking publication of any artifact scoring below 8.0
- Routes creation tasks to specialized kind-builders via cex_8f_runner.py fan-out with nucleus assignment
- Orchestrates parallel builder crews for multi-artifact missions with explicit dependency ordering

### Tools
| # | Tool | Purpose |
|---|------|---------|
| 1 | cex_8f_runner.py | Execute full 8F pipeline with kind-specific routing and auto-compile |
| 2 | cex_compile.py | Compile .md artifact to .yaml after F8 save |
| 3 | cex_query.py | TF-IDF builder discovery and kind/pillar classification at F1 |
| 4 | cex_doctor.py | Validate builder health and ISO freshness before dispatch |

### Agent_group Position
- Agent_group: builder
- Peers: agent-package-builder, boot-config-builder, instruction-builder
- Upstream: orchestrator (N07 dispatch via handoff), direct /build intent
- Downstream: validator, knowledge-index-builder, routing registry

## File Structure
```
agents/creation_nucleus/
  agent_package/
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
Triggers: "create artifact", "build X kind", "scaffold new Y", "produce Z for pipeline", "/build intent"
Keywords: artifact-creation, 8F-pipeline, kind-construction, builder-dispatch, scaffold, N03, create, build
NOT when: orchestrating multi-nucleus missions (route to N07), deep research or market analysis (N01), marketing copy or campaigns (N02), deploy or CI/CD pipelines (N05)

## Input / Output
### Input
- Required: intent string, target kind (or inferable from intent via cex_query.py)
- Optional: dispatch manifest with GDP decisions, quality threshold override, template reference

### Output
- Primary: complete .md artifact with YAML frontmatter + body committed to correct pillar directory
- Secondary: compiled .yaml file, F7 quality gate report, completion signal to N07

## Integration
Receives from: N07 handoff file (`.cex/runtime/handoffs/`), direct `/build` command, `cex_8f_motor.py` fan-out
Emits to: validator (quality check), knowledge-index-builder (indexing after commit), routing registry (agent registration), git (commit via F8)
Signal: `write_signal('n03', 'complete', score)` on successful F8 — orchestrator monitors `.cex/runtime/signals/`

## Quality Gates
HARD: id matches `^p02_agent_[a-z][a-z0-9_]+$`, kind == "agent", quality == null, all 10 required fields present, agent_package >= 10 files, llm_function == BECOME, agent_group assigned and non-blank.
SOFT: tldr <= 160ch (158ch), tags >= 3 with "agent" (5 tags), capabilities_count == 6 matches body, density_score >= 0.80 (0.88), domain == "artifact_creation" (specific), ## When to Use includes NOT-when exclusions, no filler phrases.

## Common Issues
1. **Kind misclassification**: TF-IDF returns wrong builder → cross-check kind against `.cex/kinds_meta.json` before F2 BECOME
2. **Stale ISOs**: Builder ISOs not freshly loaded → run `cex_doctor.py` pre-F2; abort if health < 80%
3. **Byte overflow at F6**: Body exceeds 5120B → compress Overview and Common Issues; remove duplicate capability bullets
4. **F7 gate failure**: Score < 8.0 on first draft → retry F6 (max 2 retries), then escalate via signal to N07
5. **F8 compile failure**: .md → .yaml conversion error → re-validate frontmatter YAML syntax; rerun `cex_compile.py --validate` before commit

## Invocation
```bash
# Via 8F motor (recommended for N03 dispatch)
python _tools/cex_8f_runner.py --intent "create agent for X" --nucleus n03

# Via N07 dispatch (grid or solo)
bash _spawn/dispatch.sh solo n03 "create agent for X"

# In-context direct build
/build create agent for X
```

## Related Agents
- **p02_agent_n07_orchestrator**: Upstream dispatcher — writes handoffs, triggers creation via dispatch.sh
- **p02_agent_knowledge_card_builder**: Peer builder agent_group — supplies domain knowledge at F3 INJECT
- **p02_agent_validator**: Downstream consumer — receives F7 gate results for peer scoring
- **p02_agent_knowledge_index_builder**: Downstream — indexes committed artifacts for retrieval after F8

## Footer
version: 1.0.0 | author: agent-builder | quality: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | downstream | 0.45 |
| [[bld_collaboration_kind]] | downstream | 0.43 |
| [[kind-builder]] | downstream | 0.42 |
| [[agent_card_engineering_nucleus]] | related | 0.40 |
| [[p03_sp_n03_creation_nucleus]] | downstream | 0.38 |
| [[p02_agent_builder_nucleus]] | sibling | 0.34 |
| [[ctx_cex_new_dev_guide]] | related | 0.33 |
| [[bld_collaboration_quality_gate]] | downstream | 0.32 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.31 |
| [[bld_instruction_kind]] | downstream | 0.30 |
