# P11 Feedback — Ecosystem Map
> Generated: 2026-03-28 | Author: builder_agent

## 1. Frameworks Audited
| Framework | Domain | Key Concepts |
|-----------|--------|--------------|
| RLHF (InstructGPT) | Alignment training | Reward model, preference dataset, PPO training loop, human feedback collection, comparison pairs, KL divergence penalty |
| DPO (Direct Preference Optimization) | Alignment training | Preference pairs, implicit reward model, reference policy, Bradley-Terry model, no separate reward model needed |
| Constitutional AI (Anthropic) | Self-alignment | Constitutional principles, red-teaming, self-critique, chain-of-thought critiques, revision loops, harmlessness training |
| OpenAI Moderation API | Content safety | Category classification (hate, violence, sexual, self-harm), category scores (0-1), flagged boolean, threshold-based filtering |
| Guardrails AI | Output validation | Validators (regex, LLM-based, custom), on_fail actions (reask, fix, filter, refrain, exception), structured output enforcement, Guard wrapper |
| NVIDIA NeMo Guardrails | Dialog safety | Input rails, output rails, dialog rails, retrieval rails, Colang flows, action chains, bot message generation, fact-checking rails |
| Reward Models | Quality scoring | Scalar reward signal, preference-trained scorer, proxy reward, reward hacking detection, reward model ensemble |
| A/B Testing for LLMs | Experimentation | Variant comparison, statistical significance, prompt variants, model variants, metric definitions, traffic splitting, experiment lifecycle |
| Online Learning | Continuous improvement | Feedback loops, incremental model updates, data flywheel, active learning, exploration-exploitation, bandit algorithms |
| Human-in-the-Loop (HITL) | Quality assurance | Approval workflows, escalation rules, confidence thresholds, human review queues, annotation interfaces, disagreement resolution |

## 2. Industry Concepts Found
| Concept | Framework(s) | Description | Frequency |
|---------|-------------|-------------|:---------:|
| Quality Gate / Validator | Guardrails AI (validators), NeMo (rails), OpenAI Moderation (threshold), Constitutional AI (self-critique pass/fail), Reward Models (threshold) | Pass/fail checkpoint that blocks or modifies output below a quality/safety threshold | 5 |
| Reward / Preference Signal | RLHF (reward model), DPO (implicit reward), Reward Models (scalar score), Constitutional AI (critique score), A/B Testing (metric delta) | Continuous quality signal that grades output on a scale, used to improve future outputs | 5 |
| Guardrail / Safety Boundary | NeMo Guardrails (input/output rails), OpenAI Moderation (category filtering), Constitutional AI (principles), Guardrails AI (on_fail actions) | Hard constraint that prevents harmful, off-topic, or policy-violating outputs | 4 |
| Feedback Loop | Online Learning (data flywheel), RLHF (human feedback collection), A/B Testing (experiment results), DPO (preference collection) | Cyclic process where output quality informs future improvement (human or automated) | 4 |
| Self-Correction Cycle | Constitutional AI (critique-revise), Guardrails AI (reask/fix on_fail), NeMo (dialog re-generation), RLHF (iterative refinement) | Automated detect-critique-fix cycle without human intervention | 4 |
| Human Review / Escalation | HITL (approval workflows), A/B Testing (human evaluation), RLHF (human preference labeling), Online Learning (active learning queries) | Human judgment injected at decision points where automated confidence is low | 4 |
| Lifecycle / Freshness Rule | Online Learning (model staleness detection), A/B Testing (experiment expiry), Reward Models (reward drift), NeMo (flow versioning) | Rules governing when artifacts should be refreshed, archived, or promoted based on age or performance | 4 |
| Experiment / A/B Config | A/B Testing (variant config), Online Learning (exploration rate), DPO (preference experiment), RLHF (comparison batch) | Structured experiment definition with variants, metrics, duration, and significance thresholds | 3 |
| Optimization Policy | Online Learning (bandit policy), DPO (optimization objective), RLHF (PPO policy), Reward Models (ensemble strategy), A/B Testing (winning variant promotion) | Strategy for improving a metric over time through iterative adjustments | 5 |
| Content Classification | OpenAI Moderation (category scores), NeMo (topical rails), Constitutional AI (harm taxonomy), Guardrails AI (topic validators) | Classifying content into categories (safe/unsafe, on-topic/off-topic) with confidence scores | 4 |

