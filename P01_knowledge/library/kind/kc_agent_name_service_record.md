---
id: kc_agent_name_service_record
kind: knowledge_card
title: Agent Name Service Record (ANS)
version: 1.0.0
quality: null
pillar: P01
---

# Agent Name Service Record (ANS)

**Description**:  
A registry record format for agent discovery, combining IETF ANS (Agent Name Service) and CNCF AgentDNS specifications. Contains:  
- **Name**: Unique agent identifier  
- **Endpoint**: Network address for communication  
- **PKI Certificate**: X.509 certificate for authentication  
- **Protocol Adapters**: Supported communication protocols (e.g., gRPC, REST, WebSockets)  

This record enables decentralized agent discovery in distributed systems, providing cryptographic validation and protocol compatibility metadata. Used by CNCF AgentDNS for service registry and IETF ANS for name resolution.
