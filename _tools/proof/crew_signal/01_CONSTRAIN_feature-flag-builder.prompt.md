# CEX Crew Runner -- Builder Execution
**Builder**: `feature-flag-builder`
**Function**: CONSTRAIN
**Intent**: reconstroi signal-builder
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:29:34.532522

## Intent Context
- **Verb**: reconstroi
- **Object**: signal-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_feature_flag.md
---
id: feature-flag-builder
kind: type_builder
pillar: P09
parent: null
domain: feature_flag
llm_function: GOVERN
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [kind-builder, feature-flag, P09, config, toggle, rollout]
---

# feature-flag-builder
## Identity
Especialista em construir feature_flag artifacts — definicoes de flags de feature com
controle on/off e rollout gradual. Domina feature toggle patterns (release, experiment,
ops, permission), percentage-based rollout, cohort targeting, kill switches, e a boundary
entre feature_flag (on/off logico) e env_config (P09, variavel generica) ou permission
(P09, controle de acesso). Produz feature_flag artifacts com frontmatter completo e
flag specification documentada.
## Capabilities
- Definir feature flags com estado (on/off), rollout percentage, e targeting rules
- Especificar flag categories: release, experiment, ops, permission
- Documentar rollout strategy (instant, gradual, cohort-based)
- Definir kill switch behavior e fallback defaults
- Validar artifact contra quality gates (8 HARD + 10 SOFT)
- Distinguir feature_flag de env_config, permission, path_config, runtime_rule
## Routing
keywords: [feature, flag, toggle, rollout, experiment, release, kill_switch, gradual, percentage, canary]
triggers: "create feature flag", "define feature toggle", "set up gradual rollout", "configure kill switch"
## Crew Role
In a crew, I handle FEATURE FLAG SPECIFICATION.
I answer: "should this feature be on or off, for whom, and with what rollout strategy?"
I do NOT handle: env_config (generic variables), permission (access control),
path_config (filesystem paths), runtime_rule (timeouts/retries).

### bld_instruction_feature_flag.md
---
kind: instruction
id: bld_instruction_feature_flag
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for feature_flag
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a feature_flag
## Phase 1: RESEARCH
1. Identify the feature to flag and write a one-sentence description of what it enables or disables
2. Classify the flag type: release (controls a new feature shipping), experiment (A/B or multivariate test), ops (operational kill switch), or permission (access control by user segment)
3. Determine the initial state: on or off at the moment of creation
4. Define the rollout strategy: instant (flip to 100% at once), gradual percentage (increase over a schedule), or cohort-based (specific user segments only)
5. Identify targeting rules: which user segments, environments, or override conditions see which state
6. Define kill switch behavior: how to emergency-disable the flag, who is notified, and what the system falls back to
7. Check existing feature_flags via brain_query [IF MCP] for conflicts — two flags must not control the same code path simultaneously
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints
3. Fill all required frontmatter fields; set `quality: null` — never self-score
4. Write **Flag Definition** section: name, type, description, initial state (on/off)
5. Write **Rollout Strategy** section: method name, percentage schedule with dates, cohort definition if applicable
6. Write **Targeting Rules** section: who sees which state — segments, environments, per-user overrides
7. Write **Kill Switch** section: emergency disable procedure, notification targets, fallback behavior
8. Write **Defaults** section: value returned when the flag service is unavailable or the flag key is missing
9. Write **Lifecycle** section: creation date, expected removal date (required — flags without removal dates accumulate as technical debt), and owner
10. Confirm body <= 1536 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm `id` matches `^p09_ff_[a-z][a-z0-9_]+$`
4. Confirm `default_state` is the string "on" or "off" — no other values
5. Confirm rollout strategy is defined with a concrete method
6. Confirm kill switch behavior is documented
7. Confirm Lifecycle section includes a removal date
8. Confirm `quality` is null
9. Confirm body <= 1536 bytes
10. Cross-check: is this an on/off toggle for a specific feature? If it catalogs general runtime variables it belongs in `env_config`. If it controls user access roles it belongs in `permission`. If it specifies file system locations it belongs in `path_config`. Flags toggle discrete behaviors, they do not store configuration values.
11. If score < 8.0: revise in the same pass before outputting

### bld_knowledge_card_feature_flag.md
---
kind: knowledge_card
id: bld_knowledge_card_feature_flag
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for feature_flag production — feature toggle specification
sources: Fowler 2017 "Feature Toggles", LaunchDarkly, Unleash, Split.io
---

