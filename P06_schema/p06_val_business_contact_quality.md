---
id: p06_val_business_contact_quality
kind: validator
pillar: P06
title: "Business Contact Quality Validator v2 — Anti-Fake"
version: 2.0.0
created: 2026-04-03
updated: 2026-04-03
author: n07_orchestrator
domain: crm-research
rule_name: validate-business-contact-quality
target_kind: response_format
scope: post_generation
severity: error
auto_fix: false
quality: 9.0
tags: [validator, crm, contact, anti-fake, quality-gate]
tldr: "Valida contatos CRM: anti-fabricação (nomes numerados, CNPJs sequenciais), completeness gate, formato telefone/email/CNPJ."
density_score: 1.0
---

# Business Contact Quality Validator v2

## Anti-Fabricação (REJECT imediato)

### AF1: Nome Numerado Sequencial
```yaml
field: nome_fantasia
rule: NÃO pode terminar em dígito se segue padrão "Segmento Cidade N"
regex_reject: "^(Pet Shop|Banho E Tosa|Clinica|Hospital|Veterinaria|Pet Business).+\d+$"
severity: REJECT
reason: "Padrão de fabricação detectado: nomes genéricos numerados"
```

### AF2: CNPJ Sequencial
```yaml
field: cnpj
rule: Diferença entre CNPJ atual e anterior deve ser > 1000
check: abs(int(cnpj_atual) - int(cnpj_anterior)) > 1000
severity: REJECT
reason: "CNPJs sequenciais indicam fabricação em lote"
```

### AF3: Endereço Genérico
```yaml
field: endereco
regex_reject: "^(Avenida|Rua)\s+(Pet Shop|Banho E Tosa|Clinica|Hospital|Veterinaria)"
severity: REJECT
reason: "Endereço usa nome de segmento como logradouro — fabricado"
```

### AF4: Fonte Ausente
```yaml
field: fonte_descoberta
rule: Campo obrigatório e não vazio
severity: REJECT
reason: "Sem fonte rastreável. Cada contato precisa de URL/query de origem."
```

---

## Completeness Score (0-5)

```yaml
scoring:
  - field: nome_fantasia
    points: 1
    condition: "não vazio e len > 2"

  - field: endereco
    points: 1
    condition: "não vazio e contém número"

  - field: telefone OR whatsapp
    points: 1
    condition: "pelo menos 1 preenchido com 10+ dígitos"

  - field: email OR website
    points: 1
    condition: "pelo menos 1 preenchido e válido"

  - field: instagram OR google_maps_url
    points: 1
    condition: "pelo menos 1 preenchido"

gates:
  - score >= 2: PASS (entra no CRM)
  - score == 1: QUARANTINE (precisa enriquecimento)
  - score == 0: REJECT (descartado)
```

---

## Validações de Formato

### F1: Telefone BR
```yaml
field: telefone
format: "^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$"
normalize: "Remover espaços, parênteses, hífens → (11) 91234-5678 (exemplo)"
severity: WARN
```

### F2: CNPJ
```yaml
field: cnpj
format: "^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$"
check: "Dígitos verificadores mod 11"
severity: INFO (campo opcional — muitos não divulgam)
```

### F3: Email
```yaml
field: email
format: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
severity: WARN
```

### F4: Website
```yaml
field: website
format: "^https?://"
check: "Idealmente HTTP 200, mas não bloquear"
severity: INFO
```

---

## Aplicação

Este validator roda no Step 3 (Validação) da pipeline `p12_wf_crm_research_pipeline.md`.

```python
# Uso:
from _tools.crm.crm_data_validator import validate_contact

result = validate_contact(record, previous_records)
# result.status: PASS | QUARANTINE | REJECT
# result.score: 0-5
# result.issues: ["AF1: nome numerado", "F1: telefone inválido"]
```
