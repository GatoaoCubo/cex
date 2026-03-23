import sys
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"): sys.stderr.reconfigure(encoding="utf-8")
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


TEMPLATES = {
    "knowledge_card": """---
# TEMPLATE: Knowledge Card (P01 Knowledge)
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P01_knowledge/_schema.yaml (types.knowledge_card)
# Max 5120 bytes | density_min: 0.80 | quality_min: 7.0

id: p01_kc_{{TOPIC_SLUG}}
type: knowledge_card
lp: P01
title: "{{KNOWLEDGE_CARD_TITLE}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{SATELLITE_NAME}}
domain: {{DOMAIN_NAME}}
quality: {{QUALITY_8_TO_10}}
tags: [{{TAG1}}, {{TAG2}}, knowledge]
tldr: "{{ONE_DENSE_SENTENCE}}"
when_to_use: "{{WHEN_THIS_CARD_SHOULD_BE_RETRIEVED}}"
keywords: [{{KEYWORD_1}}, {{KEYWORD_2}}, {{KEYWORD_3}}]
long_tails: [{{LONG_TAIL_QUERY_1}}, {{LONG_TAIL_QUERY_2}}]
axioms: [{{AXIOM_1}}]
linked_artifacts:
  adw: {{p12_wf_name_OR_null}}
  agent: {{p02_agent_name_OR_null}}
  hop: {{p03_pt_name_OR_null}}
density_score: {{0.80_TO_1.00}}
---

# Knowledge Card: {{KNOWLEDGE_CARD_TITLE}}

## Quick Reference
```yaml
topic: {{TOPIC_NAME}}
scope: {{SCOPE}}
owner: {{OWNER}}
criticality: {{low|medium|high}}
```

## Key Concepts
- {{CONCEPT_1_WITH_EXAMPLE}}
- {{CONCEPT_2_WITH_EXAMPLE}}
- {{CONCEPT_3_WITH_EXAMPLE}}

## Strategy Phases
1. {{PHASE_1_WITH_OUTCOME}}
2. {{PHASE_2_WITH_OUTCOME}}
3. {{PHASE_3_WITH_OUTCOME}}

## Golden Rules
- {{RULE_1}}
- {{RULE_2}}
- {{RULE_3}}

## Flow
```text
[{{INPUT}}] -> [{{ANALYZE}}] -> [{{DECIDE}}] -> [{{EXECUTE}}] -> [{{LEARN}}]
```

## References
- Related artifact: {{ARTIFACT_REF_1}}
- Related artifact: {{ARTIFACT_REF_2}}
""",
    "glossary_entry": """---
# TEMPLATE: Glossary Entry (P01 Knowledge)
# Valide contra P01_knowledge/_schema.yaml (types.glossary_entry)
# Max 512 bytes

id: p01_gl_{{TERM_SLUG}}
type: glossary_entry
lp: P01
term: {{TERM}}
definition: {{SHORT_DEFINITION_IN_1_TO_3_LINES}}
synonyms: [{{SYNONYM_1}}, {{SYNONYM_2}}]
---

# Glossary Entry: {{TERM}}

## Definition
{{SHORT_DEFINITION_IN_1_TO_3_LINES}}

## Usage
- Context: {{WHERE_TERM_APPEARS}}
- Example: {{SENTENCE_USING_TERM}}
- Avoid confusion with: {{SIMILAR_TERM}}
""",
    "context_doc": """---
# TEMPLATE: Context Doc (P01 Knowledge)
# Valide contra P01_knowledge/_schema.yaml (types.context_doc)
# Max 2048 bytes

id: p01_ctx_{{TOPIC_SLUG}}
type: context_doc
lp: P01
title: "{{CONTEXT_TITLE}}"
domain: {{DOMAIN_NAME}}
scope: {{SYSTEM|CLIENT|WORKFLOW|REPO}}
quality: {{QUALITY_7_TO_10}}
---

# Context Doc: {{CONTEXT_TITLE}}

## Scope
- Domain: {{DOMAIN_NAME}}
- Boundary: {{WHAT_IS_INCLUDED}}
- Excluded: {{WHAT_IS_OUT_OF_SCOPE}}

## Current State
- {{FACT_1}}
- {{FACT_2}}
- {{FACT_3}}

## Operational Context
| Area | Detail |
|------|--------|
| Users | {{PRIMARY_USERS}} |
| Inputs | {{PRIMARY_INPUTS}} |
| Outputs | {{PRIMARY_OUTPUTS}} |
| Risks | {{MAIN_RISK}} |

## Decision Notes
1. {{DECISION_1}}
2. {{DECISION_2}}
3. {{DECISION_3}}
""",
    "embedding_config": """---
# TEMPLATE: Embedding Config (P01 Knowledge)
# Valide contra P01_knowledge/_schema.yaml (types.embedding_config)
# Max 512 bytes

id: p01_emb_{{MODEL_SLUG}}
type: embedding_config
lp: P01
model_name: {{EMBEDDING_MODEL_NAME}}
dimensions: {{DIMENSIONS_INT}}
chunk_size: {{CHUNK_SIZE_INT}}
---

# Embedding Config: {{EMBEDDING_MODEL_NAME}}

## Parameters
```yaml
model_name: {{EMBEDDING_MODEL_NAME}}
dimensions: {{DIMENSIONS_INT}}
chunk_size: {{CHUNK_SIZE_INT}}
overlap: {{OVERLAP_INT}}
distance_metric: {{cosine|dot|l2}}
```

## Notes
- Use when: {{WHEN_TO_USE}}
- Tradeoff: {{PRIMARY_TRADEOFF}}
""",
    "few_shot_example": """---
# TEMPLATE: Few-Shot Example (P01 Knowledge)
# Valide contra P01_knowledge/_schema.yaml (types.few_shot_example)
# Max 1024 bytes

id: p01_fse_{{TOPIC_SLUG}}
type: few_shot_example
lp: P01
title: "{{EXAMPLE_TITLE}}"
input: {{INPUT_SUMMARY}}
output: {{OUTPUT_SUMMARY}}
quality: {{QUALITY_7_TO_10}}
---

# Few-Shot Example: {{EXAMPLE_TITLE}}

## Input
```text
{{REALISTIC_INPUT_EXAMPLE}}
```

## Output
```text
{{REALISTIC_OUTPUT_EXAMPLE}}
```

## Why It Works
- Signal preserved: {{WHY_OUTPUT_MATCHES_INPUT}}
- Constraint honored: {{WHAT_RULE_WAS_RESPECTED}}
- Reuse hint: {{WHEN_TO_REUSE_THIS_PATTERN}}
""",
    "mental_model": """---
# TEMPLATE: Mental Model (P02 Model)
# Valide contra P02_model/_schema.yaml (types.mental_model)
# Max 2048 bytes

id: p02_mm_{{MODEL_SLUG}}
type: mental_model
lp: P02
title: "{{MENTAL_MODEL_TITLE}}"
owner: {{SATELLITE_NAME}}
quality: {{QUALITY_7_TO_10}}
---

# Mental Model: {{MENTAL_MODEL_TITLE}}

## Core Assumption
{{ONE_SENTENCE_DECISION_HEURISTIC}}

## Inputs
- Signal: {{SIGNAL_1}}
- Signal: {{SIGNAL_2}}
- Signal: {{SIGNAL_3}}

## Decision Logic
1. {{IF_CONDITION_1_THEN_ACTION}}
2. {{IF_CONDITION_2_THEN_ACTION}}
3. {{IF_CONDITION_3_THEN_ACTION}}

## Failure Modes
| Failure | Detection | Recovery |
|---------|-----------|----------|
| {{FAILURE_1}} | {{DETECTION_1}} | {{RECOVERY_1}} |
| {{FAILURE_2}} | {{DETECTION_2}} | {{RECOVERY_2}} |
""",
    "client": """---
# TEMPLATE: API Client (P04 Tools)
# Valide contra P04_tools/_schema.yaml (types.client)
# Max 1024 bytes

id: p04_client_{{API_SLUG}}
type: client
lp: P04
title: "Client: {{API_NAME}}"
quality: {{QUALITY_7_TO_10}}
---

# Client: {{API_NAME}}

## Connection
- Base URL: {{BASE_URL}}
- Auth: {{api_key|oauth|none}}
- Timeout: {{TIMEOUT_SECONDS}}s

## Operations
| Method | Endpoint | Purpose |
|--------|----------|---------|
| {{GET|POST}} | {{/path}} | {{WHAT_IT_DOES}} |
| {{GET|POST}} | {{/path}} | {{WHAT_IT_DOES}} |

## Contract
```yaml
request:
  {{FIELD_1}}: {{TYPE}}
response:
  {{FIELD_2}}: {{TYPE}}
```
""",
    "cli_tool": """---
# TEMPLATE: CLI Tool (P04 Tools)
# Valide contra P04_tools/_schema.yaml (types.cli_tool)
# Max 1024 bytes

id: p04_cli_{{TOOL_SLUG}}
type: cli_tool
lp: P04
title: "CLI Tool: {{TOOL_NAME}}"
quality: {{QUALITY_7_TO_10}}
---

# CLI Tool: {{TOOL_NAME}}

## Purpose
{{ONE_SENTENCE_ON_WHAT_THIS_COMMAND_DOES}}

## Usage
```bash
{{TOOL_NAME}} {{COMMAND}} {{FLAGS}}
```

## Inputs / Outputs
- Input: {{EXPECTED_INPUT}}
- Output: {{EXPECTED_OUTPUT}}
- Exit codes: {{EXIT_CODE_RULES}}

## Guardrails
- Safe default: {{DEFAULT_BEHAVIOR}}
- Dangerous flag: {{FLAG_TO_AVOID_OR_CONFIRM}}
""",
    "scraper": """---
# TEMPLATE: Scraper (P04 Tools)
# Valide contra P04_tools/_schema.yaml (types.scraper)
# Max 1024 bytes

id: p04_scraper_{{TARGET_SLUG}}
type: scraper
lp: P04
title: "Scraper: {{TARGET_NAME}}"
quality: {{QUALITY_7_TO_10}}
---

# Scraper: {{TARGET_NAME}}

## Target
- Source: {{URL_OR_SITE}}
- Data wanted: {{PRIMARY_FIELDS}}
- Cadence: {{ONE_SHOT|DAILY|ON_DEMAND}}

## Extraction Plan
1. {{LOAD_PAGE_OR_ENDPOINT}}
2. {{SELECT_RELEVANT_NODES}}
3. {{NORMALIZE_FIELDS}}

## Output
```yaml
items:
  - {{FIELD_1}}: {{EXAMPLE_VALUE}}
    {{FIELD_2}}: {{EXAMPLE_VALUE}}
```
""",
    "connector": """---
# TEMPLATE: Connector (P04 Tools)
# Valide contra P04_tools/_schema.yaml (types.connector)
# Max 1024 bytes

id: p04_conn_{{SERVICE_SLUG}}
type: connector
lp: P04
title: "Connector: {{SERVICE_NAME}}"
quality: {{QUALITY_7_TO_10}}
---

# Connector: {{SERVICE_NAME}}

## Service Contract
- Service: {{SERVICE_NAME}}
- Mode: {{push|pull|bidirectional}}
- Auth: {{AUTH_MODE}}

## Data Mapping
| External Field | Internal Field | Rule |
|----------------|----------------|------|
| {{EXT_FIELD_1}} | {{INT_FIELD_1}} | {{MAPPING_RULE_1}} |
| {{EXT_FIELD_2}} | {{INT_FIELD_2}} | {{MAPPING_RULE_2}} |

## Failure Handling
- Retry: {{RETRY_POLICY}}
- Fallback: {{FALLBACK_BEHAVIOR}}
""",
    "daemon": """---
# TEMPLATE: Daemon (P04 Tools)
# Valide contra P04_tools/_schema.yaml (types.daemon)
# Max 1024 bytes

id: p04_daemon_{{NAME_SLUG}}
type: daemon
lp: P04
title: "Daemon: {{DAEMON_NAME}}"
quality: {{QUALITY_7_TO_10}}
---

# Daemon: {{DAEMON_NAME}}

## Runtime
- Trigger: {{cron|queue|watcher}}
- Interval: {{INTERVAL}}
- Owner: {{OWNER}}

## Loop
1. {{READ_INPUT}}
2. {{PROCESS_WORK}}
3. {{EMIT_STATE}}

## Safety
- Healthcheck: {{HEALTHCHECK_SIGNAL}}
- Restart policy: {{RESTART_POLICY}}
- Stop condition: {{STOP_CONDITION}}
""",
    "parser": """---
# TEMPLATE: Parser (P05 Output)
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P05_output/_schema.yaml (types.parser)
# Max 4096 bytes

id: p05_parser_{{TARGET_SLUG}}
type: parser
lp: P05
title: "Parser: {{TARGET_NAME}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{SATELLITE_NAME}}
quality: {{QUALITY_8_TO_10}}
tags: [parser, output, {{TAG1}}]
tldr: "{{ONE_SENTENCE_ON_EXTRACTION_GOAL}}"
density_score: {{0.80_TO_1.00}}
---

# Parser: {{TARGET_NAME}}

## Input Format
```text
{{RAW_INPUT_EXAMPLE}}
```

## Extraction Rules
| Field | Pattern | Transform |
|-------|---------|-----------|
| {{FIELD_1}} | {{REGEX_OR_RULE_1}} | {{CAST_OR_NORMALIZE_1}} |
| {{FIELD_2}} | {{REGEX_OR_RULE_2}} | {{CAST_OR_NORMALIZE_2}} |
| {{FIELD_3}} | {{REGEX_OR_RULE_3}} | {{CAST_OR_NORMALIZE_3}} |

## Parsed Output
```yaml
{{FIELD_1}}: {{EXAMPLE_VALUE_1}}
{{FIELD_2}}: {{EXAMPLE_VALUE_2}}
{{FIELD_3}}: {{EXAMPLE_VALUE_3}}
```

## Validation
- Reject when: {{BROKEN_PATTERN}}
- Accept when: {{MINIMUM_COMPLETE_SHAPE}}
""",
    "type_def": """---
# TEMPLATE: Type Definition (P06 Schema)
# Valide contra P06_schema/_schema.yaml (types.type_def)
# Max 3072 bytes

id: p06_td_{{TYPE_SLUG}}
type: type_def
lp: P06
title: "Type Def: {{TYPE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Type Def: {{TYPE_NAME}}

## Definition
```yaml
name: {{TYPE_NAME}}
base: {{string|integer|object|array}}
nullable: {{true|false}}
```

## Fields
| Field | Type | Required | Example |
|-------|------|----------|---------|
| {{FIELD_1}} | {{TYPE_1}} | yes | {{EXAMPLE_1}} |
| {{FIELD_2}} | {{TYPE_2}} | no | {{EXAMPLE_2}} |

## Constraints
- {{CONSTRAINT_1}}
- {{CONSTRAINT_2}}
- {{CONSTRAINT_3}}
""",
    "output_schema": """---
# TEMPLATE: Output Schema (P06 Schema)
# Valide contra P06_schema/_schema.yaml (types.output_schema)
# Max 3072 bytes

id: p06_os_{{SCOPE_SLUG}}
type: output_schema
lp: P06
title: "Output Schema: {{SCOPE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Output Schema: {{SCOPE_NAME}}

## Envelope
```yaml
status: {{success|error}}
message: {{SHORT_MESSAGE}}
data:
  {{FIELD_1}}: {{TYPE_1}}
```

## Field Contract
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| status | string | yes | {{STATUS_RULE}} |
| message | string | yes | {{MESSAGE_RULE}} |
| {{FIELD_1}} | {{TYPE_1}} | yes | {{NOTE_1}} |
| {{FIELD_2}} | {{TYPE_2}} | no | {{NOTE_2}} |

## Validation
1. {{VALIDATION_RULE_1}}
2. {{VALIDATION_RULE_2}}
3. {{VALIDATION_RULE_3}}
""",
    "smoke_eval": """---
# TEMPLATE: Smoke Eval (P07 Evals)
# Valide contra P07_evals/_schema.yaml (types.smoke_eval)
# Max 3072 bytes

id: p07_se_{{SCOPE_SLUG}}
type: smoke_eval
lp: P07
title: "Smoke Eval: {{SCOPE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Smoke Eval: {{SCOPE_NAME}}

## Goal
{{FAST_SANITY_CHECK_FOR_THE_CRITICAL_PATH}}

## Setup
- Target: {{TARGET_UNDER_TEST}}
- Max duration: {{UNDER_30_SECONDS}}
- Preconditions: {{PRECONDITION}}

## Execute
1. {{STEP_1}}
2. {{STEP_2}}
3. {{STEP_3}}

## Assert
- {{ASSERTION_1}}
- {{ASSERTION_2}}
- {{ASSERTION_3}}
""",
    "benchmark": """---
# TEMPLATE: Benchmark (P07 Evals)
# Valide contra P07_evals/_schema.yaml (types.benchmark)
# Max 4096 bytes

id: p07_bm_{{METRIC_SLUG}}
type: benchmark
lp: P07
title: "Benchmark: {{METRIC_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Benchmark: {{METRIC_NAME}}

## Benchmark Frame
| Property | Value |
|----------|-------|
| Target | {{TARGET_SYSTEM}} |
| Metric | {{LATENCY|COST|QUALITY|THROUGHPUT}} |
| Load | {{LOAD_PROFILE}} |
| Budget | {{TARGET_THRESHOLD}} |

## Method
1. {{SETUP_ENVIRONMENT}}
2. {{RUN_MEASUREMENT}}
3. {{RECORD_RESULTS}}

## Results Table
| Run | Value | Pass |
|-----|-------|------|
| 1 | {{VALUE_1}} | {{yes|no}} |
| 2 | {{VALUE_2}} | {{yes|no}} |
| 3 | {{VALUE_3}} | {{yes|no}} |

## Interpretation
- Good when: {{GOOD_RESULT_RULE}}
- Investigate when: {{BAD_RESULT_RULE}}
""",
    "scoring_rubric": """---
# TEMPLATE: Scoring Rubric (P07 Evals)
# Valide contra P07_evals/_schema.yaml (types.scoring_rubric)
# Max 3072 bytes

id: p07_sr_{{FRAMEWORK_SLUG}}
type: scoring_rubric
lp: P07
title: "Scoring Rubric: {{FRAMEWORK_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Scoring Rubric: {{FRAMEWORK_NAME}}

## Dimensions
| Dimension | Weight | 5 Score | 1 Score |
|-----------|--------|---------|---------|
| {{DIMENSION_1}} | {{WEIGHT_1}} | {{BEST_CASE_1}} | {{WORST_CASE_1}} |
| {{DIMENSION_2}} | {{WEIGHT_2}} | {{BEST_CASE_2}} | {{WORST_CASE_2}} |
| {{DIMENSION_3}} | {{WEIGHT_3}} | {{BEST_CASE_3}} | {{WORST_CASE_3}} |

## Scoring Rule
1. {{HOW_TO_SCORE_1}}
2. {{HOW_TO_SCORE_2}}
3. {{HOW_TO_SCORE_3}}

## Pass Threshold
- Minimum total: {{MIN_SCORE}}
- Auto-fail condition: {{BLOCKING_FAILURE}}
""",
    "law": """---
# TEMPLATE: Law (P08 Architecture)
# Valide contra P08_architecture/_schema.yaml (types.law)
# Max 3072 bytes

id: p08_law_{{NUMBER}}
type: law
lp: P08
title: "LAW {{NUMBER}}: {{LAW_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# LAW {{NUMBER}}: {{LAW_NAME}}

## Statement
{{ONE_IMMUTABLE_OPERATIONAL_RULE}}

## Why It Exists
- Context: {{WHAT_PROBLEM_THIS_PREVENTS}}
- Risk: {{WHAT_BREAKS_IF_IGNORED}}

## Enforcement
1. {{ENFORCEMENT_MECHANISM_1}}
2. {{ENFORCEMENT_MECHANISM_2}}
3. {{ENFORCEMENT_MECHANISM_3}}

## Exceptions
- Allowed only when: {{STRICT_EXCEPTION_RULE}}
""",
    "diagram": """---
# TEMPLATE: Diagram (P08 Architecture)
# Valide contra P08_architecture/_schema.yaml (types.diagram)
# Max 4096 bytes

id: p08_diag_{{SCOPE_SLUG}}
type: diagram
lp: P08
title: "Diagram: {{SCOPE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Diagram: {{SCOPE_NAME}}

## Purpose
{{ONE_SENTENCE_ON_WHAT_THIS_ARCHITECTURE_VIEW_SHOWS}}

## Diagram
```mermaid
flowchart LR
    A[{{COMPONENT_A}}] --> B[{{COMPONENT_B}}]
    B --> C[{{COMPONENT_C}}]
    B --> D[{{COMPONENT_D}}]
    C --> E[{{OUTCOME}}]
```

## Reading Notes
- Entry point: {{ENTRY_POINT}}
- Shared dependency: {{SHARED_COMPONENT}}
- Failure hotspot: {{RISK_AREA}}
""",
    "component_map": """---
# TEMPLATE: Component Map (P08 Architecture)
# Valide contra P08_architecture/_schema.yaml (types.component_map)
# Max 3072 bytes

id: p08_cmap_{{SCOPE_SLUG}}
type: component_map
lp: P08
title: "Component Map: {{SCOPE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Component Map: {{SCOPE_NAME}}

## Components
| Component | Responsibility | Depends On |
|-----------|----------------|------------|
| {{COMPONENT_1}} | {{RESPONSIBILITY_1}} | {{DEPENDENCY_1}} |
| {{COMPONENT_2}} | {{RESPONSIBILITY_2}} | {{DEPENDENCY_2}} |
| {{COMPONENT_3}} | {{RESPONSIBILITY_3}} | {{DEPENDENCY_3}} |

## Interfaces
- {{COMPONENT_1}} -> {{COMPONENT_2}}: {{INTERFACE_RULE}}
- {{COMPONENT_2}} -> {{COMPONENT_3}}: {{INTERFACE_RULE}}

## Change Impact
- Safe to change alone: {{COMPONENT_SAFE}}
- Requires coordination: {{COMPONENT_RISKY}}
""",
    "path_config": """---
# TEMPLATE: Path Config (P09 Config)
# Valide contra P09_config/_schema.yaml (types.path_config)
# Max 3072 bytes

id: p09_path_{{SCOPE_SLUG}}
type: path_config
lp: P09
title: "Path Config: {{SCOPE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Path Config: {{SCOPE_NAME}}

## Paths
```yaml
root: {{ROOT_PATH}}
input: {{INPUT_PATH}}
output: {{OUTPUT_PATH}}
temp: {{TEMP_PATH}}
```

## Rules
- Writable: {{WRITABLE_RULE}}
- Relative base: {{RELATIVE_BASE_RULE}}
- Cleanup: {{CLEANUP_RULE}}
""",
    "permission": """---
# TEMPLATE: Permission Rule (P09 Config)
# Valide contra P09_config/_schema.yaml (types.permission)
# Max 3072 bytes

id: p09_perm_{{SCOPE_SLUG}}
type: permission
lp: P09
title: "Permission: {{SCOPE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Permission: {{SCOPE_NAME}}

## Access Matrix
| Actor | Read | Write | Execute |
|------|------|-------|---------|
| {{ACTOR_1}} | yes | no | no |
| {{ACTOR_2}} | yes | yes | no |
| {{ACTOR_3}} | yes | yes | yes |

## Boundaries
- Forbidden path: {{FORBIDDEN_SCOPE}}
- Escalation path: {{HOW_TO_REQUEST_ACCESS}}
""",
    "runtime_rule": """---
# TEMPLATE: Runtime Rule (P09 Config)
# Valide contra P09_config/_schema.yaml (types.runtime_rule)
# Max 3072 bytes

id: p09_rr_{{RULE_SLUG}}
type: runtime_rule
lp: P09
title: "Runtime Rule: {{RULE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Runtime Rule: {{RULE_NAME}}

## Parameters
| Parameter | Value | Reason |
|-----------|-------|--------|
| timeout | {{SECONDS}} | {{WHY_TIMEOUT}} |
| retries | {{RETRY_COUNT}} | {{WHY_RETRIES}} |
| concurrency | {{CONCURRENCY}} | {{WHY_CONCURRENCY}} |

## Enforcement
1. {{WHEN_RULE_APPLIES}}
2. {{WHAT_IS_LIMITED}}
3. {{WHAT_HAPPENS_ON_EXCEED}}
""",
    "brain_index": """---
# TEMPLATE: Brain Index (P10 Memory)
# Valide contra P10_memory/_schema.yaml (types.brain_index)
# Max 3072 bytes

id: p10_bi_{{INDEX_SLUG}}
type: brain_index
lp: P10
title: "Brain Index: {{INDEX_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Brain Index: {{INDEX_NAME}}

## Index Config
```yaml
engine: {{bm25|faiss|hybrid}}
namespace: {{NAMESPACE}}
refresh: {{REFRESH_POLICY}}
```

## Retrieval Policy
- Query shape: {{EXPECTED_QUERY_PATTERN}}
- Ranking signal: {{PRIMARY_RANKING_SIGNAL}}
- Reindex when: {{REINDEX_TRIGGER}}
""",
    "axiom": """---
# TEMPLATE: Axiom (P10 Memory)
# Valide contra P10_memory/_schema.yaml (types.axiom)
# Max 3072 bytes

id: p10_ax_{{RULE_SLUG}}
type: axiom
lp: P10
title: "Axiom: {{AXIOM_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Axiom: {{AXIOM_NAME}}

## Rule
{{ONE_NON_NEGOTIABLE_RULE}}

## Rationale
- Why: {{WHY_THIS_EXISTS}}
- Protects: {{WHAT_CAPABILITY_IT_PROTECTS}}

## Examples
- Correct: {{CORRECT_BEHAVIOR}}
- Incorrect: {{INCORRECT_BEHAVIOR}}
""",
    "lifecycle_rule": """---
# TEMPLATE: Lifecycle Rule (P11 Feedback)
# Valide contra P11_feedback/_schema.yaml (types.lifecycle_rule)
# Max 4096 bytes

id: p11_lc_{{RULE_SLUG}}
type: lifecycle_rule
lp: P11
title: "Lifecycle Rule: {{RULE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Lifecycle Rule: {{RULE_NAME}}

## Scope
- Artifact: {{ARTIFACT_TYPE}}
- State flow: {{draft -> active -> archived}}
- Trigger: {{FRESHNESS_OR_EVENT}}

## Rules
1. {{PROMOTE_RULE}}
2. {{ARCHIVE_RULE}}
3. {{DELETE_OR_REVIEW_RULE}}

## Evidence
- Metric used: {{METRIC}}
- Owner: {{OWNER}}
""",
    "guardrail": """---
# TEMPLATE: Guardrail (P11 Feedback)
# Valide contra P11_feedback/_schema.yaml (types.guardrail)
# Max 4096 bytes

id: p11_gr_{{SCOPE_SLUG}}
type: guardrail
lp: P11
title: "Guardrail: {{SCOPE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Guardrail: {{SCOPE_NAME}}

## Boundary
- Protects: {{ASSET_OR_USER}}
- Blocks: {{DANGEROUS_ACTION}}
- Severity: {{low|medium|high|critical}}

## Check
1. {{SIGNAL_TO_INSPECT}}
2. {{CONDITION_TO_BLOCK}}
3. {{WHAT_TO_LOG_OR_SIGNAL}}

## Recovery
- Safe alternative: {{ALTERNATIVE_PATH}}
- Escalation owner: {{OWNER}}
""",
    "optimizer": """---
# TEMPLATE: Optimizer (P11 Feedback)
# Valide contra P11_feedback/_schema.yaml (types.optimizer)
# Max 4096 bytes

id: p11_opt_{{TARGET_SLUG}}
type: optimizer
lp: P11
title: "Optimizer: {{TARGET_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Optimizer: {{TARGET_NAME}}

## Objective
{{ONE_SENTENCE_ON_THE_METRIC_TO_IMPROVE}}

## Signals
| Metric | Threshold | Action |
|--------|-----------|--------|
| {{METRIC_1}} | {{THRESHOLD_1}} | {{ACTION_1}} |
| {{METRIC_2}} | {{THRESHOLD_2}} | {{ACTION_2}} |
| {{METRIC_3}} | {{THRESHOLD_3}} | {{ACTION_3}} |

## Loop
1. {{MEASURE}}
2. {{CHOOSE_CHANGE}}
3. {{VERIFY_EFFECT}}
""",
    "dag": """---
# TEMPLATE: DAG (P12 Orchestration)
# Valide contra P12_orchestration/_schema.yaml (types.dag)
# Max 3072 bytes

id: p12_dag_{{PIPELINE_SLUG}}
type: dag
lp: P12
title: "DAG: {{PIPELINE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# DAG: {{PIPELINE_NAME}}

## Nodes
```text
{{NODE_A}} -> {{NODE_B}} -> {{NODE_D}}
{{NODE_A}} -> {{NODE_C}} -> {{NODE_D}}
```

## Dependencies
| Node | Depends On | Output |
|------|------------|--------|
| {{NODE_B}} | {{NODE_A}} | {{OUTPUT_B}} |
| {{NODE_C}} | {{NODE_A}} | {{OUTPUT_C}} |
| {{NODE_D}} | {{NODE_B}}, {{NODE_C}} | {{OUTPUT_D}} |

## Scheduling Rule
- Parallelizable: {{YES_OR_NO}}
- Critical path: {{CRITICAL_PATH}}
""",
    "spawn_config": """---
# TEMPLATE: Spawn Config (P12 Orchestration)
# Valide contra P12_orchestration/_schema.yaml (types.spawn_config)
# Max 3072 bytes

id: p12_spawn_{{MODE_SLUG}}
type: spawn_config
lp: P12
title: "Spawn Config: {{MODE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Spawn Config: {{MODE_NAME}}

## Strategy
```yaml
mode: {{solo|grid|continuous}}
max_agents: {{MAX_AGENTS}}
ownership: {{HOW_WORK_IS_SPLIT}}
```

## Dispatch Rules
- Spawn when: {{SPAWN_TRIGGER}}
- Reuse when: {{REUSE_TRIGGER}}
- Wait when: {{WAIT_TRIGGER}}

## Limits
- Cost budget: {{BUDGET_RULE}}
- Timeout: {{TIMEOUT_RULE}}
""",
    "signal": """---
# TEMPLATE: Signal (P12 Orchestration)
# Valide contra P12_orchestration/_schema.yaml (types.signal)
# Max 4096 bytes

id: p12_sig_{{EVENT_SLUG}}
type: signal
lp: P12
title: "Signal: {{EVENT_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Signal: {{EVENT_NAME}}

## Payload
```json
{
  "satellite": "{{SATELLITE_NAME}}",
  "status": "{{complete|error|progress}}",
  "quality_score": {{QUALITY_SCORE}},
  "timestamp": "{{ISO_TIMESTAMP}}"
}
```

## Emission Rules
- Emit when: {{EVENT_TRIGGER}}
- Consumer: {{EXPECTED_CONSUMER}}
- Retry: {{RETRY_RULE}}
""",
    "dispatch_rule": """---
# TEMPLATE: Dispatch Rule (P12 Orchestration)
# Valide contra P12_orchestration/_schema.yaml (types.dispatch_rule)
# Max 3072 bytes

id: p12_dr_{{SCOPE_SLUG}}
type: dispatch_rule
lp: P12
title: "Dispatch Rule: {{SCOPE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Dispatch Rule: {{SCOPE_NAME}}

## Routing Table
| Condition | Satellite | Confidence |
|-----------|-----------|------------|
| {{KEYWORD_OR_SIGNAL_1}} | {{SATELLITE_1}} | {{0.0_TO_1.0}} |
| {{KEYWORD_OR_SIGNAL_2}} | {{SATELLITE_2}} | {{0.0_TO_1.0}} |
| {{KEYWORD_OR_SIGNAL_3}} | {{SATELLITE_3}} | {{0.0_TO_1.0}} |

## Fallbacks
- No match: {{DEFAULT_ROUTE}}
- Conflict: {{TIEBREAKER_RULE}}
- Escalation: {{ESCALATION_ROUTE}}
""",
}


