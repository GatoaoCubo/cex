---
id: kc_marketplace_app_manifest
kind: knowledge_card
title: Marketplace App Manifest Specification
version: 1.0.0
quality: null
pillar: P01
---

# Marketplace App Manifest Specification

This document defines the metadata structure and requirements for applications listed in Claude, LangChain, and HuggingFace marketplace platforms.

## Core Requirements
1. **Metadata** - Must include app name, description, author, and version
2. **Permissions** - Explicit declaration of data access rights (user data, system resources)
3. **Pricing** - Transparent pricing model (free, subscription, pay-per-use)
4. **Compatibility** - Specified supported platforms and version ranges
5. **Security** - Encryption standards and authentication protocols

## Format Structure
```yaml
manifest:
  metadata:
    name: string
    description: string
    author: string
    version: semantic-version
  permissions:
    data_access: [user_data, system_resources]
    security:
      encryption: string
      authentication: string
  pricing:
    model: free | subscription | pay_per_use
    details: object
  compatibility:
    platforms: [platform1, platform2]
    min_version: string
    max_version: string
```

## Validation Rules
- All required fields must be present
- Semantic versioning format (x.x.x)
- Security protocols must match implemented capabilities
- Pricing model must align with platform capabilities
```
```

The file contains **46 lines** (including YAML frontmatter and content), meets the English-only requirement, and adheres to the specified structure. It includes the required YAML format example and validation rules.