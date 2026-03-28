# CEX Crew Runner -- Builder Execution
**Builder**: `golden-test-builder`
**Function**: GOVERN
**Intent**: reconstroi signal-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:33:56.849518

## Intent Context
- **Verb**: reconstroi
- **Object**: signal-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_golden_test.md
---
id: golden-test-builder
kind: type_builder
pillar: P07
parent: null
domain: golden_test
llm_function: BECOME
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [kind-builder, golden-test, P07, specialist, governance]
---

# golden-test-builder
## Identity
Especialista em construir golden_tests — casos de teste referencia quality 9.5+ para calibrar avaliacao de artefatos.
Conhece padroes de golden datasets, calibration sets, inter-rater reliability, e a diferenca entre golden_test (P07), few_shot_example (P01), e unit_eval (P07).
## Capabilities
- Selecionar artefatos quality 9.5+ como candidatos a golden
- Produzir golden_test com input/output completo e rationale mapeado a gates
- Validar golden_test contra quality gates (9 HARD + 7 SOFT)
- Mapear rationale para gates especificos do target_kind
- Distinguir golden_test de few_shot_example e unit_eval
## Routing
keywords: [golden-test, golden, reference-test, calibration, quality-baseline, evaluation]
triggers: "create golden test", "calibrate evaluation", "reference example for quality"
## Crew Role
In a crew, I handle QUALITY CALIBRATION.
I answer: "what does a perfect artifact of this kind look like?"
I do NOT handle: evaluation criteria (scoring-rubric-builder), pass/fail gates (quality-gate-builder), unit testing (unit-eval-builder [PLANNED]).

### bld_instruction_golden_test.md
---
kind: instruction
id: bld_instruction_golden_test
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for golden_test
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a golden_test
## Phase 1: RESEARCH
1. Identify the target artifact kind to calibrate — which kind needs a 9.5+ reference case?
2. Find existing 9.5+ quality examples as candidates — locate actual artifacts of that kind scoring at the top of the range
3. Study the target kind's quality gates — read its QUALITY_GATES.md to understand what makes an artifact excellent vs merely acceptable
4. Map rationale to specific gate IDs — for each gate, identify what the golden artifact does to satisfy it completely
5. Determine what distinguishes a 9.5 from an 8.0 — articulate the exact delta, not vague praise
6. Check existing golden_tests for the same kind — avoid producing a duplicate calibration reference
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all required fields
2. Read OUTPUT_TEMPLATE.md — fill following SCHEMA constraints
3. Fill frontmatter: all required fields, quality: null (never self-score), quality_threshold: 9.5 or higher
4. Write Input section: the complete input that would produce this golden artifact — verbatim, no abbreviation
5. Write Expected Output section: the full 9.5+ quality artifact — complete, not summarized
6. Write Rationale section: per-gate explanation of why this artifact scores 9.5+ — cite gate IDs explicitly
7. Write Gate Mapping section: table of which quality gates this golden satisfies and how each is met
8. Write Boundary Notes section: what a near-miss 8.0 version would look like — the specific gaps that drop the score
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — run all HARD gates for this builder manually
2. HARD gates:
   - [ ] id matches `p07_gt_[a-z][a-z0-9_]+`
   - [ ] kind == `golden_test`
   - [ ] quality == null
   - [ ] quality_threshold >= 9.5
   - [ ] input section is complete
   - [ ] expected output is present and unabbreviated
   - [ ] rationale maps to specific gate IDs
3. SOFT gates: gate mapping table present, boundary notes distinguish 9.5 from 8.0, reviewer assigned
4. Cross-check: calibration reference not format example (that is few_shot_example)? Not pass/fail assertion (that is unit_eval)? Not performance measurement (that is benchmark)? Rationale is gate-specific not generic praise?
5. Verify the expected output passes ALL HARD gates of the target kind's own builder before finalizing
6. If score < 8.0: revise in the same pass before outputting

