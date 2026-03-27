---
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for unit_eval production
pattern: CONFIG restricts SCHEMA, never contradicts
---

# Config: unit_eval Production Rules

## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p07_ue_{target_slug}.md | p07_ue_kc_yaml_parse.md |
| Compiled | p07_ue_{target_slug}.yaml | p07_ue_kc_yaml_parse.yaml |
| Builder dir | kebab-case | unit-eval-builder/ |
| Fields | snake_case | target_kind, expected_output |

Rule: id MUST equal filename stem.

## File Paths
- Output: cex/P07_evals/p07_ue_{target_slug}.md
- Compiled: cex/P07_evals/compiled/p07_ue_{target_slug}.yaml

## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Density: >= 0.80
- Timeout: default 60s, max 300s for unit scope

## Assertion Policy
- Minimum 1 assertion per unit_eval
- Each assertion MUST reference a gate_ref from target builder
- Severity must be HARD or SOFT (no custom levels)
