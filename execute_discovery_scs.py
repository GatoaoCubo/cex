#!/usr/bin/env python3
"""
Phase 2 Execution: São Caetano do Sul Discovery
Part of CRM Hydration Plan - Advanced Business Discovery Pipeline
"""

import asyncio
import sys
import json
import time
from pathlib import Path

# Add discovery pipeline to path
sys.path.append('cex_discovery_pipeline')

from cex_discovery_pipeline import DiscoveryPipeline

async def main():
    print("=== Phase 2: Discovery Pipeline Execution ===")
    print("Target: São Caetano do Sul - Pet Ecosystem")
    print("Expected: 200-250 businesses (3.3x current 76)")
    print("")

    start_time = time.time()

    try:
        # Initialize pipeline
        print("Initializing Advanced Business Discovery Pipeline...")
        pipeline = DiscoveryPipeline()

        # Execute discovery for São Caetano do Sul
        print("Executing discovery: São Caetano do Sul pet ecosystem...")
        print("Query: 'Find all pet shops, veterinary clinics, and pet service businesses in São Caetano do Sul'")
        print("")

        results = await pipeline.discover(
            "Find all pet shops, veterinary clinics, and pet service businesses in São Caetano do Sul",
            region_key="abc_metropolitano",
            niche_key="pet_ecosystem"
        )

        execution_time = time.time() - start_time

        # Display results
        print("=== DISCOVERY RESULTS - SÃO CAETANO DO SUL ===")
        print(f"Execution time: {execution_time:.1f}s")
        print(f"Total raw discovered: {results.total_raw}")
        print(f"After deduplication: {results.total_deduplicated}")
        print(f"Validated businesses: {results.total_validated}")
        print(f"Final enriched count: {len(results.businesses)}")
        print("")

        print("Yield Summary:")
        summary = results.yield_summary
        for key, value in summary.items():
            print(f"  {key}: {value}")
        print("")

        # Save detailed results
        output_dir = Path("N01_research/output")
        output_dir.mkdir(exist_ok=True)

        results_file = output_dir / "discovery_scs_results.json"

        # Convert results to serializable format
        businesses_data = []
        for biz in results.businesses:
            businesses_data.append({
                "name": biz.name,
                "phone": biz.phone,
                "address": biz.address,
                "city": biz.city,
                "state": biz.state,
                "cep": biz.cep,
                "category": biz.category,
                "subcategory": biz.subcategory,
                "source": biz.source,
                "source_url": biz.source_url,
                "rating": biz.rating,
                "review_count": biz.review_count,
                "hours": biz.hours,
                "website": biz.website,
                "email": biz.email,
                "cnpj": biz.cnpj,
                "social_facebook": biz.social_facebook,
                "social_instagram": biz.social_instagram,
                "latitude": biz.latitude,
                "longitude": biz.longitude,
                "confidence": biz.confidence,
                "raw_data": biz.raw_data
            })

        output_data = {
            "city": "São Caetano do Sul",
            "execution_time": execution_time,
            "summary": summary,
            "businesses": businesses_data,
            "context": {
                "region": results.context.region_name if results.context else "abc_metropolitano",
                "niche": results.context.niche_name if results.context else "pet_ecosystem",
                "execution_mode": results.context.execution_mode.value if results.context else "comprehensive"
            }
        }

        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

        print(f"Detailed results saved to: {results_file}")

        # Validation analysis
        print("\n=== VALIDATION ANALYSIS ===")
        validated_contacts = 0
        has_phone = 0
        has_email = 0
        has_cnpj = 0
        high_confidence = 0

        for biz in results.businesses:
            if biz.phone:
                has_phone += 1
            if biz.email:
                has_email += 1
            if biz.cnpj:
                has_cnpj += 1
            if biz.confidence >= 0.85:
                high_confidence += 1
            if biz.phone and (biz.email or biz.cnpj):
                validated_contacts += 1

        total = len(results.businesses)
        if total > 0:
            print(f"Validated contacts: {validated_contacts}/{total} ({validated_contacts/total*100:.1f}%)")
            print(f"Phone coverage: {has_phone}/{total} ({has_phone/total*100:.1f}%)")
            print(f"Email coverage: {has_email}/{total} ({has_email/total*100:.1f}%)")
            print(f"CNPJ coverage: {has_cnpj}/{total} ({has_cnpj/total*100:.1f}%)")
            print(f"High confidence (≥85%): {high_confidence}/{total} ({high_confidence/total*100:.1f}%)")

        # Compare with current CRM (76 businesses)
        current_scs = 76
        improvement_ratio = total / current_scs if current_scs > 0 else 0
        print(f"\nComparison with current CRM:")
        print(f"Current São Caetano businesses: {current_scs}")
        print(f"Discovered businesses: {total}")
        print(f"Improvement ratio: {improvement_ratio:.1f}x")

        if improvement_ratio >= 3.0:
            print("🔥 SUCCESS: Achieved 3x+ expansion target!")
        elif improvement_ratio >= 2.0:
            print("✅ GOOD: Achieved 2x+ expansion")
        else:
            print("⚠️  REVIEW: Below 2x target, check mining efficacy")

        return results

    except Exception as e:
        print(f"ERROR during discovery execution: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    results = asyncio.run(main())
    if results:
        print("\nSão Caetano do Sul discovery completed successfully!")
        print("Ready for data integration phase...")
    else:
        print("\nDiscovery failed. Check configuration and try again.")