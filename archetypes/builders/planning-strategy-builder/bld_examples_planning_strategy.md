---
kind: examples
id: bld_examples_planning_strategy
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of planning_strategy artifacts
quality: 9.0
title: "Examples Planning Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [planning_strategy, builder, examples]
tldr: "Golden and anti-examples of planning_strategy artifacts"
domain: "planning_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
```markdown
---
title: "Urban Mobility Expansion Plan"
kind: planning_strategy
author: Urban Planning Team
date: 2023-11-01
---

**Objective**: Optimize city transportation network for 2030.

**Phases**:
1. **Research**: Analyze traffic patterns, population growth, and existing infrastructure gaps.
2. **Design**: Propose hybrid public transit (electric buses + bike lanes) and AI-driven traffic signaling.
3. **Implementation**: Prioritize high-impact zones using phased funding and community feedback loops.
4. **Evaluation**: Use real-time sensors and quarterly audits to adjust strategies.

**Constraints**: 
- Budget: $500M annual cap
- Timeline: 5-year rollout
- Equity: Ensure accessibility in underserved neighborhoods
```

## Anti-Example 1: Confusing with reasoning_strategy
```markdown
---
title: "Prompt-Based Decision Framework"
kind: planning_strategy
author: AI Team
date: 2023-10-15
---

**Steps**:
1. Use "maximize efficiency" prompt for resource allocation.
2. Apply "ethical dilemma" prompt for conflict resolution.
3. Generate options via "scenario simulation" prompt.

**Constraints**: 
- Must use predefined prompts
- No human oversight allowed
```
## Why it fails: 
Mixes planning with prompt-based reasoning. The artifact defines a *reasoning strategy* (prompt usage), not a *planning approach* (strategic framework for execution).

## Anti-Example 2: Treating as workflow
```markdown
---
title: "Project Execution Steps"
kind: planning_strategy
author: Operations
date: 2023-10-20
---

**Tasks**:
1. Collect data from sensors
2. Upload to cloud storage
3. Run ML model on dataset
4. Generate report
5. Send to stakeholders

**Constraints**: 
- Must use Python for data processing
- Reports due by 5 PM daily
```
## Why it fails: 
Describes an *execution workflow* (sequence of tasks), not a *planning strategy* (strategic framework for deciding what to do). It lacks high-level objectives and adaptive planning elements.
