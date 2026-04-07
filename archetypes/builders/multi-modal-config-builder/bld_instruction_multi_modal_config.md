---
kind: instruction
id: bld_instruction_multi_modal_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for multi_modal_config
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a multi_modal_config
## Phase 1: RESEARCH
1. Identify target use case: what non-text inputs need processing?
2. Determine supported modalities: image, audio, video, document?
3. Survey target model capabilities: which models handle which modalities natively?
4. Assess volume/cost: how many images per request? Audio duration?
5. Check existing configs to avoid duplicates
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill the template
3. Define supported_modalities list
4. Set per-modality constraints: image resolution, audio duration, video duration
5. Define preprocessing pipeline per modality (resize, compress, transcribe)
6. Create routing_model map: modality → best model
7. Estimate token costs per modality
8. Define fallback chain for unsupported modalities
9. Set quality: null
10. Keep file under 2048 bytes
## Phase 3: VALIDATE
1. Verify supported_modalities contains valid enum values
2. Check format constraints present for each modality
3. Verify routing_model maps to real models
4. Check token_cost_estimate is populated
5. Verify id matches `p04_mmc_[a-z][a-z0-9_]+`
6. Check total file under 2048 bytes
7. If any gate fails: fix and re-validate
