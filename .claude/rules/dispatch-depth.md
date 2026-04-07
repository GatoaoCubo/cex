---
glob: "**"
alwaysApply: true
description: "N07 must dispatch deep tasks that use the 1M context window, not shallow atomic tasks"
quality: 9.0
title: "Dispatch-Depth"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
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
"Create agent_card_n05.md with your capabilities"
```

GOOD (deep, uses context):
```
"Scan your entire nucleus directory N05_operations/. Read all 34 artifacts.
Cross-reference with P01_knowledge/library/ for relevant KCs.
Create agent_card_n05.md that maps every capability. Then identify 3 gaps
where you have fewer artifacts than other nuclei. For each gap,
create the missing artifact following 8F pipeline. Compile all outputs.
Run cex_doctor.py and report results. Commit everything with detailed message."
```

## Measurement

A good handoff should result in:
1. 3+ files created or modified
2. 10+ tool calls (read, write, bash)
3. 2+ minutes of work (not 30 seconds)
4. git commit with substantive changes

If a nucleus completes in under 60 seconds, the task was too shallow.

## Artifact References in Handoffs

Every handoff N07 writes MUST include a "## Context" section listing:

```markdown
## Context (pre-loaded for you)
Your agent card: {nucleus_dir}/agent_card_{nuc}.md (loaded in system prompt)

## Relevant artifacts (READ these before producing)
1. archetypes/builders/{kind}-builder/ (13 ISOs)
2. P01_knowledge/library/kind/kc_{kind}.md
3. P{xx}/{subdir}/tpl_{kind}.md (output template)
4. .claude/rules/{nuc}*.md (your rules)

## Expected output
1. File: {path}
2. Kind: {kind}
3. Frontmatter: standard (id, kind, title, version, quality: null, tags)
4. Format: structured data (tables > prose)
```

This eliminates discovery turns. The nucleus reads the handoff,
reads the referenced artifacts, and produces. No wandering.

## Properties

| Property | Value |
|----------|-------|
| Kind | `` |
| Pillar |  |
| Domain | CEX system |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
