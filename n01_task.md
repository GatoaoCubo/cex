---
mission: WAVE7
nucleus: n01
wave: governance
created: 2026-04-14
model: claude-opus-4-6
---

# N01 -- Build 3 governance kinds (39 ISOs): NIST + EU AI Act + AILuminate

## Your kinds (AI governance / compliance research docs)

1. **ai_rmf_profile** (P11/GOVERN, max 5120B) -- NIST AI 600-1 GenAI profile; 4 functions (GOVERN/MAP/MEASURE/MANAGE), 13 risk categories, action mappings per risk. US federal + enterprise mandate.

2. **gpai_technical_doc** (P11/GOVERN, max 5120B) -- EU AI Act GPAI technical documentation (Aug 2025 active law); training data summary, compute budget, energy consumption, evaluation results, intended purpose, downstream integration limits.

3. **safety_hazard_taxonomy** (P11/GOVERN, max 5120B) -- MLCommons AILuminate v1.0 hazard taxonomy aligned with Llama Guard 4; 12 hazard categories (violence/sexual/CBRN/...) + severity levels + response templates.

## Gold template to clone

Read ALL 13 files in `archetypes/builders/partner-listing-builder/`. Copy SHAPE, replace with governance content.

## Required ISOs per kind (13 each = 39 total)

Clone the 13-ISO structure into `archetypes/builders/{kind}-builder/`:
bld_manifest, bld_instruction, bld_system_prompt, bld_knowledge_card, bld_example,
bld_schema_yaml, bld_scoring_rubric, bld_skill_f6_produce, bld_few_shot, bld_test_input,
bld_golden_output, bld_validator, bld_readme.

## Domain keywords (validator check)

- **ai_rmf_profile**: NIST, AI-RMF, GOVERN, MAP, MEASURE, MANAGE, GenAI-profile, 600-1, action-ID, risk-category
- **gpai_technical_doc**: GPAI, EU-AI-Act, Annex-IV, Article-53, training-data, compute-budget, downstream-limit, technical-documentation
- **safety_hazard_taxonomy**: MLCommons, AILuminate, Llama-Guard, hazard-category, CBRN, severity-level, response-template, taxonomy

## 8F protocol

1. Read partner-listing-builder/ (gold)
2. Read kinds_meta.json entries (may need to ADD these 3 kinds first)
3. Read N01_intelligence/research/ai2ai_exhaustive_scan_20260414.md (citations for the 3 standards)
4. For each kind x 13 ISOs: adapt gold, inject governance-specific content
5. Compile: `python _tools/cex_compile.py archetypes/builders/{kind}-builder/`
6. Validate: `python _tools/cex_wave_validator.py --scope archetypes/builders/{kind}-builder/`
7. Fix FAILs
8. Commit: `git add archetypes/builders/{ai-rmf-profile,gpai-technical-doc,safety-hazard-taxonomy}-builder/ && git commit -m "[N01] WAVE7: 3 governance kinds (39 ISOs) -- NIST+EU-AI-Act+AILuminate"`

## ON COMPLETION

```
python -c "from _tools.signal_writer import write_signal; write_signal('n01', 'complete', 9.0)"
```
