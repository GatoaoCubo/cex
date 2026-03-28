---
kind: config
id: bld_config_spawn_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: spawn_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p12_spawn_{mode_slug}.yaml` | `p12_spawn_shaka_solo_research.yaml` |
| Builder directory | kebab-case | `spawn-config-builder/` |
| Frontmatter fields | snake_case | `mcp_config`, `prompt_strategy` |
| Mode slug | snake_case, lowercase | `shaka_solo_research`, `grid_wave_1` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P12_orchestration/examples/p12_spawn_{mode_slug}.yaml`
- Compiled: `cex/P12_orchestration/compiled/p12_spawn_{mode_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes
- Total (frontmatter + body): ~4500 bytes
- Density: >= 0.80
## Mode Enum
| Value | When to use | Script |
|-------|-------------|--------|
| solo | 1 satellite, 1 task | spawn_solo.ps1 |
| grid | 2-6 satellites, parallel tasks | spawn_grid.ps1 |
| continuous | >6 tasks, auto-refill slots from queue | spawn_grid.ps1 -mode continuous |
## Baseline Flags (mandatory)
| Flag | Purpose |
|------|---------|
| --dangerously-skip-permissions | Skip tool permission prompts |
| --no-chrome | Prevent Chrome extension loading |
| -p | Non-interactive mode (skip workspace trust) |
## Satellite-Model Routing
| Satellite | Model | MCP Config |
|-----------|-------|------------|
| shaka | sonnet | .mcp-shaka.json |
| lily | sonnet | .mcp-lily.json |
| edison | opus | .mcp-edison.json |
| pytha | sonnet | .mcp-pytha.json |
| atlas | opus | .mcp-atlas.json |
| york | sonnet | .mcp-york.json |
