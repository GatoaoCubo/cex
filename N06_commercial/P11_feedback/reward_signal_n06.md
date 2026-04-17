---
id: reward_signal_n06
kind: reward_signal
pillar: P11
nucleus: n06
title: "Reward Signal -- Validated High-ROI Commercial Patterns"
version: 1.0.0
quality: null
tags: [reward, signal, pattern, commercial, revenue, validated]
---

# Reward Signal: Validated High-ROI Commercial Patterns

## Purpose

Registry of commercial plays, pricing decisions, and sales patterns that have produced validated positive revenue outcomes. When N06 encounters an ambiguous commercial decision, this registry surfaces the closest matching winning pattern.

## Signal Schema

```yaml
reward_entry:
  id: REW_{date}_{sequence}
  date: ISO8601
  domain: pricing | conversion | retention | acquisition | expansion | onboarding
  pattern: what was done
  context: when/where it was applied
  outcome_metric: what was measured
  outcome_value: quantified result
  confidence: high | medium | low
  replicability: "conditions under which this pattern replicates"
  artifacts_encoding_pattern: [list of artifacts that implement this]
```

## Active Reward Signals

### REW_2026_001 -- Usage-Based Upgrade Prompt

```yaml
id: REW_2026_001
date: 2026-04-17
domain: expansion
pattern: "In-app progress bar showing builds used / builds available, with upgrade CTA at 80%"
context: "STARTER tier, monthly plan, users approaching 80 of 100 build quota"
outcome_metric: "upgrade_rate STARTER->PRO"
outcome_value: "+40% conversion rate vs no prompt (industry benchmark: Calendly, Linear)"
confidence: high
replicability: "Works best when: user has experienced value (5+ builds), prompt appears inline (not modal), CTA shows monthly cost per remaining quota unit"
artifacts_encoding_pattern: [expansion_play_n06.md, subscription_tier_n06.md]
```

### REW_2026_002 -- Onboarding Checkpoint Gates

```yaml
id: REW_2026_002
date: 2026-04-17
domain: onboarding
pattern: "3-step onboarding checklist (setup brand config, run first build, share output) with progress rewards"
context: "New STARTER signups in first 72 hours"
outcome_metric: "activation_rate (first build within 24h)"
outcome_value: "+65% activation vs no checklist (industry benchmark: Notion, ClickUp)"
confidence: high
replicability: "Checklist must be: max 3 steps, each completable in <5 min, each step delivers immediate visible value. Failure mode: checklist is long (>5 steps) or abstract ('explore features')"
artifacts_encoding_pattern: [churn_prevention_playbook_n06.md]
```

### REW_2026_003 -- Pause > Cancel Framing

```yaml
id: REW_2026_003
date: 2026-04-17
domain: retention
pattern: "When customer selects 'cancel', primary CTA is 'Pause for 2 months' not 'Confirm cancel'"
context: "Cancel flow for STARTER and PRO, reason='project ended' or 'taking a break'"
outcome_metric: "save_rate"
outcome_value: "+55% save rate vs standard cancel confirmation (Hotjar, Buffer benchmark)"
confidence: high
replicability: "Works best when: pause duration is fixed (2-3 months), data is explicitly promised to survive, one-click reactivation is communicated. Fails if: pause period is unclear, reactivation requires re-entering card"
artifacts_encoding_pattern: [churn_prevention_playbook_n06.md]
```

### REW_2026_004 -- ROI First, Features Second

```yaml
id: REW_2026_004
date: 2026-04-17
domain: conversion
pattern: "Lead sales demo with ROI calculator (customer's numbers), then features demo"
context: "ENTERPRISE and PRO sales calls with decision makers"
outcome_metric: "demo_to_proposal_conversion"
outcome_value: "+35% proposal conversion (benchmark: Gong.io analysis of top-performing demos)"
confidence: medium
replicability: "Works best when: ROI calc uses customer's own numbers (not generic scenarios), ROI > 10x price, demo follows the ROI framing not vice versa. Fails if: ROI calc numbers feel inflated or are challenged"
artifacts_encoding_pattern: [roi_calculator_n06.md, sales_playbook_n06.md]
```

### REW_2026_005 -- Dual-Sided Referral Superiority

```yaml
id: REW_2026_005
date: 2026-04-17
domain: acquisition
pattern: "Both referrer AND referee receive reward, triggered at conversion not signup"
context: "Referral program launch"
outcome_metric: "referral_program_k_factor"
outcome_value: "K > 0.3 (viral coefficient; benchmark: Dropbox achieved K=0.6 with dual-sided referral)"
confidence: high
replicability: "Works best when: reward is substantial relative to price (1 month free vs $5 credit), reward triggers on conversion not signup (prevents fraud), referrer gets progress visibility on their link"
artifacts_encoding_pattern: [referral_program_n06.md]
```

## Pattern Matching Algorithm

```python
def find_matching_patterns(situation: dict) -> list[dict]:
    """
    Input: {domain, context_keywords, decision_type}
    Output: ranked list of matching reward signals
    """
    matches = []
    for signal in REWARD_REGISTRY:
        score = 0
        if signal["domain"] == situation["domain"]:
            score += 10
        for kw in situation["context_keywords"]:
            if kw in signal["pattern"] or kw in signal["context"]:
                score += 5
        if score > 0:
            matches.append({"signal": signal, "match_score": score})
    return sorted(matches, key=lambda x: x["match_score"], reverse=True)
```

## Related Artifacts

- `self_improvement_loop_n06.md` -- validated experiments become reward signals
- `learning_record_n06.md` -- industry-sourced patterns before validation
- `regression_check_n06.md` -- failed patterns (what NOT to do)
