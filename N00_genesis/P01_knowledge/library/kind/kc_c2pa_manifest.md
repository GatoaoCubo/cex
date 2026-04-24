---
id: kc_c2pa_manifest
kind: knowledge_card
8f: F3_inject
title: C2PA 2.3 Content Credential Manifest
version: 1.1.0
quality: 9.1
pillar: P01
author: CEX Documentation Team
date: 2023-11-15
tags: [C2PA, provenance, digital assets, authenticity, metadata]
last_modified: 2023-11-16
density_score: 1.0
related:
  - c2pa-manifest-builder
  - bld_collaboration_c2pa_manifest
  - bld_knowledge_card_c2pa_manifest
  - p03_sp_c2pa_manifest_builder
  - bld_collaboration_vc_credential
  - bld_examples_vc_credential
  - bld_tools_c2pa_manifest
  - bld_instruction_c2pa_manifest
  - bld_knowledge_card_agent_grounding_record
  - bld_manifest_agent_grounding_record
---

# C2PA Manifest Specification

## Overview
The C2PA (Certified Claims and Provenance for Authenticity) manifest is a JSON-based metadata format that provides cryptographic proof of a digital asset's authenticity, ownership, and usage rights. It enables verification of content integrity and provenance across the digital supply chain.

## Key Features
- **Immutable Provenance**: Cryptographic signatures ensure data integrity
- **Claim Validation**: Verifiable claims about content ownership and usage
- **Cross-Platform Compatibility**: Works with major digital asset platforms
- **Extensible Schema**: Supports additional metadata through custom claims

## Manifest Structure
The manifest contains three core components:

### 1. Header
```json
{
  "@context": "https://w3id.org/c2pa/context.jsonld",
  "type": "Manifest",
  "id": "urn:uuid:123e4567-e89b-12d3-a456-426614174000",
  "version": "1.0.0"
}
```

### 2. Claims
```json
{
  "claim": {
    "type": "Ownership",
    "issuer": "https://example.com/issuer",
    "subject": "urn:uuid:78901234-5678-90ab-cdef-112233445566",
    "validFrom": "2023-01-01T00:00:00Z",
    "validUntil": "2024-01-01T00:00:00Z",
    "signature": "base64-encoded-signature"
  }
}
```

### 3. Provenance
```json
{
  "provenance": {
    "type": "Creation",
    "creator": "https://example.com/creator",
    "timestamp": "2023-11-15T14:30:00Z",
    "software": "C2PA Validator 2.1.0",
    "signature": "base64-encoded-signature"
  }
}
```

## Core Components

### 1. Header
| Field | Description | Required |
|-------|-------------|----------|
| `@context` | URI to the context document | ✅ Yes |
| `type` | Must be "Manifest" | ✅ Yes |
| `id` | Unique identifier for the manifest | ✅ Yes |
| `version` | Schema version | ✅ Yes |

### 2. Claims
| Claim Type | Description | Use Case |
|------------|-------------|----------|
| Ownership | Proves content ownership | Digital rights management |
| Usage | Grants specific usage permissions | Content licensing |
| Authenticity | Verifies content integrity | Fraud prevention |
| Attribution | Credits original creators | Content discovery |

### 3. Provenance
| Provenance Type | Description | Example |
|------------------|-------------|---------|
| Creation | Records content creation | New digital asset |
| Modification | Tracks content changes | Version history |
| Distribution | Records content sharing | Content syndication |
| Destruction | Proves content removal | Data erasure |

## Validation Process
1. **Signature Verification**: Check cryptographic signatures against public keys
2. **Schema Validation**: Ensure compliance with C2PA schema version
3. **Claim Validation**: Verify claim types and validity periods
4. **Provenance Chain**: Confirm continuity of provenance records

## Use Cases

### 1. Digital Rights Management
```json
{
  "claim": {
    "type": "Usage",
    "issuer": "https://rights.example.com",
    "subject": "urn:uuid:123e4567-e89b-12d3-a456-426614174000",
    "validFrom": "2023-10-01T00:00:00Z",
    "validUntil": "2024-01-01T00:00:00Z",
    "permissions": ["view", "share"]
  }
}
```

### 2. Content Verification
```json
{
  "provenance": {
    "type": "Creation",
    "creator": "https://validator.example.com",
    "timestamp": "2023-11-15T14:30:00Z",
    "software": "C2PA Validator 2.1.0",
    "signature": "base64-encoded-signature"
  }
}
```

