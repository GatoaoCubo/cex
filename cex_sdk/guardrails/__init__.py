"""
cex_sdk.guardrails — Input/Output Safety Layer

Absorbed from: agno/guardrails/
CEX version: 7.3.0
Pillar: P07 (Evals)
8F functions: CONSTRAIN (F1, input), GOVERN (F7, output)

Provides:
  - BaseGuardrail: ABC for custom guardrails
  - PIIDetectionGuardrail: regex PII detection (SSN, CC, email, phone + BR)
  - PromptInjectionGuardrail: prompt injection pattern detection
  - OpenAIModerationGuardrail: OpenAI moderation API wrapper
"""
