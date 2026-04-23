---
id: p03_ins_lens
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Lens Builder Execution Protocol
target: lens-builder agent
phases_count: 4
prerequisites:
  - A perspective or analytical viewpoint to encode is identified
  - The artifact types this lens applies to are known
  - The lens has a distinct focus not already covered by an existing lens
validation_method: checklist
domain: lens
quality: 9.2
tags: [instruction, lens, perspective, P02, filter, analysis]
idempotent: true
atomic: true
rollback: "Discard generated artifact; no system state is modified"
dependencies: []
logging: true
tldr: Define a specialized analytical perspective as a lens artifact with declared focus, filters, bias, applies_to scope, and interpretation guidance.
density_score: 0.94
llm_function: REASON
related:
  - p03_sp_lens_builder
  - bld_schema_lens
  - bld_architecture_lens
  - bld_knowledge_card_lens
  - lens-builder
  - bld_collaboration_lens
  - p11_qg_lens
  - p01_kc_lens
  - bld_memory_lens
  - bld_output_template_lens
---
## Context
The lens-builder produces `lens` artifacts (P02) — declarative filters that define how to analyze or interpret other artifacts from a specific perspective. A lens has no capabilities and takes no actions (that is an agent); it does not define routing rules (that is a mental model); it is a pure analytical perspective applied to artifacts.
**Inputs:**
- `$perspective_name (required) - string - "Human-readable name of the viewpoint (e.g. 'security lens', 'cost lens', 'user-experience lens')"`
- `$focus (required) - string - "The primary analytical concern this lens examines"`
- `$applies_to (required) - list[string] - "Artifact types or domains this lens filters (e.g. ['api_endpoint', 'agent', 'workflow'])"`
- `$declared_bias (optional) - string - "Known skew or emphasis this perspective introduces (e.g. 'favors consistency over speed')"`
- `$interpretation_weight (optional) - float[0.0-1.0] - "Relative importance when multiple lenses are applied simultaneously"`
**Output:** A single `lens` artifact with 20 frontmatter fields and body sections covering perspective, filters, application, and limitations.
**Boundary check before proceeding:**
- Perspective requires executing actions or calling tools → route to agent-builder
- Perspective defines when to route tasks → route to mental-model-builder
- Purpose is purely analytical ("view this artifact through this filter") → proceed
## Phases
### Phase 1: Discover
**Action:** Establish the analytical core and applicability boundaries of the lens.
1. Identify the **perspective**: what analytical viewpoint is needed and what question it answers.
2. Check for existing lenses covering the same focus and `applies_to` scope — avoid duplicates.
   - If exact duplicate found: return the existing lens id, do not build a new one.
   - If partial overlap: narrow the scope of this lens to the non-overlapping portion.
3. Determine `applies_to`: list specific artifact types, not broad domains.
   - If it applies universally, use `["*"]` and record justification.
4. List the specific attributes (filters) the lens highlights within those artifact types.
5. Declare the `bias` direction:
   - Directional: "favors X over Y because Z"
   - Neutral: "treats A and B equally by design" (rare — most lenses have a tilt)
**Verification:** You can answer: "When applied to [artifact type], this lens answers: [specific question]."
### Phase 2: Compose
**Action:** Write all frontmatter fields and body sections.
1. Read `SCHEMA.md` — source of truth for all 20 fields.
2. Read `OUTPUT_TEMPLATE.md` — fill every `{{var}}` following SCHEMA constraints.
3. Fill frontmatter: all 20 fields (`null` valid for optional fields).
4. Set `quality`: literal `null` — never a number.
5. Set `id`: pattern `p02_lens_{slug}` where slug is snake_case of the perspective name.
6. Set `kind`: literal string `lens`.
7. Write `## Perspective` — what the lens sees, emphasizes, and what question it answers when applied.
8. Write `## Filters` — two sub-sections:
   - `### Highlights`: concrete attributes the lens foregrounds (at least 3 specific attributes)
   - `### Suppresses`: concrete attributes the lens de-emphasizes, with reason for suppression
9. Write `## Application` — step-by-step: how to use this lens on a target artifact.
10. Write `## Limitations` — what the lens misses, what it cannot assess, and known blind spots.
**Verification:** `## Filters` has at least 3 highlight attributes and at least 1 suppress attribute. `## Limitations` names at least one concrete blind spot. No section contains capability language (no "calls", "executes", "routes").
### Phase 3: Validate
**Action:** Run all 8 HARD gates from `QUALITY_GATES.md`. Fix any failure before output.
| Gate | Check |
|------|-------|
| H01 | YAML frontmatter parses without error |
| H02 | `id` matches pattern `^p02_lens_[a-z][a-z0-9_]+$` |
| H03 | `kind` is literal string `lens` |
| H04 | `quality` is `null` |
| H05 | `perspective` field is non-empty |
| H06 | `applies_to` is a non-empty list |
| H07 | `## Filters` contains both Highlights and Suppresses sub-sections |
| H08 | No capability language in body (no actions, tools, or routing logic) |
Score SOFT gates from `QUALITY_GATES.md`. If soft score < 8.0, revise in the same pass.
**Cross-check:** Is this still a filter? Not drifting into agent capabilities? Not drifting into mental_model routing?
### Phase 4: Output
**Action:** Emit the final artifact at the correct path.
1. Write file to the path defined in `CONFIG.md` for lens artifacts.
2. Confirm filename stem matches `id` field.
3. Confirm all 4 body sections are present and non-empty.
4. Confirm `applies_to` list aligns with the `## Application` section examples.
## Output Contract
```
id: p02_lens_`{{slug}}`
kind: lens
pillar: P02
version: 1.0.0
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
author: `{{author}}`
domain: lens
lens_name: "`{{human_readable_name}}`"
focus: "`{{primary_analytical_concern}}`"
applies_to: [`{{artifact_type_list}}`]
perspective: "`{{what_this_lens_sees_and_emphasizes}}`"
declared_bias: "`{{bias_statement}}`"
interpretation_weight: {{0.0-1.0}}
filters_highlight: [`{{attribute_list}}`]
filters_suppress: [`{{attribute_list}}`]
limitations: "`{{known_blind_spots}}`"
status: active


## Validation
- Verify output matches expected schema before delivery
- Check all required fields are present and non-empty
- Confirm no template placeholders remain in output


## Edge Cases
- Empty input: return structured error with guidance
- Partial input: fill defaults, flag missing fields
- Oversized input: truncate with warning, preserve structure


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_lens_builder]] | related | 0.64 |
| [[bld_schema_lens]] | downstream | 0.63 |
| [[bld_architecture_lens]] | downstream | 0.63 |
| [[bld_knowledge_card_lens]] | upstream | 0.62 |
| [[lens-builder]] | upstream | 0.60 |
| [[bld_collaboration_lens]] | upstream | 0.59 |
| [[p11_qg_lens]] | downstream | 0.57 |
| [[p01_kc_lens]] | upstream | 0.56 |
| [[bld_memory_lens]] | downstream | 0.52 |
| [[bld_output_template_lens]] | downstream | 0.49 |
