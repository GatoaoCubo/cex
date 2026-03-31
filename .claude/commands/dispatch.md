---
description: "Dispatch task to a nucleus. Usage: /dispatch <nucleus> <task>"
---

# /dispatch — Send Task to Nucleus Builder

Write a handoff file and spawn a nucleus builder.

## Usage

- `/dispatch n03 rebuild N01 agent artifacts`
- `/dispatch n01 research competitor analysis for SaaS market`
- `/dispatch grid MISSION_NAME` — launch parallel grid

## Steps

1. Parse nucleus and task from `$ARGUMENTS`
2. Write handoff file:
   ```
   .cex/runtime/handoffs/{nucleus}_task.md
   ```
   With content: task description, references, commit rules, signal instructions.
3. Dispatch:
   ```bash
   bash _spawn/dispatch.sh solo {nucleus} ""
   ```
   (Task comes from handoff file, not CLI args — avoids nested quote hell)
4. Monitor:
   ```bash
   bash _spawn/dispatch.sh status
   ```
5. After completion, consolidate (especially for Gemini nuclei N01/N04).

## Routing Table

| Domain | Nucleus | CLI |
|--------|---------|-----|
| Build/create | n03 | claude opus |
| Research/analysis | n01 | gemini 2.5-pro |
| Marketing/copy | n02 | claude sonnet |
| Knowledge/docs | n04 | gemini 2.5-pro |
| Code/test/deploy | n05 | codex |
| Sales/pricing | n06 | claude sonnet |
