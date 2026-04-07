---
kind: knowledge_card
id: bld_knowledge_card_validation_schema
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for validation_schema production — atomic searchable facts
sources: validation-schema-builder MANIFEST.md + SCHEMA.md
---

# Domain Knowledge: validation_schema
## Executive Summary
A `validation_schema` (P06) is a post-generation structural contract the system enforces automatically — the LLM never sees it. It differs from `response_format` (injected into the prompt, guides LLM during generation), `validator` (individual explicit pass/fail rule), and `input_schema` (input contract) by being applied silently by infrastructure after output is produced. It defines what fields must exist, their types, constraints, and what happens on failure (`reject`, `warn`, or `auto_fix`).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P06 |
| Kind | `validation_schema` |
| ID pattern | `^p06_vs_[a-z][a-z0-9_]+$` |
| Naming | `p06_vs_{scope}.yaml` |
| Max body | 4096 bytes |
| Machine format | json |
| Required frontmatter fields | 13 |
| Recommended fields | 6 |
| `on_failure` values | `reject`, `warn`, `auto_fix` |
| `quality` field | always `null` |
| LLM visibility | Never — system-side only |
| Derivation order | SCHEMA (P06) > TEMPLATE (P03) > CONFIG (P04) |
## Patterns
| Pattern | Rule |
|---------|------|
| JSON types only | `string`, `integer`, `number`, `boolean`, `array`, `object` — no costm types |
| Required vs Recommended split | Required fields → HARD gate; Recommended → SOFT gate |
| 5-column fields table | Field, Type, Required, Default, Notes — all mandatory; Default = `--` for required |
| `on_failure` per criticality | Critical fields (`id`, `kind`) → `reject`; style/recommended → `warn`; safe coercions → `auto_fix` |
| ID == filename stem | `id` value must exactly match the filename without extension |
| `strict: true` | Rejects unknown fields; use when schema must be exhaustive |
| Constraint composition order | type → format → content (avoids confusing error messages) |
**Constraint syntax reference**:
| Constraint | Syntax | Use case |
|------------|--------|----------|
| Regex | `pattern: "^p06_vs_[a-z][a-z0-9_]+$"` | IDs, naming |
| Enum | `enum: [reject, warn, auto_fix]` | Closed value sets |
| Range | `min: 1, max: 100` | Numeric bounds |
| Length | `min_length: 3, max_length: 160` | String limits |
| Size | `max_bytes: 4096` | Payload limits |
| List minimum | `len >= 3` | Diversity gates |
**Boundary — what validation_schema is NOT**:
| kind | Why NOT validation_schema |
|------|--------------------------|
| `response_format` | Injected into prompt — LLM sees it during generation |
| `validator` | Explicit named pass/fail rule, not a silent contract |
| `input_schema` | Governs inputs entering the system, not outputs |
| `quality_gate` | Weighted scoring barrier — not structural enforcement |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Schema injected into prompt | LLM hallucination risk; validation_schema is system-only |
| Ambiguous field types ("data", "any") | JSON types only; ambiguous types break enforcement |
| Missing `on_failure` | System has no behavior contract; silently ignores violations |
| Impossible constraints (`min > max`) | Validation always fails; artifact is permanently blocked |
| `quality` set to a score | Never self-score; governance assigns |
| Template/config adding unknown fields | Schema is upstream; downstream must not exceed schema |
| `auto_fix` on lossy coercions | Data loss is unsafe; only coerce safe conversions (string "42" → int 42) |
## Application
1. Identify `target_kind` — the artifact kind this schema validates
2. Set `id` = `p06_vs_{scope}`, must equal filename stem
3. Set `on_failure` globally (can override per-field in body)
4. Enumerate all fields of the target kind, split into Required and Recommended
5. Write the Fields Table with all 5 columns per row (Field, Type, Required, Default, Notes)
