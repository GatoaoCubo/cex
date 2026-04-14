---
id: kc_marketplace_app_manifest
kind: knowledge_card
title: Marketplace App Manifest Spec
version: 1.0.0
quality: null
pillar: P01
description: Marketplace app manifest spec for Claude/LangChain/HuggingFace listings (metadata, perms, pricing)
---
# Marketplace App Manifest Spec

## Metadata
- **app_name**: Required string (e.g., "claude-ai-agent")
- **description**: 140-character summary of core functionality (e.g., "AI-powered document summarizer with natural language processing")
- **author**: Creator/organization name (e.g., "Anthropic Technologies")
- **version**: Semver format (e.g., "0.2.1")
- **license**: Open source license type (MIT, Apache, etc.)
- **keywords**: Array of 3-5 relevant tags (e.g., ["ai", "nlp", "summarization"])

## Permissions
- **data_access**: 
  - `read`: Access to user data (e.g., "read:email")
  - `write`: Modify user data (e.g., "write:documents")
  - `delete`: Remove user data (e.g., "delete:cache")
- **api_usage**: 
  - `rate_limit`: Max requests per minute (e.g., "500")
  - `endpoint`: Specific API endpoints allowed (e.g., "/v1/summarize")
- **third_party**: 
  - `integration`: Approved third-party services (e.g., "stripe", "paypal")
  - `sandbox`: Isolated environment for testing (enabled by default)

## Pricing
- **model**: 
  - `pay_per_use`: Based on API calls (e.g., "$0.001 per 1000 tokens")
  - `subscription`: Monthly/yearly plans (e.g., "$99/month for 10,000 API calls")
  - `freemium`: Free tier + premium upgrades (e.g., "100 free API calls/month")
- **tiers**: 
  - `basic`: Core features (e.g., 100 API calls/month)
  - `pro`: Advanced features (e.g., 1000 API calls/month)
  - `enterprise`: Custom SLA and support (e.g., "24/7 dedicated support")
- **payment**: 
  - `stripe`: Credit card processing
  - `paypal`: Alternative payment method
  - `bank_transfer`: Direct bank transfer

## Additional Fields
- **dependencies**: 
  - `libraries`: Required frameworks (e.g., "langchain@0.2.1")
  - `models`: AI models required (e.g., "huggingface/gpt2")
- **security**: 
  - `encryption`: Data protection standards (e.g., "AES-256")
  - `auth`: Authentication methods (OAuth2, JWT)
- **compliance**: 
  - `gdpr`: EU data protection compliance (certified)
  - `ccpa`: California privacy law compliance (compliant)
