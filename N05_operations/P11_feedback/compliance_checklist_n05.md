---
id: p11_cc_n05_operations
kind: compliance_checklist
pillar: P11
title: "Compliance Checklist: N05 Operations"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: n05_operations
domain: operational-compliance
regulatory_scope: CEX operational standards (8F, ASCII rule, git hygiene, process management)
audit_frequency: per-commit
compliance_status: approved
review_cycle: biannual
responsible_team: N05_operations
quality: 9.1
tags: [compliance_checklist, n05, operations, release-gate, 8F, security, git-hygiene]
tldr: "N05 Gating Wrath release gate: 40 verifiable checks across 8 categories before any release or deployment."
related:
  - p12_wf_auto_review
  - p11_qg_admin_orchestration
  - p12_wf_auto_security
  - status
  - p01_kc_cex_orchestration_architecture
  - p01_kc_orchestration_best_practices
  - p01_fse_meta_builder_recipe
  - ctx_cex_new_dev_guide
  - p12_wf_auto_health
  - p11_qg_knowledge
---

## Scope

N05 (Gating Wrath) runs these checks before any release, deployment, or major operation.
`B`=blocking (halt pipeline) | `W`=warning (flag, log, continue)
`C`=per-commit | `S`=per-session | `K`=weekly

## Master Checklist

