---
id: p11_qg_knowledge_card
kind: quality_gate
pillar: P11
title: "Gate: Knowledge Card"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "knowledge_card — atomic searchable facts with high information density"
quality: 9.0
tags: [quality-gate, knowledge-card, density, fact, distillation, searchability]
tldr: "Gates ensuring knowledge_card artifacts contain concrete atomic facts with density >= 0.8, semantic frontmatter, and file size <= 5KB."
density_score: 0.94
llm_function: GOVERN
---
# Gate: Knowledge Card
## Definition
| Field     | Value |
|-----------|-------|
| metric    | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool; 9.5 for golden |
| operator  | AND (all hard) + weighted average (soft) |
| scope     | any artifact with `kind: knowledge_card` |
## HARD Gates
All must pass. Any failure = immediate reject.
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error on any field |
| H02 | ID matches `^KC_[A-Z0-9_]+$` | Lowercase, missing KC_ prefix, or non-alphanumeric chars |
| H03 | ID equals filename stem | `id: KC_REDIS_TTL` in file `KC_CACHE_TTL.md` |
| H04 | Kind equals literal `knowledge_card` | Any other kind value |
| H05 | Quality field is `null` | Any non-null value |
| H06 | All 19 required fields present | Missing: domain, tldr, density_score, sources, or card_type |
| H07 | `density_score` is a float in range [0.0, 1.0] | Outside range or non-numeric value |
| H08 | `density_score` >= 0.8 | Score below threshold — card too sparse to be useful |
| H09 | Total file size <= 5120 bytes | Exceeds 5KB limit |
| H10 | `tldr` is <= 160 characters | tldr exceeds character limit |
## SOFT Scoring
Total weights sum to 100%.
| ID  | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|-----|-----------|--------|--------|-------|-------|
| S01 | Factual concreteness | 1.0 | Card contains specific values, numbers, or verifiable facts | Mix of facts and vague statements | Entirely vague or conceptual |
| S02 | Atomicity | 1.0 | Card covers exactly one concept with no scope creep | Mostly one concept; minor tangents | Multiple unrelated concepts |
| S03 | Searchability — tags | 1.0 | Tags cover domain, subtopic, and use-case angles (>= 4 distinct tags) | 3 tags | Fewer than 3 tags |
| S04 | Source attribution | 1.0 | At least one specific source (URL, paper, spec version, date) | Source mentioned but not specific | No sources |
| S05 | Card type classification | 0.5 | `card_type` is `domain_kc` or `meta_kc` with correct body structure for that type | Type present but body structure mismatches | Type absent |
| S06 | Density discipline | 1.0 | No padding, no restatements, no filler sentences in body | Minor padding present | More than 20% filler content |
| S07 | tldr precision | 1.0 | tldr is a standalone searchable sentence capturing the key fact | tldr too vague to retrieve the card | tldr absent or over 160 characters |
| S08 | Currency | 0.5 | `created` date present; `updated` reflects last substantive revision | Created date only, no updated | No dates |
| S09 | Cross-references | 0.5 | Related cards or concepts linked in body | Related concepts mentioned but not linked | No cross-references |
| S10 | Practical applicability | 1.0 | Body answers "when would I use this?" with a concrete scenario | Implicitly applicable but not stated | Pure theory with no application context |
**Score = sum(pts * weight) / sum(max_pts * weight) * 10**
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Publish to knowledge pool as authoritative reference card |
| >= 8.0 | Skilled | Publish to pool + log pattern |
| >= 7.0 | Learning | Use but flag for improvement |
| < 7.0 | Rejected | Return to author with gate report |
## Bypass
| Field | Value |
|-------|-------|
| Conditions | Rapidly evolving topic where sources are not yet stabilized (e.g., new library release, breaking API change) |
| Approver | Domain expert reviewer |
