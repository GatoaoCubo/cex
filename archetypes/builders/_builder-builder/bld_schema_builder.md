---
kind: schema
id: bld_schema_builder
pillar: P06
llm_function: CONSTRAIN
purpose: Field definitions and constraints for builder artifacts
---
# Schema: _builder-builder

## Frontmatter Fields (per generated ISO)
| Field | Type | Required | Constraint |
|-------|------|----------|------------|
| id | string | yes | Must equal filename stem |
| kind | string | yes | Must match target kind |
| pillar | string | yes | P01-P12 |
| llm_function | enum | yes | CONSTRAIN/BECOME/INJECT/REASON/CALL/PRODUCE/GOVERN/COLLABORATE |
| purpose | string | yes | One-line description |

## Universal Fields (added by hydration)
| Field | ISO | Type | Default |
|-------|-----|------|---------|
| keywords | manifest | list[str] | 4-8 terms |
| triggers | manifest | list[str] | 2-4 phrases |
| geo_description | manifest | string | 3 layers L1/L2/L3 |
| memory_scope | memory | enum | project |
| observation_types | memory | list | [user,feedback,project,reference] |
| effort | config | enum | medium |
| max_turns | config | int | 25 |
| disallowed_tools | config | list | [] |
| hooks | config | map | {nulls} |
| permission_scope | config | enum | nucleus |

## Size Constraints
- Standard ISO: max 4096 bytes
- Instruction ISO: max 6144 bytes
- Total builder: 13 files, < 60KB aggregate
