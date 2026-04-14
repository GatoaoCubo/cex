---
id: kc_marketplace_app_manifest
kind: knowledge_card
title: Marketplace App Manifest Spec
version: 1.0.0
quality: null
pillar: P01
---

# Marketplace App Manifest Specification

This document defines the metadata structure for apps listed on Claude, LangChain, and HuggingFace marketplaces. The manifest enables platform-specific metadata, permission declarations, and pricing models.

## Core Structure
```yaml
manifest_version: "1.0.0"
app_id: "marketplace:app:uuid"
name:
  en: "App Name"
  other_langs: {...}
description:
  en: "Brief functionality summary"
  other_langs: {...}
```

## Required Fields
- `manifest_version` (string): Required format "x.y.z"
- `app_id` (string): Unique identifier across all marketplaces
- `name` (object): Primary language (en) and optional translations
- `description` (object): Primary language (en) and optional translations

## Optional Enhancements
- `icon_url` (string): URL to app icon
- `tags` (array): Keyword categories for discovery
- `license` (string): Open source/license type
- `dependencies` (array): Required runtime dependencies

## Permissions
```yaml
permissions:
  access: ["read", "write", "execute"]
  data: ["user_data", "system_logs"]
  network: ["public", "private"]
```

## Pricing Model
```yaml
pricing:
  type: "free" | "paid" | "subscription"
  currency: "USD" | "EUR" | "GBP"
  price: 0.99
  discount: 0.15
```

## Platform-Specific Metadata
```yaml
platforms:
  claude:
    model: "claude-3-5-sonnet"
    max_tokens: 2048
  langchain:
    framework: "langchain:0.2.1"
    pipeline: "llm+chain"
  huggingface:
    model_id: "bert-base-uncased"
    task_type: "text2text"
```

## Example
```yaml
manifest_version: "1.0.0"
app_id: "marketplace:app:42"
name:
  en: "Text Summarizer"
description:
  en: "AI-powered text summarization tool"
permissions:
  access: ["read", "write"]
  data: ["user_data"]
pricing:
  type: "paid"
  currency: "USD"
  price: 2.99
platforms:
  claude:
    model: "claude-3-5-son00"
  huggingface:
    model_id: "t5-small"
```
```