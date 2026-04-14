---
id: kc_mcp_app_extension
kind: knowledge_card
title: MCP Apps Extension (SEP-1865)
version: 1.0.0
quality: null
pillar: P01
---

**Description**:  
MCP Apps Extension (SEP-1865) defines a framework for extending applications through sandboxed, isolated environments. It enables app manifest management, lifecycle control (install/launch/terminate), capability-based permissions, and secure sandboxed iframe execution.

**Key Components**:  
- **App Manifest**: Structured metadata defining app identity, version, required capabilities, and permissions.  
- **Lifecycle Events**:  
  - *Install*: Registers the app with the system.  
  - *Launch*: Initiates execution in a sandboxed iframe.  
  - *Terminate*: Gracefully shuts down the app instance.  
- **Capabilities**: Explicitly declared permissions (e.g., network access, storage) that the app can request.  
- **Permission Grants**: Dynamic authorization model for accessing system resources.  
- **Sandboxed Iframe**: Isolated execution environment to prevent cross-origin vulnerabilities and enforce security boundaries.  

**Purpose**:  
Enables secure, modular app extensions while maintaining system integrity and user privacy.
