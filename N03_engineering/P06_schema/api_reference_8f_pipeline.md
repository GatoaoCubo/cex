---
id: p06_ar_8f_pipeline
kind: api_reference
8f: F5_call
pillar: P06
title: "API Reference -- 8F Pipeline"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: artifact-construction
quality: 9.1
tags: [api-reference, 8F, pipeline, N03, build, reasoning-protocol]
tldr: "Machine-readable API reference for the 8F Universal Reasoning Pipeline. Each function documented as a callable interface: inputs, outputs, preconditions, postconditions, error handling, and inter-function contracts."
density_score: 0.94
updated: "2026-04-17"
related:
  - bld_schema_prompt_compiler
  - bld_schema_model_registry
  - bld_schema_kind
  - bld_schema_dataset_card
  - bld_schema_usage_report
  - p06_is_creation_data
  - bld_schema_sandbox_config
  - bld_schema_thinking_config
  - bld_schema_input_schema
  - bld_schema_reranker_config
---

# API Reference: 8F Pipeline

## Overview

The 8F pipeline is CEX's universal reasoning protocol. Every nucleus, every task, every artifact
flows through F1->F8 in sequence. This document is the MACHINE-READABLE reference for
builders that need to introspect, instrument, or extend the pipeline.

**Protocol source of truth:** `.claude/rules/8f-reasoning.md`
**Python implementation:** `cex_sdk/cex_8f_runner.py`
**Motor (intent -> plan):** `cex_sdk/cex_8f_motor.py`

---

## F1: CONSTRAIN

**Purpose:** Resolve kind, pillar, schema constraints. Sets the contract for the entire pipeline run.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| intent | string | yes (or kind) | Natural language input |
| kind | string | no | Explicit kind override |
| kinds_meta_path | path | no | default: .cex/kinds_meta.json |

**Returns:**
```yaml
kind: string          # resolved canonical kind
pillar: string        # canonical pillar (P01-P12)
max_bytes: integer    # body byte ceiling for this kind
naming_pattern: string # filename regex
schema_path: string   # path to kind's validation schema
```

**Errors:** `KindResolutionError` if intent cannot be mapped to a kind with confidence >= 0.6

---

## F2: BECOME

**Purpose:** Load builder identity. Transforms the agent into the builder for the resolved kind.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| kind | string | yes | Output of F1 |
| builder_base | path | no | default: archetypes/builders/ |
| required_isos | integer | no | default: 13 |

**Returns:**
```yaml
builder_id: string        # "{kind}-builder"
isos_loaded: integer      # count of ISOs successfully loaded
system_prompt: string     # builder's identity/instructions
sin_lens: string          # cultural optimization filter
```

**Precondition:** F1 must complete with status=success  
**Errors:** `BuilderNotFoundError` if `{kind}-builder/` does not exist; `ISOCountError` if loaded < 13

---

## F2b: SPEAK (sub-step)

**Purpose:** Load controlled vocabulary KC. Ensures all downstream output uses canonical terms.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| nucleus | string | yes | Executing nucleus ID |
| vocab_path | path | no | default: N0X/P01/kc_{domain}_vocabulary.md |

**Returns:**
```yaml
terms_loaded: integer       # vocabulary term count
anti_patterns_loaded: integer
prompt_compiler_loaded: boolean  # N00_genesis/P03_prompt/layers/p03_pc_cex_universal.md
```

---

## F3: INJECT

**Purpose:** Assemble knowledge context for the build: KCs, examples, brand, memory, similar artifacts.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| kind | string | yes | Resolved kind |
| domain | string | no | Domain for KC selection |
| brand_config | path | no | .cex/brand/brand_config.yaml |
| memory_path | path | no | .claude/projects/.../memory/ |
| example_count | integer | no | default: 3 |

**Returns:**
```yaml
sources_injected: integer
kc_path: string             # primary KC path
examples: string[]          # example artifact paths
template_match_score: float # similarity to best template (0.0-1.0)
brand_injected: boolean
memory_items: integer
```

---

## F4: REASON

**Purpose:** Plan the artifact: sections, approach (template/hybrid/fresh), estimated density.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| f1_output | F1Result | yes | Constraints from F1 |
| f3_output | F3Result | yes | Context from F3 |
| quality_target | float | no | default: 9.0 |

**Returns:**
```yaml
sections: string[]           # planned H2 sections
approach: string             # "template" | "hybrid" | "fresh"
estimated_density: float     # predicted density_score
construction_triad: string   # template/hybrid/fresh selection rationale
gdp_required: boolean        # true if subjective decisions needed
```

