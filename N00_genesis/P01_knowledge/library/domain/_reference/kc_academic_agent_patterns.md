---
id: p01_kc_academic_agent_patterns
kind: knowledge_card
type: domain
pillar: P01
title: 'Academic Agent Patterns: ReAct, CoT, Reflexion, CoALA, LATS'
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: agent_research
origin: src_standards_global
quality: 9.1
tags:
- react
- chain-of-thought
- reflexion
- tree-of-thoughts
- agent-patterns
- academic
tldr: Core agent reasoning patterns — ReAct (thought+action loop), CoT (step-by-step reasoning), ToT (deliberate search with
  backtracking), Reflexion (self-critique), and CoALA/LATS (cognitive architectures) — form the theoretical foundation adopted
  universally by all agent frameworks.
when_to_use: When choosing reasoning strategies for agents, implementing thought-action loops, designing self-correcting agents,
  or understanding the academic basis of agent architectures.
keywords:
- react
- chain-of-thought
- tree-of-thoughts
- reflexion
- coala
- lats
- reasoning
long_tails:
- react vs chain of thought for agent reasoning
- how reflexion self-correction works in llm agents
axioms:
- Every agent loop is a variant of Thought-Action-Observation — complexity comes from how you branch, backtrack, or reflect
linked_artifacts:
  adw: null
  agent: null
  hop: null
feeds_kinds:
- agent
- chain
- action_prompt
- system_prompt
- director
- handoff_protocol
density_score: 0.9
related:
  - p01_kc_chain_of_thought
  - atom_19_agent_taxonomy_surveys
  - kc_reasoning_strategy
  - p01_fse_kc_creation
  - bld_output_template_planning_strategy
  - planning-strategy-builder
  - p01_kc_reasoning_trace
  - cex_llm_vocabulary_whitepaper
  - audit_planning_strategy_builder
  - kc_prompt_engineering_taxonomy
---

# Knowledge Card: Academic Agent Patterns

## Quick Reference
```yaml
topic: LLM Agent Reasoning Patterns — Academic Foundations
scope: ReAct, CoT, ToT, Reflexion, CoALA, LATS
owner: Princeton, Google, Stanford, various
criticality: high
timeline: 2022-2024
```

## Core Patterns

### Chain-of-Thought (CoT) — Wei et al., 2022 (Google)
- **Core idea**: Elicit step-by-step reasoning by including reasoning examples in prompts
- **Mechanism**: Few-shot prompting with intermediate reasoning steps
- **Key insight**: LLMs can reason better when shown HOW to reason, not just WHAT to answer
- **Variants**: Zero-shot CoT ("Let's think step by step"), few-shot CoT, auto-CoT
- **Status**: Universal — every major LLM and framework supports CoT

### ReAct (Reasoning + Acting) — Yao et al., 2022 (Princeton/Google)
- **Core idea**: Interleave reasoning traces with actions in a unified loop
- **The loop**: Thought -> Action -> Observation -> Thought -> ...
- **Key insight**: Reasoning without action hallucinates; action without reasoning is blind
- **Primitives**: Thought (reasoning trace), Action (tool call), Observation (tool result)
- **Status**: Universal — the dominant agent execution pattern across all frameworks

### Tree of Thoughts (ToT) — Yao et al., 2023 (Princeton)
- **Core idea**: Explore multiple reasoning paths as a tree, with evaluation and backtracking
- **Mechanism**: Generate candidate thoughts -> evaluate -> expand best -> backtrack if needed
- **Key insight**: Not all problems are linear — some require search over reasoning space
- **Primitives**: Thought (candidate step), evaluation (self-assessed quality), backtracking
- **Status**: Adopted for search-heavy tasks (puzzles, planning); niche for general use

### Reflexion (Shinn et al., 2023)
- **Core idea**: Agent reflects on failures and stores verbal self-critique in memory
- **Mechanism**: Execute -> Evaluate -> Reflect on failure -> Store reflection -> Retry with insight
- **Key insight**: Episodic memory of what went wrong improves future attempts
- **Contribution**: Self-correction without weight updates (purely in-context learning)

