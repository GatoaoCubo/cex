---
id: kc_marketplace_app_manifest
kind: knowledge_card
title: Marketplace App Manifest Specification
version: 1.0.0
quality: null
pillar: P01
---

# Marketplace App Manifest Specification

This document defines the required metadata, permissions, and pricing structure for apps listed in Claude/LangChain/HuggingFace marketplaces.

## Core Structure
```yaml
manifest_version: "1.0"
app_id: "unique-identifier"
name:
  en: "App Name"
  other_langs: {...}
description:
  en: "Brief functionality summary"
  other_langs: {...}
author:
  name:
    en: "Author Name"
    other_langs: {...}
  contact: "email@example.com"
permissions:
  data_access: ["read", "write", "delete"]
  model_access: [" Claude", "LangChain", "HuggingFace"]
pricing:
  currency: "USD"
  tiered:
    basic: 0.00
    pro: 9.99
    enterprise: 29.99
deployment:
  environment: "production"
  region: "us-east-1"
  ssl: true
```

## Key Sections
1. **Metadata** - App identity and authorship
2. **Permissions** - Data and model access controls
3. **Pricing** - Tiered subscription model
4. **Deployment** - Cloud configuration parameters

## Compliance
All apps must include:
- Complete metadata in English and supported languages
- Explicit permission declarations
- Currency-specific pricing tiers
- SSL-enabled deployment configuration
```