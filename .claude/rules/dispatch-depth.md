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
related:
  - bld_collaboration_kind
  - ctx_cex_new_dev_guide
  - spec_n07_bootstrap_context
  - bld_instruction_kind
  - skill
  - p01_ctx_cex_project
  - p03_sp_kind_builder
  - agent_card_engineering_nucleus
  - p01_kg_cex_system_architecture
  - spec_context_assembly
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
1. archetypes/builders/{kind}-builder/ (12 ISOs)
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

## External Context Section (PREFLIGHT_EXPANSION)

For kinds where `requires_external_context: true` in `.cex/kinds_meta.json`,
N07 runs Phase 0 (MCP gather) BEFORE dispatch and injects the result inline.
Nuclei receive rich external context without holding live MCP credentials.
Non-Claude runtimes (Codex, Gemini, Ollama) rely entirely on this section.

**When to include**: check `kinds_meta[kind]["requires_external_context"]`.
- `true` (~73 kinds, 25%): knowledge cards, competitive, benchmarks, landing pages
- `false` (~220 kinds, 75%): structural kinds (schema, agent, config, workflow)

**Format to append after `## Relevant artifacts`:
```markdown
## External Context (pre-compiled by N07 via MCP)
Source: fetch + github + markitdown  (gathered {ISO-8601-timestamp})
Budget: {tokens_used} / 8192 tokens

### Web Context: "{query}"
[up to 3 results, truncated to budget]

### GitHub Context
[relevant issues, PRs, or file snippets -- only for code-related kinds]
```

**Infrastructure:**
- Phase 0 module: `_tools/cex_preflight_mcp.py`
- Provider config: `.cex/config/preflight_sources.yaml` (free defaults + opt-in premium)
- Audit trail: `.cex/cache/preflight/{hash}_audit.json`
- N07 permissions: `.claude/nucleus-settings/n07.json` (GitHub read-only; mutations denied)
- Security policy: `_docs/specs/spec_mcp_security_policy.md`

Omit the section entirely for `requires_external_context: false` kinds.

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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_kind]] | related | 0.34 |
| [[ctx_cex_new_dev_guide]] | related | 0.32 |
| [[spec_n07_bootstrap_context]] | related | 0.31 |
| [[bld_instruction_kind]] | related | 0.31 |
| [[skill]] | related | 0.29 |
| [[p01_ctx_cex_project]] | related | 0.29 |
| [[p03_sp_kind_builder]] | related | 0.29 |
| [[agent_card_engineering_nucleus]] | related | 0.29 |
| [[p01_kg_cex_system_architecture]] | related | 0.28 |
| [[spec_context_assembly]] | related | 0.28 |
