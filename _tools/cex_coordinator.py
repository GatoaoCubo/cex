#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Coordinator Protocol -- N07 orchestration runtime.

Pattern: OpenClaude Coordinator Mode (coordinatorMode.ts, Section 1-6 protocol)
Adapted for CEX: N07 NEVER builds, only orchestrates.

The Coordinator Protocol:
  1. Coordinate, don't execute.
  2. Tools: spawn, send_message, stop (NO Bash, Read, Write, Edit)
  3. Workers execute autonomously with full tool access.
  4. Workflow: Research -> SYNTHESIS GATE -> Implement -> VERIFY GATE
  5. Synthesis = prove understanding before dispatching next phase.
  6. "Never delegate understanding" -- no "based on your findings" prompts.

Integration:
  - Uses cex_agent_spawn.py for worker lifecycle
  - Uses cex_gdp.py for decision gating
  - Uses cex_router.py for provider resolution
  - Outputs to cex_mission_runner.py wave format

Usage:
    from cex_coordinator import CexCoordinator

    coord = CexCoordinator("my_mission")
    # Phase 1: Research
    wids = coord.research_phase([
        {"nucleus": "n01", "spec": "Investigate auth module..."},
        {"nucleus": "n04", "spec": "Find all test files for auth..."},
    ])
    results = coord.collect(wids)

    # Synthesis Gate
    synthesis = coord.synthesize(results)

    # Phase 2: Implement
    coord.implement_phase(synthesis.implementation_specs)

CLI:
    python cex_coordinator.py --mission ASSIMILATE --plan plan.yaml
    python cex_coordinator.py --status
