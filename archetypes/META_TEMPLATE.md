# Meta-Template v1.0
# The template that generates ALL other CEX templates
# The builder uses this file to generate templates for any pillar

## HOW TO USE

1. Builder receives: "create template for P{{N}} {{type}}"
2. Builder reads: this meta-template
3. Builder reads: P{{N}}_{{lp}}/_schema.yaml (type fields)
4. Builder generates: P{{N}}_{{lp}}/templates/tpl_{{type}}.md + .yaml
5. Builder validates: against _schema.yaml
6. Builder commits with quality >= 9.0

## OUTPUT TEMPLATE (.md)



## OUTPUT TEMPLATE (.yaml)



## GENERATION RULES

- NEVER generate empty fields (TBD, TODO, placeholder)
- ALWAYS include a concrete example in each variable
- ALWAYS calculate density (estimate useful tokens / total)
- ALWAYS include semantic_bridge if quality >= 8.0
- ALWAYS dual output: .md (human) + .yaml (LLM)
- MAX 2KB per template (the template itself, not the instance)

## SECTIONS BY TYPE (quick reference)

| Pillar | Type | Required sections |
|--------|------|-------------------|
| P01 | knowledge_card (domain) | quick_ref, concepts, phases, rules, flow |
| P01 | knowledge_card (meta) | summary, spec_table, patterns, anti, refs |
| P02 | agent | arch, when_to_use, capabilities, integration, quality |
| P03 | prompt_template | purpose, variables, body, gates, examples, bridge |
| P04 | skill | purpose, phases, anti_patterns, metrics |
| P07 | eval | setup, execute, assert, teardown |
| P08 | pattern | problem, solution, consequences, example |
| P12 | workflow | trigger, steps, output, rollback |

## EVOLUTION

This meta-template improves during use:
1. Generates a batch of templates
2. Evaluates quality of the generated artifacts
3. Identifies gaps (missing field, bad format)
4. Updates this file
5. Re-generates improved templates
6. Repeats until quality >= 9.5

---
*Meta-Template v1.0 | Shokunin: builds itself better | 2026-03-22*