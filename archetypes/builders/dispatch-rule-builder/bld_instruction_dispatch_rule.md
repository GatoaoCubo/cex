---
kind: instruction
id: bld_instruction_dispatch_rule
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for dispatch_rule
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a dispatch_rule
## Phase 1: CLASSIFY
1. Identify the domain scope for this routing rule (research, build, marketing, orchestration, execute, knowledge, monetize)
2. List 3–8 keywords that trigger this rule, covering both Portuguese and English variants of the domain terms
3. Determine the target satellite and the model it runs (opus for build/execute, sonnet for research/marketing/knowledge)
4. Define the confidence threshold for a keyword match to be considered authoritative (minimum 0.65)
5. Specify fallback behavior when confidence falls below threshold: pass to next rule, route to a default satellite, or reject with an error
6. Assign priority level: 7–8 for core domain rules, 5–6 for supporting or overlapping domains
7. Check existing dispatch_rules in P12 for scope overlap — two rules must not claim the same keywords without explicit priority separation
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints
3. Fill all required frontmatter fields; set `quality: null` — never self-score
4. Write **Keywords** section: full list of PT and EN terms that trigger routing, one per line, lowercase
5. Write **Target** section: satellite name, model, priority level
6. Write **Confidence** section: threshold value and fuzzy matching behavior (exact, stemmed, semantic)
7. Write **Fallback** section: what happens below threshold — next rule name, default satellite, or rejection reason
8. Write **Scope Fence** section: which domains this rule covers and which adjacent domains it explicitly excludes
9. Verify body <= 3072 bytes
## Phase 3: VALIDATE
1. Check all HARD gates in QUALITY_GATES.md
2. Confirm `id` matches `^p12_dr_[a-z][a-z0-9_]+$`
3. Confirm `fallback` satellite differs from the primary `satellite`
4. Confirm `quality` is the literal null, not a number
5. Confirm no runtime status fields are present (`status`, `timestamp`, `quality_score`)
6. Confirm no execution instruction fields are present (`tasks`, `scope_fence`, `commit`)
7. Confirm body <= 3072 bytes
8. Cross-check: is this a routing policy? If it contains execution steps it is a handoff, not a dispatch_rule. If it records events it is a signal. If it sequences workflow stages it belongs in a workflow artifact.
9. If validation fails, revise in the same pass before outputting