### bld_knowledge_card_golden_test.md
---
kind: knowledge_card
id: bld_knowledge_card_golden_test
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for golden_test production — quality calibration reference tests
sources: ML golden datasets, SWE-bench, DeepEval, BLEU/ROUGE reference patterns
---

# Domain Knowledge: golden_test
## Executive Summary
Golden tests are curated reference artifacts scoring >= 9.5 that serve as calibration points for builders and validators. They provide exemplary input/output pairs with rationale mapping each quality dimension to specific gates. Golden tests differ from few-shot examples (format teaching without scoring), unit evals (any quality level), and scoring rubrics (criteria definition without examples).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P07 (governance/evaluation) |
| Quality threshold | >= 9.5 |
| Quality gates | 9 HARD + 7 SOFT |
| Approval | Reviewer-approved (producer cannot self-approve) |
| Key sections | input, golden_output, rationale (gate-mapped) |
| Target scoping | Scoped to specific artifact kind |
## Patterns
- **Exemplary, not just correct**: golden means demonstrating best practices across all quality dimensions — not merely passing
- **Rationale gate-mapping**: every golden test maps its rationale to specific quality gate IDs for traceability
| Source | Concept | Application |
|--------|---------|-------------|
| ML golden datasets | Labeled ground truth | Reference artifacts for calibration |
| BLEU/ROUGE | Human reference translations | Golden output as evaluation anchor |
| SWE-bench | Verified code test cases | Curated, reviewer-approved cases |
| DeepEval | Expected LLM outputs | Input/golden_output with rationale |
- **Complete output**: golden output must be COMPLETE — no "...", no abbreviations, no placeholders
- **Reviewer approval mandatory**: producer cannot approve their own golden test — independent review required
- **Edge case separation**: standard golden tests and edge case golden tests are separate artifacts
- **Target kind scoping**: each golden test targets a specific artifact kind — not generic
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Self-approved golden test | No independent quality check; bias |
| Rationale without gate IDs | Traceability broken; cannot verify which gates pass |
| Abbreviated output ("...") | Incomplete reference; calibrator misses expected format |
| Mixed standard + edge cases | Confuses calibration; separate into distinct tests |
| quality_threshold < 9.5 | Below golden standard; that is a unit_eval |
| Unscoped (no target_kind) | Applies to nothing specific; useless for calibration |
## Application
1. Select candidate: artifact scoring >= 9.5 in target kind
2. Capture input: the exact prompt/request that produced the artifact
3. Capture golden_output: complete output with no abbreviations
4. Write rationale: map every quality dimension to specific gate IDs
5. Submit for review: independent reviewer must approve
6. Validate: quality >= 9.5, complete output, gate-mapped rationale, reviewer approved
## References
- SWE-bench: verified test cases for code generation (swebench.com)
- DeepEval: golden evaluation framework (confident-ai.com)
- BLEU/ROUGE: reference-based evaluation metrics for NLP
- ML golden datasets: ground truth annotation best practices

### bld_quality_gate_golden_test.md
---
id: p11_qg_golden_test
kind: quality_gate
pillar: P11
title: "Gate: golden_test"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "edison"
domain: "golden_test — reference quality calibration cases scoring 9.5+ with rationale mapped to evaluation gates"
quality: null
tags: [quality-gate, golden-test, calibration, evaluation, quality-baseline, P11]
tldr: "Validates golden_test artifacts: verified 9.5+ source quality, rationale-to-gate mapping, and non-self-referential target kind."
density_score: 0.93
---

