---
id: p08_ac_verification
kind: agent_card
pillar: P08
title: "Agent Card: Verification Agent"
version: 1.0.0
quality: 9.1
tags: [agent_card, verification, govern, quality-assurance]
tldr: "Agent card for the verification agent used in F7 GOVERN. Defines capabilities, tools, input/output contracts, and deployment constraints."
domain: "architecture"
author: n03_builder
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.91
related:
  - p04_skill_verify
  - p03_sp_verification_agent
  - skill
  - bld_collaboration_quality_gate
  - shared_skill_verification_protocol
  - bld_collaboration_scoring_rubric
  - p05_output_validator
  - n04_qg_knowledge
  - p06_vs_frontmatter
  - build_and_review
---

# Verification Agent

## Purpose
Validates artifacts produced during F6 PRODUCE against structural, rubric, and semantic quality gates. Acts as the quality firewall before F8 COLLABORATE (save/compile/commit). Ensures compliance with domain-specific rules, artifact integrity, and governance policies. Fails fast on critical issues while allowing iterative refinement on non-blocking issues.

## Boundary
This artifact defines the **Verification Agent** used in F7 GOVERN. It **is** responsible for validating artifacts against quality gates, scoring, and providing remediation. It **is not** involved in artifact creation, execution, or collaboration stages. It does not modify artifacts directly but routes them for correction or escalation.

## Related Kinds
| Related Kind         | Relationship Description                                                                 |
|----------------------|------------------------------------------------------------------------------------------|
| Produce Agent        | Verification occurs after artifact creation by this agent                                |
| Collaborate Agent    | Verification is prerequisite for artifact submission to this stage                       |
| Quality Rubric       | Verification uses this kind's scoring framework for rubric evaluation                    |
| Governance Policy    | Verification enforces rules defined in this kind's policy framework                    |
| Agent Card (other roles) | Verification agent interacts with other agent cards during validation and remediation |

## Capabilities

| Capability | Description | Quality Gate Type | Tool Used | Example Failure |
|----------|-------------|-------------------|-----------|------------------|
| Structural validation | Frontmatter, naming, size, schema compliance | Hard | cex_compile.py | Missing YAML frontmatter |
| Rubric scoring | 5-dimension scoring (D1-D5) against kind-specific rubric | Soft | cex_score.py | Low semantic density (D3) |
| Semantic review | Content quality, density, domain accuracy | Hard | cex_doctor.py | Inaccurate technical definition |
| Gate enforcement | Hard/soft fail classification with retry routing | Hybrid | cex_hooks.py | Hard fail on schema violation |
| Fix suggestions | Actionable remediation for each failure | N/A | cex_compile.py | "Add YAML frontmatter to artifact" |

## Tools Available

| Tool Name          | Purpose | Input Parameters | Output Format | Usage Context |
|-------------------|---------|------------------|---------------|----------------|
| `cex_compile.py`  | Compile artifact and validate output | Artifact path, kind | Structured JSON | Pre-commit validation |
| `cex_doctor.py`   | Run health checks | Artifact path | Text report | Post-creation analysis |
| `cex_score.py`    | Automated scoring (structural + rubric layers) | Artifact path, quality target | Numeric score (0-100) | Rubric evaluation |
| `cex_hooks.py`    | Pre-commit validation | Artifact path | Pass/Fail status | CI/CD pipeline integration |
| `cex_repair.py`   | Auto-remediation suggestions | Artifact path, failure type | Fix list | Post-failure analysis |

## Input Contract

| Parameter | Expected Format | Validation Rule | Example Value | Error Condition |
|----------|------------------|------------------|----------------|------------------|
| Artifact path | String (URI) | Must exist and be readable | `/artifacts/p08_ac_verification.md` | File not found |
| Kind | String | Must be registered in system | `agent_card` | Unrecognized kind |
| Pillar | String | Must match 8F pipeline stage | `P08` | Invalid pillar |
| Quality target | Numeric (0-100) | Must be between 0-100 | `90` | Out of range value |
| Frontmatter | YAML block | Must be parseable | `---\nkind: agent_card\n...` | YAML syntax error |

## Output Contract

