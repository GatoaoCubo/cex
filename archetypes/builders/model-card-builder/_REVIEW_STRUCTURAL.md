# Structural Review — model-card-builder
## Date: 2026-03-26
## Reviewer: EDISON (opus)
## Score: 8.5/10

---

## CRITICAL (blocks production)

- **C01: LP collision (SYSTEM_PROMPT + INSTRUCTIONS both P03)** — If LP determines loading order, two files at P03 creates ambiguity. One must yield. Recommendation: INSTRUCTIONS -> P03.5 or renumber to P03a/P03b, or better: SYSTEM_PROMPT stays P03, INSTRUCTIONS becomes P04 (shift all subsequent).

- **C02: Missing comparison_card example** — INSTRUCTIONS.md Phase Variants says "For comparison: use EXAMPLES.md comparison variant" but EXAMPLES.md has NO comparison_card example. Builder invoked for comparison will hallucinate format. Must add a golden comparison_card example before production.

- **C03: SCHEMA omits comparison_card size limit** — CONFIG.md defines two limits: 3072 (spec_card) and 4096 (comparison_card). SCHEMA.md Constraints only mentions `max_bytes: 3072` without variant distinction. QUALITY_GATES has no gate for variant-specific size. Any comparison_card over 3072 bytes would fail validation despite CONFIG allowing 4096.

---

## IMPROVEMENT (raises quality)

- **I01: Frontmatter field inconsistency across ISO files** — MANIFEST.md has `id` field; the other 12 files do not. If `id` is required for brain indexing of ISO files themselves, all 13 need it. If only the builder identity needs `id`, document this exception.

- **I02: Version/date quoting inconsistency in golden example** — OUTPUT_TEMPLATE.md uses quoted strings for version (`"1.0.0"`) and dates (`"{{YYYY-MM-DD}}"`). The golden example in EXAMPLES.md uses unquoted (`version: 1.0.0`, `created: 2026-03-26`). YAML treats both the same, but the template should match the example for copy-paste reliability.

- **I03: Template pseudo-code breaks {{var}} pattern** — OUTPUT_TEMPLATE.md Capabilities table contains `{{for each feature: name | bool | detail}}` which is a loop instruction, not a {{var}} substitution. All other template vars are simple replacements. This one requires the LLM to interpret differently. Recommend: list all 8 feature rows explicitly (matching SCHEMA features object), using {{bool}} placeholders.