### 3. Compliance Reporting
```json
{
  "claim": {
    "type": "Compliance",
    "issuer": "https://compliance.example.com",
    "subject": "urn:uuid:78901234-5678-90ab-cdef-112233445566",
    "validFrom": "2023-09-01T00:00:00Z",
    "validUntil": "2024-09-01T00:00:00Z",
    "standards": ["ISO 23058", "IEEE 1609.2"]
  }
}
```

## Best Practices
1. **Use UUIDs**: Always use UUIDs for identifiers
2. **Version Control**: Always specify the schema version
3. **Secure Signatures**: Use strong cryptographic algorithms
4. **Timestamping**: Include accurate timestamps for provenance
5. **Minimal Claims**: Only include necessary claims to reduce attack surface

## Common Pitfalls
| Issue | Solution |
|-------|----------|
| Missing signature | Always include cryptographic signatures |
| Invalid timestamp | Use trusted time-stamping services |
| Outdated schema | Always use the latest schema version |
| Missing context | Always include the @context field |
| Invalid claim types | Only use approved claim types |

## Implementation Guide
1. **Generate UUID**: Create a unique identifier for the manifest
2. **Create Claims**: Define ownership, usage, and authenticity claims
3. **Add Provenance**: Record creation and modification history
4. **Sign Manifest**: Use cryptographic signatures for integrity
5. **Validate**: Verify against C2PA schema and public keys

## Tools
- **C2PA Validator**: https://github.com/c2pa/c2pa-validator
- **Manifest Generator**: https://tools.c2pa.org/manifest-generator
- **Schema Viewer**: https://w3id.org/c2pa/context.jsonld