# Domain Knowledge: feature_flag
## Executive Summary
Feature flags are on/off toggles that control feature availability at runtime without code deploys. They support four categories: release (ship incomplete code safely), experiment (A/B tests), ops (kill switches), and permission (premium features). Feature flags differ from env configs (generic variables), permissions (access control), and runtime rules (behavior parameters).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P09 (config) |
| llm_function | GOVERN |
| Frontmatter fields | 15+ |
| Quality gates | 8 HARD + 10 SOFT |
| Categories | release, experiment, ops, permission |
| Default state | OFF for new features, ON for kill switches |
| Rollout pattern | 0% → 5% → 25% → 50% → 100% |
## Patterns
- **Four toggle categories** (Fowler 2017):
| Category | Lifecycle | Default | Example |
|----------|-----------|---------|---------|
| Release | Short (remove after launch) | OFF | enable_new_checkout |
| Experiment | Medium (remove after A/B) | OFF | test_search_algorithm_v2 |
| Ops | Long (keep for emergencies) | ON | enable_cache_layer |
| Permission | Permanent | OFF | premium_export_feature |
- **Gradual rollout**: increase percentage in stages (0→5→25→50→100), monitoring metrics at each step
- **Kill switch pattern**: ops flags start ON, turn OFF to disable in emergency — instant recovery without deploy
- **Cohort targeting**: by user ID, region, or plan tier — more controlled than random percentage
- **Stale flag cleanup**: remove flags after full rollout — every active flag is tech debt
- **Flag naming**: descriptive with domain prefix (enable_dark_mode, use_new_search_v2)
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Never removing flags after launch | Accumulates tech debt; code becomes unreadable |
| Kill switch defaults to OFF | Emergency recovery requires deployment — defeats purpose |
| 100% rollout on day one | No gradual confidence building; hard to rollback |
| Flag controls multiple features | Coupling; cannot toggle independently |
| No monitoring at rollout stages | Cannot detect regressions caused by new feature |
| Vague flag name ("flag_1") | Nobody knows what it controls; becomes permanent tech debt |
## Application
1. Define flag: name (descriptive), category (release/experiment/ops/permission)
2. Set default state: OFF for new features, ON for kill switches
3. Design rollout: percentage stages with monitoring criteria at each step
4. Define targeting: random percentage, cohort (user ID/region), or all
5. Plan lifecycle: when to remove flag (release/experiment) or keep (ops/permission)
6. Validate: name is descriptive, category matches lifecycle, default is correct
## References
- Fowler 2017: Feature Toggles (martinfowler.com/articles/feature-toggles.html)
- LaunchDarkly: feature flag lifecycle and best practices
- Unleash: gradual rollout strategies and user targeting
- Hodgson 2017: Feature Toggles patterns and practices

### bld_quality_gate_feature_flag.md
---
id: p11_qg_feature_flag
kind: quality_gate
pillar: P11
title: "Gate: feature_flag"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "edison"
domain: "feature_flag — on/off toggles with rollout percentage, cohort targeting, and kill switch behavior"
quality: null
tags: [quality-gate, feature-flag, toggle, rollout, P11]
tldr: "Validates feature_flag artifacts: toggle semantics, rollout strategy completeness, and kill switch safety."
density_score: 0.91
---

