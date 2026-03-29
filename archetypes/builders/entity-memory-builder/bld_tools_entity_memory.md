---
kind: tools
id: bld_tools_entity_memory
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for entity_memory production
---

# Tools: entity-memory-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing entity_memory artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| brain_query [MCP] | Find related entities for relationship mapping | Phase 1 (relationships) | CONDITIONAL |
| firecrawl [MCP] | Scrape entity official page for primary-source attributes | Phase 1 (attribute gathering) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P10_memory/_schema.yaml | Field definitions, entity_memory kind |
| CEX Examples | P10_memory/examples/ | Real entity_memory artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P10_entity_memory |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| Entity Pool Index | P10_memory/ENTITY_INDEX.md | All registered entities (dedup check) |
## NER / Extraction Support
For automated entity attribute extraction from text:
- spaCy `en_core_web_sm`: identifies PERSON, ORG, PRODUCT, DATE, VERSION spans
- LangChain `EntityMemory`: extracts entity mentions from conversation turns
- Manual extraction: read official docs, extract version, homepage, maintainer, license
## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern `^p10_em_`, attributes non-empty,
entity_type in enum, quality == null, update_policy declared, no PII, body <= 2048 bytes.
