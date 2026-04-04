# BATCH A — Diretórios Pet Especializados
**Output**: `N01_research/output/data/crm_batch_a_diretorios.json`
**Signal**: `python _tools/signal_writer.py n01 complete 9.0 BATCH_A_DIRETORIOS`

---

## LEIA PRIMEIRO
1. `P05_output/p05_rf_crm_output_standard.md` — formato JSON
2. `P06_schema/p06_val_business_contact_quality.md` — anti-fake
3. `N01_research/output/data/crm_pet_abc.json` — 244 contatos existentes (dedup)

---

## Fontes a varrer (nesta ordem)

### 1. Petlove Rede Credenciada (MAIOR ROI)
```
URL base: https://saude.petlove.com.br/rede-credenciada
Método: FIRECRAWL scrape da página filtrada por cidade

Para cada cidade ABC:
  FETCH ou FIRECRAWL: buscar clínicas credenciadas em:
  - São Caetano do Sul, SP
  - São Bernardo do Campo, SP
  - Santo André, SP
  - Diadema, SP
  - Mauá, SP
  - Ribeirão Pires, SP
  - Rio Grande da Serra, SP

Extrair: nome, endereço, telefone, especialidades
Esses dados já vêm VALIDADOS pela Petlove.
```

### 2. DogHero
```
URL base: https://doghero.com.br
Método: SERPER site:doghero.com.br "são caetano do sul" OR "são bernardo"

Para cada cidade, buscar:
  - Hospedagem pet
  - Dog walker
  - Pet sitter
  - Creche pet

Extrair: nome do cuidador/empresa, bairro, cidade, serviços, avaliação
```

### 3. Pet Anjo
```
URL base: https://petanjo.com
Método: SERPER site:petanjo.com "ABC paulista" OR "são caetano" OR "são bernardo" OR "santo andré"

Buscar:
  - Banho e tosa móvel
  - Pet sitter
  - Dog walker
  - Adestrador

Extrair: nome, região, serviços, avaliação
```

### 4. TeleListas / Guia Mais
```
FIRECRAWL ou FETCH:
  https://www.telelistas.net/sp/sao-caetano-do-sul/pet+shop
  https://www.telelistas.net/sp/sao-bernardo-do-campo/pet+shop
  https://www.telelistas.net/sp/santo-andre/pet+shop
  https://www.telelistas.net/sp/diadema/pet+shop
  https://www.telelistas.net/sp/maua/pet+shop

Repetir com: clinica+veterinaria, banho+e+tosa, hotel+pet

  https://www.guiamais.com.br/sao-caetano-do-sul-sp/pet-shop
  https://www.guiamais.com.br/sao-bernardo-do-campo-sp/pet-shop

Extrair: nome, endereço, telefone (TeleListas tem telefone validado!)
```

### 5. Apontador
```
FIRECRAWL ou FETCH:
  https://www.apontador.com.br/em/sp/sao-caetano-do-sul/pet-shops
  https://www.apontador.com.br/em/sp/sao-bernardo-do-campo/pet-shops
  https://www.apontador.com.br/em/sp/santo-andre/pet-shops

Repetir com: clinicas-veterinarias, banho-e-tosa

Extrair: nome, endereço, telefone, avaliação
```

### 6. Lista Mais
```
FIRECRAWL ou FETCH:
  https://www.listamais.com.br/sp/sao-caetano-do-sul/pet-shop
  
Extrair: nome, endereço, telefone validado
```

---

## Output JSON

```json
{
  "nome_fantasia": "Nome",
  "segmento": "clinica_vet|pet_shop|banho_tosa|hotel_pet|creche_pet|adestramento",
  "endereco": "Rua X, 123 - Bairro",
  "bairro": "Bairro",
  "cidade": "São Caetano do Sul",
  "telefone": "(11) XXXX-XXXX",
  "whatsapp": "",
  "email": "",
  "website": "",
  "instagram": "",
  "google_rating": "",
  "fonte_descoberta": "petlove:rede-credenciada:scs|telelistas:sp/scs/pet-shop|doghero:busca-scs",
  "completeness_score": 3,
  "data_discovery": "2026-04-03"
}
```

---

## Dedup contra 244 existentes
```python
import json
with open('N01_research/output/data/crm_pet_abc.json','r',encoding='utf-8') as f:
    existing = json.load(f)
existing_names = {(r.get('nome_fantasia','') or r.get('nome','')).lower().strip() for r in existing}
# Se nome já existe → skip (ou marcar ja_no_crm: true)
```

## Regras
1. NUNCA inventar dados — campo vazio se não encontrou
2. FONTE OBRIGATÓRIA em cada registro
3. JSON DIRETO — não markdown
4. Commit ao final: `git add N01_research/output/data/ && git commit -m "[N01] BATCH_A diretórios pet — +{N} contatos de Petlove/TeleListas/DogHero/Apontador" --no-verify`