# Gate: feature_flag
## Definition
| Field     | Value |
|-----------|-------|
| metric    | composite score across SOFT dimensions |
| threshold | >= 7.0 to publish; >= 9.5 for golden |
| operator  | weighted average after all HARD gates pass |
| scope     | all artifacts where `kind: feature_flag` |
All HARD gates are AND-logic: one failure rejects the artifact regardless of SOFT score.
## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Any YAML syntax error |
| H02 | ID matches `^p09_ff_[a-z][a-z0-9_]+$` | Wrong format or namespace |
| H03 | ID equals filename stem (no extension) | Mismatch between id field and file name |
| H04 | Kind equals literal `feature_flag` | Any other value |
| H05 | `quality` field is null | Any non-null value |
| H06 | Required fields present: id, kind, pillar, version, created, updated, author, flag_name, default_state, category, rollout_percentage, quality, tags, tldr | Any missing field |
| H07 | Body has sections: `## Flag Specification`, `## Rollout Strategy`, `## Lifecycle` | Any required section absent |
| H08 | `default_state` is one of: `on`, `off` | Any other value |
| H09 | `rollout_percentage` is integer 0–100 | Out of range or non-integer |
| H10 | `category` is one of: `release`, `experiment`, `ops`, `permission` | Any unlisted value |
## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| S01 | `tldr` <= 160 chars, names flag and toggle behavior | 0.10 | Accurate=1.0, vague=0.4, absent=0.0 |
| S02 | Tags list len >= 3, includes `feature_flag` | 0.05 | Met=1.0, partial=0.5 |
| S03 | `flag_name` is snake_case and descriptive | 0.07 | Snake_case+descriptive=1.0, generic=0.3 |
| S04 | Rollout strategy has stages with explicit percentages | 0.12 | All stages=1.0, partial=0.5, absent=0.0 |
| S05 | Kill switch behavior documented | 0.10 | Explicit=1.0, implied=0.4, absent=0.0 |
| S06 | Cohort targeting rules defined when `rollout_percentage` < 100 | 0.10 | Defined=1.0, missing when needed=0.0, N/A=1.0 |
| S07 | Lifecycle section includes retire or sunset date | 0.08 | Present=1.0, absent=0.0 |
| S08 | Rollback procedure described step-by-step | 0.10 | Step-by-step=1.0, brief=0.5, absent=0.0 |
| S09 | Observability hook defined (metric or log emitted on toggle change) | 0.10 | Present=1.0, absent=0.0 |
| S10 | Boundary from `env_config` and `permission` stated | 0.08 | Both stated=1.0, one=0.5, absent=0.0 |
| S11 | `density_score` >= 0.80 | 0.07 | Met=1.0, below=0.0 |
| S12 | No filler phrases ("designed to enable", "various use cases") | 0.03 | Clean=1.0, filler present=0.0 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — reference artifact for feature_flag calibration |
| >= 8.0 | PUBLISH — pool-eligible; rollout strategy and kill switch documented |
| >= 7.0 | REVIEW — usable but missing sunset date or observability hook |
| < 7.0  | REJECT — redo; likely missing rollback procedure or cohort rules |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Hotfix rollout only; flag controls an active incident mitigation with no time to complete all gates |
| approver | Product owner or on-call engineer |
| audit trail | Required: incident ticket, timestamp, approver handle |
| expiry | 24 hours; must be replaced with compliant artifact |
| never bypass | H01 (corrupt YAML), H05 (self-scored quality is invalid), H08 (boolean semantics must be exact for runtime evaluation) |

### bld_schema_feature_flag.md
---
kind: schema
id: bld_schema_feature_flag
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for feature_flag
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: feature_flag
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_ff_{feature_slug}) | YES | - | Namespace compliance |
| kind | literal "feature_flag" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| flag_name | string | YES | - | Human-readable flag name |
| default_state | enum: on, off | YES | off | Default state when no targeting matches |
| category | enum: release, experiment, ops, permission | YES | - | Flag category per Fowler |
| rollout_percentage | integer 0-100 | YES | 0 | Current rollout percentage |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "feature_flag" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What this flag controls |
| owner | string | REC | - | Team or person responsible |
| expires | date YYYY-MM-DD | REC | - | Stale flag cleanup date |
| targeting | string | REC | - | Targeting strategy summary |
## ID Pattern
Regex: `^p09_ff_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Flag Specification` — what feature, current state, rollout %, kill switch behavior
2. `## Rollout Strategy` — how to ramp: stages, percentage, timeline, cohorts
3. `## Lifecycle` — created, test, ramp, full rollout, retire/cleanup plan
## Constraints
- max_bytes: 1536 (body only — feature_flag is compact)
- naming: p09_ff_{feature_slug}.yaml
- machine_format: json (compiled artifact)
- id == filename stem
- default_state MUST be "on" or "off" (no "maybe", "partial")
- rollout_percentage MUST be integer 0-100
- quality: null always

