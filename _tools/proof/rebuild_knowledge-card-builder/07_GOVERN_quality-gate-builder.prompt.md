# CEX Crew Runner -- Builder Execution
**Builder**: `quality-gate-builder`
**Function**: GOVERN
**Intent**: reconstroi knowledge-card-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:43:19.370813

## Intent Context
- **Verb**: reconstroi
- **Object**: knowledge-card-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_quality_gate.md
---
id: quality-gate-builder
kind: type_builder
pillar: P11
parent: null
domain: quality_gate
llm_function: BECOME
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: system
tags: [kind-builder, quality-gate, P11, specialist, governance]
---

# quality-gate-builder
## Identity
Especialista em construir quality_gates — barreiras de qualidade com score numerico.
Sabe tudo sobre HARD/SOFT gate patterns, scoring formulas, bypass policies,
and the difference between gates (P11), validators (P06), and rubrics (P07).
## Capabilities
- Definir quality gates com metricas concretas e thresholds
- Produzir HARD gates (block) e SOFT gates (score contribution)
- Compor scoring formulas com pesos por dimensao
- Definir bypass policies e audit trails
## Routing
keywords: [quality-gate, gate, threshold, scoring, pass-fail, governance]
triggers: "define quality gate", "what quality checks", "scoring formula"
## Crew Role
In a crew, I handle QUALITY GOVERNANCE.
I answer: "what must pass before this artifact ships?"
I do NOT handle: validator code (P06), scoring rubric criteria (P07), bugloop cycles (P11).

### bld_instruction_quality_gate.md
---
id: p03_ins_quality_gate
kind: instruction
pillar: P11
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Quality Gate Builder Instructions
target: "quality-gate-builder agent"
phases_count: 4
prerequisites:
  - "Caller has identified the artifact kind being gated (e.g. prompt_template, router, response_format)"
  - "At least one quality dimension is named (e.g. completeness, correctness, structural validity)"
  - "Delivery threshold is known or can be inferred (numeric score 0.0-1.0)"
validation_method: checklist
domain: quality_gate
quality: null
tags: [instruction, quality-gate, P11, governance, scoring, threshold]
idempotent: true
atomic: false
rollback: "Delete produced gate file. No downstream effects until the gate is wired to a delivery pipeline."
dependencies: []
logging: true
tldr: "Define HARD block gates and SOFT scoring gates with numeric thresholds for a target artifact kind, then validate the gate spec internally."
density_score: 0.91
---