- **I04: Boot Flow layer gap** — ARCHITECTURE.md diagram shows layers 0, 1, 2, 4 — skips layer 3. Either layer 3 exists (mental_model is layer 2, what's layer 3?) or the numbering should be 0-1-2-3. Diagram says `[agent] <- layer 4` but if there are only 4 layers, it should be layer 3.

- **I05: QUALITY_GATES S03 edge case** — S03 checks "pricing has concrete numbers (not null for commercial)". Some commercial models have free tiers (e.g., Gemini Flash free tier). Gate should handle: commercial + free tier = pricing: 0.00 (not null), distinguishing from open-weight null.

- **I06: When to Use table in golden example only has 3 rows** — SCHEMA requires `>= 3 rows`. The example meets the minimum but barely. For a GOLDEN example (targeting 9.5+), 4-5 rows would demonstrate range better. Not a bug, but a missed coaching opportunity.

---

## DEBT (fix later)

- **D01: cex_forge.py existence unverified** — TOOLS.md references `cex_forge.py` as "Alternative to manual compose". If this tool doesn't exist yet, mark it as `[PLANNED]` to prevent the builder from attempting to call it.

- **D02: Future builders referenced in COLLABORATION.md** — 6 builders mentioned (agent-builder, boot-config-builder, system-prompt-builder, skill-builder, quality-gate-builder, iso-package-builder, satellite-spec-builder, benchmark-builder, scoring-rubric-builder) that don't exist yet. Expected for first archetype, but should have `[PLANNED]` markers to signal they're forward references, not broken links.

- **D03: MEMORY.md Pricing Sources mostly unverified** — Only Anthropic has "Last verified" date. Other 4 providers show "—". Initial state is fine, but the refresh protocol (quarterly) needs an automation trigger or it'll go stale silently.

- **D04: MEMORY.md Production Counter is empty** — Section describes intent but has no data. After first production run, this should be populated. Consider: add a zero-state template so the update protocol is clear.

- **D05: Naming convention not explicitly documented** — kebab-case for builder names (`model-card-builder`), snake_case for data fields (`context_window`), lowercase for provider enum. This mix is intentional and correct, but no single file states this rule. CONFIG.md covers artifact naming but not builder/field naming.

- **D06: MANIFEST llm_function debate** — MANIFEST uses `llm_function: BECOME` (identity). Could be argued as CONSTRAIN (manifest constrains what the builder is). Not wrong, but when scaling to 80 builders, the convention should be explicit: "MANIFEST always uses BECOME because it defines builder identity."

---

## FILE-BY-FILE

### MANIFEST.md (P02)
- **Structure**: 4 sections (Identity, Capabilities, Routing, Crew Role). Clean, concise.
- **Consistency**: `type: type_builder` (not `model_card`) — correct, this is the builder, not its output.
- **Cross-refs**: Crew Role boundary matches ARCHITECTURE.md boundary table.
- **Density**: High. No filler.
- **Issues**: See I01 (only file with `id` in frontmatter).

### SYSTEM_PROMPT.md (P03)
- **Structure**: Rules (8) + Boundary. Exactly what a system prompt needs.
- **Consistency**: All 8 rules map to concrete QUALITY_GATES checks.
- **Cross-refs**: Rule 3 (per_1M_tokens) = CONFIG pricing convention. Rule 7 (90 days) = CONFIG freshness. All verified.
- **Density**: Excellent. Every rule is actionable.
- **Issues**: See C01 (LP collision with INSTRUCTIONS).

### KNOWLEDGE.md (P01)
- **Structure**: Foundational Standard, Industry Implementations, Universal Fields, Key Patterns, CEX-Extensions, References.
- **Consistency**: Best file in the set. 4 satellite sources credited. Industry table covers 6 implementations.
- **Cross-refs**: CEX-Extensions table justifies every non-standard field with closest industry equivalent.
- **Density**: 0.95+. Pure information, zero filler.
- **Issues**: None. This is golden-quality domain knowledge.

### INSTRUCTIONS.md (P03)
- **Structure**: 3 phases (RESEARCH/COMPOSE/VALIDATE) + Variants.
- **Consistency**: Phase references match existing files (OUTPUT_TEMPLATE, ARCHITECTURE, QUALITY_GATES, EXAMPLES).
- **Cross-refs**: See C02 (comparison variant referenced but absent in EXAMPLES).
- **Density**: Good but Phase 3 step 7 ("loop back") is aspirational — single-pass LLM can't truly loop. Should say "revise in same pass" or "flag for re-invocation".
- **Issues**: C01 (LP collision), C02 (missing comparison example).

### TOOLS.md (P04)
- **Structure**: Production Tools table + Data Sources + Validation Tools.
- **Consistency**: Data Sources URLs are real and verifiable. Validation Tools align with QUALITY_GATES HARD gates.
- **Cross-refs**: validate_kc.py referenced (exists in codexa-core). cex_forge.py status unknown (D01).
- **Density**: Good. Compact tables.
- **Issues**: D01 (cex_forge.py unverified).

### OUTPUT_TEMPLATE.md (P05)
- **Structure**: Single YAML template with {{vars}} for all 26 frontmatter fields + 5 body sections.
- **Consistency**: All 26 fields match SCHEMA. Body sections match SCHEMA required list.
- **Cross-refs**: id pattern `p02_mc_{{provider}}_{{model_slug}}` matches CONFIG naming.
- **Density**: Template by nature — appropriate.
- **Issues**: I02 (quoting), I03 (pseudo-code loop in Capabilities).

### SCHEMA.md (P06)
- **Structure**: Frontmatter Fields table (26 rows) + Body Structure + Constraints.
- **Consistency**: Field types, required flags, and sources are well-defined. Source column credits industry standard per field.
- **Cross-refs**: Body Structure 5 sections = OUTPUT_TEMPLATE 5 sections. Constraints naming = CONFIG naming.
- **Density**: High. No prose, pure specification.
- **Issues**: C03 (missing comparison_card size limit).

### EXAMPLES.md (P07)
- **Structure**: Golden Example (spec_card) + Anti-Example + WHY annotations.
- **Consistency**: Golden example passes all 10 HARD gates mentally. Anti-example violates 10+ rules with clear annotations.
- **Cross-refs**: Golden uses id pattern from CONFIG/SCHEMA. Tags as list. quality: null.
- **Density**: Good — the WHY annotations add teaching value.
- **Issues**: C02 (no comparison_card variant). I06 (minimal When to Use rows). I02 (quoting inconsistency).

### ARCHITECTURE.md (P08)
- **Structure**: Boundary table + Boot Flow diagram + Dependency Graph + Fractal Position + Variants.
- **Consistency**: Most thorough boundary definition. 5 "confusion" cases handled with correct type redirects.
- **Cross-refs**: Dependency graph matches COLLABORATION.md dependents list. Variants match INSTRUCTIONS variants.
- **Density**: Excellent. Diagram + table + graph in 60 lines.
- **Issues**: I04 (layer numbering gap).

### CONFIG.md (P09)
- **Structure**: Naming + File Paths + Size Limits + Provider Enum + Pricing Convention + Freshness.
- **Consistency**: Naming pattern matches SCHEMA. Provider enum is superset (includes "other" fallback). Pricing convention is the most detailed treatment.
- **Cross-refs**: Density >= 0.85 matches QUALITY_GATES S13. Freshness 90 days matches KNOWLEDGE/SYSTEM_PROMPT.
- **Density**: High. Operational rules, no narrative.
- **Issues**: C03 (comparison_card size limit defined here but not in SCHEMA).

### MEMORY.md (P10)
- **Structure**: Pricing Sources + Common Mistakes + Model Families + Production Counter + State protocol.
- **Consistency**: Stateless-with-embedded-memory pattern is clearly explained.
- **Cross-refs**: Pricing URLs match TOOLS.md Data Sources (Anthropic verified, others pending).
- **Density**: Medium — Production Counter section is empty placeholder.
- **Issues**: D03 (unverified URLs), D04 (empty counter).

### QUALITY_GATES.md (P11)
- **Structure**: 10 HARD gates + 15 SOFT gates + Scoring Formula + Pre-Production Checklist.
- **Consistency**: HARD gates map 1:1 to SCHEMA required fields. Scoring formula is mathematical and automatable.
- **Cross-refs**: All HARD gates verifiable against SCHEMA. S13 density matches CONFIG.
- **Density**: Excellent. Pure gate definitions, no filler.
- **Issues**: I05 (S03 free tier edge case).

### COLLABORATION.md (P12)
- **Structure**: Role statement + 3 Crew Compositions + Handoff Protocol + Dependencies.
- **Consistency**: "I am INDEPENDENT (layer 0)" matches ARCHITECTURE.md. Dependents list matches dependency graph.
- **Cross-refs**: 5 dependent builders listed = ARCHITECTURE.md 5 dependency arrows.
- **Density**: Good. Crew compositions are forward-looking but useful for orchestration planning.
- **Issues**: D02 (future builders referenced).

---

## CROSS-REFERENCE MATRIX

| Source File | References | Target Exists? |
|-------------|------------|----------------|
| INSTRUCTIONS -> OUTPUT_TEMPLATE.md | Phase 2 step 1 | YES |
| INSTRUCTIONS -> ARCHITECTURE.md | Phase 2 step 3 | YES |
| INSTRUCTIONS -> QUALITY_GATES.md | Phase 3 step 1 | YES |
| INSTRUCTIONS -> EXAMPLES.md (comparison) | Variants section | **NO** (comparison variant missing) |
| TOOLS -> validate_kc.py | Production Tools | YES (codexa-core) |
| TOOLS -> brain_query | Production Tools | YES (MCP) |
| TOOLS -> cex_forge.py | Production Tools | **UNVERIFIED** |
| COLLABORATION -> agent-builder | Crew composition | PLANNED |
| COLLABORATION -> boot-config-builder | Crew + Dependents | PLANNED |
| COLLABORATION -> system-prompt-builder | Crew composition | PLANNED |
| COLLABORATION -> skill-builder | Crew composition | PLANNED |
| COLLABORATION -> quality-gate-builder | Crew composition | PLANNED |
| COLLABORATION -> iso-package-builder | Crew + Dependents | PLANNED |
| COLLABORATION -> router-builder | Dependents | PLANNED |
| COLLABORATION -> fallback-chain-builder | Dependents | PLANNED |
| COLLABORATION -> satellite-spec-builder | Crew composition | PLANNED |
| COLLABORATION -> benchmark-builder | Crew composition | PLANNED |
| COLLABORATION -> scoring-rubric-builder | Crew composition | PLANNED |

---

## LP LOADING ORDER

| LP | File | llm_function | Conflict? |
|----|------|-------------|-----------|
| P01 | KNOWLEDGE.md | INJECT | - |
| P02 | MANIFEST.md | BECOME | - |
| P03 | SYSTEM_PROMPT.md | BECOME | **COLLISION** |
| P03 | INSTRUCTIONS.md | REASON | **COLLISION** |
| P04 | TOOLS.md | CALL | - |
| P05 | OUTPUT_TEMPLATE.md | PRODUCE | - |
| P06 | SCHEMA.md | CONSTRAIN | - |
| P07 | EXAMPLES.md | GOVERN | - |
| P08 | ARCHITECTURE.md | CONSTRAIN | - |
| P09 | CONFIG.md | CONSTRAIN | - |
| P10 | MEMORY.md | INJECT | - |
| P11 | QUALITY_GATES.md | GOVERN | - |
| P12 | COLLABORATION.md | COLLABORATE | - |

---

## VERDICT

**8.5/10 — Publish-ready with 3 critical fixes.**

This is exceptional first-archetype work. The research depth (KNOWLEDGE.md), boundary clarity (ARCHITECTURE.md), and automatable quality gates (QUALITY_GATES.md) set a high bar for the remaining 80 builders. The 3 critical issues (LP collision, missing comparison example, schema size limit inconsistency) are all fixable in < 30 minutes and should be resolved before using this as the template for scaling.

### Priority Fix Order
1. **C01**: Renumber INSTRUCTIONS to P04 (cascade all subsequent +1)
2. **C02**: Add comparison_card golden example to EXAMPLES.md
3. **C03**: Add variant-aware size limits to SCHEMA.md Constraints
