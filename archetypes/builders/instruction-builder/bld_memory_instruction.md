---
id: p10_lr_instruction_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "Compound steps with multiple action verbs ('deploy and verify and restart') cause partial execution — agents complete the first verb and mark the step done. Vague prerequisites ('environment ready') cannot be verified and are silently skipped. Steps marked atomic:false without a rollback procedure leave systems in partially modified states. Steps_count mismatches with actual step count cause validator rejection. Including persona text in instructions ('You are an expert') misplaces content that belongs in system prompts."
pattern: "Each instruction step contains exactly one action verb and one verifiable expected output. Prerequisites are stated as machine-checkable conditions (e.g., 'Python 3.10+ installed: verify with python --version'). Steps marked atomic:false must declare a rollback procedure. Steps_count in frontmatter must match the exact count of numbered steps in the body. Idempotence classification (idempotent/non-idempotent) is required for every step."
evidence: "10 instruction reviews: 7 of 10 had at least one compound step. 8 of 10 had vague prerequisites. 4 of 10 had atomic:false steps without rollback. Steps_count mismatch found in 3 of 10 (caught by validator). Idempotence classification missing in 6 of 10 early productions."
confidence: 0.75
outcome: SUCCESS
domain: instruction
tags: [instruction, atomic-steps, idempotence, rollback, prerequisites, decomposition]
tldr: "One step = one verb + one verifiable output. Vague prerequisites are skipped. atomic:false requires rollback. steps_count must match exactly."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
keywords: [instruction, atomic, idempotent, rollback, prerequisite, decomposition, step, verification, procedure]
memory_scope: project
observation_types: [user, feedback, project, reference]
---
## Summary
Instructions describe how to execute a procedure step by step. The primary failure mode is compound steps: packaging multiple actions into one step causes partial execution that appears complete. The secondary failure is unverifiable prerequisites that agents skip silently. Both are fixed at authoring time with simple structural rules.
## Pattern
Step anatomy (all four elements required):
```
### Step N: [Single action verb] [object]
**Prerequisite**: [Machine-checkable condition with verify command]
**Idempotent**: yes | no
[Action description — one verb, one target, one expected output]
**Verify**: [Command or check that confirms step success]
**Rollback**: [Required only if idempotent:no — how to undo this step]
```
Decomposition rules:
- One verb per step: create, edit, run, verify, wait, delete — never "and"
- If a step has a conditional branch, split into two steps with explicit IF noted
- Long-running steps must include monitoring command and expected completion indicator
- Verification steps are their own numbered steps, not sub-bullets of action steps
Idempotence classification:
- `idempotent: yes` — running the step twice produces the same result as running once
- `idempotent: no` — running twice causes side effects; rollback procedure required
Steps_count in frontmatter must be updated manually after adding or removing steps. Validator rejects mismatches.
## Anti-Pattern
- Compound step: "Deploy the app and verify health and restart workers" — split into 3 steps.
- Vague prerequisite: "Environment is ready" — not machine-checkable, silently skipped.
- `atomic: false` without rollback — leaves system in partial state on failure.
- `steps_count: 5` when body has 7 steps — validator rejects, causes production failure.
- Persona text in instructions ("You are an expert deployer") — belongs in system_prompt, not here.
- Verification buried as sub-bullet inside action step — easy to skip, hard to audit.
## Context