### bld_examples_feature_flag.md
---
kind: examples
id: bld_examples_feature_flag
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of feature_flag artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: feature-flag-builder
## Golden Example
INPUT: "Create a feature flag for the new search algorithm with gradual rollout"
OUTPUT:
```yaml
id: p09_ff_enable_vector_search
kind: feature_flag
pillar: P09
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "EDISON"
flag_name: "enable_vector_search"
default_state: off
category: release
rollout_percentage: 0
quality: null
tags: [feature_flag, search, release, P09, vector]
tldr: "Vector search release flag: off by default, 4-stage rollout to 100% over 2 weeks"
description: "Controls activation of vector-based search replacing keyword search"
owner: "search_team"
expires: "2026-05-01"
targeting: "percentage-based, all users"
```
## Flag Specification
Enables vector-based semantic search to replace legacy keyword search.
Default OFF — legacy keyword search serves all users until flag ramps.
Kill switch: set rollout_percentage to 0 to instantly revert to keyword search.
## Rollout Strategy
| Stage | Percentage | Duration | Criteria |
|-------|-----------|----------|----------|
| canary | 5% | 3 days | error rate < 0.1%, latency < 200ms |
| early | 25% | 4 days | no regressions, user feedback positive |
| broad | 50% | 3 days | metrics stable, no support tickets |
| full | 100% | permanent | retire flag after 2 weeks stable |
## Lifecycle
- Created: 2026-03-26 (flag defined, code deployed behind flag)
- Test: internal QA with flag ON in staging
- Ramp: canary 5% -> early 25% -> broad 50% -> full 100%
- Retire: 2026-05-01 (remove flag, vector search becomes default)
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p09_ff_ pattern (H02 pass)
- kind: feature_flag (H04 pass)
- 19 required+recommended fields present (H06 pass)
- body has all 3 sections: Flag Specification, Rollout Strategy, Lifecycle (H07 pass)
- default_state: off (valid enum) (H08 pass)
- rollout_percentage: 0 (integer 0-100) (H09 pass)
- category: release (valid enum) (H10 pass)
- tldr: 74 chars <= 160 (S01 pass)
- tags: 5 items, includes "feature_flag" (S02 pass)
## Anti-Example
INPUT: "Add a feature flag for dark mode"
BAD OUTPUT:
```yaml
id: dark-mode
kind: flag
pillar: config
flag_name: Dark Mode Toggle
default_state: maybe
rollout_percentage: half
quality: 9.0
tags: [ui]
```
Turn on dark mode for users.
FAILURES:
1. id: "dark-mode" uses hyphens, no `p09_ff_` prefix -> H02 FAIL
2. kind: "flag" not "feature_flag" -> H04 FAIL
3. pillar: "config" not "P09" -> H06 FAIL
4. default_state: "maybe" not in enum [on, off] -> H08 FAIL
5. rollout_percentage: "half" not integer 0-100 -> H09 FAIL
6. quality: 9.0 (not null) -> H05 FAIL
7. Missing fields: version, created, updated, author, category, tldr -> H06 FAIL
8. tags: only 1 item, missing "feature_flag" -> S02 FAIL
9. Body missing ## Flag Specification, ## Rollout Strategy, ## Lifecycle -> H07 FAIL
10. flag_name uses spaces and uppercase (should be snake_case slug) -> S04 FAIL
11. No rollout strategy or lifecycle plan defined -> S05 FAIL

### bld_config_feature_flag.md
---
kind: config
id: bld_config_feature_flag
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: feature_flag Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p09_ff_{feature_slug}.yaml` | `p09_ff_enable_vector_search.yaml` |
| Builder directory | kebab-case | `feature-flag-builder/` |
| Frontmatter fields | snake_case | `flag_name`, `default_state` |
| Feature slug | snake_case, lowercase, no hyphens | `enable_dark_mode`, `use_new_api` |
| Flag names | snake_case, verb prefix | `enable_*`, `use_*`, `show_*`, `allow_*` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P09_config/examples/p09_ff_{feature_slug}.yaml`
- Compiled: `cex/P09_config/compiled/p09_ff_{feature_slug}.json`
## Size Limits (aligned with SCHEMA)
- Body: max 1536 bytes (tightest P09 kind)
- Total (frontmatter + body): ~2500 bytes
- Density: >= 0.80 (no filler — every word counts at 1536)
## Category Reference
| Category | Default State | Lifecycle | Example |
|----------|--------------|-----------|---------|
| release | off | deploy -> ramp -> full -> retire | enable_vector_search |
| experiment | off | deploy -> measure -> decide -> retire | use_new_checkout_flow |
| ops | on | always on, OFF = emergency kill | enable_rate_limiting |
| permission | off | on for entitled users only | allow_premium_export |
## Flag Naming Conventions
| Prefix | Meaning | Example |
|--------|---------|---------|
| enable_ | Activate a feature | enable_dark_mode |
| use_ | Switch implementation | use_new_search |
| show_ | UI visibility toggle | show_beta_banner |
| allow_ | Permission-like toggle | allow_bulk_export |

