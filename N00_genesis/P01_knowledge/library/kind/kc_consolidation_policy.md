---
id: kc_consolidation_policy
kind: knowledge_card
title: Consolidation Policy
version: 1.0.0
quality: 8.7
pillar: P01
density_score: 0.95
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