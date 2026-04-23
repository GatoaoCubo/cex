---
kind: instruction
id: bld_instruction_conformity_assessment
pillar: P03
llm_function: REASON
purpose: Step-by-step build instructions for producing an EU AI Act Annex-IV conformity assessment artifact
quality: 9.1
title: "Conformity Assessment Builder -- Instruction"
version: "1.0.0"
author: wave7_n05
tags: [conformity_assessment, builder, instruction]
tldr: "Three-phase build protocol: RESEARCH, COMPOSE, VALIDATE for Annex-IV conformity packages"
domain: "conformity_assessment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_knowledge_card_conformity_assessment
  - bld_manifest_conformity_assessment
  - bld_system_prompt_conformity_assessment
  - bld_examples_conformity_assessment
  - bld_output_template_conformity_assessment
  - bld_collaboration_conformity_assessment
  - bld_memory_conformity_assessment
  - bld_schema_conformity_assessment
  - kc_conformity_assessment
  - bld_knowledge_card_gpai_technical_doc
---
# Conformity Assessment Builder -- Instruction
## Overview

This instruction governs the 8F production of a `conformity_assessment` artifact under the EU-AI-Act.
Target: high-risk AI systems as defined by Annex-III, following the conformity procedure in Article-43.
Deadline: Aug-2026 for existing high-risk systems entering the market.
## Phase 1: RESEARCH (F1-F3)

### Step 1.1 -- Identify System Type (F1 CONSTRAIN)

| Action | Detail |
|--------|--------|
| Load schema | bld_schema_conformity_assessment.md |
| Confirm kind | conformity_assessment |
| Identify Annex-III category | Biometrics / Critical infrastructure / Education / Employment / Essential services / Law enforcement / Migration / Administration of justice / Democratic processes |
| Confirm Article-43 route | Internal conformity check (Annex VI) or notified body (Annex VII) |
| Flag Aug-2026 deadline | Mark all items required before Aug-2026 |

Annex-III categories that require notified body:
- Biometric identification (real-time remote, Art. 43(1)(a))
- Prohibited use exceptions reviewed by authority

All other high-risk categories: internal conformity check per Annex VI unless notified body elected.

### Step 1.2 -- Enumerate RMS Records (F3 INJECT)

Collect evidence for the risk-management-system (RMS) per EU-AI-Act Article 9:

| RMS Component | Evidence Type | Required? |
|---------------|---------------|-----------|
| Risk identification process | Process doc, SOP | MANDATORY |
| Risk estimation and evaluation | Risk register | MANDATORY |
| Risk mitigation measures | Control catalog | MANDATORY |
| Residual risk evaluation | Residual risk log | MANDATORY |
| Post-deployment risk review cadence | Schedule doc | MANDATORY |
| RMS version and update history | Change log | MANDATORY |

### Step 1.3 -- Gather Data-Governance Evidence (F3 INJECT)

Data-governance provisions per Article 10:

| Requirement | Evidence |
|-------------|----------|
| Training data description | Dataset cards or data sheets |
| Validation/test data description | Evaluation dataset docs |
| Data quality criteria | Data quality SOP |
| Bias examination and mitigation | Bias audit report |
| Dataset known limitations | Limitation registry |
| Data provenance records | Lineage documentation |

### Step 1.4 -- Collect Human-Oversight Documentation (F3 INJECT)

Human-oversight measures per Article 14:

| Measure | Evidence |
|---------|----------|
| Override capability | System architecture doc showing manual override |
| Interpretability support | Explainability report or XAI tool description |
| Operator training materials | Training curriculum and completion records |
| Monitoring dashboard specification | Dashboard spec or screenshot |
| Alerting on anomalies | Alert configuration docs |

### Step 1.5 -- Compile Post-Market-Monitoring Data (F3 INJECT)

Post-market-monitoring plan per Article 72:

| Component | Evidence |
|-----------|----------|
| Monitoring objectives and KPIs | Monitoring plan document |
| Data collection method | Telemetry or feedback pipeline spec |
| Serious incident reporting procedure | SIR SOP (Art. 73) |
| Periodic review schedule | Review calendar |
| Threshold for corrective action | Defined thresholds table |
## Phase 2: COMPOSE (F4-F6)

