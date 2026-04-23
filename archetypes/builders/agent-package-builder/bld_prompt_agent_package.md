---
kind: instruction
id: bld_instruction_agent_package
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for agent_package
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Agent Package"
version: "1.0.0"
author: n03_builder
tags: [agent_package, builder, examples]
tldr: "Golden and anti-examples for agent package construction, demonstrating ideal structure and common pitfalls."
domain: "agent package construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_agent_package
  - p03_sp_agent_package_builder
  - bld_config_agent_package
  - p10_lr_agent_package_builder
  - bld_knowledge_card_agent_package
  - p02_iso_organization_agent
  - p11_qg_agent_package
  - bld_examples_agent_package
  - bld_output_template_agent_package
  - agent-package-builder
---

# Instructions: How to Produce an agent_package
## Phase 1: RESEARCH
1. Identify the target agent by name and domain
2. Determine the tier based on delivery requirements:
   - minimal (3 files): manifest.yaml, system_instruction.md, instructions.md
   - standard (7 files): minimal + architecture.md, output_template.md, examples.md, error_handling.md
   - complete (10 files): standard + quick_start.md, input_schema.yaml, upload_kit.md
   - whitelabel (12 files): complete + upload_kit_whitelabel.md, branding_config.yaml
3. Verify all required files for the selected tier exist or can be produced
4. Check portability: no hardcoded paths (/home/, /Users/, C:\, records/), no provider-specific references, no internal project names in the instructions
5. Calculate the system_instruction token count — must be at or below 4096 tokens
6. Map each file to its pillar using the LP mapping (manifest=P02, system_instruction=P03, instructions=P03, architecture=P08, output_template=P05, examples=P07, error_handling=P11, quick_start=P01, input_schema=P06, upload_kit=P04)
7. Check existing agent_packages via brain_query [IF MCP] for the same agent — avoid duplicates
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all frontmatter fields and tier requirements
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints exactly
3. Fill frontmatter: 14 required fields + 5 recommended fields (null is acceptable for recommended)
4. Set quality: null — never self-score
5. Write manifest.yaml with all required fields: id, kind, tier, version, files inventory with LP mapping
6. Write the File Inventory section: one row per file with name / pillar / purpose / size
7. Write system_instruction.md as a composite document — must be at or below 4096 tokens
8. Write the Portability Checklist: confirm no absolute paths, no provider-specific references, no internal jargon in any file
9. Write the Tier Compliance section: declared tier, file count expected vs actual, list any gaps
10. Set files_count to match the actual number of files in the directory
11. Verify each individual file is within 4096 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — apply each gate manually
2. HARD gates (all must pass):
   - YAML in manifest.yaml parses without errors
   - id matches pattern `p02_iso_[a-z][a-z0-9_]+`
   - kind == agent_package
   - tier is one of: minimal, standard, complete, whitelabel
   - files_count matches actual file count in the directory
   - file count meets the tier minimum (minimal=3, standard=7, complete=10, whitelabel=12)
   - system_instruction.md is at or below 4096 tokens
   - manifest.yaml body is within 4096 bytes
   - quality == null
3. SOFT gates (score each against QUALITY_GATES.md):
   - LP mapping covers all included files
   - portability check passed — no hardcoded paths in any file
   - examples.md has at least 2 examples (if tier >= standard)
   - density >= 0.80 across all files
4. Cross-check scope boundaries:
   - portable self-contained bundle, not a bare agent definition (agent-builder)?
   - not a boot or runtime configuration (boot-config-builder)?
   - not a standalone system prompt (system-prompt-builder)?
   - no hardcoded paths in any file across the entire package?
5. If score < 8.0: revise files before outputting


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_agent_package]] | downstream | 0.49 |
| [[p03_sp_agent_package_builder]] | related | 0.47 |
| [[bld_config_agent_package]] | downstream | 0.44 |
| [[p10_lr_agent_package_builder]] | downstream | 0.43 |
| [[bld_knowledge_card_agent_package]] | upstream | 0.43 |
| [[p02_iso_organization_agent]] | upstream | 0.43 |
| [[p11_qg_agent_package]] | downstream | 0.41 |
| [[bld_examples_agent_package]] | downstream | 0.39 |
| [[bld_output_template_agent_package]] | downstream | 0.35 |
| [[agent-package-builder]] | upstream | 0.34 |
