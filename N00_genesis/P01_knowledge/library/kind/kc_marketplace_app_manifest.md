---
id: kc_marketplace_app_manifest
kind: knowledge_card
8f: F3_inject
title: Marketplace App Manifest Specification
version: 1.0.0
quality: 8.7
pillar: P01
tldr: "Metadata manifest for AI marketplace listings: permissions, pricing, dependencies, and security"
when_to_use: "When publishing an app to Claude, LangChain, or HuggingFace marketplaces and need a standardized listing"
density_score: 0.94
related:
  - marketplace-app-manifest-builder
  - p03_sp_marketplace_app_manifest_builder
  - bld_examples_marketplace_app_manifest
  - bld_instruction_marketplace_app_manifest
  - bld_collaboration_marketplace_app_manifest
  - app-directory-entry-builder
  - p10_lr_marketplace_app_manifest_builder
  - bld_schema_marketplace_app_manifest
  - bld_tools_marketplace_app_manifest
  - bld_knowledge_card_marketplace_app_manifest
---

# Marketplace App Manifest Specification

This document defines the structure and requirements for marketplace application manifests used in Claude, LangChain, and HuggingFace ecosystems. The manifest serves as metadata configuration for app listings, defining permissions, pricing, and functional capabilities.

## Core Components

1. **Metadata**
   - App name and description
   - Versioning information
   - Author/organization details
   - License type and restrictions

2. **Permissions**
   - Access control settings
   - Data handling policies
   - Third-party integration rights
   - User privacy preferences

3. **Pricing Model**
   - Subscription tiers
   - Pay-per-use rates
   - Free tier limitations
   - Currency and payment methods

4. **Functional Capabilities**
   - Core features and APIs
   - Performance benchmarks
   - System requirements
   - Compatibility specifications

5. **Dependencies**
   - Required libraries/frameworks
   - Recommended runtime versions
   - External service integrations

6. **Security**
   - Data encryption standards
   - Authentication mechanisms
   - Audit logging requirements
   - Compliance certifications

## Platform-Specific Notes
- **Claude**: Include model version compatibility and prompt budget allocations
- **LangChain**: Specify chain execution policies and memory management
- **HuggingFace**: Define model card requirements and training data sources

This specification ensures consistent app discovery, security, and interoperability across different AI platform ecosystems.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[marketplace-app-manifest-builder]] | downstream | 0.45 |
| [[p03_sp_marketplace_app_manifest_builder]] | downstream | 0.40 |
| [[bld_examples_marketplace_app_manifest]] | downstream | 0.38 |
| [[bld_instruction_marketplace_app_manifest]] | downstream | 0.33 |
| [[bld_collaboration_marketplace_app_manifest]] | downstream | 0.30 |
| [[app-directory-entry-builder]] | downstream | 0.27 |
| [[p10_lr_marketplace_app_manifest_builder]] | downstream | 0.25 |
| [[bld_schema_marketplace_app_manifest]] | downstream | 0.24 |
| [[bld_tools_marketplace_app_manifest]] | downstream | 0.23 |
| [[bld_knowledge_card_marketplace_app_manifest]] | sibling | 0.23 |
