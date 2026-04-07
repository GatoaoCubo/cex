---
kind: examples
id: bld_examples_spawn_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of spawn_config artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Examples Spawn Config"
version: "1.0.0"
author: n03_builder
tags: [spawn_config, builder, examples]
tldr: "Golden and anti-examples for spawn config construction, demonstrating ideal structure and common pitfalls."
domain: "spawn config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: spawn-config-builder
## Golden Example
INPUT: "Create spawn config for research_agent solo research task"
OUTPUT:
```yaml
id: p12_spawn_shaka_solo_research
kind: spawn_config
pillar: P12
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
title: "research_agent Solo Research Spawn"
mode: solo
director: "shaka"
model: "sonnet"
flags:
  - "--dangerously-skip-permissions"
  - "--no-chrome"
  - "-p"
mcp_config: ".mcp-shaka.json"
timeout: 1800
interactive: true
prompt_strategy: handoff
domain: "research"
quality: 8.8
tags: [spawn_config, shaka, solo, research]
tldr: "Solo spawn for research_agent research with sonnet, 30min timeout, handoff-based prompt"
```
## Spawn Command
```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File records/framework/powershell/spawn_solo.ps1 -sat shaka -task "Leia .claude/handoffs/RESEARCH_shaka.md e execute. Commit ANTES de parar." -interactive
```
## Parameters
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| mode | solo | Single director, single task |
| director | shaka | Research domain director |
| model | sonnet | research_agent uses sonnet per routing table |
| timeout | 1800s | 30min sufficient for research tasks |
| interactive | true | Terminal stays open for monitoring |
## Constraints
- Handoff file must exist before spawn
- Max inline prompt: 200 chars (use handoff for longer tasks)
- research_agent requires firecrawl + brain MCP servers
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p12_spawn_ pattern (H02 pass)
- kind: spawn_config (H04 pass)
- 19 required fields present (H06 pass)
- body has Spawn Command + Parameters + Constraints (H07 pass)
- mode: solo is valid enum (H08 pass)
- flags include baseline set (S03 pass)
- timeout is reasonable for task type (S05 pass)
- No task instructions in config (S07 pass)
- No filler phrases (S08 pass)
## Anti-Example
INPUT: "Create spawn config for a director"
BAD OUTPUT:
```yaml
id: spawn_config
kind: config
director: research_agent
quality: 8.0
```
Spawn the research_agent director to do research. It should use the sonnet model and
have access to firecrawl. Make sure it commits before stopping.
FAILURES:
1. id: no `p12_spawn_` prefix -> H02 FAIL
2. kind: "config" not "spawn_config" -> H04 FAIL
3. pillar: missing -> H06 FAIL
4. quality: 8.0 (not null) -> H05 FAIL
5. Missing fields: version, created, updated, author, mode, model, flags, timeout, domain, tags, tldr -> H06 FAIL
6. No ## Spawn Command section -> H07 FAIL
7. Body contains task instructions ("do research") -> S07 FAIL
8. No flags listed -> S03 FAIL
9. director uppercase "research_agent" (should be lowercase) -> S04 FAIL
10. Body is prose, not structured sections -> S08 FAIL
