---
kind: config
id: bld_config_toolkit
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, limits, and operational constraints
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
# Config: toolkit Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact file | `p04_tk_{name}.yaml` | `p04_tk_file_ops.yaml` |
| Builder directory | kebab-case | `toolkit-builder/` |
| Tool names | snake_case | `read_file`, `git_commit`, `web_search` |
| Category values | snake_case | `file_ops`, `git_ops`, `search` |
| Confirmation tiers | lowercase enum | `auto`, `confirm`, `deny` |
Rule: use `.yaml` only for this builder — toolkits are human-reviewed permission documents.
## File Paths
- Output: `cex/P04_tools/compiled/p04_tk_{name}.yaml`
- Human reference: `cex/P04_tools/examples/p04_tk_{name}.md`
## Size Limits
- Preferred toolkit size: <= 2048 bytes
- Absolute max: 4096 bytes
- Maximum 15 tools per toolkit — split into sub-toolkits if more are needed
- Tool descriptions should be one-line: purpose, not usage instructions
## Toolkit Restrictions
- Required fields must appear exactly as defined in schema
- Omit optional null/unknown fields instead of writing placeholders
- `denied_for` is only specified per tool when specific agents are blocked
- `requires_confirmation` must match risk level: auto for reads, confirm for writes
- `mcp_endpoint` only present when tool maps to an MCP server
- Category must match one of: file_ops, git_ops, search, web, system, build, analysis
## Boundary Restrictions
- No tool implementation code (functions, classes, scripts) inside the toolkit
- No agent identity, persona, or system prompt content
- No workflow steps, DAGs, or sequencing logic
- No routing tables, dispatch rules, or agent selection logic
- No duplicate tools across toolkits — each tool lives in exactly one toolkit
## Least-Privilege Rules
- Start with zero tools, add only what the agent demonstrably needs
- Read operations default to auto confirmation
- Write operations MUST require confirmation
- Delete/destructive operations default to deny unless explicitly justified
- Deny lists override allow lists — if a tool is denied, no allow can override
- Review toolkit quarterly: remove tools the agent hasn't used in 90 days
