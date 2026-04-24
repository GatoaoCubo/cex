---
id: p01_kc_chain
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P03
title: "Chain — Deep Knowledge for chain"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: operations_agent
domain: chain
quality: 9.1
tags: [chain, P03, PRODUCE, kind-kc]
tldr: "Sequence of prompts where output A feeds input B, forming a deterministic LLM pipeline"
when_to_use: "Building, reviewing, or reasoning about chain artifacts"
keywords: [pipeline, prompt-chain, sequential-prompts]
feeds_kinds: [chain]
density_score: null
related:
  - p10_lr_chain_builder
  - bld_architecture_chain
  - p11_qg_chain
  - chain-builder
  - bld_knowledge_card_chain
  - bld_instruction_chain
  - bld_collaboration_chain
  - p03_sp_chain_builder
  - bld_examples_chain
  - p03_ch_{{PIPELINE_SLUG}}
---

# Chain

## Spec
```yaml
kind: chain
pillar: P03
llm_function: PRODUCE
max_bytes: 6144
naming: p03_ch_{{pipeline}}.md
core: false
```

## What It Is
A chain is a sequence of prompts where the output of step A becomes the input of step B, forming a deterministic LLM pipeline. Each step may use a different model, temperature, or constraint. A chain is NOT a workflow (P12, which orchestrates agents + tools across systems). A chain operates purely at the prompt layer — it is a composition of prompts, not a composition of agents.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `RunnableSequence` / LCEL `|` pipe | `prompt | llm | parser` — canonical chain pattern |
| LlamaIndex | `IngestionPipeline` / `QueryPipeline` | Sequential transformations on documents or queries |
| CrewAI | `Process.sequential` tasks in a `Crew` | Tasks execute in order, each receiving prior output |
| DSPy | `dspy.Module.forward()` with nested calls | `ChainOfThought` → `Predict` composition inside forward |
| Haystack | `Pipeline` with linear component connections | `Pipeline.connect(a.output, b.input)` forms chain |
| OpenAI | Multi-turn message array | Sequential assistant/user messages building context |
| Anthropic | Multi-turn conversation / agentic loop | `tool_use` → `tool_result` → next generation cycle |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| steps | list[prompt] | required | More steps = finer control but higher latency and cost |
| pass_strategy | enum | "full" | Full output vs summary vs structured extract between steps |
| error_handling | enum | "stop" | Stop on error vs skip vs retry — reliability vs throughput |
| model_per_step | bool | false | Per-step model = cost-optimized but more complex config |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Extract-Transform-Load | Data processing pipeline | Step 1: extract entities → Step 2: normalize → Step 3: format |
| Refine chain | Iterative quality improvement | Step 1: draft → Step 2: critique → Step 3: revise |
| Map-Reduce | Process multiple inputs then merge | Map: summarize each doc → Reduce: synthesize all summaries |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Monolithic single-step chain | All logic in one prompt, no composability | Split into atomic steps with clear input/output contracts |
| Passing raw full output between steps | Token bloat, irrelevant context accumulates | Use structured extraction or summary between steps |
| No error boundaries | One step failure kills entire chain | Add error_handling per step: retry, skip, or fallback |

## Integration Graph
```
[action_prompt] --> [chain] --> [output_template]
                      |
              [prompt_template, constraint_spec]
```

## Decision Tree
- IF task is single-step THEN use action_prompt, not chain
- IF task requires iterative refinement THEN use Refine chain pattern
- IF task processes multiple independent inputs THEN use Map-Reduce pattern
- IF steps need different models THEN enable model_per_step
- DEFAULT: Linear Extract-Transform-Load chain with full output passing

## Quality Criteria
- GOOD: Clear step sequence, input/output contracts per step, under 6144 bytes
- GREAT: Per-step model assignment, error handling, structured pass_strategy
- FAIL: Single giant step pretending to be a chain; no input/output contracts; >6144 bytes

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_chain_builder]] | downstream | 0.60 |
| [[bld_architecture_chain]] | downstream | 0.55 |
| [[p11_qg_chain]] | downstream | 0.53 |
| [[chain-builder]] | related | 0.51 |
| [[bld_knowledge_card_chain]] | sibling | 0.50 |
| [[bld_instruction_chain]] | related | 0.48 |
| [[bld_collaboration_chain]] | downstream | 0.48 |
| [[p03_sp_chain_builder]] | related | 0.46 |
| [[bld_examples_chain]] | downstream | 0.46 |
| [[p03_ch_{{PIPELINE_SLUG}}]] | related | 0.45 |
