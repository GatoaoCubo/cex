---
id: tpl_instruction
kind: instruction
pillar: P03
version: 1.0.0
title: "Template — Instruction"
tags: [template, instruction, builder, pipeline, steps]
tldr: "Step-by-step build instructions for a builder ISO. Maps each step to an 8F function, defines inputs/outputs/gates, and provides the execution order."
quality: 9.0
updated: "2026-04-07"
domain: "prompt engineering"
author: n03_builder
created: "2026-04-07"
density_score: 0.95
---

# Instruction: [BUILDER_NAME]

## Build Pipeline

### Step 1: [STEP_NAME] (F[N])
**Input**: [What this step receives]
**Output**: [What this step produces]
**Gate**: [Validation check — must pass to proceed]

### Step 2: [STEP_NAME] (F[N])
**Input**: [Output from step 1]
**Output**: [Transformed state]
**Gate**: [Validation check]

### Step 3: [STEP_NAME] (F[N])
**Input**: [Output from step 2]
**Output**: [Final artifact or intermediate]
**Gate**: [Validation check]

## 8F Mapping

| Step | 8F Function | What Happens |
|------|-------------|-------------|
| 1 | F1 CONSTRAIN | Load schema, config → constraints |
| 2 | F2 BECOME | Load system_prompt, manifest → identity |
| 3 | F3 INJECT | Load KCs, examples, memory → knowledge |
| 4 | F4 REASON | LLM plans artifact structure |
| 5 | F5 CALL | Scan existing artifacts, load tools |
| 6 | F6 PRODUCE | Compose prompt → LLM generates |
| 7 | F7 GOVERN | Validate against hard gates |
| 8 | F8 COLLABORATE | Save, compile, commit, signal |

## Execution Rules
- Execute steps in order — no skipping
- If a gate fails, retry F6 with feedback (max 2 retries)
- `quality: null` — NEVER self-score
- Output starts with `---` (YAML frontmatter)

## Critical Patterns
- **DRY**: Use ISOs from builder dir, don't hardcode
- **Deterministic**: Same intent + same ISOs = same structure
- **Bounded**: Respect `max_bytes` from constraint spec
- **Traceable**: Log timing per step, save learning record

## Quality Gate
- [ ] Every step has Input/Output/Gate
- [ ] Steps map to 8F functions
- [ ] Execution order is explicit (numbered)
- [ ] Retry strategy documented

## Cross-References

- **Pillar**: P03 (Prompt)
- **Kind**: `instruction`
- **Artifact ID**: `tpl_instruction`
- **Tags**: [template, instruction, builder, pipeline, steps]

## Builder Integration

| Aspect | Detail |
|--------|--------|
| ISO | 1 of 13 builder ISOs |
| Loader | `cex_skill_loader.py` |
| Pipeline | Injected at F3 (Compose) |
