---
kind: quality_gate
id: p11_qg_glossary_entry
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of glossary_entry artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: glossary_entry"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, glossary-entry, terminology, definition, P11]
tldr: "Validates glossary_entry artifacts: 3-line definition constraint, synonym presence, disambiguation clarity, and no circular references."
domain: "glossary_entry — concise domain term definitions with synonyms, disambiguation, and usage context"
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.89
related:
  - bld_examples_glossary_entry
  - bld_instruction_glossary_entry
  - p11_qg_few_shot_example
  - p11_qg_formatter
  - p10_lr_glossary_entry_builder
  - p03_sp_glossary_entry_builder
  - p11_qg_quality_gate
  - p11_qg_golden_test
  - p01_kc_glossary_entry
  - bld_knowledge_card_glossary_entry
---

## Quality Gate

# Gate: glossary_entry
## Definition
| Field     | Value |
|-----------|-------|
| metric    | composite score across SOFT dimensions |
| threshold | >= 7.0 to publish; >= 9.5 for golden |
| operator  | weighted average after all HARD gates pass |
| scope     | all artifacts where `kind: glossary_entry` |
All HARD gates are AND-logic: one failure rejects the artifact regardless of SOFT score.
## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Any YAML syntax error |
| H02 | ID matches `^p01_gl_[a-z][a-z0-9_]+$` | Wrong format or namespace |
| H03 | ID equals filename stem (no extension) | Mismatch between id field and file name |
| H04 | Kind equals literal `glossary_entry` | Any other value |
| H05 | `quality` field is null | Any non-null value |
| H06 | Required fields present: id, kind, pillar, version, created, updated, author, term, domain, quality, tags, tldr | Any missing field |
| H07 | `definition` body section is <= 3 lines | Exceeds the conciseness constraint for this kind |
| H08 | `synonyms` is a list with len >= 1 | Missing or empty synonyms list |
| H09 | `term` is non-empty string | Missing or blank term field |
## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| S01 | `tldr` IS the definition (not meta-commentary about the entry) | 0.12 | Is the definition=1.0, meta-comment=0.2 |
| S02 | Tags list len >= 3, includes `glossary` | 0.05 | Met=1.0, partial=0.5 |
| S03 | Definition section present in body (not just frontmatter) | 0.10 | Present=1.0, absent=0.0 |
| S04 | Definition includes a concrete usage example | 0.10 | Present=1.0, absent=0.0 |
| S05 | `term` is lowercase unless it is a proper noun | 0.05 | Correct=1.0, wrong case=0.3 |
| S06 | Disambiguation section present and references at least one similar term | 0.12 | Present+reference=1.0, absent=0.0 |
| S07 | No circular reference (term not used to define itself) | 0.13 | No circular ref=1.0, circular=0.0 |
| S08 | Related Terms section with cross-references to other entries | 0.08 | Present=1.0, absent=0.0 |
| S09 | Boundary from `knowledge_card` and `context_doc` stated | 0.10 | Both stated=1.0, one=0.5, absent=0.0 |
| S10 | No filler phrases ("very important", "basically", "in summary") | 0.10 | Clean=1.0, filler present=0.0 |
| S11 | `density_score` >= 0.80 | 0.05 | Met=1.0, below=0.0 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — reference artifact for glossary_entry calibration |
| >= 8.0 | PUBLISH — pool-eligible; definition concise and disambiguated |
| >= 7.0 | REVIEW — usable but missing usage example or disambiguation |
| < 7.0  | REJECT — redo; likely circular definition, oversized, or no synonyms |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Term is a proper noun (product name, acronym) where synonyms are genuinely N/A |
| approver | Domain owner who manages the target glossary namespace |
| audit trail | Required: justification for N/A synonyms, glossary namespace, approver name |
| expiry | Permanent; terminology bypass does not expire |
| never bypass | H01 (corrupt YAML), H05 (self-scored quality invalid), H07 (3-line limit is the defining constraint of this kind — bypass makes it a knowledge_card) |

## Examples

# Examples: glossary-entry-builder
## Golden Example
INPUT: "Define o termo 'kind' no context do CEX"
OUTPUT:
```yaml
id: p01_gl_kind
kind: glossary_entry
pillar: P01
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
term: "kind"
definition: "The artifact type identifier in CEX. Each kind belongs to one pillar and has a unique schema, naming convention, and builder. Examples: knowledge_card, validator, signal."
synonyms: [type, artifact_type]
abbreviation: null
domain: "cex-taxonomy"
domain_specific: "In CEX, kind replaces 'type' to avoid language keyword conflicts and clarify artifact classification."
context: "Used in every artifact frontmatter as the kind field, in TAXONOMY_LAYERS.yaml, and in _schema.yaml files."
disambiguation: "kind is the CEX-specific term. 'type' is the generic programming concept. 'type_def' (P06) is a different artifact that defines costm types."
related_terms: [pillar, layer, artifact, type_def]
usage: "Set kind: glossary_entry in frontmatter. Route via brain_query using kind filter."
quality: 8.8
tags: [glossary, cex-taxonomy, kind, terminology]
tldr: "kind = artifact type identifier in CEX. Belongs to one pillar, has unique schema and builder."
```
## Definition
The artifact type identifier in CEX. Each kind belongs to one pillar and has a unique
schema, naming convention, and builder. Examples: knowledge_card, validator, signal.
## Usage
Set `kind: glossary_entry` in frontmatter. Route via `brain_query` using kind filter.
Every artifact MUST declare its kind. TAXONOMY_LAYERS.yaml lists all 69 kinds.
## Disambiguation
- **kind** vs **type**: kind is CEX-specific; type is generic programming concept
- **kind** vs **type_def**: type_def (P06) defines costm types; kind classifies artifacts
## Related Terms
- pillar: the domain a kind belongs to (P01-P12)
- layer: the functional layer (spec, content, prompt, runtime, governance)
- artifact: any CEX-produced output identified by kind
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p01_gl_ pattern (H02 pass)
- kind: glossary_entry (H04 pass)
- 13+ required fields present (H06 pass)
- definition <= 3 lines (H07 pass)
- synonyms has 2 entries (H08 pass)
- term is non-empty (H09 pass)
- tldr <= 160 chars, dense (S01 pass)
- tags list len >= 3, includes "glossary" (S02 pass)
- YAML parses cleanly (H01 pass)
## Anti-Example
INPUT: "Define kind"
BAD OUTPUT:
```yaml
id: kind_definition
kind: glossary
pillar: Knowledge
term: Kind
definition: Kind is a very important concept in our system. It represents the type of artifact and is used extensively throughout the entire framework ecosystem for various purposes including classification, routing, validation, and many other things that make the system work properly.
synonyms: type
quality: 7.5
tags: glossary
```
Kind is the type of thing in the system. It's used a lot.
FAILURES:
1. id: no `p01_gl_` prefix -> H02 FAIL
2. kind: "glossary" not "glossary_entry" -> H04 FAIL
3. pillar: "Knowledge" not "P01" -> H03 FAIL
4. quality: 7.5 (not null) -> H05 FAIL
5. definition: > 3 lines (verbose) -> H07 FAIL
6. synonyms: string not list -> H08 FAIL
7. tags: string not list, len < 3 -> S02 FAIL
8. body: filler prose ("very important", "used a lot") -> S07 FAIL
9. term: capitalized "Kind" instead of lowercase -> S05 FAIL
10. no disambiguation section -> S06 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
