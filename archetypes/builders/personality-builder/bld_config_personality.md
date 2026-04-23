---
quality: 8.2
quality: 7.6
kind: config
id: bld_config_personality
pillar: P09
llm_function: CONSTRAIN
purpose: Configuration knobs for personality artifact production
title: "Config: personality-builder"
version: "1.0.0"
author: n03_builder
tags: [personality, builder, config, P09, hermes_origin, hot_swap]
tldr: "Config knobs for personality-builder: tone presets, verbosity defaults, humor defaults, anti-pattern strictness."
domain: "persona construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.87
related:
  - brand_override_config
  - ex_feedback_tone_correction
  - bld_collaboration_quality_gate
---

# Config: personality-builder

## Builder Configuration

| Knob | Default | Options | Notes |
|------|---------|---------|-------|
| default_register | casual | formal, casual, technical, playful | Applied when user omits register |
| default_verbosity | balanced | terse, balanced, verbose | Applied when user omits verbosity |
| default_humor | off | off, dry, warm | Applied when user omits humor |
| min_tone_examples | 3 | 1-10 | Hard minimum; gate H07 enforces this |
| min_anti_patterns | 3 | 1-10 | Hard minimum; gate H08 enforces this |
| min_values | 3 | 1-5 | Hard minimum; gate H09 enforces this |
| max_values | 5 | 3-10 | Hard max; prevents contradiction |
| max_bytes | 3072 | 1024-8192 | Override for extended personas |
| hot_swap_default | true | true, false | Default for hot_swap_compatible |
| version | 1.0.0 | semver | Starting version for new artifacts |

## Tone Preset Shortcuts

| Preset | register | verbosity | humor |
|--------|----------|-----------|-------|
| academic | technical | verbose | dry |
| support | casual | balanced | warm |
| executive | formal | terse | off |
| dev | technical | terse | dry |
| teacher | casual | verbose | warm |
| creative | playful | balanced | warm |

## Quality Gate Settings

| Setting | Value |
|---------|-------|
| score_threshold_publish | 8.0 |
| score_threshold_golden | 9.5 |
| density_target | 0.85 |
| hard_gate_count | 10 |
| retry_on_fail | true |
| max_retries | 2 |

## Anti-Pattern Strictness Levels

| Level | Behavior |
|-------|----------|
| strict | Must be mutually exclusive from tone_examples; reviewer checks for contradiction |
| standard | Anti-patterns are validated as non-empty and >= 3; no cross-check with tone_examples |
| relaxed | Anti-patterns present but content not validated |

Default: standard

## Configuration Checklist

- Verify all required fields are present in frontmatter before saving
- Validate config values against schema constraints (type, range, enum)
- Cross-reference with related configs to avoid contradictions
- Test config loading in target runtime before committing

## Validation

```yaml
# Required config validation
fields_present: true
types_valid: true
ranges_checked: true
cross_refs_verified: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[brand_override_config]] | related | 0.17 |
| [[ex_feedback_tone_correction]] | downstream | 0.16 |
| [[bld_collaboration_quality_gate]] | downstream | 0.15 |
