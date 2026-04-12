---
id: kc_model_context_protocol
kind: knowledge_card
title: "Model Context Protocol (MCP)"
version: 1.0.0
quality: null
pillar: P01
---

# Model Context Protocol (MCP)

## What is MCP?
MCP (Model Context Protocol) is a communication protocol developed by Anthropic to enable structured context sharing between client applications and Claude models. It provides a standardized way to pass tools, resources, and prompts to models while maintaining context across interactions.

## Architecture
MCP operates on a server/client model:
- **Client**: Application requesting model interactions
- **Server**: Anthropic's API endpoint handling requests
- **Model**: Claude model executing tasks with provided context

## Primitives
MCP defines three core primitives:
1. **Tools**: Custom functions available to the model
2. **Resources**: External data sources for reference
3. **Prompts**: Structured instructions for model behavior

## CEX Integration
CEX uses MCP through `.mcp-n0X.json` configuration files:
- Define tool/resource/prompt mappings for each nucleus (n01-n07)
- Enable context persistence across multiple interactions
- Support structured data passing without raw text

## Comparison with Function Calling
| Feature          | MCP                          | Function Calling              |
|------------------|------------------------------|------------------------------|
| Context Sharing  | ✅ Structured, persistent    | ❌ Limited to single request  |
| Data Passing     | ✅ Type-safe, structured     | ✅ But requires explicit formatting |
| Reusability      | ✅ Predefined tool/resource  | ❌ Requires per-call setup   |
| Complexity       | ✅ Simplifies complex workflows | ✅ Effective for simple tasks |

MCP enables CEX to maintain consistent context across multiple nucleus interactions, improving efficiency and reducing errors in complex workflows.
```