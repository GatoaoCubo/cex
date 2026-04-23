# P07 Evals — Ecosystem Map
> Generated: 2026-03-28 | Author: builder_agent

## 1. Frameworks Audited
| Framework | Domain | Key Concepts |
|-----------|--------|--------------|
| Braintrust | LLM evals platform | Dataset, Experiment, Scorer (LLMClassifier, Factuality, Relevance), Trace, Prompt playground, CI integration |
| DeepEval | Testing framework | LLMTestCase, Metric (Faithfulness, AnswerRelevancy, Hallucination, Bias, Toxicity), Synthesizer, ConversationalMetric |
| RAGAS | RAG evaluation | EvalDataset, SingleTurnSample, MultiTurnSample, ContextPrecision, ContextRecall, Faithfulness, AnswerSimilarity, AspectCritic |
| Patronus | AI evaluation | Evaluator (Hallucination, Toxicity, PII, CustomCriteria), RemoteEvaluator, BatchEval, Guardrails |
| Promptfoo | Prompt testing | TestSuite, Provider, Assertion (contains, equals, llm-rubric, similar, cost, latency), redteam, share |
| Arize Phoenix | Observability + evals | Trace, Span, Evaluation (LLMEval, HallucinationEval, QAEval), Experiment, Inferences, Embedding drift |
| LangSmith | LLM ops + evals | Dataset, Example, Run, Evaluator (custom, off-the-shelf), Experiment, Feedback, Annotation Queue |
| W&B (Weights & Biases) | ML experiment tracking | Run, Artifact, Table, Sweep (hyperparameter search), Report, Model Registry, Trace (Weave) |
| TruLens | RAG evaluation | Feedback function, TruChain, TruLlama, Groundedness, ContextRelevance, AnswerRelevance, Dashboard |
| OpenAI Evals | Eval framework | Registry, CompletionFn, Eval (Match, FuzzyMatch, ModelGraded, CoT), Sample, RunSpec |

## 2. Industry Concepts Found
| Concept | Framework(s) | Description | Frequency |
|---------|-------------|-------------|:---------:|
| Test Case/Sample | DeepEval, RAGAS, Promptfoo, OpenAI Evals, Braintrust, LangSmith | Single input + expected output + context for evaluation | 7 |
| Metric/Scorer | Braintrust, DeepEval, RAGAS, Patronus, Arize Phoenix, TruLens | Named evaluation function that produces a score (0-1 or pass/fail) | 6 |
| LLM-as-Judge | Braintrust (LLMClassifier), DeepEval (all metrics), RAGAS, Promptfoo (llm-rubric), Patronus, OpenAI Evals (ModelGraded) | Using an LLM to evaluate another LLM's output | 7 |
| Dataset/Test Suite | Braintrust, LangSmith, Promptfoo, OpenAI Evals, DeepEval, RAGAS | Collection of test cases for batch evaluation | 7 |
| Experiment/Run | Braintrust, LangSmith, W&B, Arize Phoenix | Named evaluation run with metrics, timestamps, comparison | 5 |
| Assertion/Check | Promptfoo (assertion types), DeepEval (assert_test), OpenAI Evals (Match/Fuzzy) | Atomic pass/fail check: contains, equals, similarity, regex, cost, latency | 4 |
| Scoring Rubric | Promptfoo (llm-rubric), Braintrust (custom Scorer), DeepEval (custom Metric), RAGAS (AspectCritic) | Criteria definition for LLM-as-Judge evaluation | 5 |
| Regression Detection | Braintrust (experiment comparison), LangSmith (baseline comparison), Promptfoo (CI diff), W&B (run comparison) | Detecting quality degradation between versions | 4 |
| Red Team / Adversarial | Promptfoo (redteam), Patronus (adversarial), DeepEval (Bias, Toxicity) | Probing model for safety failures, jailbreaks, biases | 3 |
| Observability Trace | Arize Phoenix, LangSmith, W&B Weave, TruLens | Full execution trace (spans, latency, tokens, cost) per LLM call | 4 |
| Hallucination Detection | DeepEval, RAGAS, Patronus, Arize Phoenix, TruLens | Specific metric for detecting unfaithful/unsupported claims | 5 |
| Annotation/Human Eval | LangSmith (Annotation Queue), Braintrust (human review), W&B (Report) | Human-in-the-loop evaluation and labeling | 3 |
| CI Integration | Promptfoo (CLI + CI), Braintrust (CI hooks), DeepEval (pytest plugin), OpenAI Evals (CLI) | Running evals in CI/CD pipelines as quality gates | 4 |
| Benchmark Suite | OpenAI Evals (registry), W&B (Sweep), Braintrust (standard scorers) | Standardized cross-model comparison framework | 3 |

