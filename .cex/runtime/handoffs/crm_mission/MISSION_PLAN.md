# Mission: CRM_FULL_HARVEST — Plano de Continuous Batching

## Status atual
- **Base**: 164 contatos reais (0 fakes)
- **Fonte 1 (CNAE) ✅**: Rodou, produziu 152→164

---

## Waves (2 slots N01 Opus paralelos por wave)

### Wave 1 — Diretórios + Google Maps
| Slot | Batch | Fontes | Output |
|:---:|-------|--------|--------|
| A | `batch_a_diretorios_pet` | Petlove, DogHero, PetAnjo, TeleListas, GuiaMais, Apontador, ListaMais | `crm_batch_a_diretorios.json` |
| B | `batch_b_google_maps` | Google Maps, Google Business Profile (9 categorias × 7 cidades) | `crm_batch_b_gmaps.json` |

### Wave 2 — Social + Marketplaces
| Slot | Batch | Fontes | Output |
|:---:|-------|--------|--------|
| C | `batch_c_social_discovery` | Instagram hashtags, Instagram location, Facebook Pages | `crm_batch_c_social.json` |
| D | `batch_d_marketplaces` | iFood, Rappi, Mercado Livre, Shopee | `crm_batch_d_marketplaces.json` |

### Wave 3 — Reputação + CNAE Deep
| Slot | Batch | Fontes | Output |
|:---:|-------|--------|--------|
| E | `batch_e_reputation` | Reclame Aqui, CRMV-SP, Econodata, Yelp | `crm_batch_e_reputation.json` + `crm_enrichment_reputation.json` |
| F | `batch_f_cnae_deep` | Casa dos Dados, CNPJ.biz, ReceitaWS, CNPJá | `crm_batch_f_cnae.json` |

---

## Pós-Mission: Merge + Dedup + Dashboard

```bash
# N07 faz o merge final:
# 1. Carregar crm_pet_abc.json (base: 164)
# 2. Merge batch_a → dedup → append novos
# 3. Merge batch_b → dedup → append novos
# 4. Merge batch_c → dedup → append novos
# 5. Merge batch_d → dedup → append novos
# 6. Merge batch_e → novos + enriquecimento
# 7. Merge batch_f → dedup → append novos
# 8. Recalcular completeness_score
# 9. Atualizar CSV + Dashboard HTML
# 10. Commit final
```

---

## Como executar

```bash
# Wave 1 (diretórios + Google Maps):
powershell -ExecutionPolicy Bypass -File _spawn/mission_crm_harvest.ps1 -wave 1

# Quando wave 1 completar → Wave 2:
powershell -ExecutionPolicy Bypass -File _spawn/mission_crm_harvest.ps1 -wave 2

# Quando wave 2 completar → Wave 3:
powershell -ExecutionPolicy Bypass -File _spawn/mission_crm_harvest.ps1 -wave 3

# Monitor:
bash _spawn/dispatch.sh status

# Merge final (N07):
python N01_research/output/data/merge_batches.py
```

---

## Meta final

| Métrica | Atual | Meta |
|---------|:---:|:---:|
| Total contatos | 164 | **500+** |
| Com telefone | 37% | **60%+** |
| Com endereço | 62% | **85%+** |
| Com email/web | 50% | **65%+** |
| Com CNPJ | ~10% | **40%+** |
| SCS | 35 | **60+** |
| Diadema | 9 | **40+** |
| Mauá | 7 | **30+** |
| Fakes | 0 | **0** |
