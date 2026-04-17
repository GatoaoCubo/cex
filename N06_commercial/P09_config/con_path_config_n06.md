---
id: con_path_config_n06
kind: path_config
pillar: P09
nucleus: n06
title: Commercial Path Config
version: 1.0
quality: null
tags: [config, path, pricing, assets, audit]
---

<!-- 8F: F1 constrain=P09/path_config F2 become=path-config-builder F3 inject=nucleus_def_n06.md,n06-commercial.md,bld_manifest_path_config.md,kc_path_config.md,P09_config/_schema.yaml F4 reason=bounded_paths_for_commercial_assets_and_revenue_audit_trails F5 call=apply_patch;python _tools/cex_compile.py F6 produce=5121_bytes F7 govern=frontmatter_sections_ascii_density_review F8 collaborate=N06_commercial/config/con_path_config_n06.md -->

# Commercial Path Config

## Purpose

| Field | Value |
|-------|-------|
| Goal | Define the filesystem paths N06 uses for pricing inputs, offer assets, compiled outputs, and commercial audit evidence |
| Business Lens | Strategic Greed treats paths as revenue infrastructure; high-value assets must be easy to find and hard to corrupt |
| Primary Use | Keep commercial artifacts discoverable, bounded, and separated by value risk |
| Failure Prevented | overwrite of offer assets, mixed staging/prod evidence, and hidden revenue diagnostics |
| Base Strategy | anchor all paths to repo root |
| Readonly Bias | source templates stay read-only, generated revenue evidence stays write-only |

## Values

| Alias | Relative Path | Mode | Required | Why |
|-------|---------------|------|----------|-----|
| repo_root | `.` | read | yes | anchor for all commercial paths |
| pricing_output | `N06_commercial/output` | read_write | yes | finalized monetization artifacts |
| pricing_schema | `N06_commercial/schemas` | read_write | yes | typed contracts |
| pricing_config | `N06_commercial/config` | read_write | yes | runtime commercial config |
| pricing_knowledge | `N06_commercial/knowledge` | read | yes | commercial references |
| pricing_compiled | `N06_commercial/compiled` | read_write | yes | compiled machine output |
| offer_templates | `examples` | read | no | reusable pattern samples |
| signal_outbox | `.cex_signals` | read_write | no | completion and health signals |
| runtime_handoffs | `.cex/runtime/handoffs` | read | yes | upstream task source |
| audit_reports | `_reports` | read_write | no | monetization diagnostics and comparisons |
| payment_docs | `_docs` | read | no | policy and operational notes |

## Readonly Set

| Path Alias | Rule | Commercial Reason |
|------------|------|-------------------|
| pricing_knowledge | read-only | historical market logic should not be rewritten casually |
| offer_templates | read-only | examples guide offers and must stay stable |
| runtime_handoffs | read-only | execution intent should not be mutated by downstream work |
| payment_docs | read-only | policy docs are reference material, not scratch space |

## Resolution Rules

| Rule ID | Rule | Effect |
|---------|------|--------|
| PC01 | all paths resolve under repo_root | prevents accidental writes outside workspace |
| PC02 | no absolute user-specific path literals | keeps config portable across machines |
| PC03 | compiled output mirrors artifact basename | compile step remains deterministic |
| PC04 | report paths include date when mutable | preserves audit history |
| PC05 | secret material paths are excluded here | secret storage belongs in secret config, not path config |

## Rationale

| Design Choice | Why It Exists | Strategic Greed Impact |
|---------------|---------------|------------------------|
| Separate compiled directory | generated output should not pollute authoring surface | keeps revenue contracts clean and machine-ready |
| Read-only knowledge and templates | source guidance is a leverage asset | protects monetization playbooks from casual damage |
| Audit reports path | profit decisions need historical evidence | makes pricing wins and losses comparable |
| Handoffs remain read-only | commercial execution should respect upstream constraints | prevents silent mission drift |
| No secret file path here | secret sprawl becomes a breach vector | keeps credential handling isolated |

## Example

| Scenario | Resolution |
|----------|------------|
| Compile `con_rate_limit_config_n06.md` | output should land under `N06_commercial/compiled` with matching basename |
| Generate a monetization review report | file should land under `_reports` with dated suffix |

```yaml
base_dir: .
paths:
  pricing_output: N06_commercial/output
  pricing_schema: N06_commercial/schemas
  pricing_config: N06_commercial/config
  pricing_compiled: N06_commercial/compiled
  audit_reports: _reports
readonly:
  - N06_commercial/knowledge
  - examples
  - .cex/runtime/handoffs
  - _docs
```

## Properties

| Property | Value |
|----------|-------|
| Owner | N06 Commercial |
| Base Dir | `.` |
| Alias Count | 11 |
| Readonly Count | 4 |
| Portability Rule | no absolute user paths |
| Audit Rule | dated reports for mutable evidence |
| Secret Boundary | handled elsewhere |
| Commercial Bias | protect leverage assets, preserve evidence |
| Primary Consumers | compile flow, review flow, monetization ops |
| Related Pillars | P06, P09, P12 |
