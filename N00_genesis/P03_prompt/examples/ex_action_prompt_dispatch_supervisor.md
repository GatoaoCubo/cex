---
id: p03_up_dispatch_agent_group
kind: user_prompt
action: dispatch_agent_group_task
input_required: [task_description, agent_group_name, quality_target]
output_expected: "Completion signal + git commit with artifacts"
pillar: P03
version: 1.0.0
created: 2026-03-24
author: orchestrator
domain: orchestration
quality: 9.2
tags: [user-prompt, dispatch, handoff, agent_group, task]
updated: "2026-04-07"
title: "Action Prompt Dispatch Supervisor"
density_score: 0.92
tldr: "Defines user prompt for action prompt dispatch supervisor, with validation gates and integration points."
related:
  - skill
  - research_then_build
  - full_pipeline
  - doctor
  - build_and_review
  - p05_output_validator
  - validate
  - status
  - build
  - p03_ap_{{ACTION_SLUG}}
---

# User Prompt: Dispatch Agent_group Task

## Purpose
Instruct a agent_group to execute a specific task with defined inputs and quality gate.

## Input
```yaml
task: "Create 8 P04 examples from real organization artifacts"
agent_group: edison
quality_target: 9.0
autonomy: full
context_files:
  - "C:/Users/PC/Documents/GitHub/cex/P04_tools/_schema.yaml"
  - "C:/Users/PC/Documents/GitHub/cex/P04_tools/examples/ex_skill_cex_forge.md"
```

## Execution
1. Read schema to understand type constraints (max_bytes, required frontmatter)
2. Read source artifacts for real data (no invented content)
3. Write each example matching template structure
4. Validate size and frontmatter before saving
5. Commit all files with descriptive message

## Output
```text
git commit: "CEX: 8 P04 examples from real organization artifacts"
signal: .claude/signals/edison_complete_9.0.json
```

## Validation
1. Each file under type max_bytes
2. All code fences balanced (even number of backtick fences)
3. Frontmatter YAML parseable with required fields
4. Body contains all template sections
5. No placeholder text ({{VAR}} or PENDING/Configurable)

## Properties

| Property | Value |
|----------|-------|
| Kind | `user_prompt` |
| Pillar | P03 |
| Domain | orchestration |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## System Context

This artifact participates in the CEX typed knowledge system, a fractal
architecture with 12 pillars, 8 nuclei, and 125 specialized builders.
Artifacts flow through the 8F pipeline: Focus, Frame, Fetch, Filter,
Format, Forge, Furnish, and Feedback.

Quality is enforced via 3-layer scoring: structural (30%), rubric (30%),
and semantic (40%). All artifacts target quality >= 9.0.

| Layer | Weight | Method |
|-------|--------|--------|
| Structural | 30% | Automated count-based checks |
| Rubric | 30% | Quality gate dimension scoring |
| Semantic | 40% | LLM evaluation (when L1+L2 >= 8.5) |

# User Prompt: Dispatch Agent_group Task

## Purpose
Instruct a agent_group to execute a specific task with defined inputs and quality gate.

## Input
```yaml
task: "Create 8 P04 examples from real organization artifacts"
agent_group: edison
quality_target: 9.0
autonomy: full
context_files:
  - "C:/Users/PC/Documents/GitHub/cex/P04_tools/_schema.yaml"
  - "C:/Users/PC/Documents/GitHub/cex/P04_tools/examples/ex_skill_cex_forge.md"
```

## Execution
1. Read schema to understand type constraints (max_bytes, required frontmatter)
2. Read source artifacts for real data (no invented content)
3. Write each example matching template structure
4. Validate size and frontmatter before saving
5. Commit all files with descriptive message

## Output
```text
git commit: "CEX: 8 P04 examples from real organization artifacts"
signal: .claude/signals/edison_complete_9.0.json
```

## Validation
1. Each file under type max_bytes
2. All code fences balanced (even number of backtick fences)
3. Frontmatter YAML parseable with required fields
4. Body contains all template sections
5. No placeholder text ({{VAR}} or PENDING/Configurable)

## Properties

| Property | Value |
|----------|-------|
| Kind | `user_prompt` |
| Pillar | P03 |
| Domain | orchestration |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## System Context

This artifact participates in the CEX typed knowledge system, a fractal
architecture with 12 pillars, 8 nuclei, and 125 specialized builders.
Artifacts flow through the 8F pipeline: Focus, Frame, Fetch, Filter,
Format, Forge, Furnish, and Feedback.

Quality is enforced via 3-layer scoring: structural (30%), rubric (30%),
and semantic (40%). All artifacts target quality >= 9.0.

| Layer | Weight | Method |
|-------|--------|--------|
| Structural | 30% | Automated count-based checks |
| Rubric | 30% | Quality gate dimension scoring |
| Semantic | 40% | LLM evaluation (when L1+L2 >= 8.5) |

## Quality Enforcement

This artifact follows the CEX 3-layer quality model. Structural scoring
validates frontmatter completeness, content depth, and format diversity.
Rubric scoring checks dimension-specific criteria from the quality gate.
Semantic scoring provides LLM-based evaluation when layers one and two
average 8.5 or above.

All artifacts target quality 9.0 or higher. Below 8.0 triggers a rebuild.
Between 8.0 and 9.0, the evolve pipeline applies targeted improvements.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[skill]] | downstream | 0.45 |
| [[research_then_build]] | downstream | 0.41 |
| [[full_pipeline]] | downstream | 0.41 |
| [[doctor]] | downstream | 0.40 |
| [[build_and_review]] | downstream | 0.39 |
| [[p05_output_validator]] | downstream | 0.37 |
| [[validate]] | downstream | 0.36 |
| [[status]] | downstream | 0.36 |
| [[build]] | downstream | 0.35 |
| [[p03_ap_{{ACTION_SLUG}}]] | related | 0.33 |
