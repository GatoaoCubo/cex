---
# TEMPLATE: Path Config (P09 Config)
# Valide contra P09_config/_schema.yaml (types.path_config)
# Max 3072 bytes

id: p09_path_{{SCOPE_SLUG}}
type: path_config
lp: P09
title: "Path Config: {{SCOPE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Path Config: {{SCOPE_NAME}}

## Paths
```yaml
root: {{ROOT_PATH}}
input: {{INPUT_PATH}}
output: {{OUTPUT_PATH}}
temp: {{TEMP_PATH}}
```

## Rules
- Writable: {{WRITABLE_RULE}}
- Relative base: {{RELATIVE_BASE_RULE}}
- Cleanup: {{CLEANUP_RULE}}