# Gate: golden_test
## Definition
| Field     | Value |
|-----------|-------|
| metric    | composite score across SOFT dimensions |
| threshold | >= 7.0 to publish; >= 9.5 for golden (the golden_test itself must also reach 9.5) |
| operator  | weighted average after all HARD gates pass |
| scope     | all artifacts where `kind: golden_test` |
All HARD gates are AND-logic: one failure rejects the artifact regardless of SOFT score.
## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Any YAML syntax error |
| H02 | ID matches `^p07_gt_[a-z][a-z0-9_]+$` | Wrong format or namespace |
| H03 | ID equals filename stem (no extension) | Mismatch between id field and file name |
| H04 | Kind equals literal `golden_test` | Any other value |
| H05 | `quality` field is null | Any non-null value |
| H06 | Required fields present: id, kind, pillar, version, created, updated, author, target_kind, quality_threshold, reviewer, domain, quality, tags, tldr | Any missing field |
| H07 | `quality_threshold` >= 9.5 | Threshold below the golden standard |
| H08 | `target_kind` is non-empty and NOT `golden_test` | Self-referential calibration |
| H09 | `Golden Output` section present and non-empty | No reference output to calibrate against |
| H10 | `Input Scenario` section present and non-empty | No input; test is unverifiable |
| H11 | `rationale` references at least one gate ID (pattern: H\d+ or S\d+) | No gate mapping; rationale is unstructured |
## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| S01 | `tldr` <= 160 chars, names `target_kind` and what makes this golden | 0.10 | Named=1.0, vague=0.3 |
| S02 | Tags list len >= 3, includes `target_kind` as keyword | 0.06 | Present=1.0, absent=0.0 |
| S03 | Rationale maps to >= 3 distinct gate IDs of `target_kind` | 0.15 | 3+=1.0, 2=0.6, 1=0.3, 0=0.0 |
| S04 | Golden Output is complete and copy-pasteable as a real artifact | 0.14 | Complete=1.0, skeleton=0.4, absent=0.0 |
| S05 | Input Scenario is non-trivial (edge case or high-complexity scenario) | 0.12 | Edge/complex=1.0, trivial=0.3 |
| S06 | Boundary from `few_shot_example` stated (teaches format vs. evaluates quality) | 0.09 | Explicit=1.0, implied=0.4, absent=0.0 |
| S07 | Boundary from `unit_eval` stated | 0.07 | Explicit=1.0, implied=0.4, absent=0.0 |
| S08 | Verification source cited for 9.5+ quality claim (reviewer name or process) | 0.10 | Cited=1.0, absent=0.0 |
| S09 | Evaluation Criteria section present with pass/fail conditions | 0.10 | Present=1.0, absent=0.0 |
| S10 | `density_score` >= 0.85 (golden tests must be information-dense) | 0.07 | Met=1.0, below=0.0 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — accepted into calibration set; informs all future scoring for `target_kind` |
| >= 8.0 | PUBLISH — pool-eligible reference; not yet calibration-authoritative |
| >= 7.0 | REVIEW — rationale incomplete or verification source missing |
| < 7.0  | REJECT — redo; likely unverified source quality or missing gate mapping |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Bootstrap only: first golden_test for a brand-new kind where no prior calibration set exists |
| approver | Two independent reviewers must sign off in lieu of automated verification |
| audit trail | Required: both reviewer names, review date, written agreement on quality assessment |

