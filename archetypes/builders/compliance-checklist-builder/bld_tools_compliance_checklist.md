---
kind: tools
id: bld_tools_compliance_checklist
pillar: P04
llm_function: CALL
purpose: Tools available for compliance_checklist production
quality: 8.7
title: "Tools Compliance Checklist"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [compliance_checklist, builder, tools]
tldr: "Tool registry for compliance checklist builder: CEX pipeline tools (compile, score, retrieve), file system ops (Read/Write/Edit/Glob/Grep), and domain-specific automation for compliance checklist for soc2, gdpr, hipaa, eu ai act audits."
domain: "compliance_checklist construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_audit_log
  - bld_tools_data_residency
  - bld_tools_edit_format
  - bld_tools_pricing_page
  - bld_tools_legal_vertical
  - bld_tools_onboarding_flow
  - bld_knowledge_card_compliance_checklist
  - bld_tools_roi_calculator
  - bld_tools_vad_config
  - bld_tools_prompt_optimizer
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compiles checklist artifact to .yaml | After each save |
| cex_score.py | Scores artifact against 5D quality dimensions | Post-production |
| cex_retriever.py | Retrieves similar checklists and regulatory KCs | During F3 INJECT |
| cex_doctor.py | Validates builder ISO completeness and structure | During F7 GOVERN |
| cex_hygiene.py | Enforces frontmatter rules and naming conventions | During F7 GOVERN |

## External References
- SOC2 Trust Services Criteria (AICPA TSC 2017)
- ISO/IEC 27001:2022 Annex A controls
- GDPR Articles 5-32 (controller obligations)
- HIPAA Security Rule 45 CFR Part 164

## CEX Pipeline Tools

| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile .md artifact to .yaml | After Write (F8) |
| cex_score.py | Peer-review quality scoring | After production (F7) |
| cex_retriever.py | Discover similar artifacts by TF-IDF | During F3 INJECT |
| cex_doctor.py | Health check builder ISOs | Before dispatch |

## Data Sources

| Source | Content | When to use |
|--------|---------|-------------|
| SCHEMA.md | Field definitions, ID pattern, constraints | Every production run |
| OUTPUT_TEMPLATE.md | Exact frontmatter + body structure | Every production run |
| QUALITY_GATES.md | H01-H08 HARD gates | Every validation run |
| KNOWLEDGE.md | Domain concepts for compliance checklist | When designing structure |
| MEMORY.md | Common mistakes, anti-patterns | When stuck or producing a variant |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Properties

| Property | Value |
|----------|-------|
| Kind | `tools` |
| Pillar | P04 |
| Domain | compliance checklist construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_audit_log]] | sibling | 0.51 |
| [[bld_tools_data_residency]] | sibling | 0.46 |
| [[bld_tools_edit_format]] | sibling | 0.33 |
| [[bld_tools_pricing_page]] | sibling | 0.29 |
| [[bld_tools_legal_vertical]] | sibling | 0.27 |
| [[bld_tools_onboarding_flow]] | sibling | 0.26 |
| [[bld_knowledge_card_compliance_checklist]] | upstream | 0.26 |
| [[bld_tools_roi_calculator]] | sibling | 0.26 |
| [[bld_tools_vad_config]] | sibling | 0.25 |
| [[bld_tools_prompt_optimizer]] | sibling | 0.24 |
