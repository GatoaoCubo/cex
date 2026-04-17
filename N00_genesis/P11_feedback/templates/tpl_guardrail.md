---
id: "p11_gr_{{SCOPE_SLUG}}"
kind: guardrail
pillar: P11
version: 1.0.0
title: Template - Guardrail
tags: [template, guardrail, safety, constraint, filter]
tldr: "Runtime safety check: prevents harmful or policy-violating output. Can modify, flag, or block."
quality: 9.0
updated: "2026-04-07"
domain: "feedback and quality"
author: n03_builder
created: "2026-04-07"
density_score: 0.95
---

# Guardrail: [NAME]

## Purpose
[WHAT this guardrail does]
## Configuration
```yaml
severity: [block | warn | modify]
applies_to: [all | kind_list | pillar_list]
enabled: true
```
## Rules
| Rule | Check | On Violation |
|------|-------|-------------|
| no_pii | Scan for email/phone | Block + redact |
| no_hallucination | Verify sources | Warn + flag |
| no_injection | Detect prompt inject | Block + log |
| max_length | Output <= limit | Truncate + warn |
| format_valid | Schema match | Block + retry |
## Implementation
```python
def guardrail(output, rules):
    for rule in rules:
        result = rule.check(output)
        if not result.passed and rule.severity == "block":

            return GuardrailResult(blocked=True)
    return GuardrailResult(blocked=False)
```
## Quality Gate
1. [ ] >= 2 rules defined
2. [ ] Severity per rule
3. [ ] Block rules prevent delivery
4. [ ] All checks < 100ms

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `guardrail` |
| Pillar | P11 |
| Domain | feedback and quality |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |
