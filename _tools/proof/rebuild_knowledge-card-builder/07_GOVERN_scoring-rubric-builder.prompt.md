# CEX Crew Runner -- Builder Execution
**Builder**: `scoring-rubric-builder`
**Function**: GOVERN
**Intent**: reconstroi knowledge-card-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:43:19.373813

## Intent Context
- **Verb**: reconstroi
- **Object**: knowledge-card-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_scoring_rubric.md
---
id: scoring-rubric-builder
kind: type_builder
pillar: P07
parent: null
domain: scoring_rubric
llm_function: BECOME
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
tags: [kind-builder, scoring-rubric, P07, specialist, governance, evaluation]
---

# scoring-rubric-builder
## Identity
Especialista em construir scoring_rubrics — frameworks de avaliacao com dimensoes ponderadas, thresholds por tier, e calibracao.
Conhece modelos de avaliacao (5D, 12LP, custom), inter-rater reliability, calibracao com golden_tests, e a diferenca entre rubric (P07), gate (P11), e benchmark (P07).
## Capabilities
- Projetar frameworks de avaliacao com dimensoes e pesos balanceados
- Produzir scoring_rubric com dimensoes, pesos (somando 100%), thresholds por tier
- Definir escalas de pontuacao por dimensao com criterios concretos
- Integrar calibracao via golden_tests como exemplos de referencia
- Especificar automation status (manual, semi-automated, automated)
- Validar rubric contra quality gates (9 HARD + 9 SOFT)
## Routing
keywords: [scoring-rubric, rubric, evaluation-criteria, dimensions, weights, grading]
triggers: "define scoring criteria", "how to evaluate quality", "create evaluation rubric"
## Crew Role
In a crew, I handle EVALUATION CRITERIA DESIGN.
I answer: "how should we measure quality of this artifact kind?"
I do NOT handle: reference examples (golden-test-builder), pass/fail barriers (quality-gate-builder), performance metrics (benchmark-builder [PLANNED]).

### bld_instruction_scoring_rubric.md
---
id: p03_ins_scoring_rubric_builder
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Scoring Rubric Builder Instructions
target: scoring-rubric-builder agent
phases_count: 4
prerequisites:
  - Artifact kind to be evaluated is named (e.g. "skill", "agent", "satellite_spec")
  - At least one quality dimension is identified (e.g. correctness, completeness)
  - Weights must sum to exactly 100
  - Tier thresholds are defined or can be derived (e.g. master >= 9.5, skilled >= 8.0)
validation_method: checklist
domain: scoring_rubric
quality: null
tags: [instruction, scoring-rubric, evaluation, governance, P07]
idempotent: true
atomic: false
rollback: Delete generated scoring_rubric file and restart from Phase 1
dependencies: []
logging: true
tldr: Design a weighted evaluation framework with dimensions, per-tier thresholds, concrete scoring criteria, and calibration guidance.
density_score: 0.88
---

## Context
The scoring-rubric-builder produces `scoring_rubric` artifacts — structured evaluation
frameworks used to measure the quality of a specific artifact kind. A scoring_rubric defines
weighted dimensions, numeric thresholds per quality tier, concrete scoring criteria at each
scale point, and an automation status for each dimension.
**Input contract**:
- `{{artifact_kind}}`: the kind being evaluated (e.g. `skill`, `agent`, `satellite_spec`)
- `{{dimensions_raw}}`: comma-separated quality dimensions to evaluate
- `{{tier_map}}`: tier names with numeric thresholds
  (e.g. `master:9.5, skilled:8.0, learning:7.0, rejected:<7.0`)
