---
kind: config
id: bld_config_prompt_cache
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 20
disallowed_tools: []
fork_context: fork
hooks:
  pre_build: null
  post_build: null
permission_scope: nucleus
---
# Config: prompt_cache Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p10_pc_{name_slug}.yaml` | `p10_pc_rag_agent_shared.yaml` |
| Builder directory | kebab-case | `prompt-cache-builder/` |
| Frontmatter fields | snake_case | `ttl_seconds`, `eviction_strategy` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `P10_memory/examples/p10_pc_{name}.yaml`
- Compiled: `P10_memory/compiled/p10_pc_{name}.yaml`
## Size Limits
- Total file: max 2048 bytes
- tldr: <= 160 chars
## TTL Guidelines
| Freshness Need | TTL | Use Case |
|----------------|-----|----------|
| Real-time | 60s | Live data, streaming |
| Standard | 300s | General prompts, Anthropic default |
| Stable | 3600s | System prompts, few-shot |
| Long-lived | 86400s | Static reference, rarely changes |
## Provider-Specific Caching
| Provider | Type | Config | Discount |
|----------|------|--------|----------|
| Anthropic | Explicit breakpoints | cache_control: ephemeral | 90% read |
| OpenAI | Automatic prefix | >= 1024 token prefix | 50% read |
| Google | Explicit context | >= 32768 tokens | 75% read |
