---
kind: examples
id: bld_examples_sandbox_spec
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of sandbox_spec artifacts
quality: 8.9
title: "Examples Sandbox Spec"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sandbox_spec, builder, examples]
tldr: "Golden and anti-examples of sandbox_spec artifacts"
domain: "sandbox_spec construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

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
