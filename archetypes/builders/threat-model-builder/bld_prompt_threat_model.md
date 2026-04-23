---
kind: instruction
id: bld_instruction_threat_model
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for threat_model
quality: 8.9
title: "Instruction Threat Model"
version: "1.1.0"
author: n05_ops
tags: [threat_model, builder, instruction]
tldr: "Step-by-step production process for threat_model"
domain: "threat_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_output_template_threat_model
  - bld_examples_threat_model
  - p11_qg_threat_model
  - bld_tools_threat_model
  - bld_schema_threat_model
  - p10_lr_threat_model_builder
  - bld_knowledge_card_threat_model
  - p03_sp_threat_model_builder
  - n05_audit_threat_model_builder
  - bld_architecture_threat_model
---

## Phase 1: RESEARCH  

This ISO records a threat model: the assets worth protecting and the attacker profiles that target them.
1. Identify AI system components: enumerate data flows, APIs, model endpoints, training pipelines, and interfaces.  
2. Build asset inventory: classify each component by sensitivity (Critical/High/Medium/Low) and owner.  
3. Enumerate threat actors: external attackers (nation-state, criminal, researcher), malicious insiders, automated bots.  
4. Map AI-specific attack vectors: data poisoning (AML.T0020), model inversion (AML.T0024), adversarial examples (AML.T0015), model extraction (AML.T0005).  
5. Review prior incidents: search CVE database, MITRE ATT&CK for AI, and internal incident history.  
6. Identify regulatory context: GDPR Art. 32, EU AI Act Art. 9, NIST AI RMF GOVERN function.  

## Phase 2: COMPOSE (STRIDE per component)  
1. For each asset, apply STRIDE systematically:  
   - S (Spoofing): Can an attacker impersonate a user, service, or data source?  
   - T (Tampering): Can training data, model weights, or outputs be modified?  
   - R (Repudiation): Can actions be denied -- is there sufficient audit logging?  
   - I (Information Disclosure): Can sensitive data or model internals be extracted?  
   - D (Denial of Service): Can the system be overwhelmed or degraded?  
   - E (Elevation of Privilege): Can an attacker gain unauthorized model or system access?  
2. For each threat, assign: Likelihood (H/M/L), Impact (H/M/L), CVSS base score (0-10).  
3. Map each threat to MITRE ATT&CK or MITRE ATLAS technique ID.  
4. Assign mitigations from NIST CSF (Identify/Protect/Detect/Respond/Recover), ISO 27001 Annex A, or OWASP Top 10.  
5. Prioritize by risk = Likelihood x Impact; Critical risks require immediate mitigation plan with owner and due date.  
6. Add AI-specific addendum per MITRE ATLAS if ML models are in scope.  

## Phase 3: VALIDATE  
- [ ] All 6 STRIDE categories addressed for each in-scope asset.  
- [ ] Every threat has a CVSS score and MITRE technique ID.  
- [ ] Mitigations are actionable (specific control, owner, due date) -- not generic ("add more security").  
- [ ] AI-specific threats (data poisoning, model inversion) addressed if ML pipeline is in scope.  
- [ ] At least one peer review or red team exercise referenced as validation evidence.  
- [ ] Document signed off by security lead and approved by compliance officer.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_threat_model]] | downstream | 0.50 |
| [[bld_examples_threat_model]] | downstream | 0.42 |
| [[p11_qg_threat_model]] | downstream | 0.38 |
| [[bld_tools_threat_model]] | downstream | 0.38 |
| [[bld_schema_threat_model]] | downstream | 0.36 |
| [[p10_lr_threat_model_builder]] | downstream | 0.35 |
| [[bld_knowledge_card_threat_model]] | upstream | 0.34 |
| [[p03_sp_threat_model_builder]] | related | 0.34 |
| [[n05_audit_threat_model_builder]] | downstream | 0.33 |
| [[bld_architecture_threat_model]] | downstream | 0.31 |
