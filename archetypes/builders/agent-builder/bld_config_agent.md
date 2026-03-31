---
kind: config
id: bld_config_agent
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: high
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: pillar
---
# Config: agent Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p02_agent_{slug}.md` + `.yaml` | `p02_agent_knowledge_card_builder.md` |
| Builder directory | kebab-case | `agent-builder/` |
| Frontmatter fields | snake_case | `agent_node`, `capabilities_count` |
| Agent slug | snake_case, lowercase | `knowledge_card_builder`, `scout_agent` |
| ISO files | `ISO_{AGENT_UPPER}_{NNN}_{TYPE}.md` | `ISO_SCOUT_AGENT_004_INSTRUCTIONS.md` |
| Agent upper | SCREAMING_SNAKE_CASE | `KNOWLEDGE_CARD_BUILDER` |
Rule: id MUST equal filename stem.
Rule: ISO file NNN starts at 001 and increments without gaps.
## File Paths
- Output (canonical): `cex/P02_model/examples/p02_agent_{slug}.md`
- Compiled: `cex/P02_model/compiled/p02_agent_{slug}.yaml`
- ISO vectorstore: `agents/{slug}/iso_vectorstore/ISO_{UPPER}_{NNN}_{TYPE}.md`
## Size Limits (aligned with SCHEMA)
- Body: max 5120 bytes
- Total (frontmatter + body): ~6500 bytes
- Density: >= 0.80
- Per ISO file: max 4096 bytes
## Satellite Enum
| Value | When to use |
|-------|-------------|
| orchestrator | Orchestration agents |
| researcher | Research and scraping agents |
| marketer | Marketing and copy agents |
| builder | Build and code agents |
| knowledge-engine | Knowledge and documentation agents |
| executor | Execution, deploy, and infra agents |
| monetizer | Monetization and product agents |
| agnostic | Cross-agent_node utility agents |
## ISO File Type Enum
| NNN | TYPE | Pillar |
|-----|------|--------|
| 001 | MANIFEST | P02 |
| 002 | QUICK_START | P01 |
| 003 | PRIME | P03 |
| 004 | INSTRUCTIONS | P03 |
| 005 | ARCHITECTURE | P08 |
| 006 | OUTPUT_TEMPLATE | P05 |
| 007 | EXAMPLES | P07 |
| 008 | ERROR_HANDLING | P11 |
| 009 | UPLOAD_KIT | P04 |
| 010 | SYSTEM_INSTRUCTION | P03 |
## Body Requirements
- Overview: 2-3 sentences, must name agent_node and domain
- Architecture: capabilities (4-8 bullets) + tools table + agent_node position
- File Structure: full iso_vectorstore listing with correct ISO naming
- When to Use: triggers + keywords + NOT when exclusions (mandatory)
- Common Issues: 3-5 failure modes, each with one-line remediation
