---
mission: HYBRID_REVIEW3
nucleus: n03
wave: review
created: 2026-04-13
model: claude-opus-4-6
source_model: gemma4:26b (Wave 2 ML kinds)
---

# N03 -- Audit dataset_card + experiment_tracker (26 ISOs)

## Your kinds
1. dataset_card -- archetypes/builders/dataset-card-builder/ (13 ISOs)
2. experiment_tracker -- archetypes/builders/experiment-tracker-builder/ (13 ISOs)

## Pre-flight check

```bash
ls archetypes/builders/dataset-card-builder/ | grep -c bld_
ls archetypes/builders/experiment-tracker-builder/ | grep -c bld_
```
Both should return 13. If either is < 13, Wave 2 incomplete -- wait.

## Review protocol

### Step 1: Load systemic defects reference
Read `N01_intelligence/reports/master_systemic_defects.md` first.
As Builder nucleus, you are authoritative on construction quality.
Pay particular attention to: D01 (llm_function), D05 (quality null), D07 (fabricated tools),
D08 (output_template), D09 (architecture ISO), D10 (file reference drift), D11 (soft weights).

### Step 2: Per-kind audit

Open all 13 ISOs per kind and score 5D:
- D1 Structural completeness (all required bld_* files present, correct naming)
- D2 Domain accuracy (content is authoritative on its subject area)
- D3 Density (>= 0.85)
- D4 CEX compliance (8F integration, quality: null in schema, correct llm_function)
- D5 Industry alignment (terminology matches authoritative sources below)

**Score thresholds:**
- >= 8.0: leave
- 6.0-7.9: surgical fix
- < 6.0: rebuild via 8F pipeline

### Step 3: Industry citations to verify

**dataset_card:**
- HuggingFace Dataset Cards spec: dataset_info.yaml, splits, features, license
- Croissant format (ML Commons): structured metadata for ML datasets
- Data cards framework (Google): provenance, collection methodology, known limitations
- Datasheets for Datasets (Gebru et al.): motivation, composition, collection, preprocessing
- PII handling: sensitivity labels, consent, anonymization method
- GDPR/CCPA compliance fields: data origin country, retention policy
- Key fields: dataset_name, source, license, size, splits, features, intended_use, limitations, bias_notes

**experiment_tracker:**
- MLflow: run_id, experiment_name, params, metrics, artifacts, tags
- Weights & Biases (W&B): project, entity, run, sweep, artifacts versioning
- Neptune.ai: experiment, run, series, namespace, metadata
- Comet ML: experiment key, workspace, project, logged assets
- TensorBoard: scalar, histogram, image, graph, hparams
- DVC (Data Version Control): pipeline stages, params.yaml, metrics.json
- Key fields: experiment_id, model_version, hyperparameters, metrics_schema, dataset_ref, environment

### Step 4: Known gemma4 contamination to detect

1. D01: bld_system_prompt llm_function=INJECT instead of BECOME
2. D04: Domain hallucination -- financial portfolio tracking in experiment_tracker, trading datasets in dataset_card
3. D07: Fabricated tools (bld_tools should reference real cex tools, not made-up MLflow wrappers)
4. D08: Bare {{placeholders}} in output_template (e.g., {{dataset_description}} without guidance)
5. D09: bld_architecture describes data pipeline architecture, not the 13-ISO builder structure
6. D05: quality: 9.0 or other non-null values in bld_schema frontmatter
7. D10: File references to SCHEMA.md instead of bld_schema_{kind}.md
8. D11: SOFT gate weights that do not sum to 1.00 in quality_gate ISO

### Step 5: Fix or rebuild

Surgical fixes: target only defective ISOs, log each change.
Rebuilds: run 8F fully. Load the dataset-card-builder or experiment-tracker-builder ISOs as spec.
For D01 (most common): change llm_function: INJECT -> llm_function: BECOME in bld_system_prompt.

### Step 6: Validate

```bash
python _tools/cex_wave_validator.py --scope archetypes/builders/dataset-card-builder/
python _tools/cex_wave_validator.py --scope archetypes/builders/experiment-tracker-builder/
```

### Step 7: Write audit reports

1. `N03_engineering/audits/hybrid_review3_n03_dc.md` -- dataset_card audit
2. `N03_engineering/audits/hybrid_review3_n03_et.md` -- experiment_tracker audit
3. `N03_engineering/audits/hybrid_review3_n03.md` -- master summary

Frontmatter template:
```yaml
---
id: hybrid_review3_n03
kind: knowledge_card
pillar: P01
title: "HYBRID_REVIEW3 Audit: dataset_card + experiment_tracker (N03)"
version: 1.0.0
quality: null
tags: [audit, hybrid_review3, dataset_card, experiment_tracker, gemma4, wave2]
domain: data engineering quality assurance
created: "2026-04-13"
---
```

## Context (pre-loaded)

- Master defects: `N01_intelligence/reports/master_systemic_defects.md`
- Gold standard builder: `archetypes/builders/knowledge-card-builder/`
- Your prior audits: `N03_engineering/audits/hybrid_review2_n03.md`, `N03_engineering/audits/hybrid_review_n03.md`
- Builder spec: `archetypes/builders/dataset-card-builder/` (the builder-of-builders pattern applies)

## Commit

```bash
git add archetypes/builders/dataset-card-builder/ \
        archetypes/builders/experiment-tracker-builder/ \
        N03_engineering/audits/hybrid_review3_n03*.md
git commit -m "[N03] HYBRID_REVIEW3: audit+fix dataset_card + experiment_tracker (26 ISOs)"
```

## ON COMPLETION

```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'complete', 9.0)"
```