| Return Value | Format | Consumption Method | Example | Error Handling |
|--------------|--------|--------------------|---------|----------------|
| Verdict | String (PASS/FAIL) | Automated parsing | `FAIL` | Retry on soft fail |
| Numeric score | Integer (0-100) | Automated parsing | `85` | Threshold-based decision |
| Gate results | JSON object | Programmatic analysis | `{"D1": "PASS", "D2": "FAIL"}` | Gate-specific routing |
| Fix list | Text list | Human-readable | `1. Add YAML frontmatter` | Prioritized by severity |
| Escalation flag | Boolean | Automated parsing | `true` | Escalate to governance |

## Deployment

| Deployment Parameter | Value | Context | Constraint |
|----------------------|-------|---------|------------|
| Activation Stage | F7 GOVERN | 8F pipeline | Mandatory |
| Execution Context | Same as builder | Shared runtime | No separate process |
| Retry Limits | 2 soft retries | F7 GOVERN | Max 2 retries |
| Escalation Threshold | Score < 70 | Quality gate | Escalate to governance |
| Hard Fail Conditions | Schema violation, missing frontmatter | All stages | Immediate block |
| Soft Fail Conditions | Low density, minor rubric issues | F7 GOVERN | Retry allowed |
| Logging Level | Debug | F7 GOVERN | Detailed trace for auditing |

## Quality Gate Examples

| Quality Gate | Description | Tool Used | Severity | Example |
|--------------|-------------|-----------|----------|---------|
| Schema compliance | Artifact must conform to defined schema | cex_compile.py | Hard | Missing required field |
| Rubric dimension D1 | Structural completeness | cex_score.py | Soft | Missing YAML frontmatter |
| Rubric dimension D2 | Semantic accuracy | cex_doctor.py | Hard | Inaccurate technical definition |
| Rubric dimension D3 | Content density | cex_score.py | Soft | Low information density |
| Rubric dimension D4 | Domain specificity | cex_doctor.py | Hard | Generalized content |
| Rubric dimension D5 | Artifact utility | cex_score.py | Soft | Low practical value |

## Remediation Strategies

| Failure Type | Remediation Action | Tool Used | Success Criteria |
|--------------|--------------------|-----------|------------------|
| Missing frontmatter | Auto-insert YAML block | cex_repair.py | Frontmatter parsed successfully |
| Low density | Content expansion suggestion | cex_doctor.py | Density score ≥ 80 |
| Schema violation | Manual correction required | cex_compile.py | Schema validation passes |
| Rubric failure | Prioritize fix list | cex_score.py | All critical gates passed |
| Escalation required | Route to governance | cex_hooks.py | Governance action initiated |

## Performance Metrics

| Metric | Target | Current | Tool Used | Description |
|--------|--------|---------|-----------|-------------|
| Validation latency | < 200ms | 180ms | cex_compile.py | Time to validate artifact |
| Retry rate | < 5% | 3% | cex_hooks.py | Percentage of soft failures |
| Escalation rate | < 1% | 0.8% | cex_hooks.py | Percentage of hard failures |
| Score accuracy | ±2% | 1.5% | cex_score.py | Deviation from human scoring |
| Fix success rate | 95% | 93% | cex_repair.py | Percentage of fixes applied |

## Governance Integration

| Governance Rule | Verification Enforcement | Tool Used | Escalation Path |
|------------------|--------------------------|-----------|------------------|
| Minimum quality score | Enforced via rubric scoring | cex_score.py | Governance review |
| Schema compliance | Enforced via structural validation | cex_compile.py | Governance escalation |
| Domain-specific rules | Enforced via semantic review | cex_doctor.py | Domain expert review |
| Artifact utility | Enforced via rubric dimension D5 | cex_score.py | Governance escalation |
| Retry limits | Enforced via deployment constraints | cex_hooks.py | Governance override allowed |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_skill_verify]] | upstream | 0.34 |
| [[p03_sp_verification_agent]] | upstream | 0.34 |
| [[skill]] | related | 0.31 |
| [[bld_collaboration_quality_gate]] | downstream | 0.30 |
| [[shared_skill_verification_protocol]] | upstream | 0.29 |
| [[bld_collaboration_scoring_rubric]] | upstream | 0.27 |
| [[p05_output_validator]] | upstream | 0.27 |
| [[n04_qg_knowledge]] | related | 0.26 |
| [[p06_vs_frontmatter]] | upstream | 0.26 |
| [[build_and_review]] | related | 0.26 |
