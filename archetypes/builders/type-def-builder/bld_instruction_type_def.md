---
id: p03_ins_type_def
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Type Def Builder Instructions
target: "type-def-builder agent"
phases_count: 4
prerequisites:
  - "Type name is defined and follows kebab-case convention"
  - "Base type is identified: string, integer, number, boolean, object, array, or union"
  - "At least one constraint or composition rule is specified"
  - "Serialization target format is known: JSON, YAML, or Protobuf"
validation_method: checklist
domain: type_def
quality: null
tags: [instruction, type-def, spec, data-model, P06]
idempotent: true
atomic: true
rollback: "Delete generated type_def YAML; remove references from dependent input_schema and validator artifacts"
dependencies: []
logging: true
tldr: "Build a precise type_def YAML that declares base type, constraints, composition rules, nullable semantics, generics, and serialization spec."
density_score: 0.91
---

## Context

The type-def-builder produces a `type_def` artifact -- a machine-parseable YAML that declares a reusable custom type. These types form the vocabulary layer that other artifacts reference: `input_schema` uses them to define field types, `validator` uses them to enforce constraints, and `grammar` uses them for structural rules.

**Critical distinction**: `type_def` is purely declarative vocabulary. It does NOT define input validation contracts (`input_schema`), pass/fail enforcement rules (`validator`), or integration interfaces (`interface`). Confusing these produces types that duplicate validation logic they should not own.

**Input contract**:
- `type_name`: string -- kebab-case identifier (e.g. `iso-score`, `agent-id`, `wave-index`)
- `base_type`: enum -- `string` | `integer` | `number` | `boolean` | `object` | `array` | `union`
- `description`: string -- one sentence describing what values this type represents
- `constraints`: list of constraint objects (see Phase 2)
- `composition`: object or null -- union/intersection/discriminated-union definition
- `nullable`: boolean -- whether null is a valid value
- `generics`: list of type parameters or null (e.g. `[T]` for `list<T>`)
- `serialization`: object -- format-specific encoding rules per target format
- `examples`: list of 2-3 valid example values

**Output contract**: a single `type_def` YAML with all required fields, stored at `records/type_defs/{type_name}.yaml`.

**Variables**:
- `{{type_name}}` -- kebab-case type identifier
- `{{base_type}}` -- base type enum value
- `{{constraint_N}}` -- Nth constraint object
- `{{serialization_json}}` -- JSON encoding rule
- `{{serialization_yaml}}` -- YAML encoding rule

---

## Phases

### Phase 1: Classify Type and Identify Composition Pattern

**Action**: Determine the structural category of the type being defined.

```
IF base_type == "union":
    composition_kind = "union"
    REQUIRE: composition.members list with >= 2 types
    IF members share overlapping fields:
        REQUIRE: composition.discriminator (a literal string field)

ELIF base_type == "object" AND composition is not null:
    IF composition.kind == "intersection":
        composition_kind = "intersection"
        REQUIRE: composition.of list with >= 2 base object types
    ELSE:
        composition_kind = "extension"

ELSE:
    composition_kind = "primitive_or_constrained"
    composition = null
```

For discriminated unions: the discriminator field must be a literal string type present in all union members.

Verifiable exit: composition_kind is set; union types have >= 2 members; discriminated unions have a discriminator field identified.

### Phase 2: Define Constraint Set

**Action**: Translate each constraint requirement into a structured constraint object.

Constraint object schema:
```
{
  kind: enum [min, max, min_length, max_length, pattern, enum_values,
              min_items, max_items, unique_items, required_keys, custom],
  value: the constraint threshold, pattern, or list,
  error_message: string (human-readable violation message)
}
```

Constraint rules by base_type:
```
string  -> allowed: min_length, max_length, pattern, enum_values
integer -> allowed: min, max, enum_values
number  -> allowed: min, max (inclusive/exclusive flag optional)
array   -> allowed: min_items, max_items, unique_items
object  -> allowed: required_keys, custom
union   -> constraints apply to the resolved member type, not the union itself
```

Cross-type rules: `pattern` requires a valid regex; `enum_values` requires >= 2 distinct values; `min` must be <= `max` when both are present.

Verifiable exit: each constraint has kind, value, and error_message; no invalid constraint for the base_type.

### Phase 3: Specify Serialization Rules

**Action**: Define encoding behavior per serialization format.

```
FOR each target_format in [json, yaml, protobuf]:
    IF target_format in serialization input:
        encode_rule = provided rule
    ELSE:
        encode_rule = derive_default(base_type, target_format)

Default derivation:
  json:    string->string, integer->number, number->number,
           boolean->true/false, object->object, array->array
  yaml:    same as json with YAML scalar rules
  protobuf: string->wire2, integer->int32/int64, number->double,
            boolean->bool, object->message, array->repeated field
```

Verifiable exit: at least JSON serialization rule is defined; all rules are format-consistent.

### Phase 4: Validate Against Quality Gates

**Action**: Run 8 HARD gates before emitting; log 4 SOFT gates as warnings.

```
HARD gates (all must pass):
  H1: type_name is kebab-case and non-empty
  H2: base_type is one of the 7 valid enum values
  H3: description is a single sentence
  H4: at least one constraint is defined, or composition is defined for union/object
  H5: union types have >= 2 composition members
  H6: each constraint has kind, value, and error_message
  H7: at least JSON serialization rule is present
  H8: examples list has >= 2 valid values satisfying all constraints

SOFT gates (log warnings):
  S1: type_name does not shadow a primitive type name (string, int, bool)
  S2: nullable is explicitly set (not defaulted silently)
  S3: protobuf serialization defined if artifact is used in wire protocols
  S4: generics parameters use single uppercase letter convention (T, K, V)
```

Verifiable exit: 8/8 HARD gates pass; SOFT gate failures are logged.

---

## Output Contract

```yaml
id: type_def_{{type_name}}
kind: type_def
pillar: P06
version: 1.0.0
type_name: {{type_name}}
base_type: {{base_type}}
description: "{{description}}"
nullable: {{nullable}}
generics: {{generics}}
constraints:
  - kind: {{constraint_1_kind}}
    value: {{constraint_1_value}}
    error_message: "{{constraint_1_error_message}}"
composition: {{composition}}
serialization:
  json: "{{serialization_json}}"
  yaml: "{{serialization_yaml}}"
  protobuf: "{{serialization_protobuf}}"
examples:
  - {{example_1}}
  - {{example_2}}
created: "{{created}}"
updated: "{{updated}}"
```

---

## Validation

- [ ] H1: type_name is kebab-case and non-empty
- [ ] H2: base_type is one of string, integer, number, boolean, object, array, union
- [ ] H3: description is exactly one sentence
- [ ] H4: at least one constraint or composition rule is defined
- [ ] H5: union base_type has >= 2 composition members
- [ ] H6: every constraint object has kind, value, and error_message
- [ ] H7: JSON serialization rule is present
- [ ] H8: examples list contains >= 2 valid values

---

## Metacognition

**Does**:
- Produce a single reusable type declaration consumed by other spec artifacts
- Enforce constraint validity per base type (no invalid constraints)
- Specify serialization rules to prevent encoding ambiguity across formats
- Validate 8 HARD gates before emitting

**Does NOT**:
- Define input validation contracts (input_schema handles that)
- Encode pass/fail enforcement rules (validator handles that)
- Define integration surface contracts (interface handles that)
- Execute any runtime behavior -- purely declarative

**Chaining**: type-def-builder output is consumed by input-schema-builder (field type references), validator-builder (constraint enforcement), and grammar-builder (structural rules). Build type_def before the artifacts that reference it.
