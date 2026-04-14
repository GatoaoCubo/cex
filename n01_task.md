---
id: kc_marketplace_app_manifest
kind: knowledge_card
title: Marketplace App Manifest Spec
version: 1.0.0
quality: null
pillar: P01
---

# Marketplace App Manifest Specification

This manifest defines the required metadata, permissions, and pricing structure for apps listed on Claude/LangChain/HuggingFace marketplaces. It serves as a standardized template for developers to package their AI applications.

## Core Requirements

1. **Metadata Section**
   - `name`: App display name (max 100 chars)
   - `description`: 300-word summary of app functionality
   - `author`: Developer/organization name
   - `license`: Open source license type (MIT, Apache, etc.)
   - `tags`: 5-10 relevant keywords for discovery

2. **Permissions Section**
   - `access_level`: Public/Private/Subscription
   - `data_access`: List of datasets required (if any)
   - `api_keys`: Required API keys for operation
   - `environment`: Required runtime environment (e.g., Python 3.8+)

3. **Pricing Section**
   - `free_tier`: Boolean for free usage availability
   - `pricing_model`: Pay-per-use/Subscription/Free
   - `cost_per_call`: Currency + amount for pay-per-use
   - `billing_cycle`: Monthly/Annual for subscriptions

4. **Integration Details**
   - `framework`: Primary framework used (LangChain, HuggingFace, etc.)
   - `dependencies`: List of required libraries/packages
   - `compatibility`: Supported platforms (Web, Mobile, Desktop)
   - `documentation`: Link to full API/docs

## Validation Guidelines
- All required fields must be present
- File size limit: 1MB max
- Must include valid YAML syntax
- No markdown formatting allowed
- Must pass schema validation before listing

This template ensures consistent app listings across all supported marketplaces while maintaining flexibility for different development paradigms.
