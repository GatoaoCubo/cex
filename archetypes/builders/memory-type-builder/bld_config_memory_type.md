---
kind: config
id: bld_config_memory_type
pillar: P09
llm_function: CONSTRAIN
---

# Config: memory_type

- output_dir: P10_memory/compiled/
- naming: p10_mt_{type_name}.md -> p10_mt_{type_name}.yaml
- max_bytes: 2048
- machine_format: yaml
- id == filename stem
- One artifact per memory type (max 4 total)
