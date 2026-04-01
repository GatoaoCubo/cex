---
kind: memory
id: bld_memory_skill
pillar: P09
llm_function: INJECT
purpose: Persistent learnings for skill-builder across sessions
pattern: what worked, what failed, key insights from building skills
---

# Memory: skill-builder

## Learnings
- Skills are NOT agents — they have no identity, only behavior
- Skills are NOT workflows — they are reusable across workflows
- The boundary between skill and workflow: a skill is invokable, a workflow is sequential
- Universal term: Alexa Skills, Semantic Kernel Skills, AgentSkills.io

## What Worked
- Defining trigger conditions clearly prevents misuse
- Phases (setup → execute → validate → cleanup) give consistent structure
- Anti-patterns section is high-value — prevents common mistakes

## What Failed
- Over-scoping: trying to make one skill do too much → split into focused skills
- Missing boundary: skill that overlaps with agent identity → strip identity, keep behavior
