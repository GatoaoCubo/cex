---
id: kc_agent_name_service_record
kind: knowledge_card
title: Agent Name Service Record (ANS/AgentDNS)
version: 1.0.0
quality: null
pillar: P01
---

The **Agent Name Service Record (ANS/AgentDNS)** is a hybrid registry format combining IETF ANS (Application Naming Service) and CNCF AgentDNS specifications. It enables decentralized agent discovery by storing structured metadata in DNS-compatible records.

Key fields include:
- **name**: Unique agent identifier (e.g., `agent.example.org`)
- **endpoint**: Protocol-specific service address (e.g., `https://api.example.org/agent`)
- **PKI cert**: X.509 certificate for TLS authentication
- **protocol adapters**: List of supported communication protocols (e.g., `grpc`, `websocket`, `rest`)

This record type facilitates:
1. Service discovery across distributed systems
2. Secure endpoint verification via PKI
3. Protocol-agnostic communication routing
4. Integration with both DNS and service mesh ecosystems

The format balances IETF's standardized DNS semantics with CNCF's cloud-native flexibility, enabling agents to participate in both traditional and modern service discovery networks.