| id | category | check | command | pass | sev | freq |
|----|----------|-------|---------|------|-----|------|
| CQ01 | Code Quality | No non-ASCII in .py | `cex_sanitize.py --check --scope _tools/` | exit 0 | B | C |
| CQ02 | Code Quality | No non-ASCII in .ps1 | `cex_sanitize.py --check --scope boot/` | exit 0 (BOM ok) | B | C |
| CQ03 | Code Quality | No non-ASCII in .sh | `cex_sanitize.py --check --scope _spawn/` | exit 0 | B | C |
| CQ04 | Code Quality | No emoji in print/log | `grep -Prn "[^\x00-\x7F]" --include="*.py" _tools/` | 0 matches | B | C |
| CQ05 | Code Quality | Em-dash/smart-quotes replaced | `cex_sanitize.py --check --scope .` | exit 0 | W | C |
| AQ01 | Artifact | Required frontmatter on all artifacts | `cex_doctor.py --check frontmatter` | 0 violations | B | S |
| AQ02 | Artifact | quality: null (never self-scored) | `grep -rn "^quality:" N05_operations/ \| grep -v "null"` | 0 non-null | B | S |
| AQ03 | Artifact | density_score >= 0.85 | `cex_doctor.py --check density` | all >= 0.85 | W | S |
| AQ04 | Artifact | Naming matches kind pattern | `cex_hygiene.py --check naming` | 0 violations | B | S |
| AQ05 | Artifact | No duplicate IDs within pillar | `cex_doctor.py --check ids` | 0 duplicates | B | S |
| PC01 | Pipeline | 8F trace present (F1-F8) | Review build log for F1..F8 markers | All 8 present | B | S |
| PC02 | Pipeline | F7 GOVERN not skipped | Review log for "F7 GOVERN" line | Entry present | B | C |
| PC03 | Pipeline | compile ran after artifact save | `cex_compile.py --check {path}` | compiled/ newer | B | C |
| PC04 | Pipeline | cex_doctor passes on modified pillar | `cex_doctor.py` | 0 FAIL | W | S |
| PC05 | Pipeline | Builder ISOs complete (13/kind) | `cex_doctor.py --check builders` | 13 per kind | B | S |
| SE01 | Security | No API keys/secrets in artifacts | `grep -rn "api_key\|secret\|password" --include="*.md" .` | 0 matches | B | C |
| SE02 | Security | No secrets in git history | `git log --all -- "*.env" "*.key"` | 0 paths | B | C |
| SE03 | Security | N05 does not write to N01-N04 dirs | `git diff --name-only HEAD \| grep "^N0[1234]"` | 0 matches | B | C |
| SE04 | Security | .env files gitignored | `git check-ignore .env .env.local .env.production` | all matched | B | S |
| SE05 | Security | No secrets in compiled/ output | `grep -rn "password\|secret\|api_key" compiled/` | 0 matches | B | S |
| PM01 | Process Mgmt | No orphan processes from prior session | `dispatch.sh status` | All PIDs expected | B | S |
| PM02 | Process Mgmt | PID file current (no stale entries) | Check `.cex/runtime/pids/spawn_pids.txt` | all < 24h | W | S |
| PM03 | Process Mgmt | Session-aware stop used | Review last stop command | `dispatch.sh stop` confirmed | B | S |
| PM04 | Process Mgmt | Task files cleaned after dispatch | `ls n0*_task.md 2>/dev/null` | 0 stale files | W | S |
| PM05 | Process Mgmt | Kill uses taskkill /T (tree-kill) | Review kill commands in log | `/T` flag confirmed | B | S |
| SI01 | Signals | All dispatched nuclei signaled complete | `ls .cex/runtime/signals/*_complete_*.json \| wc -l` | count == dispatched | B | S |
| SI02 | Signals | No phantom signals | Cross-ref signals vs spawn_pids.txt | Every signal has known PID | B | S |
| SI03 | Signals | Signal score in range 0-10 | Parse signal JSON, check score field | 0 out-of-range | W | S |
| SI04 | Signals | Signals archived post-consolidation | `ls .cex/runtime/signals/*.json \| wc -l` | 0 unarchived | W | S |
| SI05 | Signals | No duplicate signals (nucleus+session) | Check filenames for repeated combos | 0 duplicates | W | S |
| GH01 | Git | Commits follow [N0X] prefix format | `git log --oneline -20 \| grep -v "\[N0[0-7]\]"` | 0 non-conforming | W | C |
| GH02 | Git | No force-push to main | Review push history | No rewritten main | B | C |
| GH03 | Git | No --no-verify hook bypass | Review recent commits | 0 --no-verify uses | B | C |
| GH04 | Git | No .env/.key/.pem staged | `git diff --staged --name-only \| grep -E "\\.env\|\\.key"` | 0 sensitive staged | B | C |
| GH05 | Git | git status clean after wave | `git status --short` | 0 unexpected changes | W | S |
| DO01 | Docs | CLAUDE.md matches nucleus_models.yaml | Diff routing vs `.cex/config/nucleus_models.yaml` | 0 discrepancies | W | K |
| DO02 | Docs | 13 ISOs complete per builder kind | `cex_doctor.py --check builders` | 0 incomplete sets | B | K |
| DO03 | Docs | N05 agent card present and < 30d old | `ls N05_operations/agent_card_n05.md` + updated field | exists, <= 30d | W | K |
| DO04 | Docs | Pillar schemas for all 12 pillars | Check `N00_genesis/P*/_schema.yaml` count | 12 present | W | K |
| DO05 | Docs | kinds_meta.json count matches builders | Compare `.cex/kinds_meta.json` vs `archetypes/builders/` | diff <= 2 | W | K |

---

## Corrective Actions

| sev | action | sla |
|-----|--------|-----|
| B | Halt pipeline. Fix violation, re-run check before proceeding. | Same session |
| W | Log in session summary. Dispatch may continue. | Next session |

## Reporting

Per-run record: `{nucleus}_{YYYYMMDD}_{session_id}`, checks_run, B-pass/fail,
W-pass/fail, failed_ids, corrective_actions_taken, auditor.
Retain 24 months or repo lifetime in `.cex/runtime/decisions/`.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_auto_review]] | downstream | 0.32 |
| [[p11_qg_admin_orchestration]] | related | 0.27 |
| [[p12_wf_auto_security]] | downstream | 0.25 |
| [[status]] | upstream | 0.25 |
| [[p01_kc_cex_orchestration_architecture]] | upstream | 0.25 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.23 |
| [[p01_fse_meta_builder_recipe]] | upstream | 0.22 |
| [[ctx_cex_new_dev_guide]] | related | 0.22 |
| [[p12_wf_auto_health]] | downstream | 0.21 |
| [[p11_qg_knowledge]] | related | 0.21 |
