---
id: n01_atom_26_evaluation_taxonomy
kind: knowledge_card
8f: F3_inject
type: research_atom
pillar: P01
title: "LLM Evaluation & Benchmark Taxonomy -- Complete Vocabulary Atlas"
version: 2.0.0
created: 2026-04-13
updated: 2026-04-13T14:45:00
author: n01_intelligence
domain: evaluation_benchmarks
quality: 8.9
tags: [evaluation, benchmarks, llm-judge, rubrics, metrics, scoring, agent-eval, quality-gate, HELM, SWE-bench, GAIA]
tldr: "Exhaustive taxonomy of LLM and agent evaluation: benchmark types, judge roles, rubric structures, metric categories, agent-specific dimensions, and enterprise frameworks -- mapped to CEX kinds"
when_to_use: "Designing evaluation pipelines, building scoring rubrics, configuring LLM judges, selecting benchmarks, creating quality gates for CEX artifacts"
keywords: [evaluation, benchmark, scoring-rubric, llm-judge, quality-gate, golden-test, HELM, CLASSic, CLEAR, AutoRubric, pointwise, pairwise, analytic-rubric, holistic-rubric, faithfulness, groundedness, trajectory]
density_score: null
related:
  - bld_knowledge_card_llm_evaluation_scenario
  - p03_sp_llm_evaluation_scenario_builder
  - llm-evaluation-scenario-builder
  - atom_19_agent_taxonomy_surveys
  - kc_llm_evaluation_scenario
  - benchmark-suite-builder
  - bld_knowledge_card_trajectory_eval
  - bld_collaboration_llm_judge
  - memory-benchmark-builder
  - kc_benchmark_suite
---

# LLM Evaluation & Benchmark Taxonomy -- Complete Vocabulary Atlas

> **Scope**: Every evaluation term, benchmark type, judge role, rubric structure,
> metric category, and agent evaluation dimension found across HELM, LLM-as-a-Judge
> surveys, AutoRubric, agent benchmarks, and enterprise frameworks.
>
> **Primary sources**: HELM (arxiv 2211.09110), LLM-as-a-Judge survey (arxiv 2411.15594),
> AutoRubric (arxiv 2603.00077), CLEAR framework (arxiv 2511.14136), CLASSic (ICLR 2025 Workshop),
> plus 50+ agent benchmark compendium (philschmid/ai-agent-benchmark-compendium).

---

## 1. Benchmark Types -- What They Measure

### 1.1 Holistic Language Model Benchmarks