### Step 2.1 -- Plan Annex-IV Sections (F4 REASON)

Annex IV requires 7 categories of technical documentation:

| # | Category | Key Articles |
|---|----------|-------------|
| 1 | General description of the AI system | Art. 11, Annex IV(1) |
| 2 | Detailed description of elements and development process | Annex IV(2) |
| 3 | Monitoring, functioning, and control | Annex IV(3) |
| 4 | Risk management system | Art. 9, Annex IV(4) |
| 5 | Changes to the system through its lifecycle | Annex IV(5) |
| 6 | Standards and specifications applied | Annex IV(6) |
| 7 | EU declaration of conformity | Art. 47, Annex IV(7) |

### Step 2.2 -- Map Risk Controls to EU-AI-Act Articles (F4 REASON)

| Control Domain | Article | Annex IV Section |
|----------------|---------|-----------------|
| RMS process | Art. 9 | 4 |
| Data governance | Art. 10 | 2 |
| Technical documentation | Art. 11 | All |
| Record-keeping | Art. 12 | 3 |
| Transparency to deployers | Art. 13 | 1 |
| Human-oversight | Art. 14 | 3 |
| Accuracy, robustness, cybersecurity | Art. 15 | 2 |
| Post-market-monitoring | Art. 72 | 5 |
| Serious incident reporting | Art. 73 | 5 |

### Step 2.3 -- Document Accuracy, Robustness, Cybersecurity (F6 PRODUCE)

Per Article 15:

| Metric | Minimum Documentation |
|--------|-----------------------|
| Accuracy metrics | Metric name, threshold, test dataset, achieved value |
| Robustness measures | Adversarial test results, fallback behavior spec |
| Cybersecurity controls | Threat model reference, penetration test summary |
| Performance degradation handling | Graceful degradation procedure |

### Step 2.4 -- Generate Output Artifact (F6 PRODUCE)

Use bld_output_template_conformity_assessment.md.
Populate all placeholders. Do NOT leave any [PLACEHOLDER] unfilled.
Cite Annex-IV section numbers for every claim.
Flag items with "AUG-2026-DEADLINE" where applicable.
## Phase 3: VALIDATE (F7 GOVERN)

### Step 3.1 -- Completeness Checklist

| Item | Check |
|------|-------|
| All 7 Annex-IV categories present | [ ] |
| Annex-III category specified | [ ] |
| Article-43 procedure identified | [ ] |
| RMS section complete (5 sub-components) | [ ] |
| Data-governance section complete | [ ] |
| Human-oversight section complete | [ ] |
| Accuracy/robustness/cybersecurity documented | [ ] |
| Post-market-monitoring plan present | [ ] |
| Aug-2026 deadline items flagged | [ ] |
| Provider name and contact included | [ ] |
| Notified body ID (if applicable) | [ ] |
| Declaration date included | [ ] |

### Step 3.2 -- Quality Gate

Run bld_quality_gate_conformity_assessment.md checks.
Minimum score: 8.0 to proceed. Target: 9.0+.
If FAIL: return to Phase 2, address failing gates, re-validate.

### Step 3.3 -- Compile and Signal (F8 COLLABORATE)

```
python _tools/cex_compile.py {path}
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'complete', 9.0)"
git add {path} && git commit -m "[N03] conformity_assessment: {system_name}"
```


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_conformity_assessment]] | upstream | 0.61 |
| [[bld_manifest_conformity_assessment]] | downstream | 0.61 |
| [[bld_system_prompt_conformity_assessment]] | related | 0.60 |
| [[bld_examples_conformity_assessment]] | downstream | 0.53 |
| [[bld_output_template_conformity_assessment]] | downstream | 0.51 |
| [[bld_collaboration_conformity_assessment]] | downstream | 0.51 |
| [[bld_memory_conformity_assessment]] | downstream | 0.43 |
| [[bld_schema_conformity_assessment]] | downstream | 0.40 |
| [[kc_conformity_assessment]] | upstream | 0.39 |
| [[bld_knowledge_card_gpai_technical_doc]] | upstream | 0.39 |
