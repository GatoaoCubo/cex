---
id: p10_lr_chain_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "Chains that attempted to pack multiple transformations into a single step produced outputs that were difficult to debug and impossible to partially retry. Enforcing 1 step = 1 LLM call with explicit typed input/output reduced debugging time by ~60% and enabled partial retry at the step level."
pattern: "Each chain step must have exactly one purpose, one LLM call, and explicitly typed input and output. Data flows between steps via named output references. Error handling is declared per step, not per chain."
evidence: "5 pipeline patterns validated across research, data processing, and intent routi..."
confidence: 0.7
outcome: SUCCESS
domain: chain
tags: [chain, prompt-decomposition, data-flow, step-granularity, error-handling]
tldr: "One step, one purpose, one LLM call. Typed inputs and outputs at every boundary. Handle errors per step, not per chain."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
keywords: [prompt chain, step decomposition, data flow, typed output, partial retry, error handling, atomic step]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.0
title: "Memory Chain"
density_score: 0.90
llm_function: INJECT
---
## Summary
Complex tasks decomposed into prompt chains fail in one of two ways: steps that are too coarse (multiple transformations packed together, hard to debug) or steps that are too fine (one sentence per step, creating orchestration overhead without benefit). The effective middle ground is 1 step = 1 transformation with a single LLM call, explicit typed input, and explicit typed output.
The key insight: a chain is not a script. It has no mutable state between steps except what is explicitly passed. This constraint, enforced strictly, makes each step independently testsble and retryable.
## Pattern
**Atomic step discipline.**
1. Define the chain's goal as a single sentence. Every step must serve that goal directly.
2. Assign each step a single purpose: classify, extract, summarize, format, validate, route, or generate. No compound purposes.
3. Declare typed input and output for each step before writing the prompt. Input type drives what the step receives; output type drives what the next step can consume.
4. Data flow: each step references prior step outputs by name (e.g., `step_1.output.entities`). No implicit global state.
5. Error handling per step: define what happens when that step's LLM call fails or returns unexpected type. Options: retry, skip, abort chain, return partial.
6. Steps_count in frontmatter must equal the actual count of numbered steps in the body (validator catches mismatch).
Common pipeline shapes:
- Extract-Transform-Load (3 steps, sequential): data processing
- Research-Synthesize-Format (3 steps, sequential): knowledge production
- Classify-Route-Execute (3 steps, branching): intent-based handling
- Parallel-Merge (2+ steps, parallel then merge): multi-perspective analysis
- Gather-Filter-Compose (3 steps, sequential): content curation
## Anti-Pattern
- Packing two transformations into one step to reduce step count (saves nothing; costs debuggability).
- Implicit data passing (step 3 "knows" what step 1 produced without explicit reference).
- Per-chain error handling only (when step 2 fails, which step do you retry?).
- Steps without typed output (the next step has no contract to code against).
- Confusing chain with chain-of-thought: chain = separate LLM calls between prompts; CoT = reasoning within one prompt.
- Including orchestration logic (spawns, signals, agent routing) in a chain — that belongs in a workflow.
## Context
The chain-vs-workflow boundary is the most common confusion point. A chain is purely data transformation across LLM calls with no side effects and no external system calls. The moment a step writes to a database, sends a signal, or spawns another process, it has crossed into workflow territory.
