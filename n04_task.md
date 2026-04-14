---
mission: WAVE7
nucleus: n04
wave: identity-provenance
created: 2026-04-14
model: claude-opus-4-6
---

# N04 -- Build 3 identity/provenance kinds (39 ISOs): W3C VC + C2PA + RO-Crate

## Your kinds (verifiable knowledge / content provenance)

1. **vc_credential** (P10/CONSTRAIN, max 4096B) -- W3C Verifiable Credentials 2.0 (May 2025 REC). Issuer, subject, claims, proof (data integrity), credentialSchema, credentialStatus, refreshService. DID-based issuer identity. Growing 144:1 machine:human issuance ratio.

2. **c2pa_manifest** (P10/CONSTRAIN, max 4096B) -- C2PA 2.3 content credentials (Adobe+Nikon+Canon+MS adoption). Claim + assertion + ingredient + thumbnail + signature. AI-ML generator attribution assertion (training data, model, prompt). Consolidates 8 C2PA sub-objects into one kind.

3. **workflow_run_crate** (P10/PRODUCE, max 5120B) -- RO-Crate 1.2 Workflow Run Crate (stable, scientific/Galaxy). Research object metadata: workflow, input dataset, output dataset, provenance graph, software environment, author ORCIDs, license.

## Gold template to clone

Read ALL 13 files in `archetypes/builders/partner-listing-builder/`. Clone SHAPE.

## Required ISOs per kind (13 each = 39 total)

Same 13-ISO structure in `archetypes/builders/{kind}-builder/`.

## Domain keywords (validator check)

- **vc_credential**: W3C, verifiable-credential, VC-2.0, DID, issuer, subject, proof, data-integrity, credentialSchema, refreshService
- **c2pa_manifest**: C2PA, content-credential, claim, assertion, ingredient, signature, thumbnail, AI-ML-generator, Adobe, provenance
- **workflow_run_crate**: RO-Crate, workflow-run, research-object, provenance-graph, ORCID, Galaxy, input-dataset, output-dataset, metadata

## 8F protocol

1. Read partner-listing-builder/ (gold)
2. Read kinds_meta.json (add 3 kinds)
3. Read N01_intelligence/research/ai2ai_exhaustive_scan_20260414.md (W3C VC / C2PA / RO-Crate sections)
4. For each kind x 13 ISOs: clone gold, inject identity/provenance content
5. Compile + Validate + Fix FAILs
6. Commit: `git add archetypes/builders/{vc-credential,c2pa-manifest,workflow-run-crate}-builder/ && git commit -m "[N04] WAVE7: 3 identity/provenance kinds (39 ISOs) -- W3C-VC+C2PA+RO-Crate"`

## ON COMPLETION

```
python -c "from _tools.signal_writer import write_signal; write_signal('n04', 'complete', 9.0)"
```
