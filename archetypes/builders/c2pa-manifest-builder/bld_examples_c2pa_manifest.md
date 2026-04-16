---
kind: examples
id: bld_examples_c2pa_manifest
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of c2pa_manifest artifacts
quality: 8.9
title: "Examples C2PA Manifest"
version: "1.0.0"
author: n04_wave7
tags: [c2pa_manifest, builder, examples, C2PA, AI-ML-generator, claim, assertion]
tldr: "Golden and anti-examples of c2pa_manifest artifacts"
domain: "c2pa_manifest construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```json
{
  "manifests": {
    "cex:firefly-campaign-banner": {
      "claim_generator": "CEX-N02-Marketing/1.0 c2pa-rs/0.36",
      "title": "Black Friday Campaign Banner 2026",
      "format": "image/jpeg",
      "instance_id": "xmp:iid:f3a9b2c1-d4e5-4f6a-8b7c-9d0e1f2a3b4c",
      "ingredients": [],
      "assertions": [
        {
          "label": "c2pa.ai_generator",
          "data": {
            "digitalSourceType": "trainedAlgorithmicMedia",
            "generatorModel": {
              "name": "Adobe Firefly",
              "version": "3.0"
            },
            "promptText": "Black Friday sale banner, dark background, gold typography, shopping bags, 4K"
          }
        },
        {
          "label": "c2pa.training-mining",
          "data": {
            "dataType": "trainedAlgorithmicMedia",
            "entries": [
              {"uri": "https://firefly.adobe.com/training-data-manifest", "alg": "sha256", "hash": "a1b2c3..."}
            ]
          }
        }
      ],
      "signature_info": {
        "issuer": "Adobe Inc.",
        "cert_serial_number": "0x1234ABCD"
      }
    }
  },
  "active_manifest": "cex:firefly-campaign-banner"
}
```

## Anti-Example 1: Missing AI Generator Assertion
```json
{
  "manifests": {
    "unknown:manifest": {
      "title": "Generated Image",
      "format": "image/png",
      "assertions": []
    }
  }
}
```
**Why it fails**: No c2pa.ai_generator assertion. C2PA 2.2+ requires AI-ML generator attribution for AI-generated content. Empty assertions array provides no provenance information to content consumers or auditors.

## Anti-Example 2: Missing Ingredient Hashes
```json
{
  "assertions": [
    {
      "label": "c2pa.ingredient",
      "data": {
        "title": "Source Image",
        "relationship": "parentOf"
      }
    }
  ]
}
```
**Why it fails**: Ingredient assertion without content hash. Without SHA-256 hash binding the ingredient reference to actual file content, the provenance chain is unverifiable and can be spoofed.

## Anti-Example 3: Non-IANA MIME Type
```json
{"format": "jpg"}
```
**Why it fails**: "jpg" is not an IANA MIME type. Must be "image/jpeg". Invalid format breaks manifest parsing in all C2PA-compliant readers (Adobe, Nikon, Canon, Microsoft).
