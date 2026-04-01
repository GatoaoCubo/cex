# Phase 4: Nucleus Artifacts + Templates — Content Monetization
**Nucleus**: N06 (Commercial) | **Role**: Superintendent + Executor
**REGRA: Commit e signal ANTES de qualquer pausa.**

## CONTEXTO
Mission content-monetization. Você cria nucleus artifacts + templates + examples.
Antes de começar: verifique se Phase 3 (ISOs) foi commitada por N03:
```bash
git pull origin main 2>/dev/null; git log --oneline -5
```
Se não houver commit "[N03] monetization phase3", AGUARDE 2min e tente novamente.

## CRIAR

### N06 Nucleus Artifacts (4 files)

1. **N06_commercial/knowledge/knowledge_card_content_monetization.md**
   - Kind: knowledge_card, Pillar: P01
   - Domain-specific KC: how N06 uses monetization in its workflow
   - References 8 platform KCs from Phase 2

2. **N06_commercial/tools/content_monetization_tool.md**
   - Kind: function_def, Pillar: P04
   - Tool definition: inputs (product, pricing_tier, payment_provider), outputs (monetization_config)
   - Pipeline: PARSE→PRICING→CREDITS→CHECKOUT→COURSES→ADS→EMAILS→VALIDATE→DEPLOY

3. **N06_commercial/orchestration/dispatch_rule_content_monetization.md**
   - Kind: dispatch_rule, Pillar: P12
   - Keywords: monetizar, billing, checkout, curso, pricing, credits, pagamento, PIX, assinatura
   - Routes to content-monetization-builder

4. **N06_commercial/orchestration/workflow_content_monetization.md**
   - Kind: workflow, Pillar: P12
   - Full workflow: receive intent → resolve pricing → configure credits → setup checkout → generate course content → validate ads → send emails → deploy

### P04 Template (1 file)

5. **P04_tools/templates/tpl_content_monetization.md**
   - Kind: function_def, Pillar: P04
   - Config-driven template with payment_provider, currency, pipeline_costs, packs, tiers
   - Quality gate checklist

### P04 Examples (3 files)

6. **P04_tools/examples/ex_content_monetization_saas.md**
   - SaaS model: free/pro/enterprise tiers, Stripe, USD, monthly/yearly billing

7. **P04_tools/examples/ex_content_monetization_ecommerce.md**
   - E-commerce: MercadoPago, BRL centavos, PIX discount, BaseLinker ERP sync

8. **P04_tools/examples/ex_content_monetization_infoproduct.md**
   - Infoproduct: course generation, email sequences, sales page, credit packs

### Instance Config (1 file)

9. **_instances/codexa/N06_commercial/content_monetization_config.md**
   - Codexa-specific config: MercadoPago, BRL, pipeline costs from credit_system.py

## REGRAS
- Cada artifact: frontmatter completo (id, kind, pillar, quality:null, tldr, tags)
- Templates: 1500-2500B com configuration YAML + capability table + quality gate
- Examples: 800-1500B com real config values
- Compile: `python _tools/cex_compile.py --all`

## COMMIT
```bash
git add -A && git commit -m "[N06] monetization phase4: 4 nucleus + 1 template + 3 examples + 1 instance"
```
