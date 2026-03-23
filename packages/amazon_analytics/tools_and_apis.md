# Amazon Analytics Agent — Tools & APIs

## Primary: Amazon SP-API

**Base URL**: `https://sellingpartnerapi-na.amazon.com`
**Auth**: LWA (Login With Amazon) OAuth 2.0

### Advertising API (Reports)

```
POST /reports/2021-06-30/reports   # Create report
GET  /reports/2021-06-30/reports/{reportId}
GET  /reports/2021-06-30/documents/{reportDocumentId}
```

| Report Type | Data Available | Latency |
|-------------|---------------|---------|
| SP_ADVERTISED_PRODUCT | ACOS, ROAS, spend, sales | T+2h |
| SP_TARGETING | Keyword-level metrics | T+2h |
| SP_CAMPAIGN | Campaign aggregates | T+2h |
| SP_SEARCH_TERM | Query-level performance | T+24h |

### Sales API

```
GET /sales/v1/orderMetrics
Params: granularity (Hour/Day/Week/Month), interval, marketplaceIds
```

### Catalog Items API (Product Validation)

```
GET /catalog/2022-04-01/items/{asin}
GET /catalog/2022-04-01/items?keywords={term}&marketplaceIds=A2Q3Y263D00KWC
```

### Rate Limits

| Endpoint | Rate | Burst |
|----------|------|-------|
| Reports (create) | 0.0167/s | 15 |
| Reports (get) | 2/s | 15 |
| Sales metrics | 0.5/s | 30 |
| Catalog items | 2/s | 2 |

## Secondary: Seller Central Dashboard

**URL**: `https://sellercentral.amazon.com.br`

| Section | Data | Path |
|---------|------|------|
| Business Reports | Sessions, CVR, Buy Box % | Reports > Business Reports |
| Advertising Console | Campaign ACOS, spend | Advertising > Campaign Manager |
| Brand Analytics | Search frequency, market basket | Brands > Brand Analytics |
| Inventory Health | Turn rate, aged stock | Inventory > Inventory Planning |

## Third-Party Tools (Reference)

| Tool | Use Case | Notes |
|------|----------|-------|
| Helium 10 | Keyword research, product validation | Chrome extension |
| Jungle Scout | Market size estimates | Subscription |
| Keepa | Price history, rank history | API available |
| DataDive | Listing optimization scoring | Requires Helium 10 |

## Authentication Flow

```python
# LWA Token
headers = {
    "x-amz-access-token": lwa_token,
    "x-amz-date": amz_date,
    "Authorization": aws_sig_v4
}
marketplace_id = "A2Q3Y263D00KWC"  # Amazon.com.br
```

## SP-API Error Codes

| Code | Meaning | Action |
|------|---------|--------|
| 429 | Rate limited | Exponential backoff: 2s, 4s, 8s. Max 3 retries. |
| 403 | Auth failure | Refresh LWA token, retry once |
| 404 | Report not ready | Poll every 30s, timeout after 10 min |
| 503 | SP-API down | Retry after 5 min |
| 400 | Bad request params | Log full request, return detailed error |
