---
id: self_improvement_loop_n01
kind: self_improvement_loop
8f: F7_govern
pillar: P11
nucleus: n01
title: "N01 Autonomous Quality Evolution Protocol"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.2
tags: [self_improvement_loop, evolution, quality, n01, analytical_envy, autonomous]
tldr: "N01 self-improvement loop: scan all artifacts for quality < 9.0, identify systematic gaps (missing comparisons, stale sources, thin evidence), apply targeted improvements, re-score. Driven by Analytical Envy: never accept 'good enough'."
density_score: 0.92
updated: "2026-04-17"
related:
  - n01_qg_intelligence
  - p11_qg_intelligence
  - p01_kc_artifact_quality_evaluation_methods
  - p03_sp_intelligence_nucleus
  - p07_sr_intelligence_evaluation
  - p12_wf_auto_evolve
  - p03_sp_n03_creation_nucleus
  - skill
  - p08_pat_3phase_build_protocol
  - report_intent_resolution_value_prop
---

<!-- 8F: F1 constrain=P11/self_improvement_loop F2 become=self-improvement-loop-builder F3 inject=quality_gate_intelligence+bias_audit_n01+eval_framework_n01+cex_evolve F4 reason=Analytical Envy = perpetual dissatisfaction with current quality; self-improvement loop is the systematic expression of that dissatisfaction F5 call=cex_compile+cex_evolve F6 produce=self_improvement_loop_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P11_feedback/ -->

## Purpose

N01 Analytical Envy is not satisfied with any static quality level.
Every artifact that scores < 9.5 is an affront to the sin lens.

This loop runs periodically to:
1. Identify which N01 artifacts score below threshold
2. Classify WHY (missing comparisons, weak evidence, stale sources, thin analysis)
3. Apply targeted improvements using F3-F7
4. Re-score and commit improvements

The loop is not about perfection -- it is about COMPOUNDING.
Each cycle makes N01's corpus denser, more comparative, more trustworthy.

## Trigger Conditions

| Trigger | Condition | Frequency |
|---------|-----------|-----------|
| Scheduled | cron: every Sunday 03:00 | weekly |
| Quality gate fail | new artifact scores < 8.5 in F7 | immediate |
| Stale data | source date > 90 days in any P01 KC | monthly |
| Gap detection | new artifact kind added to 257-kind list | on demand |
| N07 dispatch | explicit `cex_evolve.py sweep` call | on demand |

## Loop Phases

### Phase 1: SCAN

```
artifacts = find("N01_intelligence/**/*.md", kind!="README")
low_quality = [a for a in artifacts if a.quality < 9.0 or a.quality is None]
sort by: density_score ASC (lowest density = biggest improvement opportunity)
```

### Phase 2: CLASSIFY

For each low-quality artifact, apply the N01 Deficiency Taxonomy:

| Deficiency Code | Name | Symptom | Fix |
|-----------------|------|---------|-----|
| D1 | Thin Evidence | < 3 sources, low citation density | add triangulated sources |
| D2 | Missing Comparison | no competitive benchmark | add vs-alternatives table |
| D3 | Stale Data | sources > 90 days | refresh sources, update data |
| D4 | Weak Structure | prose > tables | convert to table-first format |
| D5 | No Confidence Score | findings stated as fact | add confidence levels |
| D6 | Selection Bias | bias_audit score < 6 | run bias_audit, add counter-evidence |
| D7 | Vocabulary Drift | uses metaphors not industry terms | transmute to canonical terms |

### Phase 3: IMPROVE

For each artifact with deficiency:

```
load_artifact(path)
load_builder_isos(kind)
classify_deficiency(artifact) -> [D1, D3, D4]
for deficiency in deficiencies:
    apply_fix(artifact, deficiency)
run_f7_govern(artifact)
if new_score > old_score:
    save(artifact)
    commit("[N01] evolve: {path} {old} -> {new}")
else:
    revert()
```

### Phase 4: SCORE REPORT

```
| Artifact | Old Score | New Score | Deficiencies Fixed |
|----------|-----------|-----------|-------------------|
| kc_openai_analysis.md | 7.2 | 9.1 | D2, D3, D4 |
| ...                   | ... | ... | ...         |

Summary:
  Artifacts improved: {n}
  Average delta: +{x}
  Remaining < 9.0: {n}
  Next cycle: {date}
```

## Quality Targets

| Tier | Score Range | Action |
|------|------------|--------|
| Elite | 9.5 - 10.0 | maintain, use as examples |
| Target | 9.0 - 9.4 | monitor for staleness |
| Improve | 8.0 - 8.9 | queue for next cycle |
| Fix now | 6.0 - 7.9 | immediate improvement |
| Reject | < 6.0 | delete and rebuild |

## Improvement Patterns (with Analytical Envy)

For N01, every improvement MUST add comparative context:

| Original (weak) | Improved (Analytical Envy) |
|-----------------|---------------------------|
| "X is good at Y" | "X outperforms A by 30%, trails B by 12%" |
| "A costs $10/mo" | "A at $10 vs B at $8 vs C at $15 -- B wins unit economics" |
| "Trend is growing" | "Trend grew 40% YoY vs category avg 18% -- 2.2x category" |
| "Sources: [3 links]" | "Sources: [3 links], confidence 87%, last verified 2026-04-10" |

## Integration

```
cex_evolve.py sweep --target n01 --quality-threshold 9.0
  -> reads: self_improvement_loop_n01.md (this file)
  -> applies: bias_audit_n01.md checks
  -> scores: quality_gate_intelligence.md gates
  -> outputs: improvement report + commits
```

## Comparison vs. Alternatives

| Approach | Coverage | Automation | Quality Delta | N01 Fit |
|----------|---------|------------|--------------|---------|
| Manual review | 100% | 0% | high | impractical |
| cex_evolve.py (generic) | 100% | 90% | medium | partial fit |
| This loop (N01-specific) | 100% | 90% | high (N01 deficiencies) | optimal |
| External LLM judge | 100% | 80% | medium | use as sanity check |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n01_qg_intelligence]] | related | 0.22 |
| [[p11_qg_intelligence]] | related | 0.20 |
| [[p01_kc_artifact_quality_evaluation_methods]] | upstream | 0.19 |
| [[p03_sp_intelligence_nucleus]] | upstream | 0.19 |
| [[p07_sr_intelligence_evaluation]] | upstream | 0.18 |
| [[p12_wf_auto_evolve]] | downstream | 0.18 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.18 |
| [[skill]] | upstream | 0.17 |
| [[p08_pat_3phase_build_protocol]] | upstream | 0.17 |
| [[report_intent_resolution_value_prop]] | upstream | 0.17 |
