---
id: atom_04_dspy
kind: knowledge_card
pillar: P01
domain: framework_atlas
title: "DSPy -- Stanford Framework for Programming (not Prompting) LMs"
version: 1.0.0
quality: null
tags: [dspy, stanford, prompt-compilation, optimizer, signature, module, framework-atlas]
sources:
  - https://dspy.ai/
  - https://github.com/stanfordnlp/dspy
  - https://dspy.ai/learn/programming/signatures/
  - https://dspy.ai/learn/programming/modules/
  - https://dspy.ai/learn/optimization/optimizers/
  - https://dspy.ai/cheatsheet/
  - https://dspy.ai/learn/programming/adapters/
  - https://dspy.ai/api/optimizers/GEPA/overview/
  - https://dspy.ai/api/optimizers/MIPROv2/
  - https://arxiv.org/abs/2310.03714
date: 2026-04-13
---

# DSPy -- Declarative Self-improving Python

> "The framework for programming -- rather than prompting -- language models."
> Origin: Stanford NLP (Oct 2023 paper, active development through 2026).
> Install: `pip install dspy`

DSPy replaces brittle hand-written prompts with composable Python modules.
Users declare WHAT the LM should do (Signatures) and HOW to invoke it (Modules).
Optimizers then automatically search for the best instructions, few-shot demos,
and/or weight updates to maximize a user-defined metric.

---

## 1. Full Module Type Registry

Modules are the building blocks. Each wraps a Signature and adds a prompting strategy.

| Module | Behavior | When to Use |
|--------|----------|-------------|
| `dspy.Predict` | Basic predictor. No added fields. Directly implements the signature. | Simple classification, extraction, QA |
| `dspy.ChainOfThought` | Injects `reasoning` field before output fields. Step-by-step thinking. | Complex reasoning, math, multi-hop QA |
| `dspy.ProgramOfThought` | LM generates executable code; execution result becomes the answer. | Math, algorithms, data transformations |
| `dspy.ReAct` | Reasoning + Acting agent loop. Can use tools iteratively. | Tool-using agents, multi-step tasks |
| `dspy.CodeAct` | Code generation + tool execution via Python interpreter. | Code-based problem solving with tool access |
| `dspy.MultiChainComparison` | Runs multiple CoT traces, compares them, picks best. | When single CoT is unreliable |
| `dspy.Parallel` | Runs multiple module instances concurrently (`num_threads`). | Batch processing, parallel exploration |
| `dspy.BestOfN` | Runs module N times, returns best by `reward_fn` or first passing `threshold`. | Quality improvement via sampling |
| `dspy.Refine` | Iterative: runs module N times, generates feedback hints between attempts. | Self-correction loops |
| `dspy.RLM` | Recursive LM -- explores large contexts via sandboxed Python REPL + recursive sub-LLM calls. | Long-context analysis, code exploration |
| `dspy.Retrieve` | Top-k passage retrieval from configured retriever. | RAG pipelines |
| `dspy.majority` | Voting function -- returns most frequent response from N predictions. | Ensemble aggregation |

### Module Composition Pattern

Custom programs inherit `dspy.Module` and override `forward()`:

```python
class MultiHopQA(dspy.Module):
    def __init__(self):
        self.generate_query = dspy.ChainOfThought("claim -> query")
        self.retrieve = dspy.Retrieve(k=5)
        self.generate_answer = dspy.ChainOfThought("context, question -> answer")

    def forward(self, question: str):
        query = self.generate_query(claim=question).query
        passages = self.retrieve(query).passages
        return self.generate_answer(context=passages, question=question)
```

Key principle: "DSPy is just Python code that uses modules in any control flow."

---

## 2. Optimizer Types and What They Optimize

### Taxonomy