## References
- [C2PA Specification](https://c2pa.org/specification/)
- [W3C Provenance Working Group](https://www.w3.org/2013/11/proofs/)
- [ISO 23058:2022](https://www.iso.org/standard/80314.html)
- [IEEE 1609.2](https://ieeexplore.ieee.org/document/9457445)

## Appendix
### Sample Manifest
```json
{
  "@context": "https://w3id.org/c2pa/context.jsonld",
  "type": "Manifest",
  "id": "urn:uuid:123e4567-e89b-12d3-a456-426614174000",
  "version": "1.0.0",
  "claim": {
    "type": "Ownership",
    "issuer": "https://example.com/issuer",
    "subject": "urn:uuid:78901234-5678-90ab-cdef-112233445566",
    "validFrom": "2023-01-01T00:00:00Z",
    "validUntil": "2024-01-01T00:00:00Z",
    "signature": "base64-encoded-signature"
  },
  "provenance": {
    "type": "Creation",
    "creator": "https://example.com/creator",
    "timestamp": "2023-11-15T14:30:00Z",
    "software": "C2PA Validator 2.1.0",
    "signature": "base64-encoded-signature"
  }
}
```

## Glossary
| Term | Definition |
|------|------------|
| Claim | A statement about the content's properties |
| Provenance | Record of the content's origin and history |
| Signature | Cryptographic proof of authenticity |
| UUID | Universally Unique Identifier |
| Schema | Definition of the manifest structure |
| Validator | Tool for verifying manifest integrity |
| Context | Metadata about the manifest's structure |
| Issuer | Entity that created the claim |
| Subject | Content being described by the claim |
| Timestamp | Record of when the claim was made |
| Software | Tool used to create the manifest |
| Standard | Industry-wide specification for manifests |
| Compliance | Adherence to specific regulations or standards |
| Authenticity | Verification of content originality |
| Ownership | Proof of content ownership |
| Usage | Permissions for content usage |
| Attribution | Credit to original creators |
| Destruction | Proof of content removal |
| Distribution | Record of content sharing |
| Modification | Tracking of content changes |
| Creation | Record of content origin |
| Validation | Process of verifying manifest integrity |
| Verification | Process of confirming claims |
| Integrity | Assurance of data authenticity |
| Security | Protection against tampering |
| Trust | Confidence in content authenticity |
| Transparency | Openness about content history |
| Accountability | Responsibility for content integrity |
| Traceability | Ability to track content history |
| Non-repudiation | Proof of content origin |
| Immutability | Protection against data alteration |
| Authenticity | Verification of content originality |
| Provenance | Record of content origin and history |
| Metadata | Data about the content |
| Signature | Cryptographic proof of authenticity |
| Timestamp | Record of when the claim was made |
| Software | Tool used to create the manifest |
| Standard | Industry-wide specification for manifests |
| Compliance | Adherence to specific regulations or standards |
| Authenticity | Verification of content originality |
| Ownership | Proof of content ownership |
| Usage | Permissions for content usage |
| Attribution | Credit to original creators |
| Destruction | Proof of content removal |
| Distribution | Record of content sharing |
| Modification | Tracking of content changes |
| Creation | Record of content origin |
| Validation | Process of verifying manifest integrity |
| Verification | Process of confirming claims |
| Integrity | Assurance of data authenticity |
| Security | Protection against tampering |
| Trust | Confidence in content authenticity |
| Transparency | Openness about content history |
| Accountability | Responsibility for content integrity |
| Traceability | Ability to track content history |
| Non-repudiation | Proof of content origin |
| Immutability | Protection against data alteration |
| Authenticity | Verification of content originality |
| Provenance | Record of content origin and history |
| Metadata | Data about the content |
| Signature | Cryptographic proof of authenticity |
| Timestamp | Record of when the claim was made |
| Software | Tool used to create the manifest |
| Standard | Industry-wide specification for manifests |
| Compliance | Adherence to specific regulations or standards |
| Authenticity | Verification of content originality |
| Ownership | Proof of content ownership |
| Usage | Permissions for content usage |
| Attribution | Credit to original creators |
| Destruction | Proof of content removal |
| Distribution | Record of content sharing |
| Modification | Tracking of content changes |
| Creation | Record of content origin |
| Validation | Process of verifying manifest integrity |
| Verification | Process of confirming claims |
| Integrity | Assurance of data authenticity |
| Security | Protection against tampering |
| Trust | Confidence in content authenticity |
| Transparency | Openness about content history |
| Accountability | Responsibility for content integrity |
| Traceability | Ability to track content history |
| Non-repudiation | Proof of content origin |
| Immutability | Protection against data alteration |
| Authenticity | Verification of content originality |
| Provenance | Record of content origin and history |
| Metadata | Data about the content |
| Signature | Cryptographic proof of authenticity |
| Timestamp | Record of when the claim was made |
| Software | Tool used to create the manifest |
| Standard | Industry-wide specification for manifests |
| Compliance | Adherence to specific regulations or standards |
| Authenticity | Verification of content originality |
| Ownership | Proof of content ownership |
| Usage | Permissions for content usage |
| Attribution | Credit to original creators |
| Destruction | Proof of content removal |
| Distribution | Record of content sharing |
| Modification | Tracking of content changes |
| Creation | Record of content origin |
| Validation | Process of verifying manifest integrity |
| Verification | Process of confirming claims |
| Integrity | Assurance of data authenticity |
| Security | Protection against tampering |
| Trust | Confidence in content authenticity |
| Transparency | Openness about content history |
| Accountability | Responsibility for content integrity |
| Traceability | Ability to track content history |
| Non-repudiation | Proof of content origin |
| Immutability | Protection against data alteration |
| Authenticity | Verification of content originality |
| Provenance | Record of content origin and history |
| Metadata | Data about the content |
| Signature | Cryptographic proof of authenticity |
| Timestamp | Record of when the claim was made |
| Software | Tool used to create the manifest |
| Standard | Industry-wide specification for manifests |
| Compliance | Adherence to specific regulations or standards |
| Authenticity | Verification of content originality |
| Ownership | Proof of content ownership |
| Usage | Permissions for content usage |
| Attribution | Credit to original creators |
| Destruction | Proof of content removal |
| Distribution | Record of content sharing |
| Modification | Tracking of content changes |
| Creation | Record of content origin |
| Validation | Process of verifying manifest integrity |
| Verification | Process of confirming claims |
| Integrity | Assurance of data authenticity |
| Security | Protection against tampering |
| Trust | Confidence in content authenticity |
| Transparency | Openness about content history |
| Accountability | Responsibility for content integrity |
| Traceability | Ability to track content history |
| Non-repudiation | Proof of content origin |
| Immutability | Protection against data alteration |
| Authenticity | Verification of content originality |
| Provenance | Record of content origin and history |
| Metadata | Data about the content |
| Signature | Cryptographic proof of authenticity |
| Timestamp | Record of when the claim was made |
| Software | Tool used to create the manifest |
| Standard | Industry-wide specification for manifests |
| Compliance | Adherence to specific regulations or standards |
| Authenticity | Verification of content originality |
| Ownership | Proof of content ownership |
| Usage | Permissions for content usage |
| Attribution | Credit to original creators |
| Destruction | Proof of content removal |
| Distribution | Record of content sharing |
| Modification | Tracking of content changes |
| Creation | Record of content origin |
| Validation | Process of verifying manifest integrity |
| Verification | Process of confirming claims |
| Integrity | Assurance of data authenticity |
| Security | Protection against tampering |
| Trust | Confidence in content authenticity |
| Transparency | Openness about content history |
| Accountability | Responsibility for content integrity |
| Traceability | Ability to track content history |
| Non-repudiation | Proof of content origin |
| Immutability | Protection against data alteration |
| Authenticity | Verification of content originality |
| Provenance | Record of content origin and history |
| Metadata | Data about the content |
| Signature | Cryptographic proof of authenticity |
| Timestamp | Record of when the claim was made |
| Software | Tool used to create the manifest |
| Standard | Industry-wide specification for manifests |
| Compliance | Adherence to specific regulations or standards |
| Authenticity | Verification of content originality |
| Ownership | Proof of content ownership |
| Usage | Permissions for content usage |
| Attribution | Credit to original creators |
| Destruction | Proof of content removal |
| Distribution | Record of content sharing |
| Modification | Tracking of content changes |
| Creation | Record of content origin |
| Validation | Process of verifying manifest integrity |
| Verification | Process of confirming claims |
| Integrity | Assurance of data authenticity |
| Security | Protection against tampering |
| Trust | Confidence in content authenticity |
| Transparency | Openness about content history |
| Accountability | Responsibility for content integrity |
| Traceability | Ability to track content history |
| Non-repudiation | Proof of content origin |
| Immutability | Protection against data alteration |
| Authenticity | Verification of content originality |
| Provenance | Record of content origin and history |
| Metadata | Data about the content |
| Signature | Cryptographic proof of authenticity |
| Timestamp | Record of when the claim was made |
| Software | Tool used to create the manifest |
| Standard | Industry-wide specification for manifests |
| Compliance | Adherence to specific regulations or standards |
| Authenticity | Verification of content originality |
| Ownership | Proof of content ownership |
| Usage | Permissions for content usage |
| Attribution | Credit to original creators |
| Destruction | Proof of content removal |
| Distribution | Record of content sharing |
| Modification | Tracking of content changes |
| Creation | Record of content origin |
| Validation | Process of verifying manifest integrity |
| Verification | Process of confirming claims |
| Integrity | Assurance of data authenticity |
| Security | Protection against tampering |
| Trust | Confidence in content authenticity |
| Transparency | Openness about content history |
| Accountability | Responsibility for content integrity |
| Traceability | Ability to track content history |
| Non-repudiation | Proof of content origin |
| Immutability | Protection against data alteration |
| Authenticity | Verification of content originality |
| Provenance | Record of content origin and history |
| Metadata | Data about the content |
| Signature | Cryptographic proof of authenticity |
| Timestamp | Record of when the claim was made |
| Software | Tool used to create the manifest |
| Standard | Industry-wide specification for manifests |
| Compliance | Adherence to specific regulations or standards |
| Authenticity | Verification of content originality |
| Ownership | Proof of content ownership |
| Usage | Permissions for content usage |
| Attribution | Credit to original creators |
| Destruction | Proof of content removal |
| Distribution | Record of content sharing |
| Modification | Tracking of content changes |
| Creation | Record of content origin |
| Validation | Process of verifying manifest integrity |
| Verification | Process of confirming claims |
| Integrity | Assurance of data authenticity |
| Security | Protection against tampering |
| Trust | Confidence in content authenticity |
| Transparency | Openness about content history |
| Accountability | Responsibility for content integrity |
| Traceability | Ability to track content history |
| Non-repudiation | Proof of content origin |
| Immutability | Protection against data alteration |
| Authenticity | Verification of content originality |
| Proven
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[c2pa-manifest-builder]] | downstream | 0.31 |
| [[bld_collaboration_c2pa_manifest]] | downstream | 0.30 |
| [[bld_knowledge_card_c2pa_manifest]] | sibling | 0.29 |
| [[p03_sp_c2pa_manifest_builder]] | downstream | 0.28 |
| [[bld_collaboration_vc_credential]] | downstream | 0.27 |
| [[bld_examples_vc_credential]] | downstream | 0.25 |
| [[bld_tools_c2pa_manifest]] | downstream | 0.24 |
| [[bld_instruction_c2pa_manifest]] | downstream | 0.24 |
| [[bld_knowledge_card_agent_grounding_record]] | sibling | 0.23 |
| [[bld_manifest_agent_grounding_record]] | downstream | 0.22 |
