---
id: n00_computer_use_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Computer Use -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, computer_use, p04, n00, archetype, template]
density_score: 1.0
updated: "2026-04-17"
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A computer_use artifact defines the interface for LLM-controlled screen, keyboard, and mouse interaction, enabling agents to operate desktop GUIs, web browsers, and native applications as a human would. It specifies the screenshot capture loop, action space (click, type, scroll, drag), and coordinate normalization protocol. The output is an agentic desktop automation tool that bridges LLM reasoning with OS-level interaction.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `computer_use` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| provider | string | yes | Backend: anthropic_claude, openai_cua, custom |
| action_space | list | yes | Supported actions: screenshot, click, type, scroll, drag |
| screenshot_interval_ms | integer | yes | How often to capture screen state |
| safety_guardrails | list | yes | Actions that are blocked (e.g., delete_files, format_disk) |

## When to use
- When an agent must interact with legacy desktop applications that have no API
- When building RPA (robotic process automation) agents that operate existing software
- When browser automation with Playwright is insufficient due to non-web UI requirements

## Builder
`archetypes/builders/computer_use-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind computer_use --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: cu_claude_desktop_operator
kind: computer_use
pillar: P04
nucleus: n05
title: "Claude Desktop Operator"
version: 1.0
quality: null
---
provider: anthropic_claude
action_space: [screenshot, click, type, scroll]
screenshot_interval_ms: 500
safety_guardrails: [delete_files, format_disk, uninstall_software, send_email_without_confirm]
```

## Related kinds
- `browser_tool` (P04) -- web-specific automation that computer_use subsumes for browser contexts
- `vision_tool` (P04) -- image analysis tool that interprets computer_use screenshots
- `guardrail` (P11) -- safety rules enforced on computer_use action execution
- `action_paradigm` (P04) -- execution loop that coordinates computer_use observe-act cycles
