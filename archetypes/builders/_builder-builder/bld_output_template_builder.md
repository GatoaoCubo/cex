---
kind: output_template
id: bld_output_template_builder
pillar: P03
llm_function: PRODUCE
purpose: Output format for generated builder artifacts
---
# Output Template: _builder-builder

## Generated Builder Structure
```
archetypes/builders/{kind}-builder/
├── bld_manifest_{kind}.md        # Identity + routing
├── bld_instruction_{kind}.md     # Step-by-step build guide
├── bld_config_{kind}.md          # Constraints + runtime fields
├── bld_memory_{kind}.md          # Learning records
├── bld_tools_{kind}.md           # Tool inventory + permissions
├── bld_collaboration_{kind}.md   # Crew compositions
├── bld_architecture_{kind}.md    # Structure + dependencies
├── bld_schema_{kind}.md          # Field definitions
├── bld_output_template_{kind}.md # Output format
├── bld_examples_{kind}.md        # Reference examples
├── bld_quality_gate_{kind}.md    # Validation gates
├── bld_knowledge_card_{kind}.md  # Domain knowledge
└── bld_system_prompt_{kind}.md   # LLM system prompt
```

## Post-Generation Checklist
1. All 13 files present
2. All frontmatter YAML-parseable
3. Universal fields hydrated
4. cex_doctor.py → PASS (0 WARN)
5. cex_compile.py --all → 0 errors
6. cex_materialize.py → sub-agent created
