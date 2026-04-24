---
# TEMPLATE: Interface (P06 Schema)
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P06_schema/_schema.yaml (types.interface)
# Max 3072 bytes

id: p06_iface_{{CONTRACT_SLUG}}
kind: interface
8f: F1_constrain
pillar: P06
title: "Interface: {{PRODUCER}} -> {{CONSUMER}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{AGENT_GROUP_NAME}}
quality: {{QUALITY_8_TO_10}}
tags: [interface, contract, {{TAG1}}]
tldr: "{{ONE_SENTENCE_ON_TRANSFER_CONTRACT}}"
density_score: {{0.85_TO_1.00}}
linked_artifacts:
  workflow: {{p12_wf_name_OR_null}}
  handoff: {{p12_ho_name_OR_null}}
---

# Interface: {{PRODUCER}} -> {{CONSUMER}}

## Contract Overview
| Property | Value |
|----------|-------|
| Producer | {{PRODUCER}} |
| Consumer | {{CONSUMER}} |
| Channel | {{handoff|api|signal|file}} |
| Encoding | {{utf-8|json|yaml}} |

## Required Fields
| Field | Type | Required | Example |
|-------|------|----------|---------|
| {{FIELD_1}} | {{TYPE_1}} | yes | {{EXAMPLE_1}} |
| {{FIELD_2}} | {{TYPE_2}} | yes | {{EXAMPLE_2}} |
| {{FIELD_3}} | {{TYPE_3}} | no | {{EXAMPLE_3}} |

## Constraints
1. {{REGRA_CONTRATUAL_1}}
2. {{REGRA_CONTRATUAL_2}}
3. {{REGRA_CONTRATUAL_3}}

## Failure Protocol
- Reject when: {{CONDICAO_BLOQUEANTE}}
- Retry when: {{CONDICAO_REPROCESSAVEL}}
- Signal: {{EVENTO_OU_LOG_DE_FALHA}}
