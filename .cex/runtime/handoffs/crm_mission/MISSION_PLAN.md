# Mission: CRM_FULL_HARVEST — Status Atualizado

## Status (04/Abr/2026 12:50)
- **Base**: 244 contatos reais (0 fakes)
- **Batches completos**: C (social +53), D (marketplaces +12), E (reputation +15)
- **Batches pendentes**: A (diretórios), B (Google Maps), F (CNAE deep)
- **Meta**: 500+ contatos

---

## Waves Executadas

### Wave 2 ✅ — Social + Marketplaces (03/Abr)
| Slot | Batch | Status | +Novos |
|:---:|-------|:------:|:------:|
| C | `batch_c_social_discovery` | ✅ MERGED | +53 |
| D | `batch_d_marketplaces` | ✅ MERGED | +12 |

### Wave 3 (parcial) ✅ — Reputação (03/Abr)
| Slot | Batch | Status | +Novos |
|:---:|-------|:------:|:------:|
| E | `batch_e_reputation` | ✅ MERGED (04/Abr) | +15 |

---

## Wave FINAL — A executar agora

| Slot | Batch | Fontes | Output | ROI estimado |
|:---:|-------|--------|--------|:---:|
| A | `batch_a_diretorios_pet` | Petlove, DogHero, PetAnjo, TeleListas, GuiaMais, Apontador | `crm_batch_a_diretorios.json` | +40-80 |
| B | `batch_b_google_maps` | Serper Google Maps, 9 categorias × 7 cidades | `crm_batch_b_gmaps.json` | +60-120 |
| F | `batch_f_cnae_deep` | Casa dos Dados, CNPJ.biz, ReceitaWS, CNPJá | `crm_batch_f_cnae.json` | +30-50 |

### Dispatch
```bash
# 3 slots paralelos — cada um roda em terminal separado
powershell -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n01 -task "BATCH_A_DIRETORIOS"
powershell -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n01 -task "BATCH_B_GMAPS"
powershell -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n01 -task "BATCH_F_CNAE"
```

---

## Pós-Grid: Merge + Consolidate

```bash
# 1. Dry-run check
python N01_research/output/data/merge_batches.py --all --dry-run

# 2. Merge
python N01_research/output/data/merge_batches.py --all

# 3. Commit
git add N01_research/output/data/ && git commit -m "[N07] merge batches A+B+F → {N} contatos"
```

---

## Meta Final

| Métrica | Antes (164) | Agora (244) | Projeção (+A+B+F) | Meta |
|---------|:-----------:|:-----------:|:------------------:|:----:|
| Total contatos | 164 | 244 | ~414 | **500+** |
| Com telefone | 37% | 34% | ~50% | 60% |
| Com endereço | 62% | 56% | ~72% | 85% |
| Com email/web | 50% | 63% | ~65% | ✅ 65% |
| Com CNPJ | ~10% | 22% | ~32% | 40% |
| Fakes | 0 | 0 | 0 | ✅ 0 |