## Context
A **quality_gate** is a pass/fail or scored checkpoint applied to an artifact before it is accepted downstream. HARD gates are binary blockers — a single failure prevents delivery. SOFT gates contribute to a weighted aggregate score; if the score falls below the delivery threshold, the artifact is rejected. This builder produces gate *specifications*, not executable validator code.
**Inputs**
| Field | Type | Description |
|---|---|---|
| `artifact_kind` | string | The kind being gated (e.g. `prompt_template`, `router`, `response_format`) |
| `dimensions` | list | Quality dimensions to evaluate (e.g. `completeness`, `correctness`, `safety`) |
| `delivery_threshold` | float | Minimum acceptable soft-gate aggregate score (0.0–1.0) |
| `bypass_policy` | string | Who may override a gate failure: `none`, `owner`, or `admin` |
**Output**
A single `.md` file with YAML frontmatter + body containing: HARD gate table, SOFT gate table with weights, aggregate scoring formula, and bypass policy. Weights across all SOFT gates must sum to 1.0.
**Boundary rules**
- quality_gate = pass/fail specification for artifact acceptance (this builder)
- validation_schema = executable code that validates artifact structure post-generation (different builder)
- rubric = criteria for human scoring panels (different builder)
- lifecycle_rule = when to promote, retire, or deprecate an artifact (different builder)
## Phases
### Phase 1: Research — Dimension Mapping
Map each quality dimension to concrete, objectively verifiable checks.
```
FOR each dimension in dimensions:
  identify 1-3 concrete checks that are objectively verifiable
  classify each check:
    HARD if: binary outcome only (present/absent, valid/invalid, correct/incorrect)
             AND failure would make the artifact non-functional or misleading
    SOFT if: gradable (partial credit exists)
             OR contributes to overall quality without blocking basic utility
  assign weight to each SOFT gate
  NOTE: all SOFT gate weights must sum to exactly 1.0
IF no dimensions provided, infer from artifact_kind using standard set:
  structural:   schema validity, required fields present
  semantic:     content correctness, boundary adherence
  operational:  usability, completeness of examples, actionability
Research existing gates for similar artifact kinds to calibrate thresholds.
Identify industry-standard thresholds for the domain where applicable.
```
Deliverable: classified list of HARD checks and SOFT checks with weights.
### Phase 2: Classify — Boundary Check
Confirm this artifact belongs to `quality_gate` and not a sibling kind.
```
IF caller wants executable code that validates artifact structure:
  RETURN "Route to validation-schema-builder — produces code, not a gate spec."
IF caller wants criteria for human scoring panels or review committees:
  RETURN "Route to rubric-builder — rubrics serve human reviewers."
IF caller wants lifecycle rules (when to retire, promote, deprecate):
  RETURN "Route to lifecycle-rule-builder."
IF caller wants runtime behavior limits (timeout, retry, rate limit):
  RETURN "Route to runtime-rule-builder."
IF caller wants HARD+SOFT gate spec with numeric delivery threshold:
  PROCEED as quality_gate
```
Deliverable: confirmed `kind: quality_gate` with one-line justification.
### Phase 3: Compose — Build the Gate Specification
Assemble frontmatter and body following SCHEMA.md and OUTPUT_TEMPLATE.md.
```
ID generation:
  id = "p11_qg_" + artifact_kind_slug
  pattern must match valid quality_gate id format
Frontmatter (required fields):
  id, kind (= quality_gate), pillar (= P11), title, version,
  created, updated, author, target_kind, delivery_threshold,
  bypass_policy, dimensions, quality (= null), tags
Body structure:
  ## Definition
  Table: metric | threshold | operator | scope
  One row per top-level quality dimension.
  ## HARD Gates
  Table: ID | Criterion | Failure Action
  Rows: H01, H02, ... (sequential, no gaps)
  Each criterion: objectively verifiable, no subjective adjectives alone.
  Failure action: always "block" for HARD gates.
  Minimum: 2 HARD gates required.
  ## SOFT Gates
  Table: ID | Criterion | Weight | Scoring Method
  Rows: S01, S02, ... (sequential, no gaps)
  Scoring method: "binary" (0 or weight) or "graduated" (partial credit)
  Weights: must sum to exactly 1.0
  Minimum: 3 SOFT gates required.
  ## Scoring Formula
  aggregate_score = SUM(gate_score * weight for each SOFT gate)
  PASS condition: all HARD gates pass AND aggregate_score >= {delivery_threshold}
  State formula explicitly — do not leave it implicit.
  ## Actions
  Table: outcome | consequence
  PASS: artifact proceeds to delivery/pool
  FAIL: artifact returned with gate failure details
  ## Bypass Policy
  Who may override: {none | owner | admin}
  Conditions for bypass: explicit criteria (not vague)
  Audit requirement: what must be logged when bypass is used
```
Deliverable: complete `.md` file with frontmatter + 5 body sections.
### Phase 4: Validate — Gate the Gate Spec
Apply meta-checks to the gate spec itself before delivering.
```

### bld_knowledge_card_quality_gate.md
---
kind: knowledge_card
id: bld_knowledge_card_quality_gate
pillar: P11
llm_function: INJECT
purpose: Domain knowledge for quality_gate production — atomic searchable facts
sources: quality-gate-builder MANIFEST.md + SCHEMA.md
---

# Domain Knowledge: quality_gate
## Executive Summary
Quality gates are numeric scoring barriers that block or score artifacts before they ship. Each gate is HARD (binary AND — one failure zeroes the final score) or SOFT (weighted dimension contributing to a 0–10 score). Gates govern one domain and never self-score (`quality: null` always). A gate is a policy; a validator implements it; a rubric defines the scoring dimensions.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P11 (governance) |
| ID pattern | `p11_qg_{gate_slug}` |
| Required frontmatter fields | 12 |
| HARD gates | 8–10 required; universal H01–H06 always present |
| SOFT gates | 5–20; each weight >= 0.5; weights sum == 100% |
| Max body | 4096 bytes |
| Body sections | 5 (Definition, HARD Gates, SOFT Scoring, Actions, Bypass) |
| Score tiers | GOLDEN >= 9.5 / PUBLISH >= 8.0 / REVIEW >= 7.0 / REJECT < 7.0 |
| Naming | `p11_qg_{slug}.md` |
## Patterns
| Pattern | Rule |
|---------|------|
| HARD gate failure | Sets final score to 0 regardless of all SOFT scores |
| Universal HARD gates | H01 (frontmatter parses), H02 (ID regex), H03 (ID == filename), H04 (kind literal), H05 (quality null), H06 (required fields present) |
| SOFT weight minimum | >= 0.5; weight 1.0 = high utility impact; weight 0.5 = polish |
| Weights invariant | Sum of all SOFT weights MUST equal 100% |
| Scoring formula | `final = hard_pass ? sum(gate * weight) / sum(weights) : 0` |
| Threshold rule | Must be numeric — no vague qualifiers ("good", "acceptable") |
| Bypass conditions | Must include: condition + approver + audit_log + expiry |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| SOFT weight < 0.5 | Creates invisible low-signal dimensions |
| Weights not summing to 100% | Breaks scoring formula invariant; validator rejects |
| Missing H01–H06 | Gate is structurally incomplete; kind-specific gates cannot replace universals |
| `quality` field non-null | Self-scoring forbidden by schema |
| Bypass without expiry | Audit trail incomplete; bypass becomes permanent |
| Vague threshold ("high quality") | Not computable; validator cannot determine pass/fail |
| > 12 HARD gates | Diminishing returns; creates unnecessary brittleness |
| Gate checks producer, not artifact | Gates evaluate the artifact output, not who made it |
## Application
1. Identify the artifact kind this gate protects — sets the `domain` field
2. Write frontmatter: 12 required fields; `quality: null`; `id` matches `p11_qg_{slug}` pattern
3. Write `## Definition` — metric, threshold (numeric), operator, scope
4. Write `## HARD Gates` — include H01–H06 universals; add kind-specific gates up to 10 total
5. Write `## SOFT Scoring` — assign weight >= 0.5 per dimension; verify sum == 100%
6. Write `## Actions` — map score ranges to GOLDEN / PUBLISH / REVIEW / REJECT tiers
7. Write `## Bypass` — condition + approver + audit_log + expiry; mark H01 and H05 as never-bypassable
8. Verify body <= 4096 bytes; `id` equals filename stem
## References
- quality-gate-builder MANIFEST.md v1.0.0
- quality_gate SCHEMA.md v2.0.0
- Boundary: quality_gate (policy) vs validator (P06, enforcement code) vs scoring_rubric (P07, dimension criteria)

