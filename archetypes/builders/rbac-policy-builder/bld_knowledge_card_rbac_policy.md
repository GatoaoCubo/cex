---
kind: knowledge_card
id: bld_knowledge_card_rbac_policy
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for rbac_policy production
quality: 9.2
title: "Knowledge Card Rbac Policy"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [rbac_policy, builder, knowledge_card]
tldr: "Domain knowledge for rbac_policy production"
domain: "rbac_policy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Domain Overview
Role-based access control (RBAC) is a foundational mechanism for enforcing multi-tenant isolation in cloud and enterprise systems. By assigning permissions to roles rather than individual users, RBAC ensures that tenants cannot access resources outside their allocated scope. This model aligns with principles like least privilege and separation of duties, critical for compliance in regulated industries. Multi-tenant isolation relies on RBAC to prevent cross-tenant data leakage while enabling scalable, policy-driven access management.

RBAC policies must balance flexibility with strict boundary enforcement. For example, in a SaaS environment, roles like "Tenant Admin" or "Service User" are scoped to specific tenants, ensuring isolation through role-tenant mappings. Standards such as NIST SP 800-53 and ISO/IEC 27001 emphasize RBAC as a core control for securing shared infrastructure.

## Key Concepts
| Concept         | Definition                                                                 | Source                          |
|-----------------|----------------------------------------------------------------------------|---------------------------------|
| Role            | A set of permissions grouped by function (e.g., "Database Reader").        | NIST SP 800-53                  |
| Permission      | An atomic right to perform an action (e.g., "read /tenant/data").         | XACML 3.0                       |
| Tenant          | A logical partition of resources isolated from other tenants.             | Cloud Security Alliance         |
| Role Hierarchy  | Inheritance of permissions from higher-level roles (e.g., "Manager" → "User"). | ISO/IEC 27001                   |
| Separation of Duty | Ensuring no single role holds conflicting permissions.                  | NIST SP 800-53                  |
| Least Privilege | Granting only necessary permissions to fulfill a role’s purpose.          | RFC 7613                        |
| Role Tenant Mapping | Linking roles to specific tenants for isolation.                        | OASIS RBAC 3.0                  |
| Policy Rule     | A condition that governs role assignment or permission enforcement.       | XACML 3.0                       |

## Industry Standards
- NIST SP 800-53 (Access Control and Authentication)
- ISO/IEC 27001 (Information Security Management)
- XACML 3.0 (eXtensible Access Control Markup Language)
- OASIS RBAC 3.0 (Role-Based Access Control Reference Model)
- RFC 7613 (OAuth 2.0 Token Revocation)
- Cloud Security Alliance (CSA) Security Guidance

## Common Patterns
1. **Tenant-specific role scoping** – Bind roles to tenant identifiers in policy rules.
2. **Hierarchical role inheritance** – Use parent roles to propagate permissions across sub-roles.
3. **Dynamic role assignment** – Automate role creation/revocation based on tenant lifecycle events.
4. **Attribute-based access control (ABAC)** – Augment RBAC with tenant-specific attributes (e.g., department).
5. **Cross-tenant audit trails** – Log role-permission changes per tenant for compliance.

## Pitfalls
- **Over-permissive default roles** – Granting broad permissions without tenant-specific constraints.
- **Ignoring tenant boundary checks** – Failing to enforce isolation in role-tenant mappings.
- **Static role definitions** – Not updating roles to reflect changing tenant needs or compliance requirements.
- **Lack of auditability** – Missing logging of role assignments and policy modifications.
- **Role explosion** – Creating excessive roles for granular control, increasing management complexity.
