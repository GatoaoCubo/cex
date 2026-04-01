# Phase 3: Builder ISOs — Content Monetization
**Nucleus**: N03 (Engineering) | **Superintendent**: N06 (Commercial)
**REGRA: Commit e signal ANTES de qualquer pausa.**

## CONTEXTO
Mission content-monetization. Você cria 14 builder ISOs para `content-monetization-builder`.
Antes de começar: verifique se Phase 2 (KCs) foi commitada por N04:
```bash
git pull origin main 2>/dev/null; git log --oneline -5
```
Se não houver commit "[N04] monetization phase2", AGUARDE 2min e tente novamente.

## CRIAR (14 ISOs em archetypes/builders/content-monetization-builder/)

Pipeline do builder: PARSE→PRICING→CREDITS→CHECKOUT→COURSES→ADS→EMAILS→VALIDATE→DEPLOY

| ISO | File | Focus |
|-----|------|-------|
| bld_manifest | bld_manifest_content_monetization.md | Identity, routing keywords (monetizar, billing, checkout, curso, pricing, credits) |
| bld_schema | bld_schema_content_monetization.md | Frontmatter schema: payment_provider, currency, pipeline_costs, packs |
| bld_config | bld_config_content_monetization.md | Default config: BRL centavos, mock mode, tiers |
| bld_system_prompt | bld_system_prompt_content_monetization.md | Persona: monetization architect |
| bld_instruction | bld_instruction_content_monetization.md | 9-step pipeline instructions |
| bld_knowledge_card | bld_knowledge_card_content_monetization.md | Pointer to 8 platform KCs |
| bld_examples | bld_examples_content_monetization.md | 3 example configs: SaaS, e-commerce, infoproduct |
| bld_output_template | bld_output_template_content_monetization.md | Output format for monetization config |
| bld_quality_gate | bld_quality_gate_content_monetization.md | Gates: pricing margins >30%, mock fallback exists, webhook idempotent |
| bld_architecture | bld_architecture_content_monetization.md | Component map: billing→credits→courses→ads→email |
| bld_tools | bld_tools_content_monetization.md | Tool requirements: payment SDK, LLM, ERP connector |
| bld_collaboration | bld_collaboration_content_monetization.md | Handoffs: N02 (marketing copy), N04 (data layer) |
| bld_memory | bld_memory_content_monetization.md | Initial observations from source analysis |
| bld_error_handling | bld_error_handling_content_monetization.md | Payment failures, webhook retries, credit insufficient |

## REGRAS
- Cada ISO: ≤4096B (≤6144B para bld_instruction)
- Frontmatter: id, kind:type_builder, pillar:P04, quality:null
- Reference existing domain builders (social-publisher, research-pipeline) as patterns
- Compile: `python _tools/cex_compile.py --all`

## COMMIT
```bash
git add -A && git commit -m "[N03] monetization phase3: 14 builder ISOs for content-monetization-builder"
```
