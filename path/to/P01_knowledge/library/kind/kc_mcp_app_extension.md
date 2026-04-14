---
id: kc_mcp_app_extension
kind: knowledge_card
title: MCP Apps Extension (SEP-1865)
version: 1.0.0
quality: null
pillar: P01
---

# MCP Apps Extension (SEP-1865)

## App Manifest
JSON file defining app metadata, capabilities, and permissions. Includes:
- Name, version, and unique identifier
- Required permissions and lifecycle hooks
- Capability declarations for sandboxed execution
- Security settings and isolation parameters

## Lifecycle
Three core events govern app behavior:
1. **Install** - Platform registration and permission requests
2. **Launch** - User-initiated execution with context setup
3. **Terminate** - Graceful shutdown and resource cleanup

## Capabilities
Declared in manifest to request:
- Network access controls
- File system operations
- UI component rendering
- Inter-process communication
- Device sensor access

## Security
- **Sandboxed Iframe**: Isolated execution environment
- **Permission Grants**: Granular access control model
- **Data Isolation**: Prevents cross-app resource sharing
- **Secure Communication**: Encrypted inter-process channels

## Compliance
Ensures:
- Platform-specific security boundaries
- Data privacy protections
- Interoperability standards
- Audit trail capabilities
