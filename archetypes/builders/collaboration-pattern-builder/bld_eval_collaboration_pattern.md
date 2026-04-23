---
kind: quality_gate
id: p11_qg_collaboration_pattern
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for collaboration_pattern artifacts
quality: 9.1
title: "Quality Gate: Collaboration Pattern"
version: "1.0.0"
author: n02_reviewer
tags: [collaboration_pattern, builder, quality_gate, P11]
tldr: "Quality gate for multi-agent coordination topology artifacts defining roles, channels, and synchronization rules."
domain: "collaboration_pattern construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - p11_qg_quality_gate
  - p11_qg_action_paradigm
  - p11_qg_response_format
  - p03_sp_collaboration_pattern_builder
  - p11_qg_voice_pipeline
  - p11_qg_prompt_template
  - p11_qg_thinking_config
  - p11_qg_runtime_state
  - bld_examples_collaboration_pattern
  - p11_qg_creation_artifacts
---

## Quality Gate

## Definition

A `collaboration_pattern` artifact defines the structural topology for how autonomous agents
interact to achieve shared goals. It specifies agent roles, communication channels,
coordination rules, and conflict resolution -- NOT sequential task workflows or handoff protocols.

Scope: files with `kind: collaboration_pattern`. Does NOT apply to workflows (sequential
execution), handoff_protocol (transfer rules), or dispatch_rule (routing logic).

## HARD Gates

Failure on any single gate means REJECT regardless of soft score.

| ID  | Predicate | How to test |
|-----|-----------|-------------|
| H01 | Frontmatter parses as valid YAML | `yaml.safe_load(frontmatter)` raises no error |
| H02 | `id` matches namespace `p12_collab_*` | `id.startswith("p12_collab_")` is true |
| H03 | `id` equals filename stem | `Path(file).stem == id` |
| H04 | `kind` equals literal `collaboration_pattern` | string equality check |
| H05 | `quality` is null at authoring time | `quality is None` |
| H06 | All required frontmatter fields present and non-empty | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr all present |
| H07 | Body defines at least 2 agent roles | `len(declared_agents) >= 2` |
| H08 | At least one communication channel or coordination rule declared | body contains channel or protocol definition |

## SOFT Scoring

Score each dimension 0 (absent or fails) to 1 (present and passes). Weights are 0.5 or 1.0.

| #  | Dimension | Weight |
|----|-----------|--------|
| 1  | `density_score` field present and >= 0.80 | 1.0 |
| 2  | Topology type declared (mesh, hierarchical, peer-to-peer, hub-and-spoke) | 1.0 |
| 3  | Communication channels explicitly named and directional | 1.0 |
| 4  | Conflict resolution or consensus mechanism documented | 1.0 |
| 5  | Failure handling or fault tolerance described | 0.5 |
| 6  | Tags include `collaboration_pattern` | 0.5 |
| 7  | Boundary note: distinguishes from workflow and handoff_protocol | 1.0 |
| 8  | Scalability or agent-count considerations documented | 0.5 |
| 9  | At least one concrete domain example or use case | 1.0 |
| 10 | Trust model or authority hierarchy declared | 0.5 |
| 11 | `tldr` is <= 160 characters | 0.5 |

**Formula**: `final_score = (sum of score_i * weight_i) / (sum of weight_i) * 10`
Weight total: 9.0. Score range: 0.0 to 10.0.

## Actions

| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool; add to curated pattern library |
| PUBLISH | >= 8.0 | Publish to pool; mark production-ready |
| REVIEW | >= 7.0 | Return to author with scored dimension feedback; one revision cycle |
| REJECT | < 7.0 | Block from pool; full rewrite required |

## Bypass

| Field | Value |
|-------|-------|
| condition | Pattern is a one-off experiment with documented lifespan under 30 days |
| approver | Domain lead must approve in writing |
| audit_log | Record in `records/pool/audits/bypasses.md` with date, approver, reason |
| expiry | 30 days from bypass grant; pattern must be retired or brought to full compliance |

## Properties

| Property | Value |
|----------|-------|
| Kind | `quality_gate` |
| Pillar | P11 |
| Domain | collaboration_pattern construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Examples

## Golden Example
```markdown
---
title: "Search and Rescue Coordination"
agents: [RescueBot, Mapper, CommandCenter]
topology: "Mesh"
---
**Coordination Rules**:
- RescueBot shares real-time sensor data with Mapper via a shared channel.
- Mapper updates the CommandCenter with terrain maps every 30s.
- CommandCenter broadcasts mission priorities to all agents using a priority queue.
**Communication Channels**:
- `sensor_data`: Bidirectional between RescueBot and Mapper.
- `map_updates`: Unidirectional from Mapper to CommandCenter.
- `mission_orders`: Broadcast from CommandCenter to all.
```

## Anti-Example 1: Workflow Confusion
```markdown
---
title: "Incorrect Workflow"
agents: [AgentA, AgentB]
topology: "Linear"
---
**Steps**:
1. AgentA performs task X.
2. AgentB performs task Y after receiving a signal from AgentA.
```
## Why it fails
This defines a *workflow* (sequential execution) rather than a *collaboration pattern*. It lacks structural rules for concurrent coordination and doesn't describe how agents interact beyond a linear handoff.

## Anti-Example 2: Missing Communication
```markdown
---
title: "Role List Only"
agents: [Harvester, Analyzer, Storage]
topology: "Unknown"
---
**Roles**:
- Harvester collects data.
- Analyzer processes data.
- Storage archives data.
```
## Why it fails
The example only lists agent roles without defining *how* they coordinate. No communication channels, synchronization rules, or structural topology are specified, making the pattern incomplete and unactionable.

## Properties

| Property | Value |
|----------|-------|
| Kind | `examples` |
| Pillar | P07 |
| Domain | collaboration_pattern construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
