---
name: dream
description: Generate 3-5 divergent approaches to a problem before committing to one. Use when user says "dream", "/dream", "brainstorm", or the problem is ill-specified / has multiple valid architectures.
---

# dream — divergent ideation before convergence

Fight premature optimization of the solution space. Enumerate, compare, then let user pick.

## When to invoke

- User asks "what could we do about X?" / "how should we approach Y?".
- Problem has ≥2 viable architectures.
- Stakes are high enough that picking wrong = multi-day rework.
- User is exploring, not executing.

## Protocol

1. **Frame**: restate the problem in 1 sentence + explicit constraints (budget, time, must-preserve, must-avoid).
2. **Diverge**: generate 3-5 approaches. Each must differ in *fundamental mechanism*, not just parameters.
3. **Score each**:
   | Approach | Mechanism | Effort | Risk | Reversibility | Best-fit-when |
4. **Surface tradeoffs** the user didn't ask about (perf vs clarity, build vs buy, now vs later).
5. **Recommend** one, with WHY (1 sentence) — but phrase as opinion, not decision.
6. **Stop** and wait for user choice. Do NOT start building.

## Anti-patterns

- 5 variants of the same idea. Reject and regenerate.
- Hiding a favorite option — be honest about bias.
- Analysis paralysis: if all 5 look identical in the table, collapse to 2 and move on.

## Output cap

≤ 200 words across all 5 options combined. Use the comparison table — prose is noise here.

## After user picks

Hand off to `/plan` or `/build` with the chosen approach as input. Do NOT implement inside `dream`.
