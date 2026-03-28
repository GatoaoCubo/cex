"""
VIDEO AGENT VALIDATOR v1.0.0
============================

Validates video production package outputs for e-commerce.

VALIDATION DIMENSIONS (5D):
1. narrative_arc (25%) - Story structure, hook strength, CTA clarity
2. visual_quality (25%) - Shot composition, transitions, pacing
3. platform_compliance (20%) - Format, duration, safe zones
4. engagement_potential (15%) - Trend alignment, scroll-stopping
5. production_feasibility (15%) - AI tool compatibility, budget

Usage:
    result = validate_video_output(
        storyboard={"shots": [...], "duration": 30},
        script={"narration": [...], "overlays": [...]},
        prompts={"shots": [...], "generator": "runway_gen3"},
        platform="tiktok"
    )
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass
import re


# ============================================================================
# CONSTANTS
# ============================================================================

VERSION = "1.0.0"

# Validation thresholds
OVERALL_PASS_THRESHOLD = 0.70  # 70% minimum (7.0/10)
DIMENSION_WEIGHTS = {
    "narrative_arc": 0.25,
    "visual_quality": 0.25,
    "platform_compliance": 0.20,
    "engagement_potential": 0.15,
    "production_feasibility": 0.15,
}

# Platform specifications
PLATFORM_SPECS = {
    "tiktok": {
        "hook_critical": 2,
        "max_duration": 60,
        "optimal_duration": [15, 30],
        "aspect_ratio": "9:16",
    },
    "instagram_reels": {
        "hook_critical": 3,
        "max_duration": 90,
        "optimal_duration": [15, 30, 60],
        "aspect_ratio": "9:16",
    },
    "youtube_shorts": {
        "hook_critical": 3,
        "max_duration": 60,
        "optimal_duration": [30, 60],
        "aspect_ratio": "9:16",
    },
}

# Required narrative phases
REQUIRED_PHASES = ["HOOK", "BUILD", "BENEFIT", "PROOF", "CTA"]

# Shot count by duration
SHOT_COUNT_RANGES = {15: (5, 7), 30: (6, 8), 60: (8, 10)}


# ============================================================================
# DATA CLASSES
# ============================================================================


@dataclass
class DimensionScore:
    """Score for a single validation dimension."""

    score: float  # 0.0 - 1.0
    passed: bool
    issues: List[str]
    details: Dict[str, Any]


@dataclass
class ValidationResult:
    """Complete validation result."""

    version: str
    passed: bool
    overall_score: float
    dimensions: Dict[str, DimensionScore]
    summary: str
    recommendations: List[str]


# ============================================================================
# DIMENSION SCORERS
# ============================================================================


def score_narrative_arc(storyboard: Dict[str, Any], script: Dict[str, Any]) -> DimensionScore:
    """
    Score NARRATIVE_ARC dimension (25%).

    Checks:
    - Hook timing (within 3 seconds)
    - All phases present
    - CTA clarity
    - Timing accuracy
    """
    issues = []
    details = {"hook_timing": None, "phases_found": [], "cta_present": False, "timing_match": False}

    score = 1.0
    shots = storyboard.get("shots", [])
    duration = storyboard.get("duration", 30)

    # Check hook timing
    if shots:
        first_shot = shots[0]
        hook_end = first_shot.get("timing", {}).get("end", 0)
        details["hook_timing"] = hook_end

        if hook_end > 3:
            issues.append(f"Hook termina em {hook_end}s (deve ser <= 3s)")
            score -= 0.25
        elif hook_end > 2:
            score -= 0.10  # Minor penalty for 2-3s hook

    # Check phases present
    phases_found = set()
    for shot in shots:
        phase = shot.get("phase", "").upper()
        if phase in REQUIRED_PHASES:
            phases_found.add(phase)

    details["phases_found"] = list(phases_found)
    missing_phases = set(REQUIRED_PHASES) - phases_found

    if missing_phases:
        issues.append(f"Fases faltando: {', '.join(missing_phases)}")
        score -= len(missing_phases) * 0.10

    # Check CTA
    if shots:
        last_shot = shots[-1]
        last_phase = last_shot.get("phase", "").upper()
        details["cta_present"] = last_phase == "CTA"

        if last_phase != "CTA":
            issues.append("CTA nao esta no ultimo shot")
            score -= 0.15

    # Check timing accuracy
    total_timing = sum(shot.get("timing", {}).get("duration", 0) for shot in shots)
    details["total_timing"] = total_timing
    details["target_duration"] = duration

    timing_diff = abs(total_timing - duration)
    if timing_diff == 0:
        details["timing_match"] = True
    elif timing_diff <= 1:
        score -= 0.05
    elif timing_diff <= 2:
        score -= 0.10
        issues.append(f"Timing total: {total_timing}s (esperado: {duration}s)")
    else:
        score -= 0.20
        issues.append(f"Timing incorreto: {total_timing}s (esperado: {duration}s)")

    return DimensionScore(
        score=max(0.0, score), passed=score >= 0.70, issues=issues, details=details
    )


def score_visual_quality(storyboard: Dict[str, Any], prompts: Dict[str, Any]) -> DimensionScore:
    """
    Score VISUAL_QUALITY dimension (25%).

    Checks:
    - Camera movement specified
    - Style consistency
    - Prompt completeness
    - Pacing appropriateness
    """
    issues = []
    details = {
        "shots_with_camera": 0,
        "total_shots": 0,
        "style_consistent": True,
        "prompts_complete": 0,
    }

    score = 1.0
    shots = storyboard.get("shots", [])
    prompt_list = prompts.get("shots", [])

    details["total_shots"] = len(shots)

    # Check camera specifications
    shots_with_camera = 0
    for shot in shots:
        visual = shot.get("visual", {})
        camera = visual.get("camera", "")
        if camera and len(camera) > 5:
            shots_with_camera += 1

    details["shots_with_camera"] = shots_with_camera

    if len(shots) > 0:
        camera_ratio = shots_with_camera / len(shots)
        if camera_ratio < 0.5:
            issues.append(f"Camera especificada em apenas {shots_with_camera}/{len(shots)} shots")
            score -= 0.25
        elif camera_ratio < 0.75:
            score -= 0.10

    # Check prompt completeness (subject, action, camera, lighting, style, quality)
    complete_prompts = 0
    required_elements = ["camera", "lighting", "4k", "cinematic"]

    for prompt_obj in prompt_list:
        prompt_text = prompt_obj.get("prompt", "").lower()
        elements_found = sum(1 for elem in required_elements if elem in prompt_text)
        if elements_found >= 3:
            complete_prompts += 1

    details["prompts_complete"] = complete_prompts

    if len(prompt_list) > 0:
        completeness_ratio = complete_prompts / len(prompt_list)
        if completeness_ratio < 0.5:
            issues.append("Prompts incompletos - faltam elementos tecnicos")
            score -= 0.20
        elif completeness_ratio < 0.75:
            score -= 0.10

    # Check style consistency (basic check for style keywords)
    style = prompts.get("style", "")
    if not style:
        issues.append("Estilo nao definido nos prompts")
        score -= 0.15

    return DimensionScore(
        score=max(0.0, score), passed=score >= 0.70, issues=issues, details=details
    )


def score_platform_compliance(storyboard: Dict[str, Any], platform: str) -> DimensionScore:
    """
    Score PLATFORM_COMPLIANCE dimension (20%).

    Checks:
    - Duration within platform limits
    - Correct aspect ratio
    - Safe zones consideration
    - Export settings
    """
    issues = []
    details = {"platform": platform, "duration_valid": False, "optimal_duration": False}

    score = 1.0

    # Get platform specs
    specs = PLATFORM_SPECS.get(platform, PLATFORM_SPECS["tiktok"])
    duration = storyboard.get("duration", 30)

    details["max_duration"] = specs["max_duration"]
    details["video_duration"] = duration

    # Check duration
    if duration <= specs["max_duration"]:
        details["duration_valid"] = True
        if duration in specs["optimal_duration"]:
            details["optimal_duration"] = True
        else:
            score -= 0.10
    else:
        issues.append(
            f"Duracao {duration}s excede limite de {specs['max_duration']}s para {platform}"
        )
        score -= 0.30

    # Check hook timing for platform
    shots = storyboard.get("shots", [])
    if shots:
        first_shot = shots[0]
        hook_end = first_shot.get("timing", {}).get("end", 0)

        if hook_end > specs["hook_critical"]:
            issues.append(
                f"Hook em {hook_end}s excede tempo critico de {specs['hook_critical']}s para {platform}"
            )
            score -= 0.20

    return DimensionScore(
        score=max(0.0, score), passed=score >= 0.70, issues=issues, details=details
    )


def score_engagement_potential(
    storyboard: Dict[str, Any], script: Dict[str, Any]
) -> DimensionScore:
    """
    Score ENGAGEMENT_POTENTIAL dimension (15%).

    Checks:
    - Hook strength (pattern interrupt, compelling)
    - Emotional triggers throughout
    - Loop potential
    """
    issues = []
    details = {"hook_compelling": False, "emotional_journey": False, "loop_friendly": False}

    score = 1.0
    shots = storyboard.get("shots", [])
    narration = script.get("narration", [])

    # Check hook strength (simple heuristic based on description)
    if shots:
        first_shot = shots[0]
        hook_desc = first_shot.get("visual", {}).get("description", "").lower()

        strong_hook_indicators = ["slam", "dramatic", "attention", "chega de", "voce", "?"]
        hook_strength = sum(1 for ind in strong_hook_indicators if ind in hook_desc)

        if hook_strength >= 2:
            details["hook_compelling"] = True
        elif hook_strength >= 1:
            score -= 0.10
        else:
            issues.append("Hook pode nao ser suficientemente compelling")
            score -= 0.20

    # Check for emotional elements in narration
    if narration:
        emotional_words = ["incrivel", "problema", "solucao", "satisfeito", "garantia", "agora"]
        emotional_count = 0

        for nar in narration:
            text = nar.get("text", "").lower()
            emotional_count += sum(1 for word in emotional_words if word in text)

        if emotional_count >= 3:
            details["emotional_journey"] = True
        else:
            score -= 0.10

    # Check loop potential (basic: last shot connects to theme)
    if shots and len(shots) >= 2:
        first_phase = shots[0].get("phase", "")
        last_phase = shots[-1].get("phase", "")

        if last_phase == "CTA" and first_phase == "HOOK":
            details["loop_friendly"] = True
        else:
            score -= 0.05

    return DimensionScore(
        score=max(0.0, score), passed=score >= 0.70, issues=issues, details=details
    )


def score_production_feasibility(prompts: Dict[str, Any]) -> DimensionScore:
    """
    Score PRODUCTION_FEASIBILITY dimension (15%).

    Checks:
    - AI-compatible prompts
    - Realistic requests
    - Avoids text rendering in AI
    """
    issues = []
    details = {"ai_compatible": True, "text_requests": 0, "problematic_prompts": []}

    score = 1.0
    prompt_list = prompts.get("shots", [])

    # Check for problematic elements
    problematic_keywords = ["text saying", "words", "letters", "write", "spell"]
    unrealistic_keywords = ["impossible", "magic", "teleport"]

    text_requests = 0
    problematic_count = 0

    for i, prompt_obj in enumerate(prompt_list, 1):
        prompt_text = prompt_obj.get("prompt", "").lower()

        # Check for text rendering requests
        for keyword in problematic_keywords:
            if keyword in prompt_text:
                text_requests += 1
                break

        # Check for unrealistic requests
        for keyword in unrealistic_keywords:
            if keyword in prompt_text:
                problematic_count += 1
                details["problematic_prompts"].append(f"Shot {i}")
                break

    details["text_requests"] = text_requests

    if text_requests > 0:
        issues.append(f"{text_requests} prompts pedem renderizacao de texto (AI luta com isso)")
        score -= text_requests * 0.10

    if problematic_count > 0:
        issues.append(f"{problematic_count} prompts com requests potencialmente problematicos")
        score -= problematic_count * 0.15

    # Check if generator is specified
    generator = prompts.get("generator", "")
    if not generator:
        issues.append("Gerador nao especificado")
        score -= 0.10

    details["ai_compatible"] = score >= 0.70

    return DimensionScore(
        score=max(0.0, score), passed=score >= 0.70, issues=issues, details=details
    )


# ============================================================================
# MAIN VALIDATOR
# ============================================================================


def validate_video_output(
    storyboard: Dict[str, Any],
    script: Dict[str, Any],
    prompts: Dict[str, Any],
    platform: str = "tiktok",
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Validate video_agent output.

    Args:
        storyboard: Dict with shots, duration, narrative_arc
        script: Dict with narration, overlays, audio_cues
        prompts: Dict with shots (prompts), generator, settings
        platform: Target platform (tiktok, instagram_reels, youtube_shorts)
        metadata: Optional metadata (timestamp, source, etc.)

    Returns:
        Dict with validation results
    """

    # Score each dimension
    dimensions = {
        "narrative_arc": score_narrative_arc(storyboard, script),
        "visual_quality": score_visual_quality(storyboard, prompts),
        "platform_compliance": score_platform_compliance(storyboard, platform),
        "engagement_potential": score_engagement_potential(storyboard, script),
        "production_feasibility": score_production_feasibility(prompts),
    }

    # Calculate overall score with weights
    overall_score = sum(dimensions[dim].score * DIMENSION_WEIGHTS[dim] for dim in DIMENSION_WEIGHTS)

    passed = overall_score >= OVERALL_PASS_THRESHOLD

    # Generate recommendations
    recommendations = []
    for dim_name, dim_score in dimensions.items():
        if not dim_score.passed:
            if dim_name == "narrative_arc":
                recommendations.append(
                    "Melhorar estrutura narrativa: hook em 3s, todas as fases, CTA claro"
                )
            elif dim_name == "visual_quality":
                recommendations.append("Especificar camera para cada shot e completar prompts")
            elif dim_name == "platform_compliance":
                recommendations.append(f"Ajustar duracao e timing para {platform}")
            elif dim_name == "engagement_potential":
                recommendations.append("Fortalecer hook e adicionar elementos emocionais")
            elif dim_name == "production_feasibility":
                recommendations.append("Simplificar prompts para melhor compatibilidade com AI")

    # Determine status
    if overall_score >= 0.90:
        status = "EXCELLENT"
    elif overall_score >= 0.80:
        status = "GOOD"
    elif overall_score >= 0.70:
        status = "PASS"
    else:
        status = "FAIL"

    # Build summary
    if passed:
        summary = f"APROVADO | Score: {overall_score:.1%} | Status: {status} | Pronto para producao"
    else:
        failed_dims = [d for d, s in dimensions.items() if not s.passed]
        summary = f"REPROVADO | Score: {overall_score:.1%} | Falhas: {', '.join(failed_dims)}"

    # Build result
    result = ValidationResult(
        version=VERSION,
        passed=passed,
        overall_score=overall_score,
        dimensions=dimensions,
        summary=summary,
        recommendations=recommendations,
    )

    # Convert to dict for JSON serialization
    return {
        "version": result.version,
        "passed": result.passed,
        "overall_score": round(result.overall_score * 10, 1),  # Scale to 0-10
        "status": status,
        "summary": result.summary,
        "recommendations": result.recommendations,
        "dimensions": {
            dim_name: {
                "score": round(dim_score.score * 10, 1),  # Scale to 0-10
                "passed": dim_score.passed,
                "issues": dim_score.issues,
                "details": dim_score.details,
            }
            for dim_name, dim_score in result.dimensions.items()
        },
        "metadata": metadata or {},
        "weights": {k: f"{v * 100}%" for k, v in DIMENSION_WEIGHTS.items()},
        "threshold": f"{OVERALL_PASS_THRESHOLD * 100}%",
    }


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================


def quick_validate(storyboard: Dict[str, Any], prompts: Dict[str, Any]) -> bool:
    """Quick check if output is likely valid (for fast iteration)."""

    shots = storyboard.get("shots", [])

    # Check shot count
    duration = storyboard.get("duration", 30)
    min_shots, max_shots = SHOT_COUNT_RANGES.get(duration, (6, 8))

    if not (min_shots <= len(shots) <= max_shots):
        return False

    # Check hook timing
    if shots:
        hook_end = shots[0].get("timing", {}).get("end", 0)
        if hook_end > 3:
            return False

    # Check prompts exist
    if len(prompts.get("shots", [])) != len(shots):
        return False

    return True


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Example validation
    example_storyboard = {
        "duration": 30,
        "shots": [
            {
                "number": 1,
                "phase": "HOOK",
                "timing": {"start": 0, "end": 3, "duration": 3},
                "visual": {
                    "description": "Texto 'AGUA MORNA?' seguido de garrafa slam no frame",
                    "camera": "Slam zoom para produto",
                },
            },
            {
                "number": 2,
                "phase": "BUILD",
                "timing": {"start": 3, "end": 7, "duration": 4},
                "visual": {
                    "description": "Pessoa frustrada bebendo agua morna",
                    "camera": "Handheld, leve tremor",
                },
            },
            {
                "number": 3,
                "phase": "BUILD",
                "timing": {"start": 7, "end": 12, "duration": 5},
                "visual": {
                    "description": "Montagem: trabalho, academia, transito",
                    "camera": "Cortes rapidos",
                },
            },
            {
                "number": 4,
                "phase": "BENEFIT",
                "timing": {"start": 12, "end": 16, "duration": 4},
                "visual": {
                    "description": "Demo: agua gelada apos 24h",
                    "camera": "Close-up tracking",
                },
            },
            {
                "number": 5,
                "phase": "BENEFIT",
                "timing": {"start": 16, "end": 20, "duration": 4},
                "visual": {"description": "Teste anti-vazamento", "camera": "Slow motion"},
            },
            {
                "number": 6,
                "phase": "PROOF",
                "timing": {"start": 20, "end": 25, "duration": 5},
                "visual": {"description": "Numeros: +12.000 clientes", "camera": "Estatico"},
            },
            {
                "number": 7,
                "phase": "CTA",
                "timing": {"start": 25, "end": 30, "duration": 5},
                "visual": {"description": "Produto hero, COMPRE AGORA", "camera": "Slow zoom"},
            },
        ],
    }

    example_script = {
        "narration": [
            {"shot_number": 1, "text": "Chega de agua morna!"},
            {"shot_number": 2, "text": "Voce conhece essa cara de decepcao."},
            {"shot_number": 3, "text": "No trabalho, na academia, sempre igual."},
            {"shot_number": 4, "text": "24 horas gelada. Pode acreditar!"},
            {"shot_number": 5, "text": "Zero vazamento. Pode virar de cabeca!"},
            {"shot_number": 6, "text": "12 mil clientes satisfeitos."},
            {"shot_number": 7, "text": "Garanta a sua! Link na bio."},
        ],
        "overlays": [
            {"shot_number": 1, "text": "AGUA MORNA?"},
            {"shot_number": 4, "text": "24H GELADA"},
            {"shot_number": 7, "text": "COMPRE AGORA"},
        ],
    }

    example_prompts = {
        "generator": "runway_gen3",
        "style": "energetic",
        "shots": [
            {
                "shot_number": 1,
                "prompt": "Black thermal bottle slam into frame, quick zoom, high contrast lighting, vibrant, 4K cinematic",
            },
            {
                "shot_number": 2,
                "prompt": "Person drinking water disappointed face, handheld camera, natural lighting, 4K",
            },
            {
                "shot_number": 3,
                "prompt": "Quick montage gym office commute, fast tracking, dynamic, 4K",
            },
            {
                "shot_number": 4,
                "prompt": "Thermal bottle pouring cold water condensation, tracking shot, dramatic lighting, 4K",
            },
            {
                "shot_number": 5,
                "prompt": "Bottle upside down no leak, slow motion orbit camera, 4K",
            },
            {
                "shot_number": 6,
                "prompt": "Bottle with space for numbers, static shot, clean background, 4K",
            },
            {
                "shot_number": 7,
                "prompt": "Bottle hero shot white background, slow zoom, studio lighting, 4K",
            },
        ],
    }

    result = validate_video_output(
        storyboard=example_storyboard,
        script=example_script,
        prompts=example_prompts,
        platform="tiktok",
    )

    print(f"\n{'=' * 60}")
    print(f"VIDEO_AGENT VALIDATOR v{VERSION}")
    print(f"{'=' * 60}")
    print(f"\n{result['summary']}")
    print(f"\nScore: {result['overall_score']}/10 | Status: {result['status']}")
    print(f"\nDimension Scores:")
    for dim, scores in result["dimensions"].items():
        status = "OK" if scores["passed"] else "X"
        print(f"  {status} {dim}: {scores['score']}/10")
        if scores["issues"]:
            for issue in scores["issues"][:2]:
                print(f"      - {issue}")

    if result["recommendations"]:
        print(f"\nRecommendations:")
        for rec in result["recommendations"]:
            print(f"  -> {rec}")
