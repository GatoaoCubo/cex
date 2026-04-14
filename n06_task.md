---
id: kc_sdk_example
kind: knowledge_card
title: SDK Example: Canonical Integration Patterns
version: 1.0.0
quality: null
pillar: P01
---

# SDK Integration Patterns

## Python
```python
from cex_sdk import Client

client = Client(api_key="your_api_key")
response = client.create_project(
    name="Example Project",
    description="SDK integration demo"
)
print(response.status_code)
```

## JavaScript
```javascript
const { Client } = require("cex-sdk");

async function run() {
    const client = new Client({ apiKey: "your_api_key" });
    const response = await client.createProject({
        name: "Example Project",
        description: "SDK integration demo"
    });
    console.log(response.status);
}
run();
```

## Java
```java
import com.cex.sdk.Client;

public class SdkExample {
    public static void main(String[] args) {
        Client client = new Client("your_api_key");
        var response = client.createProject("Example Project", "SDK integration demo");
        System.out.println(response.getStatusCode());
    }
}
```

## C#
```csharp
using Cex.Sdk;

class Program {
    static void Main() {
        var client = new Client("your_api_key");
        var response = client.CreateProject("Example Project", "SDK integration demo");
        Console.WriteLine(response.StatusCode);
    }
}
```

## Key Patterns
1. API key authentication via constructor
2. Method chaining for request building
3. Asynchronous pattern support
4. Consistent response object structure
5. Null safety pattern implementation
