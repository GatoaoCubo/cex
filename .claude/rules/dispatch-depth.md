---
glob: "**"
alwaysApply: true
description: "N07 must dispatch deep tasks that use the 1M context window, not shallow atomic tasks"
---

# Dispatch Depth Rule

## The Problem

Each nucleus has 1M token context. A simple task ("create 1 file") uses <1% of that capacity. This wastes the most powerful capability CEX has.

## The Rule

Every handoff N07 writes MUST include at least 3 of these depth amplifiers:

1. **Multi-artifact**: produce 2+ artifacts, not just 1
2. **Cross-reference**: read existing artifacts and reference them in output
3. **Research phase**: scan the codebase or knowledge library before producing
4. **Quality loop**: self-review against quality gate, revise if below 8.5
5. **Compile + verify**: compile output and run doctor/sanitize checks
6. **Memory injection**: load relevant KCs, examples, brand context into reasoning

## Examples

BAD (shallow, wastes 1M):
```
"Create deck_n05.md with your capabilities"
```

GOOD (deep, uses context):
```
"Scan your entire nucleus directory N05_operations/. Read all 34 artifacts.
Cross-reference with P01_knowledge/library/ for relevant KCs.
Create deck_n05.md that maps every capability. Then identify 3 gaps
where you have fewer artifacts than other nuclei. For each gap,
create the missing artifact following 8F pipeline. Compile all outputs.
Run cex_doctor.py and report results. Commit everything with detailed message."
```

## Measurement

A good handoff should result in:
- 3+ files created or modified
- 10+ tool calls (read, write, bash)
- 2+ minutes of work (not 30 seconds)
- git commit with substantive changes

If a nucleus completes in under 60 seconds, the task was too shallow.