**Construction Triad Logic:**

| Condition | Approach |
|-----------|---------|
| template_match_score >= 0.60 | template (adapt from match) |
| template_match_score in [0.30, 0.60) | hybrid (combine elements) |
| template_match_score < 0.30 | fresh (build from scratch) |

---

## F5: CALL

**Purpose:** Execute tools needed for enrichment: compiler check, retriever, doctor, sub-agents.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| tools | string[] | no | Tool list from builder ISO |
| similar_scan | boolean | no | default: true |

**Returns:**
```yaml
tools_ready: string[]        # confirmed available tools
similar_artifacts: integer   # artifacts found by retriever
pre_conditions_met: boolean  # all required tools accessible
```

---

## F6: PRODUCE

**Purpose:** Generate the complete artifact with frontmatter + body following builder instructions.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| f1_output | F1Result | yes | Kind + pillar + constraints |
| f2_output | F2Result | yes | Builder identity + ISOs |
| f3_output | F3Result | yes | Context sources |
| f4_output | F4Result | yes | Plan + approach |
| quality_target | float | no | default: 9.0 |

**Returns:**
```yaml
artifact_content: string     # complete artifact text (frontmatter + body)
bytes: integer               # artifact byte count
sections: integer            # H2 section count
density: float               # actual density_score
```

**Retry:** if F7 fails, caller may invoke F6 again (max 2 retries) with failure feedback injected.

---

## F7: GOVERN

**Purpose:** Validate artifact against 7 hard gates + 12LP checklist + 5D scoring.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| artifact_content | string | yes | Output of F6 |
| kind | string | yes | Expected kind |
| quality_target | float | no | default: 9.0 |
| retry_count | integer | no | Current retry number (0-2) |

**Returns:**
```yaml
score: float                 # 0.0-10.0 (never self-assigned to artifact)
gates_pass: integer          # hard gates passed (of 7)
gates_total: integer         # 7
lp_pass: integer             # 12LP items passed
lp_total: integer            # 12
status: string               # "pass" | "warn" | "fail"
failures: string[]           # list of failed gate IDs
```

**Hard Gates (H01-H07):**

| Gate | Check |
|------|-------|
| H01 | Frontmatter YAML valid |
| H02 | id matches kind naming pattern |
| H03 | kind exists in kinds_meta.json |
| H04 | quality: null (not self-scored) |
| H05 | Body >= 512 bytes |
| H06 | density_score >= 0.80 |
| H07 | No placeholder text remaining |

---

## F8: COLLABORATE

**Purpose:** Save artifact, compile to YAML, commit to git, send signal.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| artifact_content | string | yes | Validated artifact from F7 |
| output_path | string | yes | Target file path |
| compile | boolean | no | default: true |
| commit | boolean | no | default: true |
| signal | boolean | no | default: true |
| nucleus | string | yes | Sending nucleus ID |
| score | float | yes | F7 score (for signal) |

**Returns:**
```yaml
saved_path: string           # written file path
compiled: boolean            # cex_compile.py success
committed: boolean           # git commit success
signal_sent: boolean         # signal_writer success
commit_hash: string | null   # git commit hash
```

**Signal format:** `{nucleus} -> complete {score}` written to `.cex/runtime/signals/`

---

## Pipeline State Machine

```
[START]
  -> F1 CONSTRAIN -> kind resolved
  -> F2 BECOME    -> builder loaded
  -> F2b SPEAK    -> vocabulary loaded
  -> F3 INJECT    -> context assembled
  -> F4 REASON    -> plan + approach
  -> F5 CALL      -> tools ready
  -> F6 PRODUCE   -> artifact draft
  -> F7 GOVERN    -> validation
       |
       |-- pass -> F8 COLLABORATE -> [COMPLETE]
       |-- fail (retry_count < 2) -> F6 PRODUCE (retry)
       `-- fail (retry_count >= 2) -> [REJECT]
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_prompt_compiler]] | related | 0.40 |
| [[bld_schema_model_registry]] | related | 0.39 |
| [[bld_schema_kind]] | related | 0.39 |
| [[bld_schema_dataset_card]] | related | 0.38 |
| [[bld_schema_usage_report]] | related | 0.38 |
| [[p06_is_creation_data]] | related | 0.37 |
| [[bld_schema_sandbox_config]] | related | 0.37 |
| [[bld_schema_thinking_config]] | related | 0.37 |
| [[bld_schema_input_schema]] | related | 0.36 |
| [[bld_schema_reranker_config]] | related | 0.36 |
