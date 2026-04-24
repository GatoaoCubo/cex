---
id: n00_bugloop_manifest
kind: knowledge_card
8f: F3_inject
pillar: P11
nucleus: n00
title: "Bugloop -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, bugloop, p11, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_bugloop
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_multimodal_prompt
  - bld_schema_integration_guide
  - bld_schema_audit_log
  - bld_schema_pitch_deck
  - bld_schema_dual_loop_architecture
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A bugloop defines an automatic correction loop that detects errors, applies fixes, and verifies the fix before marking the issue resolved. It is the closed-loop quality enforcement mechanism that prevents human intervention for routine defects, enabling N05 (operations) to autonomously repair code, test failures, and configuration drift without stopping the pipeline.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `bugloop` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| target_kind | string | yes | Kind of artifact this bugloop applies to |
| detect_rule | string | yes | Condition or command that identifies a bug |
| fix_strategy | enum | yes | llm_rewrite \| template_apply \| rule_replace \| human_escalate |
| verify_command | string | yes | Command to run after fix to confirm resolution |
| max_iterations | integer | yes | Maximum fix attempts before human escalation |
| escalate_to | string | no | Nucleus to escalate to after max_iterations |

## When to use
- When setting up autonomous code repair for N05 engineering pipelines
- When building quality assurance loops for generated artifacts
- When configuring self-healing CI/CD pipelines that fix test failures automatically

## Builder
`archetypes/builders/bugloop-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind bugloop --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: bl_python_syntax_fixer
kind: bugloop
pillar: P11
nucleus: n05
title: "Example Bugloop"
version: 1.0
quality: null
---
# Bugloop: Python Syntax Auto-Fix
target_kind: cli_tool
detect_rule: "python -m py_compile {file} 2>&1 | grep SyntaxError"
fix_strategy: llm_rewrite
verify_command: "python -m py_compile {file}"
max_iterations: 3
escalate_to: n03
```

## Related kinds
- `quality_gate` (P11) -- gate that triggers a bugloop when it fails
- `self_improvement_loop` (P11) -- higher-order loop that may invoke bugloops
- `reward_signal` (P11) -- signal emitted when bugloop resolves an issue

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_bugloop]] | related | 0.53 |
| [[bld_schema_reranker_config]] | upstream | 0.44 |
| [[bld_schema_benchmark_suite]] | upstream | 0.43 |
| [[bld_schema_usage_report]] | upstream | 0.43 |
| [[bld_schema_dataset_card]] | upstream | 0.43 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.42 |
| [[bld_schema_integration_guide]] | upstream | 0.42 |
| [[bld_schema_audit_log]] | upstream | 0.41 |
| [[bld_schema_pitch_deck]] | upstream | 0.41 |
| [[bld_schema_dual_loop_architecture]] | upstream | 0.41 |
