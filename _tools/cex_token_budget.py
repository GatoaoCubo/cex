#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Token Budget -- accurate token counting + prompt budget allocation.

Uses tiktoken for real token counts. Allocates budget across F6 PRODUCE
prompt sections to prevent context overflow.

Usage:
    python cex_token_budget.py --count "some text here"
    python cex_token_budget.py --count --file path/to/artifact.md
    python cex_token_budget.py --budget --max-tokens 8192
    python cex_token_budget.py --budget --model claude-sonnet-4-6
"""

import argparse
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Token Counting
# ---------------------------------------------------------------------------

# Model -> tiktoken encoding mapping (static fallback)
MODEL_ENCODINGS = {
    # Anthropic (use cl100k_base as closest approximation)
    "claude-sonnet-4-6": "cl100k_base",
    "claude-opus-4-6": "cl100k_base",
    "claude-haiku-4-5-20251001": "cl100k_base",
    # OpenAI
    "gpt-4o": "o200k_base",
    "gpt-4": "cl100k_base",
    "gpt-3.5-turbo": "cl100k_base",
}

# Model -> max output tokens (static fallback)
MODEL_MAX_TOKENS = {
    "claude-sonnet-4-6": 64000,
    "claude-opus-4-6": 128000,
    "claude-haiku-4-5-20251001": 64000,
    "gpt-4o": 16384,
    "gpt-4.1": 32768,
    "gpt-4.1-mini": 32768,
}


def get_context_window(nucleus: str) -> int:
    """Resolve context window for a nucleus via model resolver.

    Falls back to 200000 if resolver unavailable.
    """
    try:
        from _tools.cex_model_resolver import resolve_model
        return resolve_model(nucleus).get("context", 200000)
    except Exception:
        return 200000


def get_model_for_nucleus(nucleus: str) -> str:
    """Resolve model string for a nucleus via model resolver.

    Falls back to claude-sonnet-4-6 if resolver unavailable.
    """
    try:
        from _tools.cex_model_resolver import get_model_string
        return get_model_string(nucleus)
    except Exception:
        return "claude-sonnet-4-6"

_encoder_cache: dict = {}


def get_encoder(model: str = "claude-sonnet-4-6"):
    """Get tiktoken encoder for model. Falls back to cl100k_base."""
    encoding_name = MODEL_ENCODINGS.get(model, "cl100k_base")
    if encoding_name not in _encoder_cache:
        try:
            import tiktoken
            _encoder_cache[encoding_name] = tiktoken.get_encoding(encoding_name)
        except ImportError:
            return None
    return _encoder_cache.get(encoding_name)


def count_tokens(text: str, model: str = "claude-sonnet-4-6") -> int:
    """Count tokens in text using tiktoken. Falls back to word-based estimate."""
    encoder = get_encoder(model)
    if encoder:
        return len(encoder.encode(text))
    # Fallback: ~1.3 tokens per word (empirical for English)
    return int(len(text.split()) * 1.3)


def count_tokens_by_section(sections: dict[str, str], model: str = "claude-sonnet-4-6") -> dict[str, int]:
    """Count tokens for each named section."""
    return {name: count_tokens(text, model) for name, text in sections.items() if text}


# ---------------------------------------------------------------------------
# Budget Allocation
# ---------------------------------------------------------------------------

# Section priority and max-share (fraction of total budget)
# Higher priority sections get their full allocation first;
# lower priority sections share remaining budget.
SECTION_BUDGET = {
    "identity":    {"priority": 1, "max_share": 0.10, "min_tokens": 100},
    "constraints": {"priority": 1, "max_share": 0.05, "min_tokens": 50},
    "instruction": {"priority": 2, "max_share": 0.15, "min_tokens": 200},
    "template":    {"priority": 2, "max_share": 0.10, "min_tokens": 100},
    "task":        {"priority": 1, "max_share": 0.08, "min_tokens": 80},
    "knowledge":   {"priority": 3, "max_share": 0.25, "min_tokens": 200},
    "examples":    {"priority": 3, "max_share": 0.15, "min_tokens": 150},
    "plan":        {"priority": 4, "max_share": 0.08, "min_tokens": 50},
    "tools":       {"priority": 4, "max_share": 0.05, "min_tokens": 50},
    "retry":       {"priority": 1, "max_share": 0.10, "min_tokens": 50},
}


def allocate_budget(
    sections: dict[str, str],
    max_tokens: int = 8192,
    model: str = "claude-sonnet-4-6",
    reserve_output: int = 4096,
) -> dict[str, dict]:
    """Allocate token budget across prompt sections.

    Args:
        sections: {section_name: text_content}
        max_tokens: Total context window for input
        model: Model name for token counting
        reserve_output: Tokens reserved for LLM output (not counted in budget)

    Returns:
        Dict per section: {tokens_actual, tokens_budget, truncated, text}
    """
    budget = max_tokens - reserve_output
    if budget <= 0:
        budget = max_tokens // 2

    # Count actual tokens per section
    actual = count_tokens_by_section(sections, model)
    total_actual = sum(actual.values())

    # If everything fits, no truncation needed
    if total_actual <= budget:
        return {
            name: {
                "tokens_actual": actual.get(name, 0),
                "tokens_budget": actual.get(name, 0),
                "truncated": False,
                "text": text,
            }
            for name, text in sections.items()
            if text
        }

    # Need to truncate -- allocate by priority
    result = {}
    remaining = budget

    # Sort sections by priority (lower = higher priority)
    sorted_sections = sorted(
        [(name, text) for name, text in sections.items() if text],
        key=lambda x: SECTION_BUDGET.get(x[0], {}).get("priority", 5),
    )

    for name, text in sorted_sections:
        cfg = SECTION_BUDGET.get(name, {"priority": 5, "max_share": 0.10, "min_tokens": 50})
        section_tokens = actual.get(name, 0)
        max_allowed = int(budget * cfg["max_share"])
        min_allowed = cfg["min_tokens"]

        # Allocate: min(actual, max_allowed, remaining)
        allocated = min(section_tokens, max_allowed, remaining)
        allocated = max(allocated, min(min_allowed, remaining))  # Ensure minimum

        truncated = section_tokens > allocated
        if truncated:
            text = truncate_to_tokens(text, allocated, model)

        result[name] = {
            "tokens_actual": section_tokens,
            "tokens_budget": allocated,
            "truncated": truncated,
            "text": text,
        }
        remaining -= allocated
        if remaining <= 0:
            break

    # Any sections that didn't get allocated
    for name, text in sections.items():
        if text and name not in result:
            result[name] = {
                "tokens_actual": actual.get(name, 0),
                "tokens_budget": 0,
                "truncated": True,
                "text": "",
            }

    return result


def truncate_to_tokens(text: str, max_tokens: int, model: str = "claude-sonnet-4-6") -> str:
    """Truncate text to fit within max_tokens, preserving paragraph boundaries."""
    encoder = get_encoder(model)
    if not encoder:
        # Fallback: truncate by estimated word count
        words = text.split()
        target_words = int(max_tokens / 1.3)
        return " ".join(words[:target_words]) + "\n\n[... truncated to fit token budget]"

    tokens = encoder.encode(text)
    if len(tokens) <= max_tokens:
        return text

    # Decode truncated tokens, try to end at paragraph boundary
    truncated = encoder.decode(tokens[:max_tokens - 10])  # Reserve 10 tokens for marker

    # Find last paragraph break
    last_para = truncated.rfind("\n\n")
    if last_para > len(truncated) // 2:
        truncated = truncated[:last_para]

    return truncated + "\n\n[... truncated to fit token budget]"


# ---------------------------------------------------------------------------
# Budget Tracker -- Continuation-aware token governor
# Pattern: OpenClaude BudgetTracker (tokenBudget.ts)
# ---------------------------------------------------------------------------

from dataclasses import dataclass, field
from time import time as _time

COMPLETION_THRESHOLD = 0.90     # Stop at 90% budget consumed
DIMINISHING_THRESHOLD = 500     # If producing < this per cycle, stop


@dataclass
class BudgetTracker:
    """Track token consumption with continuation + diminishing returns detection.

    Usage:
        tracker = BudgetTracker()
        for section in sections:
            decision = check_token_budget(tracker, max_tokens, current_tokens)
            if decision.action == "stop":
                break
            # ... produce section ...
    """
    continuation_count: int = 0
    last_delta_tokens: int = 0
    last_global_tokens: int = 0
    started_at: float = field(default_factory=_time)

    @property
    def duration_ms(self) -> int:
        return int((_time() - self.started_at) * 1000)


@dataclass
class BudgetDecision:
    """Result of a budget check: continue producing or stop."""
    action: str                     # "continue" | "stop"
    pct: int = 0                    # % of budget consumed
    turn_tokens: int = 0
    budget: int = 0
    nudge_message: str = ""
    diminishing_returns: bool = False
    continuation_count: int = 0
    duration_ms: int = 0


def check_token_budget(
    tracker: BudgetTracker,
    budget: int,
    current_tokens: int,
) -> BudgetDecision:
    """Check whether to continue producing or stop.

    Call between F6 sections to gate production.
    Returns CONTINUE with nudge, or STOP with completion stats.

    Logic:
      - Under 90% budget AND not diminishing -> CONTINUE
      - 3+ continuations with <500 new tokens each -> STOP (diminishing)
      - Over 90% -> STOP (budget exhausted)
    """
    if budget <= 0:
        return BudgetDecision(action="stop")

    pct = round((current_tokens / budget) * 100)
    delta = current_tokens - tracker.last_global_tokens

    # Diminishing returns: 3+ continuations producing <500 tokens each
    is_diminishing = (
        tracker.continuation_count >= 3
        and delta < DIMINISHING_THRESHOLD
        and tracker.last_delta_tokens < DIMINISHING_THRESHOLD
    )

    if not is_diminishing and current_tokens < budget * COMPLETION_THRESHOLD:
        tracker.continuation_count += 1
        tracker.last_delta_tokens = delta
        tracker.last_global_tokens = current_tokens

        remaining = budget - current_tokens
        nudge = (
            f"[Budget: {pct}% used ({current_tokens:,}/{budget:,} tokens). "
            f"{remaining:,} remaining. Continue producing.]"
        )
        return BudgetDecision(
            action="continue",
            pct=pct,
            turn_tokens=current_tokens,
            budget=budget,
            nudge_message=nudge,
            continuation_count=tracker.continuation_count,
        )

    if is_diminishing or tracker.continuation_count > 0:
        return BudgetDecision(
            action="stop",
            pct=pct,
            turn_tokens=current_tokens,
            budget=budget,
            diminishing_returns=is_diminishing,
            continuation_count=tracker.continuation_count,
            duration_ms=tracker.duration_ms,
        )

    return BudgetDecision(action="stop")


def budget_aware_produce(
    sections: list[dict],
    max_tokens: int,
    model: str = "claude-sonnet-4-6",
) -> tuple[list[str], BudgetDecision]:
    """Produce artifact sections with budget governance.

    Each section is produced in order. After each, we check the budget.
    Stops early on diminishing returns or budget exhaustion.

    Args:
        sections: [{"name": str, "content": str}, ...]
        max_tokens: Total token budget for production
        model: Model for token counting

    Returns:
        (produced_texts, final_decision)
    """
    tracker = BudgetTracker()
    produced = []
    total_tokens = 0
    last_decision = BudgetDecision(action="stop")

    for section in sections:
        decision = check_token_budget(tracker, max_tokens, total_tokens)
        last_decision = decision

        if decision.action == "stop":
            if decision.diminishing_returns:
                produced.append(
                    f"<!-- Budget: stopped at {decision.pct}% (diminishing returns) -->"
                )
            elif decision.pct >= 90:
                produced.append(
                    f"<!-- Budget: stopped at {decision.pct}% (budget exhausted) -->"
                )
            break

        content = section.get("content", "")
        remaining_budget = max_tokens - total_tokens
        section_tokens = count_tokens(content, model)

        if section_tokens > remaining_budget:
            content = truncate_to_tokens(content, remaining_budget, model)
            section_tokens = count_tokens(content, model)

        produced.append(content)
        total_tokens += section_tokens

    return produced, last_decision


# ---------------------------------------------------------------------------
# Prompt Analysis
# ---------------------------------------------------------------------------


def analyze_prompt(prompt: str, model: str = "claude-sonnet-4-6") -> dict:
    """Analyze a composed prompt's token distribution by section."""
    # Split by section headers (# IDENTITY, # CONSTRAINTS, etc.)
    import re
    section_re = re.compile(r"^# ([A-Z][A-Z_ ]+)$", re.MULTILINE)
    parts = section_re.split(prompt)

    sections = {}
    if len(parts) > 1:
        # parts = [preamble, header1, content1, header2, content2, ...]
        for i in range(1, len(parts) - 1, 2):
            name = parts[i].strip().lower().replace(" ", "_")
            content = parts[i + 1].strip() if i + 1 < len(parts) else ""
            sections[name] = content
    else:
        sections["full_prompt"] = prompt

    token_counts = count_tokens_by_section(sections, model)
    total = count_tokens(prompt, model)

    return {
        "total_tokens": total,
        "sections": {
            name: {
                "tokens": token_counts.get(name, 0),
                "pct": round(token_counts.get(name, 0) / total * 100, 1) if total > 0 else 0,
            }
            for name in sections
        },
        "model": model,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="CEX Token Budget -- token counting + allocation")
    parser.add_argument("--count", nargs="?", const="", help="Count tokens in text (or use --file)")
    parser.add_argument("--file", "-", help="Count tokens in a file")
    parser.add_argument("--budget", action="store_true", help="Show budget allocation for a model")
    parser.add_argument("--analyze", help="Analyze a prompt file's token distribution")
    parser.add_argument("--model", "-m", default="claude-sonnet-4-6", help="Model for counting")
    parser.add_argument("--max-tokens", type=int, default=8192, help="Max input tokens")
    args = parser.parse_args()

    if args.count is not None:
        if args.file:
            text = Path(args.file).read_text(encoding="utf-8")
        elif args.count:
            text = args.count
        else:
            text = sys.stdin.read()
        tokens = count_tokens(text, args.model)
        words = len(text.split())
        ratio = tokens / words if words > 0 else 0
        print(f"  Tokens: {tokens:,}")
        print(f"  Words:  {words:,}")
        print(f"  Ratio:  {ratio:.2f} tokens/word")
        print(f"  Model:  {args.model}")
        return

    if args.budget:
        print(f"\n=== Token Budget Allocation (max={args.max_tokens}, model={args.model}) ===\n")
        print(f"  {'Section':15s} {'Priority':>8s} {'Max Share':>10s} {'Min Tokens':>10s} {'Budget':>8s}")
        print(f"  {'-'*55}")
        reserve = 4096
        available = args.max_tokens - reserve
        for name, cfg in sorted(SECTION_BUDGET.items(), key=lambda x: x[1]["priority"]):
            budget_tokens = int(available * cfg["max_share"])
            print(
                f"  {name:15s} {cfg['priority']:>8d} {cfg['max_share']:>9.0%}"
                f" {cfg['min_tokens']:>10d} {budget_tokens:>8d}"
            )
        print(f"\n  Available: {available:,} tokens (max {args.max_tokens:,} - {reserve:,} output reserve)")
        return

    if args.analyze:
        text = Path(args.analyze).read_text(encoding="utf-8")
        analysis = analyze_prompt(text, args.model)
        print(f"\n=== Prompt Analysis ({analysis['model']}) ===\n")
        print(f"  Total: {analysis['total_tokens']:,} tokens\n")
        for name, info in sorted(analysis["sections"].items(), key=lambda x: -x[1]["tokens"]):
            bar = "#" * int(info["pct"] / 2)
            print(f"  {name:20s} {info['tokens']:>6,} ({info['pct']:>5.1f}%) {bar}")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
