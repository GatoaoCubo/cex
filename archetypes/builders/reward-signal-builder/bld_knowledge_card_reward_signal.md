---
kind: knowledge_card
id: bld_knowledge_card_reward_signal
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for reward_signal production — continuous quality scoring for agent improvement
sources: RLHF literature, DPO paper (Rafailov 2023), Constitutional AI (Anthropic 2022), LLM-as-judge (Zheng 2023)
---

# Domain Knowledge: reward_signal
## Executive Summary
Reward signals are continuous quality scores that drive agent improvement through learning loops. Unlike quality gates (binary pass/fail) or scoring rubrics (static criteria definitions), reward signals feed live systems: RLHF reward models, DPO preference datasets, Constitutional AI critique cycles, and LLM-as-judge monitoring pipelines. A reward signal is only as good as its calibration — scale semantics, baseline, and anti-reward-hacking design are load-bearing.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P11 (Feedback) |
| llm_function | GOVERN (quality enforcement) |
| Signal types | scalar, preference, critique, comparative, implicit |
| Scale options | 0-1, 0-10, binary, -1_to_1 |
| Baseline | minimum acceptable score; triggers retraining or filtering below |
| Frequency | per_turn, per_task, per_session, on_demand |
| Aggregation | mean, weighted_mean, min, max, last |
## Signal Type Patterns
| Type | Mechanism | Use case | Reward hacking risk |
|------|-----------|----------|---------------------|
| scalar | LLM-judge assigns 0-1 or 0-10 numeric score | General quality, helpfulness | High if single criterion |
| preference | Human/model picks A > B from pair | RLHF training data collection | Medium — preference noise |
| critique | LLM writes critique + revised output + score | Constitutional AI, self-improvement | Low — multi-step process |
| comparative | N outputs ranked by quality | DPO dataset construction | Medium — ranking drift |
| implicit | Behavioral signals (edits, clicks, re-prompts) | Production monitoring | Low — ground truth |
## Key Concepts
- **RLHF (Reinforcement Learning from Human Feedback)**: Train a reward model on preference pairs, then use PPO to optimize the policy against the reward model. Reward signal feeds the reward model training phase.
- **DPO (Direct Preference Optimization)**: No explicit reward model — preference pairs (chosen/rejected) implicitly define reward via the Bradley-Terry model. Signal type: preference.
- **Constitutional AI critique**: LLM evaluates its own output against principles, produces critique + revision. Signal type: critique. Produces both signal and improved output simultaneously.
- **LLM-as-judge**: A model (often GPT-4 or Claude) evaluates peer model outputs on defined criteria. Requires careful calibration to avoid positional bias and verbosity bias.
- **Reward shaping**: Adding auxiliary rewards to guide exploration toward desired behaviors without changing the optimal policy. Must be used carefully to avoid unintended optima.
## Patterns
| Pattern | Example | When to use |
|---------|---------|-------------|
| Multi-criteria scalar | factual_accuracy 0.4 + tone 0.3 + conciseness 0.3 | General text quality |
| Preference pair collection | human rates A>B on helpfulness | RLHF dataset building |
| Critique cycle | critique → revise → score | Constitutional AI pipeline |
| Implicit signal mining | edit distance after generation | Production quality monitoring |
- **Baseline calibration**: Set baseline at the P20 of human-rated outputs — scores below this percentile indicate the model is underperforming vs. human baseline.
- **Criteria weighting**: Use additive weights summing to 1.0. Minimum 2 criteria — single-criterion rewards invite hacking.
- **Scale normalization**: Normalize all criteria to same scale before weighted aggregation.
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Single-dimension reward | Model learns to maximize one dimension while degrading others (reward hacking) |
| No baseline calibration | Cannot distinguish good from acceptable from poor without reference point |
| Verbosity bias in LLM-judge | Judge model rates longer outputs higher regardless of quality; correct with length normalization |
| Positional bias | LLM-judge prefers output A over B when A is presented first; correct with swap-and-average |
| Conflating with quality_gate | Reward signals are continuous; using them as binary gates discards gradient information |
| Static criteria for evolving domain | Criteria become stale as model improves; refresh every training cycle |
| Human-only signal at scale | Human annotation cannot scale to per-turn evaluation; use LLM-judge with human spot-check calibration |
## Application Loops
1. **RLHF**: reward_signal -> reward model training -> PPO policy optimization -> deployment
2. **DPO**: preference pairs -> direct policy optimization (no reward model) -> deployment
3. **Filtering**: score outputs during generation -> filter below baseline -> include only high-quality in training data
4. **Monitoring**: per-turn scoring in production -> alert when rolling average falls below baseline -> trigger retraining
## References
- Ziegler et al. (2019): Fine-tuning language models from human preferences
- Rafailov et al. (2023): Direct Preference Optimization
- Bai et al. (2022): Constitutional AI — Anthropic
- Zheng et al. (2023): Judging LLM-as-a-Judge with MT-Bench
- clig.dev equivalent for reward signals: reward-bench.github.io
