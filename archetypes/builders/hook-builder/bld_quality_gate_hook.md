---
id: p11_qg_hook
kind: quality_gate
pillar: P11
title: "Gate: Hook"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "hook — pre/post event interceptors for system lifecycle events"
quality: 9.0
tags: [quality-gate, hook, event, lifecycle, trigger, intercept]
tldr: "Gates ensuring hook artifacts define safe, scoped event interceptors with trigger configs, timeout, and error strategies."
density_score: 0.91
llm_function: GOVERN
---
# Gate: Hook
## Definition
| Field     | Value |
|-----------|-------|
| metric    | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool; 9.5 for golden |
| operator  | AND (all hard) + weighted average (soft) |
| scope     | any artifact with `kind: hook` |
## HARD Gates
All must pass. Any failure = immediate reject.
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error on any field |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | Uppercase, spaces, or leading digit |
| H03 | ID equals filename stem | `id: pre_tool` in file `post_stop.md` |
| H04 | Kind equals literal `hook` | Any other kind value |
| H05 | Quality field is `null` | Any non-null value |
| H06 | All required fields present | Missing: event, trigger, script_path, blocking, timeout_ms |
| H07 | `event` is one of: `PreToolUse`, `PostToolUse`, `Stop`, `Notification` | Arbitrary or invented event name |
| H08 | `timeout_ms` is a positive integer | Zero, negative, or non-integer |
| H09 | `script_path` is a relative path (no drive letters, no `~`) | Absolute path or home-relative path |
| H10 | `error_strategy` field present with valid value (`continue`, `abort`, `log`) | Missing or invalid strategy |
## SOFT Scoring
Total weights sum to 100%.
| ID  | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|-----|-----------|--------|--------|-------|-------|
| S01 | Trigger specificity | 1.0 | Event + matcher condition both defined (e.g., tool name pattern) | Event only, no matcher | No trigger config |
| S02 | Blocking behavior justified | 1.0 | `blocking: true/false` stated with rationale in description | Blocking stated, no rationale | Blocking field absent |
| S03 | Timeout apownteness | 1.0 | Timeout fits event type (PreToolUse < 5000ms, PostToolUse < 30000ms) | Timeout present but oversized | No timeout or zero |
| S04 | Script path resolvable | 1.0 | Path exists or clearly references known convention | Path plausibly correct | Path invented or ambiguous |
| S05 | Error strategy completeness | 0.5 | Strategy + fallback behavior + log target all specified | Strategy only | None |
| S06 | Condition guard | 1.0 | `conditions` field narrows hook scope (env var, file exists, etc.) | Condition present but vague | No condition — fires always |
| S07 | Environment injection | 0.5 | `env` fields documented if hook reads env vars | Env used but undocumented | Hook reads undocumented env |
| S08 | Idempotency | 1.0 | Hook behavior is safe to run multiple times per event | Likely idempotent but unverified | Clearly non-idempotent |
| S09 | Async safety | 0.5 | Async execution implications documented if `blocking: false` | Async used without notes | Blocking mismatch with behavior |
| S10 | Description actionability | 0.5 | Description states WHAT the hook does + WHY it exists | Either what or why present | Generic or empty description |
**Score = sum(pts * weight) / sum(max_pts * weight) * 10**
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Publish to pool as golden hook pattern |
| >= 8.0 | Skilled | Publish to pool + log pattern |
| >= 7.0 | Learning | Use but flag for improvement |
| < 7.0 | Rejected | Return to author with gate report |
## Bypass
| Field | Value |
|-------|-------|
| Conditions | Emergency incident hook needed immediately; trigger config incomplete due to unknown event schema |
| Approver | System owner only |
| Audit trail | `bypass_reason` field required in frontmatter |
| Expiry | 48 hours; hook must reach full compliance or be deactivated |
