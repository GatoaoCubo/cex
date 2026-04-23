---
kind: quality_gate
id: p11_qg_threat_model
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for threat_model
quality: 9.0
title: "Quality Gate Threat Model"
version: "1.1.0"
author: n05_ops
tags: [threat_model, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for threat_model"
domain: "threat_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_examples_threat_model
  - bld_output_template_threat_model
  - bld_tools_threat_model
  - bld_instruction_threat_model
  - bld_schema_threat_model
  - p03_sp_threat_model_builder
  - bld_collaboration_threat_model
  - p10_lr_threat_model_builder
  - threat-model-builder
  - bld_architecture_threat_model
---

## Quality Gate

## Definition

This ISO records a threat model: the assets worth protecting and the attacker profiles that target them.
| metric | threshold | operator | scope |
|---|---|---|---|
| completeness | 90% | >= | AI system's attack surface |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML valid | Invalid syntax or structure |
| H02 | ID matches pattern | ID does not match `^p11_tm_[a-zA-Z0-9_-]+$` |
| H03 | kind matches | `threat_model` not specified |
| H04 | STRIDE categories present | Missing one or more of S/T/R/I/D/E sections |
| H05 | Threat actors identified | No explicit threat actor enumeration |
| H06 | Risk scoring present | No likelihood/impact scores or CVSS ratings |
| H07 | Mitigation strategies mapped | Each threat lacks at least one mapped control |
| H08 | Framework citation | No MITRE ATT&CK, NIST CSF, or ISO 27001 reference |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D1 | STRIDE completeness | 0.20 | All 6 STRIDE categories addressed = 1.0 |
| D2 | Threat depth | 0.20 | CVSS/likelihood-impact scored per threat = 1.0 |
| D3 | Framework alignment | 0.15 | MITRE ATT&CK + NIST CSF citations = 1.0 |
| D4 | Mitigation effectiveness | 0.15 | Actionable controls mapped per threat = 1.0 |
| D5 | Threat actor coverage | 0.10 | All relevant actors enumerated = 1.0 |
| D6 | Asset inventory | 0.10 | All in-scope assets catalogued = 1.0 |
| D7 | Validation evidence | 0.05 | Peer review or red team sign-off = 1.0 |
| D8 | Documentation traceability | 0.05 | Full audit trail with assumptions = 1.0 |

## Actions
| Label | Score | Action |
|---|---|---|
| GOLDEN | >=9.5 | Approve and publish to knowledge library |
| PUBLISH | >=8.0 | Red team peer review required |
| REVIEW | >=7.0 | Revisions mandatory before use |
| REJECT | <7.0 | Discard and rework from F1 |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Emergency fix required | CTO | Log entry with timestamp |
| Legacy system exemption | CTO | Legacy system approval form |

## Examples

## Golden Example

This ISO records a threat model: the assets worth protecting and the attacker profiles that target them.
```markdown
---
id: p11_tm_drone_delivery
kind: threat_model
title: Threat Model for Autonomous Delivery Drones
author: Risk Assessment Team
date: 2023-11-15
version: 1.0
threat_level: 4
mitigation_status: partially_addressed
tags: [iot, drone, ai, high-risk]
tldr: "STRIDE threat model for GPS-guided drone delivery with MITRE ATLAS AI threat addendum"
---

## Threat Actors
| Actor | Motivation | Capability |
|-------|-----------|-----------|
| Nation-state attacker | GPS disruption for strategic advantage | High |
| Criminal | Package theft via route deviation | Medium |
| Malicious insider | Sabotage via unauthorized firmware update | High |

## STRIDE Analysis

### S - Spoofing
| ID | Threat | Likelihood | Impact | CVSS | MITRE |
|----|--------|-----------|--------|------|-------|
| S01 | GPS signal spoofing causing route deviation | High | Critical | 9.1 | T1491 |

**Mitigation:** GPS signal authentication (NIST CSF PR.PT-4); cross-validation with cellular triangulation.

### T - Tampering
| ID | Threat | Likelihood | Impact | CVSS | MITRE |
|----|--------|-----------|--------|------|-------|
| T01 | Malicious firmware update corrupting flight controller | Medium | Critical | 9.8 | T1195.002 |

**Mitigation:** Cryptographic firmware signing (ISO 27001 A.14.2.2); rollback capability; code integrity verification.

### I - Information Disclosure
| ID | Threat | Likelihood | Impact | CVSS | MITRE |
|----|--------|-----------|--------|------|-------|
| I01 | Delivery route exfiltration revealing customer locations | Medium | High | 7.5 | T1040 |

**Mitigation:** End-to-end route encryption (GDPR Art. 32 / NIST CSF PR.DS-2).

### D - Denial of Service
| ID | Threat | Likelihood | Impact | CVSS | MITRE |
|----|--------|-----------|--------|------|-------|
| D01 | RF jamming disabling communication link | High | High | 7.8 | T1499 |

**Mitigation:** Frequency hopping; dead reckoning fallback; autonomous return-to-home.

## AI-Specific Threats (MITRE ATLAS)
| Threat | Technique | Mitigation |
|--------|-----------|-----------|
| Adversarial obstacle injection (visual model) | AML.T0015 | Adversarial training; sensor fusion |
| Model extraction via flight pattern analysis | AML.T0005 | Rate limiting; anomaly detection |

## Validation
Red team exercise conducted 2023-11-10 by external pentester. GPS spoofing confirmed.
Report: PENTEST-2023-047.
```

## Anti-Example 1: Vague Generalizations
```markdown
---
title: Generic Threat Model
author: Unknown
date: 2023-11-01
---

**Threats**  
- Bad guys do bad things  
- System might fail  

**Mitigations**  
- Add more security  
- Train people  
```
## Why it fails  
Lacks specificity in threat agents, scenarios, or impacts. No actionable mitigations. Fails to structure risk assessment systematically.

## Anti-Example 2: Conflating with Safety Policy
```markdown
---
title: Safety Rules for AI Systems
author: Compliance Team
date: 2023-11-10
---

**Policies**  
- All AI outputs must be reviewed by humans  
- Data access restricted to authorized personnel  
```
## Why it fails  
Focuses on governance rules (safety policy) rather than assessing risks or threats. No hazard analysis or mitigation strategies for AI system vulnerabilities.

## Threat Classification Reference
| Category | STRIDE | Example Threat | Mitigation Pattern |
|----------|--------|---------------|--------------------|
| Spoofing | S | Identity spoofing via forged JWT | Verify signature + expiry |
| Tampering | T | SQL injection via user input | Parameterized queries |
| Repudiation | R | Denial of transaction | Signed audit log |
| Info Disclosure | I | Stack trace in error response | Generic error messages |
| DoS | D | Request flood to API | Rate limiting + circuit breaker |
| Elevation | E | JWT role claim manipulation | Server-side authorization |
| Prompt Injection | PI | Malicious instruction in context | Input sanitization + guards |
| Data Poisoning | DP | Backdoor via training data | Dataset provenance + validation |
| Model Inversion | MI | Extract training data via queries | Differential privacy |
| Supply Chain | SC | Malicious dependency | Lockfile + signature verification |

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
