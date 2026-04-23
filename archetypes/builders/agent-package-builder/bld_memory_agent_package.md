---
id: p10_lr_agent_package_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "agent packages with hardcoded absolute paths (/home/, C:\\, /Users/) fail portability checks and require rework. Tier declarations that do not match the actual file count are caught by validator but cause avoidable rework cycles. system_instruction.md files exceeding 4096 tokens create context overflow when loaded into agent sessions. LP mapping errors (inventing mappings not in the enum) cause routing failures downstream. File inventory tables missing the status column are rejected by the manifest validator."
pattern: "Scan for absolute paths before declaring portable:true — grep for /home/, /Users/, C:\\, records/ in all files. Tier must match file count exactly (3=minimal, 7=standard, 10=extended, 12=full). Token-budget system_instruction.md early in packaging (Phase 1) to avoid rework. LP mappings must come from the CONFIG.md enum, never invented. File inventory table must include all files with a status column."
evidence: "9 agent_package productions: 4 had hardcoded paths caught by portability scan. 3 had tier/file-count mismatches. 2 had system_instruction over 4096 tokens (one at 6200 tokens). LP mapping errors in 2 productions caused routing failures in downstream testing. File inventory missing status column in 3 early productions."
confidence: 0.75
outcome: SUCCESS
domain: agent_package
tags: [agent-package, portability, tier-compliance, llm-agnostic, manifest, packaging]
tldr: "Scan for absolute paths before portable:true. Tier must match file count exactly. Token-budget system_instruction early. LP mappings from enum only."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
keywords: [agent_package, portable, manifest, tier, lp_mapping, system_instruction, token_budget, file_inventory, hardcoded_paths]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Agent Package"
density_score: 0.90
llm_function: INJECT
related:
  - bld_instruction_agent_package
  - bld_manifest_memory_type
  - bld_knowledge_card_agent_package
  - p03_sp_agent_package_builder
  - p11_qg_agent_package
  - bld_schema_agent_package
  - bld_config_agent_package
  - agent-package-builder
  - bld_tools_agent
  - bld_output_template_builder
---
## Summary
agent packages make artifacts portable across environments and LLM providers. The two most common failures are hardcoded absolute paths (breaking portability) and tier/file-count mismatches (breaking validation). Both are detectable at authoring time with a two-step check: path scan and file count.
## Pattern
Packaging workflow — execute in this order:
1. **Manifest-first** - Create manifest.yaml before generating any other files. Declare tier, file count, and LP mappings before writing content.
2. **Token budget** - Count tokens in system_instruction.md immediately after drafting. Hard limit: 4096 tokens. If over, trim before continuing.
3. **Path scan** - Before declaring `portable: true`, grep all files for: `/home/`, `/Users/`, `C:\`, `records/`, `.claude/`. Replace any absolute path with a relative path or a [PLACEHOLDER].
4. **Tier compliance** - File count must match declared tier: minimal=3, standard=7, extended=10, full=12. Count actual files before finalizing manifest.
5. **LP mapping validation** - Every LP mapping must exist in the CONFIG.md LP Mapping Enum. Never invent new mappings.
6. **File inventory** - Table in manifest must list every file with columns: filename, description, status. Status column is required by validator.
LLM-agnostic design means: no model names in instructions, no API-specific syntax, no provider-specific tool names. Instructions describe capabilities and behavior, not implementation.
## Anti-Pattern
1. Absolute paths in any file — package fails portability check, requires full re-scan.
2. `tier: "standard"` with 4 files — mismatch, validator rejects.
3. Drafting system_instruction last without token budgeting — discovered at 6200 tokens, requires major trim.
4. Inventing LP mapping not in enum — routing failure in downstream systems.
5. File inventory table without status column — manifest validator rejects.
6. Starting from content files before manifest — file count and LP mappings defined ad-hoc, inconsistently.
## Context

## Builder Context

This ISO operates within the `agent-package-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Reference

```yaml
id: p10_lr_agent_package_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_agent_package_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | agent_package |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_agent_package]] | upstream | 0.46 |
| [[bld_manifest_memory_type]] | upstream | 0.41 |
| [[bld_knowledge_card_agent_package]] | upstream | 0.39 |
| [[p03_sp_agent_package_builder]] | upstream | 0.39 |
| [[p11_qg_agent_package]] | downstream | 0.37 |
| [[bld_schema_agent_package]] | upstream | 0.34 |
| [[bld_config_agent_package]] | upstream | 0.32 |
| [[agent-package-builder]] | upstream | 0.31 |
| [[bld_tools_agent]] | upstream | 0.31 |
| [[bld_output_template_builder]] | upstream | 0.29 |
