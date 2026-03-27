---
id: p10_lr_knowledge_card_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: edison
observation: "Knowledge cards with body density below 0.80 (ratio of informative content to total words) fail the density gate and require rewrite. Bullets over 80 characters are caught by validator and force reformatting. Filler phrases ('this document describes', 'it is worth noting') consume tokens without adding information and are the primary cause of low density scores. Axioms written as observations ('caching improves performance') instead of rules ('ALWAYS declare cache TTL, NEVER cache without expiry') are rejected by S18. Cards referencing internal system paths fail H09."
pattern: "Achieve density >= 0.80 by: replacing prose paragraphs with bullet lists, replacing descriptions with comparison tables, removing all transition sentences, ensuring each bullet contains exactly one fact. Axioms must be ALWAYS/NEVER imperatives, not observations. Quality field must be null — scoring is external. Body size 200 bytes minimum, 5KB maximum. No internal paths in any field."
evidence: "11 knowledge card productions: 6 failed first density check (avg density 0.64). After applying bullet+table conversion, avg density reached 0.83. Axiom format errors in 4 of 11 (observation format instead of ALWAYS/NEVER). H09 path violations in 2 early productions. Quality set to a number in 3 early productions (validator rejections)."
confidence: 0.75
outcome: SUCCESS
domain: knowledge_card
tags: [knowledge-card, density, axioms, frontmatter, atomic-facts, classification]
tldr: "Density >= 0.80 requires bullets over prose and tables over descriptions. Axioms are ALWAYS/NEVER rules, not observations. quality:null always."
impact_score: 7.5
decay_rate: 0.05
satellite: edison
keywords: [knowledge_card, density, axiom, frontmatter, bullet, table, tldr, domain, meta, quality_null]
---

## Summary

Knowledge cards distill domain knowledge into high-density atomic facts. The primary quality gate is density >= 0.80 — the ratio of informative content to total words. The most reliable path to high density is structural: replace prose with bullets, replace descriptions with tables, and eliminate all filler language.

## Pattern

Density boosting techniques (apply in order):

1. **Prose -> bullets** - Convert every paragraph into a bullet list. Each bullet = one fact. If a bullet needs a sub-fact, use a nested bullet, not a compound sentence.
2. **Descriptions -> tables** - Convert any comparison, enumeration, or mapping into a markdown table. Tables carry ~3x the information per line compared to prose.
3. **Remove transitions** - Delete: "as we can see", "it is worth noting", "in summary", "this document", "the following". These add zero information.
4. **Bullet length** - Each bullet under 80 characters. If over, split into two bullets or use a table.
5. **Axiom format** - Every axiom must be an imperative starting with ALWAYS or NEVER. Not "caching is important" but "ALWAYS declare TTL when caching, NEVER cache without expiry".

Frontmatter rules:
- `quality: null` always — scoring is external, never self-assigned
- `id` slug uses underscores: `p01_kc_topic_name`
- `tags` as YAML list, not comma-separated string
- No paths containing `records/`, `.claude/`, `/home/`, `C:\` anywhere in the card

Body size constraints: minimum 200 bytes (4+ sections with 3+ lines each), maximum 5KB.

## Anti-Pattern

- Prose paragraphs — density drops below 0.70 immediately.
- Bullets over 80 chars — validator S10 catches, forces reformatting.
- Axiom as observation: "Caching improves performance" — must be "ALWAYS declare cache TTL".
- `quality: 8.5` — validator H05 rejects any non-null value.
- `tags: "ai, ml, cache"` as string — validator H07 rejects, must be YAML list.
- Internal paths in any field — validator H09 rejects, breaks portability.
- Self-referencing tldr: "This card describes caching" — tldr must be the direct fact, not a description of the card.

## Context

Density failures were the most common first-attempt rejection. Analysis showed the root cause was authoring cards as mini-essays rather than structured fact tables. The structural conversion (prose->bullets, descriptions->tables) was already known from writing practice, but applying it as a mandatory first pass before any other quality check proved to be the highest-leverage intervention. Axiom format errors were the second most common issue, resolved by the ALWAYS/NEVER rule.

## Impact

- First-attempt density failures: 6 of 11 productions -> 0 with structural conversion pass
- Average density before pattern: 0.64 -> 0.83 after
- Axiom format errors: 4 of 11 -> 0 with ALWAYS/NEVER rule
- H09 path violations: 2 early productions -> 0 with path exclusion rule

## Reproducibility

Structural conversion (prose->bullets, descriptions->tables) is universally applicable and takes ~5 minutes on a typical card. The ALWAYS/NEVER axiom rule is a simple format check. Quality:null and tag-as-list are mechanical rules with zero ambiguity.

## References

- Density calculation: QUALITY_GATES.md
- Frontmatter field definitions: SCHEMA.md
- High-density examples: EXAMPLES.md