"""

import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "_tools"))

from cex_agent_spawn import SpawnMode, TaskNotification, get_spawner

# ---------------------------------------------------------------------------
# Anti-Pattern Detection
# ---------------------------------------------------------------------------

LAZY_DELEGATION_PATTERNS = [
    r"based on (?:your|the) (?:findings|research|analysis)",
    r"based on what (?:you|the worker) found",
    r"implement (?:the|a) fix",
    r"fix (?:the|this) (?:bug|issue|problem)",
    r"do what(?:'s| is) needed",
    r"handle (?:this|it) appropriately",
]

_LAZY_RE = re.compile("|".join(LAZY_DELEGATION_PATTERNS), re.IGNORECASE)


def detect_lazy_delegation(spec: str) -> Optional[str]:
    """Detect "never delegate understanding" anti-patterns.

    Good spec: "Fix null pointer in src/auth/validate.ts:42. Session.user is
                undefined when expired. Add null check before user.id."
    Bad spec:  "Based on your findings, fix the bug."

    Returns the matched pattern string if lazy, None if OK.
    """
    match = _LAZY_RE.search(spec)
    if match:
        return match.group(0)
    return None


def validate_synthesis_spec(spec: str) -> tuple[bool, list[str]]:
    """Validate that a synthesis spec proves understanding.

    A valid spec should cite:
    - Specific file paths (src/..., _tools/..., etc.)
    - What specifically to change
    - Expected outcome

    Returns (is_valid, issues).
    """
    issues = []

    # Check for lazy delegation
    lazy = detect_lazy_delegation(spec)
    if lazy:
        issues.append(f"Lazy delegation detected: '{lazy}'. Synthesize findings yourself.")

    # Check for specificity (file paths)
    has_paths = bool(re.search(r'(?:src/|_tools/|P\d{2}_|N\d{2}_|\.cex/|archetypes/)\S+', spec))
    if not has_paths:
        issues.append("No specific file paths cited. A synthesis spec must reference exact files.")

    # Check for actionable verbs
    action_verbs = ["add", "remove", "replace", "change", "fix", "create", "update", "modify", "insert"]
    has_action = any(verb in spec.lower() for verb in action_verbs)
    if not has_action:
        issues.append("No actionable verb found. Spec should say WHAT to do, not just describe.")

    # Minimum length (too short = too vague)
    if len(spec.strip()) < 50:
        issues.append(f"Spec too short ({len(spec)} chars). Minimum 50 chars for a meaningful spec.")

    return len(issues) == 0, issues


# ---------------------------------------------------------------------------
# Synthesis
# ---------------------------------------------------------------------------

@dataclass
class SynthesisResult:
    """Result of coordinator synthesizing worker research results."""
    summary: str
    key_findings: List[str]
    file_paths: List[str]
    implementation_specs: List[dict]   # [{"nucleus": "n03", "spec": "..."}]
    verification_tasks: List[dict]     # [{"nucleus": "n01", "spec": "..."}]
    decisions_needed: List[str] = field(default_factory=list)
    is_valid: bool = True
    issues: List[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Coordinator
# ---------------------------------------------------------------------------

class CexCoordinator:
    """N07 Coordinator Protocol -- never builds, only orchestrates.

    Implements the 4-phase workflow:
      Research (parallel) -> SYNTHESIS GATE -> Implement (sequential) -> Verify (fresh)
    """

    # Coordinator CANNOT use these tools directly
    FORBIDDEN_TOOLS = {"bash", "read", "write", "edit", "compile", "build"}

    def __init__(self, mission_id: str = ""):
        self.mission_id = mission_id or f"mission_{int(time.time())}"
        self.spawner = get_spawner()
        self.phases: List[dict] = []
        self.current_phase: str = ""
        self.synthesis_history: List[SynthesisResult] = []

    # ------------------------------------------------------------------
    # Phase 1: RESEARCH (parallel)
    # ------------------------------------------------------------------

    def research_phase(
        self,
        tasks: List[dict],
        timeout: float = 600,
    ) -> List[TaskNotification]:
        """Spawn parallel research workers and wait for all results.

        Research tasks are read-only -- workers investigate, don't modify.
        Launch all at once for maximum parallelism.

        Args:
            tasks: [{"nucleus": "n01", "spec": "Investigate..."}, ...]
            timeout: Max seconds to wait for all workers.

        Returns:
            List of TaskNotifications (one per task).
        """
        self.current_phase = "research"

        # Spawn all research workers in parallel
        worker_ids = []
        for task in tasks:
            # Prepend research directive
            spec = (
                f"RESEARCH TASK (read-only, do NOT modify files):\n\n"
                f"{task['spec']}\n\n"
                "Report: findings, specific file paths, line numbers, types involved."
            )
            wid = self.spawner.spawn(
                nucleus=task["nucleus"],
                task_spec=spec,
                mode=SpawnMode.SPAWN,
                mission=self.mission_id,
            )
            worker_ids.append(wid)

        # Wait for all
        results = self.spawner.wait_all(worker_ids, timeout=timeout)

        # Record phase
        self.phases.append({
            "phase": "research",
            "tasks": len(tasks),
            "completed": sum(1 for r in results if r.status == "completed"),
            "failed": sum(1 for r in results if r.status == "failed"),
            "at": time.time(),
        })

        return results

    # ------------------------------------------------------------------
    # SYNTHESIS GATE
    # ------------------------------------------------------------------

    def synthesize(self, research_results: List[TaskNotification]) -> SynthesisResult:
        """Coordinator's MOST IMPORTANT JOB: understand before dispatching next.

        Reads research results, extracts:
        - File paths mentioned
        - Decisions made
        - Gaps found

        Then builds implementation specs that PROVE understanding
        by citing specific paths, lines, and changes.

        The coordinator does NOT ask a worker to synthesize.
        The coordinator does this ITSELF.
        """
        self.current_phase = "synthesis"

        # Extract file paths from all results
        all_paths = []
        all_findings = []

        for r in research_results:
            text = r.result or r.summary or ""

            # Extract file paths
            paths = re.findall(
                r'(?:src/|_tools/|P\d{2}_|N\d{2}_|\.cex/|archetypes/|boot/)\S+',
                text,
            )
            all_paths.extend(paths)

            # Extract key findings (lines starting with - or *)
            findings = re.findall(r'(?:^|\n)\s*[-*]\s+(.+)', text)
            all_findings.extend(findings)

        # Deduplicate
        unique_paths = sorted(set(all_paths))
        unique_findings = list(dict.fromkeys(all_findings))  # Preserve order

        synthesis = SynthesisResult(
            summary=f"Research phase complete. {len(research_results)} workers reported.",
            key_findings=unique_findings[:20],  # Cap at 20
            file_paths=unique_paths,
            implementation_specs=[],
            verification_tasks=[],
        )

        self.synthesis_history.append(synthesis)
        return synthesis

    def validate_synthesis(self, synthesis: SynthesisResult) -> tuple[bool, list[str]]:
        """Validate synthesis before proceeding to implementation.

        Checks:
        - At least one file path cited
        - Implementation specs are specific (not lazy)
        - Verification tasks exist
        """
        issues = []

        if not synthesis.file_paths:
            issues.append("No file paths found in research results. Cannot proceed without specifics.")

        for i, spec in enumerate(synthesis.implementation_specs):
            spec_text = spec.get("spec", "")
            ok, spec_issues = validate_synthesis_spec(spec_text)
            if not ok:
                for issue in spec_issues:
                    issues.append(f"Impl spec #{i+1}: {issue}")

        synthesis.is_valid = len(issues) == 0
        synthesis.issues = issues
        return synthesis.is_valid, issues

    # ------------------------------------------------------------------
    # Phase 2: IMPLEMENT (sequential per file set)
    # ------------------------------------------------------------------

    def implement_phase(
        self,
        impl_specs: List[dict],
        timeout_per_task: float = 300,
    ) -> List[TaskNotification]:
        """Execute implementation specs sequentially.

        One writer per file set to avoid conflicts.
        On failure, continue the same worker (it has error context).

        Args:
            impl_specs: [{"nucleus": "n03", "spec": "Fix null in..."}]
            timeout_per_task: Max seconds per task.
        """
        self.current_phase = "implement"
        results = []

        for spec in impl_specs:
            spec_text = spec.get("spec", "")

            # Validate spec before dispatch
            lazy = detect_lazy_delegation(spec_text)
            if lazy:
                print(f"[COORDINATOR] BLOCKED: Lazy delegation in spec: '{lazy}'")
                print("[COORDINATOR] Rewrite the spec with specific files, lines, and changes.")
                results.append(TaskNotification(
                    task_id="blocked",
                    status="failed",
                    summary=f"Lazy delegation blocked: '{lazy}'",
                ))
                continue

            impl_spec = (
                f"IMPLEMENTATION TASK:\n\n"
                f"{spec_text}\n\n"
                "After completing, run relevant tests and commit your changes. "
                "Report the commit hash."
            )

            wid = self.spawner.spawn(
                nucleus=spec["nucleus"],
                task_spec=impl_spec,
                mode=SpawnMode.SPAWN,
                mission=self.mission_id,
            )

            result = self.spawner.wait_for(wid, timeout=timeout_per_task)

            # On failure, try to continue the same worker (it has error context)
            if result.status == "failed" and spec.get("retry", True):
                print(f"[COORDINATOR] Worker {wid} failed. Continuing with error context.")
                self.spawner.send_message(wid, (
                    f"Your previous attempt failed. Error context is preserved.\n"
                    f"Try a different approach. Original task: {spec_text[:200]}"
                ))
                result = self.spawner.wait_for(wid, timeout=timeout_per_task)

            results.append(result)

        self.phases.append({
            "phase": "implement",
            "tasks": len(impl_specs),
            "completed": sum(1 for r in results if r.status == "completed"),
            "failed": sum(1 for r in results if r.status == "failed"),
            "at": time.time(),
        })

        return results

    # ------------------------------------------------------------------
    # Phase 3: VERIFY (fresh workers)
    # ------------------------------------------------------------------

    def verify_phase(
        self,
        verify_tasks: List[dict],
        timeout: float = 300,
    ) -> List[TaskNotification]:
        """Verify implementation with FRESH workers.

        Fresh workers verify independently -- no implementation bias.
        They should PROVE the code works, not just confirm it exists.

        Args:
            verify_tasks: [{"nucleus": "n01", "spec": "Verify auth fix..."}]
        """
        self.current_phase = "verify"

        worker_ids = []
        for task in verify_tasks:
            spec = (
                f"VERIFICATION TASK (independent review):\n\n"
                f"{task['spec']}\n\n"
                f"Prove the code works. Don't just confirm it exists.\n"
                f"Run tests with the feature enabled. Investigate errors.\n"
                "Try edge cases and error paths."
            )
            wid = self.spawner.spawn(
                nucleus=task["nucleus"],
                task_spec=spec,
                mode=SpawnMode.SPAWN,
                mission=self.mission_id,
            )
            worker_ids.append(wid)

        results = self.spawner.wait_all(worker_ids, timeout=timeout)

        self.phases.append({
            "phase": "verify",
            "tasks": len(verify_tasks),
            "completed": sum(1 for r in results if r.status == "completed"),
            "failed": sum(1 for r in results if r.status == "failed"),
            "at": time.time(),
        })

        return results

    # ------------------------------------------------------------------
    # FULL WORKFLOW
    # ------------------------------------------------------------------

    def run_workflow(
        self,
        research_tasks: List[dict],
        timeout: float = 600,
    ) -> dict:
        """Run full coordinator workflow: research -> synthesize -> implement -> verify.

        This is the main entry point for a coordinated mission.
        Synthesis gate enforces understanding between phases.
        """
        report = {
            "mission_id": self.mission_id,
            "phases": [],
            "status": "running",
        }

        # Phase 1: Research
        print(f"\n[COORDINATOR] Phase 1: Research ({len(research_tasks)} tasks, parallel)")
        research_results = self.research_phase(research_tasks, timeout=timeout)
        report["phases"].append({
            "name": "research",
            "results": [r.to_dict() for r in research_results],
        })

        completed = [r for r in research_results if r.status == "completed"]
        if not completed:
            report["status"] = "failed"
            report["reason"] = "All research tasks failed"
            return report

        # Synthesis Gate
        print(f"\n[COORDINATOR] Synthesis Gate: processing {len(completed)} results")
        synthesis = self.synthesize(research_results)
        print(f"  Findings: {len(synthesis.key_findings)}")
        print(f"  File paths: {len(synthesis.file_paths)}")

        # NOTE: Implementation specs must be added by the caller (LLM or human)
        # after reviewing the synthesis. The coordinator extracts raw data;
        # the orchestrating LLM (or /guide) writes the specific specs.

        report["synthesis"] = {
            "findings": synthesis.key_findings,
            "file_paths": synthesis.file_paths,
            "impl_specs_needed": len(synthesis.implementation_specs),
        }
        report["status"] = "awaiting_specs"

        return report

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------

    def report(self) -> dict:
        """Full coordinator status report."""
        return {
            "mission_id": self.mission_id,
            "current_phase": self.current_phase,
            "phases": self.phases,
            "workers": self.spawner.status(),
            "syntheses": len(self.synthesis_history),
        }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    import argparse

    parser = argparse.ArgumentParser(description="CEX Coordinator Protocol")
    parser.add_argument("--mission", default="", help="Mission ID")
    parser.add_argument("--status", action="store_true", help="Show coordinator status")
    parser.add_argument("--validate-spec", metavar="TEXT", help="Validate a synthesis spec")
    parser.add_argument("--check-lazy", metavar="TEXT", help="Check for lazy delegation")
    args = parser.parse_args()

    if args.validate_spec:
        ok, issues = validate_synthesis_spec(args.validate_spec)
        if ok:
            print("PASS: Spec is specific and actionable")
        else:
            print("FAIL: Spec has issues:")
            for issue in issues:
                print(f"  - {issue}")

    elif args.check_lazy:
        lazy = detect_lazy_delegation(args.check_lazy)
        if lazy:
            print(f"LAZY DELEGATION DETECTED: '{lazy}'")
            print("Rewrite with specific files, lines, and changes.")
        else:
            print("OK: No lazy delegation detected")

    elif args.status:
        coord = CexCoordinator(args.mission)
        r = coord.report()
        print(yaml.dump(r, default_flow_style=False))

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
