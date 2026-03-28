---
id: bld_examples_naming_rule
pillar: P07
llm_function: GOVERN
kind: examples
domain: naming_rule
version: 1.0.0
---

# Examples — Naming Rule Builder
## Golden Example: Knowledge Card Naming Rule
```yaml
id: p05_nr_knowledge_card
kind: naming_rule
pillar: P05
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
scope: "Naming convention for knowledge card artifacts stored in the CEX pool under pillar P01"
pattern: "^p01_kc_[a-z][a-z0-9_]+\\.md$"
prefix: "p01_kc_"
suffix: ".md"
separator: "_"
case_style: snake_case
versioning: null
collision_strategy: reject
domain: knowledge_card
quality: null
tags: [naming-rule, knowledge-card, p01, pool, convention]
tldr: "Naming rule for P01 knowledge card files: p01_kc_{topic_slug}.md in snake_case"
keywords: [knowledge_card, p01, kc, topic_slug, snake_case, pool, naming, convention]
density_score: REC
```
## Scope
Governs the file naming of all knowledge card artifacts (`kind: knowledge_card`) stored in the CEX artifact pool under pillar P01. Every file that constitutes a knowledge card must comply with this pattern.
Artifacts governed by this rule: `knowledge_card`
## Pattern Definition
**Regex**: `^p01_kc_[a-z][a-z0-9_]+\.md$`
**Human-readable**: Pillar prefix `p01_`, kind abbreviation `kc_`, followed by a topic slug in snake_case (lowercase letters and digits, segments separated by underscores), with `.md` extension.
**Segments**:
| Position | Segment | Required | Description |
|----------|---------|----------|-------------|
| 1 | `p01_` | yes | Pillar prefix — scopes artifact to knowledge layer |
| 2 | `kc_` | yes | Kind abbreviation — identifies artifact as knowledge card |
| 3 | `{topic_slug}` | yes | Snake_case descriptor of the knowledge topic |
| 4 | `.md` | yes | File extension — all knowledge cards are Markdown |
## Examples
**Valid**:
- `p01_kc_vector_search.md` — standard topic slug
- `p01_kc_pep8_style_guide.md` — multi-segment slug with digit
- `p01_kc_llm_context_window.md` — three-segment topic slug
**Invalid**:
- `kc_vector_search.md` — VIOLATES: missing pillar prefix `p01_`
- `p01_kc_VectorSearch.md` — VIOLATES: PascalCase in slug, must be snake_case
## Collision Resolution
Strategy: `reject`
If a file named `p01_kc_{topic_slug}.md` already exists, refuse to create a duplicate. Surface a naming conflict error to the caller. Resolution: either choose a more specific topic slug or update the existing knowledge card in place.
## Anti-Example: 8+ Numbered Failures
The following artifact FAILS quality gates. Failures are annotated by gate reference.
```yaml
id: KnowledgeCardNaming          # FAILURE 1 [H01] ID does not match ^p05_nr_[a-z][a-z0-9_]+$ — PascalCase, missing pillar prefix
kind: naming_convention          # FAILURE 2 [H02] Wrong kind value — must be `naming_rule` not `naming_convention`
pillar: P1                       # FAILURE 3 [H03] Malformed pillar — must be `P05` not `P1`
version: 1                       # FAILURE 4 [H04] Not semver — must be `1.0.0`
scope: "Names stuff"             # FAILURE 5 [H05] Scope too vague — must specify exact artifact kind governed
pattern: "starts with p01"       # FAILURE 6 [H06] Pattern is plain text, not regex — untestable by machines
case_style: lowercase            # FAILURE 7 [H07] Invalid enum value — `lowercase` not in allowed set (snake_case, kebab-case, camelCase, PascalCase, UPPER_SNAKE)
collision_strategy: ignore       # FAILURE 8 [H08] Invalid enum value — `ignore` not in allowed set (append_sequence, append_hash, append_date, reject, overwrite)
quality: 8.5                     # FAILURE 9 [S01] Quality must be `null` at creation — self-assigned scores not permitted
# MISSING: suffix, separator, versioning, domain, tags, tldr, keywords, density_score
```
**Body failures**:
- No `## Scope` section present [H05]
- No `## Pattern Definition` section present [H06]
- No `## Examples` section present — zero valid or invalid examples [H06]
- No `## Collision Resolution` section present [H08]
