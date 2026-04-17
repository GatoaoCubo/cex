---
kind: output_template
id: bld_output_template_api_reference
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for api_reference production
quality: 8.8
title: "Output Template Api Reference"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [api_reference, builder, output_template]
tldr: "Template with vars for api_reference production"
domain: "api_reference construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p06_ar_{{name}}.md
title: {{title}}
description: {{description}}
pillar: P06
quality: null
tags: [{{tags}}]
---
```

<!-- {{id}}: Generated filename following p06_ar_[a-z][a-z0-9_]+.md$ -->
<!-- {{title}}: API reference title -->
<!-- {{description}}: Brief overview of the API -->
<!-- {{tags}}: Comma-separated list of relevant tags -->

## Endpoints

| Path | Method | Description |
|------|--------|-------------|
| /{{endpoint}} | {{method}} | {{endpoint_description}} |

```http
{{method}} /{{endpoint}} HTTP/1.1
Host: {{host}}
Content-Type: application/json

{{request_body}}
```

```json
{
  "status": "{{status}}",
  "data": {{data}}
}
```

<!-- {{endpoint}}: API endpoint path -->
<!-- {{method}}: HTTP method (GET/POST/PUT/DELETE) -->
<!-- {{endpoint_description}}: Purpose of the endpoint -->
<!-- {{host}}: API domain -->
<!-- {{request_body}}: Example request payload -->
<!-- {{status}}: Expected HTTP status code -->
<!-- {{data}}: Example response data structure -->
