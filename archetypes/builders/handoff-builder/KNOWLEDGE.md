---
pillar: P01
llm_function: INJECT
purpose: Operational knowledge and patterns for handoff production
sources: P12 schema + CODEXA handoff patterns + STELLA dispatch
---

# Domain Knowledge: handoff

## Core Concept
`handoff` is the central delegation artifact in P12 orchestration.
It answers: "What should this satellite do, with what context, within what scope,
and how should it commit and signal completion?"

Handoffs are instructions, not events or routing rules.
They are consumed by satellite execution engines (STELLA dispatch).

## Minimum Semantic Contract
Every valid handoff carries:
- `satellite`: who executes
- `mission`: what project or campaign
- `autonomy`: how independently the satellite operates
- `quality_target`: minimum acceptable quality score

Plus 5 body sections: Context, Tasks, Scope Fence, Commit, Signal.
Plus standard CEX fields: id, kind, lp, version, dates, author, quality, tags, tldr.

## Autonomy Semantics
| Level | Meaning | Satellite behavior |
|-------|---------|-------------------|
| full | Satellite decides all implementation details | Maximum independence |
| supervised | Satellite executes but checks back on key decisions | Balanced guidance |
| assisted | Satellite follows precise instructions with minimal deviation | Strict execution |

## Body Section Patterns
- **Context**: 2-4 sentences explaining WHY this work is needed
- **Tasks**: numbered steps, each starting with an action verb
- **Scope Fence**: SOMENTE (allowed paths) + NAO TOQUE (forbidden paths)
- **Commit**: exact `git add` + `git commit -m` commands
- **Signal**: `signal_writer.write_signal()` call or file-based signal

## Boundary vs Nearby Types
| Type | What it is | Why it is not `handoff` |
|------|------------|------------------------|
| action_prompt | conversational prompt with persona and format | prompt engineering, not delegation |
| signal | atomic status event (complete/error/progress) | feedback, not instruction |
| dispatch_rule | keyword-to-satellite routing policy | routing, not execution detail |
| workflow | executable step graph with error handling | runtime engine, not one-shot brief |

Rule of thumb:
- "Do this work" -> `handoff`
- "Work is done" -> `signal`
- "Route this type of work to X" -> `dispatch_rule`

## Naming Pattern
P12 schema defines: `p12_ho_{task}.md`
Examples:
- `p12_ho_wave19_builders.md`
- `p12_ho_competitor_research.md`
- `p12_ho_deploy_api_v2.md`

## Operational Constraints
- Must stay under 4096 bytes
- Should be self-contained: satellite needs no external context
- Should be specific: no vague "do your best" instructions
- Must include scope fence to prevent satellite from touching wrong files
