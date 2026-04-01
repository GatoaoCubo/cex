# N03 Task — Content Monetization v2: Template + Enrich ISOs + Validate
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

---

## CONTEXTO
Leia `.cex/runtime/handoffs/mission_content_monetization_v2.md` para detalhes completos.

## PRÉ-REQUISITO
N01 deve ter completado Fase 0 (8 KCs criados). Verifique:
```bash
ls P01_knowledge/library/platform/kc_hotmart_api.md P01_knowledge/library/platform/kc_digistore24_api.md
```
Se não existirem, ESPERE e verifique a cada 2 minutos.

---

## TAREFA 1: FASE 1 — Template Genérico N06 (30min)

Criar `_instances/_template/N06_commercial/` com 3 arquivos:

### 1. content_monetization_config.md
Template com [PLACEHOLDERS] para qualquer empresa. Frontmatter:
```yaml
---
id: tpl_content_monetization_config
kind: env_config
pillar: P09
quality: null
tldr: "Instance template for content monetization — fill [PLACEHOLDERS] for any business"
tags: [template, monetization, config, hotmart, digistore24]
---
```
Seções: identidade, plataformas (tier_1 BR + tier_1 INT + tier_2), produtos, webhooks (hotmart + ds24), afiliados, compliance.

### 2. pricing_model.md
Template de pricing strategy: ladder (freebie→low→mid→high→recorrência), PPP por região, cupons, métricas (CAC, LTV, churn).

### 3. launch_checklist.md
Checklist genérico de lançamento: produto criado, checkout testado (sandbox), webhook configurado, página de vendas, email sequences, afiliados, compliance EU, analytics.

```bash
git add _instances/_template/N06_commercial/
git commit -m "[N03] template: create _instances/_template/N06_commercial/ (config + pricing + checklist)"
```

---

## TAREFA 2: FASE 2 — Enriquecer Builder ISOs com DS24 (1h)

Atualizar 8 dos 13 ISOs em `archetypes/builders/content-monetization-builder/`:

| ISO | O Que Adicionar |
|-----|----------------|
| bld_architecture_content_monetization.md | DS24 IPN flow (form-encoded, sha512, respond "OK") |
| bld_instruction_content_monetization.md | Steps para DS24: create product, configure IPN, test sandbox |
| bld_examples_content_monetization.md | Exemplo DS24: produto EUR, IPN handler, affiliate setup |
| bld_schema_content_monetization.md | Campos DS24: ds24_product_id, ds24_api_key, ipn_passphrase |
| bld_config_content_monetization.md | Config vars DS24: DS24_API_KEY, DS24_IPN_URL, DS24_SANDBOX |
| bld_tools_content_monetization.md | DS24 API endpoints: /products, /purchases, /affiliates |
| bld_knowledge_card_content_monetization.md | Refs aos 8 novos KCs de pesquisa |
| bld_collaboration_content_monetization.md | Crew: "Multi-Platform Launch" |

**REGRA**: Hotmart e DS24 como PARES equivalentes. Pattern: "Platform A (Hotmart/BR) ... Platform B (Digistore24/INT)"
**NÃO ALTERAR**: bld_manifest, bld_quality_gate, bld_system_prompt, bld_output_template, bld_memory

```bash
git add archetypes/builders/content-monetization-builder/
git commit -m "[N03] enrich: content-monetization-builder ISOs with Digistore24 parity (8/13 ISOs updated)"
```

---

## TAREFA 3: FASE 3 — Reindex + Validate (15min)

```bash
python _tools/cex_compile.py --all
python _tools/cex_doctor.py
```

Verificar:
- 8 novos KCs existem em P01_knowledge/library/platform/
- Builder ISOs mencionam DS24 em >= 8 files
- _instances/_template/N06_commercial/ existe com 3 files
- Doctor: 0 FAIL

```bash
git add -A
git commit -m "[N03] validate: recompile + validate after content-monetization-v2"
```

## SIGNAL
```python
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'cmv2_build_complete', 9.0)"
```
