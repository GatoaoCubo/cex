---
id: kc_sdk_example
kind: knowledge_card
title: SDK Example Integration Patterns
version: 1.0.0
quality: 8.8
pillar: P01
density_score: 1.0
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
