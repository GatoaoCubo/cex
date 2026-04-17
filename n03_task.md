---
mission: VERTICAL_DENSIFICATION
nucleus: n03
wave: W2
created: 2026-04-17
priority: HIGH
effort: opus_high
---

# N03 VERTICAL_DENSIFICATION W2: Karpathy Quality Sweep + CoC Convergence

## SPEC REFERENCE
Read first: `_docs/specs/spec_vertical_densification.md`
Your wave: W2 (parallel with N01, N02, N04-N06)

## TASK 1: Karpathy Sweep -- 99 quality:null artifacts in N03_engineering/

Inventive Pride lens: nothing leaves N03 without being architecturally sound.

```bash
# Heuristic pass:
python _tools/cex_evolve.py sweep --nucleus n03 --target 8.5 --max-rounds 1 --mode heuristic

# Agent pass on worst 15:
python _tools/cex_evolve.py sweep --nucleus n03 --target 8.5 --max-rounds 2 --mode agent --limit 15
```

## TASK 2: CoC Convergence -- Convention-over-Configuration Artifacts

N03 owns the architectural primitives. Create 3 artifacts that codify
how the 8F pipeline (the CoC default) manifests in practice -- portable
across any LLM, any runtime, any nucleus.

### Artifact 1: pattern_8f_full_trace.md
Save: `N03_engineering/P08_architecture/pattern_8f_full_trace.md`
Kind: pattern
Content: canonical 8F full-trace pattern -- the standard template for how any
nucleus executes F1-F8 with evidence output at each step. Includes:
- Exact output format per step (text templates with placeholders)
- Construction Triad decision tree (Template-First >= 60% | Hybrid 30-60% | Fresh < 30%)
- Anti-patterns (skip F7, missing F8 signal, no 12LP checklist)
Source: .claude/rules/8f-reasoning.md

### Artifact 2: action_paradigm_cex_dispatch.md
Save: `N03_engineering/P12_orchestration/action_paradigm_cex_dispatch.md`
Kind: action_paradigm
Content: the CEX dispatch paradigm -- the sequence of decisions N07 makes when
routing work to nuclei. Includes: intent resolution -> GDP check -> kind resolution
-> nucleus selection -> handoff format -> signal protocol. Machine-readable decision tree.
Source: .claude/rules/n07-input-transmutation.md + .claude/rules/guided-decisions.md

### Artifact 3: reasoning_trace_8f_example.md
Save: `N03_engineering/P08_architecture/reasoning_trace_8f_example.md`
Kind: reasoning_trace
Content: a complete worked 8F reasoning trace for a real task: "create agent for N03".
Shows every thought, every file read, every decision made at F1-F8. Pure pedagogical
artifact -- any LLM can read this and understand how to execute 8F correctly.
Source: real N03 execution trace pattern

## COMPLETION SEQUENCE

```bash
python _tools/cex_compile.py --all
git add N03_engineering/ && git commit -m "[N03] VERTICAL_DENSIFICATION W2: quality sweep 99 artifacts + CoC convergence patterns"
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'vert_dens_w2_complete', 9.0)"
```

## COMPLETION CRITERIA
- [ ] cex_evolve.py sweep completed on N03_engineering/
- [ ] quality:null reduced >= 80%
- [ ] pattern_8f_full_trace.md created
- [ ] action_paradigm_cex_dispatch.md created
- [ ] reasoning_trace_8f_example.md created
- [ ] signal sent: n03 -> vert_dens_w2_complete