### bld_architecture_quality_gate.md
---
kind: architecture
id: bld_architecture_quality_gate
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of quality_gate — inventory, dependencies, and architectural position
---

# Architecture: quality_gate in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, target_kind, pass_threshold, etc.) | quality-gate-builder | active |
| hard_gates | Blocking checks that must pass — artifact rejected on failure | author | active |
| soft_gates | Score-contributing checks that degrade quality score but do not block | author | active |
| scoring_formula | Weighted combination of soft gate scores into final quality number | author | active |
| pass_threshold | Minimum score required to pass the gate | author | active |
| bypass_policy | Conditions and audit requirements for overriding a failed gate | author | active |
## Dependency Graph
```
artifact (any)  --evaluated_by-->  quality_gate  --produces-->    pass_fail_result
scoring_rubric  --depends-->       quality_gate  --signals-->     gate_event
validator       --depends-->       quality_gate
```
| From | To | Type | Data |
|------|----|------|------|
| artifact (any) | quality_gate | data_flow | artifact submitted for quality evaluation |
| quality_gate | pass_fail_result | produces | boolean pass/fail plus numeric score |
| scoring_rubric (P07) | quality_gate | dependency | rubric dimensions inform gate criteria |
| validator (P06) | quality_gate | dependency | validators implement individual hard gate checks |
| quality_gate | gate_event (P12) | signals | emitted on pass, fail, or bypass |
| quality_gate | lifecycle_rule (P11) | data_flow | gate scores may trigger lifecycle transitions |
## Boundary Table
| quality_gate IS | quality_gate IS NOT |
|-----------------|---------------------|
| A barrier with HARD (block) and SOFT (score) checks | A technical pass/fail validation rule (validator P06) |
| Produces a numeric quality score from weighted formula | An evaluation criteria framework (scoring_rubric P07) |
| Applied before artifact is accepted into a pool or promoted | A fix-verify cycle for broken artifacts (bugloop P11) |
| Includes bypass policy with audit trail | A safety restriction on agent behavior (guardrail P11) |
| Targets a specific artifact kind with kind-aware criteria | A continuous optimization loop (optimizer P11) |
| Binary outcome (pass/fail) plus score for ranking | A subjective review without numeric scoring |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Input | artifact, scoring_rubric | Artifact under evaluation and criteria reference |
| Hard Checks | hard_gates, validator | Blocking checks that must pass |
| Soft Checks | soft_gates, scoring_formula | Score-contributing checks with weighted combination |
| Decision | pass_threshold, bypass_policy | Pass/fail determination and override rules |
| Output | pass_fail_result, gate_event | Result delivered and event signaled downstream |

