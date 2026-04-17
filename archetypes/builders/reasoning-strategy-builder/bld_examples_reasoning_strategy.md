---
kind: examples
id: bld_examples_reasoning_strategy
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of reasoning_strategy artifacts
quality: 9.0
title: "Examples Reasoning Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [reasoning_strategy, builder, examples]
tldr: "Golden and anti-examples of reasoning_strategy artifacts"
domain: "reasoning_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example

This ISO selects a reasoning strategy (e.g. chain-of-thought) and the conditions under which it applies.
```markdown
---
name: "Structured Deduction Chain"
description: "Breaks down complex problems into logical steps with explicit validation"
type: reasoning_strategy
boundary: reasoning_technique
example: "For mathematical proofs, use 'Assume X → Derive Y → Validate Z'"
---

**Phases:**
1. **Premise Mapping** - List all given facts and constraints
2. **Hypothesis Generation** - Propose 3+ possible conclusions
3. **Logical Validation** - Test each hypothesis against premises
4. **Contradiction Check** - Identify and resolve inconsistencies
5. **Conclusion Synthesis** - Select best-supported outcome

**Validation Criteria:**
- Each step must reference prior premises
- All assumptions must be explicitly stated
- Contradictions must be resolved before finalizing
```

## Anti-Example 1: Vague Instructions
```markdown
---
name: "Just Think Harder"
description: "Encourages deep thinking without structure"
type: reasoning_strategy
---

**Steps:**
1. Think about the problem
2. Consider different angles
3. Come to a conclusion
```
## Why it fails
Lacks specific methodology, validation criteria, and actionable steps. The open-ended nature makes it impossible to evaluate reasoning quality or ensure consistency.

## Anti-Example 2: Prompt Technique Confusion
```markdown
---
name: "Roleplay Reasoning"
description: "Asks AI to act as a specific expert"
type: reasoning_strategy
---

**Instructions:**
"Imagine you're a quantum physicist. Explain this concept."
```
## Why it fails
Confuses reasoning strategy with prompt technique. Focuses on roleplaying rather than structuring the reasoning process itself. Doesn't provide methodology for validating conclusions or tracking logical flow.
