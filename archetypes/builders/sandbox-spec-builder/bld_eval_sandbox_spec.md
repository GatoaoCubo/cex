---
kind: quality_gate
id: p09_qg_sandbox_spec
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for sandbox_spec
quality: 9.0
title: "Quality Gate Sandbox Spec"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sandbox_spec, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for sandbox_spec"
domain: "sandbox_spec construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_sandbox_spec
  - sandbox-spec-builder
  - p09_qg_playground_config
  - bld_instruction_sandbox_spec
  - p11_qg_audit_log
  - p03_sp_sandbox_spec_builder
  - kc_sandbox_spec
  - p10_lr_sandbox_spec_builder
  - p09_qg_sandbox_config
  - p09_qg_rbac_policy
---

## Quality Gate

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| Isolation Level | Full | equals | All environments |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Missing or invalid frontmatter |
| H02 | ID matches pattern ^p09_sb_[a-z][a-z0-9_]+.yaml$ | ID format invalid |
| H03 | kind field matches 'sandbox_spec' | kind field incorrect |
| H04 | network_isolation field present | Missing network isolation spec |
| H05 | resource_limits defined | No resource limits specified |
| H06 | no production network connectivity | Sandbox connected to production |
| H07 | teardown_policy exists | Missing teardown procedure |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Isolation | 0.20 | 1.0 = Full isolation |
| D02 | Resource Management | 0.15 | 1.0 = Strict limits |
| D03 | Compliance | 0.15 | 1.0 = Meets enterprise standards |
| D04 | Auditability | 0.10 | 1.0 = Full logging enabled |
| D05 | Scalability | 0.10 | 1.0 = Supports 100+ concurrent users |
| D06 | Security | 0.10 | 1.0 = No external exposure |
| D07 | Documentation | 0.10 | 1.0 = Complete API docs |
| D08 | Technology Stack | 0.10 | 1.0 = Approved frameworks only |

## Actions
| Score | Action |
|---|---|
| GOLDEN >=9.5 | Auto-approve for enterprise deployment |
| PUBLISH >=8.0 | Publish to sandbox registry |
| REVIEW >=7.0 | Manual review required |
| REJECT <7.0 | Reject and request revisions |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Emergency deployment | CTO | "Bypass approved for critical incident" |
| Business continuity override | CDO | "Bypass logged per incident #XYZ" |

## Examples

## Golden Example
```markdown
---
title: "Sandbox Spec for AI Model Validation"
kind: sandbox_spec
description: "Isolated environment for evaluating enterprise AI models during procurement"
---

**Environment**
- Cloud provider: AWS
- Compute: EC2 c5.4xlarge (8 vCPU, 32 GB RAM)
- Storage: EBS gp3 500 GB (IOPS 10,000)
- Networking: VPC with private subnet, no internet gateway
- Containerization: Docker 20.10.12 with SELinux policies

**Security**
- Isolation: Separate AWS account with IAM role (SandboxAdmin) limited to VPC and EC2
- Data: Encrypted at rest (AES-256) and in transit (TLS 1.3)
- Access: SSH key pairs only, no password authentication

**Procurement Gates**
- Model validation: Must pass bias audit (AI Fairness 360) and latency benchmarks (<200ms/predict)
- Compliance: GDPR data processing agreement signed by vendor
- Exit criteria: 95% test coverage via pytest and 0 critical vulnerabilities (OWASP ZAP)
```

## Anti-Example 1: Missing Security Controls
```markdown
---
title: "Quick Test Environment"
kind: sandbox_spec
description: "Basic setup for rapid prototyping"
---

**Environment**
- Cloud provider: Azure
- Compute: VM Standard_DS3_v2
- Networking: Public IP with default security group

**Procurement Gates**
- Model validation: Basic unit tests
```
## Why it fails
No isolation controls (public IP, default security group), no data encryption, no IAM restrictions, and lacks compliance requirements. Fails to meet enterprise procurement security standards.

## Anti-Example 2: Confusing with Playground Config
```markdown
---
title: "Interactive AI Lab"
kind: sandbox_spec
description: "Jupyter notebook environment for exploratory analysis"
---

**Environment**
- Cloud provider: GCP
- Compute: AI Platform notebook instance
- Networking: Public access enabled
- Tools: Jupyter, TensorFlow, PyTorch

**Procurement Gates**
- Model validation: Optional
```
## Why it fails
Includes interactive tools (Jupyter) and public access, which are playground features. Lacks strict isolation, security controls, and mandatory compliance gates required for procurement evaluation.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