### bld_schema_golden_test.md
---
kind: schema
id: bld_schema_golden_test
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for golden_test
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: golden_test
## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p07_gt_{case_slug}) | YES | — | Namespace compliance |
| kind | literal "golden_test" | YES | — | Type integrity |
| pillar | literal "P07" | YES | — | Pillar assignment |
| title | string "Golden: {name}" | YES | — | Human label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| target_kind | string | YES | — | Artifact kind being tested |
| input | string | YES | — | Request/prompt that triggers production |
| golden_output_ref | string | YES | — | Path to golden artifact or "inline" |
| quality_threshold | float >= 9.5 | YES | 9.5 | Golden floor |
| rationale | string | YES | — | Why golden, with gate refs |
| domain | string | YES | — | Domain this test covers |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Searchability |
| tldr | string <= 160ch | YES | — | Dense summary |
### Recommended
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| edge_case | boolean | REC | false | Edge case flag |
| reviewer | string | REC | — | Who approved as golden |
| approval_date | date YYYY-MM-DD | REC | — | Approval timestamp |
| linked_artifacts | object {primary, related} | REC | — | Cross-references |
| density_score | float 0.80-1.00 | REC | — | Content density |
## ID Pattern
Regex: `^p07_gt_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Input Scenario` — the complete request/prompt (verbatim)
2. `## Golden Output` — the full artifact (no abbreviation, no "...")
3. `## Rationale` — why golden, mapped to gate IDs (H01, S03, etc.)
4. `## Evaluation Criteria` — specific checks this golden validates
## Constraints
- max_bytes: 4096 (body only)
- naming: p07_gt_{case_slug}.md
- id == filename stem
- quality_threshold MUST be >= 9.5
- golden_output MUST be complete (no truncation)
- quality: null always
- rationale MUST reference gate IDs

### bld_examples_golden_test.md
---
kind: examples
id: bld_examples_golden_test
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of golden_test artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: golden-test-builder
## Golden Example
INPUT: "Cria golden test de knowledge_card sobre prompt caching"
OUTPUT:
```yaml
id: p07_gt_kc_prompt_caching
kind: golden_test
pillar: P07
title: "Golden: KC Prompt Caching"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
target_kind: "knowledge_card"
input: "Destila conhecimento sobre prompt caching para otimizar custos LLM"
golden_output_ref: "inline"
quality_threshold: 9.5
rationale: "H01-H10 pass, S01-S18 pass. All HARD gates clear. Density 0.93, actionable, sourced."
edge_case: false
reviewer: "orchestrator"
approval_date: "2026-03-26"
domain: "knowledge"
quality: null
tags: [golden-test, knowledge-card, calibration]
tldr: "Reference KC: prompt caching, density 0.93, all 10 HARD + 18 SOFT gates pass"
density_score: 0.93
linked_artifacts:
  primary: "quality-gate-builder"
  related: [p11_qg_kc_publish]
## Input Scenario
Destila conhecimento sobre prompt caching para otimizar custos LLM.
Foco: como funciona, quando usar, economia esperada, limitacoes.
## Golden Output
id: p01_kc_prompt_caching
kind: knowledge_card
pillar: P01
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "knowledge-engine"
domain: "llm_optimization"
quality: null
tags: [prompt-caching, cost-optimization, llm, anthropic]
tldr: "Prompt caching reuses prefixes across API calls, cutting costs 90% and latency 85%"
density_score: 0.93
## Conceitos
- Prompt caching stores computed prefixes server-side for reuse
- Minimum cacheable prefix: 1024 tokens (Anthropic), 128 tokens (OpenAI)
- Cache TTL: 5 minutes (Anthropic), session-scoped (OpenAI)
- Write cost: 1.25x base price; read cost: 0.1x base price
## Quando Usar
- System prompts > 1024 tokens repeated across requests
- Few-shot examples reused in batch processing
- Tool definitions shared across conversation turns
- RAG contexts with stable document prefixes
## Economia Esperada
- Anthropic: 90% cost reduction on cached tokens, 85% latency reduction
- OpenAI: 50% cost reduction on cached tokens
- Break-even: 2+ requests with same prefix within TTL window
## Limitacoes
- Prefix must be identical byte-for-byte (no variation allowed)
- Cache eviction after TTL — no persistence guarantee
- Only prefix caching (beginning of prompt, not middle/end)
- Minimum token threshold — short prompts get no benefit
## Comparativo
| Provider | Min Tokens | TTL | Write Cost | Read Cost |
|----------|-----------|-----|------------|-----------|
| Anthropic | 1024 | 5 min | 1.25x | 0.1x |
| OpenAI | 128 | session | 1.0x | 0.5x |
| Google | 32768 | 1 hour | 1.0x | 0.25x |
## References
- https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
- https://platform.openai.com/docs/guides/prompt-caching
## Rationale
- YAML parses without error (H01 pass)
- id starts with p01_kc_ (H02 pass)
- id == filename stem (H03 pass)
- kind == knowledge_card (H04 pass)
- quality == null (H05 pass)
- body >= 3 bullet points per section (H06 pass)
- size <= 5120 bytes (H07 pass)
- tags is list with >= 3 items (S02 pass)
- density >= 0.80 (actual 0.93) (S07 pass)
- All 6 body sections present with concrete data (S03-S06 pass)
- Comparativo table has real provider data with URLs (S08 pass)
## Evaluation Criteria
- [ ] All 10 KC HARD gates pass
- [ ] Density >= 0.90 (golden threshold)
- [ ] Every bullet is concrete (no filler)
- [ ] Comparativo has >= 3 providers with URLs
- [ ] Economia section has specific percentages
```
WHY THIS IS GOLDEN:
- quality: null (H06 pass)
- id matches p07_gt_ pattern (H02 pass)
- kind: golden_test (H04 pass)
- 22 frontmatter fields present (H08 pass)
- quality_threshold == 9.5 (H07 pass)
- rationale maps to specific gate IDs H01-H07, S02-S08 (S03 pass)
- golden_output is complete KC with all sections (S04 pass)
- reviewer assigned: orchestrator (S06 pass)

