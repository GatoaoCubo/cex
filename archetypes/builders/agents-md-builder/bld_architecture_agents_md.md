---
kind: architecture
id: bld_architecture_agents_md
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of agents_md -- inventory, dependencies
quality: 9.0
title: "Architecture Agents Md"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [agents_md, builder, architecture]
tldr: "Component map of agents_md -- inventory, dependencies"
domain: "agents_md construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_app_directory_entry
  - bld_architecture_api_reference
  - bld_architecture_benchmark_suite
  - bld_architecture_legal_vertical
  - bld_architecture_roi_calculator
  - bld_architecture_quickstart_guide
  - bld_architecture_fintech_vertical
  - bld_architecture_churn_prevention_playbook
  - bld_architecture_healthcare_vertical
  - bld_architecture_memory_benchmark
---

## Component Inventory
| ISO Name              | Role                              | Pillar | Status  |
|-----------------------|-----------------------------------|--------|---------|
| bld_manifest          | Builder identity + routing        | P05    | Active  |
| bld_instruction       | 3-phase build pipeline            | P03    | Active  |
| bld_system_prompt     | LLM persona and rules             | P03    | Active  |
| bld_schema            | Frontmatter + ID contract         | P06    | Active  |
| bld_quality_gate      | HARD/SOFT validation              | P11    | Active  |
| bld_output_template   | AGENTS.md skeleton with vars      | P05    | Active  |
| bld_examples          | Golden + anti-example pair        | P07    | Active  |
| bld_knowledge_card    | AAIF spec + 60K-projects corpus   | P01    | Active  |
| bld_architecture      | This component map                | P08    | Active  |
| bld_collaboration     | Crew handoffs                     | P12    | Active  |
| bld_config            | Naming, paths, limits             | P09    | Active  |
| bld_memory            | Learned patterns                  | P10    | Active  |
| bld_tools             | CLI + validator bindings          | P04    | Active  |

## Dependencies
| From                | To                    | Type         |
|---------------------|-----------------------|--------------|
| bld_manifest        | bld_config            | configuration|
| bld_instruction     | bld_system_prompt     | dependency   |
| bld_output_template | bld_schema            | dependency   |
| bld_quality_gate    | bld_examples          | validation   |
| bld_collaboration   | bld_memory            | coordination |
| bld_tools           | Codex CLI / Aider     | integration  |

## Architectural Position
agents_md serves as the coding-agent onboarding surface within CEX P05. It is the standardized, vendor-neutral manifest read by every AAIF-compliant agent (Codex CLI, Claude Code, Aider, Cursor, goose) on repo entry, sitting at project-root alongside README.md and complementing vendor-specific CLAUDE.md / .cursorrules without replacing them.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_app_directory_entry]] | sibling | 0.73 |
| [[bld_architecture_api_reference]] | sibling | 0.71 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.71 |
| [[bld_architecture_legal_vertical]] | sibling | 0.71 |
| [[bld_architecture_roi_calculator]] | sibling | 0.71 |
| [[bld_architecture_quickstart_guide]] | sibling | 0.69 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.69 |
| [[bld_architecture_churn_prevention_playbook]] | sibling | 0.69 |
| [[bld_architecture_healthcare_vertical]] | sibling | 0.68 |
| [[bld_architecture_memory_benchmark]] | sibling | 0.68 |
