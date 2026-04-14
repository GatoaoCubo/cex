---
id: kc_audit_log
kind: knowledge_card
title: Immutable Audit Log Configuration for SOC2 Type II Compliance
version: 1.0.0
quality: null
pillar: P01
description: |
  This artifact defines the structural requirements for immutable audit logs to meet SOC2 Type II compliance standards. Audit logs must capture all system access, configuration changes, and user actions with cryptographic integrity.

  ## Key Components
  | Component        | Requirement                                                                 |
  |------------------|-----------------------------------------------------------------------------|
  | Immutability     | Logs must be write-once, tamper-proof (e.g., blockchain or hash chain)     |
  | Timestamping     | Precise UTC timestamps with sub-second resolution                          |
  | User Identification | Full user identity + IP geolocation tracking                             |
  | Event Logging    | All access attempts (success/failure), configuration changes, and system events |
  | Retention Policy | Minimum 7 years of log retention with periodic integrity checks           |

  ## Implementation Considerations
  - Use cryptographic hashing (SHA-256) for log immutability
  - Store logs in separate, air-gapped storage from operational systems
  - Implement role-based access to audit logs (only auditors/developers)
  - Include metadata: user-agent, session ID, and request payload

  ## Example
  ```
  [2026-04-05T14:23:17Z] USER: admin@company.com (IP: 192.168.1.10)
  ACTION: CONFIGURE
  RESOURCE: /api/v1/permissions
  STATUS: SUCCESS
  PAYLOAD: {"role": "auditor", "permissions": ["read", "audit"]}
  ```
---