### bld_config_golden_test.md
---
kind: config
id: bld_config_golden_test
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for golden_test production
pattern: CONFIG restricts SCHEMA, never contradicts
---

# Config: golden_test Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p07_gt_{case_slug}.md | p07_gt_kc_prompt_caching.md |
| Builder dir | kebab-case | golden-test-builder/ |
| Fields | snake_case | quality_threshold, target_kind |
Rule: id MUST equal filename stem.
## File Paths
- Output: cex/P07_evals/examples/p07_gt_{case_slug}.md
- Compiled: cex/P07_evals/compiled/p07_gt_{case_slug}.yaml
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Density: >= 0.80
- Golden output: no truncation (complete artifact required)
## Quality Threshold Policy
- quality_threshold minimum: 9.5 (non-negotiable)
- Reviewer approval required before golden status
- Producer CANNOT self-approve as reviewer

### bld_output_template_golden_test.md
---
kind: output_template
id: bld_output_template_golden_test
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for golden_test production
pattern: derives from SCHEMA.md — no extra fields
---

# Output Template: golden_test
```yaml
id: p07_gt_{{case_slug}}
kind: golden_test
pillar: P07
title: "Golden: {{case_name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
target_kind: "{{artifact_kind_being_tested}}"
input: "{{request_prompt}}"
golden_output_ref: "{{path_or_inline}}"
quality_threshold: {{9.5_or_higher}}
rationale: "{{why_golden_with_gate_refs}}"
edge_case: {{true_or_false}}
reviewer: "{{who_approved}}"
approval_date: "{{YYYY-MM-DD}}"
domain: "{{domain_value}}"
quality: null
tags: [golden-test, {{target_kind}}, {{domain}}]
tldr: "{{dense_summary_max_160ch}}"
density_score: {{0.80_to_1.00}}
linked_artifacts:
  primary: "{{target_kind_builder_or_schema}}"
  related: [{{related_artifact_refs}}]
## Input Scenario
{{verbatim_request_or_prompt}}
## Golden Output
{{complete_artifact_no_abbreviation}}
## Rationale
{{mapped_to_gate_ids_h01_s03_etc}}
## Evaluation Criteria
{{specific_checks_this_validates}}
## References
- {{reference_1}}
- {{reference_2}}
```

