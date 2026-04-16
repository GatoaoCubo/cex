---
kind: output_template
id: bld_output_template_gpai_technical_doc
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for gpai_technical_doc production
quality: 9.1
title: "Output Template GPAI Technical Doc"
version: "1.0.0"
author: n01_wave7
tags: [gpai_technical_doc, builder, output_template, GPAI, EU-AI-Act, Annex-IV, Article-53, training-data, compute-budget, downstream-limit, technical-documentation]
tldr: "Template with vars for gpai_technical_doc production"
domain: "gpai_technical_doc construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```markdown
---
id: p11_gpai_{{model_slug}}.md
kind: gpai_technical_doc
pillar: P11
title: "GPAI Technical Documentation -- {{model_name}} v{{model_version}} (EU AI Act Article 53)"
provider: "{{provider_legal_entity}}"
model_version: "{{model_name}}-v{{model_version}}"
submission_date: "{{submission_date}}"
annex_iv_version: "EU AI Act 2024/1689"
domain: "{{domain}}"
quality: null
tags: [gpai_technical_doc, GPAI, EU-AI-Act, Annex-IV, Article-53]
tldr: "GPAI technical documentation for {{model_name}} per EU AI Act Article 53 and Annex IV"
created: "{{created_date}}"
updated: "{{updated_date}}"
author: "{{author}}"
---

## 1. Model Identity
- **Name**: {{model_name}}
- **Version**: {{model_version}}
- **Architecture**: {{architecture_type}} ({{parameter_count}} parameters)
- **Release Date**: {{release_date}}
- **Provider**: {{provider_legal_entity}} ({{country_of_registration}})
- **EU Representative**: {{eu_representative}} <!-- Required if non-EU provider -->
- **Model Family**: {{model_family}}

## 2. Training Data Summary
- **Datasets**: {{dataset_list}}
- **Total Volume**: {{token_count}} tokens (post-filtering)
- **Languages**: {{language_count}} languages; {{top_language}} {{top_language_pct}}%
- **Preprocessing**: {{preprocessing_methods}}
- **Data Governance**: {{data_governance_procedures}}
- **Copyright Compliance**: {{copyright_measures}}

## 3. Compute Budget
- **Total FLOP**: {{flop_estimate}}
- **Hardware**: {{gpu_count}} x {{gpu_model}}
- **Training Duration**: {{training_duration}}
- **Datacenter**: {{datacenter_location}}
- **Systemic Risk Threshold**: {{above_1e25_flop}} <!-- True/False: >= 10^25 FLOP -->

## 4. Energy Consumption
- **Total Energy**: {{mwh_consumed}} MWh
- **CO2-Equivalent**: {{co2_eq}} tonnes CO2-eq
- **PUE**: {{pue_value}}
- **Methodology**: {{energy_methodology}} <!-- e.g., GHG Protocol Scope 2 market-based -->
- **Grid Factor**: {{grid_factor}} kgCO2/kWh ({{grid_location}})

## 5. Evaluation Results

| Benchmark | Score | Date | Methodology |
|-----------|-------|------|-------------|
| {{benchmark_1}} | {{score_1}} | {{date_1}} | {{method_1}} |
| {{benchmark_2}} | {{score_2}} | {{date_2}} | {{method_2}} |
| {{benchmark_3}} | {{score_3}} | {{date_3}} | {{method_3}} |

**Known Performance Gaps**: {{known_gaps}}

## 6. Intended Purpose
- **Primary Use Cases**: {{primary_use_cases}}
- **Target Users**: {{target_users}}
- **Deployment Context**: {{deployment_context}}
- **Prohibited Uses**: {{prohibited_uses}}

## 7. Downstream Integration Limits
API consumers are prohibited from using this model for:
1. {{prohibited_downstream_1}}
2. {{prohibited_downstream_2}}
3. {{prohibited_downstream_3}}

Required safeguards for integrators: {{required_safeguards}}

## 8. Risk Mitigation Measures
- **Known Limitations**: {{known_limitations}}
- **Bias Assessments**: {{bias_assessments}}
- **Safety Evaluations**: {{safety_evaluations}}
- **Incident Reporting**: {{incident_reporting_contact}}
```
