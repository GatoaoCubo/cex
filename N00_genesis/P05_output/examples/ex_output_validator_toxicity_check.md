---
id: p05_ov_toxicity_pii_check
kind: output_validator
pillar: P05
title: Toxicity + PII Post-LLM Validator
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: output_safety
quality: 9.1
tags: [output-validator, toxicity, pii, guardrails, safety, nemo, retry, content-filter]
tldr: Validator pos-LLM que checa toxicidade (Perspective API) e PII (regex + spaCy NER) em output antes de entregar ao usuario — on_fail=retry_with_warning, max_retries=2
when_to_use: Qualquer agente organization que gera texto user-facing — especialmente copy de marketing, respostas de chatbot, e conteudo publicavel em redes sociais
related:
  - bld_tools_content_filter
  - bld_output_template_content_filter
  - p01_kc_output_validator
  - n06_audit_content_filter_builder
  - kc_guardrail
  - p01_kc_lens
  - bld_knowledge_card_content_filter
  - n06_api_access_pricing
---

# Output Validator: Toxicity + PII Check

## Overview
Validator de duas camadas que intercepta output do LLM antes de entregar ao usuario ou publicar. Camada 1 detecta conteudo toxico (hate speech, profanity, harassment) via Perspective API. Camada 2 detecta PII (CPF, email, telefone, endereco) via regex patterns + spaCy NER. Se qualquer check falhar, retry com warning injetado no prompt; apos max_retries, retornar fallback seguro.

## Checks
| Check | Engine | Threshold | Severity |
|-------|--------|-----------|----------|
| Toxicity | Perspective API (`TOXICITY` attribute) | score > 0.7 | critical |
| Severe toxicity | Perspective API (`SEVERE_TOXICITY`) | score > 0.5 | critical |
| Profanity | Perspective API (`PROFANITY`) | score > 0.8 | warning |
| Identity attack | Perspective API (`IDENTITY_ATTACK`) | score > 0.6 | critical |
| CPF | Regex `\d{3}\.?\d{3}\.?\d{3}-?\d{2}` | any match | critical |
| Email | Regex `[\w.-]+@[\w.-]+\.\w+` | any match | high |
| Phone (BR) | Regex `\(?\d{2}\)?\s?\d{4,5}-?\d{4}` | any match | high |
| Person name | spaCy NER (`PER` entity) | confidence > 0.85 | medium |
| Address | spaCy NER (`LOC` + pattern: "Rua/Av/Alameda") | confidence > 0.80 | medium |

## Parameters
| Param | Value | Rationale |
|-------|-------|-----------|
| on_fail | retry_with_warning | Dar ao modelo chance de se corrigir antes de fallback |
| max_retries | 2 | 2 retries = 3 tentativas total. Alem disso, modelo provavelmente nao consegue corrigir |
| fallback_response | "Desculpe, nao consigo gerar uma resposta adequada para este pedido." | Mensagem segura e neutra |
| perspective_api_url | https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze | Google Perspective API |
| spacy_model | pt_core_news_lg | Modelo portugues large para NER |
| log_violations | true | Registrar todas violacoes para auditoria (sem incluir o PII detectado) |
| async_check | false | Sincrono — output nao deve ser entregue antes da validacao |

## Architecture
```text
[LLM Output] --> [Toxicity Check (Perspective API)]
                        |
                  toxic? (score > threshold)
                   /              \
                 yes               no
                  |                 |
          [Log violation]    [PII Check (regex + spaCy)]
                  |                 |
                  |           pii_found?
                  |            /        \
                  |          yes         no
                  |           |           |
                  |    [Log violation]  [PASS -> deliver to user]
                  |           |
                  +-----+-----+
                        |
                  retries < max_retries?
                   /              \
                 yes               no
                  |                 |
          [Retry with warning]  [Return fallback_response]
                  |
          [Inject warning into prompt:]
          "Sua resposta anterior continha
           {toxicity|PII}. Reescreva sem
           {conteudo toxico|dados pessoais}."
                  |
          [LLM generates new output]
                  |
          [Loop back to Toxicity Check]
```

