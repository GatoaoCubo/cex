---
kind: schema
id: bld_schema_memory_architecture
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for memory_architecture
quality: null
title: "Schema Memory Architecture"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [memory_architecture, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for memory_architecture"
domain: "memory_architecture construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field | Type | Required | Default | Notes |  
|---|---|---|---|---|  
| id | string | yes | null | Must match ID pattern |  
| kind | string | yes | "memory_architecture" | Fixed value |  
| pillar | string | yes | "P10" | Fixed value |  
| title | string | yes | null | Descriptive name |  
| version | string | yes | "1.0" | Schema version |  
| created | datetime | yes | null | ISO 8601 format |  
| updated | datetime | yes | null | ISO 8601 format |  
| author | string | yes | null | Responsible party |  
| domain | string | yes | "memory" | Technical domain |  
| quality | null | yes | null | Never self-score; peer review assigns |  
| tags | list | yes | [] | Keywords for categorization |  
| tldr | string | yes | null | Summary in 1-2 sentences |  
| memory_type | string | yes | null | E.g., RAM, ROM |  
| capacity | integer | yes | null | Bytes |  
| access_time | float | yes | null | Nanoseconds |  

### Recommended  
| Field | Type | Notes |  
|---|---|---|  
| error_rate | float | Percentage (e.g., 0.01%) |  
| manufacturer | string | Vendor name |  
| technology | string | E.g., DRAM, SRAM |  

## ID Pattern  
^p10_marc_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Overview**  
   - Purpose and scope of the memory architecture.  
2. **Memory Types**  
   - Classification (volatile/non-volatile, cache/main).  
3. **Performance Metrics**  
   - Capacity, speed, latency, and error rates.  
4. **Integration**  
   - Compatibility with hardware/software ecosystems.  
5. **Scalability**  
   - Expansion capabilities and limitations.  
6. **Security**  
   - Data protection mechanisms (e.g., ECC, encryption).  

## Constraints  
- Memory capacity must be specified in bytes (integer).  
- Access time must be in nanoseconds (float).  
- Error rate must be a percentage (float, 0–100).  
- All memory types must be standardized (e.g., JEDEC).  
- Documentation must include manufacturer and technology details.  
- Versioning required for updates (YYYY-MM-DD format).
