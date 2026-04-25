---
quality: 8.2
quality: 7.6
id: p11_collab_curation_nudge
kind: handoff
pillar: P12
llm_function: COLLABORATE
purpose: F8 COLLABORATE signals and handoff protocol for curation_nudge builder
title: "Collaboration: Curation Nudge Builder"
version: "1.0.0"
author: n03_hermes_w1_8
tags: [collaboration, curation_nudge, builder, p12, f8, signals, handoff, memory]
domain: "curation_nudge construction"
created: "2026-04-18"
updated: "2026-04-18"
tldr: "F8 COLLABORATE signals and handoff protocol for curation_nudge builder"
density_score: 0.87
related:
  - bld_collaboration_memory_scope
  - bld_collaboration_memory_type
  - p02_agent_creation_nucleus
  - agent_card_n04
  - bld_collaboration_knowledge_graph
  - p12_ho_admin_template
  - bld_collaboration_knowledge_card
  - agent_card_engineering_nucleus
  - bld_collaboration_kind
  - kc_intent_resolution_map
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
git commit -m "[N03] build: curation_nudge/{trigger_type} via 8F pipeline"

# 4. Signal
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'complete', {score}, mission='curation_nudge_build')"
```

### Signal Format
```json
{
  "nucleus": "n03",
  "status": "complete",
  "quality_score": 9.0,
  "kind": "curation_nudge",
  "artifact": "p11_cn_{trigger_type}.yaml",
  "mission": "curation_nudge_build",
  "timestamp": "{iso8601}"
}
```

### Handoff to N04 (on confirmed nudge at runtime)
When an agent's nudge fires and knowledge is confirmed for persistence:
```markdown
## Handoff: curation_nudge Persistence
Trigger: {trigger_type} at threshold {threshold}
Observation: {observation}
Destination: {target_memory.destination}
Action: write confirmed knowledge to {destination}
```

### Cross-Builder Collaboration

| Builder | When to collaborate |
|---------|-------------------|
| `entity-memory-builder` | When destination=entity_memory and structured entity observed |
| `knowledge-card-builder` | When destination=knowledge_card and rich domain knowledge observed |
| `user-model-builder` | When nudge outputs feed Honcho long-term preference model |
| `memory-summary-builder` | When session ends and accumulated nudge output needs compression |

### Upstream/Downstream

| Direction | System | Signal |
|-----------|--------|--------|
| Upstream | N07 orchestrator (dispatched this build) | Write signal on complete |
| Downstream | Agent session that uses this nudge config | Nudge fires at threshold |
| Downstream | Target memory (MEMORY.md / entity_memory / knowledge_card) | Confirmed observations written |
| Peer | N04 knowledge nucleus | Owns memory destinations |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_memory_scope]] | related | 0.37 |
| [[bld_collaboration_memory_type]] | related | 0.29 |
| [[p02_agent_creation_nucleus]] | upstream | 0.27 |
| [[agent_card_n04]] | upstream | 0.27 |
| [[bld_collaboration_knowledge_graph]] | related | 0.27 |
| [[p12_ho_admin_template]] | sibling | 0.26 |
| [[bld_collaboration_knowledge_card]] | related | 0.26 |
| [[agent_card_engineering_nucleus]] | upstream | 0.25 |
| [[bld_collaboration_kind]] | related | 0.24 |
| [[kc_intent_resolution_map]] | upstream | 0.24 |
