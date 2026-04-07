---
kind: collaboration
id: bld_collaboration_system_prompt
pillar: P03
llm_function: COLLABORATE
purpose: How system-prompt-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration System Prompt"
version: "1.0.0"
author: n03_builder
tags: [system_prompt, builder, examples]
tldr: "Golden and anti-examples for system prompt construction, demonstrating ideal structure and common pitfalls."
domain: "system prompt construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Collaboration: system-prompt-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "who is this agent, what are its rules, and how does it respond?"
I define persona, ALWAYS/NEVER constraints, tone, knowledge boundaries, and output format. I do NOT write task prompts (action_prompt), step-by-step recipes (instruction), or prompt templates with variables (prompt_template).
## Crew Compositions
### Crew: "Agent Bootstrap"
```
  1. knowledge-card-builder -> "provides domain knowledge to ground the agent's expertise"
  2. system-prompt-builder -> "builds agent identity: persona, rules, tone, output format"
  3. unit-eval-builder -> "tests the system prompt against expected agent behavior"
```
### Crew: "Full Agent Package"
```
  1. model-card-builder -> "defines LLM specs and routing decision"
  2. system-prompt-builder -> "defines persona, ALWAYS/NEVER rules, and response format"
  3. quality-gate-builder -> "sets validation criteria for output produced by the agent"
```
## Handoff Protocol
### I Receive
- seeds: target agent name, domain, expertise level required
- optional: mental_model reference, knowledge_cards to internalize, guardrails, safety constraints
### I Produce
- system_prompt artifact (YAML frontmatter + markdown body, frontmatter 19 fields)
- committed to: `cex/P03_prompt/examples/p03_sp_{agent_slug}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- knowledge-card-builder: domain knowledge cards ground the agent's expertise and knowledge boundary
- model-card-builder: LLM capability specs inform constraint calibration in ALWAYS/NEVER rules
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| unit-eval-builder | tests the system prompt to verify the agent behaves as identity defines |
| workflow-builder | multi-step workflows reference which agent handles each step |
| spawn-config-builder | agent_group spawn configuration often pairs with a system_prompt as the agent identity layer |
