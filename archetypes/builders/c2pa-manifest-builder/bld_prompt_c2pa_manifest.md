---
kind: instruction
id: bld_instruction_c2pa_manifest
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for c2pa_manifest
quality: 8.9
title: "Instruction C2PA Manifest"
version: "1.0.0"
author: n04_wave7
tags: [c2pa_manifest, builder, instruction, C2PA, claim, assertion, ingredient, signature]
tldr: "Step-by-step production process for c2pa_manifest"
domain: "c2pa_manifest construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_knowledge_card_c2pa_manifest
  - c2pa-manifest-builder
  - p03_sp_c2pa_manifest_builder
  - bld_examples_c2pa_manifest
  - bld_output_template_c2pa_manifest
  - p10_lr_c2pa_manifest_builder
  - p10_qg_c2pa_manifest
  - bld_tools_c2pa_manifest
  - bld_schema_c2pa_manifest
  - bld_architecture_c2pa_manifest
---

## Phase 1: RESEARCH
1. Identify content type: image (JPEG/PNG/AVIF), audio (MP3/WAV), video (MP4), or document (PDF).
2. Determine AI-ML generator details: model name, version, provider, training data references.
3. Identify ingredient sources: base image, prompt text, model artifact, reference assets.
4. Select digital source type: trainedAlgorithmicMedia (AI-generated) or compositeSynthetic (mixed).
5. Identify signer certificate: X.509 from C2PA-trusted CA or DID-based signer.
6. Determine assertion set: c2pa.ai_generator (required), c2pa.training-mining (if applicable), c2pa.ingredient (for source references).

## Phase 2: COMPOSE
1. Reference SCHEMA.md for C2PA manifest structure (manifest_store, active_manifest, claim, assertions).
2. Set manifest JUMBF box structure: manifest store -> manifest -> claim -> assertions.
3. Populate claim: dc:format, ingredients array, assertions array, signature reference.
4. Add c2pa.ai_generator assertion: digitalSourceType, generatorModel (name, version), promptText.
5. Add ingredient assertions for each source: title, format, relationship, thumbnail_hash.
6. Add c2pa.training-mining assertion if training data is referenced: dataType, source URIs.
7. Generate thumbnail with SHA-256 hash for content binding.
8. Sign manifest with COSE_Sign1 using signer certificate/DID key.
9. Embed manifest in content file (JPEG Exif/APP11, MP4 moov box, PDF xpacket).

## Phase 3: VALIDATE
- [ ] claim.dc:format matches actual content MIME type
- [ ] c2pa.ai_generator assertion present with digitalSourceType
- [ ] All ingredient hashes verified against actual files
- [ ] Signature chain validates to trusted C2PA certificate store
- [ ] Manifest size within JUMBF box limits
- [ ] Domain keywords present: C2PA, content-credential, claim, assertion, ingredient, signature


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_c2pa_manifest]] | upstream | 0.58 |
| [[c2pa-manifest-builder]] | downstream | 0.58 |
| [[p03_sp_c2pa_manifest_builder]] | related | 0.56 |
| [[bld_examples_c2pa_manifest]] | downstream | 0.47 |
| [[bld_output_template_c2pa_manifest]] | downstream | 0.46 |
| [[p10_lr_c2pa_manifest_builder]] | downstream | 0.45 |
| [[p10_qg_c2pa_manifest]] | downstream | 0.44 |
| [[bld_tools_c2pa_manifest]] | downstream | 0.39 |
| [[bld_schema_c2pa_manifest]] | downstream | 0.37 |
| [[bld_architecture_c2pa_manifest]] | downstream | 0.33 |
