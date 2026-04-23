---
id: p05_fmt_knowledge_report
kind: formatter
pillar: P05
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "formatter-builder"
target_format: "markdown"
input_type: "structured_data"
rule_count: 7
domain: "knowledge_management"
quality: 9.1
tags: [formatter, markdown, knowledge-report, P05, intelligence, documentation]
tldr: "Converts structured knowledge report data into Markdown with metadata block, TL;DR callout, findings list, body sections, and numbered references"
template_engine: "string_format"
pretty_print: true
escaping: "none"
encoding: "utf8"
locale: "en-US"
streaming: false
keywords: [knowledge-report, intelligence-brief, research-output, markdown-formatter, N01-output, N04-output]
density_score: 0.89
related:
  - p05_fmt_brand_report
  - p06_schema_kc_structure
  - p01_kc_chain_of_thought
  - p05_fmt_intelligence_report
  - p01_kc_pydantic_patterns
  - SPEC_05_skills_runtime
  - bld_examples_response_format
  - p03_ins_response_format
  - bld_instruction_reasoning_strategy
  - p01_fse_kc_creation
---
## Formatting Rules
| Name | Input Field | Transform | Pattern | Options |
|------|-------------|-----------|---------|---------|
| title_block | report_title | template | `# {value}` | none |
| meta_block | report_date, domain, author, confidence_score | template | `> **Domain**: {domain} · **Date**: {report_date} · **Author**: {author} · **Confidence**: {confidence_pct}%` | confidence_score × 100, round to int |
| tldr_block | tldr | template | `> **TL;DR**: {value}` | max_length: 200, truncate: ellipsis |
| tags_inline | tags | stringify | `**Tags**: {joined}` | separator: `, `, each tag wrapped in backticks |
| sections_block | sections[].heading, sections[].content | template | `## {heading}\n\n{content}` | items joined with `\n\n` |
| findings_list | findings[] | tabulate | `- {item}` | bullet: `-`, items joined with `\n` |
| sources_list | sources[] | tabulate | `{idx}. {item}` | numbered: true, start: 1 |

## Input Specification
Type: structured_data
Structure: dict with scalar fields (`report_title` str, `report_date` YYYY-MM-DD str, `domain` str, `author` str, `confidence_score` float 0.0–1.0, `tldr` str) and list fields (`tags` list[str], `findings` list[str], `sections` list[{heading: str, content: str}], `sources` list[str]).
Example:
```json
{
  "report_title": "LLM Reasoning Patterns — Q1 2026",
  "report_date": "2026-04-02",
  "domain": "AI Research",
  "author": "N01",
  "confidence_score": 0.87,
  "tldr": "CoT and self-correction loops dominate; tool-augmented retrieval closes accuracy gaps by 40%.",
  "tags": ["reasoning", "CoT", "retrieval", "benchmark"],
  "findings": ["CoT improves multi-step math accuracy by 22%", "Self-correction reduces hallucination by 35%"],
  "sections": [{"heading": "Background", "content": "Reasoning benchmarks have shifted..."}, {"heading": "Methodology", "content": "Evaluated 6 models across 3 suites..."}],
  "sources": ["Wei et al. (2022) Chain-of-Thought — arXiv:2201.11903", "Shinn et al. (2023) Reflexion — arXiv:2303.11366"]
}
```

## Output Specification
Format: markdown
Example:
```markdown
# LLM Reasoning Patterns — Q1 2026

> **Domain**: AI Research · **Date**: 2026-04-02 · **Author**: N01 · **Confidence**: 87%

> **TL;DR**: CoT and self-correction loops dominate; tool-augmented retrieval closes accuracy gaps by 40%.

**Tags**: `reasoning`, `CoT`, `retrieval`, `benchmark`

## Background

Reasoning benchmarks have shifted...

## Methodology

Evaluated 6 models across 3 suites...

## Key Findings

- CoT improves multi-step math accuracy by 22%
- Self-correction reduces hallucination by 35%

## References

1. Wei et al. (2022) Chain-of-Thought — arXiv:2201.11903
2. Shinn et al. (2023) Reflexion — arXiv:2303.11366
```

## Template
Engine: string_format
```text
# {report_title}

> **Domain**: {domain} · **Date**: {report_date} · **Author**: {author} · **Confidence**: {confidence_pct}%

> **TL;DR**: {tldr}

**Tags**: {tags_formatted}

{sections_formatted}

## Key Findings

{findings_formatted}

## References

{sources_formatted}
```

## Edge Cases
- Null values: `confidence_score` null → omit confidence clause from meta_block; `tldr` null → omit TL;DR line; any list field null → omit its section block entirely
- Empty strings: field value `""` → treated as null (section omitted, not rendered as blank)
- Special characters: backtick in a tag name escaped as `` \` ``; pipe `|` in section content passed through unescaped (not inside a table); no HTML escaping required for plain Markdown
- Overflow: `tldr` truncated at 200 chars with trailing ellipsis; `sections[].content` unbounded by design; `report_title` not truncated
- **Boundary**: transforms structured data → presentation only. Does NOT extract from raw text (that is `parser`). Does NOT instruct an LLM on output schema (that is `response_format`).

## References
- CommonMark Markdown specification: commonmark.org/spec
- Python string format mini-language: docs.python.org/3/library/string.html#format-spec-mini-language
- CEX formatter schema: P06/_schema.yaml (`p05_fmt_*` pattern)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p05_fmt_brand_report]] | sibling | 0.27 |
| [[p06_schema_kc_structure]] | downstream | 0.24 |
| [[p01_kc_chain_of_thought]] | upstream | 0.24 |
| [[p05_fmt_intelligence_report]] | sibling | 0.22 |
| [[p01_kc_pydantic_patterns]] | upstream | 0.22 |
| [[SPEC_05_skills_runtime]] | upstream | 0.22 |
| [[bld_examples_response_format]] | downstream | 0.20 |
| [[p03_ins_response_format]] | related | 0.20 |
| [[bld_instruction_reasoning_strategy]] | upstream | 0.19 |
| [[p01_fse_kc_creation]] | upstream | 0.19 |
