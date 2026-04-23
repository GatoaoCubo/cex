---
kind: tools
id: bld_tools_pipeline_template
pillar: P04
llm_function: CALL
purpose: Tools available for pipeline_template production
quality: 8.0
title: "Tools Pipeline Template"
version: "1.0.0"
author: n03_hermes_w1_5
tags: [pipeline_template, builder, tools, hermes, scenario_indexed]
tldr: "Tools available for pipeline_template production"
domain: "pipeline_template construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.86
related:
  - bld_tools_crew_template
  - bld_tools_role_assignment
  - bld_tools_roi_calculator
  - bld_tools_skill
  - bld_tools_sales_playbook
  - bld_tools_discovery_questions
  - bld_tools_benchmark_suite
  - bld_tools_memory_benchmark
  - bld_tools_eval_metric
  - bld_architecture_webinar_script
---

## Production Tools
| Tool              | Purpose                                           | When              |
|-------------------|---------------------------------------------------|-------------------|
| cex_compile.py    | Compile pipeline_template .yaml to .json          | F8 COLLABORATE    |
| cex_retriever.py  | Find similar pipeline templates (reuse)           | F3 INJECT         |
| cex_query.py      | Discover role_assignment refs for stage binding   | F1 CONSTRAIN      |
| cex_doctor.py     | Validate schema + gate compliance                 | F7 GOVERN         |
| cex_score.py      | Peer-review scoring (HARD + SOFT)                 | F7 GOVERN         |
| signal_writer.py  | Signal N07 on completion                          | F8 COLLABORATE    |

## Validation Tools
| Tool                      | Purpose                                      | When       |
|---------------------------|----------------------------------------------|------------|
| cex_validate_scenario.py  | Confirm scenario in canonical 7-value enum   | Pre-commit |
| cex_stage_linter.py       | Validate stage order + role names            | F7 GOVERN  |
| cex_gate_checker.py       | Confirm reviewer + tester in mandatory gates | F7 GOVERN  |
| cex_tier_validator.py     | Validate model_tier values per stage         | F7 GOVERN  |

## External References
- OpenCode-Hermes multiagent catalog: github.com/1ilkhamov/opencode-hermes-multiagent
- SWE-bench revision-loop evaluation methodology
- aider.chat task mode taxonomy (maps to scenario enum)
- Claude Code /build pipeline patterns

## Tool Integration Checklist

- Verify tool name follows snake_case convention
- Validate input/output schema matches interface contract
- Cross-reference with capability_registry for discoverability
- Test tool invocation in sandbox before production use

## Invocation Pattern

```yaml
# Tool invocation contract
name: tool_name
input_schema: validated
output_schema: validated
error_handling: defined
timeout: configured
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_crew_template]] | sibling | 0.44 |
| [[bld_tools_role_assignment]] | sibling | 0.40 |
| [[bld_tools_roi_calculator]] | sibling | 0.29 |
| [[bld_tools_skill]] | sibling | 0.29 |
| [[bld_tools_sales_playbook]] | sibling | 0.26 |
| [[bld_tools_discovery_questions]] | sibling | 0.26 |
| [[bld_tools_benchmark_suite]] | sibling | 0.25 |
| [[bld_tools_memory_benchmark]] | sibling | 0.23 |
| [[bld_tools_eval_metric]] | sibling | 0.23 |
| [[bld_architecture_webinar_script]] | downstream | 0.23 |