| Category | What it tunes | Optimizers |
|----------|--------------|------------|
| **Automatic Few-Shot** | Demonstrations (examples in prompt) | LabeledFewShot, BootstrapFewShot, BootstrapFewShotWithRandomSearch, KNNFewShot |
| **Automatic Instruction** | Natural-language instructions + demos | COPRO, MIPROv2, SIMBA, GEPA, InferRules |
| **Automatic Finetuning** | LM weights | BootstrapFinetune |
| **Meta / Program Transforms** | Combinations of above | Ensemble, BetterTogether |

### Individual Optimizer Details

| Optimizer | Optimizes | Algorithm | Key Parameters |
|-----------|-----------|-----------|----------------|
| **LabeledFewShot** | Demos | Randomly samples k labeled examples from trainset | `k` |
| **BootstrapFewShot** | Demos | Teacher module generates demos; metric validates which to keep | `max_labeled_demos`, `max_bootstrapped_demos`, `max_rounds` |
| **BootstrapFewShotWithRandomSearch** | Demos | Repeats BootstrapFewShot with random search over candidates | `num_candidate_programs`, `num_threads` |
| **BootstrapFewShotWithOptuna** | Demos | Hyperparameter search via Optuna | Same as BootstrapFewShot + Optuna config |
| **KNNFewShot** | Demos | Semantic similarity (embeddings) to select nearest training examples | `Embedder`, trainset |
| **COPRO** | Instructions | Coordinate ascent (hill-climbing) over instruction candidates | `depth`, `breadth`, `init_temperature` |
| **MIPROv2** | Instructions + Demos | 3-phase: (1) bootstrap demos, (2) propose instructions, (3) Bayesian optimization over combos | `num_trials`, `auto="light\|medium\|heavy"`, `minibatch_size` |
| **SIMBA** | Instructions + Demos | Stochastic mini-batch sampling; finds high-variability examples; LM self-reflects on failures | `max_steps`, `max_demos` |
| **GEPA** | Instructions | Evolutionary: Pareto-frontier candidates, reflective mutation via LM trace analysis, textual feedback | `reflection_lm`, `max_metric_calls`, `use_merge` |
| **InferRules** | Rules/Instructions | Infers explicit rules from execution traces | -- |
| **BootstrapFinetune** | LM Weights | Distills prompt-based program into weight updates via finetuning | `epochs`, `batch_size`, `learning_rate` |
| **Ensemble** | Program selection | Combines N programs via `reduce_fn` (e.g., `dspy.majority`) | `reduce_fn` |
| **BetterTogether** | Instructions + Weights | Meta-optimizer: sequences prompt optimization then weight optimization | -- |

### Decision Guide

| Situation | Recommended Optimizer |
|-----------|-----------------------|
| ~10 labeled examples | BootstrapFewShot |
| 50+ examples | BootstrapFewShotWithRandomSearch |
| 0-shot (instructions only) | MIPROv2 (`max_*_demos=0`) or COPRO |
| 200+ examples, 40+ trial budget | MIPROv2 (medium or heavy) |
| Rich textual feedback available | GEPA |
| Latency-sensitive, need small model | BootstrapFinetune |

### MIPROv2 Three Phases (Detail)

1. **Bootstrap stage**: Randomly sample trainset examples, run through program, keep valid outputs as demo candidates (`num_candidates` sets).
2. **Grounded proposal stage**: Synthesize instruction candidates using dataset summaries, program code, bootstrapped examples, and random tips.
3. **Discrete search stage**: Bayesian optimization over `num_trials` iterations, evaluating instruction+demo combinations on validation data.

### GEPA Algorithm (Detail)

1. Initialize with unoptimized program
2. Sample candidate from Pareto frontier
3. Collect execution traces + textual feedback on minibatch
4. LM reflects on traces: what worked, what failed, why
5. Propose mutated instruction targeting observed failures
6. Evaluate; update Pareto frontier if improved
7. Optional merge: combine best-performing module variants
8. Repeat until budget exhausted
9. Return best on validation set

