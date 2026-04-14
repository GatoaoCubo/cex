---
id: kc_mcp_app_extension
kind: knowledge_card
title: MCP Apps Extension (SEP-1865)
version: 1.0.0
quality: null
pillar: P01
---

# MCP Apps Extension (SEP-1865)

## Overview
MCP Apps Extension (SEP-1865) defines a standardized framework for creating and managing sandboxed applications within the CEX ecosystem. This extension enables developers to create modular, secure, and scalable applications that integrate seamlessly with the platform.

## App Manifest
The app manifest is a JSON file that describes the application's metadata, capabilities, and configuration. It includes:
- Application name and version
- Required permissions
- Lifecycle events (install, launch, terminate)
- Capability declarations
- Security settings

## Lifecycle
The MCP Apps Extension manages the application lifecycle through three key events:
1. **Install**: Triggered when the app is first added to the platform
2. **Launch**: Initiated when the user interacts with the app
3. **Terminate**: Called when the app is removed or closed

## Capabilities
Apps can declare various capabilities through the manifest, including:
- Network access
- File system operations
- Device sensors
- Inter-process communication
- Custom API endpoints

## Permissions
Permission grants are managed through a granular access control system:
- **Runtime permissions**: Granted during app execution
- **Persistent permissions**: Stored in the app's security profile
- **Revocation**: Supported through the platform's permission management interface

## Sandboxed Iframe
The extension provides a sandboxed iframe environment for:
- Secure UI rendering
- Isolated execution contexts
- Resource containment
- Security boundary enforcement
- Cross-origin communication

## Conclusion
The MCP Apps Extension enables developers to create secure, scalable applications that integrate seamlessly with the CEX platform. Its sandboxed execution model, granular permission system, and standardized manifest format provide a robust foundation for building modern applications.
