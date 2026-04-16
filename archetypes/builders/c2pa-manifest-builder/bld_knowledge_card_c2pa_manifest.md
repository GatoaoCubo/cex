---
kind: knowledge_card
id: bld_knowledge_card_c2pa_manifest
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for c2pa_manifest production
quality: 9.2
title: "Knowledge Card C2PA Manifest"
version: "1.0.0"
author: n04_wave7
tags: [c2pa_manifest, builder, knowledge_card, C2PA, content-credential, claim, assertion, ingredient, signature, thumbnail, AI-ML-generator, Adobe, provenance]
tldr: "Domain knowledge for c2pa_manifest production"
domain: "c2pa_manifest construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Domain Overview
C2PA (Coalition for Content Provenance and Authenticity) 2.3 defines a technical standard for binding content provenance to digital media. Founded by Adobe, BBC, Intel, Microsoft, Nikon, and Sony, C2PA is the industry standard for content credentials. Version 2.3 adds Implementation Guidance for AI-ML specifics, with v2.4 adding further AI watermarking integration.

C2PA manifests answer: "Where did this content come from?" For AI-generated media, this means recording the AI model, prompt, training data references, and generation parameters. The manifest is cryptographically signed and embedded in the media file itself (JUMBF box), surviving format conversions and distribution.

## Key Concepts
| Concept | Definition | Source |
|---------|-----------|--------|
| C2PA Manifest | Signed provenance record embedded in or linked to media | C2PA 2.3 Spec |
| Claim | Core assertion set: format, ingredients, assertions array, signature ref | C2PA 2.3 Section 8 |
| Assertion | Named data record in claim (ai_generator, training-mining, ingredient) | C2PA 2.3 Section 9 |
| Ingredient | Referenced source media with content hash and relationship type | C2PA 2.3 Section 9.4 |
| JUMBF | ISO 19566-5 box format used to embed C2PA data in media files | ISO 19566-5 |
| COSE_Sign1 | CBOR Object Signing, single signature per C2PA claim | RFC 8152 |
| trainedAlgorithmicMedia | C2PA digital source type for AI-model-generated content | C2PA DST vocab |
| compositeSynthetic | C2PA digital source type for AI-composited content | C2PA DST vocab |
| c2pa.ai_generator | Assertion recording AI model, digital source type, prompt | C2PA 2.2+ AI guidance |
| c2pa.training-mining | Assertion recording training data references and policies | C2PA 2.3 Section 9.9 |

## C2PA Adoption (2025-2026)
| Platform | Integration | Notes |
|----------|------------|-------|
| Adobe Firefly | Native C2PA 2.3 | All outputs signed by default |
| Nikon Z-series | C2PA camera manifest | Hardware signing chip |
| Canon EOS | C2PA camera manifest | Certification program |
| Microsoft Designer | C2PA 2.3 | Azure content credentials |
| Midjourney | C2PA in progress | Announced 2025 |
| Content Credentials (CAI) | Verify.contentauthenticity.org | Public verification portal |

## Industry Standards
- C2PA Specification 2.3: https://spec.c2pa.org/specifications/specifications/2.3/
- ISO 19566-5 (JUMBF): Box format for embedded metadata
- RFC 8152 (COSE): Cryptographic signing format
- XMP (ISO 16684-1): Cross-format metadata embedding
- IPTC Photo Metadata Standard: Interoperability layer

## Common Patterns
1. GenAI platform workflow: generate content -> add c2pa.ai_generator assertion -> sign -> embed in JPEG.
2. Derivative content: original + AI upscale = new manifest with ingredient link to original C2PA manifest.
3. Multi-assertion manifest: ai_generator + training-mining + thumbnail for full provenance chain.
4. Hard binding: content hash in manifest; soft binding: XMP reference to external manifest.

## Pitfalls
- Missing c2pa.ai_generator assertion on AI-generated content (C2PA 2.2+ requirement).
- Using non-IANA MIME types in claim.format field (causes reader failure).
- Omitting ingredient hashes (makes provenance chain unverifiable).
- Embedding manifest after file compression (hash changes; must embed before final compress).
- Confusing hard binding (hash embedded) with soft binding (external reference only).