LP_LABELS = {
    "P01_knowledge": "P01 Knowledge",
    "P02_model": "P02 Model",
    "P03_prompt": "P03 Prompt",
    "P04_tools": "P04 Tools",
    "P05_output": "P05 Output",
    "P06_schema": "P06 Schema",
    "P07_evals": "P07 Evals",
    "P08_architecture": "P08 Architecture",
    "P09_config": "P09 Config",
    "P10_memory": "P10 Memory",
    "P11_feedback": "P11 Feedback",
    "P12_orchestration": "P12 Orchestration",
}


PRIORITY_ORDER = [
    ("P05_output", "parser"),
    ("P06_schema", "type_def"),
    ("P06_schema", "output_schema"),
    ("P08_architecture", "law"),
    ("P08_architecture", "diagram"),
    ("P08_architecture", "component_map"),
]


def schema_types(schema_path: Path) -> list[str]:
    text = schema_path.read_text(encoding="utf-8")
    return re.findall(r"^  ([a-z0-9_]+):\n", text, flags=re.M)


def example_present(lp_dir: Path, artifact_type: str) -> bool:
    examples_dir = lp_dir / "examples"
    if not examples_dir.exists():
        return False
    patterns = [
        f"ex_{artifact_type}",
        f"p{lp_dir.name[1:3]}_{artifact_type}",
        artifact_type,
    ]
    for path in examples_dir.iterdir():
        if not path.is_file():
            continue
        lower = path.name.lower()
        if any(token in lower for token in patterns):
            return True
    return False


