---
id: kc_marketplace_app_manifest
kind: knowledge_card
title: Marketplace App Manifest Spec
version: 1.0.0
quality: null
pillar: P01
description: |
  Specification for marketplace app manifests used in Claude, LangChain, and HuggingFace listings. Contains metadata, permissions, pricing, and integration details required for app discovery and deployment.
---

# Marketplace App Manifest Specification

## Core Structure
```yaml
manifest_version: "1.0.0"
app_id: "unique-identifier"
name:
  en: "App Name"
  other: "localized names"
description:
  en: "Brief description"
  other: "localized descriptions"
```

## Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `app_id` | string | Unique identifier for the app |
| `name` | object | Application name in different languages |
| `description` | object | Description in different languages |

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `permissions` | object | Required access rights (e.g., `read`, `write`, `execute`) |
| `pricing` | object | Pricing model details (pay-per-use, subscription, etc.) |
| `integrations` | object | Supported platforms (Claude, LangChain, HuggingFace) |
| `metadata` | object | Additional technical specifications |
| `license` | string | Software license type |

## Example
```yaml
manifest_version: "1.0.0"
app_id: "langchain-ai-123"
name:
  en: "LangChain AI Assistant"
  es: "Asistente de LangChain"
description:
  en: "Advanced AI assistant with LangChain integration"
  es: "Asistente de IA avanzado con integración de LangChain"
permissions:
  read: ["user_data", "system_logs"]
  write: ["output_files"]
pricing:
  model: "pay-per-use"
  rate: "0.05 USD per 1000 tokens"
integrations:
  claude: true
  langchain: true
  huggingface: true
metadata:
  framework: "LangChain v0.2"
  api_version: "1.1.0"
license: "MIT"
```

## Best Practices
- Use ISO 639-1 language codes for localization
- Specify exact API versions for compatibility
- Document all permission scopes clearly
- Use standard pricing units and currencies
- Include metadata for technical compatibility
```
```