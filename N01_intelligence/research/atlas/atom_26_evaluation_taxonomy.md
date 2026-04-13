---
id: n01_atom_26_evaluation_taxonomy
kind: knowledge_card
type: research_atom
pillar: P01
title: "LLM Evaluation & Benchmark Taxonomy -- Complete Vocabulary Atlas"
version: 1.1.0
created: 2026-04-13
updated: 2026-04-13
author: n01_intelligence
domain: evaluation_benchmarks
quality: 8.9
tags: [evaluation, benchmarks, llm-judge, rubrics, metrics, scoring, agent-eval, quality-gate, HELM, SWE-bench, GAIA]
tldr: "Exhaustive taxonomy of LLM and agent evaluation: benchmark types, judge roles, rubric structures, metric categories, agent-specific dimensions, and enterprise frameworks -- mapped to CEX kinds"
when_to_use: "Designing evaluation pipelines, building scoring rubrics, configuring LLM judges, selecting benchmarks, creating quality gates for CEX artifacts"
keywords: [evaluation, benchmark, scoring-rubric, llm-judge, quality-gate, golden-test, HELM, CLASSic, CLEAR, AutoRubric, pointwise, pairwise, analytic-rubric, holistic-rubric, faithfulness, groundedness, trajectory]
density_score: null
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

### 3.6 AutoRubric Calibration Techniques

| Technique | Description |
|-----------|-------------|
| **Verdict-Balanced Few-Shot** | 3-5 examples with correct verdicts (no reasoning chains) |
| **Per-Criterion Atomic Evaluation** | Separate LLM call per criterion -- prevents conflation |
| **Multi-Judge Ensemble** | N judges x M criteria concurrent calls |
| **Option Shuffling** | Deterministic per-item seeds to counter position bias |
| **CANNOT_ASSESS Verdict** | Native abstention handling (SKIP/ZERO/PARTIAL/FAIL) |

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

| Dimension | Sub-Metrics |
|-----------|-------------|
| **Cost (C)** | Cost per task, infrastructure costs, token consumption, scaling costs |
| **Latency (L)** | Time to first response, planning latency, execution latency, throughput |
| **Accuracy (A)** | Task completion rate, step-level accuracy, precision/recall, reflection accuracy |
| **Security (S)** | Threat detection rate, session security, tool/data security, model integrity, policy compliance |
| **Stability (S)** | Response consistency, error rates, cross-task consistency, dynamic workload performance |

### 5.2 CLEAR Framework (arxiv 2511.14136)

| Dimension | Key Metric | Formula / Threshold |
|-----------|-----------|---------------------|
| **Cost (C)** | Cost-Normalized Accuracy (CNA) | Accuracy / Cost x 100 |
| **Latency (L)** | SLA Compliance Rate (SCR) | % tasks within time threshold (3s support, 30s code) |
| **Efficacy (E)** | Domain-specific accuracy | Functional correctness varies by use case |
| **Assurance (A)** | Policy Adherence Score (PAS) | 1 - (violations / total policy-critical actions) |
| **Reliability (R)** | Pass@k | Probability of k consecutive successes (pass@8 >= 80% for mission-critical) |

**Composite**: CLEAR = wC*Cnorm + wL*Lnorm + wE*E + wA*A + wR*R (default 0.2 each)

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

## Sources

- [HELM: Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110) (Stanford CRFM)
- [LLM-as-a-Judge Survey](https://arxiv.org/abs/2411.15594)
- [AutoRubric: Unifying Rubric-based LLM Evaluation](https://arxiv.org/abs/2603.00077)
- [CLEAR Framework for Enterprise Agentic AI](https://arxiv.org/abs/2511.14136)
- [CLASSic: AI Agent Evaluation](https://aisera.com/blog/ai-agent-evaluation/) (ICLR 2025 Workshop)
- [Agent Benchmark Compendium](https://github.com/philschmid/ai-agent-benchmark-compendium) (50+ benchmarks)
- [Galileo Agent Evaluation Framework](https://galileo.ai/blog/agent-evaluation-framework-metrics-rubrics-benchmarks)
- [Beyond Task Completion Assessment](https://arxiv.org/abs/2512.12791)
- [LLM-as-a-Judge Primer](https://aman.ai/primers/ai/LLM-as-a-judge/)
- [Confident AI Evaluation Metrics Guide](https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation)
