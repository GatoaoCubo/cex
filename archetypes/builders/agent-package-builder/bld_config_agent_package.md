---
kind: config
id: bld_config_agent_package
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
---
# Config: agent_package Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Package directory | `{agent_slug}/` | `scout_agent/` |
| Manifest file | `manifest.yaml` | `scout_agent/manifest.yaml` |
| builder specs | lowercase with underscores | `system_instruction.md` |
| Builder directory | kebab-case | `agent-package-builder/` |
| Frontmatter fields | snake_case | `agent_name`, `files_count` |
| Agent slug | snake_case, lowercase | `knowledge_card_builder` |
| Package id | `p02_iso_{agent_slug}` | `p02_iso_scout_agent` |
Rule: id MUST equal directory name with p02_iso_ prefix.
Rule: manifest.yaml is ALWAYS the entry point file.
## File Paths
- Output: `cex/agents/{agent_slug}/manifest.yaml`
- Package dir: `cex/agents/{agent_slug}/`
- Each file lives at root of agent directory (no subdirectories)
## Size Limits (aligned with SCHEMA)
- Manifest body: max 4096 bytes
- Per-file: max 4096 bytes
- system_instruction.md: max 4096 tokens
- Density: >= 0.80 across all files
## Tier Rules
| Tier | Files | When to use |
|------|-------|-------------|
| minimal | 3 | Quick prototype, internal-only agent |
| standard | 7 | Production agent with full documentation |
| complete | 10 | Sharable agent with onboarding and deployment |
| whitelabel | 12 | Redistributable agent with branding support |
Rule: files_count MUST match actual files in directory.
Rule: tier MUST match file count (minimal=3, standard=7, complete=10, whitelabel=12).
## Portability Rules
- No hardcoded paths: `/home/`, `/Users/`, `C:\`, `records/`, `.claude/`
- No framework-specific agent_group names in system_instruction.md
- All file references use relative paths within package directory
- LLM-agnostic: no provider-specific API calls in instructions.md
## LP Mapping Enum
| File | Pillar | Function |
|------|--------|----------|
| manifest.yaml | P02 | BECOME |
| system_instruction.md | P03 | BECOME |
| instructions.md | P03 | REASON |
| architecture.md | P08 | CONSTRAIN |
| output_template.md | P05 | PRODUCE |
| examples.md | P07 | GOVERN |
| error_handling.md | P11 | GOVERN |
| quick_start.md | P01 | INJECT |
| input_schema.yaml | P06 | CONSTRAIN |
| upload_kit.md | P04 | CALL |
