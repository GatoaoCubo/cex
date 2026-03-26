---
pillar: P04
llm_function: CALL
purpose: Tools and data sources available to context-doc-builder
---

# Tools: context-doc-builder

## Primary Tools

| Tool | Purpose | When to Use |
|------|---------|-------------|
| `brain_query` | Search existing context_docs by domain/scope | Phase 1 — before producing new artifact |
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
