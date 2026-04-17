---
kind: instruction
id: bld_instruction_kind
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for scaffolding a complete builder package
pattern: 4-phase pipeline (discover, reference, produce, validate)
quality: 9.2
title: "Instruction Kind Builder"
version: "1.0.0"
author: n03_builder
tags: [kind_builder, builder, instruction, meta-builder]
tldr: "4-phase process: discover kind metadata, load reference builder, produce 13 ISOs, validate package."
domain: "kind builder construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Instructions: How to Produce a Builder Package

## Phase 1: DISCOVER

1. Read `.cex/kinds_meta.json` -- locate the target kind entry
2. Extract metadata: pillar, description, naming pattern, max_bytes, core flag, llm_function, boundary
3. If boundary field exists, use it as the primary scope definition for the builder
4. Read `P{xx}/_schema.yaml` for the target kind's pillar -- understand sibling kinds
5. Read `P01_knowledge/library/kind/kc_{kind}.md` if it exists -- absorb domain knowledge
6. Identify 3-5 related kinds in the same pillar and adjacent pillars for boundary clarity
7. Check if `.claude/agents/{kind}-builder.md` already exists -- do not overwrite without cause

## Phase 2: REFERENCE

1. Select a reference builder from `archetypes/builders/` -- choose one in the same or adjacent pillar
2. Read ALL 13 ISOs of the reference builder to understand structural patterns
3. Note the frontmatter field patterns, body section structures, and content density
4. Read the reference builder's sub-agent file at `.claude/agents/{ref_kind}-builder.md`
5. Map which parts are kind-generic (keep structure) vs kind-specific (replace content)

## Phase 3: PRODUCE

For each of the 13 ISOs, in this order:

| Order | ISO | Key content to produce |
|-------|-----|----------------------|
| 1 | bld_manifest_{kind}.md | Identity, capabilities (6+), routing keywords, crew role |
| 2 | bld_schema_{kind}.md | Frontmatter fields table, ID pattern regex, body sections, constraints |
| 3 | bld_system_prompt_{kind}.md | Persona, 13 rules, knowledge boundary, output format |
| 4 | bld_instruction_{kind}.md | 3-phase process (research, compose, validate) with numbered steps |
| 5 | bld_output_template_{kind}.md | YAML frontmatter template + body sections with `{{vars}}` |
| 6 | bld_examples_{kind}.md | Golden example (passes all gates) + anti-example (shows failures) |
| 7 | bld_memory_{kind}.md | Domain patterns, anti-patterns, evidence, confidence scores |
| 8 | bld_tools_{kind}.md | Production tools table, data sources table, tool permissions |
| 9 | bld_quality_gate_{kind}.md | HARD gates (8-12) + SOFT dimensions (8-12), scoring actions |
| 10 | bld_knowledge_card_{kind}.md | Domain knowledge, industry patterns, spec table, references |
| 11 | bld_architecture_{kind}.md | Component inventory, dependency graph, boundary table |
| 12 | bld_collaboration_{kind}.md | Crew compositions, handoff protocol, builder dependencies |
| 13 | bld_config_{kind}.md | Naming conventions, file paths, size limits, runtime constraints |

Rules for all 13 files:
- YAML frontmatter with quality: null
- kind-specific content (not generic placeholders)
- Tables over prose wherever data is structured
- ASCII-only (no emoji, no smart quotes)
- Cross-reference the target kind's pillar schema and related kinds

Then produce:
- `.claude/agents/{kind}-builder.md` -- sub-agent definition referencing the 13 ISOs

## Phase 4: VALIDATE

1. Count files in `archetypes/builders/{kind}-builder/` -- must be exactly 13
2. Verify every file has parseable YAML frontmatter
3. Verify quality: null in all 13 files
4. Verify file naming matches `bld_{iso_type}_{kind}.md` pattern
5. Verify `.claude/agents/{kind}-builder.md` exists
6. Verify the golden example in bld_examples passes all HARD gates in bld_quality_gate
7. Verify bld_output_template's `{{vars}}` match bld_schema's required fields
8. Run `python _tools/cex_compile.py archetypes/builders/{kind}-builder/` if available
9. If any check fails, fix in the same pass before signaling completion