## 3. CEX Current vs Industry
| CEX Kind | Maps To | Coverage % | Gap |
|----------|---------|:----------:|-----|
| quality_gate | Quality Gate / Validator | 90% | Excellent match. CEX quality_gate (score-based pass/fail) aligns perfectly with Guardrails AI validators and reward model thresholds. Gap: industry gates support chained validators with different on_fail strategies per validator. |
| bugloop | Self-Correction Cycle | 80% | Good match to Constitutional AI critique-revise and Guardrails AI reask/fix. Gap: industry self-correction tracks iteration count and has a max-retries escape hatch. CEX bugloop is well-designed (detect>fix>verify) but could add iteration metadata. |
| lifecycle_rule | Lifecycle / Freshness Rule | 85% | Strong match. Industry validates freshness-based archival and performance-based promotion. Gap: industry lifecycle rules increasingly include metric-triggered transitions (e.g., "archive if accuracy drops below X"), not just time-based. |
| guardrail | Guardrail / Safety Boundary | 90% | Excellent match. Maps directly to NeMo rails and OpenAI Moderation. CEX guardrails are well-scoped as safety boundaries distinct from quality gates. Gap: industry guardrails support layered rail types (input rail, output rail, dialog rail). |
| optimizer | Optimization Policy | 75% | Reasonable match. CEX optimizer (metric>action) captures the core concept. Gap: industry optimizers are more sophisticated — bandit algorithms (Online Learning), PPO policies (RLHF), winning-variant promotion (A/B Testing). CEX lacks experiment-linkage. |

## 4. Proposed NEW Kinds (ONLY if 2+ frameworks use it)
| Kind | Justification | Frameworks | Priority |
|------|---------------|------------|:-------:|
| reward_signal | A continuous quality signal that scores output (0-1 or scalar). Distinct from quality_gate (binary pass/fail) and optimizer (acts on signals, doesn't define them). Every alignment framework produces reward signals: RLHF trains explicit reward models, DPO derives implicit rewards, Constitutional AI generates critique scores. CEX currently has no kind for "the score itself" as a reusable artifact. | RLHF (reward model output), DPO (implicit reward), Reward Models (scalar scores), Constitutional AI (critique scores), A/B Testing (metric deltas) | high |
| experiment_config | Structured experiment definitions (variants, metrics, duration, significance threshold, traffic split). Distinct from optimizer (ongoing improvement) and quality_gate (single-point check). Experiments are time-bounded, hypothesis-driven evaluations. CEX has no kind for managing prompt/model experiments. | A/B Testing (experiment config), Online Learning (exploration config), DPO (preference experiment batches), RLHF (comparison batch config) | med |

## 5. Proposed REMOVALS/RENAMES
| Kind | Action | Reason |
|------|--------|--------|
| bugloop | KEEP (add iteration metadata) | Well-designed CEX concept validated by Constitutional AI and Guardrails AI patterns. Consider adding `max_iterations` and `iteration_log` fields to prevent infinite loops and track convergence. |
| optimizer | KEEP (link to reward_signal) | Valid kind. If reward_signal is added, optimizer.boundary should reference it: "Acts on reward_signals to improve a target metric." This creates a clean signal→optimizer pipeline. |

## 6. KEEPS (validated)
| Kind | Frameworks That Match |
|------|----------------------|
| quality_gate | Guardrails AI validators, NeMo Guardrails rails, OpenAI Moderation thresholds, Reward Model score thresholds, Constitutional AI self-critique pass/fail |
| bugloop | Constitutional AI critique-revise loop, Guardrails AI reask/fix on_fail, NeMo dialog re-generation |
| lifecycle_rule | Online Learning staleness detection, A/B Testing experiment expiry, Reward Model drift detection, NeMo flow versioning |
| guardrail | NeMo Guardrails (input/output/dialog rails), OpenAI Moderation (category filtering), Constitutional AI (principles), Guardrails AI (validators with refrain/exception) |
| optimizer | Online Learning bandit policies, DPO optimization objective, RLHF PPO policy, A/B Testing winning-variant promotion |

## 7. Summary
Current: 5 kinds → Proposed: 7 kinds (+reward_signal, +experiment_config) | Coverage: ~84% → ~93%

Key insight: CEX's feedback pillar is the strongest of the five audited — all 5 existing kinds are well-validated by industry. The primary gap is the **signal/experiment layer**: industry universally separates the quality signal (reward_signal) from the gate that enforces it (quality_gate) and the policy that improves it (optimizer). This creates a clean three-stage pipeline: **measure** (reward_signal) → **enforce** (quality_gate) → **improve** (optimizer). Adding experiment_config brings the missing scientific rigor — the ability to formally test whether a change actually improves the reward signal before promoting it.
