---
kind: knowledge_card
id: bld_knowledge_card_reasoning_strategy
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for reasoning_strategy production
quality: 9.2
title: "Knowledge Card Reasoning Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [reasoning_strategy, builder, knowledge_card]
tldr: "Domain knowledge for reasoning_strategy production"
domain: "reasoning_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - p03_sp_reasoning_strategy_builder
  - reasoning-strategy-builder
  - kc_reasoning_strategy
  - bld_instruction_reasoning_strategy
  - p10_lr_reasoning_strategy_builder
  - bld_output_template_reasoning_strategy
  - p03_qg_reasoning_strategy
  - bld_examples_reasoning_strategy
  - bld_collaboration_reasoning_strategy
  - reasoning-trace-builder
---

## Domain Overview

This ISO selects a reasoning strategy (e.g. chain-of-thought) and the conditions under which it applies.
Reasoning_strategy artifacts structure how AI systems process information to derive conclusions, often used in complex domains like healthcare diagnostics, legal analysis, and autonomous systems. These strategies define the logical flow, heuristics, and constraints guiding inference engines, ensuring alignment with domain-specific rules and objectives. They differ from generic prompt techniques by embedding domain knowledge into the reasoning process, enabling systems to handle ambiguity, prioritize evidence, and validate outputs through formal or semi-formal methods.

Industries leverage reasoning strategies to enhance transparency, reduce errors, and comply with regulations. For example, in finance, strategies may enforce risk-assessment hierarchies, while in law, they might encode precedent-based argumentation. Effective strategies balance computational efficiency with accuracy, often integrating knowledge graphs, rule-based systems, or probabilistic models.

## Key Concepts
| Concept               | Definition                                                                 | Source                          |
|-----------------------|----------------------------------------------------------------------------|---------------------------------|
| Deductive Reasoning   | Deriving specific conclusions from general premises                          | Aristotle, *Organon*           |
| Abductive Inference   | Hypothesis generation from incomplete observations                         | Peirce, *Collected Papers*      |
| Heuristic-Based Reasoning | Rule-of-thumb methods for approximating solutions in complex scenarios | Simon, *Science of the Artificial* |
| Constraint Satisfaction | Solving problems by adhering to predefined constraints                     | CSP frameworks (ACM)          |
| Chain-of-Thought      | Explicit, stepwise reasoning to model human-like problem-solving           | Brown et al., *NeurIPS 2020*    |
| Knowledge Graph Reasoning | Inference using structured relationships in semantic networks           | Google’s KBQA system           |
| Backward Chaining     | Starting from a goal to trace logical dependencies                         | Prolog, *Logic Programming*     |
| Uncertainty Handling  | Quantifying and propagating uncertainty in probabilistic reasoning         | Pearl, *Probabilistic Reasoning* |

## Industry Standards
- ISO/IEC 23894: AI Trustworthiness Framework
- IBM’s SOAR (Situation, Option, Action, Result) for decision modeling
- Google’s PaLM reasoning benchmarks
- ACL 2023 guidelines on structured inference in NLP
- DARPA’s Explainable AI (XAI) standards

## Common Patterns
1. **Hierarchical decomposition** – Breaking problems into subtasks with prioritized resolution.
2. **Premise validation loops** – Iteratively verifying assumptions against domain knowledge.
3. **Counterfactual reasoning** – Evaluating outcomes by altering variables in controlled scenarios.
4. **Multi-agent consensus** – Aggregating reasoning from specialized sub-models.
5. **Constraint propagation** – Narrowing solution spaces via interdependent rules.

## Pitfalls
- Over-reliance on heuristics without validation against ground truth.
- Ignoring edge cases in rule-based systems, leading to brittle inferences.
- Misaligning reasoning depth with task complexity (e.g., over-engineering simple queries).
- Failing to document strategy assumptions, reducing auditability.
- Neglecting computational limits, causing cascading failures in complex chains.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_reasoning_strategy_builder]] | downstream | 0.49 |
| [[reasoning-strategy-builder]] | downstream | 0.43 |
| [[kc_reasoning_strategy]] | sibling | 0.41 |
| [[bld_instruction_reasoning_strategy]] | downstream | 0.38 |
| [[p10_lr_reasoning_strategy_builder]] | downstream | 0.37 |
| [[bld_output_template_reasoning_strategy]] | downstream | 0.32 |
| [[p03_qg_reasoning_strategy]] | downstream | 0.30 |
| [[bld_examples_reasoning_strategy]] | downstream | 0.30 |
| [[bld_collaboration_reasoning_strategy]] | downstream | 0.30 |
| [[reasoning-trace-builder]] | downstream | 0.29 |