GEPA uniquely accepts `ScoreWithFeedback` (score + textual explanation) rather than just scalar metrics.

### Historical Note: Teleprompter -> Optimizer

DSPy originally called these "teleprompters" (2023 paper). Renamed to "optimizers" for clarity. The `.compile()` method persists. Old code: `dspy.teleprompt.BootstrapFewShot` still works as import alias.

---

## 3. Signature System -- How Prompts Become Programs

### Core Concept

A **Signature** is a declarative specification of input/output behavior.
It separates INTERFACE ("what should the LM do?") from IMPLEMENTATION ("how do we prompt it?").
DSPy infers or learns the implementation automatically.

### Inline Signatures (shorthand)

```python
# Basic QA
predict = dspy.Predict("question -> answer")

# With types
predict = dspy.Predict("question: str -> answer: str")

# Multi-input
predict = dspy.Predict("context: list[str], question: str -> answer: str")

# Boolean classification
predict = dspy.Predict("sentence -> sentiment: bool")

# With instructions
sig = dspy.Signature("comment -> toxic: bool",
    instructions="Mark toxic if comment includes insults or harassment.")
predict = dspy.Predict(sig)
```

### Class-Based Signatures (full control)

```python
class CheckCitationFaithfulness(dspy.Signature):
    """Verify that the text is based on the provided context."""

    context: str = dspy.InputField(desc="facts here are assumed to be true")
    text: str = dspy.InputField()
    faithfulness: bool = dspy.OutputField()
    evidence: dict[str, list[str]] = dspy.OutputField(desc="supporting evidence for claims")
```

### Field Parameters

| Parameter | Applies To | Purpose |
|-----------|-----------|---------|
| `desc` | InputField, OutputField | Semantic hint for the LM |
| Type hints | Both | `str`, `int`, `bool`, `float`, `list[str]`, `dict`, `Optional`, `Literal[...]`, Pydantic models |
| `dspy.Image` | InputField | Multimodal image input |
| `dspy.History` | InputField | Conversation history |

### Literal Type Constraints

```python
class Emotion(dspy.Signature):
    """Classify emotion."""
    sentence: str = dspy.InputField()
    sentiment: Literal['sadness', 'joy', 'love', 'anger', 'fear', 'surprise'] = dspy.OutputField()
```

### How Expansion Works

1. Adapter reads the Signature's fields and docstring
2. Generates system message with field structure
3. Formats input data per field types
4. Module may inject extra fields (e.g., ChainOfThought adds `reasoning`)
5. Optimizer may inject instructions and few-shot demos
6. LM produces output; adapter parses it back into `dspy.Prediction`

### Adapters (Signature -> Prompt formatters)

| Adapter | Format | Best For |
|---------|--------|----------|
| `ChatAdapter` (default) | `[[ ## field_name ## ]]` markers + `[[ ## completed ## ]]` | Universal compatibility |
| `JSONAdapter` | JSON object output | Models with `response_format` support; lower latency |
| `XMLAdapter` | XML-structured output | When XML format preferred |
| `TwoStepAdapter` | Free-form first stage, structured extraction second | Reasoning models (o3, o1) that struggle with structured output |

Configuration:
```python
dspy.configure(adapter=dspy.JSONAdapter())
# or per-block:
with dspy.context(adapter=dspy.XMLAdapter()):
    result = my_module(input="...")
```

---

## 4. Metric / Evaluation Vocabulary

### Built-in Metrics

| Metric | Type | What It Measures |
|--------|------|-----------------|
| `dspy.evaluate.answer_exact_match` | Function | Exact string match between prediction and gold |
| `dspy.evaluate.answer_passage_match` | Function | Whether answer appears in a passage |
| `dspy.evaluate.SemanticF1` | Class | Precision + recall + F1 via semantic overlap |
| `dspy.evaluate.CompleteAndGrounded` | Class | Completeness (covers question) + groundedness (supported by context) |

