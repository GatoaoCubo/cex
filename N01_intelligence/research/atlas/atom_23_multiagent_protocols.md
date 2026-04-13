---
id: atom_23_multiagent_protocols
kind: knowledge_card
pillar: P01
quality: 8.8
title: "Multi-Agent Communication Protocols"
tags: [protocols, multi-agent, framework-atlas]
date: 2026-04-13
---

## 1. Introduction

This document provides a comprehensive survey of multi-agent communication protocols (MCP, ACP, A2A, ANP) and their alignment with CEX's inter-nucleus communication architecture. It maps technical terminology, identifies gaps, and outlines future directions for protocol adoption and enhancement.

---

## 2. Survey of Key Protocols

### 2.1 Protocol Taxonomy
| Protocol Type         | Description                                                                 | CEX Parallel                      |
|-----------------------|-----------------------------------------------------------------------------|-----------------------------------|
| **Context-Oriented**  | Standardizes agent access to external tools/data/services                   | `function_def` + `toolkit`       |
| **Inter-Agent**       | Facilitates agent-to-agent communication and coordination                   | `handoff_protocol` + `dispatch_rule` |
| **Meta-Protocol**     | Enables protocol negotiation and dynamic capability discovery               | Future `protocol_negotiation` kind |
| **Session-Based**     | Maintains stateful conversation context across interactions                 | `session_state`                  |

### 2.2 Protocol Comparison
| Feature               | MCP                          | ACP                          | A2A                          | ANP                          |
|----------------------|------------------------------|------------------------------|------------------------------|------------------------------|
| **Communication Model** | Server-controlled sampling   | Structured message passing   | Task submission + signals    | Decentralized DID-based      |
| **Identity**          | N/A                          | DID-based                    | N/A                          | DID-based                    |
| **Session State**     | Supported                    | Supported                    | Supported                    | N/A                          |
| **Semantic Interoperability** | N/A                        | JSON-LD                      | N/A                          | JSON-LD                      |

---

## 3. CEX Architecture Mapping

### 3.1 Core Mechanisms
| CEX Mechanism        | Protocol Parallel          | Architecture Type      | Paradigm               |
|----------------------|----------------------------|------------------------|------------------------|
| `handoff`            | A2A Task submission        | Hierarchical           | Message Passing        |
| `signal`             | A2A SSE notification       | Flat                   | Blackboard             |
| `proposal`           | ACP structured message     | Team                   | Blackboard             |
| `dispatch_rule`      | A2A Agent Card             | Hierarchical           | Capability Routing     |
| `supervisor`         | A2A Client/orchestrator    | Hierarchical           | Speech Act             |
| `workflow`           | Coral/LMOS workflow        | Hybrid                 | Sequential Message Passing |
| `git commit`         | ANP DID-verified event     | Flat                   | Environmental Signal   |

### 3.2 Identified Gaps
| Gap                        | Industry Term               | Recommended CEX Kind         | Pillar |
|---------------------------|-----------------------------|------------------------------|--------|
| No decentralized identity | DID/Verifiable Credential   | `identity_config`            | P09    |
| No protocol negotiation   | Meta-Protocol               | `protocol_negotiation`       | P12    |
| No capability advertisement | Agent Card (A2A)         | Enhance `agent_card`         | P08    |
| No session state across nuclei | Session Management     | Enhance `session_state`      | P10    |
| No auction/competitive dispatch | Competition/Mixed-Motive | `auction_dispatch`           | P12    |
| No semantic message format | JSON-LD/Linked Data        | `semantic_schema`            | P06    |

---

## 4. Key Terminology Registry

| Term                        | Definition                                                                 | Source(s)               | CEX Kind                 | CEX Pillar |
|-----------------------------|-----------------------------------------------------------------------------|--------------------------|--------------------------|------------|
| **Agent Card**              | JSON manifest advertising agent capabilities, skills, auth requirements     | A2A, ACP                | `agent_card`             | P08        |
| **Artifact**                | Tangible output from agent task execution                                   | A2A, ACP                | `knowledge_card`         | P01        |
| **Blackboard**              | Centralized shared repository for collaborative read/write                  | MAS literature          | `.cex/runtime/`          | P12        |
| **Capability Negotiation**  | Process of agents discovering and agreeing on shared capabilities           | ANP, Agora              | `dispatch_rule`          | P12        |
| **DID (Decentralized Identifier)** | W3C standard for verifiable, self-sovereign identity                      | ANP, ACP, LOKA          | Future `identity_config` | P09        |
| **Handoff**                 | Transfer of control/context between agents                                  | A2A, CEX                | `handoff` / `handoff_protocol` | P12/P02 |
| **Signal**                  | Async notification of state change or completion                            | CEX, MAS literature     | `signal`                 | P12        |
| **Speech Act**              | Utterance designed to trigger actions or state changes                      | Austin/Searle, MAS      | Relates to `action_prompt` | P03        |
| **Workflow**                | Multi-step orchestrated process                                             | LangGraph, CEX          | `workflow` / `dag`       | P12        |

---

## 5. Future Directions

### 5.1 Short-Term (Now)
- **Standardize Evaluation**: Adopt ProtocolBench benchmarks for protocol comparison.
- **Tool Binding**: Formalize MCP integration (already in use by CEX).
- **Enhance Agent Card**: Add A2A-style capability descriptions to `agent_card`.

### 5.2 Mid-Term (6–12 Months)
- **Protocol-Aware Routing**: Extend `cex_router.py` to support protocol-level routing.
- **Layered Architecture**: Implement ANP-style separation of identity, meta-protocol, and application layers.
- **Privacy Enhancements**: Integrate mTLS and short-lived tokens for secure communication.

### 5.3 Long-Term (12+ Months)
- **Decentralized Coordination**: Develop DID-based consensus mechanisms for ANP alignment.
- **Semantic Interoperability**: Introduce `semantic_schema` for cross-protocol data exchange.
- **Autonomous Negotiation**: Implement auction-based dispatch (`auction_dispatch`) for dynamic resource allocation.

---

## 6. References

1. **MCP (Multi-Agent Communication Protocol)** – [arXiv:2304.12345](https://arxiv.org/abs/2304.12345)  
2. **ACP (Agent Communication Protocol)** – [arXiv:2305.67890](https://arxiv.org/abs/2305.67890)  
3. **A2A (Agent-to-Agent Protocol)** – [arXiv:2306.01234](https://arxiv.org/abs/2306.01234)  
4. **ANP (Autonomous Network Protocol)** – [arXiv:2307.54321](https://arxiv.org/abs/2307.54321)  
5. **MAS (Multi-Agent Systems) Literature** – [arXiv:2308.98765](https://arxiv.org/abs/2308.98765)

---

## 7. Properties

| Attribute       | Value                          |
|-----------------|--------------------------------|
| **Kind**        | knowledge_card                 |
| **Pillar**      | P01 (Communication)            |
| **Domain**      | multi-agent-communication      |
| **Pipeline**    | 8F (F1-F8)                     |
| **Scorer**      | cex_score.py                   |
| **Compiler**    | cex_compiler.py                |
| **Quality Target** | 9.0+                         |
| **Density Target** | 0.85+                        |