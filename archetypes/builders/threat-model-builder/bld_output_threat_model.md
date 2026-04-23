---
kind: output_template
id: bld_output_template_threat_model
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for threat_model production
quality: 9.1
title: "Output Template Threat Model"
version: "1.1.0"
author: n05_ops
tags: [threat_model, builder, output_template, stride, mitre]
tldr: "STRIDE-structured threat model template with risk matrix and MITRE ATT&CK mapping"
domain: "threat_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_instruction_threat_model
  - bld_examples_threat_model
  - p11_qg_threat_model
  - bld_schema_threat_model
  - bld_tools_threat_model
  - p03_sp_threat_model_builder
  - bld_collaboration_threat_model
  - bld_architecture_threat_model
  - n05_audit_threat_model_builder
  - p10_lr_threat_model_builder
---

```yaml
id: p11_tm_{{name}}
kind: threat_model
pillar: P11
title: "Threat Model: {{system_name}}"
version: "{{version}}"
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
domain: "{{domain}}"
quality: null
threat_level: {{threat_level_1_to_5}}
mitigation_status: "unaddressed"
tags: [{{tags}}]
tldr: "{{one_sentence_summary}}"
```

## 1. Scope and System Description

This ISO records a threat model: the assets worth protecting and the attacker profiles that target them.

**System:** `{{system_name}}`
**Boundaries:** `{{what_is_in_scope}}`
**Out of scope:** `{{what_is_excluded}}`
**Stakeholders:** `{{security_team}}`, {{dev_team}}, `{{compliance_team}}`
**Framework:** STRIDE + MITRE ATT&CK for Enterprise/AI

## 2. Asset Inventory

| Asset | Type | Sensitivity | Owner |
|-------|------|-------------|-------|
| `{{asset_1}}` | Data/Model/API/Infra | Critical/High/Medium/Low | `{{team}}` |
| `{{asset_2}}` | Data/Model/API/Infra | Critical/High/Medium/Low | `{{team}}` |

## 3. Threat Actors

| Actor | Motivation | Capability | Access Level |
|-------|-----------|-----------|--------------|
| External Attacker | `{{motivation}}` | High/Medium/Low | Remote |
| Malicious Insider | `{{motivation}}` | High/Medium/Low | Privileged |
| Automated Bot | `{{motivation}}` | High/Medium/Low | Remote |

## 4. STRIDE Threat Analysis

### 4.1 Spoofing (S)
| ID | Threat | Asset | Likelihood | Impact | CVSS | MITRE Technique |
|----|--------|-------|-----------|--------|------|-----------------|
| S01 | `{{threat_desc}}` | {{asset}} | H/M/L | H/M/L | {{score}} | T`{{technique_id}}` |

### 4.2 Tampering (T)
| ID | Threat | Asset | Likelihood | Impact | CVSS | MITRE Technique |
|----|--------|-------|-----------|--------|------|-----------------|
| T01 | `{{threat_desc}}` | {{asset}} | H/M/L | H/M/L | {{score}} | T`{{technique_id}}` |

### 4.3 Repudiation (R)
| ID | Threat | Asset | Likelihood | Impact | CVSS | MITRE Technique |
|----|--------|-------|-----------|--------|------|-----------------|
| R01 | `{{threat_desc}}` | {{asset}} | H/M/L | H/M/L | {{score}} | T`{{technique_id}}` |

### 4.4 Information Disclosure (I)
| ID | Threat | Asset | Likelihood | Impact | CVSS | MITRE Technique |
|----|--------|-------|-----------|--------|------|-----------------|
| I01 | `{{threat_desc}}` | {{asset}} | H/M/L | H/M/L | {{score}} | T`{{technique_id}}` |

### 4.5 Denial of Service (D)
| ID | Threat | Asset | Likelihood | Impact | CVSS | MITRE Technique |
|----|--------|-------|-----------|--------|------|-----------------|
| D01 | `{{threat_desc}}` | {{asset}} | H/M/L | H/M/L | {{score}} | T`{{technique_id}}` |

### 4.6 Elevation of Privilege (E)
| ID | Threat | Asset | Likelihood | Impact | CVSS | MITRE Technique |
|----|--------|-------|-----------|--------|------|-----------------|
| E01 | `{{threat_desc}}` | {{asset}} | H/M/L | H/M/L | {{score}} | T`{{technique_id}}` |

## 5. Risk Priority Matrix

| Threat ID | Risk Score (Likelihood x Impact) | Priority | Status |
|-----------|----------------------------------|----------|--------|
| S01 | `{{score}}` | Critical/High/Medium/Low | Open/Mitigated |

## 6. Mitigation Strategies

| Threat ID | Control | Type | Framework Reference | Owner | Due Date |
|-----------|---------|------|---------------------|-------|----------|
| S01 | `{{control_name}}` | Technical/Process/Physical | NIST CSF PR.AC-1 / ISO27001 A.9 | {{team}} | `{{date}}` |

## 7. AI-Specific Threat Addendum

_(Required when system includes ML models or AI pipelines)_

| AI Threat | Description | MITRE ATLAS Technique | Mitigation |
|-----------|-------------|----------------------|------------|
| Data Poisoning | `{{desc}}` | AML.T0020 | Differential privacy, data provenance |
| Model Inversion | `{{desc}}` | AML.T0024 | Output noise injection, access controls |
| Adversarial Examples | `{{desc}}` | AML.T0015 | Adversarial training, input sanitization |
| Model Extraction | `{{desc}}` | AML.T0005 | Rate limiting, query monitoring |

## 8. Assumptions and Limitations

- `{{assumption_1}}`
- `{{assumption_2}}`

## 9. Open Issues

| Issue | Owner | Due Date | Status |
|-------|-------|----------|--------|
| `{{issue}}` | {{team}} | `{{date}}` | Open |

## 10. References

- STRIDE: Microsoft SDL Threat Modeling
- MITRE ATT&CK: https://attack.mitre.org
- MITRE ATLAS: https://atlas.mitre.org
- NIST AI RMF: https://airc.nist.gov/Home
- ISO/IEC 23894:2021 AI Risk Management
- NIST SP 800-160 Vol. 2 Cyber Resiliency Engineering

## Validation Checklist
| Check | Requirement |
|-------|-------------|
| System boundary defined | Clear in/out of scope |
| Assets listed | All valuable data/functions cataloged |
| STRIDE applied | All 6 categories addressed |
| Threat severity rated | CVSS or HIGH/MED/LOW/INFO |
| Mitigations mapped | 1:1 threat-to-mitigation |
| Residual risk documented | After-mitigation exposure noted |
| Assumptions listed | Explicit trust boundaries stated |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_threat_model]] | upstream | 0.59 |
| [[bld_examples_threat_model]] | downstream | 0.53 |
| [[p11_qg_threat_model]] | downstream | 0.48 |
| [[bld_schema_threat_model]] | downstream | 0.45 |
| [[bld_tools_threat_model]] | upstream | 0.42 |
| [[p03_sp_threat_model_builder]] | upstream | 0.41 |
| [[bld_collaboration_threat_model]] | downstream | 0.37 |
| [[bld_architecture_threat_model]] | downstream | 0.36 |
| [[n05_audit_threat_model_builder]] | downstream | 0.36 |
| [[p10_lr_threat_model_builder]] | downstream | 0.35 |