- `{{golden_tests_available}}`: boolean — whether reference examples exist for calibration
- `{{automation_target}}`: desired level (`manual`, `semi-automated`, `automated`)
**Output contract**: A single `scoring_rubric` Markdown file with YAML frontmatter,
weighted dimension table, per-dimension scoring scales, tier thresholds, and calibration notes.
**Boundaries**:
- Handles evaluation criteria design only.
- Reference examples for calibration belong in golden_test artifacts.
- Binary pass/fail barriers belong in quality_gate artifacts.
- Performance benchmarks (throughput, latency) belong in benchmark artifacts.
## Phases
### Phase 1: Analyze Artifact Kind and Dimensions
**Primary action**: Understand what quality means for `{{artifact_kind}}` and decompose
it into measurable, non-overlapping dimensions.
```
INPUT: artifact_kind, dimensions_raw
1. Characterize the artifact kind:
   artifact_profile = {
     kind: {{artifact_kind}},
     primary_consumer: "human" | "machine" | "both",
     output_type: "text" | "code" | "data" | "config",
     correctness_verifiable: true | false
   }
2. Parse and expand dimensions_raw into dimension_list:
   for each dimension in dimensions_raw.split(","):
     dimension_entry = {
       name: dimension.strip(),
       description: one-sentence definition,
       measurability: "objective" | "subjective" | "semi-objective",
       automation_feasibility: "high" | "medium" | "low"
     }
3. Validate non-overlap:
   for each pair (d1, d2) in dimension_list:
     if d1 and d2 measure the same thing: merge or rename
4. Enforce coverage floor:
   required = ["correctness", "completeness", "clarity"]
   for each missing in required - dimension_list.names:
     add with default one-sentence definition
OUTPUT: artifact_profile{}, dimension_list[] (>= 3 dimensions, non-overlapping)
```
Verification: `dimension_list` has >= 3 entries. No two dimensions share identical
descriptions.
### Phase 2: Assign Weights and Define Tiers
**Primary action**: Distribute the 100-point weight budget across dimensions and define
numeric thresholds for each quality tier.
```
INPUT: dimension_list[], tier_map, artifact_profile
1. Weight allocation:
   if artifact_profile.correctness_verifiable == true:
     correctness_weight >= 30
   Distribute remaining weight by measurability:
     "objective" dimensions receive higher weight
     "subjective" dimensions receive lower weight
   ASSERT sum(all weights) == 100  # hard requirement
2. Tier threshold definition from tier_map:
   tiers = []
   for each (tier_name, min_score) in tier_map:
     tiers.append({
       name: tier_name,
       min_score: min_score,
       label: descriptive label,
       action: what happens at this tier (e.g. "promote", "reject with feedback")
     })
   Sort tiers by min_score descending.
   Verify no gaps or overlaps between adjacent tier ranges.
3. Per-dimension automation status:
   for each dimension in dimension_list:
     if automation_feasibility == "high":   status = "automated"
     elif automation_feasibility == "medium": status = "semi-automated"
     else:                                    status = "manual"
   Document any gap between dimension status and {{automation_target}}.
OUTPUT: weighted_dimensions[] (sum == 100), tier_thresholds[], automation_map{}
```
Verification: weights sum exactly to 100. Each tier has a distinct, non-overlapping range.
### Phase 3: Define Scoring Scales
**Primary action**: For each dimension, write concrete, discriminating criteria at each
key score point on the chosen scale.
```
INPUT: weighted_dimensions[], artifact_profile
1. Choose scale type (consistent across all dimensions):
   default: 1-10 integer scale
   alternative: 1-5 integer scale (only if tier_map max is <= 5)
2. For each dimension, write score anchors at points [1, 3, 5, 7, 9, 10]:
   Criterion rules:
     - Must be observable (not "good" or "acceptable" without qualifier)
     - Must discriminate from adjacent score point
     - Must reference the artifact's actual content, not meta-quality
   Standard anchor pattern:
     10: "{{dimension}} is exemplary — exceeds all requirements, zero gaps"
     9:  "{{dimension}} is complete with at most one minor, non-blocking issue"
     7:  "{{dimension}} is present and functional with 1-2 small gaps"
     5:  "{{dimension}} is present but has significant gaps affecting usability"
     3:  "{{dimension}} is partially present, major issues block correct use"

### bld_knowledge_card_scoring_rubric.md
---
kind: knowledge_card
id: bld_knowledge_card_scoring_rubric
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for scoring_rubric production — atomic searchable facts
sources: scoring-rubric-builder MANIFEST.md + SCHEMA.md, AAC&U VALUE Rubrics, Bloom taxonomy
---

# Domain Knowledge: scoring_rubric
## Executive Summary
Scoring rubrics are multi-dimensional weighted evaluation frameworks that define how to measure artifact quality across orthogonal dimensions with concrete criteria per level. Each rubric targets specific artifact kinds, assigns weights summing to 100%, and maps scores to action tiers (GOLDEN/PUBLISH/REVIEW/REJECT). They differ from quality gates (which enforce pass/fail barriers), golden tests (which provide reference examples), benchmarks (which measure performance metrics), and unit evals (which test specific behaviors) by defining the complete evaluation methodology with weighted dimensions and calibration.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P07 (evaluation) |
| Kind | `scoring_rubric` (exact literal) |
| ID pattern | `p07_sr_{slug}` |
| Required frontmatter | 15 fields |
| Quality gates | 9 HARD + 9 SOFT |
| Max body | 4096 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Weight invariant | All dimension weights MUST sum to 100% |
| Score tiers | GOLDEN >= 9.5, PUBLISH >= 8.0, REVIEW >= 7.0, REJECT < 7.0 |
| Min dimensions | 3 orthogonal dimensions |
## Patterns
| Pattern | Application |
|---------|-------------|
| Orthogonal dimensions | Each dimension measures ONE thing; no overlap between dimensions |
| Explicit weights | Sum to exactly 100%; higher weight = more impact on final score |
| Concrete criteria | Specify what counts at each level, not "good" or "appropriate" |
| Consistent scales | All dimensions use same scale (0-10) for comparability |
| Golden test calibration | Anchor rubric with known-good examples at 9.5+ |
| Automation status | Declare per dimension: manual, semi-automated, or automated |
| Inter-rater reliability | >= 0.80 agreement indicates reliable rubric |
| Target kind scoping | Rubric applies to specific artifact kinds, not everything |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Weights not summing to 100% | Breaks scoring formula; validator rejects |
| Overlapping dimensions | Double-counting inflates or deflates scores |
| Vague criteria ("good quality") | Not actionable; different raters interpret differently |
| No golden test calibration | Rubric floats without anchoring examples |
| Fewer than 3 dimensions | Insufficient coverage of artifact quality |
| All dimensions equal weight | Usually wrong; some dimensions matter more |
| No automation status declared | Unknown whether scoring is manual or automated |
## Application
1. Identify target artifact kinds this rubric evaluates
2. Define >= 3 orthogonal dimensions, each measuring ONE aspect
3. Assign weights summing to exactly 100%
4. Write concrete criteria per dimension per level (0-10 scale)
5. Map scores to tiers: GOLDEN >= 9.5, PUBLISH >= 8.0, REVIEW >= 7.0, REJECT < 7.0
6. Link golden test examples for calibration
7. Declare automation status per dimension
8. Validate: 9 HARD + 9 SOFT gates, body <= 4096 bytes
## References
- scoring-rubric-builder SCHEMA.md v1.0.0
- AAC&U VALUE Rubrics (16 rubrics for learning outcomes)
- Bloom Taxonomy (Anderson & Krathwohl 2001 revision)
- LLM-as-Judge evaluation framework

### bld_quality_gate_scoring_rubric.md
---
id: p11_qg_scoring-rubric
kind: quality_gate
pillar: P11
title: "Gate: Scoring Rubric"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: scoring_rubric
quality: null
density_score: 0.85
tags:
  - quality-gate
  - scoring-rubric
  - evaluation
  - p11
tldr: "Gates ensuring scoring rubric files define measurable dimensions, justified weights summing to 100%, and calibrated tier thresholds."
---

## Definition
A scoring rubric is an evaluation framework that rates a target artifact on multiple weighted dimensions and maps the aggregate score to an action tier. A rubric passes this gate when a reviewer with no prior context could apply it consistently, two independent reviewers would reach scores within 1.0 point of each other on the same input, and the tier thresholds match established system standards.
## HARD Gates
Failure on any HARD gate = immediate REJECT regardless of score.
| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches the file's directory namespace (`scoring-rubric-builder/...`) | Mismatched IDs cause routing failures |
| H03 | `id` value equals the filename stem (slug portion) | Filename and ID must be the same addressable key |
| H04 | `kind` is exactly `scoring_rubric` (literal match, no variation) | Kind drives the loader; wrong literal silently misroutes |
| H05 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H06 | All required frontmatter fields present: id, kind, pillar, title, version, created, updated, author, domain, tags, tldr | Incomplete frontmatter breaks downstream consumers |
| H07 | Spec contains a **Dimensions list** with >= 3 named dimensions, each with a description | Fewer than 3 dimensions cannot capture meaningful variation in artifact quality |
| H08 | Spec contains **Weights** for all dimensions, and weights sum to exactly 100% (or normalize to 100%) | Unbalanced weights produce scores that cannot be compared across rubric versions |
| H09 | Spec contains **Tier thresholds** for >= 3 distinct tiers (e.g., GOLDEN / PUBLISH / REVIEW / REJECT) with numeric boundaries | Without tiers, a score is a number with no actionable meaning |
## SOFT Scoring
Dimensions are weighted; total normalized weight = 100%.
| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler prose | Mostly substantive | No filler; every sentence carries information |
| 2 | Each dimension has concrete scale descriptors (what 1, 5, 10 look like) | 1.0 | No descriptors | Endpoint anchors only (1 and 10) | Full anchors at 1, 5, and 10 with examples |
| 3 | Weights justified by utility impact (rationale provided per weight) | 1.0 | No justification | One-sentence generic rationale | Per-dimension rationale tied to artifact utility |
| 4 | Tiers align with standard thresholds (>= 9.5 golden, >= 8.0 publish, >= 7.0 review, < 7.0 reject) | 1.0 | Custom non-standard thresholds | Partially aligned | Exact alignment with system standards |
| 5 | Calibration via golden tests referenced (pointer to 1+ example with known scores) | 0.5 | No calibration reference | Reference named but not accessible | Accessible example with expected score documented |
| 6 | Tags include `scoring-rubric` | 0.5 | Missing | Present but misspelled | Exactly `scoring-rubric` in tags list |
| 7 | Automation status per dimension (manual / semi-auto / fully automated) | 0.5 | No automation noted | Some dimensions labeled | All dimensions labeled with tool or check reference |
| 8 | Inter-rater guidance (instructions for resolving disagreements between reviewers) | 1.0 | No guidance | General tiebreaker rule | Specific procedure with escalation path |

### bld_schema_scoring_rubric.md
---
kind: schema
id: bld_schema_scoring_rubric
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for scoring_rubric
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: scoring_rubric
## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p07_sr_{framework_slug}) | YES | — | Namespace compliance |
| kind | literal "scoring_rubric" | YES | — | Type integrity |
| pillar | literal "P07" | YES | — | Pillar assignment |
| title | string "Rubric: {name}" | YES | — | Human label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| framework | string | YES | — | Framework name (5D, 12LP, custom) |
| target_kinds | list[string] | YES | — | Artifact kinds this rubric evaluates |
| dimensions_count | integer >= 3 | YES | — | Number of evaluation dimensions |
| total_weight | literal 100 | YES | 100 | Weights must sum to 100% |
| threshold_golden | float | YES | 9.5 | GOLDEN tier floor |
| threshold_publish | float | YES | 8.0 | PUBLISH tier floor |
| threshold_review | float | YES | 7.0 | REVIEW tier floor |
| automation_status | enum (manual, semi-automated, automated) | YES | — | How dimensions are checked |
| domain | string | YES | — | Domain this rubric covers |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Searchability |
| tldr | string <= 160ch | YES | — | Dense summary |
### Recommended
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| calibration_set | list[string] | REC | — | golden_test refs for anchoring |
| inter_rater_agreement | float 0.0-1.0 | REC | — | Reliability measure |
| appeals_process | string | REC | — | How to contest a score |
| density_score | float 0.80-1.00 | REC | — | Content density |
| linked_artifacts | object {primary, related} | REC | — | Cross-references |
## ID Pattern
Regex: `^p07_sr_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Framework Overview` — what it measures, why, and for which artifact kinds
2. `## Dimensions` — table: name, weight(%), scale, criteria, examples
3. `## Thresholds` — 4-tier table: GOLDEN/PUBLISH/REVIEW/REJECT with score ranges and actions
4. `## Calibration` — examples at each tier with rationale (link golden_tests)
5. `## Automation` — status per dimension (manual/semi/automated) with tool refs
## Constraints
- max_bytes: 5120 (body only)
- naming: p07_sr_{framework_slug}.md
- id == filename stem
- dimension weights MUST sum to exactly 100%
- dimensions_count MUST be >= 3
- all 4 tier thresholds MUST be present
- criteria MUST be concrete (no subjective language)
- quality: null always

