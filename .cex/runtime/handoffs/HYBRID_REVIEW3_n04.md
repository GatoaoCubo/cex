---
mission: HYBRID_REVIEW3
nucleus: n04
wave: review
created: 2026-04-13
model: claude-opus-4-6
source_model: gemma4:26b (Wave 2 ML kinds)
---

# N04 -- Audit model_registry (13 ISOs)

## Your kind
1. model_registry -- archetypes/builders/model-registry-builder/ (13 ISOs)

## Pre-flight check

```bash
ls archetypes/builders/model-registry-builder/ | grep -c bld_
```
Should return 13. If < 13, Wave 2 is incomplete -- wait for gemma4 signal before proceeding.

## Review protocol

### Step 1: Load systemic defects reference
Read `N01_intelligence/reports/master_systemic_defects.md` first.
N04 domain is knowledge management and cataloging -- model_registry is a catalog/index artifact.
Check especially: D04 (domain hallucination), D07 (fabricated tools), D08 (bare placeholders),
D14 (empty config fields), D15 (generic collaboration tables).

### Step 2: Per-ISO audit (5D scoring)

Open all 13 ISOs and score:
- D1 Structural completeness (all bld_* files present, correct YAML frontmatter, no blank required fields)
- D2 Domain accuracy (content covers model versioning, metadata, deployment lineage -- not generic registries)
- D3 Density (>= 0.85, no repetition, no padding)
- D4 CEX compliance (8F correct, quality: null, llm_function: BECOME in bld_system_prompt)
- D5 Industry alignment (terminology matches MLflow, W&B, SageMaker, Vertex AI below)

**Score thresholds:**
- >= 8.0: leave
- 6.0-7.9: surgical fix
- < 6.0: rebuild

### Step 3: Industry citations to verify

**model_registry:**
- MLflow Model Registry: registered_model, model_version, stage (Staging/Production/Archived), alias, tag
- W&B Artifacts: artifact name, type, version, aliases (latest, best), lineage graph
- SageMaker Model Registry: model_package, model_package_group, approval_status, inference specs
- Vertex AI Model Registry: model resource, version, evaluation metrics, deployment config
- Hugging Face Hub: model card, model_id, safetensors, GGUF quantization variants
- Key fields: registry_name, model_name, model_version, base_model, training_dataset, eval_metrics, deployment_stage, lineage

**What the ISOs must cover correctly:**
- bld_schema: registry_url, model_id, version, stage, metrics, lineage_ref -- all present
- bld_instruction: how to create a registry entry that captures full model provenance
- bld_system_prompt: llm_function=BECOME (not INJECT)
- bld_tools: real CEX tools (cex_compile.py, cex_doctor.py), not fabricated MLflow Python SDK calls
- bld_examples: real-looking registry entries (mlflow-style or wandb-style), not synthetic placeholders

### Step 4: Known gemma4 contamination to detect

1. D01: bld_system_prompt llm_function=INJECT (most common defect)
2. D04: Financial model registry (portfolio models, trading models) contaminating ML model registry
3. D07: bld_tools references mlflow.register_model() or wandb.Artifact() directly -- should be CEX tools
4. D08: output_template with bare {{model_name}}, {{version}} without guidance on what to fill
5. D14: Empty config fields -- max_turns, effort_level left blank in bld_agent_config
6. D15: Collaboration tables reference generic "Knowledge Manager", "Data Engineer" instead of N01, N03, N04 nuclei

### Step 5: Fix or rebuild

For D01: change llm_function: INJECT -> llm_function: BECOME in bld_system_prompt.
For D04: replace financial domain examples with MLflow/SageMaker examples.
For D15: replace generic roles with actual CEX nuclei (N01 Research, N03 Build, N04 Knowledge).

### Step 6: Validate

```bash
python _tools/cex_wave_validator.py --scope archetypes/builders/model-registry-builder/
```
Fix any failures.

### Step 7: Write audit report

`N04_knowledge/audits/hybrid_review3_n04.md`

Frontmatter:
```yaml
---
id: hybrid_review3_n04
kind: knowledge_card
pillar: P01
title: "HYBRID_REVIEW3 Audit: model_registry (N04)"
version: 1.0.0
quality: null
tags: [audit, hybrid_review3, model_registry, gemma4, wave2]
domain: knowledge catalog quality assurance
created: "2026-04-13"
---
```

Report sections:
1. Scope (13 ISOs examined)
2. Defects found (vs D01-D15 taxonomy)
3. Fixes applied (per-ISO)
4. ISOs rebuilt (list + reason)
5. Final 5D scores per ISO
6. Remaining issues (if any)

## Context (pre-loaded)

- Master defects: `N01_intelligence/reports/master_systemic_defects.md`
- Gold standard builder: `archetypes/builders/knowledge-card-builder/` (reference for correct ISO structure)
- Prior N04 audits: `N04_knowledge/audits/hybrid_review2_n04.md`, `N04_knowledge/audits/hybrid_review_n04.md`
- CEX knowledge catalog patterns: `P10_memory/` (knowledge_index, entity_memory kinds)

## Commit

```bash
git add archetypes/builders/model-registry-builder/ \
        N04_knowledge/audits/hybrid_review3_n04.md
git commit -m "[N04] HYBRID_REVIEW3: audit+fix model_registry (13 ISOs)"
```

## ON COMPLETION

```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n04', 'complete', 9.0)"
```
