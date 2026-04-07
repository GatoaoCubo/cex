---
kind: knowledge_card
id: bld_knowledge_card_chain
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for chain production — sequential prompt pipelines
sources: LangChain SequentialChain, DSPy Module composition, Anthropic prompt chaining guide
quality: 9.1
title: "Knowledge Card Chain"
version: "1.0.0"
author: n03_builder
tags: [chain, builder, examples]
tldr: "Golden and anti-examples for chain construction, demonstrating ideal structure and common pitfalls."
domain: "chain construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Domain Knowledge: chain
## Executive Summary
Chains are sequential prompt pipelines where output A feeds input B across multiple LLM calls. Each step performs one atomic task with typed I/O, enabling reliable composition without agent overhead. Chains differ from workflows (runtime orchestration with agents), DAGs (dependency graphs without execution), and instructions (step-by-step recipes for one agent).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P03 (prompts) |
| Frontmatter fields | 19 |
| Quality gates | 8 HARD + 10 SOFT |
| Flow types | sequential, branching, parallel, mixed |
| Error strategies | fail_fast, skip, retry, fallback |
| Context passing | full, filtered, summary |
| Step constraint | 1 step = 1 LLM call |
## Patterns
- **Atomic steps**: each step has one clear purpose and one LLM call — compound steps are split into separate chain links
- **Typed I/O contracts**: explicit input/output types per step prevent data mismatches between chain links
- **Context passing strategies**: full (all prior output), filtered (relevant subset), summary (compressed) — choose based on context window budget
- **Error propagation**: fail_fast for critical paths; skip for optional enrichment steps; retry for transient failures
- **Narrowing funnel**: early steps gather broadly, later steps filter and refine — most efficient information flow
| Source | Concept | Application |
|--------|---------|-------------|
| LangChain SequentialChain | Chained LLMChains with variable passing | Direct: steps with typed I/O |
| DSPy Module composition | Composable modules with typed signatures | Typed contracts per step |
| Anthropic prompt chaining | Multi-step prompt best forctices | Step atomicity, error strategy |
| LangGraph | Stateful graph-based chains | Branching and parallel flows |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Multi-purpose steps | Step does too much; hard to debug and test in isolation |
| Untyped I/O between steps | Data format mismatches cause silent failures |
| Full context passing always | Context window overflows on long chains |
| No error strategy defined | One step failure crashes entire chain silently |
| Missing data flow diagram | Hidden dependencies between steps go unnoticed |
| Chain used for agent coordination | That is a workflow (P12), not a prompt chain |
## Application
1. Decompose task into atomic steps: each step = 1 LLM call with 1 purpose
2. Define typed I/O for each step: input type, output type, format
3. Choose context passing: full, filtered, or summary per step transition
4. Set error strategy: fail_fast for critical, skip for enrichment, retry for transient
5. Draw data flow: visualize which output feeds which input
6. Validate: each step independently testsble, total steps <= 10 for maintainability
## References
- LangChain: SequentialChain, LCEL documentation
- DSPy: Module composition and typed signatures
- Anthropic: prompt chaining best forctices guide
- LangGraph: stateful graph-based chain execution
