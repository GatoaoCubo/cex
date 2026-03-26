---
pillar: P03
llm_function: REASON
kind: instructions
domain: naming_rule
version: 1.0.0
---

# Instructions — Naming Rule Builder

## Execution Protocol

Three phases: CLASSIFY → COMPOSE → VALIDATE. Each numbered step is ONE action.

---

## Phase 1: CLASSIFY

**Goal**: Establish the exact scope and gather context before writing any pattern.

1. Read the scope description provided in the task input
2. Identify the artifact kind this naming rule governs (e.g., `knowledge_card`, `signal`, `builder_dir`)
3. Identify the CEX pillar this scope belongs to (p01–p12)
4. Run `Grep: pattern="kind: naming_rule"` in `records/pool/` to list existing naming rules
5. Check if a naming rule for this exact scope already exists
6. If existing rule found: read it and determine if update or new version is needed
7. If no existing rule: proceed to Phase 2
8. Identify any sibling naming rules in the same pillar for pattern consistency
9. Note the separator style used by siblings (underscore vs hyphen)
10. Note the case style used by siblings (snake_case vs kebab-case)

---

## Phase 2: COMPOSE

**Goal**: Define the complete naming convention with zero ambiguity.

11. Set `scope` to a one-sentence description of what this rule governs
12. Define `prefix` as the fixed string that all names must start with (e.g., `p01_kc_`)
13. Define `separator` as the single character between name segments (`_` or `-`)
14. Define `case_style` from the allowed enum: snake_case, kebab-case, camelCase, PascalCase, UPPER_SNAKE
15. Define `suffix` as the fixed terminal string, or set to `null` if none
16. Define `versioning` strategy: how version is embedded in the name, or `null` if not versioned
17. Write the `pattern` as a regex: must be testable against all examples
18. Write 3 valid name examples that match the pattern
19. Write 2 invalid name examples that violate the pattern (with reason)
20. Define `collision_strategy`: one of append_sequence, append_hash, append_date, reject, or overwrite
21. Write `tldr` as one sentence: "Naming rule for {scope} artifacts following {pattern_summary}"
22. Assign `keywords` (5–8 terms covering scope, kind, pattern elements)

---

## Phase 3: VALIDATE

**Goal**: Confirm the composed rule is internally consistent and spec-compliant.

23. Test each valid example against the regex — confirm all match
24. Test each invalid example against the regex — confirm all fail
25. Verify `id` follows `^p05_nr_[a-z][a-z0-9_]+$`
26. Verify `OUTPUT_TEMPLATE.md` fields are all present in the artifact
27. Verify `SCHEMA.md` required fields are all populated
28. Verify `quality: null` is set (quality assigned post-review, not self-assigned)
29. Set `density_score` to `REC` (recommended, not computed during authoring)
30. Write the final artifact using `OUTPUT_TEMPLATE.md` structure
