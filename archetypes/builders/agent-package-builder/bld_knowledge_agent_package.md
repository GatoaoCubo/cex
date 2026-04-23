---
kind: knowledge_card
id: bld_knowledge_card_agent_package
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for agent_package production — portable agent bundle packaging
sources: Docker OCI spec, ISO 42001 AI management, HuggingFace Model Hub, agent packaging patterns
quality: 9.1
title: "Knowledge Card Agent Package"
version: "1.0.0"
author: n03_builder
tags: [agent_package, builder, examples]
tldr: "Golden and anti-examples for agent package construction, demonstrating ideal structure and common pitfalls."
domain: "agent package construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_agent_package
  - p03_sp_agent_package_builder
  - bld_config_agent_package
  - p10_lr_agent_package_builder
  - agent-package-builder
  - p01_kc_agent_package
  - p11_qg_agent_package
  - p02_iso_organization_agent
  - bld_schema_agent_package
  - bld_examples_agent_package
---

# Domain Knowledge: agent_package
## Executive Summary
agent packages are self-contained, portable, LLM-agnostic bundles that encapsulate an AI agent's complete operational context. Inspired by Docker images and ISO 42001 AI management systems, each package provides everything needed to instantiate an agent on any compatible runtime. They use a tiered file system with pillar-mapped contents and quality validation. agent packages differ from agent definitions (source), boot configs (provider-specific init), and spawn configs (orchestration params).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P02 (identity/model) |
| Frontmatter fields | 14 required + 5 recommended |
| Quality gates | 9 HARD + 10 SOFT |
| system_instruction max | 4096 tokens |
| Density minimum | >= 0.80 per file |
| Portability | Zero hardcoded paths |
| Entry point | manifest.yaml |
## Patterns
- **Tier system**: graduated completeness
| Tier | Files | Use case |
|------|-------|----------|
| minimal | 3 | Prototype, early development |
| standard | 7 | Production-ready deployment |
| complete | 10 | Full-featured with all extensions |
| whitelabel | 12 | Distributable, rebrandable |
- **Manifest-first**: manifest.yaml is the single entry point — everything discoverable from it
| Source | Concept | Application |
|--------|---------|-------------|
| Docker OCI | Layered manifest with image config | Tiered manifest.yaml |
| ISO 42001 | AI management documentation | Quality gates, audit trail |
| HuggingFace | Model card + weights + tokenizer | manifest + system_instruction + instructions |
| OpenAI GPTs | System prompt + knowledge + actions | system_instruction + instructions + input_schema |
- **LP mapping**: each file maps to a pillar — enables fractal navigation within the package
- **Token budgeting**: system_instruction.md capped at 4096 tokens to fit context windows across providers
- **Portability enforcement**: zero hardcoded paths guarantees cross-platform, cross-machine deployment
- **File inventory**: manifest lists all files with status (present/absent) for completeness audit
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Hardcoded paths in files | Package breaks on different machine/OS |
| system_instruction > 4096 tokens | Overflows context window; silently truncated |
| Missing manifest.yaml | No entry point; package is undiscoverable |
| Filler in files (density < 0.80) | Wastes token budget; low information value |
| Tier mismatch (claiming standard, missing files) | Audit failure; false completeness claim |
| LLM-specific instructions | Not portable; tied to one provider |
## Application
1. Select tier: minimal (3), standard (7), complete (10), or whitelabel (12)
2. Create manifest.yaml: list all files with LP mapping and status
3. Write system_instruction.md: <= 4096 tokens, LLM-agnostic
4. Ensure portability: grep for hardcoded paths; replace with relative
5. Verify density: every file >= 0.80 density — no filler
6. Validate: file count matches tier, manifest is complete, all files present
## References
- Docker OCI Image Spec: layered manifest and portability patterns
- ISO 42001:2023: AI management systems documentation standards
- HuggingFace Model Hub: model card and packaging conventions
- Agent packaging: portable agent distribution best forctices

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_agent_package]] | downstream | 0.54 |
| [[p03_sp_agent_package_builder]] | downstream | 0.48 |
| [[bld_config_agent_package]] | downstream | 0.45 |
| [[p10_lr_agent_package_builder]] | downstream | 0.45 |
| [[agent-package-builder]] | downstream | 0.45 |
| [[p01_kc_agent_package]] | sibling | 0.45 |
| [[p11_qg_agent_package]] | downstream | 0.44 |
| [[p02_iso_organization_agent]] | downstream | 0.40 |
| [[bld_schema_agent_package]] | downstream | 0.40 |
| [[bld_examples_agent_package]] | downstream | 0.38 |
