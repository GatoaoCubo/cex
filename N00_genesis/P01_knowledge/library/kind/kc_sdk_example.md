---
id: kc_sdk_example
kind: knowledge_card
8f: F3_inject
title: SDK Example Integration Patterns
version: 1.0.0
quality: 8.8
pillar: P01
tldr: "Multi-language SDK code samples showing canonical integration patterns for API authentication and usage"
when_to_use: "When providing developers with copy-paste SDK examples in Python, JavaScript, or Java"
density_score: 1.0
related:
  - bld_output_template_sdk_example
  - bld_collaboration_sdk_example
  - sdk-example-builder
  - bld_config_sdk_example
  - bld_schema_sdk_example
  - p10_lr_sdk_example_builder
  - bld_tools_sdk_example
  - p01_kc_memory_session_compression
  - p01_kc_api_client
  - bld_instruction_sdk_example
---

# SDK Integration Patterns

This card demonstrates canonical SDK integration patterns across major languages.

## Python
```python
from cex_sdk import SDK

sdk = SDK(api_key="your_key")
response = sdk.create_project(name="Example Project")
print(response.status_code)
```

## JavaScript
```javascript
const SDK = require('cex-sdk');
const sdk = new SDK({ apiKey: 'your_key' });
sdk.createProject("Example Project")
  .then(data => console.log(data))
  .catch(err => console.error(err));
```

## Java
```java
import com.cex.sdk.SDK;

public class Example {
    public static void main(String[] args) {
        SDK sdk = new SDK("your_key");
        System.out.println(sdk.createProject("Example Project"));
    }
}
```

## Key Patterns
1. API key authentication via constructor
2. Asynchronous pattern for non-blocking I/O
3. Consistent error handling patterns
4. Type-safe method signatures
5. Environment variable support for credentials

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_sdk_example]] | downstream | 0.56 |
| [[bld_collaboration_sdk_example]] | downstream | 0.51 |
| [[sdk-example-builder]] | downstream | 0.49 |
| [[bld_config_sdk_example]] | downstream | 0.44 |
| [[bld_schema_sdk_example]] | downstream | 0.35 |
| [[p10_lr_sdk_example_builder]] | downstream | 0.33 |
| [[bld_tools_sdk_example]] | downstream | 0.30 |
| [[p01_kc_memory_session_compression]] | sibling | 0.29 |
| [[p01_kc_api_client]] | sibling | 0.25 |
| [[bld_instruction_sdk_example]] | downstream | 0.23 |