### bld_examples_scoring_rubric.md
---
kind: examples
id: bld_examples_scoring_rubric
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of scoring_rubric artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: scoring-rubric-builder
## Golden Example
INPUT: "Cria rubric de avaliacao 5D para knowledge_cards"
OUTPUT:
```yaml
id: p07_sr_5d_knowledge_card
kind: scoring_rubric
pillar: P07
title: "Rubric: 5D Knowledge Card"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
framework: "5D"
target_kinds: [knowledge_card]
dimensions_count: 5
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "knowledge"
quality: null
tags: [scoring-rubric, 5d, knowledge-card, evaluation]
tldr: "5-dimension rubric for KCs: density 25%, completeness 25%, actionability 20%, boundary 15%, references 15%"
density_score: 0.92
calibration_set: [p07_gt_kc_prompt_caching]
inter_rater_agreement: 0.85
appeals_process: "Submit to p01-chief with rationale for re-evaluation"
linked_artifacts:
  primary: "quality-gate-builder"
  related: [p11_qg_kc_publish, p07_gt_kc_prompt_caching]
## Framework Overview
5D evaluates knowledge_cards across 5 orthogonal dimensions.
Designed to complement the KC quality_gate (P11) which enforces HARD pass/fail.
This rubric provides the SOFT scoring framework for nuanced quality assessment.
## Dimensions
| Dimension | Weight | Scale | Criteria | Example (10) | Example (5) |
|-----------|--------|-------|----------|-------------|-------------|
| Density | 25% | 0-10 | Ratio of concrete data to total text >= 0.80 | 0.93 density, zero filler phrases | 0.65 density, has "this document describes" |
| Completeness | 25% | 0-10 | All required sections present, >= 3 bullets each | 7 sections, 4+ bullets, all fields filled | 4 sections, some empty, missing tags |
| Actionability | 20% | 0-10 | Contains commands, code, or specific steps | 3 CLI commands, 2 code snippets, concrete steps | General advice, no specific commands |
| Boundary | 15% | 0-10 | Clear EH/NAO EH, no drift to other types | Explicit boundary table, 3+ NAO EH rows | Vague scope, overlaps with other kinds |
| References | 15% | 0-10 | >= 1 source URL, dates, verifiable claims | 3 URLs, all accessible, dated 2026 | No URLs, unverifiable claims |
## Thresholds
| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Promote to calibration set, mark as reference |
| PUBLISH | >= 8.0 | Merge to pool |
| REVIEW | >= 7.0 | Return with specific dimension feedback |
| REJECT | < 7.0 | Redo from scratch with new research |
## Calibration
- GOLDEN (9.8): p07_gt_kc_prompt_caching — density 0.93, 7 sections, 3 URLs, explicit boundary
- PUBLISH (8.3): typical KC with all sections, density 0.82, 1 URL, adequate boundary
- REVIEW (7.2): KC with 5 sections, density 0.75, no URLs, vague boundary
- REJECT (5.0): KC with 3 sections, density 0.50, filler prose, no boundary section
## Automation
| Dimension | Status | Tool |
|-----------|--------|------|
| Density | automated | validate_kc.py (char ratio calculation) |
| Completeness | automated | validate_kc.py (section/field counting) |
| Actionability | manual | Human review for command quality |
| Boundary | semi-automated | Grep for EH/NAO EH patterns |
| References | semi-automated | URL presence check + manual accessibility |
## References
- AAC&U VALUE Rubrics: https://www.aacu.org/initiatives/value-initiative
- validate_kc.py v2.0 (CEX 5D implementation reference)
```
WHY THIS IS GOLDEN:
- quality: null (H06 pass)
- id matches p07_sr_ pattern (H02 pass)
- kind: scoring_rubric (H04 pass)
- 25 frontmatter fields present (H08 pass)
- 5 dimensions with weights 25+25+20+15+15 = 100% (H07 pass)
- All 4 tiers defined with score ranges and actions (H09 pass)
- Criteria are concrete per dimension with examples at 10 and 5 (S03 pass)
- Calibration section has examples at all 4 tiers (S05 pass)
- Automation status per dimension with tool refs (S06 pass)

