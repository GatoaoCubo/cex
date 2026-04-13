---
kind: examples
id: bld_examples_action_paradigm
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of action_paradigm artifacts
quality: null
title: "Examples Action Paradigm"
version: "1.0.0"
author: wave1_builder_gen
tags: [action_paradigm, builder, examples]
tldr: "Golden and anti-examples of action_paradigm artifacts"
domain: "action_paradigm construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
```markdown
---
title: "Reactive Action Paradigm for Autonomous Navigation"
kind: action_paradigm
description: "Agent continuously senses environment, selects actions based on real-time feedback, and adjusts behavior dynamically."
---

**Paradigm**: Reactive control loop with prioritized action selection.

**Steps**:
1. **Sense**: Use LIDAR and cameras to map surroundings.
2. **Evaluate**: Prioritize safety (avoid obstacles) > efficiency (minimize route).
3. **Act**: Execute lowest-latency action (e.g., brake, turn).
4. **Monitor**: Re-evaluate every 100ms using new sensor data.
5. **Adapt**: Adjust decision thresholds based on terrain type (e.g., reduce speed on ice).

**Key Features**:
- Decoupled perception and action modules
- Action selection weighted by urgency
- Built-in fallback to emergency stop
```

## Anti-Example 1: Overly Vague
```markdown
---
title: "Generic Action Paradigm"
kind: action_paradigm
description: "Agents do things in environments."
---

**Paradigm**: "Do actions when needed."

**Steps**:
1. Wait
2. Do something
3. Repeat
```
## Why it fails
Lacks specificity on how actions are selected, executed, or evaluated. No mechanism for decision-making, feedback, or error handling. Fails to define boundaries between perception, planning, and execution.

## Anti-Example 2: Protocol Confusion
```markdown
---
title: "REST API Action Paradigm"
kind: action_paradigm
description: "Agents use HTTP requests to perform actions."
---

**Paradigm**: Send POST to `/act` with JSON payload.

**Steps**:
1. Client sends `{"action": "move", "params": {}}`
2. Server returns `200 OK` or error code
3. Client waits for response
```
## Why it fails
Confuses action execution paradigm with a specific communication protocol (agent_computer_interface). Focuses on API mechanics rather than agent behavior logic. Doesn't address how agents reason about actions or adapt to environment changes.
