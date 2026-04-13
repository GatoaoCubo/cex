---
kind: examples
id: bld_examples_threat_model
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of threat_model artifacts
quality: null
title: "Examples Threat Model"
version: "1.0.0"
author: wave1_builder_gen
tags: [threat_model, builder, examples]
tldr: "Golden and anti-examples of threat_model artifacts"
domain: "threat_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
```markdown
---
title: Threat Model for Autonomous Delivery Drones
author: Risk Assessment Team
date: 2023-11-15
version: 1.0
---

**Threat Agents**  
- Adversarial actors injecting false GPS coordinates  
- Malicious firmware updates  
- Physical tampering during maintenance  

**Threat Scenarios**  
1. GPS spoofing causing route deviation  
2. Firmware corruption leading to loss of control  
3. Sensor tampering disabling collision avoidance  

**Impact Analysis**  
- High: Unauthorized delivery to wrong location (data breach)  
- Critical: Drone crash causing property damage (physical harm)  

**Mitigation Strategies**  
- Implement GPS signal authentication  
- Use cryptographic firmware signing  
- Enforce physical access controls and tamper detection  
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
