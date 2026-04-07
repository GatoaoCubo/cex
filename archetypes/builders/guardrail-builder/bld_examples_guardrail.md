---
kind: examples
id: bld_examples_guardrail
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of guardrail artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: guardrail-builder
## Golden Example
INPUT: "Create guardrail para prevenir que agents executem comandos destrutivos no filesystem"
OUTPUT:
```yaml
id: p11_gr_destructive_commands
kind: guardrail
pillar: P11
title: "Guardrail: Destructive Commands"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
scope: "filesystem operations by agents"
severity: "critical"
enforcement: "block"
applies_to: [agent, skill, hook, daemon]
domain: "safety"
quality: null
tags: [guardrail, filesystem, destructive, safety, critical]
tldr: "Blocks rm -rf, format, DROP TABLE, and other destructive commands in agent execution"
density_score: 0.91
bypass_approver: "orchestrator"
remediation: "Review command, replace with safe alternative, re-submit"
linked_artifacts:
  primary: "p08_law_003"
  related: [p09_perm_agent_write, p11_qg_pre_commit]
## Definition
Prevents agents from executing filesystem or database commands that
cause irreversible data loss. Threat model: agent hallucination generates
destructive command; automated pipeline executes without human review.
## Rules
1. NEVER execute `rm -rf` on directories outside designated temp paths
2. NEVER execute `DROP TABLE`, `DROP DATABASE`, or `TRUNCATE` without explicit user confirmation
3. NEVER execute `git push --force` to main/master branches
4. NEVER execute `format`, `fdisk`, or disk-level operations
5. NEVER delete files matching `*.env`, `*.key`, `*.pem`, `credentials.*`
6. ALWAYS validate file paths against an allowlist before deletion
7. ALWAYS log every delete/destructive operation with timestamp and agent ID
## Violations
| Violation | Severity | Example |
|-----------|----------|---------|
| Recursive delete outside temp | critical | `rm -rf /home/user/projects/` |
| Force push to main | critical | `git push --force origin main` |
| Database drop without confirm | critical | `DROP TABLE users;` |
| Credential file deletion | high | `rm .env.production` |
| Unlogged file deletion | medium | `os.remove(path)` without audit log |
## Enforcement
| Check | Method | Trigger |
|-------|--------|---------|
| Command pattern matching | automated (regex on shell commands) | pre-execution hook |
| Path allowlist validation | automated (path prefix check) | pre-execution hook |
| Database DDL detection | automated (SQL parser) | pre-query hook |
| Audit log presence | automated (log file check) | post-execution hook |
## Bypass
- Conditions: emergency data recovery requiring destructive ops
- Approver: orchestrator (orchestrator level only)
- Audit: bypass logged with reason, agent ID, timestamp, and command in signal
## References
- OWASP LLM Top 10: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- CEX Law 003: "Never execute destructive operations without confirmation"
```
WHY THIS IS GOLDEN:
- quality: null (H06 pass)
- id matches p11_gr_ pattern (H02 pass)
- kind: guardrail (H04 pass)
- 20 frontmatter fields present (H08 pass)
- severity: "critical" valid enum (H07 pass)
- enforcement: "block" valid enum (H09 pass)
- 7 concrete, measurable rules (S03 pass)
- 5 violation examples with severity and concrete commands (S04 pass)
- 4 enforcement checks with method and trigger (S05 pass)
- Bypass section with approver and audit (S06 pass)
## Anti-Example
INPUT: "Make agents safe"
BAD OUTPUT:
```yaml
id: safety_guardrail
kind: guardrail
title: "Be Safe"
quality: 8.0
severity: "important"
enforcement: "stop"
## Rules
- Be careful with commands
- Don't do bad things
- Think before acting
## Bypass
Contact admin if needed.
```
FAILURES:
1. id: no p11_gr_ prefix -> H02 FAIL
2. pillar: missing -> H05 FAIL
3. quality: self-scored 8.0 instead of null -> H06 FAIL
4. severity: "important" not valid enum (must be critical/high/medium/low) -> H07 FAIL
5. enforcement: "stop" not valid enum (must be block/warn/log) -> H09 FAIL

## Golden Example 2 (Production — OpenClaude Action Reversibility)
INPUT: "Create guardrail that blocks irreversible actions without authorization"
OUTPUT: Reference artifact `P11_feedback/compiled/p11_gr_action_reversibility.yaml`

Key patterns:
1. **5-point blast radius checklist**: reversible? local? visible? destructive? authorized?
   Binary checklist — any "no" triggers block. No subjective judgment needed.
2. **Scope-limited authorization**: "Approving once does NOT authorize in all contexts."
   Prevents authorization creep.
3. **Root cause over shortcut**: "Do not use destructive actions as shortcuts. Fix root causes."
   Prevents agents from rm -rf'ing their way out of build errors.
4. **Enforcement: block** (not warn): Irreversible actions are blocked entirely, not just flagged.
5. **GDP integration**: Routes blocked actions to USER-scope decision in decision_manifest.yaml.

WHY THIS IS GOLDEN:
- Checklist is binary (yes/no), not subjective
- Severity is justified (HIGH because irreversible)
- Enforcement is the strongest available (block)
- Violations are concrete (rm -rf, force-push, DROP TABLE)
- Bypass policy requires explicit authorization + audit trail

## Golden Example 3 (Production — OpenClaude Cyber Risk)
INPUT: "Create guardrail for security boundary on tool-using agents"
OUTPUT: Reference artifact `P11_feedback/compiled/p11_gr_cyber_risk.yaml`

Key patterns:
1. **Dual-use tool handling**: Explicitly addresses tools that are both offensive and defensive
   (C2 frameworks, credential testing). Requires "clear authorization context."
2. **Enforcement: warn** (not block): Security context often needs nuance. Warn + request
   clarification rather than hard blocking legitimate pentesting.
3. **Short and dense**: Only 3 rules. Each covers a broad category. No redundancy.