### bld_config_scoring_rubric.md
---
kind: config
id: bld_config_scoring_rubric
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for scoring_rubric production
pattern: CONFIG restricts SCHEMA, never contradicts
---

# Config: scoring_rubric Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p07_sr_{framework_slug}.md | p07_sr_5d_knowledge_card.md |
| Builder dir | kebab-case | scoring-rubric-builder/ |
| Fields | snake_case | dimensions_count, threshold_golden |
| Framework names | descriptive slug | 5d, 12lp, kc_quality |
Rule: id MUST equal filename stem.
## File Paths
- Output: cex/P07_evals/examples/p07_sr_{framework_slug}.md
- Compiled: cex/P07_evals/compiled/p07_sr_{framework_slug}.yaml
## Size Limits (aligned with SCHEMA)
- Body: max 5120 bytes
- Density: >= 0.80
- Dimensions: >= 3 (no upper limit, but 3-8 recommended)
## Weight Policy
- All dimension weights MUST sum to exactly 100%
- Integer percentages preferred (25%, 20%, 15%)
- No dimension below 5% (too small to matter)
- No dimension above 40% (avoid single-dimension dominance)

### bld_output_template_scoring_rubric.md
---
kind: output_template
id: bld_output_template_scoring_rubric
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for scoring_rubric production
pattern: derives from SCHEMA.md — no extra fields
---

