---
kind: examples
id: bld_examples_glossary_entry
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of glossary_entry artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: glossary-entry-builder
## Golden Example
INPUT: "Define o termo 'kind' no contexto do CEX"
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
disambiguation: "kind is the CEX-specific term. 'type' is the generic programming concept. 'type_def' (P06) is a different artifact that defines custom types."
related_terms: [pillar, layer, artifact, type_def]
usage: "Set kind: glossary_entry in frontmatter. Route via brain_query using kind filter."
quality: null
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
- **kind** vs **type_def**: type_def (P06) defines custom types; kind classifies artifacts
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
