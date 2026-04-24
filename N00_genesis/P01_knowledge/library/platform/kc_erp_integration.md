---
id: kc_erp_integration
kind: knowledge_card
8f: F3_inject
pillar: P01
quality: 9.1
tldr: "Integration patterns for ERP/marketplace connectors — BaseLinker, Bling v3, order sync, inventory management, webhook-driven data flow, and OAuth2 token rotation."
tags: ["ERP", "BaseLinker", "Bling", "integration", "orders", "inventory", "OAuth2"]
when_to_use: "Apply when integration patterns for erp/marketplace connectors — baselinker, bling v3, order sync, inventory..."
keywords: [knowledge-card, pattern, baselinker, patterns, connector]
linked_artifacts:
  primary: null
  related: []
density_score: 1.0
related:
  - SPEC_06_multi_provider
  - p01_kc_error_handling_python
  - bld_examples_repo_map
  - SPEC_05_skills_runtime
  - kc_model_context_protocol
  - p09_ratelimit_anthropic_tier2
  - SPEC_07_gdp_enforcement
  - atom_08_crewai
  - kc_agentic_rag
  - bld_examples_connector
---

# ERP Integration Patterns

Patterns for integrating content monetization platforms with ERP systems and marketplace connectors, focusing on order synchronization, inventory management, and reliable data flow.

## 1. Connector Architecture (ERPConnector Pattern)

Build a centralized connector class that abstracts all ERP interactions behind a clean interface.

```python
class ERPConnector:
    """Unified interface for ERP operations."""
    
    def __init__(self, provider: str, mode: str = "LIVE"):
        self.provider = provider  # "baselinker", "bling", "custom"
        self.mode = mode          # LIVE, TEST, MOCK
        self.client = self._init_client()
    
    def sync_order(self, order_id: str) -> SyncResult: ...
    def update_inventory(self, sku: str, qty: int) -> bool: ...
    def get_order_status(self, order_id: str) -> OrderStatus: ...
    def list_pending_orders(self, since: datetime) -> list[Order]: ...
```

**Rule**: The connector MUST support MOCK mode — returns realistic fake data without API calls. This is non-negotiable for CI and local development.

## 2. BaseLinker Integration

BaseLinker is a multi-marketplace connector popular in BR/PL/EU markets. It aggregates orders from Mercado Livre, Shopee, Amazon, and custom stores.

### Key Endpoints
| Method | Endpoint | Purpose |
|--------|----------|---------|
| `getOrders` | POST /connector/api/orders | Fetch orders with filters |
| `setOrderStatus` | POST /connector/api/orders | Update order lifecycle |
| `getInventory` | POST /connector/api/inventory | Stock levels per warehouse |
| `updateInventory` | POST /connector/api/inventory | Adjust stock quantities |
| `getOrderSources` | POST /connector/api/orders | List connected marketplaces |

### Authentication
```python
headers = {
    "X-BLToken": BASELINKER_API_TOKEN,
    "Content-Type": "application/x-www-form-urlencoded"
}
# All requests are POST with method name in body
data = {"method": "getOrders", "parameters": json.dumps(params)}
```

### Pagination Pattern
BaseLinker uses cursor-based pagination via `date_confirmed_from`:
```python
def fetch_all_orders(since: datetime) -> list:
    orders = []
    cursor = int(since.timestamp())
    while True:
        batch = api.getOrders(date_confirmed_from=cursor)
        if not batch: break
        orders.extend(batch)
        cursor = max(o["date_confirmed"] for o in batch) + 1
    return orders
```

## 3. Bling v3 API (Brazilian ERP)

Bling is the dominant ERP in the Brazilian SMB market. v3 uses OAuth2 (replacing the deprecated v2 API key model).

### OAuth2 Flow
```
1. User authorizes: GET /authorize?client_id=X&redirect_uri=Y&scope=Z
2. Exchange code:   POST /token {grant_type: authorization_code, code: C}
3. Access:          GET /pedidos/vendas {Authorization: Bearer TOKEN}
4. Refresh:         POST /token {grant_type: refresh_token, refresh_token: R}
```

### Token Rotation
```python
class BlingTokenManager:
    def __init__(self, client_id, client_secret, token_store):
        self.client_id = client_id
        self.client_secret = client_secret
        self.store = token_store  # Redis, DB, or file
    
    def get_valid_token(self) -> str:
        token = self.store.get("bling_access_token")
        if token and not self._is_expired(token):
            return token["access_token"]
        return self._refresh()
    
    def _refresh(self) -> str:
        refresh = self.store.get("bling_refresh_token")
        new_tokens = self._call_token_endpoint(
            grant_type="refresh_token",
            refresh_token=refresh
        )
        self.store.set("bling_access_token", new_tokens, ttl=3600)
        self.store.set("bling_refresh_token", new_tokens["refresh_token"])
        return new_tokens["access_token"]
```

**Rule**: Bling refresh tokens are single-use. If you fail to store the new refresh token after rotation, you lose access permanently and must re-authorize.

