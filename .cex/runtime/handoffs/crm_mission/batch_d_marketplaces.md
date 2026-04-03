# BATCH D — Marketplaces & Delivery (iFood + Rappi + ML + Shopee)
**Output**: `N01_research/output/data/crm_batch_d_marketplaces.json`
**Signal**: `python _tools/signal_writer.py n01 complete 9.0 BATCH_D_MARKETPLACES`

---

## LEIA PRIMEIRO
1. `P05_output/p05_rf_crm_output_standard.md` — formato JSON
2. `P06_schema/p06_val_business_contact_quality.md` — anti-fake
3. `N01_research/output/data/crm_pet_abc.json` — 164 contatos (dedup)

---

## Objetivo

Encontrar pet shops e negócios pet que vendem via delivery/marketplace no ABC. Esses são os mais digitalmente ativos e potencialmente os melhores clientes B2B (já vendem online, entendem e-commerce).

---

## Fonte 1: iFood Pet

### Método:
```
SERPER: site:ifood.com.br "pet shop" "são caetano" OR "são bernardo" OR "santo andré" OR "diadema" OR "mauá"
SERPER: site:ifood.com.br "pet" "ABC paulista"
SERPER: site:ifood.com.br "ração" "são caetano" OR "são bernardo"

FIRECRAWL: https://www.ifood.com.br/delivery/sao-caetano-do-sul-sp (buscar categoria pet)
FIRECRAWL: https://www.ifood.com.br/delivery/sao-bernardo-do-campo-sp

Para cada loja encontrada:
  - Nome
  - Endereço
  - Rating/reviews iFood
  - Categoria
  - Se faz delivery de produtos pet
```

### Por que isso importa:
Se um pet shop está no iFood, ele:
- Tem operação ativa
- Aceita vendas digitais
- Tem estrutura de entrega
- É um ótimo candidato pra revender GATO³

---

## Fonte 2: Rappi

### Método:
```
SERPER: site:rappi.com.br "pet" "são caetano do sul" OR "são bernardo" OR "santo andré"
SERPER: site:rappi.com.br "ração" OR "pet shop" "ABC"

FIRECRAWL: buscar categoria pet na Rappi para cada cidade ABC
```

---

## Fonte 3: Mercado Livre (vendedores locais)

### Método:
```
SERPER: site:mercadolivre.com.br "pet" "são caetano" OR "são bernardo" "vendedor"
SERPER: site:mercadolivre.com.br "ração gato" localização:"São Paulo" "ABC"
SERPER: site:lista.mercadolivre.com.br "pet shop" "ABC paulista"

EXA: "vendedor pet shop mercado livre ABC paulista são caetano são bernardo"

Para vendedores MercadoPet:
  - Nome da loja/vendedor
  - Localização (cidade)
  - Reputação (verde/amarelo)
  - Volume de vendas
  - Produtos que vende
```

---

## Fonte 4: Shopee (vendedores locais)

### Método:
```
SERPER: site:shopee.com.br "pet" "são caetano" OR "são bernardo" OR "santo andré"
SERPER: site:shopee.com.br "ração" OR "acessório pet" "SP" "ABC"

Para cada loja:
  - Nome
  - Localização
  - Rating
  - Número de produtos
```

---

## Output JSON

```json
{
  "nome_fantasia": "Pet Delivery ABC",
  "segmento": "pet_shop",
  "sub_segmento": "delivery",
  "endereco": "R. Marechal Deodoro, 500 - Centro",
  "bairro": "Centro",
  "cidade": "São Caetano do Sul",
  "telefone": "",
  "whatsapp": "",
  "email": "",
  "website": "https://ifood.com.br/loja/pet-delivery-abc",
  "instagram": "",
  "marketplace_ifood": true,
  "marketplace_rappi": false,
  "marketplace_ml": true,
  "marketplace_shopee": false,
  "rating_marketplace": "4.8",
  "digital_maturity": "alta",
  "potencial_b2b": "alto",
  "notas": "Presente no iFood e ML. Delivery ativo. Vende ração, acessórios. Ótimo candidato B2B.",
  "fonte_descoberta": "serper:site:ifood.com.br+'pet shop'+'são caetano'",
  "completeness_score": 3,
  "data_discovery": "2026-04-03"
}
```

### Campos extras:
- `marketplace_ifood` / `marketplace_rappi` / `marketplace_ml` / `marketplace_shopee` — booleano
- `digital_maturity` — alta/media/baixa (baseado em presença em marketplaces)
- `rating_marketplace` — rating no marketplace principal

---

## Regras
1. NUNCA inventar lojas — só as que realmente aparecem nos marketplaces
2. FONTE OBRIGATÓRIA
3. DEDUP contra 164 existentes
4. Marcar `potencial_b2b: "alto"` para quem já vende pet online
5. JSON DIRETO
6. Commit: `git add N01_research/output/data/ && git commit -m "[N01] BATCH_D marketplaces — +{N} sellers pet via iFood/Rappi/ML/Shopee, {N} digital-ready" --no-verify`