### Custom Metric Pattern

```python
def my_metric(gold, pred, trace=None):
    # gold: dspy.Example with .labels()
    # pred: dspy.Prediction from your program
    # trace: optimization context (None during eval)
    # Return: bool (pass/fail) or float (0.0-1.0)
    return pred.answer == gold.answer
```

### LLM-as-Judge Pattern

```python
class AnswerQuality(dspy.Signature):
    """Judge whether the answer is correct given context and question."""
    context: str = dspy.InputField()
    question: str = dspy.InputField()
    answer: str = dspy.InputField()
    correct: bool = dspy.OutputField()

judge = dspy.ChainOfThought(AnswerQuality)
def llm_metric(gold, pred, trace=None):
    return judge(context=gold.context, question=gold.question, answer=pred.answer).correct
```

### GEPA Feedback Metric (advanced)

```python
from dspy import ScoreWithFeedback

def feedback_metric(gold, pred, trace=None, predictor_name=None, predictor_trace=None):
    score = compute_score(gold, pred)
    feedback = f"Missing key facts: {find_gaps(gold, pred)}"
    return ScoreWithFeedback(score=score, feedback=feedback)
```

### Evaluate Utility

```python
evaluator = dspy.Evaluate(
    devset=my_devset,
    metric=my_metric,
    num_threads=8,
    display_progress=True,
    display_table=5        # show top 5 rows
)
score = evaluator(my_program)
```

### Data Primitives

| Class | Role |
|-------|------|
| `dspy.Example` | Training/test data row. Dict-like with `.inputs()` / `.labels()` split. |
| `dspy.Prediction` | Module output. Subclass of Example. Access via `pred.field_name`. |
| `dspy.Image` | Multimodal image wrapper for signatures |
| `dspy.History` | Conversation history primitive |
| `dspy.Audio` | Audio data primitive |
| `dspy.Code` | Code execution primitive |

---

## 5. Assertions -- Computational Constraints

| Construct | Type | On Failure |
|-----------|------|-----------|
| `dspy.Assert(condition, message)` | Hard constraint | Retries up to max; halts pipeline if exhausted |
| `dspy.Suggest(condition, message)` | Soft constraint | Retries with feedback; continues if exhausted |

Both inject the failing output + error message back into the prompt for self-refinement.
Assertions also improve optimization: optimizers can bootstrap harder few-shot examples
from assertion-validated traces.

---

## 6. Tools and Retrieval

| Class | Purpose |
|-------|---------|
| `dspy.Tool` | Wraps any Python function as a callable tool with signature introspection |
| `dspy.ToolCalls` | Tool invocation handling within agent modules |
| `dspy.Retrieve` | Top-k retrieval from configured retriever |
| `dspy.ColBERTv2` | Dense retrieval backend |
| `dspy.PythonInterpreter` | Sandboxed code execution tool |

### Utilities

| Utility | Purpose |
|---------|---------|
| `dspy.streamify` | Enable streaming output with `StreamListener` |
| `dspy.asyncify` | Convert sync modules to async |
| `dspy.configure_cache` | Control disk/memory caching |
| `dspy.configure(track_usage=True)` | Token usage tracking per model |

---

## 7. Language Model Interface

| Class | Purpose |
|-------|---------|
| `dspy.LM` | Language model wrapper (backed by litellm). Supports any provider. |
| `dspy.Embedder` | Embedding model interface for retrieval/similarity |

Configuration:
```python
lm = dspy.LM("openai/gpt-4o", temperature=0.7)
dspy.configure(lm=lm)
```

---

## 8. DSPy "Prompt Compilation" -> CEX `prompt_compiler` Kind Mapping

DSPy's core thesis: **prompts should be compiled, not written.** This maps directly
to CEX's `prompt_compiler` kind (P03), which performs intent-to-artifact transmutation.

### Conceptual Alignment

