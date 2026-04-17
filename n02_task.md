---
mission: VERTICAL_DENSIFICATION
nucleus: n02
wave: W2
created: 2026-04-17
priority: HIGH
effort: opus_high
---

# N02 VERTICAL_DENSIFICATION W2: Karpathy Quality Sweep

## SPEC REFERENCE
Read first: `_docs/specs/spec_vertical_densification.md`
Your wave: W2 (parallel with N01, N03-N06)

## TASK: Karpathy Sweep -- 99 quality:null artifacts in N02_marketing/

The Karpathy loop: score each quality:null artifact, improve if < 8.5, keep if >= 8.5.
Creative Lust lens: every artifact must earn its presence -- mediocre copy is worse than none.

```bash
# Heuristic pass (free):
python _tools/cex_evolve.py sweep --nucleus n02 --target 8.5 --max-rounds 1 --mode heuristic

# Check remaining:
python _tools/cex_score.py --nucleus n02 --show-below 8.5 | head -20

# Agent pass on worst 15:
python _tools/cex_evolve.py sweep --nucleus n02 --target 8.5 --max-rounds 2 --mode agent --limit 15
```

## SYNTHESIS TASK: Few-Shot Examples for 8F Marketing Patterns

Create reusable few-shot examples that any LLM can use to understand
how 8F applies to marketing/copy tasks. These become portable training artifacts.

Save: `N02_marketing/P01_knowledge/few_shot_examples_8f_marketing.md`
Kind: knowledge_card (type: few_shot_examples)
Content: 3 complete 8F trace examples for marketing tasks:
  1. "write ad copy for Black Friday" -- full F1-F8 with output
  2. "create landing page headline" -- full F1-F8 with output
  3. "build brand voice guide" -- full F1-F8 with output
Each example must be self-contained and immediately runnable by any LLM.
Source: .claude/rules/8f-reasoning.md + N02_marketing/P01_knowledge/ KCs

## COMPLETION SEQUENCE

```bash
python _tools/cex_compile.py --all
git add N02_marketing/ && git commit -m "[N02] VERTICAL_DENSIFICATION W2: quality sweep 99 artifacts + 8F few-shot examples"
python -c "from _tools.signal_writer import write_signal; write_signal('n02', 'vert_dens_w2_complete', 9.0)"
```

## COMPLETION CRITERIA
- [ ] cex_evolve.py sweep completed on N02_marketing/
- [ ] quality:null count in N02_marketing/ reduced by >= 80%
- [ ] few_shot_examples_8f_marketing.md created with 3 complete examples
- [ ] signal sent: n02 -> vert_dens_w2_complete
