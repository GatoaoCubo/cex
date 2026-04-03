---
id: p06_val_business_contact_quality
kind: validator
pillar: P06
title: Business Contact Quality Validator
version: 1.0.0
created: 2026-04-03
updated: 2026-04-03
author: builder_agent
domain: crm-research
rule_name: validate-business-contact-quality
target_kind: response_format
scope: post_generation
severity: warning
auto_fix: false
llm_function: GOVERN
tags: [validator, crm, contact, phone, cnpj, email, website, GATO3]
tldr: "Valida qualidade de contatos business descobertos — telefone BR, CNPJ algoritmico, email formato+dominio, website SSL+200."
quality: null
density_score: null
---

# Business Contact Quality Validator

## Overview
Regra de validacao para contatos de businesses pet descobertos pela pipeline CRM. Verifica 4 dimensoes de qualidade: telefone, CNPJ, email e website. Cada dimensao produz pass/fail independente; o contato recebe um completeness_score baseado em quantas dimensoes passam.

## Conditions

### C1: Telefone BR Valido
```yaml
field: business.telefone
operator: matches
value: "^\\+?55\\d{2}[2-9]\\d{7,8}$"
on_fail: warning
remediation: "Normalizar para formato +55XX9XXXXXXXX. Remover espacos, parenteses, hifens."
notes: |
  - Celular: 11 digitos (com 9 inicial)
  - Fixo: 10 digitos
  - DDD obrigatorio (2 digitos)
  - Aceita com ou sem +55
```

### C2: CNPJ Algoritmico
```yaml
field: business.cnpj
operator: matches
value: "^\\d{14}$"
on_fail: info
remediation: "Verificar digitos verificadores (mod 11). Consultar ReceitaWS se disponivel."
notes: |
  - 14 digitos sem formatacao
  - Digitos verificadores: posicoes 13 e 14
  - Algoritmo: multiplicar por pesos [5,4,3,2,9,8,7,6,5,4,3,2], mod 11
  - Campo opcional — muitos pequenos negocios nao divulgam
```

### C3: Email Formato + Dominio
```yaml
field: business.email
operator: matches
value: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
on_fail: warning
remediation: "Verificar formato RFC 5322 basico. Checar MX record do dominio se possivel."
notes: |
  - Rejeitar emails genericos sem dominio corporativo (gmail, hotmail) com flag
  - Verificar se dominio resolve (DNS MX lookup)
  - Flag dominios expirados ou parked
```

### C4: Website SSL + Response 200
```yaml
field: business.website
operator: matches
value: "^https?://[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}"
on_fail: info
remediation: "Verificar URL com HEAD request. Aceitar 200, 301, 302. Rejeitar 404, 5xx, timeout."
notes: |
  - Preferir HTTPS (flag HTTP-only)
  - Timeout: 10s max
  - Aceitar redirects (301/302) como validos
  - Rejeitar paginas de parking/domain-for-sale
```

## Scoring
```yaml
completeness_score:
  4/4: "A — contato completo, pronto para outreach"
  3/4: "B — contato parcial, util para campanha"
  2/4: "C — contato basico, requer enriquecimento"
  1/4: "D — contato minimo, apenas referencia"
  0/4: "F — sem dados de contato, descartavel para CRM ativo"
minimum_viable: 2  # Minimo 2 campos validados para entrar no CRM
```

## Error Message
```
"Contact validation: {passed}/{total} checks passed. 
 Failed: {failed_fields}. Score: {completeness_score}."
```

## Bypass Policy
```yaml
allowed: false
reason: "Contatos nao-validados poluem CRM e desperdicam budget de outreach"
```

## Footer
Rule: validate-business-contact-quality | Quality: null | Domain: crm-research
