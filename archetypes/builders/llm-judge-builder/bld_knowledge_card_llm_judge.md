---
kind: knowledge_card
id: bld_knowledge_card_llm_judge
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for llm_judge production — LLM-as-Judge configuration
sources: Braintrust scorer, DeepEval LLMTestCase, RAGAS metrics, Promptfoo llm-rubric, OpenAI Evals, Zheng et al. 2023 (MT-Bench)
---

# Domain Knowledge: llm_judge
## Executive Summary
LLM-as-Judge uses a language model to automatically evaluate the quality of another model's output. The judge receives an input (prompt + response) and returns a score on a defined scale. Quality depends on three decisions made at spec time: which model judges (capability), what criteria it uses (coverage), and how it is calibrated (consistency). Uncalibrated judges exhibit position bias, verbosity bias, and self-enhancement bias.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P07 (Evals) |
| llm_function | GOVERN (controls quality signal) |
| Scale types | binary (pass/fail), likert (1-5), extended (1-10), continuous (0.0-1.0) |
| Recommended judge models | gpt-4o, claude-3-5-sonnet, gemini-1.5-pro (frontier = lower bias) |
| Chain-of-thought | Required for criteria with subjective dimensions |
| Temperature | 0.0 for reproducibility; 0.2 max for creative criteria |
| Few-shot minimum | 2 examples (1 high, 1 low); 5+ for production |
## Framework Patterns
### Braintrust scorer
```yaml
framework: braintrust
# Scorer maps to a named scoring function
# score() returns {score: float, metadata: {rationale: str}}
# Scale: 0.0-1.0 continuous
```
### DeepEval LLMTestCase
```yaml
framework: deepeval
# GEval metric: criteria -> evaluation_steps -> model
# LLMTestCase(input, actual_output, expected_output)
# threshold: float (pass if score >= threshold)
```
### RAGAS metrics
```yaml
framework: ragas
# Core metrics: faithfulness, answer_relevancy, context_precision, context_recall
# faithfulness: claims in answer supported by context (0-1)
# answer_relevancy: answer addresses the question (0-1)
```
### Promptfoo llm-rubric
```yaml
framework: promptfoo
# assert type: llm-rubric
# value: "The response must be factually accurate and cite sources"
# rubricPrompt: custom judge prompt override
```
### OpenAI Evals
```yaml
framework: openai_evals
# eval_type: model-graded-closedqa or model-graded-fact
# completion_fn: judge model
# eval_completion_fn: evaluated model
```
## Patterns
- **Single-criterion judges**: one criterion per judge, combine scores downstream — reduces criteria interference
- **Reference-based**: judge receives (input, output, reference) — higher accuracy for factual tasks
- **Reference-free**: judge receives (input, output) only — required when ground truth unavailable
- **Pairwise**: judge compares two outputs (A vs B) — reduces absolute scale calibration issues
- **Chain-of-thought scoring**: judge writes rationale BEFORE score — reduces position bias by ~15%
| Pattern | Use case | Bias risk |
|---------|----------|-----------|
| Single criterion | Targeted quality dimension | Low |
| Multi-criteria | Holistic evaluation | Medium (criteria bleed) |
| Pairwise | A/B comparison | Low (relative scale) |
| Reference-based | Factual accuracy | Low |
| Reference-free | Style, tone, creativity | High (needs calibration) |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No few-shot examples | Judge drifts on edge cases; inconsistent scores across runs |
| Overlapping criteria | Double-penalizes same flaw; inflates variance |
| Vague scale anchors | "1=bad, 5=good" is not actionable; judge assigns arbitrary scores |
| judge_model == evaluated_model | Self-enhancement bias; model favors its own style |
| temperature > 0.2 | Score variance increases; same input gets different scores |
| Criteria count > 7 | Cognitive overload in judge; later criteria get less attention |
| Binary scale for nuanced tasks | Loses signal gradient; everything is pass/fail |
## Key Biases to Mitigate
| Bias | Mitigation |
|------|-----------|
| Position bias | Randomize order in pairwise; use reference-based |
| Verbosity bias | Penalize length explicitly in criteria anchors |
| Self-enhancement | Use different model family as judge |
| Sycophancy | Few-shot with examples where confident-but-wrong = low score |
## Application
1. Choose judge_model: frontier model from different family than evaluated model
2. Define criteria: 1-5 independent dimensions, each measuring ONE quality aspect
3. Set scale: likert 1-5 for most cases; binary for pass/fail gates; 1-10 for fine-grained
4. Write anchors: define exactly what score 1, 3, 5 look like (not just low/mid/high)
5. Compose few_shot: minimum 1 high score + 1 low score example with rationale
6. Set chain_of_thought: true (default); false only if latency < 500ms is required
7. Set temperature: 0.0 for reproducibility
## References
- Zheng et al. 2023: "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"
- DeepEval documentation: GEval metric design
- Braintrust: scorer API patterns
- RAGAS: RAG evaluation metrics (faithfulness, relevancy)
- Promptfoo: llm-rubric assertion type
