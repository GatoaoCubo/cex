---
kind: tools
id: bld_tools_context_doc
pillar: P04
llm_function: CALL
purpose: Tools and data sources available to context-doc-builder
quality: 9.1
title: "Tools Context Doc"
version: "1.0.0"
author: n03_builder
tags: [context_doc, builder, examples]
tldr: "Golden and anti-examples for context doc construction, demonstrating ideal structure and common pitfalls."
domain: "context doc construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_retriever_config
  - bld_tools_memory_scope
  - bld_tools_chunk_strategy
  - bld_tools_cli_tool
  - bld_tools_few_shot_example
  - bld_tools_response_format
  - bld_tools_validation_schema
  - bld_tools_prompt_version
  - bld_tools_golden_test
  - bld_tools_handoff_protocol
---

# Tools: context-doc-builder
## Primary Tools
| Tool | Purpose | When to Use |
|------|---------|-------------|
| `brain_query` [MCP] | Search existing context_docs by domain/scope | Phase 1 — before producing new artifact |
| `validate_artifact.py --kind context_doc` | Automated gate check | Phase 3 — post-composition [PLANNED] |
## brain_query Patterns
```python
# Check for existing context_doc in target domain
brain_query("context_doc ecommerce imports brazil")
# Find related knowledge_cards to avoid overlap
brain_query("knowledge_card [domain_keywords]")
# Find system_prompts that consume this domain context
brain_query("system_prompt [domain] inject")
```
## Data Sources
| Source | Path | Purpose |
|--------|------|---------|
| Kind schema | `cex/P01_knowledge/_schema.yaml` | Field definitions, constraints |
| Seed bank | `cex/P01_knowledge/SEED_BANK.yaml` | Domain seed words |
| Examples | `cex/P01_knowledge/examples/` | Reference context_docs |
| Output template | `OUTPUT_TEMPLATE.md` (this builder) | Structural skeleton |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation (until validate_artifact.py ships)
Manual gate check against QUALITY_GATES.md:
1. YAML parse check: paste frontmatter into YAML linter
2. id pattern: verify `^p01_ctx_[a-z][a-z0-9_]+$` regex match
3. Byte count: `wc -c < artifact.md` — must be <= 2048 (body only)
4. Required fields: id, kind, domain, scope all present?
5. quality == null: confirm not self-scored
6. Scope section: >= 3 lines present?
## Output Destinations
Produced artifacts go to: `cex/P01_knowledge/examples/` (canonical storage)
Naming: `p01_ctx_{topic_slug}.md` + `p01_ctx_{topic_slug}.yaml`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_retriever_config]] | sibling | 0.46 |
| [[bld_tools_memory_scope]] | sibling | 0.44 |
| [[bld_tools_chunk_strategy]] | sibling | 0.43 |
| [[bld_tools_cli_tool]] | sibling | 0.41 |
| [[bld_tools_few_shot_example]] | sibling | 0.41 |
| [[bld_tools_response_format]] | sibling | 0.41 |
| [[bld_tools_validation_schema]] | sibling | 0.41 |
| [[bld_tools_prompt_version]] | sibling | 0.41 |
| [[bld_tools_golden_test]] | sibling | 0.41 |
| [[bld_tools_handoff_protocol]] | sibling | 0.40 |
