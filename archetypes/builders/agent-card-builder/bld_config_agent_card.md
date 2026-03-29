---
kind: config
id: bld_config_director
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: agent_card Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p08_sat_{name_lower}.yaml` | `p08_sat_shaka.yaml` |
| Builder directory | kebab-case | `agent-card-builder/` |
| Frontmatter fields | snake_case | `domain_area`, `boot_sequence` |
| Satellite names | UPPERCASE in name field | `researcher`, `builder`, `marketer` |
| Name slugs | lowercase in id | `shaka`, `edison`, `lily` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P08_architecture/examples/p08_sat_{name_lower}.yaml`
- Compiled: `cex/P08_architecture/compiled/p08_sat_{name_lower}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total: ~6000 bytes including frontmatter
- Density: >= 0.80
## Model Enum
| Model | When to use |
|-------|-------------|
| opus | Complex reasoning, code generation, architecture |
| sonnet | Balanced cost/quality, research, marketing |
| haiku | Simple tasks, classification, formatting |
## MCP Convention
- List all MCPs even if empty: `mcps: []`
- Use short names: `brain`, `firecrawl`, `railway`, `pg`
- MCP config path follows: `.mcp-{sat_lower}.json`
## Scaling Defaults
| Field | Default | Max |
|-------|---------|-----|
| max_concurrent | 1 | 3 (BSOD prevention) |
| timeout_minutes | 30 | 120 |
| memory_limit_mb | 2048 | 8192 |