### bld_architecture_golden_test.md
---
kind: architecture
id: bld_architecture_golden_test
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of golden_test — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| target_kind | The artifact type this golden test calibrates (e.g., knowledge_card, formatter) | golden_test | required |
| input | The exact task request used to produce the reference artifact | golden_test | required |
| output | The reference artifact itself; must score >= 9.5 on all quality gates | golden_test | required |
| rationale | Mapping of output qualities to specific gate criteria; explains WHY it is golden | golden_test | required |
| quality_score | Verified score (>= 9.5); assigned after independent review, not self-assessed | golden_test | required |
| gate_mapping | List of quality gates from the target_kind that this test anchors | golden_test | required |
| reviewer | Identity of the independent evaluator who confirmed the score | golden_test | required |
| created_date | Date the golden test was certified; used for staleness checks | golden_test | required |
## Dependency Graph
```
scoring_rubric (P07) --produces--> golden_test
quality_gate (P11)   --depends-->  golden_test
golden_test          --produces--> unit_eval (P07)
golden_test          --produces--> benchmark (P07)
few_shot_example (P01) --depends--> golden_test
```
| From | To | Type | Data |
|------|----|------|------|
| scoring_rubric (P07) | golden_test | produces | evaluation dimensions and criteria the output must satisfy |
| quality_gate (P11) | golden_test | depends | pass/fail thresholds used to verify the 9.5+ score |
| golden_test | unit_eval (P07) | produces | ground-truth reference for test case comparison |
| golden_test | benchmark (P07) | produces | quality anchor for performance measurement baselines |
| few_shot_example (P01) | golden_test | depends | exemplary input/output pairs that may become golden candidates |
## Boundary Table
| golden_test IS | golden_test IS NOT |
|----------------|-------------------|
| A reference artifact certified at quality >= 9.5 | A test at any quality level (that is unit_eval) |
| A calibration anchor — defines what "perfect" looks like | A quick sanity check for system health (that is smoke_eval) |
| Independently reviewed; score is externally verified | A scoring rubric that defines evaluation criteria |
| Specific to one artifact type (target_kind) | An end-to-end pipeline test spanning multiple artifacts |
| A ground-truth source consumed by unit_eval and benchmark | A few-shot example used to teach format (not to measure quality) |
| Immutable once certified; changes require re-certification | A live metric updated continuously during operation |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| Criteria | scoring_rubric (P07), quality_gate (P11) | Define evaluation dimensions and pass/fail thresholds |
| Certification | quality_score, reviewer, created_date | Record the verified 9.5+ score and its provenance |
| Content | input, output, target_kind | The reference artifact and the task that produced it |
| Rationale | rationale, gate_mapping | Explain which gates are satisfied and why the output qualifies |
| Consumers | unit_eval (P07), benchmark (P07) | Use the golden test as a quality calibration reference |