| DSPy Concept | CEX Equivalent | Notes |
|-------------|----------------|-------|
| **Signature** | Kind schema (`_schema.yaml`) | Declarative I/O spec. DSPy: `"question -> answer"`. CEX: kind frontmatter + field definitions. |
| **Module** | Builder (`archetypes/builders/{kind}-builder/`) | Wraps a signature with strategy. DSPy: `ChainOfThought`. CEX: 13-ISO builder with sin lens. |
| **Optimizer** | `cex_evolve.py` + `cex_score.py` | Tunes program quality. DSPy: MIPROv2 searches instruction space. CEX: evolve loop rescans + rewrites weak artifacts. |
| **Metric** | Quality gate (3-layer scoring) | DSPy: `SemanticF1`. CEX: structural (30%) + rubric (30%) + semantic (40%). |
| **Evaluate** | `cex_doctor.py` + `cex_system_test.py` | Batch validation. DSPy: `Evaluate(devset=...)`. CEX: 54-test suite + flywheel audit. |
| **Adapter** | Prompt layers (`cex_prompt_layers.py`) | Formats context for LM. DSPy: ChatAdapter/JSONAdapter. CEX: 15+ pillar artifacts compiled into prompt. |
| **Assertion** | 8F F7 GOVERN gates | Hard/soft constraints. DSPy: `dspy.Assert`. CEX: H01-H07 hard gates + 12LP checklist. |
| **Teleprompter (old)** | Prompt Compiler kind | The original DSPy name for optimizer. CEX's `prompt_compiler` kind description explicitly references "DSPy term". |
| **`.compile()`** | `cex_compile.py` | DSPy: optimize program. CEX: .md -> .yaml compilation + index. |
| **Example / trainset** | Knowledge Cards (KCs) | Training data. DSPy: labeled Examples. CEX: kc_{kind}.md files with domain knowledge. |
| **Few-shot demos** | `examples/` + `compiled/` artifacts | In-context examples. DSPy: bootstrapped demos. CEX: F3 INJECT pulls similar artifacts. |
| **Program** | 8F Pipeline | The composed system. DSPy: Module with forward(). CEX: F1-F8 sequential reasoning. |
| **`dspy.configure(lm=...)`** | `nucleus_models.yaml` + `cex_router.py` | Model routing. DSPy: single LM config. CEX: per-nucleus model assignment with fallback chains. |

### Deeper Parallel: The Compilation Loop

```
DSPy:
  Signature -> Module -> Program -> Optimizer.compile(trainset, metric) -> Optimized Program
  (declare)    (wrap)   (compose)   (search instruction/demo space)       (better prompts)

CEX:
  Kind -> Builder -> 8F Pipeline -> cex_evolve.py(artifacts, quality_gate) -> Improved Artifacts
  (schema) (ISOs)   (F1-F8)        (rescan, rewrite, score, keep/discard)   (higher quality)
```

Both systems share the thesis that prompt quality should be **searched, not hand-crafted**.
DSPy searches over instruction text and demo selection via Bayesian optimization.
CEX searches over artifact content via heuristic passes and agent-mode rewrites.

### Key Difference

DSPy optimizes the **prompt parameters** (instructions, demos, weights) for a fixed program structure.
CEX optimizes the **artifact content** (knowledge cards, templates, configs) for a fixed pipeline structure (8F).
DSPy is runtime prompt optimization. CEX is build-time artifact optimization.

---

## 9. Complete Vocabulary Index

