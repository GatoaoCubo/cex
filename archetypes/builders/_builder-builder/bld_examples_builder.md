---
kind: examples
id: bld_examples_builder
pillar: P03
llm_function: INJECT
purpose: Reference examples of well-built builders
---
# Examples: _builder-builder

## Example 1: Minimal Skeleton Builder
Builder: `memory-scope-builder` (13 files, 24KB)
- Created via Validation Registry spec
- Skeleton pattern: minimal content per ISO
- All universal fields present
- Doctor: PASS, 0 WARN

## Example 2: Full-Featured Builder
Builder: `agent-builder` (13 files, 42KB)
- Full content in all ISOs
- 212 crew compositions in bld_collaboration
- Non-default overrides: effort=high, permission_scope=pillar
- Doctor: PASS, 0 WARN

## Example 3: Domain-Specific Builder
Builder: `content-monetization-builder` (13 files, 45KB)
- Hotmart + Digistore24 parity in tools
- Platform-specific quality gates
- effort=high, permission_scope=nucleus
- Doctor: PASS, 0 WARN

## Anti-Example: Missing Universal Fields
❌ Builder without keywords in manifest → doctor WARN
❌ Builder without memory_scope → hydration required
❌ Builder with effort but no model mapping → runtime failure
