---
id: kc_marketplace_app_manifest
kind: knowledge_card
title: Marketplace App Manifest Spec
version: 1.0.0
quality: null
pillar: P01
---

# Marketplace App Manifest Specification

This document defines the required metadata structure for apps listed on Claude, LangChain, and HuggingFace marketplaces. The manifest contains:

## Core Metadata
- **name**: App display name (max 100 chars)
- **description**: 3-5 sentence summary of app functionality
- **version**: Semver format (e.g. 1.2.3)
- **license**: Open source license type (MIT, Apache, GPL, etc)
- **keywords**: 3-5 relevant search terms

## Platform Configuration
- **platforms**: Array of supported platforms (claude, langchain, huggingface)
- **permissions**: Object defining access controls
  - **read**: Array of allowed data types
  - **write**: Array of allowed data types
  - **execute**: Array of allowed operations

## Pricing Model
- **free**: Boolean indicating free availability
- **premium**: Object for paid features
  - **price**: Decimal value
  - **currency**: ISO 4217 code
  - **interval**: monthly/annual

## Technical Specs
- **dependencies**: Object of required libraries
  - **langchain**: Version range
  - **huggingface**: Version range
  - **claude**: Version range
- **entrypoint**: Main function identifier
- **framework**: Technology stack (e.g. React, FastAPI, TensorFlow)

## Compliance
- **terms_of_service**: URL to legal terms
- **privacy_policy**: URL to data usage policy
- **security_contact**: Email for security issues

## Example
```yaml
name: "Text2SQL Generator"
description: "Convert natural language queries to SQL for database interaction"
version: 1.1.0
license: MIT
keywords: ["sql", "nlp", "database"]
platforms: ["claude", "langchain"]
permissions:
  read: ["user_data", "query_history"]
  write: ["execution_logs"]
  execute: ["generate_sql"]
pricing:
  free: true
dependencies:
  langchain: "^0.2.0"
  huggingface: "^4.3.2"
entrypoint: "generate_sql"
framework: "FastAPI"
terms_of_service: "https://example.com/tos"
privacy_policy: "https://example.com/privacy"
security_contact: "security@example.com"
```
```