---
id: p05_fmt_artifact_creation_report
kind: formatter
8f: F6_produce
pillar: P05
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "formatter-builder"
target_format: "markdown"
input_type: "structured_data"
rule_count: 11
domain: "artifact_reporting"
quality: 9.0
tags: [formatter, markdown, artifact-report, pipeline, P05, 8F, creation-report]
tldr: "Formats artifact creation reports into structured Markdown with build metadata, quality score, file path, size, and pipeline gate summary"
template_engine: "string_format"
pretty_print: true
escaping: "none"
encoding: "utf8"
locale: "en-US"
streaming: false
keywords: [artifact-report, creation-report, build-report, 8F-pipeline, formatter, pipeline-output]
density_score: 0.89
title: "P05 Formatter Create Output Template For Artifact Creation Report"
related:
  - formatter-builder
  - bld_collaboration_formatter
  - bld_architecture_formatter
  - p01_kc_output_formatting
  - p01_kc_formatter
  - bld_schema_formatter
  - bld_examples_formatter
  - bld_output_template_formatter
  - bld_architecture_course_module
  - bld_architecture_integration_guide
---
## Formatting Rules

| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| title_header | artifact_id | template | `# Artifact Creation Report: {value}` | none |
| kind_pill | kind | stringify | `**Kind:** \`{value}\`` | none |
| pillar_badge | pillar | stringify | `**

## Cross-References

- **Pillar**: P05 (Output)
- **Kind**: `formatter`
- **Artifact ID**: `p05_fmt_artifact_creation_report`
- **Tags**: [formatter, markdown, artifact-report, pipeline, P05, 8F, creation-report]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P05 | Output domain |
| Kind `formatter` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Cross-References

- **Pillar**: P05 (Output)
- **Kind**: `formatter`
- **Artifact ID**: `p05_fmt_artifact_creation_report`
- **Tags**: [formatter, markdown, artifact-report, pipeline, P05, 8F, creation-report]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P05 | Output domain |
| Kind `formatter` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Artifact Metadata

```yaml
kind: formatter
pillar: P05
pipeline: 8F
scoring: hybrid_3_layer
compilation: cex_compile
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[formatter-builder]] | related | 0.40 |
| [[bld_collaboration_formatter]] | downstream | 0.36 |
| [[bld_architecture_formatter]] | downstream | 0.35 |
| [[p01_kc_output_formatting]] | upstream | 0.28 |
| [[p01_kc_formatter]] | upstream | 0.27 |
| [[bld_schema_formatter]] | downstream | 0.25 |
| [[bld_examples_formatter]] | downstream | 0.25 |
| [[bld_output_template_formatter]] | related | 0.25 |
| [[bld_architecture_course_module]] | downstream | 0.25 |
| [[bld_architecture_integration_guide]] | downstream | 0.24 |
