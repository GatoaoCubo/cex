# BATCH B — Google Maps / Google Business Profile Deep Harvest
**Output**: `N01_research/output/data/crm_batch_b_gmaps.json`
**Signal**: `python _tools/signal_writer.py n01 complete 9.0 BATCH_B_GMAPS`

---

## LEIA PRIMEIRO
1. `P05_output/p05_rf_crm_output_standard.md` — formato JSON
2. `P06_schema/p06_val_business_contact_quality.md` — anti-fake
3. `N01_research/output/data/crm_pet_abc.json` — 244 contatos (dedup)

---

## Objetivo

Varrer Google Maps/Business Profile por CATEGORIA + CIDADE para descobrir negócios pet que não aparecem em outras fontes. Google Maps é a fonte mais completa para telefone, rating, reviews, horário, coordenadas exatas.

---

## Queries por cidade × segmento

### Método SERPER (google_maps mode se disponível)
```
Para cada combinação, usar SERPER:

CATEGORIAS:
  "pet shop" | "loja de animais" | "agropet" | "casa de ração"
  "clínica veterinária" | "veterinário" | "hospital veterinário"
  "banho e tosa" | "estética animal" | "grooming pet"
  "hotel pet" | "hospedagem pet" | "pensão para animais"
  "creche pet" | "daycare pet"
  "adestrador" | "adestramento canino"
  "farmácia veterinária" | "medicamentos veterinários"
  "funerária pet" | "cremação animal"
  "táxi pet" | "transporte animal"

CIDADES (varrer TODAS):
  "São Caetano do Sul"
  "São Bernardo do Campo"  
  "Santo André"
  "Diadema"
  "Mauá"
  "Ribeirão Pires"
  "Rio Grande da Serra"
```

### Query format:
```
SERPER: "{categoria}" near "{cidade}" SP
SERPER: "{categoria}" "{cidade}" telefone horário
```

### Para cada resultado do Google:
```
Extrair:
  - nome do negócio
  - endereço completo
  - telefone
  - rating (estrelas)
  - número de reviews
  - horário de funcionamento
  - website (se listado)
  - categorias Google (ex: "Veterinarian", "Pet store")
  - Google Maps URL
  - coordenadas (lat, lng)
```

### Enriquecimento extra:
```
Se o resultado tem website → FETCH o site:
  - Buscar email no rodapé/contato
  - Buscar WhatsApp (muitos pet shops têm no site)
  - Buscar Instagram handle
```

---

## Prioridade de varredura

1. **SCS** — epicentro, todas categorias (pet_shop, vet, banho_tosa, hotel, creche, adestramento)
2. **Diadema** — só 9 contatos, varrer tudo
3. **Mauá** — só 7, varrer tudo
4. **Ribeirão Pires + Rio Grande da Serra** — quase vazio
5. **SBC + SA** — focar nos segmentos menos cobertos (hotel, creche, adestramento, farmácia vet)

---

## Output JSON

```json
{
  "nome_fantasia": "Pet Center Marginal",
  "segmento": "pet_shop",
  "endereco": "Av. Kennedy, 1.500 - Rudge Ramos",
  "bairro": "Rudge Ramos",
  "cidade": "São Bernardo do Campo",
  "telefone": "(11) 4330-1234",
  "whatsapp": "(11) 94330-1234",
  "email": "contato@petcentermarginal.com.br",
  "website": "https://petcentermarginal.com.br",
  "instagram": "@petcentermarginal",
  "google_maps_url": "https://maps.google.com/?cid=...",
  "google_rating": "4.7",
  "google_reviews": "328",
  "horario": "Seg-Sáb 8h-20h, Dom 9h-14h",
  "categorias_google": "Pet store, Veterinarian",
  "lat": -23.6789,
  "lng": -46.5432,
  "fonte_descoberta": "serper:google_maps:'pet shop são caetano do sul SP'",
  "completeness_score": 5,
  "data_discovery": "2026-04-03"
}
```

---

## Regras
1. NUNCA inventar — só dados que aparecem nos resultados Google
2. FONTE OBRIGATÓRIA — query exata usada
3. DEDUP contra 164 existentes por nome (case insensitive)
4. JSON DIRETO
5. Commit: `git add N01_research/output/data/ && git commit -m "[N01] BATCH_B Google Maps — +{N} negócios, {N} com tel, {N} cidades cobertas" --no-verify`
