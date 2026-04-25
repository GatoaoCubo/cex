---
id: kc_consolidation_policy
kind: knowledge_card
8f: F3_inject
title: Consolidation Policy
version: 1.0.0
quality: 8.7
pillar: P01
tldr: "Memory lifecycle policy governing creation, retention, pruning, and deletion of stored data"
when_to_use: "When defining automated rules for data retention, deduplication, and time-based archival"
density_score: 0.95
related:
  - bld_knowledge_card_consolidation_policy
  - p09_kc_data_residency
  - consolidation-policy-builder
  - p03_sp_consolidation_policy_builder
  - kc_ai_compliance_gdpr
  - p01_kc_memory_scope
  - p09_qg_data_residency
  - atom_22_memory_taxonomy
  - bld_instruction_consolidation_policy
  - kc_compliance_checklist
---

# Consolidation Policy

This policy governs memory lifecycle management through three stages:

1. **Creation**  
   - New data is stored in volatile memory  
   - Metadata is automatically tagged with timestamp and priority

2. **Retention**  
   - Data is retained based on:  
     - Frequency of access (last 7 days)  
     - Criticality flags  
     - User-defined retention rules  
   - Automatic pruning occurs daily at 2:00 AM

3. **Deletion**  
   - Data older than 90 days is archived  
   - Data with zero access in 30 days is deleted  
   - User confirmation required for sensitive data

## Consolidation Guidelines
- Consolidate redundant data weekly
- Prioritize consolidation of:  
  - Duplicate entries  
  - Obsolete formats  
  - Low-value metadata
- Maintain 30-day audit trail for all deletions
- Use the `/consolidate` command for manual reviews
- Automatic consolidation runs nightly with 15% buffer
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_consolidation_policy]] | sibling | 0.26 |
| [[p09_kc_data_residency]] | sibling | 0.23 |
| [[consolidation-policy-builder]] | downstream | 0.23 |
| [[p03_sp_consolidation_policy_builder]] | downstream | 0.22 |
| [[kc_ai_compliance_gdpr]] | sibling | 0.22 |
| [[p01_kc_memory_scope]] | sibling | 0.18 |
| [[p09_qg_data_residency]] | downstream | 0.17 |
| [[atom_22_memory_taxonomy]] | sibling | 0.17 |
| [[bld_instruction_consolidation_policy]] | downstream | 0.16 |
| [[kc_compliance_checklist]] | sibling | 0.16 |
