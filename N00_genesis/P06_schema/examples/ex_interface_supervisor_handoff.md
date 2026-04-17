---
id: p06_iface_agent_group_handoff
kind: interface
pillar: P06
title: "Interface: orchestrator → Agent_group Handoff Contract"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: knowledge_agent
quality: 9.0
tags: [interface, stella, agent_group, handoff, contract]
tldr: "Interface contract for handoff files: orchestrator writes, agent_group reads — required sections, naming, signal protocol"
max_bytes: 1024
density_score: 0.91
source: organization-core/.claude/rules/orchestrator_RULES.md (COMPOSE phase)
linked_artifacts:
  workflow: p12_wf_stella_dispatch
  handoff: p12_ho_isofix_batch
---

# Interface: orchestrator → Agent_group Handoff Contract

## Contract Overview

| Property | Value |
|----------|-------|
| Producer | orchestrator (orchestrator) |
| Consumer | Agent_group (research_agent, marketing_agent, builder_agent, knowledge_agent, operations_agent, commercial_agent) |
| Location | `.claude/handoffs/{MISSION}_{SAT}.md` |
| Encoding | UTF-8, ASCII-safe Portuguese |
| Trigger | orchestrator COMPOSE phase (Step 3 of 5) |

## Required Sections

```markdown
# {SAT} — {MISSION}: {Title}
**Autonomia Total** | **Quality {N}.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## CONTEXTO
[1-3 paragraphs: what, why, background]

## SEEDS
`[keyword1], [keyword2], [keyword3], ...`  # min 5, max 10

## TAREFAS
### Step N: [ACTION_VERB] [OBJECT]
[Description with [OPEN_VARIABLES] where agent_group decides]

## SCOPE FENCE
- SOMENTE: [permitted paths]
- NAO TOQUE: [forbidden paths]

## COMMIT
git add [paths] && git commit -m "{SAT}[{MISSION}]: [description]"

## SIGNAL
python -c "from records.core.python.signal_writer import write_signal; write_signal('{sat}', 'complete', {score})"
```

## Field Constraints

| Field | Type | Constraint |
|-------|------|-----------|
| MISSION | string | UPPER_SNAKE_CASE, max 20 chars |
| SAT | string | UPPER: research_agent, marketing_agent, builder_agent, knowledge_agent, operations_agent, commercial_agent |
| Title | string | max 60 chars, no emoji |
| Quality target | float | 8.0 to 9.5 (never lower) |
| SEEDS | list[str] | 5-10 keywords, comma-separated |
| SCOPE FENCE | list[str] | min 1 SOMENTE + 1 NAO TOQUE |
| Inline prompt | string | < 200 chars (TSP -p limit) |

## Signal Protocol

Agent_group MUST signal before stopping:
```python
write_signal(sat_name, 'complete', score, task=mission_id)
# Writes to: .claude/signals/{sat}_complete_{timestamp}.json
```

## Naming Conventions

| Mode | File Pattern | Example |
|------|-------------|---------|
| Solo | `{MISSION}_{sat}.md` | `CEX7_pytha.md` |
| Grid static | `{MISSION}_{sat}.md` | `CEX7_edison.md` |
| Grid continuous | `{MISSION}_batch_{N}_{sat}.md` | `CEX7_batch_2_pytha.md` |