### CoALA — Cognitive Architectures for Language Agents (Sumers et al., 2023)
- **Core idea**: Unified framework for understanding agent architectures
- **Components**: Memory (working + long-term), Action space (internal + external), Decision-making
- **Key insight**: All agent designs can be described as configurations of memory, action, and decision modules
- **Contribution**: Taxonomy that unifies ReAct, Reflexion, AutoGPT, etc. under one lens

### LATS — Language Agent Tree Search (Zhou et al., 2023)
- **Core idea**: Combine Monte Carlo Tree Search (MCTS) with LLM agents
- **Mechanism**: Use LLM as value function + policy for tree search over action space
- **Key insight**: Planning agents benefit from principled search algorithms, not just greedy action
- **Contribution**: Bridges classical AI planning with LLM-based agents

## Pattern Comparison

| Pattern | Reasoning | Action | Memory | Backtrack | Self-Critique |
|---------|-----------|--------|--------|-----------|---------------|
| CoT | Linear steps | No | No | No | No |
| ReAct | Interleaved | Yes (tools) | Short-term | No | No |
| ToT | Branching | No | Tree state | Yes | Evaluation |
| Reflexion | Linear | Yes | Episodic | Retry | Yes (verbal) |
| CoALA | Configurable | Configurable | Working + LT | Configurable | Configurable |
| LATS | Tree (MCTS) | Yes | Tree + value | Yes (MCTS) | Value function |

## Evolution
```text
[CoT 2022: think step-by-step] -> [ReAct 2022: think+act loop] -> [ToT 2023: branching search] -> [Reflexion 2023: self-critique] -> [CoALA 2023: unified taxonomy] -> [LATS 2023: MCTS planning]
```

## Framework Adoption

| Pattern | LangChain | LlamaIndex | CrewAI | DSPy | AgentScope | MetaGPT |
|---------|-----------|------------|--------|------|------------|---------|
| CoT | ChatModel | LLM | implicit | ChainOfThought | implicit | implicit |
| ReAct | AgentExecutor | ReActAgent | Process | ReAct module | ReAct agent | Action loop |
| ToT | — | — | — | — | — | — |
| Reflexion | — | — | — | — | — | — |

## Industry Terms Derived from Papers

| Paper Term | Industry Usage | Status |
|------------|----------------|--------|
| Chain-of-Thought | CoT / "reasoning" / "thinking" | Universal |
| Thought/Action/Observation | Agent loop / ReAct loop | Universal |
| Reasoning trace | "thinking" / "scratchpad" | Universal |
| Few-shot prompting | Few-shot / in-context learning | Universal |
| Deliberate problem solving (ToT) | Tree search (niche) | Niche |
| Backtracking (ToT) | Retry with different approach | Adopted concept |

## Golden Rules
- Default to ReAct for most agent tasks — it covers 90% of use cases
- Add Reflexion when agents repeatedly fail at similar tasks (episodic self-correction)
- Use ToT/LATS only for tasks with large search spaces (planning, puzzles, code generation)
- CoT is free — always enable reasoning traces even in simple agents

## References
- Wei et al. 2022: "Chain-of-Thought Prompting Elicits Reasoning in LLMs"
- Yao et al. 2022: "ReAct: Synergizing Reasoning and Acting in Language Models"
- Yao et al. 2023: "Tree of Thoughts: Deliberate Problem Solving with LLMs"
- Shinn et al. 2023: "Reflexion: Language Agents with Verbal Reinforcement Learning"
- Sumers et al. 2023: "Cognitive Architectures for Language Agents"
- Zhou et al. 2023: "Language Agent Tree Search Unifies Reasoning Acting and Planning"
- Source: src_standards_global.md (Section 3: Academic Origins)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_chain_of_thought]] | sibling | 0.41 |
| [[atom_19_agent_taxonomy_surveys]] | sibling | 0.34 |
| [[kc_reasoning_strategy]] | sibling | 0.29 |
| [[p01_fse_kc_creation]] | related | 0.29 |
| [[bld_output_template_planning_strategy]] | downstream | 0.29 |
| [[planning-strategy-builder]] | downstream | 0.28 |
| [[p01_kc_reasoning_trace]] | sibling | 0.27 |
| [[cex_llm_vocabulary_whitepaper]] | sibling | 0.25 |
| [[audit_planning_strategy_builder]] | downstream | 0.25 |
| [[kc_prompt_engineering_taxonomy]] | sibling | 0.25 |
