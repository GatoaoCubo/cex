---
kind: config
id: bld_config_boot_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: boot_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p02_boot_{provider_slug}.md` | `p02_boot_claude_code.md` |
| Builder directory | kebab-case | `boot-config-builder/` |
| Frontmatter fields | snake_case | `mcp_config`, `system_prompt_ref` |
| Provider slug | snake_case, lowercase | `claude_code`, `cursor_ai`, `codex` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P02_model/examples/p02_boot_{provider_slug}.md`
- Compiled: `cex/P02_model/compiled/p02_boot_{provider_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~3000 bytes
- Density: >= 0.80
## Provider Enum (non-exhaustive, extensible)
| Provider | Slug | Runtime |
|----------|------|---------|
| Claude Code | claude_code | CLI terminal |
| Cursor AI | cursor_ai | IDE extension |
| Codex CLI | codex | CLI terminal |
| Windsurf | windsurf | IDE extension |
| Aider | aider | CLI terminal |
| Custom | custom_{name} | User-defined |
## Identity Block Rules
- name: human-readable agent name (not slug)
- role: one-sentence role description
- agent_node: real agent_node name or "agnostic" — never blank
## Constraints Rules
- All numeric fields must be integers (not strings)
- temperature must be float 0.0-2.0
- timeout_seconds: reasonable range (30-600)
- max_retries: 0-5 range
