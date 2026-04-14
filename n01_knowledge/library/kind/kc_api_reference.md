---
id: kc_api_reference
kind: knowledge_card
title: API Reference
version: 1.0.0
quality: null
pillar: P01
description: Comprehensive API documentation with endpoints, parameters, response formats, authentication methods, and usage examples
---

# API Reference

## Authentication
- **API Key**: Include `X-API-Key: <your_key>` in headers
- **OAuth2**: Use bearer token in `Authorization: Bearer <token>`

## Endpoints

### GET /api/v1/data
**Description**: Retrieve dataset metadata
```bash
curl https://api.example.com/api/v1/data \
  -H "X-API-Key: your_key"
```
**Response**:
```json
{
  "total_records": 12345,
  "last_updated": "2023-09-20T12:34:56Z"
}
```

### POST /api/v1/submit
**Description**: Submit new data records
```bash
curl -X POST https://api.example.com/api/v1/submit \
  -H "Content-Type: application/json" \
  -d '{"records": [{"id": "123", "value": "example"}]}'
```
**Response**:
```json
{
  "status": "success",
  "record_id": "abc123"
}
```

## Parameters
- `limit`: Max results (default 100)
- `format`: `json` or `csv` (default json)
- `sort`: Field to sort by (ascending/descending)

## Error Responses
- `401 Unauthorized`: Invalid authentication
- `429 Too Many Requests`: Rate limit exceeded
- `503 Service Unavailable`: Temporarily down for maintenance
