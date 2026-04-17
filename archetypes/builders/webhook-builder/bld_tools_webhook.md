---
kind: tools
id: bld_tools_webhook
pillar: P04
llm_function: CALL
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
quality: 9.0
tags: [tools, webhook, P04, brain_query, validate, forge]
tldr: "Tools available to webhook-builder: brain_query for discovery, validate for gate checks, forge for artifact writing."
density_score: 0.99
title: Tools ISO - webhook
---
# Tools: webhook-builder
## Available Tools
### brain_query
**Purpose**: Discover existing webhook artifacts and related knowledge.
**When to use**: Before creating a new artifact (check duplicates), find provider-specific payload schemas (Stripe, GitHub, Slack), locate related artifacts (api_client, notifier) to confirm boundary.
**Queries**:
```
brain_query("webhook stripe payment")
brain_query("webhook github push event")
brain_query("p04_webhook existing artifacts")
brain_query("inbound webhook signature verification")
```
**Expected output**: file paths, artifact IDs, payload schema examples.
### validate (quality gate)
**Purpose**: Run HARD + SOFT gate checks against a draft artifact.
**When to use**: After composing the artifact before writing to disk, when uncertain if body is within 1024 bytes, when direction or signature_method might fail enum check.
**Usage pattern**:
```
validate(artifact_draft, gate="bld_quality_gate_webhook.md")
```
**Returns**: list of gate failures (H01-H10) + soft scores (S01-S12) + pass/fail.
### forge (write artifact)
**Purpose**: Write the final artifact file to the correct path.
**When to use**: Only after validate() returns PASS. Creates `p04_webhook_{event_slug}.md` in the correct pillar directory.
**Usage pattern**:
```
forge(artifact, path="P04/webhooks/p04_webhook_{event_slug}.md")
```
**Constraints**: Will reject if id does not match filename stem. Will reject if quality != null. Atomically writes — no partial files on error.
## Tool Call Order
```
1. brain_query(topic)          # discover existing, avoid duplicates
2. [compose artifact]          # fill output_template
3. validate(draft)             # gate check
4. [fix failures if any]       # iterate until PASS
5. forge(artifact, path)       # write to disk
```
## When NOT to Use Tools
- Do not call `forge` before `validate` passes
- Do not skip `brain_query` when provider is known (Stripe/GitHub/Slack) — a payload schema may already exist
- Do not call `validate` on partial drafts — complete frontmatter first

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |
