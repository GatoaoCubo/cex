"""
CRM Data Validator — quality control for GATO³ CRM database.

Validates:
  - CNPJ (algorithmic check digit verification)
  - Phone numbers (BR format, DDD validation)
  - Email addresses (format + domain check)
  - Duplicate detection (fuzzy name + city matching)
  - Data completeness scoring per record

Output: data quality report with per-record scores and cleanup recommendations.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

from _tools.crm.crm_parser import CRMBusiness, CRMParser, DEFAULT_CRM

OUTPUT_DIR = Path(__file__).parent.parent.parent / "N01_research" / "output"

# Valid DDDs for São Paulo state
VALID_DDDS_SP = {"11", "12", "13", "14", "15", "16", "17", "18", "19"}


@dataclass
class ValidationResult:
    """Validation result for a single business."""
    business_id: str
    business_name: str
    cidade: str = ""
    cnpj_valid: bool | None = None  # None = not present
    cnpj_issue: str = ""
    phone_valid: bool | None = None
    phone_issue: str = ""
    email_valid: bool | None = None
    email_issue: str = ""
    completeness_score: float = 0.0
    missing_fields: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    quality_score: float = 0.0

    def to_dict(self) -> dict[str, Any]:
        return {
            "business_id": self.business_id,
            "business_name": self.business_name,
            "cidade": self.cidade,
            "cnpj_valid": self.cnpj_valid,
            "cnpj_issue": self.cnpj_issue,
            "phone_valid": self.phone_valid,
            "phone_issue": self.phone_issue,
            "email_valid": self.email_valid,
            "email_issue": self.email_issue,
            "completeness_score": self.completeness_score,
            "missing_fields": self.missing_fields,
            "warnings": self.warnings,
            "quality_score": self.quality_score,
        }


@dataclass
class DuplicateGroup:
    """Group of potential duplicate businesses."""
    canonical_id: str
    canonical_name: str
    duplicates: list[dict] = field(default_factory=list)
    similarity: float = 0.0

    def to_dict(self) -> dict[str, Any]:
        return {
            "canonical_id": self.canonical_id,
            "canonical_name": self.canonical_name,
            "duplicates": self.duplicates,
            "similarity": self.similarity,
        }


# --- CNPJ Validation ---

def validate_cnpj(cnpj: str) -> tuple[bool, str]:
    """Validate Brazilian CNPJ using check digits algorithm."""
    if not cnpj or cnpj == "a_validar":
        return False, "missing"

    # Strip formatting
    digits = re.sub(r"[^\d]", "", cnpj)

    if len(digits) != 14:
        return False, f"invalid_length ({len(digits)} digits)"

    # Check for known invalid patterns
    if digits == digits[0] * 14:
        return False, "all_same_digits"

    # First check digit
    weights1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    total = sum(int(digits[i]) * weights1[i] for i in range(12))
    remainder = total % 11
    d1 = 0 if remainder < 2 else 11 - remainder

    if int(digits[12]) != d1:
        return False, "check_digit_1_failed"

    # Second check digit
    weights2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    total = sum(int(digits[i]) * weights2[i] for i in range(13))
    remainder = total % 11
    d2 = 0 if remainder < 2 else 11 - remainder

    if int(digits[13]) != d2:
        return False, "check_digit_2_failed"

    return True, "valid"


def format_cnpj(cnpj: str) -> str:
    """Format CNPJ as XX.XXX.XXX/XXXX-XX."""
    digits = re.sub(r"[^\d]", "", cnpj)
    if len(digits) != 14:
        return cnpj
    return f"{digits[:2]}.{digits[2:5]}.{digits[5:8]}/{digits[8:12]}-{digits[12:]}"


# --- Phone Validation ---

def validate_phone(phone: str) -> tuple[bool, str]:
    """Validate Brazilian phone number format."""
    if not phone or phone == "a_validar":
        return False, "missing"

    # Extract digits
    digits = re.sub(r"[^\d]", "", phone)

    if len(digits) < 10:
        return False, f"too_short ({len(digits)} digits)"

    if len(digits) > 13:
        return False, f"too_long ({len(digits)} digits)"

    # Strip country code
    if digits.startswith("55") and len(digits) >= 12:
        digits = digits[2:]

    ddd = digits[:2]
    number = digits[2:]

    if ddd not in VALID_DDDS_SP and not (20 <= int(ddd) <= 99):
        return False, f"invalid_ddd ({ddd})"

    # Mobile: 9XXXX-XXXX (9 digits starting with 9)
    # Landline: XXXX-XXXX (8 digits)
    if len(number) == 9 and number[0] == "9":
        return True, "mobile"
    elif len(number) == 8:
        return True, "landline"
    else:
        return False, f"invalid_number_length ({len(number)} digits)"


def format_phone(phone: str) -> str:
    """Format phone as (DD) XXXXX-XXXX or (DD) XXXX-XXXX."""
    digits = re.sub(r"[^\d]", "", phone)
    if digits.startswith("55") and len(digits) >= 12:
        digits = digits[2:]
    if len(digits) == 11:
        return f"({digits[:2]}) {digits[2:7]}-{digits[7:]}"
    elif len(digits) == 10:
        return f"({digits[:2]}) {digits[2:6]}-{digits[6:]}"
    return phone


# --- Email Validation ---

def validate_email(email: str) -> tuple[bool, str]:
    """Validate email address format."""
    if not email or email == "a_validar":
        return False, "missing"

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(pattern, email):
        return False, "invalid_format"

    # Check for common disposable/suspicious patterns
    domain = email.split("@")[1].lower()
    if domain in ("example.com", "test.com", "localhost"):
        return False, "suspicious_domain"

    return True, "valid"


# --- Completeness Scoring ---

# Fields and their weights for completeness
COMPLETENESS_WEIGHTS = {
    "cnpj": 15,
    "nome_fantasia": 10,
    "segmento": 5,
    "endereco": 10,
    "cidade": 10,
    "telefone": 15,
    "whatsapp": 10,
    "email": 5,
    "instagram": 5,
    "website": 5,
    "google_rating": 5,
    "google_reviews": 5,
}


def score_completeness(biz: CRMBusiness) -> tuple[float, list[str]]:
    """Score data completeness (0-100). Returns (score, missing_fields)."""
    total_weight = sum(COMPLETENESS_WEIGHTS.values())
    earned = 0.0
    missing = []

    for field_name, weight in COMPLETENESS_WEIGHTS.items():
        val = getattr(biz, field_name, "")
        if isinstance(val, str):
            has_value = bool(val) and val != "a_validar"
        elif isinstance(val, (int, float)):
            has_value = val > 0
        else:
            has_value = bool(val)

        if has_value:
            earned += weight
        else:
            missing.append(field_name)

    return round(earned / total_weight * 100, 1), missing


# --- Duplicate Detection ---

def _normalize_name(name: str) -> str:
    """Normalize business name for comparison."""
    name = name.lower().strip()
    # Remove common suffixes
    for suffix in [" ltda", " me", " mei", " epp", " eireli", " s/a", " s.a."]:
        name = name.replace(suffix, "")
    # Remove punctuation
    name = re.sub(r"[^\w\s]", "", name)
    return re.sub(r"\s+", " ", name).strip()


def find_duplicates(businesses: list[CRMBusiness], threshold: float = 0.80) -> list[DuplicateGroup]:
    """Find potential duplicate businesses using fuzzy name + city matching."""
    groups: list[DuplicateGroup] = []
    seen: set[str] = set()

    for i, biz_a in enumerate(businesses):
        if biz_a.id in seen:
            continue

        norm_a = _normalize_name(biz_a.nome_fantasia)
        if not norm_a:
            continue

        dupes = []
        for j, biz_b in enumerate(businesses):
            if i >= j or biz_b.id in seen:
                continue

            norm_b = _normalize_name(biz_b.nome_fantasia)
            if not norm_b:
                continue

            # Same city or both unknown
            same_city = (
                biz_a.cidade.lower() == biz_b.cidade.lower()
                or not biz_a.cidade
                or not biz_b.cidade
            )

            if not same_city:
                continue

            # Fuzzy name match
            sim = SequenceMatcher(None, norm_a, norm_b).ratio()
            if sim >= threshold:
                dupes.append({
                    "id": biz_b.id,
                    "name": biz_b.nome_fantasia,
                    "cidade": biz_b.cidade,
                    "similarity": round(sim, 3),
                })
                seen.add(biz_b.id)

        # CNPJ-based exact match
        if biz_a.has_cnpj:
            cnpj_digits = re.sub(r"[^\d]", "", biz_a.cnpj)
            for j, biz_b in enumerate(businesses):
                if i >= j or biz_b.id in seen or not biz_b.has_cnpj:
                    continue
                if re.sub(r"[^\d]", "", biz_b.cnpj) == cnpj_digits:
                    dupes.append({
                        "id": biz_b.id,
                        "name": biz_b.nome_fantasia,
                        "cidade": biz_b.cidade,
                        "similarity": 1.0,
                        "match_type": "cnpj_exact",
                    })
                    seen.add(biz_b.id)

        if dupes:
            avg_sim = sum(d["similarity"] for d in dupes) / len(dupes)
            groups.append(DuplicateGroup(
                canonical_id=biz_a.id,
                canonical_name=biz_a.nome_fantasia,
                duplicates=dupes,
                similarity=round(avg_sim, 3),
            ))
            seen.add(biz_a.id)

    return groups


class DataValidator:
    """Validate and score CRM data quality."""

    def __init__(self, crm_path: Path | str | None = None):
        self.parser = CRMParser(crm_path)
        self.businesses: list[CRMBusiness] = []
        self.results: list[ValidationResult] = []
        self.duplicates: list[DuplicateGroup] = []

    def run(self) -> list[ValidationResult]:
        """Run full validation on all CRM records."""
        self.businesses = self.parser.parse()
        self.results = []

        for biz in self.businesses:
            result = ValidationResult(
                business_id=biz.id,
                business_name=biz.nome_fantasia,
                cidade=biz.cidade,
            )

            # CNPJ validation
            if biz.cnpj and biz.cnpj != "a_validar":
                valid, issue = validate_cnpj(biz.cnpj)
                result.cnpj_valid = valid
                result.cnpj_issue = issue
                if not valid and issue not in ("missing",):
                    result.warnings.append(f"CNPJ invalid: {issue}")

            # Phone validation
            if biz.telefone and biz.telefone != "a_validar":
                valid, issue = validate_phone(biz.telefone)
                result.phone_valid = valid
                result.phone_issue = issue
                if not valid and issue not in ("missing",):
                    result.warnings.append(f"Phone invalid: {issue}")

            # Email validation
            if biz.email and biz.email != "a_validar":
                valid, issue = validate_email(biz.email)
                result.email_valid = valid
                result.email_issue = issue
                if not valid and issue not in ("missing",):
                    result.warnings.append(f"Email invalid: {issue}")

            # Completeness
            result.completeness_score, result.missing_fields = score_completeness(biz)

            # Overall quality score (weighted average)
            quality = result.completeness_score * 0.5
            if result.cnpj_valid:
                quality += 20
            if result.phone_valid:
                quality += 15
            if result.email_valid:
                quality += 10
            # Bonus for multiple channels
            quality += min(biz.contact_channels * 2, 10)
            result.quality_score = round(min(quality, 100), 1)

            biz.data_quality_score = result.quality_score
            biz.validation_flags = result.warnings
            self.results.append(result)

        # Duplicate detection
        self.duplicates = find_duplicates(self.businesses)

        return self.results

    def summary(self) -> dict[str, Any]:
        """Generate validation summary statistics."""
        if not self.results:
            self.run()

        total = len(self.results)
        cnpj_valid = sum(1 for r in self.results if r.cnpj_valid is True)
        cnpj_invalid = sum(1 for r in self.results if r.cnpj_valid is False)
        cnpj_missing = sum(1 for r in self.results if r.cnpj_valid is None)
        phone_valid = sum(1 for r in self.results if r.phone_valid is True)
        email_valid = sum(1 for r in self.results if r.email_valid is True)
        avg_completeness = sum(r.completeness_score for r in self.results) / max(total, 1)
        avg_quality = sum(r.quality_score for r in self.results) / max(total, 1)
        warnings_total = sum(len(r.warnings) for r in self.results)

        # Most common missing fields
        missing_counts: dict[str, int] = defaultdict(int)
        for r in self.results:
            for f in r.missing_fields:
                missing_counts[f] += 1

        return {
            "total_records": total,
            "cnpj_valid": cnpj_valid,
            "cnpj_invalid": cnpj_invalid,
            "cnpj_missing": cnpj_missing,
            "phone_valid": phone_valid,
            "email_valid": email_valid,
            "avg_completeness": round(avg_completeness, 1),
            "avg_quality_score": round(avg_quality, 1),
            "total_warnings": warnings_total,
            "duplicate_groups": len(self.duplicates),
            "duplicate_records": sum(len(g.duplicates) for g in self.duplicates),
            "most_missing": dict(sorted(missing_counts.items(), key=lambda x: -x[1])[:10]),
        }

    def export_report(self, output_path: Path | None = None) -> Path:
        """Export full validation report as JSON."""
        if not self.results:
            self.run()

        output_path = output_path or OUTPUT_DIR / "crm_validation_report.json"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        report = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "summary": self.summary(),
            "duplicates": [g.to_dict() for g in self.duplicates],
            "low_quality": [
                r.to_dict() for r in sorted(self.results, key=lambda x: x.quality_score)[:50]
            ],
            "warnings": [
                r.to_dict() for r in self.results if r.warnings
            ],
        }

        output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        return output_path

    def print_summary(self) -> None:
        """Print validation summary to console."""
        s = self.summary()
        print("=" * 60)
        print("GATO³ CRM Data Validation Report")
        print("=" * 60)
        print(f"Total records:     {s['total_records']}")
        print(f"Avg completeness:  {s['avg_completeness']}%")
        print(f"Avg quality score: {s['avg_quality_score']}")
        print()
        print(f"CNPJ:   {s['cnpj_valid']} valid / {s['cnpj_invalid']} invalid / {s['cnpj_missing']} missing")
        print(f"Phone:  {s['phone_valid']} valid")
        print(f"Email:  {s['email_valid']} valid")
        print(f"Warnings: {s['total_warnings']}")
        print(f"Duplicate groups: {s['duplicate_groups']} ({s['duplicate_records']} records)")
        print()
        print("Most missing fields:")
        for field_name, count in list(s["most_missing"].items())[:8]:
            pct = count / s["total_records"] * 100
            print(f"  {field_name:<20} {count:>4} ({pct:.0f}%)")
        print("=" * 60)


# --- CLI ---
if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="CRM Data Validator for GATO³")
    ap.add_argument("--crm", default=str(DEFAULT_CRM), help="Path to CRM .md file")
    ap.add_argument("--export", action="store_true", help="Export validation report")
    ap.add_argument("--duplicates", action="store_true", help="Show duplicate groups only")
    ap.add_argument("--low-quality", type=int, default=0, help="Show N lowest quality records")
    ap.add_argument("--validate-cnpj", help="Validate a single CNPJ")
    args = ap.parse_args()

    if args.validate_cnpj:
        valid, issue = validate_cnpj(args.validate_cnpj)
        formatted = format_cnpj(args.validate_cnpj)
        print(f"CNPJ: {formatted} -> {'VALID' if valid else f'INVALID ({issue})'}")
    else:
        validator = DataValidator(args.crm)
        validator.run()

        if args.duplicates:
            print(f"\n{len(validator.duplicates)} duplicate groups found:")
            for g in validator.duplicates:
                print(f"\n  Canonical: {g.canonical_name}")
                for d in g.duplicates:
                    print(f"    -> {d['name']} ({d['cidade']}) sim={d['similarity']:.0%}")
        elif args.low_quality > 0:
            worst = sorted(validator.results, key=lambda x: x.quality_score)[:args.low_quality]
            print(f"\nLowest quality records:")
            for r in worst:
                print(f"  {r.quality_score:5.1f} | {r.business_name:<30} | missing: {', '.join(r.missing_fields[:3])}")
        elif args.export:
            path = validator.export_report()
            print(f"Report exported to: {path}")
            validator.print_summary()
        else:
            validator.print_summary()
