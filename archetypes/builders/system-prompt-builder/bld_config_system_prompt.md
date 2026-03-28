---
kind: config
id: bld_config_system_prompt
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: system_prompt Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p03_sp_{agent_slug}.md` | `p03_sp_knowledge_card_builder.md` |
| Builder directory | kebab-case | `system-prompt-builder/` |
| Frontmatter fields | snake_case | `target_agent`, `rules_count` |
| Agent slug | snake_case, lowercase | `scout_agent`, `model_card_builder` |

Rule: id MUST equal filename stem.

## File Paths
- Output: `cex/P03_prompt/examples/p03_sp_{agent_slug}.md`
- Compiled: `cex/P03_prompt/compiled/p03_sp_{agent_slug}.yaml`

## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total (frontmatter + body): ~5500 bytes
- Density: >= 0.80

## Tone Enum

| Value | When to use |
|-------|-------------|
| formal | Enterprise, compliance, legal agents |
| technical | Builder agents, infrastructure, code |
| conversational | User-facing, chat, support agents |
| authoritative | Governance, quality, security agents |

## Safety Level Enum

| Value | When to use |
|-------|-------------|
| standard | Most agents — reasonable constraints |
| strict | Security, compliance, payment agents |
| permissive | Creative, research, exploration agents |

## Body Requirements
- Identity: 2-4 sentences, must name domain expertise
- Rules: 7-12 numbered items, ALWAYS/NEVER pattern mandatory
- Output Format: must specify format type and sections
- Constraints: must include knowledge boundary and exclusions
