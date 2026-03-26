---
pillar: P01
llm_function: INJECT
purpose: Standards and patterns for guardrail production
sources: [NIST AI RMF, OWASP LLM Top 10, Anthropic Usage Policy, CEX Laws]
---

# Domain Knowledge: guardrail

## Foundational Concepts
Guardrails originate from safety engineering (physical barriers preventing harm).
In AI: constraints on model behavior to prevent harmful outputs or actions.
In CEX: declarative restrictions applied externally to agents and artifacts to prevent damage.

## Industry Patterns
| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| NIST AI RMF | Risk management framework for AI systems | Severity classification + enforcement |
| OWASP LLM Top 10 | Security risks for LLM applications | Specific violation categories |
| Anthropic Usage Policy | Acceptable use constraints | Content and behavior boundaries |
| AWS Bedrock Guardrails | Content filters, denied topics, word filters | Block/warn/log enforcement modes |
| LangChain Guardrails | Input/output validation for LLM chains | Runtime constraint enforcement |

## Key Principles
- Guardrails PREVENT DAMAGE, not ensure quality (that is quality_gate)
- Guardrails are EXTERNAL to the agent (agent cannot disable its own guardrails)
- Severity determines response: critical=block, high=block+alert, medium=warn, low=log
- Every guardrail needs a BYPASS for emergencies (with audit trail)
- Rules must be CONCRETE and ENFORCEABLE (no "be responsible")
- Violation examples must be SPECIFIC (not "bad things")

## CEX-Specific Extensions
| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| scope | What the guardrail protects (agent, pipeline, output) | NIST: system boundary |
| enforcement | How violation is handled (block/warn/log) | AWS Bedrock: filter action |
| severity | Impact classification (critical/high/medium/low) | NIST: risk level |

## Boundary vs Nearby Types
| Type | What it does | NOT this |
|------|-------------|----------|
| permission (P09) | Controls WHO can ACCESS what (read/write/execute) | Does NOT prevent harmful behavior |
| law (P08) | Defines OPERATIONAL rules (inviolable, architectural) | Does NOT constrain agent safety |
| quality_gate (P11) | Ensures QUALITY with scoring (pass/fail) | Does NOT prevent damage |
| lifecycle_rule (P11) | Manages FRESHNESS and archival (time-based) | Does NOT enforce safety |

## References
- NIST AI Risk Management Framework: https://www.nist.gov/artificial-intelligence/ai-risk-management-framework
- OWASP LLM Top 10: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- AWS Bedrock Guardrails: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html
