# BATCH E — Reputação + Registros Profissionais (Reclame Aqui + CRMV + Econodata)
**Output**: `N01_research/output/data/crm_batch_e_reputation.json`
**Signal**: `python _tools/signal_writer.py n01 complete 9.0 BATCH_E_REPUTATION`

---

## LEIA PRIMEIRO
1. `P05_output/p05_rf_crm_output_standard.md` — formato JSON
2. `P06_schema/p06_val_business_contact_quality.md` — anti-fake
3. `N01_research/output/data/crm_pet_abc.json` — 164 contatos (dedup)

---

## Objetivo

Enriquecer dados com reputação + descobrir via registros profissionais. Duas funções:
1. **Discovery**: encontrar negócios novos via CRMV-SP e Econodata
2. **Enrichment**: adicionar dados de reputação aos 164 existentes

---

## Fonte 1: Reclame Aqui (enrichment dos existentes)

### Método:
```
Para os TOP 50 contatos existentes (com nome_fantasia):
  SERPER: site:reclameaqui.com.br "{nome_fantasia}"
  
Se encontrar página:
  FIRECRAWL: https://www.reclameaqui.com.br/empresa/{slug}/
  
  Extrair:
    - Nota geral (0-10)
    - % respondidas
    - % voltariam a fazer negócio
    - Número de reclamações (últimos 12 meses)
    - Status: "Ótimo" / "Bom" / "Regular" / "Ruim" / "Não recomendada"
```

### Para quem NÃO tem Reclame Aqui:
É um sinal POSITIVO para pequenos — significa que são pequenos/locais e não têm volume de reclamações. Anotar: `reclame_aqui: "sem_registro"`.

---

## Fonte 2: CRMV-SP (Conselho Regional de Medicina Veterinária)

### Método:
```
EXA: "CRMV-SP registro clínica veterinária ABC paulista"
EXA: "CRMV-SP clínicas credenciadas São Caetano do Sul"

SERPER: site:crmvsp.gov.br "clínica" "são caetano" OR "são bernardo" OR "santo andré"
SERPER: "CRMV" "clínica veterinária" "ABC paulista" lista registro

FIRECRAWL: https://www.crmvsp.gov.br (buscar seção de consulta pública)

Para cada clínica encontrada:
  - Nome
  - Número do registro CRMV
  - Endereço
  - Responsável técnico
  - Cidade
```

---

## Fonte 3: Econodata (Freemium — busca básica gratuita)

### Método:
```
SERPER: site:econodata.com.br "pet shop" "são caetano" OR "são bernardo" OR "santo andré"
SERPER: site:econodata.com.br "veterinária" "ABC paulista" OR "diadema" OR "mauá"
SERPER: site:econodata.com.br CNAE "4789-0/04" "SP"
SERPER: site:econodata.com.br CNAE "7500-1/00" "SP" "ABC"

FETCH: páginas de resultado Econodata

Extrair:
  - Razão social
  - CNPJ
  - Porte (MEI, ME, EPP)
  - Faturamento estimado
  - Número de funcionários
  - Endereço
  - Telefone
```

---

## Fonte 4: Yelp / Foursquare (complementar)

### Método:
```
SERPER: site:yelp.com.br "pet shop" "são caetano" OR "são bernardo" OR "santo andré"
SERPER: site:foursquare.com "pet" "São Caetano do Sul" OR "São Bernardo do Campo"

Extrair: nome, endereço, categorias, rating, reviews
```

---

## Output JSON

### Para NOVOS contatos (discovery):
```json
{
  "nome_fantasia": "Clínica Vet Dr. Silva",
  "segmento": "clinica_vet",
  "endereco": "R. Santo Antônio, 400",
  "cidade": "São Caetano do Sul",
  "telefone": "(11) 4200-5678",
  "crmv_registro": "CL-12345",
  "responsavel_tecnico": "Dr. Silva - CRMV 54321",
  "fonte_descoberta": "crmvsp:consulta-publica",
  "completeness_score": 3,
  "data_discovery": "2026-04-03"
}
```

### Para ENRIQUECIMENTO dos existentes (salvar em arquivo separado):
Criar: `N01_research/output/data/crm_enrichment_reputation.json`
```json
{
  "nome_fantasia": "Pets House",
  "match_crm": true,
  "reclame_aqui_nota": "8.5",
  "reclame_aqui_status": "Ótimo",
  "reclame_aqui_respondidas": "95%",
  "reclame_aqui_reclamacoes_12m": "12",
  "reclame_aqui_url": "https://reclameaqui.com.br/empresa/pets-house",
  "econodata_faturamento": "500k-1M",
  "econodata_funcionarios": "10-20",
  "yelp_rating": "4.5",
  "fonte_enriquecimento": "reclameaqui+econodata+yelp"
}
```

---

## Regras
1. NUNCA inventar ratings ou reputação
2. FONTE OBRIGATÓRIA — URL exata do Reclame Aqui / CRMV / Econodata
3. Dois outputs: novos em batch_e, enriquecimento em enrichment_reputation
4. DEDUP contra 164 existentes
5. JSON DIRETO
6. Commit: `git add N01_research/output/data/ && git commit -m "[N01] BATCH_E reputation + registros — +{N} novos CRMV/Econodata, {N} enriquecidos com reputação" --no-verify`
