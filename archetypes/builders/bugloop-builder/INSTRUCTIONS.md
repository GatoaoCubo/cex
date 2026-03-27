---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for bugloop
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a bugloop

## Phase 1: RESEARCH
1. Identify the scope: what system, module, or pipeline does this bugloop monitor?
2. Identify the failure class: what KNOWN failure signature triggers this loop?
3. brain_query [IF MCP]: search P11_feedback/examples/ for existing bugloops in same domain
4. Determine detect.method: is the signal from static analysis, test failure, runtime trace, or log scan?
5. Determine detect.trigger: when does detection run (on_commit, on_deploy, scheduled, continuous)?
6. Determine fix.strategy: based on failure class risk (patch_and_retry / rollback_first / isolate_then_fix)
7. Calibrate confidence: use KNOWLEDGE.md table — do NOT inflate confidence for non-deterministic failures
8. Determine cycle_count: how many retry cycles before escalation is acceptable for this domain?
9. Identify escalation.target: who or what system receives the escalation payload?
10. Determine rollback need: is rollback required given the fix strategy and domain risk?

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all required fields
2. Read OUTPUT_TEMPLATE.md — fill following SCHEMA field names and types exactly
3. Set id: p11_bl_{scope_slug} — id MUST equal filename stem
4. Set kind: bugloop, pillar: P11, quality: null (never self-score)
5. Fill detect object: method + trigger + pattern (concrete regex or named signature)
6. Fill fix object: strategy + auto_fix boolean + max_attempts (must be <= cycle_count)
7. Fill verify object: test_suite path + assertions list (>= 1) + timeout in seconds
8. Set cycle_count: max iterations before escalation fires
9. Set auto_fix at root level: MUST match fix.auto_fix exactly
10. Fill escalation object: threshold (<= cycle_count) + target (named system or role)
11. Set confidence: calibrated float 0.0-1.0 per KNOWLEDGE.md table
12. Set test_suite at root level: canonical path or name of verification suite
13. Fill rollback object: enabled boolean + strategy (git_revert/snapshot_restore/blue_green)
14. Write ## Detection section: describe triggers, pattern, and signal sources
15. Write ## Fix Strategy section: describe auto vs manual rationale and strategy choice
16. Write ## Verification section: describe suite, pass criteria, timeout policy
17. Write ## Escalation section: describe threshold logic and payload content
18. Write ## Rollback section: describe trigger conditions and procedure

## Phase 3: VALIDATE
1. Check against QUALITY_GATES.md — 14 HARD gates must all pass
2. HARD: id format p11_bl_*, kind==bugloop, pillar==P11, quality==null
3. HARD: detect has method+trigger+pattern, fix.max_attempts integer 1-10
4. HARD: cycle_count >= fix.max_attempts, escalation.threshold <= cycle_count
5. HARD: confidence float 0.0-1.0, auto_fix root == fix.auto_fix
6. HARD: verify.assertions non-empty, rollback has enabled+strategy
7. INVARIANT: if auto_fix==true and confidence < 0.7 — REJECT (unsafe)
8. INVARIANT: if rollback.enabled==false and fix.strategy==rollback_first — REJECT (contradiction)
9. SOFT: all 5 body sections present, tldr < 160 chars, tags >= 3 with "bugloop"
10. If any HARD gate fails: fix before outputting
11. If score < 8.0: revise before outputting
