---
quality: 8.2
quality: 7.6
id: p11_collab_revision_loop_policy
kind: handoff
pillar: P12
llm_function: COLLABORATE
purpose: F8 COLLABORATE signals and handoff protocol for revision_loop_policy builder
title: "Collaboration: Revision Loop Policy Builder"
version: "1.0.0"
author: n03_hermes_w1_6
tags: [collaboration, revision_loop_policy, builder, p12, f8, signals, handoff]
domain: "revision_loop_policy construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.87
related:
  - p02_agent_creation_nucleus
  - agent_card_engineering_nucleus
  - p12_ho_admin_template
  - p03_sp_n03_creation_nucleus
  - bld_collaboration_quality_gate
  - p11_qg_admin_orchestration
  - bld_collaboration_kind
  - bld_collaboration_handoff_protocol
  - p12_sig_admin_orchestration
  - bld_collaboration_signal
---

## F8 COLLABORATE Protocol

### On Build Complete
```bash
# 1. Compile
python _tools/cex_compile.py {artifact_path}

# 2. Index (if available)
python _tools/cex_index.py 2>/dev/null || true

# 3. Commit
git add {artifact_path} {compiled_yaml_path}
git commit -m "[N03] build: revision_loop_policy/{name} via 8F pipeline"

# 4. Signal
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'complete', {score}, mission='revision_loop_policy_build')"
```

### Signal Format
```json
{
  "nucleus": "n03",
  "status": "complete",
  "quality_score": 9.0,
  "kind": "revision_loop_policy",
  "artifact": "p11_rlp_{name}.yaml",
  "mission": "revision_loop_policy_build",
  "timestamp": "{iso8601}"
}
```

### Handoff to N07 (on escalation)
When an artifact exhausts its revision budget and escalates to `senior_nucleus`:
```markdown
## Handoff: revision_loop_policy Escalation
Artifact: {artifact_path}
Iterations exhausted: {max_iterations}
Failing gates: {failing_gates}
Recommended action: review gate failures, adjust artifact manually or lower quality floor
```

### Cross-Builder Collaboration

| Builder | When to collaborate |
|---------|-------------------|
| `quality-gate-builder` | When defining per-gate thresholds embedded in revision cycles |
| `pipeline-template-builder` | When revision_loop_policy is embedded in a pipeline stage |
| `bugloop-builder` | When code-specific correction is needed alongside content revision |

### Upstream/Downstream

| Direction | System | Signal |
|-----------|--------|--------|
| Upstream | N07 orchestrator (dispatched this build) | Write signal on complete |
| Downstream | pipeline_template that references this policy | Policy `rlp_{{name}}` available for embedding |
| Peer | quality_gate artifacts (evaluated each iteration) | Read quality_gate results at F7 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_agent_creation_nucleus]] | upstream | 0.33 |
| [[agent_card_engineering_nucleus]] | upstream | 0.32 |
| [[p12_ho_admin_template]] | sibling | 0.31 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.31 |
| [[bld_collaboration_quality_gate]] | upstream | 0.30 |
| [[p11_qg_admin_orchestration]] | upstream | 0.27 |
| [[bld_collaboration_kind]] | related | 0.27 |
| [[bld_collaboration_handoff_protocol]] | related | 0.26 |
| [[p12_sig_admin_orchestration]] | related | 0.25 |
| [[bld_collaboration_signal]] | related | 0.24 |
