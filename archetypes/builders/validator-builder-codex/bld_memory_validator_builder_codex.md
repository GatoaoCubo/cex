---
kind: memory
id: bld_memory_validator_builder_codex
pillar: P10
llm_function: REMEMBER
purpose: Persistent heuristics for validator-builder-codex
pattern: store reusable validator authoring rules and anti-patterns
---

# Memory: validator-builder-codex
## Stable Heuristics
- If a rule needs weights or score thresholds, it is probably `quality_gate`
- If a rule constrains decoder output tokens, it is probably `grammar`
- If the artifact explains fields broadly, it is probably `input_schema`
- Prefer one failure reason per check row; split compound logic when noisy
## Common Mistakes
- subjective wording: "clean", "good", "strong"
- missing trigger or severity
- examples that do not actually exercise the rule
- anti-examples drifting into policy or workflow steps
## Reusable Pattern
Target -> Condition -> Checks -> Errors -> PASS/FAIL examples
