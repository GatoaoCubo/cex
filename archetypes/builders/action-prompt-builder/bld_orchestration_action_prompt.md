---
kind: collaboration
id: bld_collaboration_action_prompt
pillar: P12
llm_function: COLLABORATE
purpose: How action-prompt-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Action Prompt"
version: "1.0.0"
author: n03_builder
tags: [action_prompt, builder, examples]
tldr: "Golden and anti-examples for action prompt construction, demonstrating ideal structure and common pitfalls."
domain: "action prompt construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - action-prompt-builder
  - bld_collaboration_few_shot_example
  - bld_collaboration_context_doc
  - bld_collaboration_prompt_version
  - bld_collaboration_instruction
  - bld_collaboration_input_schema
  - bld_collaboration_golden_test
  - bld_collaboration_system_prompt
  - bld_collaboration_response_format
  - bld_collaboration_prompt_template
---

# Collaboration: action-prompt-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what prompt should be injected to make the agent execute this specific task?"
I do not define agent identity. I do not write step-by-step recipes.
I produce task-focused prompts so agents can execute specific operations with defined input/output.
## Crew Compositions
### Crew: "Agent Prompt Stack"
```
  1. context-doc-builder -> "domain context for hydration"
  2. instruction-builder -> "step-by-step execution recipe"
  3. action-prompt-builder -> "task-focused prompt with I/O contract"
  4. few-shot-example-builder -> "format examples for the prompt"
```
### Crew: "Task Execution Setup"
```
  1. input-schema-builder -> "input contract definition"
  2. action-prompt-builder -> "execution prompt with defined I/O"
  3. golden-test-builder -> "reference output for quality calibration"
```
## Handoff Protocol
### I Receive
- seeds: task description, expected input format, expected output format
- optional: domain context, edge cases, validation criteria
### I Produce
- action_prompt artifact (.md + .yaml frontmatter)
- committed to: `cex/P03/examples/p03_ap_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- context-doc-builder: provides domain context for prompt hydration
- input-schema-builder: provides input contract that the prompt must respect
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| chain-builder | Chains compose multiple action_prompts in sequence |
| golden-test-builder | Needs prompt output to create reference examples |
| e2e-eval-builder | Tests full pipeline that includes action_prompts |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[action-prompt-builder]] | upstream | 0.55 |
| [[bld_collaboration_few_shot_example]] | sibling | 0.54 |
| [[bld_collaboration_context_doc]] | sibling | 0.51 |
| [[bld_collaboration_prompt_version]] | sibling | 0.49 |
| [[bld_collaboration_instruction]] | sibling | 0.48 |
| [[bld_collaboration_input_schema]] | sibling | 0.47 |
| [[bld_collaboration_golden_test]] | sibling | 0.47 |
| [[bld_collaboration_system_prompt]] | sibling | 0.47 |
| [[bld_collaboration_response_format]] | sibling | 0.46 |
| [[bld_collaboration_prompt_template]] | sibling | 0.45 |
