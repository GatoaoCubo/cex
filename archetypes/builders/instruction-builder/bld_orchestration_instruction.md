---
kind: collaboration
id: bld_collaboration_instruction
pillar: P12
llm_function: COLLABORATE
purpose: How instruction-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Instruction"
version: "1.0.0"
author: n03_builder
tags: [instruction, builder, examples]
tldr: "Golden and anti-examples for instruction construction, demonstrating ideal structure and common pitfalls."
domain: "instruction construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_action_prompt
  - bld_collaboration_agent
  - bld_collaboration_agent_package
  - bld_collaboration_system_prompt
  - bld_collaboration_boot_config
  - bld_collaboration_chain
  - bld_collaboration_builder
  - bld_collaboration_context_doc
  - bld_collaboration_knowledge_card
  - instruction-builder
---

# Collaboration: instruction-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what are the exact steps to execute this task?"
I do not define agent identity. I do not write task prompts with I/O.
I compose step-by-step recipes so agents can execute tasks in correct order with validation.
## Crew Compositions
### Crew: "New Agent End-to-End"
```
  1. knowledge-card-builder -> "domain knowledge"
  2. agent-builder -> "agent definition"
  3. instruction-builder -> "execution steps for agent tasks"
  4. boot-config-builder -> "provider configuration"
  5. agent-package-builder -> "deployable package"
```
### Crew: "Task Recipe Design"
```
  1. context-doc-builder -> "domain context for grounding"
  2. instruction-builder -> "step-by-step operational recipe"
  3. action-prompt-builder -> "task prompt that follows the recipe"
  4. e2e-eval-builder -> "end-to-end test of recipe execution"
```
## Handoff Protocol
### I Receive
- seeds: task name, high-level goal, execution environment
- optional: prerequisites, rollback procedures, validation criteria, dependencies
### I Produce
- instruction artifact (.md + .yaml frontmatter)
- committed to: `cex/P03/examples/p03_instruction_{task}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- context-doc-builder: provides domain background that grounds recipe steps
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| action-prompt-builder | Prompts may implement instruction steps |
| chain-builder | Chains may encode instruction sequences as prompt pipelines |
| handoff-builder | Embeds instruction steps in delegation packages |
| agent-package-builder | Includes instructions in agent packages |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_action_prompt]] | sibling | 0.56 |
| [[bld_collaboration_agent]] | sibling | 0.55 |
| [[bld_collaboration_agent_package]] | sibling | 0.48 |
| [[bld_collaboration_system_prompt]] | sibling | 0.47 |
| [[bld_collaboration_boot_config]] | sibling | 0.46 |
| [[bld_collaboration_chain]] | sibling | 0.45 |
| [[bld_collaboration_builder]] | sibling | 0.45 |
| [[bld_collaboration_context_doc]] | sibling | 0.45 |
| [[bld_collaboration_knowledge_card]] | sibling | 0.44 |
| [[instruction-builder]] | upstream | 0.43 |