# Output Template: scoring_rubric
```yaml
id: p07_sr_{{framework_slug}}
kind: scoring_rubric
pillar: P07
title: "Rubric: {{framework_name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
framework: "{{framework_name}}"
target_kinds: [{{kind_1}}, {{kind_2}}]
dimensions_count: {{integer_gte_3}}
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "{{manual_or_semi_or_automated}}"
domain: "{{domain_value}}"
quality: null
tags: [scoring-rubric, {{framework}}, {{domain}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80_to_1.00}}
calibration_set: [{{golden_test_ref_1}}, {{golden_test_ref_2}}]
inter_rater_agreement: {{0.0_to_1.0}}
appeals_process: "{{how_to_contest_a_score}}"
linked_artifacts:
  primary: "{{target_kind_builder_or_schema}}"
  related: [{{related_artifact_refs}}]
## Framework Overview
{{what_it_measures_and_why}}
## Dimensions
| Dimension | Weight | Scale | Criteria | Example (10) | Example (5) |
|-----------|--------|-------|----------|-------------|-------------|
| {{dim_1}} | {{pct}}% | 0-10 | {{concrete_criteria}} | {{high_example}} | {{mid_example}} |
| {{dim_2}} | {{pct}}% | 0-10 | {{concrete_criteria}} | {{high_example}} | {{mid_example}} |
| {{dim_3}} | {{pct}}% | 0-10 | {{concrete_criteria}} | {{high_example}} | {{mid_example}} |
## Thresholds
| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | {{golden_action}} |
| PUBLISH | >= 8.0 | {{publish_action}} |
| REVIEW | >= 7.0 | {{review_action}} |
| REJECT | < 7.0 | {{reject_action}} |
## Calibration
{{examples_at_each_tier_with_rationale}}
## Automation
| Dimension | Status | Tool |
|-----------|--------|------|
| {{dim_1}} | {{manual_or_semi_or_automated}} | {{tool_ref}} |
| {{dim_2}} | {{manual_or_semi_or_automated}} | {{tool_ref}} |
## References
- {{reference_1}}
- {{reference_2}}
```

