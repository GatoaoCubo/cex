---
id: p05_fmt_agent_markdown
kind: formatter
pillar: P05
title: "Formatter: Agent Markdown Response"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: knowledge_agent
format: markdown
quality: 9.1
tags: [formatter, markdown, agent, output]
tldr: "Canonical markdown formatter for agent responses — structured sections, tables, code blocks, quality score footer"
max_bytes: 4096
density_score: 0.88
source: organization-core/records/agents/*/iso_vectorstore/ISO_*_OUTPUT_TEMPLATE.md
linked_artifacts:
  schema: p06_is_quality_audit
related:
  - p05_rf_security_audit
  - p05_rf_builder_artifact
  - bld_schema_response_format
  - tpl_response_format
  - bld_examples_response_format
  - bld_schema_system_prompt
  - bld_knowledge_card_response_format
  - bld_schema_pitch_deck
  - p03_ins_response_format
  - bld_schema_integration_guide
---

# Formatter: Agent Markdown Response

## Purpose

Defines how organization agents format their markdown output. All ISO OUTPUT_TEMPLATE files follow this formatter. Ensures human-readable + machine-parseable outputs with consistent structure.

## Structure

```
[HEADER: identity + metadata]
[EXECUTIVE SUMMARY: tldr + key_findings]
[BODY: domain-specific sections]
[ARTIFACTS: code blocks, tables, YAML]
[QUALITY FOOTER: score + confidence]
```

## Section Rules

| Section | Required | Format | Max Lines |
|---------|----------|--------|-----------|
| Header | yes | YAML frontmatter | 15 |
| Executive Summary | yes | 2-3 bullet points | 5 |
| Body | yes | H2/H3 headers + tables | variable |
| Code blocks | if applicable | fenced ``` with lang tag | variable |
| Quality Footer | yes | `Score: X.X | Confidence: TX` | 3 |

## Formatting Rules

1. **Tables**: Use for structured comparisons, inventories, route lists
2. **Code blocks**: Always tag language (`python`, `yaml`, `bash`, `json`)
3. **Emphasis**: `**bold**` for critical findings, `` `inline code` `` for paths/values
4. **Headers**: H1 = title, H2 = major section, H3 = subsection — max 3 levels
5. **No emoji**: Unless explicitly requested by user

## Valid Example

```markdown
# Security Audit: FastAPI Auth Routes

## Executive Summary
- 3 critical findings (CWE-306, CWE-862, CWE-284)
- 5 routes missing authentication middleware
- Estimated remediation: 2h

## Findings

| ID | Severity | CWE | Route |
|----|----------|-----|-------|
| F001 | CRITICAL | CWE-306 | DELETE /users/:id |
| F002 | HIGH | CWE-862 | GET /admin/stats |

---
Score: 9.2 | Confidence: T1 | Agent: access_control_auditor v1.0
```

## Invalid Example

```markdown
# audit results
found some issues with auth. you should fix them.
route1 has problem, route2 also bad
```
// FAILS: no structure, no severity, no actionable data

## Error Handling

| Condition | Action |
|-----------|--------|
| Empty body section | Return `## Body\n_No data available_` — never omit section |
| Code > 4096 bytes | Truncate at last complete block + `[truncated — see full output]` |
| Non-ASCII in output | Normalize to UTF-8 or ASCII equivalent |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p05_rf_security_audit]] | related | 0.45 |
| [[p05_rf_builder_artifact]] | related | 0.27 |
| [[bld_schema_response_format]] | downstream | 0.23 |
| [[tpl_response_format]] | related | 0.23 |
| [[bld_examples_response_format]] | downstream | 0.22 |
| [[bld_schema_system_prompt]] | downstream | 0.21 |
| [[bld_knowledge_card_response_format]] | related | 0.21 |
| [[bld_schema_pitch_deck]] | downstream | 0.20 |
| [[p03_ins_response_format]] | related | 0.20 |
| [[bld_schema_integration_guide]] | downstream | 0.19 |
