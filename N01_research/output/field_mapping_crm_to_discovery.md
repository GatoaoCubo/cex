# Field Mapping: Existing CRM → Discovery Pipeline BusinessRecord

## Purpose
Maps the 20-field CRM structure to BusinessRecord schema for seamless integration.

## Current CRM Structure (20 fields)
Based on: `output_crm_pet_abc.md` line 50

| # | CRM Field | Type | Example | Status |
|---|-----------|------|---------|--------|
| 1 | CNPJ | str | 12.345.678/0001-90 | Core ID |
| 2 | Razão Social | str | Pet Shop ABC Ltda | Legal name |
| 3 | Nome Fantasia | str | ABC Pet | Trade name |
| 4 | Segmento | str | Pet Shop | Category |
| 5 | Sub-segmento | str | Ração Premium | Subcategory |
| 6 | Endereço | str | Rua A, 123 | Address |
| 7 | Cidade | str | São Caetano do Sul | City |
| 8 | Ring | int | 1 | Priority tier |
| 9 | Telefone | str | (11) 1234-5678 | Phone |
| 10 | WhatsApp | str | (11) 9876-5432 | WhatsApp |
| 11 | Email | str | contato@abc.com | Email |
| 12 | Instagram | str | @abcpet | Social |
| 13 | Website | str | www.abc.com | Website |
| 14 | Google Maps URL | str | maps.google.com/... | Source URL |
| 15 | Google Rating | float | 4.5 | Rating |
| 16 | Google Reviews | int | 123 | Review count |
| 17 | Porte | str | MEI/Pequeno | Size |
| 18 | Foco Felino | str | Alto/Médio | Cat specialty |
| 19 | Potencial B2B | str | S+/S/Tier 1-3 | Business potential |
| 20 | Notas | str | Manual annotations | Notes |

## BusinessRecord Schema (24 fields)
From: `cex_discovery_pipeline/miners/base_miner.py`

| # | BusinessRecord Field | Type | Purpose | Source |
|---|---------------------|------|---------|--------|
| 1 | name | str | Business name | Discovery |
| 2 | phone | str | Primary phone | Discovery |
| 3 | address | str | Full address | Discovery |
| 4 | city | str | City name | Discovery |
| 5 | state | str | State (SP) | Discovery |
| 6 | cep | str | Postal code | Discovery |
| 7 | category | str | Business category | Discovery |
| 8 | subcategory | str | Detailed category | Discovery |
| 9 | source | str | Discovery method | Discovery |
| 10 | source_url | str | Source URL | Discovery |
| 11 | rating | float | Average rating | Discovery |
| 12 | review_count | int | Review count | Discovery |
| 13 | hours | str | Operating hours | Discovery |
| 14 | website | str | Website URL | Discovery |
| 15 | email | str | Email address | Discovery |
| 16 | cnpj | str | Tax ID | Discovery |
| 17 | social_facebook | str | Facebook handle | Discovery |
| 18 | social_instagram | str | Instagram handle | Discovery |
| 19 | latitude | float | GPS latitude | Discovery |
| 20 | longitude | float | GPS longitude | Discovery |
| 21 | confidence | float | Data quality score | Discovery |
| 22 | raw_data | dict | Original data | Discovery |

## Field Mapping Matrix

### Direct Mappings (1:1)
| CRM Field | BusinessRecord Field | Notes |
|-----------|---------------------|-------|
| CNPJ | cnpj | Primary key for deduplication |
| Nome Fantasia | name | Trade name preferred |
| Endereço | address | Direct mapping |
| Cidade | city | Direct mapping |
| Telefone | phone | Primary contact |
| Email | email | Direct mapping |
| Instagram | social_instagram | Clean @ prefix |
| Website | website | Direct mapping |
| Google Maps URL | source_url | When source=google_maps |
| Google Rating | rating | Direct mapping |
| Google Reviews | review_count | Direct mapping |
| Segmento | category | Direct mapping |
| Sub-segmento | subcategory | Direct mapping |

### Derived Mappings
| CRM Field | BusinessRecord Field | Logic |
|-----------|---------------------|-------|
| WhatsApp | phone | If no primary phone, use WhatsApp |
| Razão Social | raw_data['legal_name'] | Store in metadata |
| Ring | raw_data['ring'] | Preserve priority tier |
| Porte | raw_data['size'] | Preserve size classification |
| Foco Felino | raw_data['cat_focus'] | Preserve specialty rating |
| Potencial B2B | raw_data['b2b_potential'] | Preserve business tier |
| Notas | raw_data['notes'] | Preserve manual annotations |

### New Fields (Discovery Only)
| BusinessRecord Field | Source | Purpose |
|---------------------|--------|---------|
| state | "SP" | Always São Paulo |
| cep | Discovery | Postal code lookup |
| hours | Discovery | Operating hours |
| social_facebook | Discovery | Facebook discovery |
| latitude | Discovery | GPS coordinates |
| longitude | Discovery | GPS coordinates |
| confidence | Discovery | Quality score |
| source | Discovery | Mining technique |

## Integration Strategy

### Deduplication Priority
1. **CNPJ exact match** → Update existing record
2. **Name + City fuzzy match (85%+)** → Update existing record  
3. **Phone exact match** → Update existing record
4. **No match** → Add as new record

### Data Merge Rules

#### For Existing Records (CRM → Discovery)
- **PRESERVE**: Ring, Porte, Foco Felino, Potencial B2B, Notas (manual classifications)
- **ENHANCE**: Fill empty fields with validated discovery data
- **UPDATE**: Contact data if discovery has higher confidence
- **ADD**: New fields (CEP, hours, GPS, social_facebook)

#### For New Records (Discovery → CRM)
- **ADD**: All discovery fields
- **FLAG**: For manual classification (Ring, Foco Felino, Potencial B2B)
- **SET**: Ring=0, Foco Felino="a_validar", Potencial B2B="a_validar"

### Quality Gates
- **Phone confidence**: ≥85%
- **Address confidence**: ≥80%
- **Name similarity**: ≥75% for deduplication
- **Overall confidence**: ≥70% to include

## Backup Recovery
- **Original CRM**: `output_crm_pet_abc_backup_20260403_114505.md`
- **Field preservation**: Manual tiers and annotations cannot be lost
- **Rollback**: Restore from backup if integration fails