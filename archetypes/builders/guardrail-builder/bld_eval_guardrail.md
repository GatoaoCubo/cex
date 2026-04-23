---
kind: quality_gate
id: p11_qg_guardrail
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of guardrail artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: guardrail"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, guardrail, safety, enforcement, security-boundary, P11]
tldr: "Validates guardrail artifacts: enforcement mode specificity, concrete violation examples, severity classification, and bypass policy."
domain: "guardrail — safety boundaries and enforcement policies applied to agents and artifacts"
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.94
related:
  - bld_instruction_guardrail
  - p10_lr_guardrail_builder
  - guardrail-builder
  - bld_architecture_guardrail
  - bld_examples_guardrail
  - p03_sp_guardrail_builder
  - bld_output_template_guardrail
  - bld_knowledge_card_guardrail
  - p11_qg_formatter
  - p11_qg_feature_flag
---

## Quality Gate

# Gate: guardrail
## Definition
| Field     | Value |
|-----------|-------|
| metric    | composite score across SOFT dimensions |
| threshold | >= 7.0 to publish; >= 9.5 for golden |
| operator  | weighted average after all HARD gates pass |
| scope     | all artifacts where `kind: guardrail` |
All HARD gates are AND-logic: one failure rejects the artifact regardless of SOFT score.
## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Any YAML syntax error |
| H02 | ID matches `^p11_gr_[a-z][a-z0-9_]+$` | Wrong format or namespace |
| H03 | ID equals filename stem (no extension) | Mismatch between id field and file name |
| H04 | Kind equals literal `guardrail` | Any other value |
| H05 | `quality` field is null | Any non-null value |
| H06 | Required fields present: id, kind, pillar, version, created, updated, author, severity, scope, enforcement, domain, quality, tags, tldr | Any missing field |
| H07 | `severity` is one of: `critical`, `high`, `medium`, `low` | Unlisted value; drives escalation routing |
| H08 | `enforcement` is one of: `block`, `warn`, `log` | Unlisted value; missing causes system no-op |
| H09 | `scope` defines where this guardrail applies (agent, artifact, pipeline, or all) | Scope absent; guardrail cannot be targeted |
| H10 | Rules section has >= 3 concrete, measurable restrictions | Fewer than 3 or rules are subjective |
## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| S01 | `tldr` <= 160 chars, names protected boundary and enforcement mode | 0.09 | Named=1.0, vague=0.3 |
| S02 | Tags list len >= 3, includes severity level keyword | 0.05 | Met=1.0, partial=0.5 |
| S03 | Violations section has >= 2 specific, concrete examples | 0.13 | 2+=1.0, 1=0.5, 0=0.0 |
| S04 | Enforcement action describes exact system response (not just "block") | 0.12 | Precise=1.0, generic "block"=0.3 |
| S05 | Detection method specified (pattern match, LLM judge, static rule, regex) | 0.11 | Specified=1.0, absent=0.0 |
| S06 | Severity classification justified with written rationale | 0.09 | Justified=1.0, bare label=0.2 |
| S07 | Bypass policy defined: who can override and under what conditions | 0.10 | Explicit=1.0, absent=0.0 |
| S08 | Audit trail requirement documented for violations | 0.09 | Documented=1.0, absent=0.0 |
| S09 | False-positive risk assessed with mitigation strategy | 0.09 | Assessed+mitigated=1.0, absent=0.0 |
| S10 | Boundary from `permission`, `law`, and `quality_gate` stated | 0.08 | All 3=1.0, 2=0.6, 1=0.3, 0=0.0 |
| S11 | No subjective language in rules ("be careful", "apownte", "reasonable") | 0.05 | Clean=1.0, subjective language found=0.0 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — reference artifact for guardrail calibration |
| >= 8.0 | PUBLISH — pool-eligible; enforcement, detection, and bypass documented |
| >= 7.0 | REVIEW — usable but detection method or false-positive risk missing |
| < 7.0  | REJECT — redo; likely no concrete violation examples or missing enforcement spec |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Severity is `low` or `medium` only AND guardrail blocks a critical production hotfix path |
| approver | Security lead; written sign-off required before bypass activates |
| audit trail | Required: security lead name, incident ID, timestamp, expected re-enable date |

## Examples

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
quality: 9.0
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
