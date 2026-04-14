---
id: kc_marketplace_app_manifest
kind: knowledge_card
title: Marketplace App Manifest Specification
version: 1.0.0
quality: null
pillar: P01
---

# Marketplace App Manifest Specification

## Overview
This document defines the required metadata, permissions, and pricing structure for apps listed on Claude, LangChain, and HuggingFace marketplaces.

## Core Structure
```yaml
manifest:
  metadata:
    name: App Name
    description: Brief functionality summary
    author: Creator information
    version: Semver format
    license: Open source/license type
    tags: Array of category tags
  permissions:
    access: Public/private visibility
    features: Array of enabled capabilities
    restrictions: Array of usage limitations
  pricing:
    model: free/premium/subscription
    rate: Price per usage unit
    currency: ISO currency code
    billing: Interval frequency
  metadata_extensions:
    framework: LangChain/Claude/HuggingFace
    compatibility: Supported versions
    dependencies: Required libraries
```

## Requirements
- All fields are required except `metadata_extensions`
- Use semantic versioning for software artifacts
- Pricing models must specify currency and billing cycle
- Permissions must include at minimum access control

## Best Practices
- Use consistent naming conventions across all manifests
- Document API rate limits in permissions section
- Include framework-specific metadata extensions
- Specify exact dependency versions for reproducibility
```