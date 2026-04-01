---
id: "p11_gr_{{SCOPE_SLUG}}"
kind: guardrail
pillar: P11
version: 1.0.0
title: Template - Guardrail
tags: [template, guardrail, safety, constraint, filter]
tldr: "Runtime safety check: prevents harmful or policy-violating output. Can modify, flag, or block."
quality: 8.6
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
- [ ] >= 2 rules defined
- [ ] Severity per rule
- [ ] Block rules prevent delivery
- [ ] All checks < 100ms
