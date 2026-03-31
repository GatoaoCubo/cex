---
description: "Execute a mission — decompose goal into artifacts and build them. Usage: /mission <goal>"
---

# /mission — Autonomous Mission Execution

Decompose a high-level goal into concrete artifact tasks and execute them.

## Steps

1. Parse mission from `$ARGUMENTS`
2. Decompose into artifact kinds:
   ```bash
   python _tools/cex_mission.py decompose "$ARGUMENTS"
   ```
3. Execute the mission (builds all artifacts):
   ```bash
   python _tools/cex_mission.py execute "$ARGUMENTS" --complexity standard
   ```
4. With nucleus targeting:
   ```bash
   python _tools/cex_mission.py execute "$ARGUMENTS" --nucleus N02
   ```
5. Check mission status:
   ```bash
   python _tools/cex_mission.py status
   ```

## Complexity Levels
- `minimal` — 4 artifacts: agent, system_prompt, knowledge_card, agent_card
- `standard` — 7 artifacts: + dispatch_rule, workflow, quality_gate
- `full` — 12 artifacts: + scoring_rubric, prompt_template, action_prompt, pattern, dag

## Examples
```
/mission build a content marketing automation system --nucleus N02
/mission create a code review pipeline --nucleus N05
/mission design a competitive intelligence system --nucleus N01
```
