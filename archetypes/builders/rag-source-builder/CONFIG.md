---
pillar: P09
llm_function: CONSTRAIN
version: 1.0.0
---

# Config: rag_source

## File Naming

| Component | Rule | Example |
|-----------|------|---------|
| Prefix | p01_rs_ | p01_rs_ |
| Slug | lowercase, underscores, max 30 chars | anthropic_claude_api_docs |
| Extension | .md (primary) + .yaml (twin) | p01_rs_anthropic_claude_api_docs.md |
| id == stem | Mandatory — id field must equal filename without extension | id: p01_rs_anthropic_claude_api_docs |

## File Paths

| File | Path |
|------|------|
| Primary artifacts | cex/P01_knowledge/examples/p01_rs_{slug}.md |
| YAML twins | cex/P01_knowledge/examples/p01_rs_{slug}.yaml |
| Schema reference | cex/P01_knowledge/_schema.yaml |
| Builder | cex/archetypes/builders/rag-source-builder/ |

## Size Constraints

| Constraint | Value | Scope |
|-----------|-------|-------|
| max_bytes | 1024 | body (below frontmatter) |
| tldr | <= 160 chars | frontmatter field |
| tags | >= 3 items | frontmatter list |
| keywords | 3-8 items | frontmatter list (recommended) |

## Freshness Config

| Setting | Recommended Value |
|---------|------------------|
| Re-check interval | 30 days |
| Staleness threshold | 90 days |
| Auto-flag stale | last_checked > 90 days ago |
| Trigger for forced refresh | upstream version release |

## Enum Values

| Field | Allowed Values |
|-------|---------------|
| reliability | high, medium, low |
| format | html, json, api, pdf, csv |
| extraction_method | crawl, api_call, scrape, download |

## Version Policy
- Start at "1.0.0" for new sources
- Bump patch (1.0.1) on metadata update (freshness, reliability)
- Bump minor (1.1.0) on URL change or domain reclassification
- Bump major (2.0.0) on source structural change (format change, auth added)

## Quality field
Always null at creation. Updated by validation pipeline, never by the builder.
