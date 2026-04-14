---
id: kc_marketplace_app_manifest
kind: knowledge_card
title: Marketplace App Manifest Specification
version: 1.0.0
quality: null
pillar: P01
---

# Marketplace App Manifest Specification

This document defines the required structure for marketplace app manifests used in Claude, LangChain, and HuggingFace platforms. The manifest contains metadata, permissions, pricing, and integration specifications.

## Core Structure
```yaml
manifest_version: 1.0.0
app_id: string
name: string
description: string
author: string
license: string
```

## Metadata
- `manifest_version`: Required. Current version is 1.0.0
- `app_id`: Unique identifier for the application
- `name`: Human-readable name
- `description`: 140-character summary
- `author`: Creator/organization name
- `license`: Open source license type

## Permissions
```yaml
permissions:
  - type: read
    scope: user_data
  - type: write
    scope: system_config
```

## Pricing
```yaml
pricing:
  currency: USD
  tiers:
    - name: free
      price: 0
      features:
        - basic_access
    - name: pro
      price: 9.99
      features:
        - advanced_features
```

## Integrations
```yaml
integrations:
  - platform: claude
    api_key: <required>
  - platform: langchain
    model: <required>
  - platform: huggingface
    token: <required>
```

## Additional Fields
- `dependencies`: List of required libraries
- `keywords`: Search optimization tags
- `icon`: URL to application icon
- `category`: Platform-specific classification
```