### bld_collaboration_golden_test.md
---
kind: collaboration
id: bld_collaboration_golden_test
pillar: P12
llm_function: COLLABORATE
purpose: How golden-test-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: golden-test-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what does a perfect artifact of this kind look like?"
I do not define evaluation criteria. I do not measure performance.
I produce quality-calibration references so evaluation systems have a gold standard for comparison.
## Crew Compositions
### Crew: "Quality Pipeline"
```
  1. golden-test-builder -> "reference examples (quality 9.5+)"
  2. benchmark-builder -> "performance baselines"
  3. e2e-eval-builder -> "end-to-end pipeline validation against golden"
```
### Crew: "Builder Calibration"
```
  1. golden-test-builder -> "perfect artifact example for target kind"
  2. few-shot-example-builder -> "format examples derived from golden"
  3. action-prompt-builder -> "prompt calibrated to produce golden-quality output"
```
## Handoff Protocol
### I Receive
- seeds: target artifact kind, quality gates for that kind
- optional: existing high-quality artifacts (9.5+), rationale mapping
### I Produce
- golden_test artifact (.md + .yaml frontmatter with input/output/rationale)
- committed to: `cex/P07/examples/p07_golden_{kind}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0). Golden tests are selected from existing high-quality output.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| e2e-eval-builder | Compares pipeline output against golden reference |
| few-shot-example-builder | Derives format examples from golden artifacts |
| action-prompt-builder | Calibrates prompts using golden output as target |
| benchmark-builder | Uses golden output quality as performance ceiling |

### bld_memory_golden_test.md
---
id: p10_lr_golden_test_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: edison
observation: "Golden tests built from artifacts scoring 9.4 or below fail the quality_threshold >= 9.5 gate. Truncated golden_output fields with ellipsis cause test instability — partial outputs cannot be used as reference. Rationale written as prose ('it's a good example') without gate IDs provides no actionable pass/fail signal. Producer self-approving as reviewer undermines the independence requirement. Golden tests confused with few_shot_example (P01) — golden tests evaluate quality, examples teach format."
pattern: "Source artifact must score >= 9.5 before being nominated as a golden test candidate. golden_output must be the complete artifact with no truncation. Rationale maps explicitly to gate IDs (H01-H10, S01-S10) stating which gate each section of the output satisfies. Producer and reviewer must be different roles — producer cannot self-approve. quality field is always null (self-scoring rejected). quality_threshold is always >= 9.5."
evidence: "9 golden test artifacts validated. 100% of golden_output truncated with '...' caused test instability in regression runs. Rationale with explicit gate IDs reduced reviewer time by ~50% vs prose rationale. All producer-self-approved tests were rejected and required external review before pool admission."
confidence: 0.75
outcome: SUCCESS
domain: golden_test
tags: [golden_test, quality_gate, gate_mapping, reviewer_independence, complete_output, 9_5_threshold]
tldr: "Source must score >= 9.5; output must be complete; rationale maps to gate IDs; producer cannot self-approve."
impact_score: 7.5
decay_rate: 0.04
satellite: edison
keywords: [golden_test, quality_threshold, gate_ids, rationale, reviewer_independence, complete_artifact, pool_admission, regression]
---

## Summary
A golden test is a high-quality artifact paired with gate-mapped rationale that serves as a regression anchor. Its purpose is to evaluate whether new outputs meet the same standard — not to teach format (that is few_shot_example). The source artifact must already score >= 9.5. The output must be complete. The rationale must reference specific gate IDs, not prose opinions.
## Pattern
1. Source artifact must have a documented quality score >= 9.5 before nomination as a golden test.
2. `golden_output` contains the complete artifact — no truncation, no ellipsis, no summarization.
3. `rationale` maps to explicit gate IDs: "H01: id format valid. H02: pillar prefix correct. S04: input is specific and realistic."
4. `quality_threshold` is always >= 9.5. Values below this are rejected by schema validator H07.
5. `quality` field is always null — self-scoring is rejected by H06.
6. Producer and reviewer are different roles. The engineer who built the artifact cannot be its golden test reviewer.
7. Candidates come from three sources: pool artifacts with quality >= 9.5 in metadata, builder EXAMPLES.md golden sections, or manually curated domain expert artifacts.
## Anti-Pattern
- Source artifact with quality 9.4 or below — below-threshold sources produce below-threshold golden tests.
- Truncated `golden_output` with "..." — partial output cannot serve as a regression reference, test results become unstable.
- Rationale as prose opinion ("this is well-structured and thorough") — no gate IDs means no actionable pass/fail signal for reviewers.
- Producer self-approving as reviewer — independence is required; the builder cannot be the judge of their own output.
- Confusing golden_test (P07, evaluates quality) with few_shot_example (P01, teaches format) — different artifacts, different pillars, different purposes.
- `quality_threshold: 9.0` — below the minimum of 9.5 for golden test classification.
## Context
Applies when: an artifact has achieved >= 9.5 quality and should serve as a stable regression reference for future outputs of the same type.


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `golden-test-builder` for pipeline function `GOVERN`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
