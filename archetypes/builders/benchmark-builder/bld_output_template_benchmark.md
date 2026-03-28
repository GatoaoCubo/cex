---
kind: output_template
id: bld_output_template_benchmark
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for benchmark production
pattern: derives from SCHEMA.md — no extra fields
---

# Output Template: benchmark
```yaml
id: p07_bm_{{metric_slug}}
kind: benchmark
pillar: P07
title: "Benchmark: {{benchmark_name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
metric: "{{what_is_measured}}"
unit: "{{measurement_unit}}"
direction: "{{lower_is_better_or_higher_is_better}}"
baseline: {{current_measured_value}}
target: {{goal_value}}
iterations: {{integer_gte_10}}
warmup: {{integer_gte_1}}
percentiles: [50, 95, 99]
environment: "{{hardware_software_config}}"
domain: "{{domain_value}}"
quality: null
tags: [benchmark, {{metric}}, {{domain}}]
tldr: "{{dense_summary_max_160ch}}"
comparison_subjects: [{{subject_1}}, {{subject_2}}]
statistical_test: "{{test_name_or_null}}"
confidence_interval: 0.95
density_score: {{0.80_to_1.00}}
linked_artifacts:
  primary: "{{related_builder_or_schema}}"
  related: [{{related_artifact_refs}}]
## Benchmark Overview
{{what_is_measured_why_and_business_impact}}
## Methodology
- **Iterations**: {{iterations}} runs per subject
- **Warmup**: {{warmup}} runs discarded before measurement
- **Protocol**: {{step_by_step_measurement_process}}
- **Statistical test**: {{test_name}} at {{confidence}}% confidence
- **Outlier handling**: {{how_outliers_are_treated}}
## Metrics
| Metric | Unit | Direction | Baseline | Target |
|--------|------|-----------|----------|--------|
| {{metric_1}} | {{unit}} | {{direction}} | {{baseline}} | {{target}} |
| {{metric_2}} | {{unit}} | {{direction}} | {{baseline}} | {{target}} |
## Environment
- **Hardware**: {{cpu_ram_disk_network}}
- **Software**: {{os_runtime_versions}}
- **Config**: {{relevant_configuration_settings}}
- **Date**: {{when_baseline_was_measured}}
## Results Template
| Percentile | Subject A | Subject B | Delta |
|------------|-----------|-----------|-------|
| p50 | — | — | — |
| p95 | — | — | — |
| p99 | — | — | — |
## References
- {{reference_1}}
- {{reference_2}}
```
