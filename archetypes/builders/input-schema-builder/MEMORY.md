---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: input-schema-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any value)
2. Using hyphens in id slug (must be underscores: p06_is_brain_query, not p06_is_brain-query)
3. Writing fields as a string instead of list[object] (must be structured objects)
4. Missing type on a field (every field MUST have a type)
5. Required field with a default value (required means caller MUST provide)
6. Optional field without a default (optional MUST have default)
7. Using "any" or "mixed" as type (use "object" or "string" with coercion)
8. Drifting into bilateral territory — adding response/output shapes (that is interface P06)

### Input Schema Patterns

| Pattern | When to use | Fields typically |
|---------|-------------|-----------------|
| Simple query | Single search operation | 1-3 fields |
| CRUD operation | Create/update entity | 5-10 fields |
| Configuration | Agent/tool setup | 3-8 fields |
| Filter/search | Complex query with filters | 2-6 fields |
| Batch operation | Multiple items at once | 1-2 fields (list type) |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | required vs optional semantics, coercion rules |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing an input_schema, update:
- New common mistake (if encountered)
- New input schema pattern (if discovered)
- Production counter increment
