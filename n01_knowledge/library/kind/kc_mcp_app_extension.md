---
id: kc_mcp_app_extension
kind: knowledge_card
title: MCP Apps Extension (SEP-1865)
version: 1.0.0
quality: null
pillar: P01
---

# MCP Apps Extension (SEP-1865)

## Core Concepts
- **App Manifest**: JSON metadata defining app identity, capabilities, and permissions
- **Lifecycle Events**: install/launch/terminate workflow for app deployment
- **Sandboxed Iframe**: Isolated execution environment for app content

## Key Features
- **Permission Model**: Granular access controls for device resources
- **Capability Framework**: Defined API interfaces for app functionality
- **Security Isolation**: Runtime sandboxing to prevent system interference

## Technical Specifications
- **Manifest Structure**:
  ```json
  {
    "name": "App Name",
    "version": "1.0.0",
    "permissions": ["camera", "storage"],
    "capabilities": ["network", "ui"]
  }
  ```
- **Lifecycle Callbacks**:
  - `onInstall()`: Initialization logic
  - `onLaunch(args)`: Entry point with parameters
  - `onTerminate()`: Cleanup operations

## Security Considerations
- **Sandboxing**: Apps run in isolated iframe with restricted DOM access
- **Permission Grants**: Explicit user approval required for sensitive operations
- **Resource Limits**: Memory and CPU usage caps to prevent abuse

## Implementation Guide
1. Create manifest file with required metadata
2. Implement lifecycle callbacks for app behavior
3. Request necessary permissions via user interface
4. Package app with security sandbox configuration
5. Deploy through MCP app management system
