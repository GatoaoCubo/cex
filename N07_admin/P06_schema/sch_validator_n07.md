---
id: sch_validator_n07
kind: validator
pillar: P06
nucleus: n07
title: "Orchestrator Validation Rules"
version: 1.0
quality: 8.6
tags: [validator, orchestration, pre-dispatch, quality-gate, handoff]
rule: "N07 orchestration domain validation rules"
conditions:
  - field: "handoff_file"
    operator: "exists"
    value: true
    target: "body"
  - field: "nucleus"
    operator: "in"
    value: ["n01","n02","n03","n04","n05","n06"]
    target: "frontmatter"
error_message: "N07 validation failed. Check pre-dispatch, handoff, signal, consolidation, or mission gates. See Fail Action column for remediation."
severity: "error"
auto_fix: false
pre_commit: false
threshold: null
bypass:
  conditions: ["dry-run mode", "--dry-run flag passed to dispatch.sh"]
  approver: "n07-orchestrator"
  audit: true
logging: true
domain: "orchestration"
tldr: "Pass/fail rules for N07 dispatch, handoff quality, signal validation, consolidation gates, and mission pre-flight."
density_score: 0.91
---
<!-- 8F: F1=P06/validator F2=validator-builder F3=nucleus_def_n07+n07-orchestrator F4=reason F5=call F6=produce F7=govern F8=collaborate -->

## Purpose

Atomic pass/fail rules governing N07 orchestration lifecycle. Five validators cover
pre-dispatch readiness, handoff quality, incoming signal integrity, post-wave
consolidation, and mission pre-flight. Validators run in order; a hard failure at
any stage blocks the next stage.

## Severity Levels

| Level | Meaning                        | Blocks execution? |
|-------|--------------------------------|-------------------|
| hard  | Fatal -- do not proceed        | YES               |
| soft  | Warning -- flag, continue      | NO                |

---

## V1 -- Pre-Dispatch Validator

**Purpose:** Block dispatch before a nucleus boots with missing or malformed preconditions.
Catching failures here is free; catching them post-spawn costs a full nucleus boot (~30k tokens).

| # | Check                          | Input                              | Pass Condition                                   | Fail Action                            | Severity |
|---|--------------------------------|------------------------------------|--------------------------------------------------|----------------------------------------|----------|
| 1 | Handoff file exists            | `.cex/runtime/handoffs/{M}_{n}.md` | File exists, size > 0                            | Abort dispatch, write error to stderr  | hard     |
| 2 | Handoff frontmatter parseable  | handoff .md file                   | YAML block parses without error                  | Abort dispatch, log parse error        | hard     |
| 3 | Task file written               | `n0X_task.md` in repo root         | File exists and matches handoff id               | Create task file from handoff, retry   | hard     |
| 4 | Nucleus id is valid            | nucleus param                      | Value in {n01..n06}                              | Abort, log invalid nucleus id          | hard     |
| 5 | No orphan processes            | `.cex/runtime/pids/spawn_pids.txt` | No stale PID entries for target nucleus          | Run `dispatch.sh stop {nucleus}` first | hard     |
| 6 | Provider quota ok              | `nucleus_models.yaml` fallback     | At least one healthy provider in fallback chain  | Swap to alternate provider or abort    | hard     |
| 7 | Session ID unique              | `spawn_pids.txt`                   | No duplicate session_id for this dispatch        | Generate new session_id, log warning   | soft     |

---

## V2 -- Handoff Validator

**Purpose:** Ensure each handoff carries enough structured context for the nucleus to
operate at 1M-token depth without discovery turns. Shallow handoffs waste context budget.

| # | Check                          | Input            | Pass Condition                                              | Fail Action                              | Severity |
|---|--------------------------------|------------------|-------------------------------------------------------------|------------------------------------------|----------|
| 1 | Context refs section present   | handoff body     | Section `## Context` with >= 1 artifact path               | Regenerate handoff with context section  | hard     |
| 2 | Deliverables list present      | handoff body     | Section `## Expected output` with >= 1 file path            | Regenerate handoff with deliverables     | hard     |
| 3 | 8F trace markers present       | handoff body     | At least F1/F2/F3 referenced in body                       | Append 8F pointers to handoff            | soft     |
| 4 | Depth amplifiers >= 3          | handoff body     | At least 3 of: multi-artifact / cross-ref / research / quality-loop / compile+verify / memory-injection | Warn, do not block | soft     |
| 5 | No CLI arg task passing        | handoff header   | Task NOT passed as CLI arg (boot reads file, not arg)       | Rewrite task to n0X_task.md file         | hard     |
| 6 | GDP manifest reference present | handoff body     | If subjective decisions required: manifest path listed      | Run GDP before dispatch                  | hard     |
| 7 | Nucleus matches routing table  | handoff metadata | nucleus field maps to correct domain per routing table      | Log mismatch, suggest correct nucleus    | soft     |

---

## V3 -- Signal Validator

**Purpose:** Validate incoming completion signals before N07 acts on them.
A fabricated or malformed signal can trigger premature consolidation.

