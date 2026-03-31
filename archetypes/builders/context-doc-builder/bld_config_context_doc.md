---
kind: config
id: bld_config_context_doc
pillar: P09
llm_function: CONSTRAIN
purpose: Runtime configuration constraints for context_doc production
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
# Config: context_doc
## Naming Rules
| Rule | Pattern | Example |
|------|---------|---------|
| Markdown file | `p01_ctx_{topic_slug}.md` | `p01_ctx_br_import_regs.md` |
| YAML companion | `p01_ctx_{topic_slug}.yaml` | `p01_ctx_br_import_regs.yaml` |
| id field | `p01_ctx_{topic_slug}` | `p01_ctx_br_import_regs` |
| topic_slug | `[a-z][a-z0-9_]+` (snake_case, no hyphens) | `br_import_regs` |
**Critical**: id MUST equal filename stem. Brain search depends on this invariant.
## File Paths
| Artifact | Canonical Path |
|----------|---------------|
| Produced context_docs | `cex/P01_knowledge/examples/` |
| Schema reference | `cex/P01_knowledge/_schema.yaml` |
| Seed bank | `cex/P01_knowledge/SEED_BANK.yaml` |
| Builder files | `cex/archetypes/builders/context-doc-builder/` |
## Size Constraints
| Constraint | Value | Scope |
|------------|-------|-------|
| max_bytes | 2048 | Body only (all sections after frontmatter) |
| tldr max | 160 chars | frontmatter.tldr field |
| tags min | 3 items | frontmatter.tags list |
| keywords min | 3 items | frontmatter.keywords list |
| scope min | 1 sentence | frontmatter.scope field |
| density_score min | 0.80 | if provided (recommended) |
## Trim Priority (if body exceeds 2048 bytes)
1. Trim `## References` section first (least dense)
2. Trim `## Background` narrative prose (keep facts, remove transitions)
3. Trim `## Stakeholders` to bullet list only
4. Never trim `## Scope` or `## Constraints & Assumptions`
## Invariants (never override)
- `quality: null` — never self-assign score
- `kind: context_doc` — literal, no variation
- `pillar: P01` — pillar assignment fixed
- id == filename stem — enforced by gate H03