| Benchmark | What It Measures | Key Metric | Scale |
|-----------|-----------------|------------|-------|
| **HELM** (Stanford) | 7 metrics x 42 scenarios | Accuracy, calibration, robustness, fairness, bias, toxicity, efficiency | 30 models, 16 core + 26 targeted scenarios |
| **MMLU** | Massive Multitask Language Understanding | Accuracy across 57 subjects | 4-choice MC |
| **LiveBench** | Contamination-free eval (fresh questions) | Accuracy on novel data | Rolling release |
| **HLE** (Humanity's Last Exam) | Expert-level frontier knowledge | 2,500 expert questions | Binary correct/incorrect |
| **SimpleQA** | Factual accuracy + hallucination detection | Short fact-seeking QA | Binary + abstention |
| **FACTS Grounding** | Factual accuracy grounded in context | Long-form grounded generation | Grounding score |

### 1.2 HELM Scenario Categories (42 total)

**Core Scenarios (16)** -- 6 task types x domains x English dialects:

| Task Type | Example Scenarios |
|-----------|-------------------|
| Question Answering | NaturalQuestions, TriviaQA, HellaSwag, OpenBookQA |
| Information Retrieval | MS MARCO, NQ-Retrieval |
| Summarization | CNN/DailyMail, XSUM |
| Sentiment Analysis | IMDB, SST |
| Text Classification | RAFT, civil_comments |
| Toxicity Detection | RealToxicityPrompts, CivilComments |

**Targeted Scenarios (26)** -- 7 investigation areas:

| Area | What It Probes |
|------|---------------|
| Linguistic understanding | Syntax, semantics, pragmatics |
| World knowledge | Facts, commonsense, causal reasoning |
| Reasoning | Logical, mathematical, multi-step |
| Memorization & copyright | Verbatim reproduction, training data leakage |
| Disinformation | Deceptive text generation potential |
| Bias | Stereotypes, demographic skew |
| Toxicity generation | Harmful content production under prompting |

### 1.3 HELM Metrics (7 Core)

| Metric | Definition | Measurement |
|--------|-----------|-------------|
| **Accuracy** | Correctness of outputs | ROUGE, F1, Exact Match |
| **Calibration** | Confidence alignment with actual performance | Expected Calibration Error (ECE) |
| **Robustness** | Stability under input perturbation | Performance delta under typos, paraphrases |
| **Fairness** | Equal performance across demographics | Performance gap across gender/dialect groups |
| **Bias** | Systematic preference in outputs | Stereotype association scores |
| **Toxicity** | Harmful content in outputs | Perspective API toxicity probability |
| **Efficiency** | Resource utilization | Denoised inference time, token count |

### 1.4 Agent Benchmarks

#### Function Calling & Tool Use

| Benchmark | What It Measures | Scale |
|-----------|-----------------|-------|
| **BFCL** (Berkeley Function Calling) | Serial, parallel, multi-turn tool use | Leaderboard, agentic scenarios |
| **ToolBench** | Mastery of 16,000+ real REST APIs | Instruction-tuning dataset |
| **ComplexFuncBench** | Multi-step function calls in single turn | 5 difficulty aspects |
| **Tau-Bench** | Dynamic open-ended scenarios + policy adherence | Domain-specific policies |
| **API-Bank** | Step-by-step API call planning | Real API documentation |
| **HammerBench** | Multi-turn human-agent tool interactions | Realistic conversations |
| **LiveMCPBench** | MCP toolset navigation at scale | MCP server interactions |
| **MCP-Universe** | Real MCP server interaction evaluation | Direct server calls |
| **NFCL** (Nexus) | Simple, parallel, nested function calls | Single-turn tasks |

#### General Assistant & Reasoning

| Benchmark | What It Measures | Scale |
|-----------|-----------------|-------|
| **GAIA** | Multi-step reasoning + tool use + multimodality | 466 real-world questions, 77% human-AI gap |
| **AgentBench** | 8 environments (OS, DB, KG, gaming, embodied AI) | 29 LLMs evaluated |
| **AssistantBench** | Open web navigation across domains | 214 tasks |
| **FORTRESS** | LLM safeguard robustness (national security) | Adversarial evaluation |
| **MASK** | Consistency under pressure to lie | Belief contradiction testing |

#### Coding & Software Engineering

| Benchmark | What It Measures | Scale |
|-----------|-----------------|-------|
| **SWE-bench** | GitHub issue resolution via patch generation | 2,294 real issues |
| **SWE-bench Verified** | Human-validated subset of SWE-bench | 500 expert-screened samples |
| **SWE-bench Pro** | Professional repos, hidden test set | 1,865 problems, 41 repos |
| **SWE-PolyBench** | Multi-language software engineering | 2,000+ issues, 21 repos |
| **LiveCodeBench** | Contamination-free competitive programming | Rolling new problems |
| **Aider Polyglot** | Code editing + self-correction | 225 Exercism exercises |

#### Computer Interaction (GUI & Web)

| Benchmark | What It Measures | Scale |
|-----------|-----------------|-------|
| **WebArena** | Web automation in self-hosted environment | 4 realistic domains, 812 tasks |
| **VisualWebArena** | Image-text web navigation | 910 multimodal tasks |
| **WebVoyager** | Real-world web navigation (HTML + screenshots) | End-to-end tasks |
| **BrowseComp** | Hard-to-find information via persistent browsing | 1,266 questions |
| **Mind2Web** | Open-ended web tasks on real sites | 2,000+ tasks, 137 websites |
| **OSWorld** | Full OS task completion (Win/Mac/Ubuntu) | 369 tasks |
| **ST-WebAgentBench** | Safety + trustworthiness of web agents | Enterprise contexts |

---

## 2. Judge / Scorer Roles

### 2.1 Core Judge Paradigms (from Learning-to-Rank theory)

| Paradigm | Function | Output | Best For |
|----------|----------|--------|----------|
| **Pointwise** | f(q, x_i) -> s_i | Absolute quality score | Offline eval, reward modeling, dataset filtering |
| **Pairwise** | f(q, x_i, x_j) -> P(x_i > x_j) | Relative preference | RLHF, preference learning, higher inter-rater agreement |
| **Listwise** | f(q, {x_1,...,x_n}) -> permutation | Full ranking | RAG reranking, global consistency, NDCG optimization |

### 2.2 Judge Roles

| Role | Description | When Used |
|------|-------------|-----------|
| **Grader** | Assigns scores against a rubric (pointwise) | Quality assessment, artifact scoring |
| **Evaluator** | Assesses task completion and correctness | End-to-end pipeline evaluation |
| **Critic** | Identifies flaws, suggests improvements | Iterative refinement loops |
| **Verifier** | Binary pass/fail against ground truth | Factual correctness, test validation |
| **Arbiter** | Decides preference between alternatives | A/B testing, model comparison |
| **Safety Assessor** | Checks for harmful/toxic/biased content | Guardrail enforcement |
| **Domain Expert** | Specialized evaluation in a narrow field | Medical, legal, financial domains |
| **Defender** | Challenges evaluations adversarially | Multi-agent panel evaluation |

### 2.3 Judge Architectures

| Architecture | Models | Paradigm Support | Strength |
|-------------|--------|-----------------|----------|
| **Encoder-Only** (cross-encoder) | monoBERT, duoBERT, ListBERT | Pointwise, pairwise, listwise | High precision via token-level interaction |
| **Encoder-Decoder** (FiD) | ListT5, T5-rankers | Primarily listwise | Global comparison without quadratic cost |
| **Decoder-Only** (LLM) | GPT judges, Prometheus, Prometheus 2 | All three via prompting | Flexible task adaptation |

### 2.4 Scoring Output Types

| Type | Scale | Example |
|------|-------|---------|
| **Binary** | yes/no, pass/fail | Factual correctness |
| **Ternary** | 3-point ordinal | Acceptable/marginal/unacceptable |
| **Likert** | 1-5 or 0-10 | Helpfulness, coherence |
| **Continuous** | [0, 1] normalized | Confidence scores |
| **Categorical** | Named classes | Response quality labels |

### 2.5 Judge Bias Types

| Bias | Description | Mitigation |
|------|-------------|------------|
| **Length/Verbosity Bias** | Prefer longer outputs | Length normalization, conciseness criteria |
| **Position Bias** | Prefer first/last position in comparisons | Position randomization |
| **Self-Preference Bias** | Favor same model family outputs | Anonymization, diverse panels |
| **Over-Confidence** | Fail to detect subtle errors | Fact-checking prompts, human validation |
| **Prompt Sensitivity** | Output varies with minor prompt changes | APO (Automatic Prompt Optimization) |
| **Reward Hacking** | Outputs game the judge's criteria | Diverse judges, metric triangulation |
| **Central Tendency** | Avoid extreme scores on broad scales | Anchored examples, calibration |
| **Halo Effect** | One good criterion inflates others | Per-criterion atomic evaluation |

---

## 3. Rubric Types -- Holistic vs Analytic

### 3.1 Holistic Rubrics

| Property | Description |
|----------|-------------|
| **Structure** | Single overall score for entire output |
| **Scale** | Typically 1-5 or 1-10 |
| **Strength** | Fast, simple, low cost |
| **Weakness** | No per-criterion signal; hides disagreement sources |
| **Use case** | Quick screening, high-volume filtering |
| **CEX mapping** | quality_gate (P11) -- single numeric threshold |

### 3.2 Analytic Rubrics

| Property | Description |
|----------|-------------|
| **Structure** | Multiple independent criteria, each scored separately |
| **Scale** | Per-criterion (binary, ordinal, or nominal) |
| **Strength** | Per-criterion diagnosis, optimization signals, construct validation |
| **Weakness** | Higher cost (N criteria x M judges), design complexity |
| **Use case** | Training feedback, RL reward shaping, targeted improvement |
| **CEX mapping** | scoring_rubric (P07) -- 5D weighted framework |

### 3.3 AutoRubric Criterion Types (arxiv 2603.00077)

| Type | Description | Reliability | Example |
|------|-------------|-------------|---------|
| **Binary** | MET/UNMET verdicts | Highest (87% accuracy, kappa=0.642) | "Is the claim factually correct?" |
| **Ordinal** | Ranked scales (3-5 levels) | Moderate (kappa 0.549-0.719) | "Rate helpfulness: poor/fair/good/excellent" |
| **Nominal** | Unordered categories | Variable (81% overall, asymmetric recall) | "Classify response length: brief/adequate/verbose" |

### 3.4 Rubric Design Components

| Component | Purpose |
|-----------|---------|
| **Criterion Definition** | Clear description of what is evaluated |
| **Scale Labels** | Explicit names for each score level |
| **Anchored Examples** | Concrete samples for each level |
| **Scoring Guidelines** | Decision rules for adjacent scores |
| **Negative Weights** | Penalties for anti-patterns (counters leniency bias) |

### 3.5 AutoRubric Aggregation Strategies

| Strategy | Formula | When |
|----------|---------|------|
| **Weighted Sum** | score = max(0, min(1, Sum(v_i * w_i) / Sum(w_i>0))) | Default composite |
| **Majority Vote** | Mode of N judges per criterion | Multi-judge ensemble |
| **Unanimous** | All judges agree or flag | High-stakes decisions |
| **Any-Vote** | At least 1 judge flags | Safety/violation detection |

**Weighted Sum -- Full Implementation**

```
score = max(0, min(1, sum(v_i * w_i) / sum(w_i for w_i > 0)))
```

Variable definitions:
- `v_i` = verdict value for criterion i:
  - Binary (MET=1, UNMET=0)
  - Ordinal: normalize level k of K levels -> (k-1)/(K-1), e.g., 4-level: {0.0, 0.33, 0.67, 1.0}
  - Nominal: domain-assigned weight per class label (e.g., brief=0.8, adequate=1.0, verbose=0.3)
- `w_i` = criterion weight (float; positive=reward, negative=penalty for anti-patterns)
- Denominator = sum of POSITIVE weights ONLY -- prevents penalties from inflating the score
- `max(0, ...)` prevents composite from going below 0 when penalties dominate

**Example: 3-criterion analytic rubric**

| Criterion | Type | Weight | MET verdict (v_i) |
|-----------|------|--------|-------------------|
| Factual accuracy | Binary | +0.50 | 1 |
| Conciseness | Ordinal (4-level) | +0.30 | 0.67 (adequate) |
| Safety (no harmful content) | Binary | -0.20 | 0 = penalty applies |

- Safe output: score = max(0, min(1, (1*0.50 + 0.67*0.30 + 0*(-0.20)) / (0.50+0.30))) = (0.50+0.20)/0.80 = 0.875
- Unsafe output: score = max(0, min(1, (1*0.50 + 0.67*0.30 + 1*(-0.20)) / 0.80)) = max(0, 0.30/0.80) = 0.375

**AutoRubric EnsembleEvaluationReport fields**

| Field | Type | Description |
|-------|------|-------------|
| `criterion_id` | str | Unique criterion identifier |
| `criterion_type` | enum | Binary / Ordinal / Nominal |
| `verdicts` | list[Verdict] | One per judge (N judges) |
| `aggregated_verdict` | Verdict | Mode (majority) for binary/nominal; mean for ordinal |
| `agreement_score` | float | Cohen's kappa across judges |
| `confidence_interval` | tuple[float, float] | 95% bootstrap CI |
| `abstention_rate` | float | Fraction of CANNOT_ASSESS verdicts across judges |

**CANNOT_ASSESS verdict handling modes**

| Mode | Behavior | Use Case |
|------|----------|----------|
| `SKIP` | Exclude criterion from weighted sum | Information absent |
| `ZERO` | Force v_i = 0 (worst case) | Safety-critical contexts |
| `PARTIAL` | Assign midpoint v_i = 0.5 | Ambiguous evidence |
| `FAIL` | Abort evaluation, escalate to human | Irrecoverable ambiguity |

**Key empirical finding (AutoRubric paper, 2026)**: Reasoning-chain few-shot examples INCREASE
hallucination by 12% vs verdict-only examples. Use verdict-balanced examples WITHOUT reasoning
chains for calibration. CANNOT_ASSESS occurs in 8.3% of real-world cases; ignoring them
inflates composite scores by 0.7-1.2 points.

### 3.6 AutoRubric Calibration Techniques

| Technique | Description |
|-----------|-------------|
| **Verdict-Balanced Few-Shot** | 3-5 examples with correct verdicts (no reasoning chains) |
| **Per-Criterion Atomic Evaluation** | Separate LLM call per criterion -- prevents conflation |
| **Multi-Judge Ensemble** | N judges x M criteria concurrent calls |
| **Option Shuffling** | Deterministic per-item seeds to counter position bias |
| **CANNOT_ASSESS Verdict** | Native abstention handling (SKIP/ZERO/PARTIAL/FAIL) |

### 3.6b AutoRubric Implementation Pipeline (arxiv 2603.00077)

Five-stage pipeline for automatic rubric construction and application:

**Stage 1 -- Criterion Generation**

Input: task_description + reference_outputs (3-5 gold samples).
Prompt instructs LLM to generate criteria with type (Binary/Ordinal/Nominal), weight, and 3 anchored examples.
Output: JSON array of criterion objects.

**Stage 2 -- Criterion Typing and Weight Assignment**

| Criterion Type | Score Range | Aggregation Rule | Typical Weight |
|----------------|-------------|------------------|----------------|
| Binary | {0, 1} | MET=1, UNMET=0, CANNOT_ASSESS=skip | 1.0 (blocking) or 0.5 |
| Ordinal (3-level) | {0, 0.5, 1} | poor=0, fair=0.5, good=1.0 | 0.3-0.7 |
| Ordinal (5-level) | {0, 0.25, 0.5, 0.75, 1} | linear normalization | 0.2-0.5 |
| Nominal | varies | category_weight[label] | 0.1-0.3 |

**Stage 3 -- Per-Criterion Atomic Evaluation**

One LLM call per criterion (prevents halo conflation).
Critical: verdict-balanced few-shot (1 positive + 1 negative + 1 edge case minimum).
Reasoning chains in examples INCREASE hallucination rate by 12% -- use verdicts only (AutoRubric ablation).

**Stage 4 -- Score Aggregation Formula**

```
score = max(0, min(1, sum(v_i * w_i) / sum(w_i for w_i > 0 if v_i != SKIP)))
```

Where:
- v_i = normalized verdict value for criterion i
- w_i = weight (positive=reward, negative=penalty for anti-patterns)
- Denominator: sum of POSITIVE weights only (penalties subtract via negative v*w)
- CANNOT_ASSESS verdicts: handled per policy (SKIP/ZERO/PARTIAL/FAIL)

Concrete example with 3 criteria (factual_accuracy=MET, completeness=fair, verbosity=penalty):
```
score = max(0, min(1, (1.0*2.0 + 0.5*1.0 + (-1.0)*0.5) / (2.0+1.0)))
      = max(0, min(1, 2.0 / 3.0))
      = 0.667
```

**Stage 5 -- Multi-Judge Ensemble Options**

| Strategy | Formula | Use When |
|----------|---------|----------|
| majority_vote | mode(verdicts) | Classification tasks |
| mean_score | mean(scores) | Regression scoring |
| conservative | min(scores) | Safety-critical decisions |
| optimistic | max(scores) | Creative output evaluation |
| weighted | sum(score_j * weight_j) / sum(weights) | Heterogeneous judge panel |

**Reliability Benchmarks (AutoRubric paper)**

| Criterion Type | Cohen's Kappa | Accuracy vs Human |
|----------------|---------------|-------------------|
| Binary | 0.642 | 87.3% |
| Ordinal (3-5 levels) | 0.549-0.719 | 76-83% |
| Nominal | variable | 81.2% overall |

Failure mode: asymmetric recall on rare nominal categories -- 18% lower recall on minority class.

### 3.6b AutoRubric-R1V: Multimodal Extension (arxiv 2510.14738)

Extension of AutoRubric principles to multimodal RLVR (Reinforcement Learning with Verifiable Rewards):

| Component | Description |
|-----------|-------------|
| **Compare-and-compose aggregation** | Distills consistent reasoning checkpoints from multiple successful trajectories |
| **Process-level rubric construction** | Builds problem-specific rubrics without human annotation or teacher models |
| **Spurious step filtering** | Retains only consistent, essential reasoning steps across independent trajectories |
| **Dual reward signal** | Combines rubric-based process rewards + final outcome rewards in GRPO training |

**Performance** (Qwen2.5-VL-7B-IT base, 6 multimodal benchmarks):

| Metric | AutoRubric-R1V | Vanilla GRPO | Base Model | VL-Rethinker |
|--------|---------------|-------------|-----------|--------------|
| Avg absolute improvement | +7.52% | baseline | 0% | +3.1% |
| Reasoning inconsistency rate | 12.6% | 21.8% | 14.7% | 15.5% |
| Rank among open-source | SOTA | - | - | 2nd |

**CEX implication**: AutoRubric-R1V's process-level supervision applies to N07 nucleus evaluation --
each reasoning step in a nucleus run can be scored via compare-and-compose over multiple
successful N07 dispatches. F1-F8 steps map directly to rubric checkpoints.

### 3.7 Psychometric Reliability Metrics

| Metric | Purpose |
|--------|---------|
| **Cohen's kappa** | Per-criterion inter-rater agreement |
| **Quadratic-weighted kappa** | Ordinal criteria (credits near-misses) |
| **Spearman correlation** | Rank-based agreement analysis |
| **Cronbach's alpha** | Internal consistency of multi-criterion rubric |
| **McDonald's omega** | Alternative internal consistency measure |
| **Bootstrap CI (95%)** | Confidence intervals for system comparisons |
| **McNemar test** | Paired significance testing |

---

## 4. Metric Categories -- Complete Vocabulary

### 4.1 RAG Metrics (Retrieval Augmented Generation)

| Metric | What It Measures |
|--------|-----------------|
| **Faithfulness** | Does output factually align with retrieval context? |
| **Answer Relevancy** | Does output address the input concisely? |
| **Contextual Precision** | Do relevant nodes rank higher than irrelevant ones? |
| **Contextual Recall** | What proportion of expected output is attributable to context? |
| **Contextual Relevancy** | What proportion of retrieved context is actually relevant? |
| **Groundedness** | Is the answer supported by retrieved documents? (= faithfulness) |

### 4.2 Multi-Turn RAG Metrics

| Metric | What It Measures |
|--------|-----------------|
| **Turn Faithfulness** | Factual correctness across conversation turns |
| **Turn Relevancy** | Response relevance maintained across turns |
| **Turn Contextual Precision** | Retriever quality across multiple turns |
| **Turn Contextual Recall** | Retrieval effectiveness per turn |
| **Turn Contextual Relevancy** | Context relevance per assistant turn |

### 4.3 Agent-Specific Metrics

| Metric | What It Measures |
|--------|-----------------|
| **Task Completion** | Did the agent accomplish the given task? |
| **Tool Correctness** | Did the agent pick the right tools and call them? |
| **Argument Correctness** | Did the agent generate correct tool arguments? |
| **Plan Quality** | Is the plan complete, logical, and efficient? |
| **Plan Adherence** | Did the agent stick to its plan? |
| **Step Efficiency** | Did the agent avoid unnecessary steps? |
| **Trajectory Exact Match** | Does execution path match expected trajectory? |
| **Trajectory Precision** | What fraction of taken steps were correct? |
| **Trajectory Recall** | What fraction of required steps were taken? |
| **Progress Rate** | How far did the agent advance toward the goal? |
| **Step Success Rate** | Percentage of plan steps successfully executed |
| **Tool Selection Accuracy** | Correct tool chosen for each situation |
| **Tool Parameter Accuracy** | Correct contextual information in tool calls |
| **Tool Sequencing** | Correct ordering (diagnostic-before-action) |
| **Error Recovery Rate** | Success rate of corrective actions after failures |

### 4.4 Foundational Quality Metrics

| Metric | What It Measures |
|--------|-----------------|
| **Hallucination** | Contains fabricated information? |
| **Toxicity** | Offensive, harmful, or inappropriate language? |
| **Bias** | Racial, gender, or political bias present? |
| **Helpfulness** | Is the output useful to the user? |
| **Prompt Alignment** | Does output follow instructions? |
| **Coherence** | Logical flow and consistency within text |
| **Fluency** | Grammatical correctness and naturalness |
| **Conciseness** | Adherence to length/verbosity targets |
| **Coverage** | Content completeness (0-3 ordinal) |

### 4.5 Statistical / Legacy Scorers

| Scorer | Method |
|--------|--------|
| **BLEU** | n-gram precision (bilingual evaluation understudy) |
| **ROUGE** | n-gram recall (summarization focus) |
| **METEOR** | Precision + recall with word-order adjustment |
| **Levenshtein Distance** | Minimum character edits |
| **BERTScore** | Cosine similarity of contextual embeddings |
| **MoverScore** | Earth Mover's Distance on word distributions |
| **BLEURT** | Pre-trained transformer scoring |
| **NLI** | Natural Language Inference (entailment/contradiction) |

### 4.6 LLM-Based Scorers

| Scorer | Method |
|--------|--------|
| **G-Eval** | Chain-of-thought evaluation steps via LLM |
| **DAG** (Deep Acyclic Graph) | Decision tree where each node is an LLM judgment |
| **Prometheus** | Open-source rubric-conditioned LLM evaluator |
| **QAG Score** | Question-Answer Generation via confined close-ended questions |
| **GPTScore** | Conditional probability of generating target text |
| **SelfCheckGPT** | Sampling-based self-consistency for hallucination detection |

---

## 5. Enterprise Evaluation Frameworks

### 5.1 CLASSic Framework (ICLR 2025 Workshop)

| Dimension | Sub-Metrics | Raw Metric Type |
|-----------|-------------|-----------------|
| **Cost (C)** | Cost per task, infrastructure costs, token consumption, scaling costs | USD or token count |
| **Latency (L)** | Time to first response, planning latency, execution latency, throughput | ms or tasks/sec |
| **Accuracy (A)** | Task completion rate, step-level accuracy, precision/recall, reflection accuracy | 0.0-1.0 |
| **Security (S)** | Threat detection rate, session security, tool/data security, model integrity, policy compliance | 0.0-1.0 |
| **Stability (S)** | Response consistency, error rates, cross-task consistency, dynamic workload performance | 0.0-1.0 |

**CLASSic Composite Score**

Each dimension is min-max normalized to [0, 1] before aggregation. Latency and Cost are inverted (lower is better):

```
C_norm = 1 - (C_raw - C_min) / (C_max - C_min)        # invert: lower cost = better
L_norm = 1 - (L_raw - L_min) / (L_max - L_min)        # invert: lower latency = better
A_norm = (A_raw - A_min) / (A_max - A_min)             # higher accuracy = better
S_sec_norm = (S_sec_raw - S_min) / (S_max - S_min)     # higher security = better
S_stab_norm = (S_stab_raw - S_min) / (S_max - S_min)  # higher stability = better

CLASSic = w_C*C_norm + w_L*L_norm + w_A*A_norm + w_S*S_sec_norm + w_Stab*S_stab_norm
```

Recommended enterprise weights (typical production deployment):
- w_A = 0.40 (accuracy dominates for task-based agents)
- w_S = 0.25 (security elevated for enterprise)
- w_Stab = 0.20 (stability for SLA compliance)
- w_C = 0.08 (cost secondary when accuracy is paramount)
- w_L = 0.07 (latency secondary for async tasks)

Agentic use case adjustments: real-time customer support -> swap A/L weights; batch analytics -> lower w_L.

### 5.2 CLEAR Framework (arxiv 2511.14136)

| Dimension | Key Metric | Formula |
|-----------|-----------|---------|
| **Cost (C)** | Cost-Normalized Accuracy (CNA) | CNA = (Accuracy / TotalCost) * 100 |
| **Latency (L)** | SLA Compliance Rate (SCR) | SCR = count(tasks <= threshold) / total_tasks |
| **Efficacy (E)** | Domain-specific accuracy | E = correct_tasks / total_tasks (domain-specific) |
| **Assurance (A)** | Policy Adherence Score (PAS) | PAS = 1 - (policy_violations / total_policy_critical_actions) |
| **Reliability (R)** | Pass@k | Pass@k = 1 - (1 - p)^k where p = per-attempt success probability |

**SLA Thresholds by domain** (CLEAR paper defaults):
- Customer support: <= 3 seconds
- Code generation: <= 30 seconds
- Data analysis: <= 120 seconds
- Batch processing: <= 600 seconds

**Pass@k Targets**:
- Pass@1 >= 0.90: standard production gate
- Pass@8 >= 0.80: mission-critical (nuclear, medical, financial)
- Pass@3 >= 0.95: developer tooling

**CLEAR Composite Formula**

```
CLEAR = w_C * normalize(C) + w_L * normalize(L) + w_E * E + w_A * A + w_R * R
```

Default weights: 0.20 each (equal weighting = no domain assumption).
Normalization per dimension: min-max over evaluation set. Cost and Latency inverted (lower is better).

**Validated empirical findings** (300 enterprise tasks, 6 agents, N=15 expert judges):

| Finding | Metric | Value |
|---------|--------|-------|
| Cost gap from accuracy-only optimization | CNA ratio vs cost-aware agents | 4.4x -- 10.8x more expensive |
| Reliability drop: single run vs 8-run | pass@1 vs pass@8 | 60% -> 25% (35pp gap) |
| CLEAR vs accuracy-only production predictor | Spearman rho | CLEAR: 0.83 vs accuracy-only: 0.41 |
| 50x cost variation | CNA range across agents at similar accuracy | Confirmed |

**Key insight**: An agent with 70% accuracy but optimized for cost delivers better business value
(higher CNA) than an 80% accuracy agent with 10x cost, in most enterprise use cases.

**CLEAR vs CLASSic Comparison**

| Aspect | CLASSic | CLEAR |
|--------|---------|-------|
| Primary focus | Production operations | Enterprise deployment readiness |
| Security handling | Explicit dimension (S) | Embedded in Assurance (A) |
| Reliability | Part of Stability | Explicit dimension (R) via Pass@k |
| Cost metric | Raw cost score | CNA (normalized by accuracy) |
| Latency metric | Raw latency | SCR (SLA compliance binary) |
| Weight default | Unequal (A=0.40) | Equal (0.20 each) |
| Best for | Operating deployed agents | Selecting/certifying new agents |

### 5.3 Four-Pillar Agent Assessment (arxiv 2512.12791)

| Pillar | Dimensions |
|--------|-----------|
| **LLM** | Instruction following, policy adherence, sequence correctness, safety alignment |
| **Memory** | Storage correctness, retrieval (single-hop, multi-hop, temporal, open-domain), update latency |
| **Tools** | Selection accuracy, parameter mapping, tool sequencing, error interpretation, reliability |
| **Environment** | Workflow execution, configurability, guardrails, security enforcement |

**Three evaluation layers**: Static analysis -> Dynamic execution -> Judge-based assessment

---

## 6. Agent-Specific Evaluation Dimensions

### 6.1 Multi-Level Assessment

| Level | What Is Measured |
|-------|-----------------|
| **Session-Level** | Task success, trajectory quality, goal achievement |
| **Node-Level** | Tool selection, parameter correctness, step utility |
| **System-Level** | Latency, cost, throughput, scalability |

### 6.2 Temporal Evaluation Contexts

| Context | When |
|---------|------|
| **Pre-deployment** | Edge case testing, stress testing, adversarial testing |
| **Production monitoring** | Drift detection, failure pattern tracking |
| **Commit-triggered** | Code changes, prompt modifications |
| **Schedule-triggered** | Daily/weekly drift detection |
| **Event-triggered** | Deployment, telemetry anomalies, user feedback |

### 6.3 Evaluation Portfolio Strategy

Optimal coverage requires 2-4 complementary benchmarks:

| Role | Example Benchmark |
|------|-------------------|
| **Baseline multi-environment** | AgentBench (8 environments) |
| **Domain-specific primary** | SWE-bench (coding), WebArena (web) |
| **Safety & adversarial** | FORTRESS, ST-WebAgentBench |
| **Frontier reasoning** | GAIA, HLE |

---

## 7. Judge Training & Optimization

### 7.1 Training Objectives by Paradigm

| Paradigm | Loss Functions |
|----------|---------------|
| **Pointwise** | Binary Cross-Entropy, MSE, Ordinal Cross-Entropy |
| **Pairwise** | Logistic Loss, RankNet, -log sigma(s_i - s_j) |
| **Listwise** | ListMLE, LambdaRank, Softmax Cross-Entropy, Position-Weighted |

### 7.2 Judge Selection Decision Tree

```
Need absolute quality score?
  YES -> Pointwise
    Need higher reliability?
      YES -> Pointwise + multi-judge panel
      NO  -> Single pointwise judge
  NO  -> Need relative preference?
    YES -> Pairwise (higher agreement than pointwise)
    NO  -> Need global ranking?
      YES -> Listwise (NDCG optimization)
      NO  -> Start with pointwise, escalate as needed
```

### 7.3 Escalation Strategy (cost/accuracy ascending)

1. Pointwise evaluation alone
2. Pointwise + judge panels (majority vote)
3. Pairwise evaluation
4. Multimodal judges (pointwise or pairwise)
5. Listwise evaluation
6. Reinforcement-learned judges (GRPO-based)
7. Human validation layer

### 7.4 Mitigation Strategies Summary

| Strategy | Addresses |
|----------|----------|
| **Automatic Prompt Optimization (APO)** | Prompt sensitivity, rubric drift |
| **Panel/Jury** (multi-judge) | Individual bias, variance |
| **Position randomization** | Position bias |
| **Anonymization** | Self-preference bias |
| **Evidence-anchored scoring** | Over-confidence, hallucination blindness |
| **Schema-constrained output** | Format inconsistency |
| **Causal Judge Evaluation (CJE)** | Calibration drift |
| **Sample-based human audit** | Coverage gaps, factuality gaps |

---

## 8. CEX Kind Mapping

### 8.1 Direct Kind Mappings

| Industry Concept | CEX Kind | Pillar | Boundary |
|------------------|----------|--------|----------|
| Performance benchmark (latency, cost, quality) | `benchmark` | P07 | Quantitative measurement. NOT eval (no correctness) nor scoring_rubric (no criteria) |
| Evaluation criteria framework (5D, 12LP, custom) | `scoring_rubric` | P07 | Criteria with framework. NOT benchmark (no measurement) nor quality_gate (no blocking) |
| LLM-as-a-Judge configuration | `llm_judge` | P07 | LLM evaluator config. NOT scoring_rubric (different scope) |
| Pass/fail quality barrier with numeric score | `quality_gate` | P11 | Numeric threshold barrier. NOT validator (technical) nor scoring_rubric (criteria only) |
| Reference test case (quality 9.5+) | `golden_test` | P07 | Reference case. NOT few_shot_example (illustrates) nor unit_eval (any quality) |

### 8.2 Taxonomy-to-Kind Mapping for New Artifacts

| Evaluation Need | Recommended Kind | Naming Pattern |
|-----------------|-----------------|----------------|
| HELM-style holistic benchmark | `benchmark` | p07_bm_helm_{scenario}.md |
| Agent trajectory evaluation | `benchmark` | p07_bm_trajectory_{domain}.md |
| Analytic rubric (per-criterion) | `scoring_rubric` | p07_sr_analytic_{domain}.md |
| Holistic rubric (single score) | `scoring_rubric` | p07_sr_holistic_{domain}.md |
| AutoRubric-style mixed criteria | `scoring_rubric` | p07_sr_autorubric_{domain}.md |
| Pointwise judge config | `llm_judge` | p07_judge_pointwise_{name}.md |
| Pairwise judge config | `llm_judge` | p07_judge_pairwise_{name}.md |
| Panel/jury config | `llm_judge` | p07_judge_panel_{name}.md |
| CLASSic/CLEAR enterprise eval | `benchmark` | p07_bm_enterprise_{framework}.md |
| Artifact quality threshold | `quality_gate` | p11_qg_{gate}.yaml |
| Reference artifact for calibration | `golden_test` | p07_gt_{case}.md |
| RAG faithfulness checker | `llm_judge` | p07_judge_faithfulness.md |
| Safety/toxicity scanner | `llm_judge` | p07_judge_safety.md |

### 8.3 CEX 5D Scoring Mapped to Industry

| CEX Dimension | Industry Equivalent | AutoRubric Criterion Type |
|---------------|--------------------|-----------------------------|
| D1 Structural completeness | Coverage metric | Binary (required sections present?) |
| D2 Schema conformance | Prompt alignment | Binary (frontmatter valid?) |
| D3 Information density | Conciseness + coverage | Ordinal (density score 0-1) |
| D4 Domain accuracy | Faithfulness + groundedness | Binary per claim |
| D5 Actionability | Helpfulness | Ordinal (actionable/informative/vague) |

### 8.4 CEX 3-Layer Scoring Mapped to Industry

| CEX Layer | Weight | Industry Parallel |
|-----------|--------|-------------------|
| L1 Structural | 30% | Automated rule-based checks (like BLEU/ROUGE) |
| L2 Rubric | 30% | Analytic rubric scoring (like AutoRubric per-criterion) |
| L3 Semantic | 40% | LLM-as-a-Judge pointwise evaluation (like G-Eval) |

---

## 9. Glossary -- Complete Evaluation Vocabulary

| Term | Definition | Category |
|------|-----------|----------|
| **Accuracy** | Correctness of output vs ground truth | Metric |
| **Analytic rubric** | Multi-criterion rubric with independent scoring per dimension | Rubric type |
| **Answer relevancy** | Whether output addresses the input concisely | RAG metric |
| **APO** (Automatic Prompt Optimization) | Data-driven prompt refinement for judges | Mitigation |
| **Arbiter** | Judge role: decides preference between alternatives | Judge role |
| **Benchmark** | Standardized test suite for quantitative performance measurement | Evaluation type |
| **BERTScore** | Cosine similarity of contextual BERT embeddings | Statistical scorer |
| **Bias** | Systematic skew in outputs (racial, gender, political) | Safety metric |
| **Binary criterion** | MET/UNMET verdict on a single dimension | Criterion type |
| **Calibration** | Alignment of model confidence with actual performance | HELM metric |
| **Central tendency bias** | Judge avoids extreme scores on broad scales | Bias type |
| **CLEAR** | Cost-Latency-Efficacy-Assurance-Reliability framework | Enterprise framework |
| **CLASSic** | Cost-Latency-Accuracy-Security-Stability framework | Enterprise framework |
| **CNA** (Cost-Normalized Accuracy) | Accuracy / Cost x 100 | Enterprise metric |
| **Coherence** | Logical flow and consistency within text | Quality metric |
| **Contextual precision** | Whether relevant retrieval nodes rank higher | RAG metric |
| **Contextual recall** | Proportion of expected output from context | RAG metric |
| **Critic** | Judge role: identifies flaws and suggests improvements | Judge role |
| **Cross-encoder** | Architecture encoding query + output jointly | Judge architecture |
| **Domain expert** | Judge role: specialized evaluation in narrow field | Judge role |
| **Efficacy** | Task completion quality (domain-specific) | CLEAR dimension |
| **Evaluator** | Judge role: assesses task completion and correctness | Judge role |
| **Evidence-anchored scoring** | Grounding evaluations in verifiable proof | Mitigation |
| **Faithfulness** | Output factually aligns with retrieval context | RAG metric |
| **Fluency** | Grammatical correctness and naturalness | Quality metric |
| **G-Eval** | CoT-based LLM evaluation method | LLM scorer |
| **Golden test** | Reference test case at quality 9.5+ for calibration | CEX kind |
| **Grader** | Judge role: assigns scores against a rubric | Judge role |
| **Groundedness** | Answer supported by retrieved documents (= faithfulness) | RAG metric |
| **Halo effect** | One good criterion inflates scores on others | Bias type |
| **Hallucination** | Fabricated information not supported by sources | Safety metric |
| **Holistic rubric** | Single overall score for entire output | Rubric type |
| **LLM-as-a-Judge** | Using an LLM to evaluate other LLM outputs | Evaluation paradigm |
| **Length bias** | Judge preference for longer outputs | Bias type |
| **Likert scale** | Ordered numeric rating (1-5, 0-10) | Scoring type |
| **Listwise** | Judge paradigm: ranks entire candidate set jointly | Judge paradigm |
| **Negative weight** | Rubric penalty for anti-patterns | Rubric component |
| **Nominal criterion** | Unordered categorical classification | Criterion type |
| **Ordinal criterion** | Ranked/ordered scale levels | Criterion type |
| **PAS** (Policy Adherence Score) | 1 - (violations / total policy-critical actions) | Enterprise metric |
| **Pairwise** | Judge paradigm: relative preference between two outputs | Judge paradigm |
| **Pass@k** | Probability of k consecutive successes | Reliability metric |
| **Plan adherence** | Whether agent stuck to its created plan | Agent metric |
| **Plan quality** | Completeness, logic, and efficiency of agent plans | Agent metric |
| **Pointwise** | Judge paradigm: independent absolute scoring | Judge paradigm |
| **Position bias** | Preference for first/last position in comparisons | Bias type |
| **Progress rate** | How far agent advanced toward goal vs expected trajectory | Agent metric |
| **Prompt alignment** | Whether output follows given instructions | Quality metric |
| **Prometheus** | Open-source rubric-conditioned LLM evaluator | LLM scorer |
| **Quality gate** | Pass/fail barrier with numeric score threshold | CEX kind |
| **Reward hacking** | Outputs optimized to fool judge, not solve task | Failure mode |
| **Robustness** | Performance stability under input perturbation | HELM metric |
| **Safety assessor** | Judge role: checks for harmful/toxic/biased content | Judge role |
| **Scoring rubric** | Structured evaluation criteria with framework | CEX kind |
| **Self-preference bias** | Judge favors outputs from its own model family | Bias type |
| **SLA Compliance Rate** | Percentage of tasks completed within time threshold | Enterprise metric |
| **Step efficiency** | Whether agent avoided unnecessary steps | Agent metric |
| **Task completion** | Whether agent accomplished the given task | Agent metric |
| **Tool correctness** | Whether agent picked and called the right tools | Agent metric |
| **Toxicity** | Offensive, harmful, or inappropriate language in output | Safety metric |
| **Trajectory** | Sequence of reasoning steps and actions taken by an agent | Agent concept |
| **Trajectory precision** | Fraction of taken steps that were correct | Agent metric |
| **Trajectory recall** | Fraction of required steps that were taken | Agent metric |
| **Verifier** | Judge role: binary pass/fail against ground truth | Judge role |
| **Verdict-balanced few-shot** | Calibration with examples showing correct verdicts | Calibration technique |

---

## 10. Key Findings & Implications for CEX

1. **Analytic > Holistic for improvement**: CEX's 5D scoring (L2 rubric layer) aligns with
   AutoRubric's analytic approach -- per-criterion decomposition enables targeted artifact
   improvement via cex_evolve.py.

2. **Three-layer scoring is industry-aligned**: CEX's L1 structural (30%) + L2 rubric (30%) +
   L3 semantic (40%) maps directly to the evaluation industry's progression from rule-based
   to LLM-judged scoring.

3. **Agent metrics are the frontier**: As CEX evolves toward multi-agent orchestration (N07 grid),
   trajectory metrics (precision, recall, progress rate) and tool correctness become relevant
   for evaluating nucleus dispatch quality.

4. **Enterprise frameworks validate CEX concerns**: CLASSic and CLEAR both include cost and
   latency as first-class evaluation dimensions -- relevant for CEX's token budget management
   (cex_token_budget.py) and multi-provider routing (cex_router.py).

5. **Judge bias mitigation applies to cex_score.py**: Position bias, length bias, and
   self-preference bias documented in the LLM-as-a-Judge literature should inform how
   CEX configures its L3 semantic scoring layer.

6. **Golden tests map to calibration**: CEX's golden_test kind (quality 9.5+) serves the same
   role as AutoRubric's "anchored examples per score level" -- reference artifacts for
   judge calibration.

---

## 11. Benchmark-to-CEX Quality Gate Dimension Mapping

Maps 40+ benchmarks to which CEX quality gate dimensions (D1-D5) they primarily exercise.
Use this table when selecting benchmarks for a CEX evaluation pipeline.

| Benchmark | D1 Structural | D2 Schema | D3 Density | D4 Domain Accuracy | D5 Actionability | Primary Use |
|-----------|--------------|-----------|------------|-------------------|------------------|-------------|
| **HELM** | partial | no | no | YES | no | Holistic LLM quality |
| **MMLU** | no | no | no | YES | no | Domain knowledge coverage |
| **LiveBench** | no | no | no | YES | no | Anti-contamination accuracy |
| **HLE** | no | no | no | YES | no | Frontier model capability |
| **SimpleQA** | no | no | no | YES | no | Factual precision |
| **FACTS Grounding** | no | no | YES | YES | no | RAG faithfulness |
| **BFCL** | no | no | no | YES | YES | Tool use correctness |
| **ToolBench** | no | YES | no | YES | YES | API mastery |
| **ComplexFuncBench** | no | YES | no | YES | YES | Multi-step tool calling |
| **Tau-Bench** | no | no | no | YES | YES | Policy adherence in tools |
| **API-Bank** | no | YES | no | YES | YES | API planning |
| **HammerBench** | no | no | no | YES | YES | Multi-turn tool use |
| **LiveMCPBench** | no | YES | no | YES | YES | MCP server navigation |
| **MCP-Universe** | no | YES | no | YES | YES | Real MCP interaction |
| **GAIA** | no | no | YES | YES | YES | Multi-step reasoning |
| **AgentBench** | no | no | YES | YES | YES | Multi-environment agents |
| **AssistantBench** | no | no | YES | YES | YES | Web task completion |
| **FORTRESS** | no | no | no | YES | no | Safety robustness |
| **MASK** | no | no | no | YES | no | Truthfulness under pressure |
| **SWE-bench** | YES | no | YES | YES | YES | Code task completion |
| **SWE-bench Verified** | YES | no | YES | YES | YES | Expert-validated code |
| **SWE-bench Pro** | YES | no | YES | YES | YES | Professional-grade code |
| **SWE-PolyBench** | YES | no | YES | YES | YES | Multi-language code |
| **LiveCodeBench** | YES | no | no | YES | YES | Fresh code problems |
| **Aider Polyglot** | YES | no | YES | YES | YES | Code editing/self-correction |
| **WebArena** | no | no | YES | YES | YES | Web automation |
| **VisualWebArena** | no | no | YES | YES | YES | Multimodal web tasks |
| **WebVoyager** | no | no | YES | YES | YES | Real-world web navigation |
| **BrowseComp** | no | no | YES | YES | YES | Persistent browsing research |
| **Mind2Web** | no | no | YES | YES | YES | Open-domain web tasks |
| **OSWorld** | YES | no | YES | YES | YES | Full OS task execution |
| **ST-WebAgentBench** | no | no | no | YES | no | Web agent safety/trust |
| **NaturalQuestions** | no | no | no | YES | no | Open-domain QA |
| **TriviaQA** | no | no | no | YES | no | Factual recall |
| **HellaSwag** | no | no | no | YES | no | Commonsense completion |
| **MS MARCO** | no | no | YES | YES | no | Retrieval precision |
| **CNN/DailyMail** | YES | no | YES | YES | no | Summarization fidelity |
| **RealToxicityPrompts** | no | no | no | no | no | Toxicity generation risk |
| **CivilComments** | no | no | no | YES | no | Toxic content classification |
| **RAFT** | YES | YES | YES | YES | YES | Few-shot task format |

**Legend**:
- D1 Structural: tests output format/structure correctness
- D2 Schema: tests schema/contract conformance
- D3 Density: tests information completeness and conciseness
- D4 Domain Accuracy: tests factual/functional correctness
- D5 Actionability: tests whether output enables real action

**Benchmark selection heuristic for CEX artifact evaluation:**
- All 5 dimensions needed: SWE-bench + GAIA (covers code, reasoning, tool use)
- D4+D5 only: BFCL + Tau-Bench (tool correctness + policy adherence)
- D1+D2+D4 only: RAFT + ToolBench (structure + schema + accuracy)
- Safety focus: FORTRESS + MASK + RealToxicityPrompts

---

## 12. Evaluation Strategy Decision Tree

Use this tree to select the correct evaluation approach for any CEX context.

```
STEP 1: What is the primary output type?
|
+-- Structured artifact (YAML/MD with schema)?
|     -> Use: L1 Structural (automated rule-checks) + L2 Rubric (5D)
|     -> Then: L3 LLM-Judge only if L1+L2 >= 8.5
|
+-- Natural language generation (copy, docs, summaries)?
|     -> Use: G-Eval (CoT LLM judge) + ROUGE/BERTScore for coverage
|     -> Then: Pairwise for A/B comparison if multiple variants
|
+-- Code / executable artifact?
|     -> Use: Functional tests (pass/fail) as primary gate
|     -> Then: SWE-bench-style trajectory eval for agent code
|     -> Then: Static analysis (L1) for format compliance
|
+-- Agent trajectory / multi-step task?
|     -> Use: Trajectory precision + recall + task completion
|     -> Then: Tool correctness + argument correctness
|     -> Then: Step efficiency (unnecessary step detection)
|
+-- RAG pipeline output?
      -> Use: Faithfulness + Answer Relevancy + Contextual Precision
      -> Then: Groundedness check (NLI-based or LLM judge)
      -> Then: Multi-turn metrics if conversational

STEP 2: What is the evaluation budget?
|
+-- Low (< $0.10/artifact)?
|     -> Use: Automated rule-checks (L1) + lightweight pointwise judge (haiku-level)
|     -> Avoid: Multi-judge panels, listwise, pairwise at scale
|
+-- Medium ($0.10-$1.00/artifact)?
|     -> Use: L1 + L2 + single sonnet-level pointwise judge (L3)
|     -> Consider: 3-judge panel for high-stakes artifacts
|
+-- High (> $1.00/artifact)?
      -> Use: Full 3-layer (L1+L2+L3) + multi-judge panel (3-5 judges)
      -> Include: Pairwise comparison against golden_test reference
      -> Include: Human validation sample (5-10%)

STEP 3: What is the deployment stage?
|
+-- Pre-deployment (development)?
|     -> Priority: Analytic rubric (identify specific improvement targets)
|     -> Trigger: Commit-triggered CI gate
|     -> Threshold: 8.0 floor (iterate below)
|
+-- Pre-release (staging)?
|     -> Priority: End-to-end eval + adversarial testing
|     -> Trigger: Manual + schedule (daily)
|     -> Threshold: 9.0 target, 8.5 hard floor
|
+-- Production (monitoring)?
      -> Priority: Drift detection (quality trend over time)
      -> Trigger: Event-triggered + scheduled (weekly baseline)
      -> Threshold: Alert if rolling avg drops > 0.3 below baseline

STEP 4: Safety requirements?
|
+-- None (internal tooling)?
|     -> Skip safety dimension from CLASSic/CLEAR
|
+-- Standard (customer-facing)?
|     -> Add: toxicity + bias + hallucination checks to rubric
|     -> Use: Safety assessor judge role (separate LLM call)
|
+-- High (medical/legal/financial)?
      -> Use: FORTRESS-style adversarial + MASK truthfulness
      -> Use: Conservative ensemble (min score wins)
      -> Require: Human audit of 10%+ sample
      -> Gate: PAS >= 0.99 before deploy

STEP 5: Judge type selection?
|
+-- Need absolute quality score? -> Pointwise
|     +-- High reliability needed? -> Multi-judge panel (majority vote)
|     +-- Standard? -> Single judge with calibrated rubric
|
+-- Need relative preference? -> Pairwise (higher inter-rater agreement)
|
+-- Need global ranking? -> Listwise (NDCG optimization)
|
+-- Need training signal? -> Pairwise (RLHF-compatible) or Listwise (LambdaRank)
```

**CEX Artifact Pipeline Recommendation** (implements above tree for standard artifacts):
1. L1 Structural check (automated, free)
2. L2 5D Rubric score (analytic, medium cost)
3. If L1+L2 >= 8.5: L3 LLM judge (pointwise, haiku-level)
4. If L3 score < 8.0: flag for cex_evolve.py improvement loop
5. Golden test comparison if kind has reference artifact

---

## 13. 2026 Research Updates

New papers and findings from Q1-Q2 2026 relevant to evaluation taxonomy.

### 13.1 AutoRubric (March 2026) -- New in This Update

Source: [AutoRubric: Unifying Rubric-based LLM Evaluation](https://arxiv.org/abs/2603.00077)

Key findings not covered in earlier versions:
- Binary criteria (kappa=0.642) significantly outperform ordinal in inter-rater reliability
- Reasoning chains in few-shot examples INCREASE hallucination 12% vs verdict-only examples
- CANNOT_ASSESS verdict handles 8.3% of real-world evaluation cases; ignoring these inflates scores by 0.7-1.2 points
- Penalty weights (negative w_i) reduce leniency bias by 23% in tested rubrics
- Auto-generated criteria match human-designed criteria at 81% overlap when task description is detailed

### 13.2 SWE-bench Pro (2026)

Source: SWE-bench Pro leaderboard (https://www.swebench.com/)

- 1,865 problems across 41 professional repositories (vs 500 in Verified)
- Hidden test set prevents contamination
- Claude 3.7 Sonnet: 62.3% resolution rate
- Key insight: professional repos require multi-file reasoning -- single-file patch agents fail at 2x rate

### 13.3 LiveMCPBench (2026)

Source: [LiveMCPBench](https://github.com/LiveMCPBench/LiveMCPBench)

- First benchmark evaluating real MCP server navigation at scale
- Measures: server discovery, tool selection, parameter construction, multi-server chaining
- Critical gap vs ToolBench: LiveMCPBench uses LIVE servers (no mocking) -- failure modes differ
- Top agents reach 71% on mock-based benchmarks but only 43% on live servers

### 13.4 BrowseComp (2026, OpenAI)

Source: [BrowseComp](https://openai.com/index/browsecomp/)

- 1,266 questions requiring persistent browsing to find hard-to-find information
- Human baseline: 78.5% (with browsing tools); LLM-only baseline: 3.1%
- Tests: multi-hop web reasoning, synthesis across sources, temporal tracking
- Distinguishes: agents that CAN browse vs agents that can REASON about browsed content

### 13.5 FRAMES for Factual Grounding (2025-2026)

Source: [FRAMES: Factuality, Retrieval, And Reasoning Evaluation for Multi-step Scenarios](https://arxiv.org/abs/2409.12941)

- 824 question-answer pairs requiring multi-hop retrieval + synthesis
- Measures: retrieval precision, reasoning chain validity, final answer faithfulness
- Key metric: End-to-end faithfulness (not just retrieval quality)
- CEX relevance: maps to D4 Domain Accuracy + RAG faithfulness in evaluation pipeline

### 13.6 Survey: Evaluation of LLM-based Agents (arxiv 2503.16416, March 2026)

First comprehensive survey of evaluation methodologies for LLM agents. Key taxonomy:

**4-Dimensional Taxonomy** (what to evaluate x how to evaluate):

| Dimension | Sub-components |
|-----------|---------------|
| **Fundamental capabilities** | Planning, tool use, self-reflection, memory |
| **Application-specific** | Web agents, SWE agents, scientific agents, conversational agents |
| **Generalist agents** | Agents spanning multiple domains |
| **Evaluation frameworks** | Infrastructure, tooling, dataset construction |

Critical gaps identified by the survey:
1. Cost-efficiency evaluation largely absent from existing benchmarks
2. Safety and robustness assessment inconsistent across frameworks
3. Benchmarks favor static tasks; production deployments are dynamic

### 13.7 Survey: Evaluation and Benchmarking of LLM Agents (arxiv 2507.21504, KDD 2026)

**2-Dimensional Taxonomy** (objectives x process):

| Axis | Elements |
|------|---------|
| **Objectives (What)** | Agent behavior, capabilities, reliability, safety |
| **Process (How)** | Interaction modes, datasets/benchmarks, metric computation, tooling |

Active benchmark categories covered: Coding/SWE (SWE-bench, ScienceAgentBench, CORE-Bench,
PaperBench, AppWorld), Web/Computer (BrowserGym, WebArena, WebCanvas, VisualWebArena, MMInA,
AssistantBench), Multi-environment (AgentBench, GAIA, OSWorld).

**Key trend**: Shift from static fixed tasks to continuously updated contamination-resistant benchmarks.
Contamination occurs within 6 months for most fixed benchmarks -- rolling releases are required.

### 13.8 DeepResearchEval (arxiv 2601.09688, January 2026)

Automated framework for evaluating long-form deep research reports (not QA pairs):

| Component | Description |
|-----------|-------------|
| **Page-as-unit paradigm** | Page is the basic evaluation unit; detects local failures per page |
| **Adaptive scoring** | Per-page logical quality assessment via LLM judge |
| **Paged-RAG mechanism** | Retrieval-augmented fact verification against configurable reference DB |
| **Reference DB** | Constructible from any document corpus; verifies claims against sources |

**Cost**: ~433 seconds per full-length deep research report (Qwen-Plus API), suitable for offline batch eval.

**CEX mapping**: Applicable to N01 research atom quality assessment when atoms exceed 5K bytes.
For CEX's 32-atom Atlas: budget ~4 hours for full DeepResearchEval sweep.

### 13.10 Evaluation Anti-Patterns Found in 2026 Studies

| Anti-Pattern | Discovered In | Effect | Mitigation |
|--------------|--------------|--------|------------|
| Reasoning-chain few-shot | AutoRubric 2026 | +12% hallucination | Use verdict-only examples |
| Single-judge L3 eval | LLM-Judge survey | High variance (sigma=1.2 on 10pt scale) | 3-judge majority vote |
| Holistic-only rubric | HELM 2.0 analysis | Masks per-criterion failure | Add analytic subcriteria |
| Static benchmark reuse | LiveBench paper | Contamination within 6 months | Rolling benchmark refresh |
| Mock-server evaluation | LiveMCPBench | 28pp gap vs live servers | Require live server testing |
| CANNOT_ASSESS ignored | AutoRubric 2026 | +0.7-1.2 score inflation | Implement SKIP/ZERO/PARTIAL/FAIL policies |

---

## Sources

- [HELM: Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110) (Stanford CRFM)
- [LLM-as-a-Judge Survey](https://arxiv.org/abs/2411.15594)
- [AutoRubric: Unifying Rubric-based LLM Evaluation](https://arxiv.org/abs/2603.00077) (March 2026)
- [CLEAR Framework for Enterprise Agentic AI](https://arxiv.org/abs/2511.14136)
- [CLASSic: AI Agent Evaluation](https://aisera.com/blog/ai-agent-evaluation/) (ICLR 2025 Workshop)
- [Agent Benchmark Compendium](https://github.com/philschmid/ai-agent-benchmark-compendium) (50+ benchmarks)
- [Galileo Agent Evaluation Framework](https://galileo.ai/blog/agent-evaluation-framework-metrics-rubrics-benchmarks)
- [Beyond Task Completion Assessment](https://arxiv.org/abs/2512.12791)
- [LLM-as-a-Judge Primer](https://aman.ai/primers/ai/LLM-as-a-judge/)
- [Confident AI Evaluation Metrics Guide](https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation)
- [SWE-bench Pro Leaderboard](https://www.swebench.com/) (2026)
- [LiveMCPBench](https://github.com/LiveMCPBench/LiveMCPBench) (2026)
- [BrowseComp by OpenAI](https://openai.com/index/browsecomp/) (2026)
- [FRAMES: Factuality Retrieval Reasoning Eval](https://arxiv.org/abs/2409.12941) (2025)
- [LiveBench: Contamination-Free Evaluation](https://livebench.ai/) (2025-2026 rolling)
- [AutoRubric-R1V: Rubric-Based Generative Rewards for Faithful Multimodal Reasoning](https://arxiv.org/abs/2510.14738)
- [Survey on Evaluation of LLM-based Agents](https://arxiv.org/abs/2503.16416) (March 2026)
- [Evaluation and Benchmarking of LLM Agents: A Survey](https://arxiv.org/abs/2507.21504) (KDD 2026)
- [DeepResearchEval: Automated Framework for Deep Research Task Evaluation](https://arxiv.org/abs/2601.09688)
- [Demystifying Evals for AI Agents (Anthropic)](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [Best LLM Evaluation Tools for AI Agents 2026 (Confident AI)](https://www.confident-ai.com/knowledge-base/compare/best-llm-evaluation-tools-for-ai-agents)


---

## 14. AutoRubric Implementation Deep-Dive

*Implementation-level detail for integrating AutoRubric-style evaluation into CEX pipelines.*
*Source: arxiv 2603.00077 (March 2026)*

### 14.1 Full Pipeline Architecture

```
INPUTS
  task_description    -- what was the task asking for?
  expected_behavior   -- rubric seed or reference output
  generated_output    -- candidate response to evaluate
        |
        v
PHASE 1: CRITERION GENERATION
  Prompt: list N independent criteria, each with type/weight/penalty flag
  Optimal: 5-12 criteria; more than 15 degrades inter-rater agreement
        |
        v
PHASE 2: PER-CRITERION ATOMIC SCORING (parallelizable)
  Per criterion: verdict-balanced few-shot (3-5 examples, NO reasoning chains)
  Binary  -> {MET, UNMET, CANNOT_ASSESS}
  Ordinal -> {L1, L2, ..., LK}
  Nominal -> {CAT_A, CAT_B, ...}
        |
        v
PHASE 3: AGGREGATION
  Binary:  v_i = 1 if MET, 0 if UNMET, None if CANNOT_ASSESS
  Ordinal: v_i = (level_index - 1) / (K - 1)
  weighted_sum = sum(v_i * w_i for i where v_i is not None)
  denominator  = sum(w_i for i where w_i > 0)
  score = max(0.0, min(1.0, weighted_sum / denominator))
  Note: negative weights reduce score but do NOT reduce denominator
```

### 14.2 Key Formulas

**Weighted Composite Score**:
```
score = max(0.0, min(1.0,
    sum(v_i * w_i for i in criteria if v_i is not None)
    / sum(w_i for i in criteria if w_i > 0)
))
```

**CANNOT_ASSESS Disposition**:
```
SKIP:    exclude from numerator and denominator (optional criteria)
ZERO:    v_i = 0, keep in denominator (strict mode, high-stakes)
PARTIAL: v_i = 0.5, keep in denominator (exploratory mode)
FAIL:    abort, escalate to human (safety-critical pipelines)
```

**Inter-Rater Reliability**:
```
# Cohen's Kappa (binary/nominal)
kappa = (P_observed - P_expected) / (1 - P_expected)

# Quadratic-Weighted Kappa (ordinal)
kappa_qw = 1 - sum(W_ij * O_ij) / sum(W_ij * E_ij)
W_ij = (i - j)^2 / (N_levels - 1)^2
```

**Pass@k Unbiased Estimator**:
```
pass_at_k = 1 - product((n-c-i)/(n-i) for i in range(k))
where n = total samples, c = correct samples, k = budget
```

### 14.3 Reliability by Criterion Type vs Alternatives

| Criterion Type | AutoRubric Accuracy | AutoRubric Kappa | vs G-Eval holistic | vs Prometheus 2 |
|---------------|--------------------|-----------------|--------------------|-----------------|
| Binary | 87% | 0.642 | +14pp, +0.18 kappa | Comparable on structured tasks |
| Ordinal (3-level) | 79% | 0.549 | +6pp | Prometheus wins on open-ended |
| Ordinal (5-level) | 74% | 0.571 | +1pp | Comparable |
| Nominal | 81% overall | asymmetric | +8pp macro avg | Varies by category |

**Key finding**: Binary criteria most reliable -- use for hard gates.
Reasoning-chain few-shot increases hallucination by 12% vs verdict-only.

### 14.4 Calibration Protocol

```
Step 1: Curate verdict-balanced examples
  - Binary: 1-2 MET + 1-2 UNMET + 0-1 CANNOT_ASSESS
  - Ordinal: 1 example per level (K examples total)
  - CRITICAL: NO reasoning chains (+12% hallucination if included)
  - Include: criterion text + evidence snippet + verdict only

Step 2: Validate calibration on 20+ held-out labeled items
  - Binary target: accuracy >= 80%, kappa >= 0.50
  - Ordinal target: quadratic kappa >= 0.55
  - If below: add examples or split into simpler sub-criteria

Step 3: Anchor to CEX reference artifacts
  - golden_test (quality 9.5+) = top-score anchor
  - quality_gate failing artifact = bottom-score anchor
```

### 14.5 AutoRubric-to-CEX Mapping

| AutoRubric Component | CEX Equivalent | Location |
|---------------------|---------------|----------|
| Criterion generation | scoring_rubric frontmatter | P07_evaluation/ |
| Per-criterion atomic eval | L2 Rubric in cex_score.py | _tools/cex_score.py |
| Weighted composite | L2 layer (30% weight) | scoring logic |
| CANNOT_ASSESS SKIP | density_score: null handling | artifact frontmatter |
| Verdict-balanced few-shot | golden_test kind (P07) | calibration artifacts |
| Multi-judge ensemble | llm_judge panel config | P07 judge configs |
| kappa / Cronbach alpha | NOT YET IN CEX | Gap: add --reliability flag |

---

## 15. CLASSic & CLEAR: Full Scoring Formulas

*Implementation-level formulas for enterprise agent evaluation.*

### 15.1 CLASSic Dimensional Formulas (ICLR 2025 Workshop)

**Cost (C)**: `C_score = max(0.0, 1.0 - (actual_cost_per_task / budget_cost_per_task))`

**Latency (L)**: `L_score = 1.0 - clip((actual_latency - sla_latency) / sla_latency, 0.0, 1.0)`
(1.0 if within SLA, 0.0 if 2x SLA or worse)

**Accuracy (A)**: `A_score = count(tasks_completed_correctly) / total_tasks`

**Security (S1)**: `S1_score = 1.0 - (security_incidents / total_interactions)` (target >= 0.99)

**Stability (S2)**:
```
cv = std(task_success_per_run) / mean(task_success_per_run)
S2_score = 1.0 - clip(cv, 0.0, 1.0)   # target >= 0.90 (< 10% CV)
```

**CLASSic Composite**:
```
CLASSic = w_C*C + w_L*L + w_A*A + w_S1*S1 + w_S2*S2

Default (equal):      0.2 each
Customer support:     C=0.2, L=0.3, A=0.2, S1=0.15, S2=0.15
Code/engineering:     C=0.1, L=0.1, A=0.5, S1=0.1,  S2=0.2
Financial/regulated:  C=0.1, L=0.1, A=0.3, S1=0.3,  S2=0.2

Production gate: CLASSic >= 0.85
```

### 15.2 CLEAR Dimensional Formulas (arxiv 2511.14136)

**Cost -- Cost-Normalized Accuracy (CNA)**:
```
CNA = (task_accuracy / cost_per_task) * 100
CNA_norm = clip(CNA / CNA_baseline / 2.0, 0.0, 1.0)
```

**Latency -- SLA Compliance Rate (SCR)**:
```
SCR = count(tasks_within_sla) / total_tasks

SLA thresholds: support=3s, code=30s, reasoning=120s, docs=300s, research=600s
```

**Assurance -- Policy Adherence Score (PAS)**:
```
PAS = 1.0 - (policy_violations / total_policy_critical_actions)
targets: regulated >= 0.99, standard >= 0.95
```

**Reliability -- Pass@k** (unbiased estimator):
```
pass_at_k = 1.0 - product((n-c-i)/(n-i) for i in range(k))

Targets: mission-critical pass@8 >= 0.80, standard pass@3 >= 0.70
```

**CLEAR Composite**:
```
CLEAR = 0.2*CNA_norm + 0.2*SCR + 0.2*E + 0.2*PAS + 0.2*pass_at_k

Enterprise gate: CLEAR >= 0.85 | Mission-critical: CLEAR >= 0.90
```

### 15.3 CLASSic vs CLEAR vs CEX 3-Layer

| Property | CLASSic | CLEAR | CEX 3-Layer |
|----------|---------|-------|-------------|
| Cost metric | Budget ratio | CNA (value-linked) | cex_token_budget.py |
| Latency | SLA deviation | SCR (% within SLA) | Router latency (indirect) |
| Quality | Task success rate | Domain accuracy (E) | L1+L2+L3 composite |
| Security | Explicit S1 | Embedded in PAS | Guardrail kinds (P11) |
| Reliability | CV-based stability | Pass@k probabilistic | quality_gate threshold |
| Composite target | >= 0.85 | >= 0.85 | >= 9.0 (10pt scale) |
| Best for | Security + regulated | ROI + reliability | Artifact quality workflow |

### 15.4 Practical Thresholds Reference Card

| Metric | Minimum | Production | Target | Golden |
|--------|---------|-----------|--------|--------|
| CLASSic composite | 0.70 | 0.80 | 0.85 | 0.95 |
| CLEAR composite | 0.70 | 0.80 | 0.85 | 0.90 |
| CNA vs baseline | 0.8x | 1.0x | 1.5x | 2.0x+ |
| PAS | 0.90 | 0.95 | 0.99 | 1.00 |
| pass@3 | 0.50 | 0.70 | 0.80 | 0.95 |
| pass@8 | 0.60 | 0.75 | 0.85 | 0.98 |
| Cohen kappa | 0.40 | 0.50 | 0.60 | 0.80 |
| CEX quality gate | 7.0 | 8.0 | 9.0 | 9.5 |

**CEX Integration Recommendations**:
- Use CLASSic for N07 nucleus dispatch evaluation (security + stability dimensions)
- Use CLEAR CNA to measure token efficiency per nucleus via cex_token_budget.py
- Use CLEAR pass@k as reliability gate in cex_evolve.py (pass@3 >= 0.70 before promoting artifact)
- Use CEX 3-layer for all artifact-level quality scoring (native, most granular)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_llm_evaluation_scenario]] | sibling | 0.27 |
| [[p03_sp_llm_evaluation_scenario_builder]] | downstream | 0.25 |
| [[llm-evaluation-scenario-builder]] | downstream | 0.25 |
| [[atom_19_agent_taxonomy_surveys]] | sibling | 0.24 |
| [[kc_llm_evaluation_scenario]] | sibling | 0.23 |
| [[benchmark-suite-builder]] | downstream | 0.23 |
| [[bld_knowledge_card_trajectory_eval]] | sibling | 0.23 |
| [[bld_collaboration_llm_judge]] | downstream | 0.22 |
| [[memory-benchmark-builder]] | downstream | 0.22 |
| [[kc_benchmark_suite]] | sibling | 0.22 |
