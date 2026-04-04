# BATCH C — Social Media Discovery (Instagram + Facebook)
**Output**: `N01_research/output/data/crm_batch_c_social.json`
**Signal**: `python _tools/signal_writer.py n01 complete 9.0 BATCH_C_SOCIAL`

---

## LEIA PRIMEIRO
1. `P05_output/p05_rf_crm_output_standard.md` — formato JSON
2. `P06_schema/p06_val_business_contact_quality.md` — anti-fake
3. `N01_research/output/data/crm_pet_abc.json` — 244 contatos (dedup)

---

## Objetivo

Descobrir negócios pet INFORMAIS e MEIs que não aparecem em diretórios formais: banho e tosa à domicílio, pet sitters, groomers independentes, criadores, etc. Redes sociais são onde esses negócios vivem.

---

## Fonte 1: Instagram Hashtag Mining

### Hashtags por cidade
```
SERPER ou EXA para cada hashtag:

SCS:
  site:instagram.com #petshopscs OR #petshopsaocaetano OR #vetscs OR #veterinariasaocaetano
  site:instagram.com #banhoetosascs OR #banhoetosasaocaetano
  site:instagram.com #petloverscs OR #gatosscs OR #catloverscs

SBC:
  site:instagram.com #petshopsbc OR #petshopsaobernardo
  site:instagram.com #vetsbc OR #veterinariasaobernardo
  site:instagram.com #banhoetosasbc OR #groomingsbc

SA:
  site:instagram.com #petshopsantoandre OR #petshopsa
  site:instagram.com #vetsantoandre OR #veterinariasa
  site:instagram.com #banhoetosasa OR #groomingsa

ABC geral:
  site:instagram.com #petabc OR #petshopabcpaulista
  site:instagram.com #veterinarioabc OR #vetabc
  site:instagram.com #banhoetosaabc
  site:instagram.com #hotelpeabc OR #crechepetabc
  site:instagram.com #adestramentoabc
  site:instagram.com #petsitterabc OR #dogwalkerabc

Diadema/Mauá:
  site:instagram.com #petdiadema OR #petshopdiademma
  site:instagram.com #petmaua OR #petshopmaua
```

### Para cada perfil encontrado:
```
FETCH perfil Instagram (se público):
  - Nome do negócio (display name)
  - Bio → extrair telefone/WhatsApp/endereço/link
  - Cidade na bio ou posts
  - Categoria (se business profile)
  - URL do perfil → anotar como fonte
  - Link na bio → pode ter Linktree com mais contatos
```

---

## Fonte 2: Facebook Pages

### Queries SERPER:
```
site:facebook.com "pet shop" "são caetano do sul"
site:facebook.com "clínica veterinária" "são bernardo do campo"
site:facebook.com "banho e tosa" "santo andré"
site:facebook.com "hotel pet" "diadema"
site:facebook.com "pet shop" "mauá"
site:facebook.com "banho e tosa" "ribeirão pires"

Variações:
  "pet shop em" "{cidade}" site:facebook.com
  "veterinária" "{cidade}" site:facebook.com/pages
```

### Para cada Page:
```
FETCH página Facebook:
  - Nome do negócio
  - Endereço (se listado)
  - Telefone (se listado)
  - Horário
  - Categoria
  - Website (link externo)
  - Rating/reviews do Facebook
```

---

## Fonte 3: Google Business Profile (discovery via Serper)

### Queries focadas em negócios MENORES:
```
SERPER: "banho e tosa a domicílio" "são caetano" OR "são bernardo" OR "santo andré"
SERPER: "pet sitter" "ABC paulista"
SERPER: "dog walker" "são caetano" OR "são bernardo"
SERPER: "adestrador" "ABC" OR "são caetano" OR "santo andré"
SERPER: "cat sitter" OR "cuidador de gatos" "ABC"
SERPER: "táxi pet" OR "transporte pet" "ABC paulista"
SERPER: "creche pet" OR "daycare pet" "são bernardo" OR "santo andré" OR "são caetano"
SERPER: "funerária pet" OR "cremação animal" "ABC"
```

---

## Output JSON

```json
{
  "nome_fantasia": "Bia Grooming",
  "segmento": "banho_tosa",
  "sub_segmento": "domicilio",
  "endereco": "",
  "bairro": "Barcelona",
  "cidade": "São Caetano do Sul",
  "telefone": "",
  "whatsapp": "(11) 97777-1234",
  "email": "",
  "website": "",
  "instagram": "@biagrooming",
  "facebook": "facebook.com/biagrooming",
  "porte": "mei",
  "notas": "Banho e tosa a domicílio, atende SCS e SBC. Bio: WhatsApp no link",
  "fonte_descoberta": "serper:instagram:#banhoetosascs",
  "completeness_score": 2,
  "data_discovery": "2026-04-03"
}
```

---

## Regras
1. NUNCA inventar perfis — só os que realmente existem
2. FONTE OBRIGATÓRIA — hashtag/query que levou ao perfil
3. MEIs e informais SÃO VÁLIDOS — esses são os que queremos achar aqui
4. WhatsApp na bio conta como contato
5. DEDUP contra 164 existentes + contra Instagram handles existentes
6. JSON DIRETO
7. Commit: `git add N01_research/output/data/ && git commit -m "[N01] BATCH_C social discovery — +{N} negócios via Instagram/Facebook, {N} MEIs, {N} domicílio" --no-verify`
