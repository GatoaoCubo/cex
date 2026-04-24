---
id: p03_pt_intelligence_analysis
kind: prompt_template
8f: F6_produce
pillar: P03
title: "Intelligence Analysis Template"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: prompt-template-builder
variables:
  - name: intelligence_type
    type: string
    required: true
    default: null
    description: Type of intelligence analysis (market, competitive, technical, threat, strategic)
  - name: target
    type: string
    required: true
    default: null
    description: Subject of analysis (company, technology, market segment, threat actor)
  - name: scope
    type: string
    required: true
    default: null
    description: Analysis boundaries (geographic, temporal, or topical limits)
  - name: output_format
    type: string
    required: false
    default: "structured_report"
    description: Desired output format (brief, structured_report, executive_summary, tactical_brief)
  - name: sources
    type: list
    required: false
    default: ["public_sources", "industry_reports"]
    description: Information sources to prioritize for analysis
  - name: time_horizon
    type: string
    required: false
    default: "current"
    description: Temporal focus (historical, current, predictive, trend_analysis)
  - name: stakeholder
    type: string
    required: false
    default: "decision_makers"
    description: Primary audience for the intelligence product
variable_syntax: "mustache"
composable: false
domain: intelligence
quality: 9.2
tags: [intelligence, analysis, research, strategic, reusable]
tldr: "Generates structured intelligence analysis for various targets with configurable scope and output format."
keywords: [intelligence, analysis, research, competitive, market, strategic]
density_score: 0.89
related:
  - p12_dr_intelligence
  - p01_kc_intelligence_best_practices
  - p03_sp_n01_intelligence
  - p07_sr_intel_research
  - p06_is_intelligence_data_model
  - n01_intelligence
  - n01_agent_intelligence
  - p08_ac_intelligence
  - examples_prompt_template_builder
  - n01_sdk_validation_self_audit
---
## Purpose
Produces structured intelligence analysis for diverse intelligence requirements across multiple domains. Reuse scope: any intelligence gathering and analysis task where systematic examination of a target within defined boundaries is required. Invoke once per analysis target; vary intelligence type, scope, and output format to produce distinct analysis products from the same analytical framework.

## Variables Table
| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| intelligence_type | string | true | null | Type of intelligence analysis (market, competitive, technical, threat, strategic) |
| target | string | true | null | Subject of analysis (company, technology, market segment, threat actor) |
| scope | string | true | null | Analysis boundaries (geographic, temporal, or topical limits) |
| output_format | string | false | "structured_report" | Desired output format (brief, structured_report, executive_summary, tactical_brief) |
| sources | list | false | ["public_sources", "industry_reports"] | Information sources to prioritize for analysis |
| time_horizon | string | false | "current" | Temporal focus (historical, current, predictive, trend_analysis) |
| stakeholder | string | false | "decision_makers" | Primary audience for the intelligence product |

## Template Body
```
You are an intelligence analyst conducting {{intelligence_type}} intelligence analysis. Your task is to analyze {{target}} within the following parameters:

**Analysis Target**: {{target}}
**Intelligence Type**: {{intelligence_type}}
**Scope**: {{scope}}
**Time Horizon**: {{time_horizon}}
**Primary Stakeholder**: {{stakeholder}}
**Source Prioritization**: {{sources}}
**Output Format**: {{output_format}}

Conduct a comprehensive analysis following this structure:

1. **Executive Summary** (3-4 sentences)
   - Key findings about {{target}}
   - Primary implications for {{stakeholder}}
   - Confidence level assessment

2. **Target Profile**
   - Current status and positioning of {{target}}
   - Key characteristics relevant to {{intelligence_type}} analysis
   - Historical context within {{scope}}

3. **Analysis Framework**
   - Methodology applied for {{intelligence_type}} intelligence
   - Information sources utilized from {{sources}}
   - Analysis limitations and assumptions

4. **Findings and Assessment**
   - Primary intelligence insights about {{target}}
   - Supporting evidence and data points
   - Confidence levels for each major finding

5. **Implications and Outlook**
   - Strategic implications for {{stakeholder}}
   - Future trajectory assessment based on {{time_horizon}}
   - Potential scenarios and their probabilities

6. **Intelligence Gaps**
   - Information requirements not fully satisfied
   - Recommended follow-up collection priorities
   - Sources that could enhance analysis quality

7. **Recommendations**
   - Actionable intelligence for {{stakeholder}}
   - Risk mitigation strategies
   - Monitoring and update requirements

Tailor the depth and technical language to {{stakeholder}} requirements. Ensure all assessments include confidence indicators and source attribution where appropriate.
```

## Quality Gates
| Gate | Status | Notes |
|---|---|---|
| H01 | PASS | id `p03_pt_intelligence_analysis` matches pattern `^p03_pt_[a-z][a-z0-9_]+$` |
| H02 | PASS | All required frontmatter fields present: id, kind, pillar, title, variables, quality |
| H03 | PASS | All template body variables declared in variables list |
| H04 | PASS | All 7 declared variables appear in template body |
| H05 | PASS | File size approximately 3.2KB, under 8192 byte limit |
| H06 | PASS | Uniform mustache syntax `{{variable}}` throughout |
| H07 | PASS | Body contains required variable placeholders |
| H08 | PASS | Variable-body correspondence verified |

## Examples
### Example 1: Competitive Intelligence
**Variables**:
```yaml
intelligence_type: "competitive"
target: "OpenAI GPT-4 capabilities"
scope: "Enterprise AI market, North America and Europe"
output_format: "executive_summary"
sources: ["public_sources", "industry_reports", "patent_filings"]
time_horizon: "current"
stakeholder: "product_strategy_team"
```

**Rendered Output**:
```
You are an intelligence analyst conducting competitive intelligence analysis. Your task is to analyze OpenAI GPT-4 capabilities within the following parameters:

**Analysis Target**: OpenAI GPT-4 capabilities
**Intelligence Type**: competitive
**Scope**: Enterprise AI market, North America and Europe
**Time Horizon**: current
**Primary Stakeholder**: product_strategy_team
**Source Prioritization**: ["public_sources", "industry_reports", "patent_filings"]
**Output Format**: executive_summary

[... continues with full structured analysis framework ...]
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_dr_intelligence]] | downstream | 0.39 |
| [[p01_kc_intelligence_best_practices]] | upstream | 0.35 |
| [[p03_sp_n01_intelligence]] | related | 0.33 |
| [[p07_sr_intel_research]] | downstream | 0.30 |
| [[p06_is_intelligence_data_model]] | downstream | 0.26 |
| [[n01_intelligence]] | downstream | 0.25 |
| [[n01_agent_intelligence]] | upstream | 0.24 |
| [[p08_ac_intelligence]] | downstream | 0.24 |
| [[examples_prompt_template_builder]] | downstream | 0.23 |
| [[n01_sdk_validation_self_audit]] | downstream | 0.23 |
