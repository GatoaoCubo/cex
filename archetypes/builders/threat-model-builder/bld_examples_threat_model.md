---
kind: examples
id: bld_examples_threat_model
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of threat_model artifacts
quality: 9.1
title: "Examples Threat Model"
version: "1.1.0"
author: n05_ops
tags: [threat_model, builder, examples]
tldr: "Golden and anti-examples of threat_model artifacts"
domain: "threat_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

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