### bld_output_template_feature_flag.md
---
kind: output_template
id: bld_output_template_feature_flag
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a feature_flag artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: feature_flag
```yaml
id: p09_ff_{{feature_slug}}
kind: feature_flag
pillar: P09
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
flag_name: "{{human_readable_flag_name}}"
default_state: {{on|off}}
category: {{release|experiment|ops|permission}}
rollout_percentage: {{0_to_100}}
quality: null
tags: [feature_flag, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_flag_controls_max_200ch}}"
owner: "{{responsible_team_or_person}}"
expires: "{{YYYY-MM-DD_or_null}}"
targeting: "{{targeting_strategy_summary}}"
```
## Flag Specification
{{feature_description_and_current_state}}
{{kill_switch_behavior_if_ops}}
## Rollout Strategy
{{rollout_stages_with_percentages_and_timeline}}
## Lifecycle
{{lifecycle_stages_create_test_ramp_full_retire}}
## References
- {{reference_1}}
```

### bld_architecture_feature_flag.md
---
kind: architecture
id: bld_architecture_feature_flag
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of feature_flag — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| flag_id | Unique identifier for the flag; used by consumers to query state | feature_flag | required |
| flag_state | Default on/off value when no targeting rule matches | feature_flag | required |
| flag_category | Classification: release, experiment, ops, or permission | feature_flag | required |
| rollout_strategy | How the flag activates: instant, percentage-based, or cohort-based | feature_flag | required |
| rollout_percentage | Fraction of traffic (0–100%) receiving the enabled state | feature_flag | conditional |
| targeting_rules | Conditions (user cohort, environment, region) that override default state | feature_flag | optional |
| kill_switch | Emergency override that forces flag off regardless of rollout state | feature_flag | required |
| fallback_default | Value returned when evaluation fails or flag is undefined | feature_flag | required |
| evaluation_context | Runtime data (user ID, env, request metadata) used by targeting rules | feature_flag | required |
## Dependency Graph
```
feature_flag --depends-->  guardrail (P11)
feature_flag --produces--> agent (P02)
feature_flag --produces--> router (P02)
feature_flag --produces--> skill (P04)
kill_switch   --signals-->  feature_flag
targeting_rules --depends--> evaluation_context
```
| From | To | Type | Data |
|------|----|------|------|
| guardrail (P11) | feature_flag | depends | safety rules constraining flag behavior and kill-switch policy |
| feature_flag | agent (P02) | produces | on/off decision consumed before feature execution |
| feature_flag | router (P02) | produces | A/B routing decision based on flag state |
| feature_flag | skill (P04) | produces | optional phase enablement within skill execution |
| kill_switch | feature_flag | signals | emergency-off override forces disabled state |
| evaluation_context | targeting_rules | data_flow | runtime metadata used to resolve cohort and percentage rules |
## Boundary Table
| feature_flag IS | feature_flag IS NOT |
|-----------------|---------------------|
| A logical on/off toggle for a named feature | A generic configuration variable (that is env_config) |
| Evaluated at runtime per request or per user | A static value read once at startup |
| Owner of rollout strategies (percentage, cohort, instant) | An access-control rule determining who can use a resource |
| Capable of gradual canary rollout (1% → 10% → 100%) | A filesystem path or infrastructure variable |
| Equipped with a kill switch for emergency disable | A timeout or retry rule governing technical behavior |
| Classified by category: release, experiment, ops, permission | A permission artifact controlling read/write access |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| Identity | flag_id, flag_category | Name and classify the flag for discovery and routing |
| State | flag_state, fallback_default | Define default behavior when no targeting rule applies |
| Rollout | rollout_strategy, rollout_percentage, targeting_rules | Control progressive activation across traffic segments |
| Context | evaluation_context | Supply runtime data for targeting rule evaluation |
| Safety | kill_switch, guardrail (P11) | Enable emergency override and constrain flag behavior |
| Consumers | agent (P02), router (P02), skill (P04) | Receive and act on the evaluated flag decision |

### bld_collaboration_feature_flag.md
---
kind: collaboration
id: bld_collaboration_feature_flag
pillar: P12
llm_function: COLLABORATE
purpose: How feature-flag-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: feature-flag-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "should this feature be on or off, for whom, and with what rollout strategy?"
I do not set environment variables. I do not control access permissions.
I specify feature toggles so teams can control rollout, experiments, and kill switches.
## Crew Compositions
### Crew: "Deployment Configuration"
```
  1. boot-config-builder -> "provider startup configuration"
  2. env-config-builder -> "environment variables"
  3. feature-flag-builder -> "feature toggles (on/off, rollout %, cohorts)"
