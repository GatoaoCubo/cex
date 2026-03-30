# P06 Schema — Ecosystem Map
> Generated: 2026-03-28 | Author: builder_agent

## 1. Frameworks Audited
| Framework | Domain | Key Concepts |
|-----------|--------|--------------|
| JSON Schema draft-2020 | Schema standard | $schema, $ref, $defs, allOf/anyOf/oneOf, if/then/else, unevaluatedProperties, prefixItems |
| Pydantic v2 | Python validation | BaseModel, Field (alias, description, default, validators), model_validator, field_validator, TypeAdapter, ConfigDict |
| Zod | TypeScript validation | z.object(), z.string(), z.number(), z.enum(), z.union(), z.discriminatedUnion(), z.transform(), z.refine() |
| OpenAPI 3.1 | API contracts | Schema Object (JSON Schema superset), RequestBody, Response, Components, Discriminator, Webhook |
| GraphQL SDL | Type language | type, input, interface, union, enum, scalar, directive, subscription, schema stitching |
| Protobuf | Binary serialization | message, field (type + number), enum, oneof, map, service, rpc, import, package |
| TypeBox | JSON Schema builder | Type.Object(), Type.String(), Type.Optional(), Type.Union(), Type.Ref(), TypeCompiler |
| Valibot | Modular validation | object(), string(), number(), pipe(), transform(), custom(), flatten errors, tree-shakable |
| ArkType | TypeScript-first | type(), morph(), narrow(), scope(), unit types, branded types, cyclic references |

## 2. Industry Concepts Found
| Concept | Framework(s) | Description | Frequency |
|---------|-------------|-------------|:---------:|
| Input Schema/Contract | JSON Schema, Pydantic (BaseModel), Zod (z.object), OpenAPI (RequestBody), GraphQL (input), Protobuf (message) | Formal definition of required input fields and their types | 8 |
| Type Definition | Pydantic (BaseModel), Zod (z.object), GraphQL (type), Protobuf (message), TypeBox, Valibot, ArkType | Custom composite type with named fields | 7 |
| Validator/Rule | Pydantic (field_validator, model_validator), Zod (z.refine), Valibot (pipe+custom), ArkType (narrow) | Custom validation logic beyond type checking (ranges, patterns, cross-field) | 6 |
| Interface/Contract | GraphQL (interface), OpenAPI (Components), Protobuf (service/rpc), TypeBox (Type.Ref) | Shared type definition that multiple producers/consumers agree on | 5 |
| Output/Response Schema | JSON Schema, OpenAPI (Response), Pydantic, Zod | Formal definition of output/response shape | 6 |
| Union/Discriminated Union | Zod (z.discriminatedUnion), Pydantic (Discriminated Union), GraphQL (union), JSON Schema (oneOf), Protobuf (oneof) | Type that can be one of several shapes, determined by discriminator field | 6 |
| Enum/Literal | Pydantic (Literal), Zod (z.enum), GraphQL (enum), Protobuf (enum), JSON Schema (enum), ArkType (unit) | Fixed set of allowed values | 7 |
| Transform/Coerce | Zod (z.transform), Pydantic (validators that transform), Valibot (transform), ArkType (morph) | Convert input value during validation (string→date, trim, lowercase) | 4 |
| Reference/Composition | JSON Schema ($ref, $defs), OpenAPI (Components), Protobuf (import), GraphQL (type composition) | Reuse type definitions via reference | 5 |
| Error Format | Pydantic (ValidationError), Zod (ZodError), Valibot (flatten), ArkType (ArkErrors) | Structured error reporting with path, message, code | 4 |
| Schema Versioning | OpenAPI (info.version), JSON Schema ($schema), Protobuf (field numbering for backward compat) | Evolving schemas while maintaining backward compatibility | 3 |

## 3. CEX Current vs Industry
| CEX Kind | Maps To | Coverage % | Gap |
|----------|---------|:----------:|-----|
| input_schema | Input Schema/Contract | 90% | Direct match. CEX uses JSON format. Well-aligned with JSON Schema + Pydantic + Zod patterns. |
| type_def | Type Definition | 85% | Good match. CEX type_def = custom composite type. Industry has richer features (generics, branded types, discriminated unions). |
| validator | Validator/Rule | 80% | Good match. CEX validator is pass/fail rule. Industry validators can also transform (Zod, Pydantic). CEX correctly keeps transform out of scope. |
| interface | Interface/Contract | 75% | Reasonable match. CEX interface = bilateral agent contract. Industry interface = shared type (GraphQL interface). CEX is more specific (agent-to-agent), which is valid. |
| validation_schema | Output/Response Schema | 70% | Partial overlap with P05 response_format. CEX distinguishes: response_format = LLM sees it, validation_schema = system applies post-generation. Industry doesn't always make this distinction. |

## 4. Proposed NEW Kinds (ONLY if 2+ frameworks use it)
| Kind | Justification | Frameworks | Priority |
|------|---------------|------------|:-------:|
| enum_def | Standalone enumeration of allowed values. Currently embedded inside type_def/input_schema fields. Every schema framework has first-class enums. Extracting them enables reuse across schemas. | Pydantic (Literal/Enum), Zod (z.enum), GraphQL (enum), Protobuf (enum), JSON Schema (enum) | med |
| transform_rule | Input coercion/normalization applied during validation (string→date, trim, lowercase). Distinct from validator (which rejects) — transforms accept-and-modify. Industry increasingly separates these. | Zod (z.transform), Pydantic (validators), Valibot (transform), ArkType (morph) | low |

## 5. Proposed REMOVALS/RENAMES
| Kind | Action | Reason |
|------|--------|--------|
| validation_schema | CLARIFY vs P05 response_format | The CEX distinction (response_format = LLM-visible, validation_schema = system-applied post-gen) is valid but confusing. Consider renaming to `post_gen_schema` or `output_contract` to reduce ambiguity. |
| interface | KEEP with scope note | CEX interface is agent-to-agent bilateral contract. Industry "interface" is a shared type definition. Both valid — document the difference in boundary. |

## 6. KEEPS (validated)
| Kind | Frameworks That Match |
|------|----------------------|
| input_schema | JSON Schema, Pydantic BaseModel, Zod z.object, OpenAPI RequestBody, GraphQL input type, Protobuf message |
| type_def | Pydantic BaseModel, Zod z.object, GraphQL type, Protobuf message, TypeBox Type.Object, Valibot object |
| validator | Pydantic field_validator/model_validator, Zod z.refine, Valibot pipe+custom, ArkType narrow |
| interface | GraphQL interface, OpenAPI Components, Protobuf service/rpc |
| validation_schema | JSON Schema (output validation), OpenAPI Response schema, Pydantic (response validation) |

## 7. Summary
Current: 5 kinds → Proposed: 7 kinds (+enum_def, +transform_rule) | Coverage: ~80% → ~90%

Key insight: CEX P06 is already well-structured and closely aligned with industry. The schema space is mature (JSON Schema is 15+ years old). The main opportunities are: (1) **enum_def** as a reusable first-class kind (every framework has standalone enums), and (2) clarifying the validation_schema vs response_format boundary which trips up newcomers. The transform_rule concept is growing but lower priority.
