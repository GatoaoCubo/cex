---
id: config_governance_rules
kind: config
pillar: P09
nucleus: N07
title: Governance Configuration
references: [ex_env_config_default, ex_validation_rule_density, quality_gate_deploy]
---
# Governance Configuration
| Rule | Value | Enforced by |
|------|-------|------------|
| Naming | v2.0 strict | pre-commit hook |
| Density | >= 0.80 | [[ex_validation_rule_density]] |
| Quality | >= 8.0 | [[quality_gate_deploy]] |
| Max size | per-kind (_schema.yaml) | pre-commit hook |
Defaults: [[ex_env_config_default]]