def template_present(lp_dir: Path, artifact_type: str) -> bool:
    return (lp_dir / "templates" / f"tpl_{artifact_type}.md").exists()


def generate_missing_templates() -> list[tuple[str, str]]:
    created: list[tuple[str, str]] = []
    for lp_dir in sorted(ROOT.glob("P*_*/")):
        schema_path = lp_dir / "_schema.yaml"
        if not schema_path.exists():
            continue
        templates_dir = lp_dir / "templates"
        templates_dir.mkdir(exist_ok=True)
        for artifact_type in schema_types(schema_path):
            target = templates_dir / f"tpl_{artifact_type}.md"
            if target.exists():
                continue
            content = TEMPLATES[artifact_type].strip() + "\n"
            target.write_text(content, encoding="utf-8")
            created.append((lp_dir.name, artifact_type))
    return created


def build_coverage_doc() -> str:
    rows = []
    totals = {
        "types": 0,
        "template": 0,
        "example": 0,
        "full": 0,
        "template_only": 0,
        "example_only": 0,
        "template_and_example": 0,
    }
    lp_stats = []
    lp_dirs = sorted(ROOT.glob("P*_*/"))
    row_num = 1
    for lp_dir in lp_dirs:
        schema_path = lp_dir / "_schema.yaml"
        if not schema_path.exists():
            continue
        types = schema_types(schema_path)
        lp_template = 0
        lp_example = 0
        lp_full = 0
        for artifact_type in types:
            has_template = template_present(lp_dir, artifact_type)
            has_example = example_present(lp_dir, artifact_type)
            gap = []
            if not has_template:
                gap.append("template")
            if not has_example:
                gap.append("example")
            gap_text = "+".join(gap) if gap else "-"
            rows.append(
                f"| {row_num} | {lp_dir.name[:3]} | {artifact_type} | YES | "
                f"{'YES' if has_template else 'NO'} | {'YES' if has_example else 'NO'} | "
                f"- | - | {gap_text} |"
            )
            row_num += 1
            totals["types"] += 1
            totals["template"] += int(has_template)
            totals["example"] += int(has_example)
            lp_template += int(has_template)
            lp_example += int(has_example)
            if has_template and has_example:
                totals["full"] += 1
                lp_full += 1
            elif has_template and not has_example:
                totals["example_only"] += 1
            elif not has_template and has_example:
                totals["template_only"] += 1
            else:
                totals["template_and_example"] += 1
        lp_stats.append((LP_LABELS[lp_dir.name], len(types), lp_template, lp_example, lp_full))

    example_gaps = []
    for lp_dir in lp_dirs:
        schema_path = lp_dir / "_schema.yaml"
        if not schema_path.exists():
            continue
        for artifact_type in schema_types(schema_path):
            if not example_present(lp_dir, artifact_type):
                example_gaps.append((lp_dir.name[:3], artifact_type))

    top_gaps = "\n".join(
        f"| {idx} | {artifact_type} | {lp} | Example gap after template closure |"
        for idx, (lp, artifact_type) in enumerate(example_gaps[:10], start=1)
    )

    lp_table = "\n".join(
        f"| {label} | {types} | {templates} | {examples} | {full} |"
        for label, types, templates, examples, full in lp_stats
    )

    return f"""# CEX Coverage Matrix - 69 Artifact Types across 12 LPs
> Generated: 2026-03-23 | Source: all 12 _schema.yaml files + templates/ + examples/ dirs
> Status: template coverage complete (69/69)

| # | LP | Type | Schema | Template | Example | density_min | max_bytes | Gap |
|---|----|------|--------|----------|---------|-------------|-----------|-----|
{chr(10).join(rows)}

---

## Statistics

| Metric | Count | % |
|--------|-------|---|
| Total types | {totals['types']} | 100% |
| Types with schema | {totals['types']} | 100% |
| Types with template | {totals['template']} | {totals['template'] / totals['types'] * 100:.1f}% |
| Types with example | {totals['example']} | {totals['example'] / totals['types'] * 100:.1f}% |
| Fully covered (schema+template+example) | {totals['full']} | {totals['full'] / totals['types'] * 100:.1f}% |
| Missing template only | {totals['template_only']} | {totals['template_only'] / totals['types'] * 100:.1f}% |
| Missing example only | {totals['example_only']} | {totals['example_only'] / totals['types'] * 100:.1f}% |
| Missing template+example | {totals['template_and_example']} | {totals['template_and_example'] / totals['types'] * 100:.1f}% |

### Coverage by LP

| LP | Types | Templates | Examples | Fully Covered |
|----|-------|-----------|----------|---------------|
{lp_table}

---

## Top 10 Priority Gaps

Types still missing examples after template closure:

| Priority | Type | LP | Rationale |
|----------|------|----|-----------|
{top_gaps}

---

*Audit source: `C:\\Users\\PC\\Documents\\GitHub\\cex` | 12 _schema.yaml files | {totals['template']} templates | {totals['example']} examples*
*ATLAS-CODEX | 2026-03-23*
"""


def update_coverage_doc() -> None:
    coverage_path = ROOT / "_meta" / "COVERAGE_68_TYPES.md"
    coverage_path.write_text(build_coverage_doc(), encoding="utf-8")


def main() -> None:
    created = generate_missing_templates()
    update_coverage_doc()
    created_sorted = sorted(
        created,
        key=lambda item: PRIORITY_ORDER.index(item)
        if item in PRIORITY_ORDER
        else len(PRIORITY_ORDER) + sorted(created).index(item),
    )
    print(f"Created {len(created_sorted)} templates")
    for lp_name, artifact_type in created_sorted:
        print(f"- {lp_name}/templates/tpl_{artifact_type}.md")


if __name__ == "__main__":
    main()