### bld_collaboration_quality_gate.md
---
kind: collaboration
id: bld_collaboration_quality_gate
pillar: P11
llm_function: COLLABORATE
purpose: How quality-gate-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: quality-gate-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what must pass before this artifact ships?"
I define HARD gates (block on fail) and SOFT gates (score contribution) with numeric thresholds. I do not write validator code, scoring rubric criteria, or run bugloop cycles.
## Crew Compositions
### Crew: "Artifact Quality Assurance"
```
  1. scoring-rubric-builder   -> "criteria dimensions and weights for evaluation"
  2. quality-gate-builder     -> "HARD/SOFT gates with numeric thresholds and bypass policy"
  3. validator-builder        -> "executable code that enforces the gates post-generation"
```
### Crew: "Agent Governance Layer"
```
  1. law-builder              -> "inviolable rules that override all other decisions"
  2. guardrail-builder        -> "safety boundaries on agent behavior"
  3. quality-gate-builder     -> "quality thresholds artifacts must clear before acceptance"
  4. lifecycle-rule-builder   -> "rules governing artifact lifecycle transitions"
```
### Crew: "Builder Certification Pack"
```
  1. prompt-template-builder  -> "template artifact under review"
  2. response-format-builder  -> "output format artifact under review"
  3. quality-gate-builder     -> "gates both artifacts must pass (score >= 8.0)"
  4. iso-package-builder      -> "packages certified artifacts into deployable unit"
```
## Handoff Protocol
### I Receive
- seeds: artifact kind, domain, required quality dimensions, minimum passing score
- optional: scoring rubric reference, existing gate definitions to extend, bypass policy conditions
### I Produce
- quality_gate artifact (YAML frontmatter + HARD gates list + SOFT gates list + scoring formula, max 4096 bytes)
- committed to: `cex/P11/examples/p11_qg_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- scoring-rubric-builder: provides evaluation dimensions that map to SOFT gate contributions
- law-builder: inviolable laws become mandatory HARD gates with no bypass
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| validator-builder | Implements executable checks that enforce the gates I define |
| iso-package-builder | Uses my gates as acceptance criteria before packaging artifacts |
| bugloop-builder | Triggers fix cycles when gate scores fall below threshold |
| benchmark-builder | References my thresholds to define pass/fail on benchmark runs |
| every kind-builder | Each builder's QUALITY_GATES.md is produced by me |

### bld_config_quality_gate.md
---
kind: config
id: bld_config_quality_gate
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for quality_gate production
pattern: CONFIG restricts SCHEMA, never contradicts
---

# Config: quality_gate Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p11_qg_{slug}.md | p11_qg_kc_publish.md |
| Builder dir | kebab-case | quality-gate-builder/ |
| Fields | snake_case | density_score |
Rule: id MUST equal filename stem.
## File Paths
- Output: cex/P11_feedback/examples/p11_qg_{slug}.md
- Compiled: cex/P11_feedback/compiled/p11_qg_{slug}.yaml
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Density: >= 0.80

### bld_examples_quality_gate.md
---
kind: examples
id: bld_examples_quality_gate
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of quality_gate artifacts
---

# Examples: quality-gate-builder
## Golden Example
INPUT: "Define gate pra knowledge_cards antes de publicar no pool"
OUTPUT:
```yaml
id: p11_qg_kc_publish
kind: quality_gate
pillar: P11
title: "Gate: KC Publish"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "system"
domain: "knowledge_card"
quality: null
tags: [quality-gate, knowledge-card, pre-publish]
tldr: "Pre-publish gate for KCs: 10 HARD checks + 5-dimension scoring >= 8.0"
density_score: 0.92
## Definition
| Property | Value |
|----------|-------|
| Metric | combined_score |
| Threshold | 8.0 |
| Operator | >= |
| Scope | All knowledge_card artifacts before pool merge |
## Checklist (HARD)
- [ ] YAML parses without error
- [ ] id starts with p01_kc_
- [ ] id == filename stem
- [ ] kind == knowledge_card
- [ ] quality == null
- [ ] body >= 3 bullet points
- [ ] size <= 5120 bytes
## Scoring (SOFT)
| Dimension | Weight | Criteria |
|-----------|--------|----------|
| Density | 25% | >= 0.80 |
| Completeness | 25% | All required fields present |
| Actionability | 20% | Concrete examples or commands |
| Boundary | 15% | EH/NAO EH section |
| References | 15% | >= 1 source URL |
## Actions
| Result | Action | Escalation |
|--------|--------|------------|
| Pass >= 8.0 | Merge to pool | None |
| Fail < 8.0 | Return with report | Retry required |
## Bypass
- Conditions: SOFT 7.0-7.9 with architect approval
- Approver: p01-chief [PLANNED]
- Audit: bypass in commit message
```
## Anti-Example
```yaml
id: quality_check
kind: quality_gate
title: "Make sure it's good"
quality: 9.0
Check that the artifact is high quality. If good enough, approve.
```
FAILURES:
1. id: no p11_qg_ prefix
2. lp: missing
3. quality: self-scored
4. "good enough": subjective, not measurable
5. No Definition table, no scoring, no bypass

### bld_memory_quality_gate.md
---
kind: memory
id: bld_memory_quality_gate
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for quality_gate artifact generation
---

# Memory: quality-gate-builder
## Summary
Quality gates are pass/fail barriers with numeric scoring that artifacts must clear before shipping. The critical production lesson is the HARD/SOFT distinction: HARD gates block (fail = reject), SOFT gates score (low = penalty but not rejection). Mixing these causes either false rejections (SOFT treated as HARD) or quality leaks (HARD treated as SOFT). The second lesson is that scoring formulas must have weights summing to exactly 100% — weights that sum to more or less create score inflation or deflation.
## Pattern
- Classify every gate as HARD (blocking) or SOFT (scoring) before writing the check logic
- HARD gates must be binary: pass or fail with no partial credit — ambiguous gates cause inconsistent enforcement
- SOFT gate weights must sum to exactly 100% — verify arithmetic before delivery
- Scoring formulas should be transparent: any reviewer can manually calculate the score from gate results
- Bypass policies must require explicit audit trail entry — no silent bypasses
- Include calibration examples: one artifact that barely passes, one that barely fails
## Anti-Pattern
- HARD gates with partial scoring — creates ambiguity about whether the artifact is blocked or just penalized
- SOFT gate weights summing to 110% or 90% — inflated or deflated scores break threshold comparisons
- Bypass without audit trail — quality gates with easy silent bypasses provide no enforcement value
- Gates that check the same dimension twice — double-counting inflates that dimension's influence
- Confusing quality_gate (P11, pass/fail barrier) with validator (P06, technical check) or scoring_rubric (P07, evaluation framework)
## Context
Quality gates operate in the P11 governance layer. They are the final checkpoint before an artifact enters a pool or ships to production. Gates consume validator results (P06) and scoring rubric evaluations (P07) but make the binary ship/no-ship decision. In high-throughput systems, automated gates process artifacts without human review; only bypasses require human authorization.
## Impact
Clear HARD/SOFT classification eliminated 100% of false rejection incidents. Weight normalization to 100% produced scores that accurately predicted downstream artifact performance. Audit-trail-required bypasses reduced unauthorized quality exceptions by 90%.
## Reproducibility
Reliable quality gate production: (1) enumerate all checks and classify each as HARD or SOFT, (2) define binary pass/fail logic for HARD gates, (3) assign weights to SOFT gates summing to 100%, (4) write transparent scoring formula, (5) define bypass policy with audit requirements, (6) provide calibration examples at the pass/fail boundary.
## References
- quality-gate-builder SCHEMA.md (HARD/SOFT gate specification)
- P11 governance pillar specification
- Quality assurance gate patterns

### bld_output_template_quality_gate.md
---
kind: output_template
id: bld_output_template_quality_gate
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for quality_gate production
pattern: derives from SCHEMA.md — no extra fields
---

# Output Template: quality_gate
```yaml
id: p11_qg_{{gate_slug}}
kind: quality_gate
pillar: P11
title: "Gate: {{gate_name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
domain: "{{what_domain_this_protects}}"
quality: null
tags: [quality-gate, {{domain}}, {{scope}}]
tldr: "{{one_sentence_what_gate_enforces}}"
density_score: {{0.80_to_1.00}}
## Definition
| Property | Value |
|----------|-------|
| Metric | {{metric_name}} |
| Threshold | {{numeric_value}} |
| Operator | {{>= / <= / == / !=}} |
| Scope | {{where_gate_applies}} |
## Checklist (HARD gates — ALL must pass)
- [ ] {{check_1}}: {{description}}
- [ ] {{check_2}}: {{description}}
- [ ] {{check_3}}: {{description}}
## Scoring (SOFT gates — weighted dimensions)
| Dimension | Weight | Criteria |
|-----------|--------|----------|
| {{dim_1}} | {{pct}}% | {{what_to_check}} |
| {{dim_2}} | {{pct}}% | {{what_to_check}} |
| {{dim_3}} | {{pct}}% | {{wha

### bld_quality_gate_quality_gate.md
---
id: p11_qg_quality_gate
kind: quality_gate
pillar: P11
title: "Gate: Quality Gate"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: quality_gate
quality: null
density_score: 0.85
tags:
  - quality-gate
  - p11
  - scoring
  - governance
  - recursive
tldr: "Recursive quality gate for quality_gate artifacts: verifies HARD/SOFT structure, weight math, and bypass rules."
---

## Definition
A quality gate artifact defines the acceptance criteria for one artifact kind. It contains blocking HARD gates (binary pass/fail), a weighted SOFT scoring table, a four-tier action map, and a bypass policy. This gate is self-applicable: it evaluates other quality gate files, including itself.
Scope: files with `kind: quality_gate`. Does not apply to scoring rubrics (P08), validators (P07), or benchmark suites (P13).
## HARD Gates
Failure on any single gate means REJECT regardless of soft score.
| ID  | Predicate | How to test |
|-----|-----------|-------------|
| H01 | Frontmatter parses as valid YAML | `yaml.safe_load(frontmatter)` raises no error |
| H02 | `id` matches namespace `p11_qg_*` | `id.startswith("p11_qg_")` is true |
| H03 | `id` equals filename stem | `Path(file).stem == id` |
| H04 | `kind` equals literal `quality_gate` | string equality check |
| H05 | `quality` is null at authoring time | `quality is None` |
| H06 | All required frontmatter fields present and non-empty | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr all present |
| H07 | HARD gates section present with >= 6 gates | count rows in HARD Gates table >= 6 |
| H08 | SOFT scoring table present with weights that sum to 100% when normalized | sum(weight_i / total_weight) == 1.0 within float tolerance |
| H09 | Actions section present with all four tiers: GOLDEN, PUBLISH, REVIEW, REJECT | all four tier names present in Actions table |
| H10 | Bypass section present with condition, approver, audit_log, and expiry fields | all four fields non-empty in Bypass table |
## SOFT Scoring
Score each dimension 0 (absent or fails) to 1 (present and passes). Weights are 0.5 or 1.0.
| #  | Dimension | Weight |
|----|-----------|--------|
| 1  | `density_score` field present and >= 0.80 | 1.0 |
| 2  | Universal HARD gates H01-H06 (YAML, id namespace, id=filename, kind, quality null, required fields) are all present | 1.0 |
| 3  | SOFT weights use only values 0.5 or 1.0 (no fractional intermediates) | 0.5 |
| 4  | Scoring formula is documented inline (not just assumed) | 1.0 |
| 5  | Bypass section explicitly states H01 and H05 cannot be bypassed | 1.0 |
| 6  | Tags list includes `quality-gate` | 0.5 |
| 7  | Tier thresholds match standard: GOLDEN >= 9.5, PUBLISH >= 8.0, REVIEW >= 7.0, REJECT < 7.0 | 1.0 |
| 8  | Every gate predicate is testable (binary outcome, no subjective language) | 1.0 |
| 9  | Gate set is domain-adapted, not a copy-paste of a generic template | 1.0 |
| 10 | `tldr` is <= 160 characters | 0.5 |
**Formula**: `final_score = (sum of score_i * weight_i) / (sum of weight_i) * 10`
Weight total: 8.5. Each dimension contributes proportionally. Score range: 0.0 to 10.0.
## Actions
| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool as golden; use as reference for new gate authors |
| PUBLISH | >= 8.0 | Publish to pool; mark production-ready |
| REVIEW | >= 7.0 | Return to author with scored dimension feedback; one revision cycle allowed |
| REJECT | < 7.0 | Block from pool; full rewrite required before re-evaluation |
## Bypass
| Field | Value |
|-------|-------|
| condition | Gate covers an experimental artifact kind in active design (schema not yet stable) |
| approver | Pillar owner must approve in writing before bypass takes effect |
| audit_log | Record in `records/pool/audits/bypasses.md` with date, approver, and reason |
| expiry | 14 days from bypass grant; gate must reach full compliance before expiry |

### bld_schema_quality_gate.md
---
kind: schema
id: bld_schema_quality_gate
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for quality_gate
pattern: TEMPLATE derives from this. CONFIG restricts this.
version: "2.0.0"
---

# Schema: quality_gate
## Frontmatter Fields
### Required (12)
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p11_qg_{slug}) | YES | — | Namespace compliance |
| kind | literal "quality_gate" | YES | — | Type integrity |
| pillar | literal "P11" | YES | — | Pillar assignment |
| title | string "Gate: {name}" | YES | — | Human label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| domain | string | YES | — | What this gate protects |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3, includes "quality-gate" | YES | — | Classification |
| tldr | string <= 160ch | YES | — | Dense summary |
### Recommended (1)
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| density_score | float 0.80-1.00 | REC | — | Content density metric |
## Gate Counts
| Metric | Type | Constraint | Rationale |
|--------|------|------------|-----------|
| hard_gates_count | integer | 8-10 required | <6 too permissive, >12 diminishing returns |
| soft_gates_count | integer | 5-20 recommended | Varies by kind complexity |
| scoring_weights_sum | percentage | MUST equal 100% | Invariant: all SOFT weights sum to 1.0 |
## Body Structure (5 required sections)
1. **Definition** — metric, threshold, operator, scope
2. **HARD Gates** — binary checks, all must pass (AND logic)
3. **SOFT Scoring** — weighted dimensions, each with explicit weight (0.5 or 1.0)
4. **Actions** — pass/fail/tier consequences (GOLDEN >= 9.5, PUBLISH >= 8.0, REVIEW >= 7.0, REJECT < 7.0)
5. **Bypass** — conditions, approver, audit trail, expiry; NEVER bypass H01 or H05
## Constraints
- max_bytes: 4096 (body only)
- naming: p11_qg_{gate_slug}.md
- id == filename stem
- threshold MUST be numeric
- scoring weights MUST sum to 100%
- quality: null always
- HARD gates: universal H01-H06 always present, kind-specific gates extend beyond
- SOFT gates: weight >= 0.5 (never use weight < 0.5)
- Bypass: MUST include condition + approver + audit_log + expiry fields
## Scoring Formula
```
hard_pass = ALL hard gates pass (AND)
soft_score = sum(gate * weight) / sum(weights)
final = hard_pass ? soft_score : 0
```
## ID Pattern
Regex: `^p11_qg_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `quality-gate-builder` for pipeline function `GOVERN`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
