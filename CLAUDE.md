# CEX — LLM Entry Point

> **You are inside a CEX repository.** This is a typed, indexed knowledge base.
> Navigate by filename. Every file follows `{layer}_{kind}_{topic}.{ext}`.

## Quick Navigation

| Need | Command | Links |
|------|---------|-------|
| Architecture | Read this file | [[CEX_ARCHITECTURE_MAP]] |
| 8 Functions | | [[LLM_PIPELINE]] |
| Governance | | [[archetypes/CODEX]] |
| Whitepaper | | [[_docs/WHITEPAPER_CEX]] |
| Naming rules | | [[_docs/NAMING_CONVENTION]] |

## Find by Function

| Function | Find | Pillar |
|----------|------|--------|
| BECOME | `find -name "bld_system_prompt_*"` | [[P01_knowledge]] [[P02_model]] |
| INJECT | `find -name "bld_knowledge_card_*"` | [[P01_knowledge]] |
| REASON | `find -name "bld_instruction_*"` | [[P03_prompt]] |
| CALL | `find -name "bld_tools_*"` | [[P04_tools]] |
| PRODUCE | `find -name "bld_output_template_*"` | [[P05_output]] |
| CONSTRAIN | `find -name "bld_schema_*"` | [[P06_schema]] |
| GOVERN | `find -name "bld_quality_gate_*"` | [[P07_evals]] |
| COLLABORATE | `find -name "bld_collaboration_*"` | [[P12_orchestration]] |

## Layers

| Layer | Location | Count |
|-------|----------|-------|
| L0 DNA | [[archetypes]]/builders/ | 932 bld_* files |
| L1 Schema | [[P01_knowledge]] — [[P12_orchestration]] | 85 tpl_* + examples |
| L2 Instance | [[N01_intelligence]] — [[N07_admin]] | Company-specific |
| L3 Engine | _tools/ | Pipeline + governance |
| L4 Root | This file + [[README]] + [[INDEX]] | Entry points |

## Naming Grammar

```
{layer}_{kind}_{topic}.{ext}

bld_  = builder (L0)     | bld_system_prompt_agent.md
tpl_  = template (L1)    | tpl_knowledge_card.md
ex_   = example (L1)     | ex_knowledge_card_rag.md
(none)= instance (L2)    | knowledge_card_company_product.md
```
