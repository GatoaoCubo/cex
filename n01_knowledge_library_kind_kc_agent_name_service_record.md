---
id: kc_agent_name_service_record
kind: knowledge_card
title: Agent Name Service Record (ANS)
version: 1.0.0
quality: null
pillar: P01
---

The Agent Name Service Record (ANS) is a registry entry combining IETF ANS and CNCF AgentDNS standards for decentralized agent discovery. This record contains:

- **Name**: Unique identifier for the agent service
- **Endpoint**: Network address for service discovery (e.g., HTTPS endpoint)
- **PKI Certificate**: X.509 certificate for authentication and encryption
- **Protocol Adapters**: Supported communication protocols (e.g., gRPC, REST, WebSockets)
- **Service Metadata**: Version, capabilities, and operational status

This standardized record format enables machines to autonomously discover and authenticate agents across distributed systems while maintaining cryptographic security and protocol flexibility.
