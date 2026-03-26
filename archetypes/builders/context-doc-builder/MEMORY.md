---
pillar: P10
llm_function: INJECT
purpose: Accumulated production patterns and anti-patterns for context-doc-builder
---

# Memory: context-doc-builder

## Common Mistakes (avoid these)

| Mistake | Gate | Fix |
|---------|------|-----|
| `quality: 8.5` in frontmatter | H05 | Always `quality: null` — never self-score |
| id: `ctx_foo` missing prefix | H02 | Always `p01_ctx_` prefix |
| id != filename stem | H03 | Set id first, name file to match |
| Body > 2048 bytes | H07 | Trim References then Background prose |
| Missing `scope` field | H06 | scope is required — one sentence boundary |
| Drifting into KC territory | - | context_doc allows narrative; KC does not. If you find yourself writing atomic single-fact structure, you are building a KC, not a context_doc |
| Missing `## Scope` section | S03 | Scope section is required, minimum 3 lines |
| Filler prose | S05 | Delete "this document", "basically", "in summary" on sight |
| tags list len < 3 | S02 | Minimum: [context-doc, {domain_tag}, {scope_tag}] |
| tldr > 160 chars | S01 | Count chars before committing; trim to key facts |

## Domain Patterns: Scope Templates

| Domain Type | Scope Template |
|-------------|---------------|
| Regulatory | `[Country] [regulation_name] for [actor_type], [year_range] enforcement cycle` |
| Technical | `[System_name] [component] constraints for [consumer_type] integration` |
| Organizational | `[Team_name] [process_name] context for [onboarding|handoff|planning]` |
| Market | `[Market_name] competitive landscape for [decision_type] in [quarter/year]` |

## Production Counter
0 context_docs produced via this builder.

## Session Patterns (updated on use)
- brain_query before produce: prevents duplicate context_docs
- Scope first, write second: prevents scope creep in body
- Byte count after compose: prevents H07 failures at validation
