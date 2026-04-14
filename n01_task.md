---
id: kc_marketplace_app_manifest
kind: knowledge_card
title: Marketplace App Manifest Spec
version: 1.0.0
quality: null
pillar: P01
---

# Marketplace App Manifest Specification

This document defines the required metadata structure for apps listed on Claude/LangChain/HuggingFace marketplaces. The manifest enables platform-specific functionality and permissions management.

## Core Metadata
- **name**: App display name (max 100 chars)
- **description**: 300-word summary of app capabilities
- **version**: Semver format (e.g. 1.2.3)
- **license**: Open source license type (MIT, Apache, etc.)
- **author**: Developer/organization name
- **homepage**: Official project URL

## Permissions
- **read**: Access to user data (boolean)
- **write**: Modify user data (boolean)
- **execute**: Run background processes (boolean)
- **network**: Internet access (boolean)
- **storage**: File system access (boolean)

## Pricing Model
- **free**: No cost (boolean)
- **premium**: Subscription tiers (object)
  - **monthly**: $X
  - **annual**: $Y
- **pay_per_use**: Usage-based pricing (number)

## Technical Specs
- **framework**: Primary development framework (Claude, LangChain, HuggingFace)
- **dependencies**: Required libraries/versions
- **compatibility**: Supported OS/architectures
- **api_keys**: Required for API access (boolean)

## Optional Fields
- **documentation**: Link to developer docs
- **demo**: Interactive demo URL
- **social**: Social media links
- **keywords**: Search optimization tags

## Validation Rules
- All required fields must be present
- License must be valid open source
- Pricing model cannot be empty
- Framework must match platform capabilities
