---
id: kc_agent_name_service_record
kind: knowledge_card
title: Agent Name Service Record (ANS/AgentDNS)
version: 1.0.0
quality: null
pillar: P01
---

# Agent Name Service Record (ANS/AgentDNS)

The Agent Name Service Record (ANS/AgentDNS) is a standardized registry entry for decentralized agent discovery, combining IETF ANS (RFC 8605) and CNCF AgentDNS specifications. This record enables machines to locate and authenticate agents across distributed systems.

## Core Components

1. **Name**: Unique identifier for the agent (e.g., `agent.example.com`)
2. **Endpoint**: Network address and port for agent communication (e.g., `tcp://[2001:db8::1]:5555`)
3. **PKI Certificate**: X.509 certificate for TLS/SSL authentication
4. **Protocol Adapters**: Supported communication protocols (e.g., `grpc`, `websocket`, `rest`)

## Technical Specifications

- **Discovery Mechanism**: DNS-based lookup with TXT records for metadata
- **Security**: Requires TLS 1.2+ with certificate pinning
- **Versioning**: Semver-compatible versioning for protocol updates
- **TTL**: Time-to-live for DNS record caching (default 3600 seconds)

## Use Cases

- Service discovery in microservices architectures
- Secure agent-to-agent communication
- Distributed system monitoring and management
- API gateway routing based on agent identity

## Implementation Notes

- Must include both ANS and AgentDNS fields for cross-compatibility
- Certificate authority must be trusted by all participating nodes
- Protocol adapters should follow RFC 7546 for secure transport
- Regularly update records to reflect protocol version changes