```
### Crew: "Gradual Rollout"
```
  1. feature-flag-builder -> "flag definition with rollout strategy"
  2. benchmark-builder -> "performance impact measurement per cohort"
  3. bugloop-builder -> "auto-rollback if metrics degrade"
```
## Handoff Protocol
### I Receive
- seeds: feature name, flag category (release, experiment, ops, permission)
- optional: rollout percentage, cohort targeting, kill switch config, expiry date
### I Produce
- feature_flag artifact (.md + .yaml frontmatter)
- committed to: `cex/P09/examples/p09_flag_{feature}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0). Flags are defined from product requirements.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| env-config-builder | May reference flags as environment overrides |
| bugloop-builder | Uses flag state as detection trigger for rollback |
| benchmark-builder | Measures performance per flag cohort |

### bld_memory_feature_flag.md
---
id: p10_lr_feature_flag_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: edison
observation: "Feature flags without expiration dates accumulate as permanent tech debt — stale flags found in codebases after 18+ months. rollout_percentage as string '50%' fails schema validation; must be integer 0-100. category field confused with 'feature' or 'toggle' (invalid) instead of the four valid values: release, experiment, ops, permission. Kill switch documentation absent from ops flags causes outage risk — no one knows how to disable a live feature under incident. Lifecycle section omitted means no retirement plan, flags never get removed."
pattern: "Every feature flag requires: default_state (on/off only), rollout_percentage (integer 0-100), category (release/experiment/ops/permission), expires date, kill_switch procedure, and a ## Lifecycle section. Ops flags default to on and need emergency disable documented. Release and experiment flags default to off and expire in 2-6 weeks. Permission flags are permanent but need documented revocation path. Never use flag to represent WHO has access — that is a permission artifact."
evidence: "9 feature flag artifacts validated. 100% of flags missing expires field had no documented retirement path. Ops flags without kill_switch documentation were implicated in 2 incident post-mortems. rollout_percentage string vs integer caused 4 schema rejections in early production runs."
confidence: 0.75
outcome: SUCCESS
domain: feature_flag
tags: [feature_flag, rollout, kill_switch, gradual_rollout, lifecycle, ops_safety]
tldr: "Set expires on every flag; document kill_switch for ops flags; rollout_percentage is integer not string."
impact_score: 7.5
decay_rate: 0.04
satellite: edison
keywords: [feature_flag, rollout_percentage, kill_switch, default_state, category, expires, lifecycle, gradual_rollout]
---

## Summary
Feature flags enable gradual rollout and emergency disable without code deployment. The builder must enforce four category types, integer rollout percentages, expiration dates, and kill switch documentation or flags become permanent liabilities that no one knows how to safely disable.
## Pattern
1. `default_state` accepts only `"on"` or `"off"` — no intermediate values.
2. `rollout_percentage` is an integer 0-100 with no percent symbol.
3. `category` is one of four values: `release` (new feature), `experiment` (A/B test), `ops` (operational toggle), `permission` (access control).
4. Every flag has an `expires` date. Release and experiment flags expire in 2-6 weeks. Ops and permission flags set expires to a review date, not infinity.
5. Ops flags default to `on` and must document a kill switch procedure — the exact steps to disable under incident conditions.
6. Every artifact includes a `## Lifecycle` section: how the flag is created, monitored, and retired.
7. Targeting rules (user segment, region, percentage) live in the targeting block, not in the flag description.
## Anti-Pattern
- `default_state: "maybe"` or `"partial"` — only `"on"` or `"off"` are valid.
- `rollout_percentage: "50%"` — string with percent symbol fails schema.
- `category: "feature"` or `"toggle"` — these are not valid category values.
- Omitting `expires` creates permanent flags with no retirement plan.
- Omitting kill switch for ops flags means no runbook during incidents.
- Using a feature flag to represent WHO has access — that is a permission artifact, not a flag.
- Body exceeding 1536 bytes — P09 has the tightest size limit; every word must earn its place.
## Context
Applies when: shipping a new feature behind a gate, running an A/B experiment, adding an emergency ops toggle, or restricting access to a capability.
Does not apply when: the decision is permanent and binary with no rollout phase needed.
Boundary: feature_flag controls whether a feature exists; permission controls who can use it. Do not conflate.
Category decision: if the flag will exist beyond 6 weeks permanently, evaluate whether it should be a permission instead.


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `feature-flag-builder` for pipeline function `CONSTRAIN`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