| # | Check                        | Input                                    | Pass Condition                                  | Fail Action                               | Severity |
|---|------------------------------|------------------------------------------|-------------------------------------------------|-------------------------------------------|----------|
| 1 | Signal file parseable        | `signal_*_*.json` in runtime/signals/    | JSON parses without error                       | Discard signal, log parse error           | hard     |
| 2 | Nucleus id matches expected  | signal.nucleus field                     | Matches a nucleus in active wave list           | Discard as stray signal                   | hard     |
| 3 | Quality score present        | signal.score field                       | Numeric value >= 0                              | Treat as unscored; flag for review        | soft     |
| 4 | Artifact paths exist on disk | signal.artifacts[] paths                 | Each path resolves to a real file               | Re-verify with `cex_doctor.py`            | hard     |
| 5 | Timestamp within window      | signal.timestamp                         | Within 3600s of dispatch timestamp              | Log stale signal, do not consolidate      | hard     |
| 6 | Git commit present           | git log since dispatch time              | At least 1 commit by the nucleus since dispatch | Do not treat as complete; investigate PID | hard     |
| 7 | Score meets floor            | signal.score                             | score >= 8.0                                    | Flag for quality review before merge      | soft     |

---

## V4 -- Consolidation Gate

**Purpose:** Final checks before N07 archives a wave, kills processes, and advances to
the next wave. A failed gate here prevents corrupted state from propagating forward.

| # | Check                          | Input                                  | Pass Condition                                  | Fail Action                                    | Severity |
|---|--------------------------------|----------------------------------------|-------------------------------------------------|------------------------------------------------|----------|
| 1 | All expected artifacts exist   | handoff deliverables list              | Every listed path exists on disk                | Re-dispatch missing artifacts                  | hard     |
| 2 | No artifact below quality floor| compiled artifacts in wave             | All scored artifacts have quality >= 8.0        | Re-dispatch artifact or accept with flag       | hard     |
| 3 | All signals received           | active wave nucleus list               | Signal present for every dispatched nucleus     | Wait or timeout; kill hung process tree        | hard     |
| 4 | No orphan processes            | `spawn_pids.txt` for session           | All wave PIDs have corresponding complete signal | Run `taskkill /F /PID {pid} /T` per orphan     | hard     |
| 5 | Signals archived               | `runtime/signals/` directory           | Processed signals moved to archive subfolder    | Archive before advancing wave                  | soft     |
| 6 | `cex_doctor.py` pass           | full repo state                        | Doctor exits 0                                  | Investigate failures before next wave          | soft     |
| 7 | Commit message format valid    | wave consolidation commit              | Message includes `[N0X]` prefix and wave label  | Amend commit message before pushing            | soft     |

---

## V5 -- Mission Validator

**Purpose:** Pre-mission checks before the first wave of any multi-nucleus dispatch.
N07 sin lens: Orchestrating Sloth -- validate upfront so no wave is ever re-run.

| # | Check                          | Input                                           | Pass Condition                                    | Fail Action                               | Severity |
|---|--------------------------------|-------------------------------------------------|---------------------------------------------------|-------------------------------------------|----------|
| 1 | GDP manifest exists            | `.cex/runtime/decisions/decision_manifest.yaml` | File exists if mission has subjective decisions   | Run GDP co-pilot before dispatch          | hard     |
| 2 | Wave plan has no circular deps | mission wave dependency graph                   | Topological sort succeeds with no cycles          | Rewrite wave plan; remove circular deps   | hard     |
| 3 | Budget within limits           | token + cost estimate                           | Estimated tokens <= approved budget               | Reduce scope or get explicit approval     | hard     |
| 4 | Handoffs written for wave 1    | `.cex/runtime/handoffs/` directory              | One handoff per nucleus in wave 1 exists          | Write missing handoffs before dispatch    | hard     |
| 5 | No active session collision    | `spawn_pids.txt`                                | No other N07 session running same mission         | Abort or coordinate with other N07        | hard     |
| 6 | Routing table coverage         | nucleus list in wave plan                       | Every nucleus maps to a valid domain in table     | Correct nucleus assignment before dispatch | soft    |
| 7 | Task files pre-written         | `n0X_task.md` files                             | All task files for wave 1 nuclei exist            | Write task files from handoffs            | hard     |

---

## Rationale

| Principle                     | Application                                                                  |
|-------------------------------|------------------------------------------------------------------------------|
| Fail fast, fail cheap         | V1 (pre-dispatch) blocks before spending any nucleus boot budget             |
| Single responsibility         | Each row checks exactly one condition -- no compound validators               |
| Tiered severity               | hard blocks forward progress; soft logs without blocking                     |
| Audit trail required          | All bypasses logged; no silent skips                                         |
| Deterministic pass/fail       | No weighted scoring -- that belongs to quality_gate (P11)                    |
| Orchestrating Sloth sin lens  | Pay validation cost upfront; avoid re-dispatching waves                      |

## References

1. `.claude/rules/n07-orchestrator.md` -- dispatch workflow, consolidate protocol
2. `.claude/rules/8f-reasoning.md` -- F7 GOVERN gates
3. `N00_genesis/P08_architecture/nucleus_def_n07.md` -- nucleus identity + sin lens
4. `.cex/kinds_meta.json` -- kind taxonomy (validator = P06)
5. `_tools/cex_doctor.py` -- health check tool called at consolidation gate

## Properties

| Property      | Value                          |
|---------------|--------------------------------|
| Kind          | validator                      |
| Pillar        | P06                            |
| Nucleus       | N07                            |
| Domain        | orchestration                  |
| Pipeline      | 8F (F1-F8)                     |
| Scorer        | cex_score.py                   |
| Compiler      | cex_compile.py                 |
| Quality target| 9.0+                           |
| Density target| 0.85+                          |
