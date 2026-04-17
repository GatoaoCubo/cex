---
id: p11_sil_n03
kind: self_improvement_loop
pillar: P11
title: "Self-Improvement Loop -- N03 Engineering Evolution"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: artifact-construction
quality: 9.1
tags: [self-improvement-loop, N03, evolution, quality, autonomous, flywheel, 8F]
tldr: "Autonomous quality evolution protocol for N03. Scans all N03 artifacts for quality < 9.0, ranks by improvement ROI, applies heuristic + LLM improvement passes, and compounds quality over time via the Inventive Pride flywheel."
density_score: 0.91
updated: "2026-04-17"
---

# Self-Improvement Loop: N03 Engineering Evolution

## Purpose

N03 does not just BUILD -- it IMPROVES what it has built.
Inventive Pride demands that the portfolio gets better over time, not just bigger.
This loop is the mechanism: scan -> rank -> improve -> verify -> repeat.

**Target:** all N03 artifacts reach quality >= 9.0 or are flagged for human review.

## Loop Architecture

```
SCAN: Read all N03 artifacts (find N03_engineering -name "*.md")
  |
RANK: Score each artifact; sort by improvement ROI
  |   ROI = (9.0 - current_score) * pillar_priority_weight
  |
SELECT: Take top N candidates per run (default: 5)
  |
IMPROVE: Apply improvement strategy per score band
  |
VERIFY: Re-score; accept if improved; revert if worse
  |
PERSIST: Update baseline in results.tsv; write learning records
  |
REPEAT: Next run (scheduled or triggered)
```

## Trigger Conditions

| Trigger | When | Mode |
|---------|------|------|
| Post-wave | After SELF_ASSEMBLY wave completes | Full scan |
| Nightly | Scheduled 02:00 UTC | Full scan |
| On-demand | N07 dispatches `/evolve n03` | Full scan |
| Post-build | After any F8 COLLABORATE | Single artifact |
| Regression | bugloop detects quality drop | Targeted fix |

## Score Bands and Strategies

### Band A: score < 7.0 (below floor)

**Strategy:** Full rewrite via 8F pipeline  
**Reason:** Below-floor artifacts cannot be patched; they need to be rebuilt from intent.

```bash
python cex_sdk/cex_8f_runner.py --kind {kind} --verb REWRITE --quality-target 9.0
```

### Band B: score in [7.0, 8.5) (acceptable, needs improvement)

**Strategy:** Targeted section improvement  
**Approach:**
1. Load artifact + scoring rubric
2. Identify lowest-scoring dimension (D1-D5)
3. Inject improvement prompt: "The {dimension} dimension scored {score}/10. Improve specifically: {rationale}"
4. Regenerate only the failing sections (not full rewrite)
5. Re-validate via quality gate

### Band C: score in [8.5, 9.0) (good, close to target)

**Strategy:** Precision polish  
**Approach:**
1. Check vocabulary compliance (often the gap at this score band)
2. Increase density_score by converting prose to tables
3. Add missing examples if LP04 failed
4. Ensure all cross-references are canonical

### Band D: score >= 9.0 (excellent)

**Strategy:** Exemplar promotion  
**Approach:**
1. Mark artifact as candidate example for builder ISO injection
2. Check if this artifact can be cited in kc_{kind} as a model
3. Run regression_check to ensure it stays at this level

## ROI Weighting

```python
PILLAR_PRIORITY_WEIGHTS = {
    "P06": 3.0,   # schema -- critical, blocking
    "P07": 2.5,   # evaluation -- quality infrastructure
    "P08": 2.0,   # architecture -- decisions compound
    "P11": 2.0,   # feedback -- self-improving
    "P04": 1.5,   # tools -- operational leverage
    "P03": 1.5,   # prompt -- interface quality
    "P02": 1.0,   # model -- stable
    "P01": 1.0,   # knowledge -- gradual accumulation
    "P05": 0.8,   # output -- often ephemeral
    "P09": 1.2,   # config -- high blast radius if wrong
    "P10": 1.0,   # memory -- value accrues over time
    "P12": 1.0,   # orchestration -- stable
}

roi = (9.0 - current_score) * pillar_priority_weight
# Higher ROI = improve this first
```

## Improvement Run Report

```yaml
loop_run:
  nucleus: n03
  timestamp: 2026-04-17T14:00:00
  trigger: post_wave
  artifacts_scanned: 98
  artifacts_below_target: 12
  artifacts_selected: 5
  improvements:
    - id: p06_is_build_contract
      score_before: null
      score_after: null
      strategy: post_build_check
      status: passed_gate
    - id: p07_gt_n03
      score_before: null
      score_after: null
      strategy: exemplar_check
      status: candidate_example
  artifacts_improved: 0      # quality: null means peer-review pending
  artifacts_regressed: 0
  artifacts_flagged_for_human: 0
  next_run: scheduled
```

## Invariants

1. Self-improvement loop NEVER sets quality field -- it remains null until peer review
2. If improvement makes score WORSE: revert to original (git checkout the file)
3. Maximum 3 improvement attempts per artifact per loop run
4. Exemplar promotion requires N07 confirmation (GDP required for ISO injection)
5. Loop stops after 3 hours wall-clock to prevent infinite execution
6. All improvements are committed as: `[N03] self-improvement: {kind} quality improvement pass`