### bld_architecture_scoring_rubric.md
---
kind: architecture
id: bld_architecture_scoring_rubric
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of scoring_rubric — inventory, dependencies, and architectural position
---

# Architecture: scoring_rubric in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, target_kind, dimensions_count, etc.) | scoring-rubric-builder | active |
| dimensions | Named evaluation axes with descriptions and rationale | author | active |
| weights | Percentage weight per dimension (must sum to 100%) | author | active |
| scale_definitions | Per-dimension scoring scale with concrete criteria at each level | author | active |
| tier_thresholds | Score ranges mapped to quality tiers (master, skilled, learning, rejected) | author | active |
| calibration_refs | Golden test references used to anchor consistent scoring | author | active |
| automation_status | Which dimensions are automated, semi-automated, or manual | author | active |
## Dependency Graph
```
domain_knowledge  --produces-->  scoring_rubric  --consumed_by-->  quality_gate
golden_test       --calibrates-> scoring_rubric  --consumed_by-->  evaluator
scoring_rubric    --signals-->   calibration_drift
```
| From | To | Type | Data |
|------|----|------|------|
| knowledge_card (P01) | scoring_rubric | data_flow | domain expertise informing dimension selection |
| golden_test (P07) | scoring_rubric | data_flow | reference examples for scoring calibration |
| scoring_rubric | quality_gate (P11) | consumes | gate uses rubric criteria for scoring decisions |
| scoring_rubric | evaluator | consumes | human or automated evaluator applies the rubric |
| scoring_rubric | calibration_drift (P12) | signals | emitted when inter-rater agreement drops |
| benchmark (P07) | scoring_rubric | dependency | benchmarks may inform threshold selection |
## Boundary Table
| scoring_rubric IS | scoring_rubric IS NOT |
|-------------------|----------------------|
| An evaluation framework with weighted dimensions and tiers | A reference example of ideal output (golden_test P07) |
| Defines how quality is measured with concrete criteria | A pass/fail quality barrier (quality_gate P11) |
| Dimensions sum to 100% weight for balanced scoring | A technical validation rule (validator P06) |
| Calibrated against golden tests for consistency | A performance measurement (benchmark P07) |
| Scoped to one artifact kind with kind-specific criteria | A universal evaluation applicable to all kinds |
| Supports manual, semi-automated, and automated evaluation | An exclusively automated check without human option |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Domain | knowledge_card, benchmark | Supply domain expertise and performance baselines |
| Framework | frontmatter, dimensions, weights | Define evaluation axes and their relative importance |
| Criteria | scale_definitions, tier_thresholds | Specify concrete scoring levels and quality tiers |
| Calibration | calibration_refs, golden_test | Anchor consistent scoring with reference examples |
| Application | quality_gate, evaluator, automation_status | Apply the rubric in automated or manual evaluation |


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `scoring-rubric-builder` for pipeline function `GOVERN`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