### Key Bling v3 Endpoints
| Resource | Method | Path |
|----------|--------|------|
| Orders (vendas) | GET/POST | `/pedidos/vendas` |
| Products | GET/POST | `/produtos` |
| Stock | GET/PUT | `/estoques` |
| Invoices (NF-e) | GET/POST | `/nfe` |
| Contacts | GET/POST | `/contatos` |

## 4. Order Sync Pipeline

Reliable bidirectional order synchronization between your platform and the ERP.

```
[Platform Order Created]
    │
    ▼
[Queue: order.created event]  ←── Redis/SQS
    │
    ▼
[Sync Worker]
    ├── Transform to ERP format (field mapping)
    ├── Check idempotency (external_ref exists?)
    │   ├── YES → skip (already synced)
    │   └── NO → create in ERP
    ├── Store sync_id mapping (platform_id ↔ erp_id)
    └── Update platform order status
    │
    ▼
[ERP Webhook/Poll]
    ├── Status change → update platform
    ├── Invoice issued → attach NF-e PDF
    └── Shipment → update tracking
```

### Field Mapping
```python
ORDER_FIELD_MAP = {
    "platform_order_id": "numero",           # Bling
    "customer_email":    "contato.email",     # Bling nested
    "total_centavos":    "valorTotal",        # Convert centavos→BRL
    "items":             "itens",             # Array transform
    "shipping_address":  "transporte.endereco"
}
```

**Rule**: Always use a field mapping dictionary — never hardcode field translations inline. When the ERP updates their API, you change one dict.

## 5. Inventory Sync Strategies

| Strategy | When to Use | Latency | Complexity |
|----------|-------------|---------|------------|
| Webhook push | ERP supports real-time webhooks | < 1min | Low |
| Polling (5min) | No webhook support | 5min | Medium |
| Event-driven | High volume (>1000 orders/day) | < 30s | High |
| Manual sync | Low volume, infrequent changes | On-demand | Low |

### Stock Reservation Pattern
```
1. Customer adds to cart → reserve(sku, qty) → decrement available, increment reserved
2. Payment confirmed → confirm(sku, qty) → decrement reserved, increment sold
3. Payment failed → release(sku, qty) → decrement reserved, increment available
4. Timeout (30min) → auto-release reserved → back to available
```

**Rule**: Never oversell. Reserve stock at cart time, not at payment time. The 30-minute timeout prevents ghost reservations.

## 6. Error Handling and Retry

ERP APIs are notoriously unreliable. Build resilience into every integration point.

```python
RETRY_CONFIG = {
    "max_retries": 3,
    "backoff_base": 2,       # Exponential: 2s, 4s, 8s
    "backoff_jitter": 0.5,   # ±50% randomization
    "retryable_codes": [429, 500, 502, 503, 504],
    "dead_letter_after": 3    # Move to DLQ after 3 failures
}
```

### Dead Letter Queue (DLQ)
Failed syncs after max retries go to a DLQ for manual review:
```
[Sync attempt 1] → 503 → retry
[Sync attempt 2] → 503 → retry  
[Sync attempt 3] → 503 → DEAD LETTER QUEUE
    │
    ▼
[Dashboard alert] → operator reviews → manual retry or fix
```

## 7. Multi-ERP Abstraction

When supporting multiple ERPs, use a provider registry pattern:

```python
ERP_PROVIDERS = {
    "baselinker": BaseLinkerConnector,
    "bling_v3":   BlingV3Connector,
    "custom":     CustomERPConnector,
    "mock":       MockERPConnector,
}

def get_connector(provider: str, mode: str = "LIVE") -> ERPConnector:
    cls = ERP_PROVIDERS.get(provider)
    if not cls:
        raise ConfigError(f"Unknown ERP provider: {provider}")
    return cls(mode=mode)
```

**Rule**: Every connector implements the same `ERPConnector` interface. Business logic never imports a specific provider — always goes through the registry.

## Regras de Ouro

1. **MOCK mode is mandatory** — every connector must work without real API calls in CI.
2. **Single-use refresh tokens (Bling)** — store immediately after rotation or lose access.
3. **Field mapping dictionaries** — never hardcode field translations inline.
4. **Reserve at cart, confirm at payment** — prevents overselling.
5. **Dead letter queue** — failed syncs must be recoverable, not silently dropped.
6. **Provider registry** — business logic never imports a specific ERP connector directly.


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[SPEC_06_multi_provider]] | related | 0.32 |
| [[p01_kc_error_handling_python]] | sibling | 0.30 |
| [[bld_examples_repo_map]] | downstream | 0.29 |
| [[SPEC_05_skills_runtime]] | related | 0.28 |
| [[kc_model_context_protocol]] | sibling | 0.27 |
| [[p09_ratelimit_anthropic_tier2]] | downstream | 0.24 |
| [[SPEC_07_gdp_enforcement]] | related | 0.23 |
| [[atom_08_crewai]] | sibling | 0.22 |
| [[kc_agentic_rag]] | sibling | 0.21 |
| [[bld_examples_connector]] | downstream | 0.21 |
