---
name: new-nucleus-bootstrap
description: Bootstrap a new nucleus N08+ with its rule, agent card, prompt, agent, four boot scripts, and scoped permissions across all runtimes.
when:
  - Creating a new nucleus N08 or higher.
  - Scaffolding the rule, card, prompt, runtime wrappers, and permissions for a new domain.
  - Extending CEX to a new trusted nucleus that must start scoped and multi-runtime.
kind: skill
pillar: P04
nucleus: n03
quality: 8.6
version: 1.0.0
created: 2026-04-16
multi_runtime: true
runtimes: [claude, codex, gemini, ollama]
density_score: 0.94
---

# New Nucleus Bootstrap

## When this fires
- Creating a nucleus beyond N01-N07.
- Scaffolding its rule, card, prompt, agent, boots, and permissions.
- Requiring launch parity across Claude, Codex, Gemini, and Ollama.

## What to do
1. Create the nine required assets: rule file, agent card, system prompt, agent definition, four boot scripts, and `.claude/nucleus-settings/n{XX}.json`.
2. Cover all four runtimes. Shared skills must also mirror into `.cex/skills/`.
3. Copy `.claude/nucleus-settings/_template.json`, then add only the nucleus-specific allowlist. New nuclei start scoped, not trusted.
4. Make every boot wrapper accept `-WorktreeDir`, `-Task`, and `-AutoAccept`, reusing `boot/_shared/worktree_helpers.ps1`.
5. Export the nucleus identity so shared completion signaling works.
6. Finish with `python -c "from _tools.signal_writer import write_signal; write_signal('n{XX}', 'complete', 9.0)"`.

## Example
- A request to create N08 Research Ops triggers this skill. Build the rule, card, prompt, agent, four `boot/n08*.ps1` wrappers, and scoped `n08.json` before dispatch.
