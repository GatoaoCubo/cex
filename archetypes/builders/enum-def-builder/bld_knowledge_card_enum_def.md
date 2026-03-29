---
kind: knowledge_card
id: bld_knowledge_card_enum_def
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for enum_def production — enumeration specification
sources: JSON Schema draft-07, Pydantic v2, Zod v3, GraphQL spec June 2018, TypeScript 5.x
---

# Domain Knowledge: enum_def
## Executive Summary
Enumerations are finite named value sets that constrain a field to a known list of options. They are the simplest form of schema constraint — no methods, no structural nesting, no computed properties. An enum_def is reusable: defined once, referenced by many schemas, types, and validators. They must declare extensibility (open vs closed) and handle deprecation explicitly, because consumers (especially exhaustive match in TypeScript/Rust/Swift) rely on the set being stable.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P06 (Schema) |
| llm_function | CONSTRAIN (restricts field values) |
| Min values | 2 (1 value = constant) |
| Value naming | SCREAMING_SNAKE or lowercase — consistent within enum |
| Default | optional; must be member of values |
| Extensible | false = closed/exhaustive; true = open/future values expected |
| Deprecated | subset of values; removal only on major version |
## Framework Patterns
### JSON Schema
```json
{"type": "string", "enum": ["draft", "published", "archived"]}
```
- Values are literals (string, number, boolean, null all supported)
- No per-value metadata in JSON Schema itself — documentation lives in enum_def artifact
- `const` is JSON Schema's single-value form (not enum_def)
### Pydantic (Python)
```python
from enum import Enum
class PublicationStatus(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"
```
- Inherit from `(str, Enum)` for JSON-serializable string enums
- `StrEnum` (Python 3.11+) as alternative: `class Status(StrEnum): DRAFT = auto()`
- Pydantic v2 validates enum membership automatically on model fields
### Zod (TypeScript/JavaScript)
```typescript
const PublicationStatus = z.enum(["draft", "published", "archived"]);
type PublicationStatus = z.infer<typeof PublicationStatus>;
```
- `z.enum()` takes a readonly string tuple — values must be literals, not variables
- `.exclude()` and `.extract()` allow sub-enums without redefining
- `z.nativeEnum()` bridges TypeScript `enum` declarations
### GraphQL
```graphql
enum PublicationStatus {
  DRAFT
  PUBLISHED
  ARCHIVED
}
```
- GraphQL enum values are ALWAYS SCREAMING_SNAKE_CASE (spec requirement)
- Client receives string form; server maps to internal representation
- No per-value arguments or directives in base spec
### TypeScript
```typescript
// Preferred: string literal union (no runtime cost)
type PublicationStatus = "draft" | "published" | "archived";
// Alternative: const enum (erased at compile time)
const enum PublicationStatus { DRAFT = "draft", PUBLISHED = "published" }
// Avoid: numeric enum (loses type safety on serialization)
```
- String literal unions preferred for JSON-serializable enums
- `const enum` acceptable for internal use; avoid for public APIs
- Exhaustive switch: TypeScript enforces all values handled when `extensible: false`
## Patterns
| Pattern | When to use | Example |
|---------|-------------|---------|
| Closed enum | Domain has fixed finite states | HTTP methods: GET, POST, PUT, DELETE, PATCH |
| Open enum | Domain evolves; new values expected | Plugin categories, user-defined tags |
| Lifecycle enum | Ordered state machine states | draft -> review -> published -> archived |
| Category enum | Unordered classification set | artifact kind, pillar code, log level |
| Flag-like enum | Values combined additively | permissions: READ, WRITE, ADMIN |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Single-value enum | Use constant-builder instead; enum implies choice |
| Values without descriptions | Consumer cannot distinguish similar values (ACTIVE vs ENABLED) |
| Mixed case convention | DRAFT and published in same enum breaks serialization parity |
| Missing extensible declaration | Consumers cannot safely use exhaustive match |
| Removing deprecated values without major bump | Breaks consumers with exhaustive match |
| Embedding business logic in enum names | STATUS_WAITING_FOR_APPROVAL is a workflow state, not a value name |
| Using enums for open-ended categories | If values grow unboundedly, use a taxonomy or tag system instead |
## Application
1. Identify: what field is being constrained? What are all meaningful distinct values?
2. Name: pick a case convention and apply it uniformly across all values
3. Describe: write one sentence per value explaining meaning and when to use it
4. Declare: extensible true/false, default if applicable, deprecated if any
5. Represent: produce JSON Schema + at least one of Pydantic/Zod/TypeScript forms
6. Validate: >= 2 values, all deprecated in values, default in values, body <= 1024 bytes
## References
- JSON Schema draft-07: `enum` and `const` keywords
- Pydantic v2 docs: enum field validation
- Zod v3 docs: z.enum(), z.nativeEnum()
- GraphQL June 2018 spec: enum type definition
- TypeScript handbook: string literal types, const enums