## 3. CEX Current vs Industry
| CEX Kind | Maps To | Coverage % | Gap |
|----------|---------|:----------:|-----|
| unit_eval | Test Case + Assertion (single target) | 80% | Good match. CEX unit_eval = atomic agent/prompt test. Industry test cases are more granular (per-assertion). |
| smoke_eval | Quick sanity check | 70% | CEX-unique naming. Maps loosely to Promptfoo fast assertions or CI smoke suites. Industry doesn't formalize "smoke" as a category. |
| e2e_eval | Dataset/Test Suite (pipeline) | 75% | Reasonable match. Industry e2e = full dataset run across pipeline. CEX e2e_eval is pipeline-scoped. |
| benchmark | Experiment/Run + Benchmark Suite | 80% | Good match. CEX benchmark = quantitative perf measurement. Industry Experiment adds comparison features. |
| golden_test | Test Case (high quality) | 85% | CEX golden_test = quality 9.5+ reference case. Industry equivalent: curated dataset examples, Braintrust "expected" outputs. |
| scoring_rubric | Scoring Rubric + Metric definition | 90% | Excellent match. CEX scoring_rubric = criteria framework. Direct alignment with Promptfoo llm-rubric, RAGAS AspectCritic. |

## 4. Proposed NEW Kinds (ONLY if 2+ frameworks use it)
| Kind | Justification | Frameworks | Priority |
|------|---------------|------------|:-------:|
| llm_judge | LLM-as-Judge configuration: judge model, prompt, scoring scale, criteria, few-shot calibration. The dominant eval paradigm. Currently embedded inside scoring_rubric but deserves own kind as it's a runtime config, not just criteria. | Braintrust, DeepEval, RAGAS, Patronus, Promptfoo, OpenAI Evals, Arize Phoenix | high |
| eval_dataset | Named collection of test cases with versioning, splits (train/test/val), and metadata. Industry universally separates dataset from individual test case. CEX has golden_test (single) but no collection kind. | Braintrust, LangSmith, DeepEval, RAGAS, Promptfoo, OpenAI Evals | high |
| regression_check | Baseline comparison config: previous experiment ID, threshold for degradation, alert rules. Regression detection is how industry prevents quality decay in production. | Braintrust, LangSmith, Promptfoo, W&B | med |
| red_team_eval | Adversarial test targeting safety: jailbreak, prompt injection, bias, toxicity, PII leakage. Growing industry category distinct from functional evals. | Promptfoo, Patronus, DeepEval | med |

## 5. Proposed REMOVALS/RENAMES
| Kind | Action | Reason |
|------|--------|--------|
| smoke_eval | KEEP (CEX-enriched) | Industry doesn't formalize "smoke" but the concept is universal (fast CI check). CEX's explicit naming adds clarity. No rename needed. |
| unit_eval | KEEP but refine boundary | Risk of confusion with software unit tests. Boundary should emphasize: this tests LLM behavior (non-deterministic), not code logic. |

## 6. KEEPS (validated)
| Kind | Frameworks That Match |
|------|----------------------|
| unit_eval | DeepEval LLMTestCase, Promptfoo single assertion, OpenAI Evals Sample, RAGAS SingleTurnSample |
| smoke_eval | Promptfoo fast CI assertions, DeepEval pytest quick-run |
| e2e_eval | RAGAS full pipeline eval, LangSmith experiment, Braintrust experiment |
| benchmark | W&B Sweep, Braintrust standard scorers, OpenAI Evals registry |
| golden_test | Braintrust expected outputs, LangSmith curated examples, RAGAS reference answers |
| scoring_rubric | Promptfoo llm-rubric, Braintrust LLMClassifier criteria, RAGAS AspectCritic, DeepEval custom Metric |

## 7. Summary
Current: 6 kinds → Proposed: 10 kinds (+llm_judge, +eval_dataset, +regression_check, +red_team_eval) | Coverage: ~80% → ~95%

Key insight: The LLM evaluation landscape has matured dramatically. **LLM-as-Judge** is now the dominant paradigm (7/10 frameworks), and **eval datasets** are universally treated as first-class entities separate from individual test cases. CEX's biggest gap is lacking a dataset kind (golden_test is a single case, not a collection) and not formalizing the LLM judge config. The emerging **red team** category (Promptfoo, Patronus) represents a distinct eval type that will grow in importance with AI regulation.
