#!/usr/bin/env python3
"""
Phase 3: CRM Integration and Conflict Resolution
Merges discovered businesses with existing CRM while preserving manual classifications.
"""

import json
import re
from pathlib import Path
from datetime import datetime

def load_existing_crm():
    """Load current CRM data structure by parsing the markdown table."""
    crm_file = Path("N01_research/output/output_crm_pet_abc.md")

    if not crm_file.exists():
        print(f"ERROR: CRM file not found: {crm_file}")
        return []

    existing_businesses = []
    with open(crm_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the table section
    lines = content.split('\n')
    table_started = False
    header_processed = False

    for line in lines:
        if '| CNPJ | Razão Social' in line:
            table_started = True
            continue
        elif table_started and ('| ---' in line or '|---' in line):
            header_processed = True
            continue
        elif table_started and header_processed and line.startswith('|') and '|' in line[1:] and not line.strip() == '|':
            # Parse table row
            fields = [field.strip() for field in line.split('|')[1:-1]]  # Remove empty first and last

            if len(fields) >= 19:  # Ensure we have all expected fields
                business = {
                    'cnpj': fields[0],
                    'razao_social': fields[1],
                    'nome_fantasia': fields[2],
                    'segmento': fields[3],
                    'sub_segmento': fields[4],
                    'endereco': fields[5],
                    'cidade': fields[6],
                    'ring': fields[7],
                    'telefone': fields[8],
                    'whatsapp': fields[9],
                    'email': fields[10],
                    'instagram': fields[11],
                    'website': fields[12],
                    'google_maps_url': fields[13],
                    'google_rating': fields[14],
                    'google_reviews': fields[15],
                    'porte': fields[16],
                    'foco_felino': fields[17],
                    'potencial_b2b': fields[18],
                    'notas': fields[19] if len(fields) > 19 else ''
                }
                existing_businesses.append(business)
        elif table_started and not line.strip():
            # Empty line after table
            break

    print(f"Loaded {len(existing_businesses)} existing businesses from CRM")
    return existing_businesses

def load_discovered_businesses():
    """Load discovered businesses from pragmatic discovery results."""
    results_file = Path("N01_research/output/pragmatic_discovery_results.json")

    if not results_file.exists():
        print(f"ERROR: Discovery results not found: {results_file}")
        return []

    with open(results_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    all_discovered = []
    for city, results in data.items():
        for business in results['businesses']:
            all_discovered.append(business)

    print(f"Loaded {len(all_discovered)} discovered businesses")
    return all_discovered

def normalize_phone(phone):
    """Normalize phone number for comparison."""
    if not phone:
        return ""
    # Remove all non-digits
    digits = re.sub(r'\D', '', str(phone))
    return digits[-10:] if len(digits) >= 10 else digits  # Last 10 digits

def normalize_name(name):
    """Normalize business name for comparison."""
    if not name:
        return ""
    return re.sub(r'[^a-z0-9]', '', name.lower())

def calculate_similarity(name1, name2):
    """Calculate simple string similarity (Jaccard index on words)."""
    if not name1 or not name2:
        return 0.0

    words1 = set(name1.lower().split())
    words2 = set(name2.lower().split())

    if not words1 or not words2:
        return 0.0

    intersection = len(words1.intersection(words2))
    union = len(words1.union(words2))

    return intersection / union if union > 0 else 0.0

def find_duplicate(discovered_biz, existing_businesses):
    """
    Find if a discovered business matches an existing one.
    Returns (match_found, match_confidence, matched_business)
    """
    d_cnpj = discovered_biz.get('cnpj', '').replace('.', '').replace('/', '').replace('-', '')
    d_phone = normalize_phone(discovered_biz.get('phone', ''))
    d_name = discovered_biz.get('name', '')
    d_city = discovered_biz.get('city', '')

    for existing in existing_businesses:
        e_cnpj = existing['cnpj'].replace('.', '').replace('/', '').replace('-', '')
        e_phone = normalize_phone(existing['telefone'])
        e_name = existing['nome_fantasia']
        e_city = existing['cidade']

        # Match criteria (in priority order)

        # 1. CNPJ exact match (highest confidence)
        if d_cnpj and e_cnpj and d_cnpj == e_cnpj:
            return True, 0.95, existing

        # 2. Phone exact match
        if d_phone and e_phone and len(d_phone) >= 8 and len(e_phone) >= 8:
            if d_phone == e_phone:
                return True, 0.90, existing

        # 3. Name + City fuzzy match (85%+ similarity)
        if d_city.lower() == e_city.lower():
            name_sim = calculate_similarity(d_name, e_name)
            if name_sim >= 0.85:
                return True, name_sim, existing

    return False, 0.0, None

def merge_business_data(discovered, existing, match_confidence):
    """
    Merge discovered business data with existing business, preserving manual classifications.
    """
    merged = existing.copy()

    # PRESERVE manual classifications (never overwrite)
    preserve_fields = ['ring', 'porte', 'foco_felino', 'potencial_b2b', 'notas']

    # ENHANCE empty fields with validated discovery data
    field_mapping = {
        'telefone': discovered.get('phone', ''),
        'whatsapp': discovered.get('phone', ''),  # Use phone as WhatsApp if empty
        'email': discovered.get('email', ''),
        'instagram': discovered.get('social_instagram', ''),
        'website': discovered.get('website', ''),
        'google_rating': str(discovered.get('rating', '')),
        'google_reviews': str(discovered.get('review_count', '')),
        'endereco': discovered.get('address', '')
    }

    for crm_field, discovery_value in field_mapping.items():
        if discovery_value and (not merged[crm_field] or merged[crm_field] == 'a_validar'):
            merged[crm_field] = discovery_value

    # ADD new metadata
    merged['_enhanced'] = True
    merged['_discovery_confidence'] = discovered.get('confidence', 0.0)
    merged['_match_confidence'] = match_confidence
    merged['_discovery_source'] = discovered.get('source', 'pragmatic_discovery')

    return merged

def create_new_business_entry(discovered):
    """
    Convert discovered business to CRM format as new entry.
    """
    return {
        'cnpj': discovered.get('cnpj', 'a_validar'),
        'razao_social': discovered.get('name', ''),  # Will need manual update
        'nome_fantasia': discovered.get('name', ''),
        'segmento': discovered.get('category', '').replace('_', ' ').title(),
        'sub_segmento': discovered.get('subcategory', '').replace('_', ' ').title(),
        'endereco': discovered.get('address', ''),
        'cidade': discovered.get('city', ''),
        'ring': '0',  # Flag for manual classification
        'telefone': discovered.get('phone', ''),
        'whatsapp': discovered.get('phone', ''),
        'email': discovered.get('email', ''),
        'instagram': discovered.get('social_instagram', ''),
        'website': discovered.get('website', ''),
        'google_maps_url': discovered.get('source_url', ''),
        'google_rating': str(discovered.get('rating', '')),
        'google_reviews': str(discovered.get('review_count', '')),
        'porte': 'a_validar',  # Flag for manual classification
        'foco_felino': 'a_validar',  # Flag for manual classification
        'potencial_b2b': 'a_validar',  # Flag for manual classification
        'notas': f"Discovery: {discovered.get('source', '')} | Confidence: {discovered.get('confidence', 0.0):.2f}",
        '_new_entry': True,
        '_discovery_confidence': discovered.get('confidence', 0.0),
        '_discovery_source': discovered.get('source', 'pragmatic_discovery')
    }

def integrate_businesses():
    """Main integration function."""
    print("=== PHASE 3: CRM INTEGRATION AND CONFLICT RESOLUTION ===")
    print("")

    # Load data
    existing_businesses = load_existing_crm()
    discovered_businesses = load_discovered_businesses()

    if not existing_businesses or not discovered_businesses:
        print("ERROR: Failed to load required data")
        return

    # Integration statistics
    stats = {
        'existing_count': len(existing_businesses),
        'discovered_count': len(discovered_businesses),
        'exact_matches': 0,
        'fuzzy_matches': 0,
        'new_businesses': 0,
        'enhanced_existing': 0,
        'total_after_integration': 0
    }

    integrated_businesses = []
    matched_discovery_ids = set()

    # Process existing businesses - check for matches with discovered
    print("Processing existing businesses for enhancement...")
    for existing in existing_businesses:
        enhanced = False

        for i, discovered in enumerate(discovered_businesses):
            if i in matched_discovery_ids:
                continue

            match_found, confidence, _ = find_duplicate(discovered, [existing])

            if match_found:
                # Merge data
                merged = merge_business_data(discovered, existing, confidence)
                integrated_businesses.append(merged)
                matched_discovery_ids.add(i)
                stats['enhanced_existing'] += 1
                enhanced = True

                if confidence >= 0.90:
                    stats['exact_matches'] += 1
                else:
                    stats['fuzzy_matches'] += 1

                print(f"  Enhanced: {existing['nome_fantasia']} (confidence: {confidence:.2f})")
                break

        if not enhanced:
            # No match found, keep existing as-is
            integrated_businesses.append(existing)

    # Process unmatched discovered businesses as new entries
    print("\nAdding new discovered businesses...")
    for i, discovered in enumerate(discovered_businesses):
        if i not in matched_discovery_ids:
            new_business = create_new_business_entry(discovered)
            integrated_businesses.append(new_business)
            stats['new_businesses'] += 1
            print(f"  New: {discovered.get('name', 'Unknown')} in {discovered.get('city', '')}")

    stats['total_after_integration'] = len(integrated_businesses)

    # Generate integration report
    print("\n=== INTEGRATION RESULTS ===")
    print(f"Original CRM businesses: {stats['existing_count']}")
    print(f"Discovered businesses: {stats['discovered_count']}")
    print(f"Exact matches (CNPJ/phone): {stats['exact_matches']}")
    print(f"Fuzzy matches (name+city): {stats['fuzzy_matches']}")
    print(f"Enhanced existing businesses: {stats['enhanced_existing']}")
    print(f"New businesses added: {stats['new_businesses']}")
    print(f"Total after integration: {stats['total_after_integration']}")
    print("")

    expansion_ratio = stats['total_after_integration'] / stats['existing_count'] if stats['existing_count'] > 0 else 0
    enhancement_rate = stats['enhanced_existing'] / stats['existing_count'] if stats['existing_count'] > 0 else 0

    print(f"Database expansion: {expansion_ratio:.1f}x")
    print(f"Enhancement rate: {enhancement_rate:.1%}")

    # Save integrated results
    save_integrated_crm(integrated_businesses, stats)

    return integrated_businesses, stats

def save_integrated_crm(businesses, stats):
    """Save the integrated CRM to a new file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = Path(f"N01_research/output/output_crm_pet_abc_integrated_{timestamp}.md")

    with open(output_file, 'w', encoding='utf-8') as f:
        # Write header
        f.write("---\n")
        f.write("id: BRAND_GATO3_CRM_PET_ABC_INTEGRATED\n")
        f.write("kind: research\n")
        f.write("pillar: P01\n")
        f.write("title: \"Banco de Dados CRM Pet - ABC Paulista INTEGRADO\"\n")
        f.write(f"version: 2.0\n")
        f.write("quality: null\n")
        f.write("---\n\n")

        f.write("# CRM Pet ABC Paulista - VERSÃO INTEGRADA COM DISCOVERY PIPELINE\n\n")

        f.write("## Resumo da Integração\n\n")
        f.write(f"**Data da integração**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Businesses originais**: {stats['existing_count']}\n")
        f.write(f"**Businesses descobertos**: {stats['discovered_count']}\n")
        f.write(f"**Total após integração**: {stats['total_after_integration']}\n")
        f.write(f"**Expansão da base**: {stats['total_after_integration']/stats['existing_count']:.1f}x\n")
        f.write(f"**Taxa de enhancement**: {stats['enhanced_existing']}/{stats['existing_count']} ({stats['enhanced_existing']/stats['existing_count']:.1%})\n\n")

        f.write("### Estatísticas de Integração\n")
        f.write(f"- Matches exatos (CNPJ/telefone): {stats['exact_matches']}\n")
        f.write(f"- Matches fuzzy (nome+cidade): {stats['fuzzy_matches']}\n")
        f.write(f"- Businesses existentes aprimorados: {stats['enhanced_existing']}\n")
        f.write(f"- Novos businesses adicionados: {stats['new_businesses']}\n\n")

        f.write("### Preservation Notes\n")
        f.write("- ✅ **Ring/Tier classifications PRESERVED** - todas classificações manuais mantidas\n")
        f.write("- ✅ **Foco Felino ratings PRESERVED** - especialidades felinas mantidas\n")
        f.write("- ✅ **Potencial B2B PRESERVED** - classificações estratégicas mantidas\n")
        f.write("- ✅ **Notas manuais PRESERVED** - anotações e observações mantidas\n")
        f.write("- 🔄 **Empty fields ENHANCED** - campos 'a_validar' preenchidos com dados validados\n")
        f.write("- 🆕 **New entries FLAGGED** - novos businesses marcados para classificação manual\n\n")

        # Write table header
        f.write("## Tabela Principal Integrada\n\n")
        f.write("| CNPJ | Razão Social | Nome Fantasia | Segmento | Sub-segmento | Endereço | Cidade | Ring | Telefone | WhatsApp | Email | Instagram | Website | Google Maps URL | Google Rating | Google Reviews | Porte | Foco Felino | Potencial B2B | Notas |\n")
        f.write("|------|--------------|---------------|----------|--------------|----------|--------|------|----------|----------|-------|-----------|---------|----------------|---------------|----------------|-------|-------------|---------------|-------|\n")

        # Write business entries
        for business in businesses:
            row = f"| {business['cnpj']} | {business['razao_social']} | {business['nome_fantasia']} | {business['segmento']} | {business['sub_segmento']} | {business['endereco']} | {business['cidade']} | {business['ring']} | {business['telefone']} | {business['whatsapp']} | {business['email']} | {business['instagram']} | {business['website']} | {business['google_maps_url']} | {business['google_rating']} | {business['google_reviews']} | {business['porte']} | {business['foco_felino']} | {business['potencial_b2b']} | {business['notas']} |\n"
            f.write(row)

        f.write("\n## Integration Metadata\n\n")
        f.write("Campos com prefixo `_` contêm metadados da integração (não exibidos na tabela principal):\n")
        f.write("- `_enhanced`: Business existente que foi aprimorado\n")
        f.write("- `_new_entry`: Novo business descoberto\n")
        f.write("- `_discovery_confidence`: Score de confiança do discovery\n")
        f.write("- `_match_confidence`: Score de confiança do match\n")
        f.write("- `_discovery_source`: Método de discovery utilizado\n")

    print(f"\nIntegrated CRM saved to: {output_file}")

def main():
    """Execute the full integration process."""
    integrated_businesses, stats = integrate_businesses()

    if integrated_businesses:
        print("\n🔥 SUCCESS: CRM integration completed!")
        print(f"   Database expanded from {stats['existing_count']} to {stats['total_after_integration']} businesses")
        print(f"   {stats['enhanced_existing']} existing businesses enhanced with validated data")
        print(f"   {stats['new_businesses']} new businesses ready for manual classification")
        print("\n✅ Ready for Phase 4: Quality Control and Validation")
    else:
        print("❌ Integration failed")

if __name__ == "__main__":
    main()