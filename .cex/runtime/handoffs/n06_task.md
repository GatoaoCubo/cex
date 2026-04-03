---
mission: SDK_VALIDATION
nucleus: N06
task: smoke_test
priority: high
---

# N06 Brand/Commercial — SDK Validation Smoke Test

## Objetivo
Validar ferramentas de brand e pipeline de monetização.

## Tarefas
1. Verifique que `boot/n06.cmd` existe e aponta para modelo correto
2. Execute `python _tools/brand_validate.py` (se brand_config existir)
3. Execute `python _tools/cex_query.py "brand monetization"` e confirme resultados
4. Verifique que guardrails BR funcionam: `python -c "from cex_sdk.guardrails.pii import PIIDetectionGuardrail; g=PIIDetectionGuardrail(); print(g.check('CPF: 123.456.789-09'))"`
5. Signal: `python _tools/signal_writer.py n06 complete 9.0 SDK_VALIDATION`

## Critério de Sucesso
Boot OK, brand tools funcionais, guardrails BR detectam CPF.
