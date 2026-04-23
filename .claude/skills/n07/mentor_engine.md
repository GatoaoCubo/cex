---
id: skill_mentor_engine
kind: instruction
pillar: P12
title: "Mentor Engine Orchestration"
version: 1.0.0
author: n07_orchestrator
created: 2026-04-19
tags: [mentor, orchestration, teaching, media, lenses]
tldr: "N07 routing logic for /mentor subcommands: lens selection, mode detection, media dispatch."
density_score: 0.90
quality: 8.9
related:
  - bld_schema_lens
  - bld_architecture_lens
  - lens-builder
  - p03_sp_lens_builder
  - p11_qg_lens
  - p03_ins_lens
  - bld_memory_lens
  - p01_kc_lens
  - bld_output_template_lens
  - bld_knowledge_card_lens
updated: "2026-04-22"
---

# Mentor Engine -- N07 Orchestration Layer

## When This Fires

This skill activates when the user invokes `/mentor` with any subcommand.
It handles routing, context assembly, and media dispatch.

## Routing Table

| Subcommand | Handled by | Needs N05? | Needs lens KC? |
|------------|-----------|-----------|---------------|
| explain | N07 in-session | No | Yes |
| quiz | N07 in-session | No | Yes |
| translate | N07 in-session | No | Yes |
| reverse | N07 in-session | No | Yes (all 4) |
| journey | N07 in-session | No | Yes + concept graph |
| produce | N05 dispatch | Yes | Yes |
| (legacy) | N07 in-session | No | Optional |

## Context Assembly (F3 INJECT for mentor)

For every /mentor invocation, load in this order:

1. **Core vocabulary**: `N00_genesis/boot/mentor_context.md` (448 lines, always)
2. **Lens KC**: `N04_knowledge/P01_knowledge/kc_lens_{lens}.md` (selected lens)
3. **Lens index**: `N04_knowledge/P01_knowledge/kc_lens_index.md` (cross-reference)
4. **Language locale**: `N04_knowledge/P03_prompt/mentor_locale_{lang}.md`
5. **Teaching template**: based on subcommand:
   - explain: `mentor_storyteller.md`
   - quiz: `mentor_socratic.md`
   - journey: `mentor_journey.md` + `kc_concept_graph.md`
6. **Bilingual terms**: `N04_knowledge/P01_knowledge/kc_bilingual_term_map.md` (if lang=both)

## Lens Selection Logic

```
if --lens flag provided:
    use that lens
elif user has used a lens before in this session:
    reuse the same lens (consistency)
elif user is a beginner (first /mentor call):
    default to factory (most intuitive)
elif concept is about architecture:
    suggest city lens
elif concept is about pipeline/process:
    suggest factory lens
elif concept is about growth/evolution:
    suggest biology lens
elif concept is about interaction/roles:
    suggest game lens
```

## Media Dispatch (produce subcommand only)

When user runs `/mentor produce`:

1. Parse: concept, format, lang, lens
2. Check: does `_tools/cex_media_produce.py` exist?
   - Yes: run it directly via Bash
   - No: generate text output in-session, warn about missing pipeline
3. For NotebookLM formats (audio, video):
   - Check: is NotebookLM MCP available? (`notebooklm` in .mcp.json, not disabled)
   - Yes: include in produce command
   - No: skip audio/video, produce text + ppt only
4. Report output paths to user

## Session Memory

Track within the session (not persisted):
- Which concepts have been explained (avoid repetition)
- Which lens the user prefers (sticky within session)
- Which language the user is using (auto-detect from their messages)
- Learning progress: beginner -> intermediate -> advanced (based on concepts covered)

## Integration with /build

If during a /mentor session the user wants to build something:
```
User: "ok now I want to actually create one of those"
N07: Switches from mentor mode to build mode.
     The lens context stays loaded -- build output references the metaphor.
     "Great -- let's build it. /build knowledge_card about X"
```

## Integration with infoproducts

/mentor produce is the content factory for the monetization strategy:
- Each `produce --format all --lang both` generates a complete teaching module
- Modules accumulate in `_output/mentor/` organized by concept
- A course is a curated journey + produced modules for each step
- The repo literally teaches itself to strangers through its own tools

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_lens]] | upstream | 0.39 |
| [[bld_architecture_lens]] | upstream | 0.38 |
| [[lens-builder]] | upstream | 0.35 |
| [[p03_sp_lens_builder]] | upstream | 0.34 |
| [[p11_qg_lens]] | upstream | 0.33 |
| [[p03_ins_lens]] | sibling | 0.32 |
| [[bld_memory_lens]] | upstream | 0.30 |
| [[p01_kc_lens]] | upstream | 0.29 |
| [[bld_output_template_lens]] | upstream | 0.28 |
| [[bld_knowledge_card_lens]] | upstream | 0.28 |
