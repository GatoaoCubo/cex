---
id: p01_kc_dspy_patterns
kind: knowledge_card
type: domain
pillar: P01
title: "DSPy Patterns — Signatures, Modules, Optimizers, Assertions"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: dspy
origin: src_framework_taxonomy
quality: 9.1
tags: [dspy, signature, module, optimizer, assertion, few-shot, prompt-optimization]
tldr: "DSPy treats prompts as optimizable programs — Signatures declare I/O, Modules compose logic, Optimizers tune prompts automatically"
when_to_use: "Building or mapping DSPy constructs to CEX kinds"
keywords: [dspy, signature, module, optimizer, predict, chain-of-thought, few-shot]
long_tails:
  - "How does DSPy Signature map to CEX prompt_template and input_schema kinds"
  - "Which DSPy optimizers map to CEX optimizer and few_shot_example kinds"
axioms:
  - "Signature = declarative I/O contract; Module = composable program unit (PyTorch-inspired)"
  - "Optimizers tune prompts and demos automatically — no manual prompt engineering"
linked_artifacts:
  primary: null
  related: [p01_kc_cex_taxonomy, p01_kc_langchain_patterns, p01_kc_crewai_patterns]
feeds_kinds:
  - prompt_template  # Signature (declarative I/O behavior spec)
  - input_schema     # InputField (typed input contract)
  - response_format  # OutputField, Prediction (typed output)
  - chain            # Module.forward(), ChainOfThought, ProgramOfThought
  - agent            # ReAct module (tool-using reasoning + acting)
  - optimizer        # MIPROv2, BootstrapFewShot, COPRO, SIMBA, GEPA, BetterTogether
  - few_shot_example # LabeledFewShot, BootstrapFewShot demonstrations
  - scoring_rubric   # SemanticF1, answer_exact_match (eval metrics)
  - retriever        # ColBERTv2 retrieval integration
  - constraint_spec  # Signature type constraints on fields
density_score: 0.90
related:
  - atom_04_dspy
  - p01_kc_academic_rag_patterns
  - atom_20_prompt_taxonomy
  - bld_instruction_prompt_optimizer
  - p01_kc_few_shot_example
  - kc_llm_agent_frameworks
  - chain-builder
  - p01_kc_chain
  - p01_kc_agent
  - taxonomy_completeness_audit
---

# DSPy Patterns

## Quick Reference
```yaml
topic: DSPy Core (dspy)
scope: Declarative signatures, composable modules, automatic prompt optimization
source: dspy.ai
criticality: high
```

## Key Concepts

| Concept | Module | CEX Kind | Role |
|---------|--------|----------|------|
| `Signature` | `dspy` | prompt_template | Declarative I/O behavior spec ("question -> answer") |
| `InputField` | `dspy` | input_schema | Typed input field in a Signature |
| `OutputField` | `dspy` | response_format | Typed output field in a Signature |
| `Prediction` | `dspy` | response_format | Output object from any module call |
| `Module` | `dspy` | chain | Base class for programs (PyTorch-inspired) |
| `Predict` | `dspy` | chain | Basic predictor — no prompt modification |
| `ChainOfThought` | `dspy` | chain | Step-by-step reasoning before output |
| `ProgramOfThought` | `dspy` | chain | Code-execution-based reasoning |
| `ReAct` | `dspy` | agent | Tool-using agent (Reasoning + Acting) |
| `LM` | `dspy` | prompt_template | Language model wrapper (provider-agnostic) |
| `ColBERTv2` | `dspy` | retriever | ColBERT retrieval model integration |
| `LabeledFewShot` | `dspy` | few_shot_example | Few-shot from labeled examples |
| `BootstrapFewShot` | `dspy` | few_shot_example | Self-generated demonstrations |
| `MIPROv2` | `dspy` | optimizer | Bayesian instruction + demo optimization |
| `COPRO` | `dspy` | optimizer | Instruction optimization via coordinate ascent |
| `SIMBA` | `dspy` | optimizer | Stochastic mini-batch self-reflection |
| `BetterTogether` | `dspy` | optimizer | Meta-optimizer: prompt + weight combined |
| `SemanticF1` | `dspy.evaluate` | scoring_rubric | Semantic F1 evaluation metric |
| `answer_exact_match` | `dspy.evaluate` | scoring_rubric | Exact match evaluation |

## Patterns

| Trigger | Action |
|---------|--------|
| Define I/O contract | `class MyTask(dspy.Signature): question = dspy.InputField(); answer = dspy.OutputField()` |
| Basic prediction | `dspy.Predict(MyTask)(question="...")` |
| Reasoning chain | `dspy.ChainOfThought(MyTask)` — adds rationale before output |
| Tool-using agent | `dspy.ReAct(MyTask, tools=[...])` |
| Optimize prompts | `MIPROv2(metric=SemanticF1()).compile(program, trainset=data)` |
| Bootstrap few-shot | `BootstrapFewShot(metric=fn).compile(program, trainset=data)` |
| Compose modules | `Module.forward()` calls sub-modules — compose like PyTorch |
| Evaluate quality | `dspy.evaluate.Evaluate(devset=data, metric=SemanticF1())` |

## Anti-Patterns

- Writing manual prompts instead of using Signatures — defeats optimization
- Skipping `dspy.configure(lm=...)` — no LM configured
- Using `Predict` when reasoning is needed — use `ChainOfThought`
- Optimizing with too few examples (<20) — optimizers underperform
- Ignoring `Prediction` fields — losing structured access to outputs
- Running `BetterTogether` without sufficient compute budget — expensive meta-optimization

## CEX Mapping

```text
[input_schema (InputField)] -> [prompt_template (Signature)] -> [chain (Module/CoT)]
    -> [response_format (OutputField/Prediction)] -> [optimizer + few_shot_example + scoring_rubric]
    -> [retriever (ColBERTv2)] -> [agent (ReAct)]
```

## References

- source: dspy.ai/learn/
- related: p01_kc_cex_taxonomy

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[atom_04_dspy]] | sibling | 0.76 |
| [[p01_kc_academic_rag_patterns]] | sibling | 0.26 |
| [[atom_20_prompt_taxonomy]] | sibling | 0.25 |
| [[bld_instruction_prompt_optimizer]] | downstream | 0.25 |
| [[p01_kc_few_shot_example]] | sibling | 0.24 |
| [[kc_llm_agent_frameworks]] | sibling | 0.22 |
| [[chain-builder]] | downstream | 0.21 |
| [[p01_kc_chain]] | sibling | 0.21 |
| [[p01_kc_agent]] | sibling | 0.20 |
| [[taxonomy_completeness_audit]] | sibling | 0.20 |
