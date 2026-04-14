---
id: kc_c2pa_manifest
kind: knowledge_card
title: C2PA Manifest for AI-Generated Media
version: 1.0.0
quality: null
pillar: P01
language: en
---

# C2PA Manifest for AI-Generated Media (C2PA 2.3)

## Core Elements
1. **Claim**: Provenance statement asserting AI generation (e.g., "This content was created by an AI system").
2. **Assertions**: Technical claims about AI generation (e.g., model type, training data, generation parameters).
3. **Ingredient**: Metadata about AI system components (e.g., model architecture, training data sources).
4. **Signature**: Cryptographic signature verifying manifest authenticity and integrity.
5. **AI-ML Generator Attribution**: Explicit identification of AI/ML systems responsible for content creation.

## Technical Requirements
- **Schema Compliance**: Manifest must conform to C2PA 2.3 schema standards
- **Immutable Provenance**: Signature must be verifiable across content formats
- **Transparency**: Clear documentation of AI system capabilities and limitations
- **Audit Trail**: Immutable record of generation parameters and data sources

## Use Cases
- Digital media authentication
- Content origin verification
- AI-generated art attribution
- Synthetic media detection

## Implementation
Manifests are embedded in content files (e.g., JSON metadata in images/videos) or stored separately with cryptographic links. Verification tools validate signatures and check schema compliance against C2PA standards.
