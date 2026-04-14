---
id: kc_agent_name_service_record
kind: knowledge_card
title: Agent Name Service Record
version: 1.0.0
quality: null
pillar: P01
---

# Agent Name Service Record

The Agent Name Service Record (ANSR) is a standardized format for registering and discovering AI agents across distributed systems. It contains:

1. **Name**: Unique identifier for the agent (e.g., `n03-builder`)
2. **Endpoint**: Network address for agent communication (e.g., `ws://agent-api.example.com`)
3. **PKI Certificate**: X.509 certificate for secure authentication
4. **Protocol Adapters**: Supported communication protocols (e.g., `websocket`, `grpc`, `http`)
5. **Metadata**: Additional information about the agent's capabilities

This record enables:
- Decentralized agent discovery
- Secure inter-agent communication
- Versioned service discovery
- Policy enforcement for agent interactions

The record is implemented as a JSON-LD document with:
- Version control for schema evolution
- Timestamped metadata
- Reference to the agent's cryptographic key
- Hashes of the agent's service definition
- Provenance chain of agent deployment steps
