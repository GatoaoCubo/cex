---
id: p03_ins_code_review
kind: instruction
pillar: P03
version: "1.0.0"
created: "2026-03-28"
updated: "2026-03-28"
author: "builder_agent"
title: "Instruction: Code Review Checklist"
target: "code-reviewer agent or human reviewer"
steps_count: 6
prerequisites:
  - "Code diff or PR available for review"
  - "Access to project's quality standards (CLAUDE.md or equivalent)"
validation_method: checklist
idempotent: true
atomic: false
rollback: null
dependencies:
  - "Source code repository access"
logging: true
domain: "code_review"
quality: 9.0
tags: [instruction, code-review, checklist, quality]
tldr: "6-step code review instruction: read diff, check correctness, security, style, tests, then produce structured verdict."
density_score: 0.90
related:
  - p01_kc_code_review
  - p02_agent_code_review
  - p03_sp_code_review
  - p12_wf_code_review
  - bld_instruction_output_validator
  - p04_tool_software_project
  - bld_instruction_context_doc
  - p12_wf_auto_security
  - bld_instruction_memory_scope
  - bld_instruction_retriever_config
---
## Prerequisites
- Code diff or pull request is available and accessible
- Reviewer has context on the project's conventions and quality standards
## Steps
1. **Read the full diff** — understand the change scope before reviewing individual lines
2. **Check correctness** — verify logic handles edge cases, null values, off-by-one errors, and race conditions
3. **Check security** — scan for injection (SQL/XSS/command), hardcoded secrets, unvalidated input at system boundaries
4. **Check style** — confirm naming conventions, import ordering, and formatting match project standards
5. **Check tests** — verify new/changed behavior has corresponding test coverage; flag untested paths
6. **Produce verdict** — output structured review: APPROVE, REQUEST_CHANGES, or COMMENT with specific line references
## Validation
- [ ] Every changed function has at least one test covering the change
- [ ] No hardcoded secrets or credentials in diff
- [ ] All review comments reference specific line numbers
- [ ] Verdict includes severity per finding (critical/major/minor/nit)
- [ ] Final outcome: structured review document with actionable findings
## Rollback
Not applicable — code review is read-only and idempotent.
## References
- OWASP Top 10 for security checks
- Project CLAUDE.md for style and convention rules

## Template Loading

```yaml
# This instruction is ISO 3 of 13 in the builder stack
loader: cex_skill_loader.py
injection_point: F3_compose
priority: high
```

```bash
# Verify instruction loads correctly
python _tools/cex_skill_loader.py --verify code_review
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_code_review]] | upstream | 0.31 |
| [[p02_agent_code_review]] | upstream | 0.29 |
| [[p03_sp_code_review]] | related | 0.26 |
| [[p12_wf_code_review]] | downstream | 0.24 |
| [[bld_instruction_output_validator]] | sibling | 0.22 |
| [[p04_tool_software_project]] | downstream | 0.21 |
| [[bld_instruction_context_doc]] | sibling | 0.20 |
| [[p12_wf_auto_security]] | downstream | 0.20 |
| [[bld_instruction_memory_scope]] | sibling | 0.20 |
| [[bld_instruction_retriever_config]] | sibling | 0.20 |