## Implementation
```python
from googleapiclient import discovery
import spacy
import re

nlp = spacy.load("pt_core_news_lg")

# PII patterns (Brazilian)
PII_PATTERNS = {
    "cpf": re.compile(r"\d{3}\.?\d{3}\.?\d{3}-?\d{2}"),
    "email": re.compile(r"[\w.-]+@[\w.-]+\.\w+"),
    "phone_br": re.compile(r"\(?\d{2}\)?\s?\d{4,5}-?\d{4}"),
    "cep": re.compile(r"\d{5}-?\d{3}"),
}

def check_toxicity(text: str, api_key: str) -> dict:
    """Check text toxicity via Perspective API."""
    client = discovery.build("commentanalyzer", "v1alpha1",
                             developerKey=api_key,
                             static_discovery=False)
    request = {
        "comment": {"text": text},
        "languages": ["pt"],
        "requestedAttributes": {
            "TOXICITY": {},
            "SEVERE_TOXICITY": {},
            "PROFANITY": {},
            "IDENTITY_ATTACK": {},
        }
    }
    response = client.comments().analyze(body=request).execute()
    scores = {
        attr: response["attributeScores"][attr]["summaryScore"]["value"]
        for attr in request["requestedAttributes"]
    }
    return scores

def check_pii(text: str) -> list[dict]:
    """Detect PII via regex + spaCy NER."""
    violations = []
    # Regex checks
    for pii_type, pattern in PII_PATTERNS.items():
        matches = pattern.findall(text)
        if matches:
            violations.append({
                "type": pii_type,
                "count": len(matches),
                "severity": "critical" if pii_type == "cpf" else "high",
            })
    # NER checks
    doc = nlp(text)
    person_ents = [ent for ent in doc.ents if ent.label_ == "PER"]
    if person_ents:
        violations.append({
            "type": "person_name",
            "count": len(person_ents),
            "severity": "medium",
        })
    return violations

def validate_output(text: str, api_key: str, max_retries: int = 2) -> dict:
    """Full validation pipeline."""
    toxicity = check_toxicity(text, api_key)
    toxic_flags = {k: v for k, v in toxicity.items() if (
        (k == "TOXICITY" and v > 0.7) or
        (k == "SEVERE_TOXICITY" and v > 0.5) or
        (k == "PROFANITY" and v > 0.8) or
        (k == "IDENTITY_ATTACK" and v > 0.6)
    )}
    pii_violations = check_pii(text)
    critical_pii = [v for v in pii_violations if v["severity"] in ("critical", "high")]

    return {
        "passed": len(toxic_flags) == 0 and len(critical_pii) == 0,
        "toxicity_scores": toxicity,
        "toxic_flags": toxic_flags,
        "pii_violations": pii_violations,
        "action": "deliver" if not toxic_flags and not critical_pii else "retry",
    }
```

## Retry Warning Templates
```python
RETRY_WARNINGS = {
    "toxicity": (
        "Sua resposta anterior foi sinalizada por conteudo potencialmente "
        "inadequado (toxicity score > threshold). Reescreva mantendo o mesmo "
        "conteudo informativo mas com tom neutro e profissional."
    ),
    "pii": (
        "Sua resposta anterior continha dados pessoais identificaveis "
        "(CPF, email, telefone ou nome real). Reescreva substituindo "
        "qualquer dado pessoal por placeholders genericos (ex: [EMAIL], [CPF])."
    ),
    "both": (
        "Sua resposta anterior continha conteudo inadequado E dados pessoais. "
        "Reescreva com tom profissional e sem nenhum dado pessoal real."
    ),
}
```

## Monitoring
| Metric | Alert Threshold | Dashboard |
|--------|-----------------|-----------|
| Toxicity trigger rate | > 5% of outputs | Grafana: organization/output-safety |
| PII leak rate | > 1% of outputs | Grafana: organization/output-safety |
| Retry success rate | < 80% (retries not fixing issue) | Grafana: organization/output-safety |
| Fallback rate | > 2% of outputs | PagerDuty: critical |
| Perspective API latency | p99 > 500ms | Grafana: organization/external-apis |

## When NOT to Use
- Internal agent-to-agent communication — overhead desnecessario, contexto e confiavel
- Code generation outputs — false positives em variable names e test data
- Dados ja anonimizados — PII check redundante

## Related
- `ex_constraint_spec_json_output.md` — Constraint na geracao (pre-LLM); este validator e pos-LLM
- `ex_response_format_security_audit.md` — Response format que pode conter dados sensiveis (precisa deste validator)
- `ex_naming_rule_cex_naming.md` — Naming conventions (este validator nao checa naming)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_content_filter]] | upstream | 0.24 |
| [[bld_output_template_content_filter]] | related | 0.23 |
| [[p01_kc_output_validator]] | upstream | 0.19 |
| [[n06_audit_content_filter_builder]] | downstream | 0.19 |
| [[kc_guardrail]] | upstream | 0.19 |
| [[p01_kc_lens]] | upstream | 0.18 |
| [[bld_knowledge_card_content_filter]] | upstream | 0.18 |
| [[n06_api_access_pricing]] | downstream | 0.16 |
