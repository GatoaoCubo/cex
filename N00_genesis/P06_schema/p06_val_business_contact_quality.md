---
id: p06_val_business_contact_quality
kind: validator
pillar: P06
title: "Business Contact Quality Validator v2 — Anti-Fake"
version: 2.1.0
created: 2026-04-03
updated: 2026-04-07
author: n04_knowledge
domain: crm-research
rule_name: validate-business-contact-quality
target_kind: response_format
scope: post_generation
severity: error
auto_fix: false
quality: 9.0
tags: [validator, crm, contact, anti-fake, quality-gate, lgpd]
tldr: "Validates CRM contacts: 4 anti-fabrication rules (sequential names, CNPJs, generic addresses, missing sources), 5-point completeness scoring, 4 format validators (phone, CNPJ, email, website), LGPD compliance gate. Used in Step 3 of p12_wf_crm_research_pipeline."
density_score: 1.0
---

# Business Contact Quality Validator v2

> **Purpose**: Ensure every CRM contact is real, complete, and compliant before entering the GATO³ prospect pipeline.
> **Trigger**: Step 3 (Validation) of `p12_wf_crm_research_pipeline.md`
> **Scope**: All 471+ ABC Paulista business contacts (vets, pet shops, groomers, hospitals)
> **LGPD**: All processing must comply with Lei Geral de Proteção de Dados

## Anti-Fabricação Rules (REJECT imediato)

### AF1: Nome Numerado Sequencial
```yaml
field: nome_fantasia
rule: NÃO pode terminar em dígito se segue padrão "Segmento Cidade N"
regex_reject: "^(Pet Shop|Banho E Tosa|Clinica|Hospital|Veterinaria|Pet Business).+\\d+$"
severity: REJECT
reason: "Padrão de fabricação detectado: nomes genéricos numerados"
example_reject: "Pet Shop Santo André 3"
example_pass: "Pet Shop Amigo Fiel"
```

### AF2: CNPJ Sequencial
```yaml
field: cnpj
rule: Diferença entre CNPJ atual e anterior deve ser > 1000
check: abs(int(cnpj_atual) - int(cnpj_anterior)) > 1000
severity: REJECT
reason: "CNPJs sequenciais indicam fabricação em lote"
example_reject: "12.345.678/0001-01, 12.345.678/0001-02"
example_pass: "12.345.678/0001-90, 45.678.123/0001-55"
```

### AF3: Endereço Genérico
```yaml
field: endereco
regex_reject: "^(Avenida|Rua)\\s+(Pet Shop|Banho E Tosa|Clinica|Hospital|Veterinaria)"
severity: REJECT
reason: "Endereço usa nome de segmento como logradouro — fabricado"
example_reject: "Rua Pet Shop, 100"
example_pass: "Rua das Flores, 245 - Centro"
```

### AF4: Fonte Ausente
```yaml
field: fonte_descoberta
rule: Campo obrigatório e não vazio
severity: REJECT
reason: "Sem fonte rastreável. Todo contato precisa de URL/query de origem."
valid_sources:
  - "Google Maps: query 'pet shop São Caetano do Sul'"
  - "Instagram: @petshopamigofiel"
  - "CNAE 4789-0/04 via ReceitaWS"
  - "Indicação de parceiro existente"
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
  - score >= 3: PASS (entra no CRM com prioridade)
  - score == 2: PASS (entra no CRM, flag para enriquecimento)
  - score == 1: QUARANTINE (precisa enriquecimento antes de outreach)
  - score == 0: REJECT (descartado — insuficiente para qualquer ação)
```

### Completeness by Segment (expected minimums)

| Segment | Min Score | Rationale |
|---------|-----------|-----------|
| Vet Clinics | 4 | Professional businesses with online presence |
| Pet Shops | 3 | Most have Google Maps + phone minimum |
| Groomers | 2 | Many Instagram-only, no website |
| 24h Hospitals | 4 | Well-established, full online presence |

---

## Format Validators

### F1: Telefone BR
```yaml
field: telefone
format: "^\\(?\\d{2}\\)?\\s?\\d{4,5}-?\\d{4}$"
normalize: "Remover espaços, parênteses, hífens → (XX) XXXXX-XXXX"
severity: WARN
examples:
  valid: ["(11) 99999-1234", "11999991234", "(11) 4002-8922"]
  invalid: ["999-1234", "123", "+55 11 99999-1234"]
note: "DDD 11 = Grande SP (Ring 1-2). DDD 13/15/16/17/19 = Ring 3."
```

### F2: CNPJ
```yaml
field: cnpj
format: "^\\d{2}\\.\\d{3}\\.\\d{3}/\\d{4}-\\d{2}$"
check: "Dígitos verificadores mod 11"
severity: INFO
note: "Campo opcional — muitos pequenos negócios não divulgam CNPJ publicamente"
```

### F3: Email
```yaml
field: email
format: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
severity: WARN
common_domains: ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com.br"]
note: "Business domains (e.g., @petshopamigofiel.com.br) increase trust score"
```

### F4: Website
```yaml
field: website
format: "^https?://"
check: "Idealmente HTTP 200, mas não bloquear se timeout"
severity: INFO
note: "Many small ABC Paulista businesses use only Instagram as 'website'"
```

---

## LGPD Compliance Gate

```yaml
lgpd_checks:
  - rule: "Data source must be publicly available (Google Maps, public Instagram, government registry)"
    severity: REJECT_IF_PRIVATE
  - rule: "No personal CPF or personal phone unless business-registered"
    severity: REJECT
  - rule: "Opt-out mechanism must exist before any outreach"
    severity: BLOCK_OUTREACH
  - rule: "Data retention: max 180 days without interaction, then archive"
    severity: WARN
  - rule: "Processing purpose: B2B partnership outreach only (not resale)"
    severity: MANDATORY
```

---

## Pipeline Integration

This validator runs at **Step 3 (Validação)** of `p12_wf_crm_research_pipeline.md`.

```python
# Usage:
from _tools.crm.crm_data_validator import validate_contact

result = validate_contact(record, previous_records)
# result.status: PASS | QUARANTINE | REJECT
# result.score: 0-5
# result.issues: ["AF1: nome numerado", "F1: telefone inválido"]
# result.lgpd_ok: True | False
```

### Decision Flow
```
Contact → AF1-AF4 (anti-fake) → REJECT? → discard
                                    ↓ PASS
                               Completeness (0-5) → score < 2? → QUARANTINE
                                    ↓ score >= 2
                               F1-F4 (format) → normalize + WARN
                                    ↓
                               LGPD gate → private data? → REJECT
                                    ↓ OK
                               → CRM PASS (ready for outreach)
```

## Cross-References
- CRM pipeline → `P12_orchestration/p12_wf_crm_research_pipeline.md`
- Outreach workflow → `N02_marketing/p12_wf_gato_strategic_outreach.md`
- Research guidelines → `N01_research/config/brand_context.md`
- Brand config → `.cex/brand/brand_config.yaml`
