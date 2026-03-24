---
id: p03_up_dispatch_satellite
type: user_prompt
action: dispatch_satellite_task
input_required: [task_description, satellite_name, quality_target]
output_expected: "Completion signal + git commit with artifacts"
lp: P03
version: 1.0.0
created: 2026-03-24
author: STELLA
domain: orchestration
quality: 9.0
tags: [user-prompt, dispatch, handoff, satellite, task]
---

# User Prompt: Dispatch Satellite Task

## Purpose
Instruct a satellite to execute a specific task with defined inputs and quality gate.

## Input
```yaml
task: "Create 8 P04 examples from real CODEXA artifacts"
satellite: edison
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
git commit: "CEX: 8 P04 examples from real CODEXA artifacts"
signal: .claude/signals/edison_complete_9.0.json
```

## Validation
- Each file under type max_bytes
- All code fences balanced (even number of backtick fences)
- Frontmatter YAML parseable with required fields
- Body contains all template sections
- No placeholder text ({{VAR}} or TODO/TBD)
