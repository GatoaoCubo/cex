---
kind: tools
id: bld_tools_audit_log
pillar: P04
llm_function: CALL
purpose: Tools available for audit_log production
quality: 8.7
title: "Tools Audit Log"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [audit_log, builder, tools]
tldr: "Tool registry for audit log builder: CEX pipeline tools (compile, score, retrieve), file system ops (Read/Write/Edit/Glob/Grep), and domain-specific automation for immutable audit log configuration for soc2 type ii compliance."
domain: "audit_log construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_compliance_checklist
  - bld_tools_data_residency
  - bld_tools_edit_format
  - audit-log-builder
  - bld_tools_pricing_page
  - bld_tools_ai_rmf_profile
  - bld_tools_legal_vertical
  - bld_tools_onboarding_flow
  - bld_tools_roi_calculator
  - bld_tools_vad_config
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compiles audit_log artifact to .yaml | After each save |
| cex_score.py | Scores artifact against 5D quality dimensions | Post-production |
| cex_retriever.py | Retrieves similar audit log specs and KCs | During F3 INJECT |
| cex_doctor.py | Validates builder ISO completeness and structure | During F7 GOVERN |
| cex_hygiene.py | Enforces frontmatter rules and naming conventions | During F7 GOVERN |

## External References
- SOC2 Type II Trust Service Criteria CC6.1, CC7.1, CC7.2
- ISO/IEC 27001:2022 Annex A.8.15 (logging)
- NIST SP 800-92 (Guide to Computer Security Log Management)
- AWS CloudTrail, Datadog Audit Trail, Splunk SIEM (implementation references)

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
| KNOWLEDGE.md | Domain concepts for audit log | When designing structure |
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
| Domain | audit log construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_compliance_checklist]] | sibling | 0.53 |
| [[bld_tools_data_residency]] | sibling | 0.42 |
| [[bld_tools_edit_format]] | sibling | 0.27 |
| [[audit-log-builder]] | downstream | 0.27 |
| [[bld_tools_pricing_page]] | sibling | 0.27 |
| [[bld_tools_ai_rmf_profile]] | sibling | 0.25 |
| [[bld_tools_legal_vertical]] | sibling | 0.25 |
| [[bld_tools_onboarding_flow]] | sibling | 0.24 |
| [[bld_tools_roi_calculator]] | sibling | 0.24 |
| [[bld_tools_vad_config]] | sibling | 0.23 |
