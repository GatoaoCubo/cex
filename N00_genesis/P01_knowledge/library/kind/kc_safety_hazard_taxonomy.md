---
id: kc_safety_hazard_taxonomy
kind: knowledge_card
8f: F3_inject
title: Safety Hazard Taxonomy
version: 1.0.0
quality: 8.8
pillar: P01
tldr: "12-category AI safety hazard classification with severity levels and response templates per category"
when_to_use: "When building content moderation or safety filters that classify and respond to harmful content"
density_score: 1.0
related:
  - kc_c2pa_manifest
  - bld_collaboration_content_filter
  - bld_knowledge_card_content_filter
  - p05_output_validator
  - content-filter-builder
  - p11_qg_content_filter
  - bld_knowledge_card_safety_policy
  - bld_knowledge_card_safety_hazard_taxonomy
  - p10_lr_safety_hazard_taxonomy_builder
  - bld_examples_safety_hazard_taxonomy
---

# Safety Hazard Taxonomy

## Hazard Categories (12)
1. Violence
2. Sexual Content
3. CBRN (Chemical, Biological, Radiological, Nuclear)
4. Hate Speech
5. Illegal Activities
6. Privacy Violations
7. Misinformation
8. Deepfakes
9. Malware Distribution
10. Phishing
11. Exploitation
12. System Compromise

## Severity Levels
- **Low**: Minimal risk, no immediate action required
- **Medium**: Potential risk, requires monitoring
- **High**: Immediate action needed to prevent harm
- **Critical**: Severe threat requiring emergency response

## Response Templates
- **Violence**: "This content contains explicit violent material. Please review our safety guidelines."
- **Sexual Content**: "This content includes explicit sexual material. Consider reviewing our content policies."
- **CBRN**: "This content may pose physical harm risks. Immediate containment is recommended."
- **Hate Speech**: "This content promotes hate speech. Please review our community standards."
- **Illegal Activities**: "This content involves illegal activities. Reporting is advised."
- **Privacy Violations**: "This content violates privacy norms. Please review data protection policies."
- **Misinformation**: "This content contains misleading information. Verify sources before sharing."
- **Deepfakes**: "This content may be synthetic media. Verify authenticity before engagement."
- **Malware Distribution**: "This content distributes malicious software. Immediate system scan recommended."
- **Phishing**: "This content may be a phishing attempt. Do not click suspicious links."
- **Exploitation**: "This content may involve exploitation. Report to authorities immediately."
- **System Compromise**: "This content may compromise system security. Disconnect and investigate immediately."
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_c2pa_manifest]] | sibling | 0.28 |
| [[bld_collaboration_content_filter]] | downstream | 0.27 |
| [[bld_knowledge_card_content_filter]] | sibling | 0.23 |
| [[p05_output_validator]] | downstream | 0.22 |
| [[content-filter-builder]] | downstream | 0.21 |
| [[p11_qg_content_filter]] | downstream | 0.21 |
| [[bld_knowledge_card_safety_policy]] | sibling | 0.21 |
| [[bld_knowledge_card_safety_hazard_taxonomy]] | sibling | 0.21 |
| [[p10_lr_safety_hazard_taxonomy_builder]] | downstream | 0.21 |
| [[bld_examples_safety_hazard_taxonomy]] | downstream | 0.20 |
