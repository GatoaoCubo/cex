# BATCH F — CNAE Deep Harvest (Casa dos Dados + CNPJ.biz + ReceitaWS)
**Output**: `N01_research/output/data/crm_batch_f_cnae.json`
**Signal**: `python _tools/signal_writer.py n01 complete 9.0 BATCH_F_CNAE`

---

## LEIA PRIMEIRO
1. `P05_output/p05_rf_crm_output_standard.md` — formato JSON
2. `P06_schema/p06_val_business_contact_quality.md` — anti-fake
3. `N01_research/output/data/crm_pet_abc.json` — 164 contatos (dedup)

---

## Objetivo

Complementar o CNAE harvest anterior que ficou incompleto. Varrer SISTEMATICAMENTE cada CNAE × cidade via Casa dos Dados, CNPJ.biz e validar via ReceitaWS/CNPJ.ws.

---

## CNAEs alvo (8 códigos)

| CNAE | Descrição | Segmento |
|------|-----------|----------|
| **4789-0/04** | Com. varejista animais vivos e artigos pet | `pet_shop` |
| **7500-1/00** | Atividades veterinárias | `clinica_vet` |
| **9609-2/08** | Higiene e embelezamento de animais | `banho_tosa` |
| **4771-7/04** | Com. varejista medicamentos veterinários | `farmacia_vet` |
| **0159-8/02** | Criação de animais de estimação | `criador` |
| **5590-6/99** | Outros alojamentos | `hotel_pet` |
| **9609-2/99** | Outras ativ. serviços pessoais | `servicos_pet` |
| **4789-0/01** | Com. varejista suprimentos pet (ração) | `pet_shop` |

---

## Cidades (7 ABC)

| Cidade | Prioridade | Contatos atuais |
|--------|:---:|:---:|
| São Caetano do Sul | 1 | 35 |
| Diadema | 2 | 9 |
| Mauá | 3 | 7 |
| Ribeirão Pires | 4 | 1 |
| Rio Grande da Serra | 5 | 0 |
| São Bernardo do Campo | 6 | 56 |
| Santo André | 7 | 45 |

---

## Método SISTEMÁTICO

### Para CADA combinação CNAE × cidade:

```
Step 1: Casa dos Dados
  SERPER: site:casadosdados.com.br "{CNAE}" "{cidade}" "SP" "ativa"
  FETCH: https://casadosdados.com.br/solucao/cnpj?cnae={CNAE}&municipio={cidade}&uf=SP&situacao=ATIVA
  
  Se página acessível → FIRECRAWL para extrair tabela de resultados

Step 2: CNPJ.biz
  SERPER: site:cnpj.biz "{CNAE}" "{cidade}" "SP"
  FETCH: https://cnpj.biz/procura/{CNAE}/{cidade}-SP

Step 3: CNPJá / Consulta CNPJ
  SERPER: site:cnpja.com.br "{CNAE}" "{cidade}"

Step 4: Para CNPJs encontrados — validar dados básicos:
  FETCH: https://publica.cnpj.ws/cnpj/{CNPJ_14_digitos}
  (Rate limit: ~3/min — NÃO fazer mais que 3 por minuto)
  
  OU: https://www.receitaws.com.br/v1/cnpj/{CNPJ_14_digitos}
  (Rate limit: 3/min grátis)
```

---

## Tracking de cobertura

Criar um log de progresso no commit message:
```
CNAE 4789-0/04 × SCS: 15 resultados, 8 novos
CNAE 7500-1/00 × SCS: 22 resultados, 12 novos
CNAE 9609-2/08 × SCS: 10 resultados, 5 novos
...
```

---

## Output JSON

```json
{
  "cnpj": "12.345.678/0001-90",
  "razao_social": "Pet House Comércio de Artigos para Animais Ltda ME",
  "nome_fantasia": "Pet House SCS",
  "cnae_principal": "4789-0/04",
  "cnae_descricao": "Comércio varejista de animais vivos e de artigos e alimentos para animais de estimação",
  "segmento": "pet_shop",
  "endereco": "R. Oswaldo Cruz, 123",
  "bairro": "Oswaldo Cruz",
  "cidade": "São Caetano do Sul",
  "uf": "SP",
  "cep": "09571-000",
  "situacao_cadastral": "ATIVA",
  "data_abertura": "2018-05-14",
  "porte": "me",
  "natureza_juridica": "Sociedade Empresária Limitada",
  "capital_social": "30000.00",
  "telefone_receita": "(11) 4200-1234",
  "email_receita": "contato@pethouse.com.br",
  "fonte_descoberta": "casadosdados:cnae=4789-0/04&municipio=sao-caetano-do-sul&uf=SP",
  "ja_no_crm": false,
  "completeness_score": 4,
  "data_discovery": "2026-04-03"
}
```

---

## Regras
1. NUNCA fabricar CNPJs — cada um deve vir de fonte real verificável
2. SÓ situação ATIVA — ignorar BAIXADA/INAPTA/SUSPENSA
3. RESPEITAR rate limits das APIs (3/min ReceitaWS)
4. FONTE OBRIGATÓRIA
5. DEDUP contra 164 existentes (por CNPJ e por nome)
6. JSON DIRETO
7. Commit por cidade: `git add N01_research/output/data/ && git commit -m "[N01] BATCH_F CNAE {cidade} — {N} CNPJs ativos, {N} novos, CNAEs: {lista}" --no-verify`
