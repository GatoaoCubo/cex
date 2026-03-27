---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for dispatch_rule
pattern: classify -> compose -> validate
---

# Instructions: How to Produce a dispatch_rule

## Phase 1: CLASSIFY
1. Confirm the request is a routing policy, not an execution instruction or runtime event
2. Identify the scope slug for naming: `research`, `build`, `marketing`, `orchestration`
3. Determine which satellite owns this domain (consult KNOWLEDGE.md routing table)
4. Select the appropriate model for that satellite (`opus` for build/execute, `sonnet` for research/marketing)
5. Set priority based on domain criticality (7-8 for core domains, 5-6 for supporting)
6. Identify 3-8 trigger keywords covering PT and EN variants for the scope
7. Choose `fallback` satellite (must differ from primary `satellite`)

## Phase 2: COMPOSE
1. Read SCHEMA.md first — it is the single source of truth for all fields
2. Use OUTPUT_TEMPLATE.md as direct derivative of SCHEMA.md
3. Set filename as `p12_dr_{scope}.yaml`
4. Set `id` as `p12_dr_{scope}` matching filename exactly
5. Set `quality: null` — never assign a numeric score at authoring time
6. Fill `keywords` list with lowercase terms, no punctuation, bilingual where applicable
7. Set `confidence_threshold` >= 0.65 unless domain requires permissive matching
8. Add `routing_strategy` only when non-default (`keyword_match`) is needed
9. Add `conditions` only when AND-conditions beyond keywords are required
10. Write body sections: Purpose, Keyword Rationale, Fallback Logic

## Phase 3: VALIDATE
1. Check all 15 HARD gates in QUALITY_GATES.md
2. Verify `id` matches `^p12_dr_[a-z][a-z0-9_]+$`
3. Verify `fallback` != `satellite`
4. Verify `quality` is literal `null`
5. Verify no runtime status fields are present (`status`, `timestamp`, `quality_score`)
6. Verify no handoff fields are present (`tasks`, `scope_fence`, `commit`)
7. Confirm file size <= 3072 bytes
8. brain_query [IF MCP] `dispatch_rule {scope}` to check for duplicate rules in same scope
9. If validation fails, revise in the same pass before output