| Term | Category | Definition |
|------|----------|-----------|
| Adapter | Core | Bridge between Signature and LM; formats prompts, parses responses |
| Assert | Assertion | Hard constraint; halts pipeline on repeated failure |
| Audio | Primitive | Audio data type for multimodal signatures |
| BestOfN | Module | Sample N outputs, return best by reward function |
| BetterTogether | Optimizer | Meta-optimizer combining prompt + weight optimization |
| BootstrapFewShot | Optimizer | Teacher generates validated demos for few-shot |
| BootstrapFewShotWithOptuna | Optimizer | Hyperparameter search variant via Optuna |
| BootstrapFewShotWithRandomSearch | Optimizer | Random search over candidate programs |
| BootstrapFinetune | Optimizer | Distill prompt program into LM weight updates |
| BootstrapRS | Optimizer | Alias/variant for bootstrap with random search |
| ChainOfThought | Module | Injects step-by-step reasoning before output |
| ChatAdapter | Adapter | Default; uses `[[ ## field ## ]]` markers |
| Code | Primitive | Code execution data type |
| CodeAct | Module | Code generation + tool execution agent |
| ColBERTv2 | Tool | Dense retrieval backend |
| compile() | Method | Apply optimizer to program; returns optimized version |
| CompleteAndGrounded | Metric | Checks completeness + context groundedness |
| configure() | Function | Global settings: lm, adapter, rm, track_usage |
| configure_cache() | Function | Control disk/memory caching |
| COPRO | Optimizer | Coordinate ascent over instruction candidates |
| Document | Experimental | Document handling primitive |
| Embedder | Core | Embedding model interface |
| Ensemble | Optimizer | Combine N programs via reduce function |
| Evaluate | Core | Batch evaluation utility with threading + display |
| Example | Primitive | Training/test data row with inputs()/labels() split |
| GEPA | Optimizer | Evolutionary; Pareto-frontier + reflective mutation |
| History | Primitive | Conversation history for multi-turn |
| Image | Primitive | Multimodal image wrapper |
| InferRules | Optimizer | Infer explicit rules from execution traces |
| InputField | Signature | Input field declaration with desc, type hints |
| JSONAdapter | Adapter | JSON-structured output; lower latency |
| KNNFewShot | Optimizer | Semantic-similarity example selection |
| LabeledFewShot | Optimizer | Simple random selection from labeled trainset |
| LM | Core | Language model wrapper (litellm backend) |
| majority | Function | Voting aggregator for ensemble predictions |
| MCP | Experimental | Model Context Protocol integration |
| MIPROv2 | Optimizer | 3-phase Bayesian: bootstrap + propose + search |
| Module | Core | Base class for all DSPy components; override forward() |
| MultiChainComparison | Module | Compare multiple CoT traces, pick best |
| OutputField | Signature | Output field declaration with desc, type constraints |
| Parallel | Module | Concurrent multi-module execution |
| Predict | Module | Basic predictor; no added fields |
| Prediction | Primitive | Module output; subclass of Example |
| ProgramOfThought | Module | LM generates code; execution = answer |
| PythonInterpreter | Tool | Sandboxed code execution |
| ReAct | Module | Reasoning + Acting agent loop with tools |
| Refine | Module | Iterative self-correction with feedback hints |
| Retrieve | Module | Top-k passage retrieval |
| RLM | Module | Recursive LM with sandboxed REPL |
| ScoreWithFeedback | Metric | Score + textual explanation (for GEPA) |
| SemanticF1 | Metric | Precision + recall + F1 via semantic overlap |
| Signature | Core | Declarative I/O behavior specification |
| SIMBA | Optimizer | Mini-batch sampling + self-reflective improvement |
| streamify | Utility | Enable streaming output |
| asyncify | Utility | Sync -> async module conversion |
| Suggest | Assertion | Soft constraint; continues on repeated failure |
| Teleprompter | Deprecated | Old name for Optimizer (2023 paper) |
| Tool | Core | Function wrapper with signature introspection |
| ToolCalls | Core | Tool invocation handling |
| TwoStepAdapter | Adapter | Free-form then structured; for reasoning models |
| XMLAdapter | Adapter | XML-structured output format |

---

## Properties

| Property | Value |
|----------|-------|
| Kind | knowledge_card |
| Pillar | P01 |
| Domain | framework_atlas |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
