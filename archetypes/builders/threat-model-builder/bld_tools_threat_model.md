---
kind: tools
id: bld_tools_threat_model
pillar: P04
llm_function: CALL
purpose: Tools available for threat_model production
quality: 8.9
title: "Tools Threat Model"
version: "1.1.0"
author: n05_ops
tags: [threat_model, builder, tools]
tldr: "Tools available for threat_model production"
domain: "threat_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## CEX Production Tools

This ISO records a threat model: the assets worth protecting and the attacker profiles that target them.
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compiles threat model artifact to YAML + validates frontmatter | After draft completion |
| cex_score.py | Runs 3-layer quality scoring (structural + rubric + semantic) | Post-draft before publish |
| cex_retriever.py | Finds similar threat models and relevant KCs for F3 injection | During F3 INJECT phase |
| cex_doctor.py | Validates artifact structure, required fields, and ID patterns | Pre-commit validation |

## External Security Tools (reference integration)
| Tool | Purpose | When |
|------|---------|------|
| MITRE ATT&CK Navigator | Maps threats to ATT&CK techniques, visualize coverage | During threat enumeration |
| OWASP Threat Dragon | Diagrammatic STRIDE threat modeling with export | During Phase 1 RESEARCH |
| Microsoft Threat Modeling Tool | Automated STRIDE analysis for system diagrams | During Phase 2 COMPOSE |
| Shodan / Censys | Attack surface discovery for external assets | Scope validation |

## External References
- MITRE ATT&CK: https://attack.mitre.org (enterprise threat taxonomy)
- MITRE ATLAS: https://atlas.mitre.org (AI/ML adversarial tactics)
- OWASP ASVS: Application Security Verification Standard
- NIST NVD: https://nvd.nist.gov (CVE database for vulnerability scoring)
- CVSS Calculator: https://www.first.org/cvss/calculator/4-0
