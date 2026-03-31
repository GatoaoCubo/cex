---
kind: tools
id: bld_tools_system_prompt
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for system_prompt production
---

# Tools: system-prompt-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing system_prompts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P03_prompt/_schema.yaml | Field definitions, kinds |
| CEX Examples | P03_prompt/examples/ | Real system_prompt artifacts |
| PRIME files | records/agent_nodes/*/PRIME_*.md | 7 existing system prompts |
| ISO Instructions | records/agents/*/iso_vectorstore/ISO_*_SYSTEM_INSTRUCTION.md | 101 agent system prompts |
| Rules files | .claude/rules/*.md | 10 operational rule sets |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P03_system_prompt |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | BashTool | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, rules_count match,
body has all 4 required sections, no task instructions leaked into identity.
