---
id: p11_reward_signal
kind: reward_signal
pillar: P11
version: 1.0.0
title: "Template — Reward Signal"
tags: [template, reward, signal, reinforcement, feedback]
tldr: "A scalar or structured signal indicating output quality. Drives learning: positive rewards reinforce patterns, negative rewards trigger correction. Includes source, confidence, and decay."
quality: 9.0
related:
  - bld_collaboration_reward_signal
  - bld_examples_lifecycle_rule
  - bld_instruction_reward_signal
  - signal-builder
  - bld_memory_signal
  - bld_examples_reward_signal
  - reward-signal-builder
  - p01_kc_confidence_scoring
  - p06_schema_source_quality
  - bld_knowledge_card_reward_model
---

# Reward Signal: [SIGNAL_NAME]

## Purpose
[WHAT behavior this reward reinforces or discourages]

## Signal Schema
```yaml
id: "[SIGNAL_ID]"
source: [user | peer_review | automated | llm_judge]
target: "[ARTIFACT_ID or AGENT_ID]"
value: [-1.0 to 1.0]  # negative = bad, 0 = neutral, positive = good
confidence: [0.0-1.0]
timestamp: "[ISO8601]"
dimension: [quality | accuracy | tone | speed | format]
```

## Signal Sources

| Source | Reliability | Latency | Example |
|--------|------------|---------|---------|
| User explicit | High (0.9) | Immediate | Thumbs up/down |
| User implicit | Medium (0.6) | Delayed | Engagement metrics |
| Peer review | High (0.85) | Hours | cex_score.py rating |
| Automated gate | Very high (0.95) | Immediate | F7 pass/fail |
| LLM judge | Medium (0.7) | Seconds | Rubric score |

## Reward Aggregation
When multiple signals for same target:
```python
final_reward = weighted_average(
    signals,
    weights={
        "automated": 0.3,
        "peer_review": 0.3,
        "user_explicit": 0.25,
        "llm_judge": 0.1,
        "user_implicit": 0.05,
    }
)
```

## Decay Policy
- **Fresh** (< 7 days): Full weight
- **Recent** (7-30 days): 80% weight
- **Old** (30-90 days): 50% weight
- **Stale** (> 90 days): 20% weight — still influences, doesn't dominate

## Response to Signals

| Signal Range | Interpretation | Action |
|-------------|---------------|--------|
| 0.8 to 1.0 | Excellent | Reinforce pattern in memory |
| 0.5 to 0.8 | Good | No action needed |
| 0.0 to 0.5 | Mediocre | Flag for review |
| -0.5 to 0.0 | Poor | Trigger correction cycle |
| -1.0 to -0.5 | Bad | Immediate constraint update |

## Quality Gate
- [ ] Value range is bounded [-1.0, 1.0]
- [ ] Source reliability documented
- [ ] Decay policy prevents stale signals from dominating
- [ ] Action thresholds defined

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_reward_signal]] | downstream | 0.22 |
| [[bld_examples_lifecycle_rule]] | related | 0.20 |
| [[bld_instruction_reward_signal]] | upstream | 0.20 |
| [[signal-builder]] | downstream | 0.20 |
| [[bld_memory_signal]] | upstream | 0.19 |
| [[bld_examples_reward_signal]] | upstream | 0.19 |
| [[reward-signal-builder]] | related | 0.19 |
| [[p01_kc_confidence_scoring]] | upstream | 0.19 |
| [[p06_schema_source_quality]] | upstream | 0.19 |
| [[bld_knowledge_card_reward_model]] | upstream | 0.18 |
