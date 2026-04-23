---
kind: quality_gate
id: p11_qg_hook
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of hook artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: Hook"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, hook, event, lifecycle, trigger, intercept]
tldr: "Gates ensuring hook artifacts define safe, scoped event interceptors with trigger configs, timeout, and error strategies."
domain: "hook — pre/post event interceptors for system lifecycle events"
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.91
related:
  - bld_instruction_hook
  - bld_architecture_hook
  - p03_sp_hook_builder
  - bld_examples_hook
  - bld_knowledge_card_hook
  - p04_hook_NAME
  - bld_schema_hook
  - hook-builder
  - p11_qg_input_schema
  - hook-config-builder
---

## Quality Gate

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

## Examples

# Examples: hook-builder
## Golden Example
INPUT: "Create a hook that tracks tool usage after each tool call for metrics"
OUTPUT:
```yaml
id: p04_hook_post_tool_metrics
kind: hook
pillar: P04
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
trigger_event: "post_tool_use"
script_path: ".claude/hooks/tool_metrics.sh"
execution: "post"
blocking: false
domain: "observability"
quality: null
tags: [hook, metrics, post-tool, P04, observability, tracking]
tldr: "Logs tool name, duration, and success status to metrics file after each tool invocation"
timeout: 5000
conditions: ["tool_name != AskUserQuestion"]
async: true
error_handling: "log"
logging: true
environment: ["METRICS_FILE=.claude/metrics/tool_usage.jsonl", "SESSION_ID"]
keywords: [tool-metrics, post-tool-hook, usage-tracking, observability]
density_score: 0.88
```
## Trigger Configuration
Event: post_tool_use
Execution: post (fires after tool complete)
Conditions:
- tool_name != AskUserQuestion (skip interactive tools)
## Script
Path: .claude/hooks/tool_metrics.sh
Language: bash
Arguments: none (reads from environment)
```bash
echo "{\"tool\":\"$TOOL_NAME\",\"duration_ms\":$DURATION,\"success\":$SUCCESS,\"ts\":\"$(date -Is)\"}" >> "$METRICS_FILE"
```
## Input/Output
Input (from event): tool_name, duration_ms, success (boolean), output_size
Output (to caller): none (async, fire-and-forget)
## Error Handling
Strategy: log (never block on metrics failure)
- On script failure: log error to stderr, continue
- On timeout: kill script, log timeout event
- On missing script: log warning, skip execution
WHY THIS IS GOLDEN:
- quality: null (H05 pass) | id p04_hook_ pattern (H02 pass) | kind: hook (H04 pass)
- 22 fields present (H06 pass) | trigger_event: post_tool_use valid (H07 pass)
- timeout: 5000 <= 30000 (H08 pass) | blocking: false (H09 n/a)
- tldr: 79ch (S01 pass) | tags: 6 items (S02 pass)
- Trigger Configuration present (S03 pass) | Script present with bash (S04 pass)
- Input/Output present (S05 pass) | Error Handling present (S06 pass) | density: 0.88 (S09 pass)
## Anti-Example
INPUT: "Make a hook"
BAD OUTPUT:
```yaml
id: my_hook
kind: event
pillar: P11
trigger_event: "anything"
blocking: true
timeout: 60000
quality: 9.5
tags: [hook]
tldr: "This hook is designed to handle various events in the system lifecycle."
```
Run the script when something happens.
FAILURES:
1. id: no `p04_hook_` prefix -> H02 FAIL
2. kind: "event" not "hook" -> H04 FAIL
3. pillar: "P11" not "P04" -> H06 FAIL
4. quality: 9.5 (not null) -> H05 FAIL
5. trigger_event: "anything" not in enum -> H07 FAIL
6. timeout: 60000 exceeds 30000 max -> H08 FAIL
7. blocking: true with timeout 60000 exceeds 10000 -> H09 FAIL
8. Missing fields: version, created, updated, author, script_path, execution, domain -> H06 FAIL
9. tags: only 1 item -> S02 FAIL
10. tldr: filler ("designed to handle various") -> S10 FAIL
11. No ## Trigger Configuration section -> S03 FAIL
12. No ## Script section -> S04 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
