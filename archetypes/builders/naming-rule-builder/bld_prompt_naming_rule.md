---
id: p03_ins_naming_rule
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Naming Rule Builder Instructions
target: naming-rule-builder agent
phases_count: 3
prerequisites:
  - Scope of the naming convention is explicitly stated (artifact type, domain, or system area)
  - At least one example name or candidate name is available
  - Target platform or environment is known (filesystem, code identifier, URL slug, etc.)
validation_method: checklist
domain: naming_rule
quality: 9.1
tags:
  - instruction
  - naming-rule
  - convention
  - P05
idempotent: true
atomic: false
rollback: "Delete the produced naming_rule artifact file; no system state changes occur"
dependencies: []
logging: true
tldr: "Classify naming scope, derive regex pattern and collision strategy, validate and write a naming_rule artifact to `p05_nr_{{scope}}.md`."
density_score: 0.88
llm_function: REASON
related:
  - bld_knowledge_card_naming_rule
  - bld_memory_naming_rule
  - bld_collaboration_naming_rule
  - p03_sp_naming_rule_builder
  - p11_qg_naming_rule
  - p01_kc_naming_rule
  - bld_examples_naming_rule
  - bld_config_naming_rule
  - naming-rule-builder
  - bld_schema_naming_rule
---
## Context
The naming-rule-builder receives a **scope definition** and produces a `naming_rule` artifact encoding the naming convention for that scope.
**Input variables**:
- `{{scope}}` — category of entity being named (e.g., `knowledge_card`, `signal`, `builder_dir`)
- `{{examples}}` — 1–5 candidate or existing names that must conform to the rule
- `{{platform}}` — constraining environment: `filesystem`, `python_identifier`, `url_slug`, `yaml_key`
- `{{constraints}}` — optional known requirements: max length, required prefix, version segment
**Output**: a single `naming_rule` artifact at `p05_nr_{{scope}}.md` with a testsble regex, valid/invalid examples, and a collision resolution strategy.
**Boundaries**: defines conventions only. Does NOT validate existing names (validator), define entity semantics (type_def), or format output (formatter-builder).
## Phases
### Phase 1: CLASSIFY
**Goal**: Establish the exact scope, gather pattern constraints, and check for existing rules before writing.
1. Parse `{{scope}}`. Identify the artifact kind this rule governs and its CEX pillar (p01–p12).
2. Search for an existing naming rule for this scope (grep `kind: naming_rule` in records/pool/ or use brain_query). If one exists, read it and determine whether an update or new version is needed.
3. Identify sibling naming rules in the same pillar. Note their separator style (underscore vs hyphen) and case style (snake_case vs kebab-case) for consistency.
4. Inspect each example in `{{examples}}`. Extract:
   - separator in use (`_`, `-`, `.`, camelCase boundary)
   - case style (lowercase, UPPER, PascalCase, camelCase, kebab-case, snake_case)
   - required prefix or suffix patterns
   - presence of a version segment (e.g., `_v2`, `-1.0.0`)
5. Map `{{platform}}` to its hard character constraints:
   - `filesystem/windows`: no `\/:*?"<>|`, max 260 chars total
   - `filesystem/linux`: no `/` or null byte, case-sensitive
   - `python_identifier`: `[a-zA-Z_][a-zA-Z0-9_]*`, no reserved keywords
   - `url_slug`: RFC 3986 unreserved chars only (`[A-Za-z0-9\-._~]`)
6. Record minimum and maximum name lengths observed in examples.
```
constraints_map = {
  separator: <inferred>,
  case: <inferred>,
  prefix: <explicit or null>,
  suffix: <explicit or null>,
  max_length: <platform max or example-derived>,
  versioning: <present or absent>,
  reserved_words: <platform list>
}
```
**Exit**: all 5 structural dimensions (separator, case, prefix/suffix, length, versioning) are resolved or explicitly marked unconstrained.
### Phase 2: COMPOSE
**Goal**: Produce the regex, examples, collision strategy, and complete artifact body.
7. Translate `constraints_map` into regex components. Always include `^` and `$` anchors. Use named groups if the platform allows.
8. Construct the full `{{pattern}}` regex string. Verify it compiles.
9. Generate 3 **valid** names that match the regex.
10. Generate 2 **invalid** names that violate the regex. For each, state the specific constraint it breaks.
11. Test all input `{{examples}}` against the regex. If any fail, revise `constraints_map` in step 6 and rebuild the regex.
12. Set `{{collision_strategy}}` to one of: `append_sequence`, `append_hash`, `append_date`, `reject`, `namespace_qualify`. Document: uniqueness scope, detection mechanism, automation level, and reserved name segments.
13. Write `tldr` as one sentence: "Naming rule for `{{scope}}` artifacts following `{{pattern_summary}}`."
14. Assign 5–8 `keywords` covering scope, kind, and pattern elements.
15. Set `quality: null` and `density_score: REC`.
**Exit**: regex matches all 3 valid examples, rejects all 2 invalid examples, and matches all input `{{examples}}`.
### Phase 3: VALIDATE
**Goal**: Confirm internal consistency and spec compliance before writing the file.
16. Verify `id` matches `^p05_nr_[a-z][a-z0-9_]+$`.
17. Verify `pattern` field compiles as a valid regex without error.
18. Confirm `quality: null` is set (never self-assign a score).
19. Confirm `OUTPUT_TEMPLATE.md` and `SCHEMA.md` required fields are all populated.
20. Confirm the filename will be `p05_nr_{{scope}}.md` with scope in kebab-case.
21. If any HARD gate fails, return to Phase 2 and correct. Do not output a failing artifact.
22. Write the final artifact using the Output Contract template below.
## Output Contract
```
id: `p05_nr_{{scope}}`
kind: naming_rule
pillar: P05
domain: `{{scope}}`
version: 1.0.0
created: `{{date}}`
author: naming-rule-builder
scope: `{{scope_description}}`
pattern: "`{{regex_pattern}}`"
case_style: `{{case_style}}`
separator: "`{{separator_char}}`"
max_length: `{{max_length}}`
versioning: {{true|false}}
collision_strategy: `{{collision_strategy}}`
quality: null
tags: [naming-rule, `{{scope}}`, convention]
## Pattern
`{{regex_pattern}}`
**Case style**: `{{case_style}}` | **Separator**: `{{separator_char}}` | **Max length**: `{{max_length}}`
## Constraints
| Dimension | Rule |
|-----------|------|
| Prefix | `{{prefix_rule}}` |
| Suffix | `{{suffix_rule}}` |
| Versioning | `{{versioning_rule}}` |
| Reserved words | `{{reserved_words_list}}` |
| Platform | `{{platform}}` |
## Examples
**Valid**: `{{example_valid_1}}`, `{{example_valid_2}}`, `{{example_valid_3}}`
**Invalid**:


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_naming_rule]] | upstream | 0.45 |
| [[bld_memory_naming_rule]] | downstream | 0.40 |
| [[bld_collaboration_naming_rule]] | downstream | 0.37 |
| [[p03_sp_naming_rule_builder]] | related | 0.36 |
| [[p11_qg_naming_rule]] | downstream | 0.35 |
| [[p01_kc_naming_rule]] | downstream | 0.34 |
| [[bld_examples_naming_rule]] | downstream | 0.33 |
| [[bld_config_naming_rule]] | downstream | 0.30 |
| [[naming-rule-builder]] | downstream | 0.30 |
| [[bld_schema_naming_rule]] | downstream | 0.29 |
