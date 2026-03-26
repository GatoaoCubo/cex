---
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of hook artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: hook-builder

## Golden Example

INPUT: "Create a hook that tracks tool usage after each tool call for metrics"

OUTPUT:
```yaml
---
id: p04_hook_post_tool_metrics
kind: hook
pillar: P04
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "EDISON"
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
---
```

## Trigger Configuration
Event: post_tool_use
Execution: post (fires after tool completes)
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
---
id: my_hook
kind: event
pillar: P11
trigger_event: "anything"
blocking: true
timeout: 60000
quality: 9.5
tags: [hook]
tldr: "This hook is designed to handle various events in the system lifecycle."
---
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
