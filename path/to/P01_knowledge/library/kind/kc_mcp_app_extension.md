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
MCP Apps Extension (SEP-1865) defines a standardized framework for creating and managing sandboxed applications within the CEX ecosystem. It enables developers to build modular, secure, and isolated applications that integrate seamlessly with the platform.

## Key Concepts
- **App Manifest**: A JSON file describing the app's metadata, capabilities, and permissions.
- **Lifecycle Events**: Install, launch, and terminate events trigger specific actions during app interaction.
- **Capabilities**: Define the app's functionality (e.g., data access, UI components).
- **Permission Grants**: Explicit user authorization for sensitive operations.
- **Sandboxed Iframe**: Isolated execution environment for app UI components.

## Lifecycle
1. **Install**: App is registered with the system and permissions are requested.
2. **Launch**: User initiates app execution, triggering the launch event.
3. **Terminate**: App is closed or suspended, triggering the terminate event.

## Capabilities
- **Data Access**: Read/write permissions for specific data types.
- **UI Components**: Custom UI elements rendered in sandboxed iframes.
- **Event Handling**: Respond to platform events (e.g., user actions, system signals).

## Permissions
- **User Consent**: Required for sensitive operations (e.g., data access, network requests).
- **Granular Control**: Fine-grained permission management for different app features.

## Sandboxed Iframe
- **Isolation**: Apps run in isolated environments to prevent cross-app interference.
- **Security**: Restricts access to system resources and prevents malicious activity.
- **Communication**: Secure messaging between the host and sandboxed components.

## Conclusion
MCP Apps Extension provides a robust framework for building secure, modular applications. By leveraging sandboxed iframes and granular permissions, developers can create powerful extensions that integrate seamlessly with the CEX platform while maintaining system integrity.
