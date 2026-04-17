---
mission: VERTICAL_DENSIFICATION
nucleus: n06
wave: W2
created: 2026-04-17
priority: HIGH
effort: opus_high
---

# N06 VERTICAL_DENSIFICATION W2: Karpathy Quality Sweep + Revenue Synthesis

## SPEC REFERENCE
Read first: `_docs/specs/spec_vertical_densification.md`
Your wave: W2 (parallel with N01-N05)

## TASK 1: Karpathy Sweep -- 113 quality:null artifacts in N06_commercial/

Strategic Greed lens: every artifact must either generate revenue or protect it.
An artifact that does neither must be improved until it does, or discarded.

```bash
# Heuristic pass:
python _tools/cex_evolve.py sweep --nucleus n06 --target 8.5 --max-rounds 1 --mode heuristic

# Agent pass on worst 20:
python _tools/cex_evolve.py sweep --nucleus n06 --target 8.5 --max-rounds 2 --mode agent --limit 20
```

## TASK 2: Revenue Architecture Synthesis

### Artifact 1: few_shot_examples_pricing_scenarios.md
Save: `N06_commercial/P01_knowledge/few_shot_examples_pricing_scenarios.md`
Kind: knowledge_card (type: few_shot_examples)
Content: 4 complete pricing decision examples showing N06 reasoning:
  1. "design SaaS pricing tiers" -- full 8F trace with 3-tier output
  2. "calculate LTV for enterprise segment" -- LTV_CAC ratio worked example
  3. "model churn intervention ROI" -- churn_prevention_playbook applied
  4. "structure referral program incentives" -- referral mechanics design
Each example: problem statement + 8F trace summary + structured output.
Source: N06_commercial/P11_feedback/ + N06_commercial/P06_schema/ artifacts

### Artifact 2: mental_model_revenue_flywheel.md
Save: `N06_commercial/P01_knowledge/mental_model_revenue_flywheel.md`
Kind: mental_model
Content: the CEX commercial flywheel as a mental model for any LLM:
acquire -> activate -> retain -> expand -> measure -> improve.
Each stage: which kinds activate it, which metrics govern it,
which N06 artifacts implement it. Portable across any SaaS business.
Source: N06_commercial/P12_orchestration/workflow_revenue_loop.md + P11_feedback artifacts

## COMPLETION SEQUENCE

```bash
python _tools/cex_compile.py --all
git add N06_commercial/ && git commit -m "[N06] VERTICAL_DENSIFICATION W2: quality sweep 113 artifacts + pricing few-shots + revenue flywheel"
python -c "from _tools.signal_writer import write_signal; write_signal('n06', 'vert_dens_w2_complete', 9.0)"
```

## COMPLETION CRITERIA
- [ ] cex_evolve.py sweep completed on N06_commercial/
- [ ] quality:null reduced >= 80%
- [ ] few_shot_examples_pricing_scenarios.md created with 4 examples
- [ ] mental_model_revenue_flywheel.md created
- [ ] signal sent: n06 -> vert_dens_w2_complete
