---
name: dream
description: Generate 3-5 divergent approaches to a problem before committing to one.
runtime_agnostic: true
invoked_by: [claude, codex, gemini, ollama]
activation:
  triggers: ["/dream", "dream up", "brainstorm", "what are our options"]
  nuclei: [N01, N02, N03, N07]
  depth: full
mirror_of: .claude/skills/dream.md
---

# dream — divergent ideation before convergence

Fight premature optimization of the solution space. Enumerate, compare, then let user pick.

## When to invoke

- User asks "what could we do about X?" / "how should we approach Y?".
- Problem has >=2 viable architectures.
- Stakes are high enough that picking wrong = multi-day rework.
- User is exploring, not executing.

## Protocol

1. **Frame**: restate problem in 1 sentence + explicit constraints (budget, time, must-preserve, must-avoid).
2. **Diverge**: 3-5 approaches, each differing in *fundamental mechanism* not parameters.
3. **Score each**:
   | Approach | Mechanism | Effort | Risk | Reversibility | Best-fit-when |
4. **Surface tradeoffs** user didn't ask about (perf vs clarity, build vs buy, now vs later).
5. **Recommend** one with WHY (1 sentence). Phrase as opinion, not decision.
6. **Stop** and wait. Do NOT start building.

## Anti-patterns

- 5 variants of the same idea -- reject and regenerate.
- Hiding a favorite -- be honest about bias.
- Analysis paralysis -- if all look identical, collapse to 2 and move on.

## Output cap

<= 200 words across all options. Use the table -- prose is noise here.

## After user picks

Hand off to `/plan` or `/build` with chosen approach. Do NOT implement inside `dream`.
