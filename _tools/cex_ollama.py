#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_ollama.py -- Ollama Provider Client for CEX Pipeline.

Handles all Ollama interactions: model listing, generation, structured output
parsing, and retry logic for malformed output.

This is the bridge between CEX's 8F pipeline and local Ollama models.
It replaces the hardcoded llama3.2 calls scattered across cex_intent.py.

Usage:
    # As library
    from cex_ollama import OllamaClient
    client = OllamaClient()
    result = client.generate("qwen3:8b", prompt, system="You are a CEX builder.")

    # CLI
    python cex_ollama.py --list
    python cex_ollama.py --model qwen3:8b --prompt "Create a knowledge card about RAG"
    python cex_ollama.py --model qwen3:8b --health
    python cex_ollama.py --model qwen3:8b --prompt-file handoff.md
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

CEX_ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
DEFAULT_MODEL = os.environ.get("CEX_OLLAMA_MODEL", "qwen3:8b")
DEFAULT_TIMEOUT = int(os.environ.get("CEX_OLLAMA_TIMEOUT", "600"))
MAX_RETRIES = 2

# Structured output instructions appended to system prompt
STRUCTURE_ENFORCEMENT = """
CRITICAL OUTPUT FORMAT RULES:
1. Start with YAML frontmatter between --- delimiters
2. Include these fields: id, kind, title, version, quality, tags
3. quality MUST be: "null" (never self-score)
4. After frontmatter, write structured markdown with ## headings
5. Use tables (| col | col |) for structured data
6. Do NOT wrap output in ```markdown``` code blocks
7. Do NOT include chain-of-thought or reasoning preamble
8. Start DIRECTLY with ---
"""


@dataclass
class OllamaResponse:
    """Parsed response from Ollama API."""
    content: str
    model: str
    duration_ms: float = 0.0
    tokens_generated: int = 0
    tokens_per_second: float = 0.0
    success: bool = True
    error: str = ""


class OllamaClient:
    """Client for Ollama HTTP API with CEX-specific features."""

    def __init__(self, host: str = OLLAMA_HOST, timeout: int = DEFAULT_TIMEOUT):
        self.host = host.rstrip("/")
        self.timeout = timeout

    # -------------------------------------------------------------------
    # Core API
    # -------------------------------------------------------------------

    def health(self) -> bool:
        """Check if Ollama server is running."""
        try:
            req = urllib.request.Request(f"{self.host}/api/tags")
            with urllib.request.urlopen(req, timeout=5) as resp:
                return resp.status == 200
        except Exception:
            return False

    def list_models(self) -> list[dict]:
        """List installed models."""
        try:
            req = urllib.request.Request(f"{self.host}/api/tags")
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data.get("models", [])
        except Exception as e:
            print(f"[FAIL] Cannot list models: {e}", file=sys.stderr)
            return []

    def has_model(self, model: str) -> bool:
        """Check if a specific model is installed."""
        models = self.list_models()
        for m in models:
            name = m.get("name", "")
            # Match exact or without tag (qwen3:8b matches qwen3:8b)
            if name == model or name.split(":")[0] == model.split(":")[0]:
                return True
        return False

    def generate(
        self,
        model: str,
        prompt: str,
        system: str = "",
        temperature: float = 0.3,
        max_tokens: int = 8192,
        structured: bool = False,
    ) -> OllamaResponse:
        """Generate text via Ollama /api/generate endpoint.

        Args:
            model: Model name (e.g., 'qwen3:8b')
            prompt: User prompt
            system: System prompt (prepended)
            temperature: Sampling temperature (lower = more deterministic)
            max_tokens: Maximum output tokens
            structured: If True, append structure enforcement to system prompt

        Returns:
            OllamaResponse with content and metrics
        """
        if structured and STRUCTURE_ENFORCEMENT not in system:
            system = (system + "\n\n" + STRUCTURE_ENFORCEMENT).strip()

        # For DeepSeek R1, disable thinking mode to avoid verbose CoT
        # /no_think tag tells DeepSeek R1 to skip chain-of-thought
        if "deepseek" in model.lower() and "r1" in model.lower():
            prompt = "/no_think\n" + prompt

        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens,
            },
        }
        if system:
            payload["system"] = system

        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            f"{self.host}/api/generate",
            data=data,
            headers={"Content-Type": "application/json"},
        )

        try:
            start = time.monotonic()
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                elapsed_ms = (time.monotonic() - start) * 1000
                result = json.loads(resp.read().decode("utf-8"))

            content = result.get("response", "")
            eval_count = result.get("eval_count", 0)
            eval_duration = result.get("eval_duration", 1)  # nanoseconds

            # Strip DeepSeek R1 <think>...</think> blocks if present
            content = self._strip_thinking(content)

            return OllamaResponse(
                content=content.strip(),
                model=model,
                duration_ms=elapsed_ms,
                tokens_generated=eval_count,
                tokens_per_second=(eval_count / (eval_duration / 1e9))
                if eval_duration > 0 else 0,
            )
        except urllib.error.URLError as e:
            return OllamaResponse(
                content="", model=model, success=False,
                error=f"Connection failed: {e.reason}",
            )
        except Exception as e:
            return OllamaResponse(
                content="", model=model, success=False,
                error=str(e)[:200],
            )

    def generate_artifact(
        self,
        model: str,
        prompt: str,
        system: str = "",
        max_retries: int = MAX_RETRIES,
    ) -> OllamaResponse:
        """Generate a CEX artifact with retry on malformed output.

        Validates that output has YAML frontmatter and markdown structure.
        Retries with stronger formatting instructions if validation fails.
        """
        attempt = 0
        last_response = None

        while attempt <= max_retries:
            resp = self.generate(
                model=model,
                prompt=prompt,
                system=system,
                structured=True,
                temperature=0.2 + (attempt * 0.1),  # Slightly increase temp on retry
            )

            if not resp.success:
                return resp

            last_response = resp
            validation = self._validate_artifact_output(resp.content)

            if validation["valid"]:
                return resp

            # Retry with stronger prompt
            attempt += 1
            if attempt <= max_retries:
                issues = ", ".join(validation["issues"])
                prompt = (
                    f"YOUR PREVIOUS OUTPUT HAD THESE ISSUES: {issues}\n"
                    f"FIX THEM. Output MUST start with --- (YAML frontmatter).\n\n"
                    f"{prompt}"
                )
                print(
                    f"  [RETRY {attempt}/{max_retries}] "
                    f"Output malformed: {issues}",
                    file=sys.stderr,
                )

        # Return last attempt even if imperfect
        return last_response

    # -------------------------------------------------------------------
    # Validation
    # -------------------------------------------------------------------

    def _validate_artifact_output(self, content: str) -> dict:
        """Validate that output looks like a CEX artifact."""
        issues = []

        # Check frontmatter
        if not content.startswith("---"):
            # Maybe wrapped in code block
            cleaned = re.sub(r"^```(?:markdown|yaml|md)?\s*\n", "", content)
            if cleaned.startswith("---"):
                issues.append("wrapped_in_codeblock")
            else:
                issues.append("no_frontmatter")

        # Check frontmatter closure
        fm_match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not fm_match:
            issues.append("frontmatter_not_closed")
        else:
            fm_text = fm_match.group(1)
            # Check required fields
            for req in ["kind:", "title:"]:
                if req not in fm_text:
                    issues.append(f"missing_{req.strip(':')}")

        # Check for markdown structure after frontmatter
        body_start = content.find("---", 3)
        if body_start > 0:
            body = content[body_start + 3:]
            if "##" not in body and "|" not in body:
                issues.append("no_structure_in_body")

        return {
            "valid": len(issues) == 0,
            "issues": issues,
        }

    def _strip_thinking(self, content: str) -> str:
        """Strip <think>...</think> blocks from DeepSeek R1 output."""
        return re.sub(r"<think>.*?</think>\s*", "", content, flags=re.DOTALL)

    # -------------------------------------------------------------------
    # Prompt Helpers
    # -------------------------------------------------------------------

    @staticmethod
    def build_cex_system_prompt(
        kind: str = "",
        nucleus: str = "",
        brand_name: str = "",
    ) -> str:
        """Build a CEX-appropriate system prompt for Ollama models."""
        parts = [
            "You are a CEX artifact builder -- a specialized AI that produces "
            "structured knowledge artifacts with YAML frontmatter and markdown body.",
            "",
            "OUTPUT FORMAT (mandatory):",
            "1. Start with --- (YAML frontmatter)",
            "2. Include: id, kind, title, version, quality: null, tags",
            "3. Close frontmatter with ---",
            "4. Write structured markdown body with ## sections",
            "5. Use tables for structured data",
            "6. Be dense -- every sentence must add information",
            "7. Never self-score quality (always quality: null)",
        ]

        if kind:
            parts.append(f"\nYou are building a '{kind}' artifact.")
        if nucleus:
            parts.append(f"You are operating as nucleus {nucleus}.")
        if brand_name:
            parts.append(f"Brand context: {brand_name}")

        return "\n".join(parts)


# ---------------------------------------------------------------------------
# Integration: drop-in replacement for execute_prompt()
# ---------------------------------------------------------------------------

def execute_via_ollama(
    prompt: str,
    model: str = DEFAULT_MODEL,
    system: str = "",
    structured: bool = True,
) -> str:
    """Drop-in replacement for cex_intent.execute_prompt() using Ollama.

    Returns the generated text (same interface as execute_prompt).
    Raises SystemExit on failure (same behavior).
    """
    client = OllamaClient()

    if not client.health():
        print("[FAIL] Ollama server not running. Start with: ollama serve",
              file=sys.stderr)
        sys.exit(1)

    if not client.has_model(model):
        print(f"[FAIL] Model '{model}' not installed. Run: ollama pull {model}",
              file=sys.stderr)
        sys.exit(1)

    if structured:
        resp = client.generate_artifact(model=model, prompt=prompt, system=system)
    else:
        resp = client.generate(model=model, prompt=prompt, system=system)

    if not resp.success:
        print(f"[FAIL] Ollama generation failed: {resp.error}", file=sys.stderr)
        sys.exit(1)

    # Log metrics
    print(
        f"  [Ollama] {model} | {resp.tokens_generated} tokens | "
        f"{resp.tokens_per_second:.1f} tok/s | {resp.duration_ms:.0f}ms",
        file=sys.stderr,
    )

    return resp.content


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="CEX Ollama Client -- local model interface"
    )
    parser.add_argument("--list", action="store_true", help="List installed models")
    parser.add_argument("--health", action="store_true", help="Check Ollama health")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Model to use")
    parser.add_argument("--prompt", help="Prompt text")
    parser.add_argument("--prompt-file", help="Read prompt from file")
    parser.add_argument("--system", default="", help="System prompt")
    parser.add_argument("--structured", action="store_true",
                        help="Enforce CEX artifact structure")
    parser.add_argument("--kind", default="", help="CEX kind for system prompt")
    parser.add_argument("--temperature", type=float, default=0.3)
    parser.add_argument("--max-tokens", type=int, default=8192)
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    args = parser.parse_args()

    client = OllamaClient(timeout=args.timeout)

    if args.health:
        ok = client.health()
        print(f"Ollama: {'OK' if ok else 'OFFLINE'}")
        if ok:
            models = client.list_models()
            print(f"Models: {len(models)}")
            for m in models:
                size_gb = m.get("size", 0) / (1024**3)
                print(f"  {m.get('name', '?'):30s} {size_gb:.1f} GB")
        sys.exit(0 if ok else 1)

    if args.list:
        models = client.list_models()
        if not models:
            print("No models installed (or Ollama not running)")
            sys.exit(1)
        print(f"{'Model':30s} {'Size':>8s} {'Modified':>20s}")
        print("-" * 60)
        for m in models:
            size_gb = m.get("size", 0) / (1024**3)
            modified = m.get("modified_at", "")[:19]
            print(f"{m.get('name', '?'):30s} {size_gb:>7.1f}G {modified:>20s}")
        sys.exit(0)

    # Generation
    prompt = args.prompt
    if args.prompt_file:
        prompt = Path(args.prompt_file).read_text(encoding="utf-8")

    if not prompt:
        parser.print_help()
        sys.exit(1)

    system = args.system
    if args.kind and not system:
        system = OllamaClient.build_cex_system_prompt(kind=args.kind)

    if args.structured:
        resp = client.generate_artifact(
            model=args.model, prompt=prompt, system=system
        )
    else:
        resp = client.generate(
            model=args.model, prompt=prompt, system=system,
            temperature=args.temperature, max_tokens=args.max_tokens,
        )

    if resp.success:
        print(resp.content)
        print(
            f"\n--- Metrics: {resp.tokens_generated} tokens, "
            f"{resp.tokens_per_second:.1f} tok/s, "
            f"{resp.duration_ms:.0f}ms ---",
            file=sys.stderr,
        )
    else:
        print(f"[FAIL] {resp.error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
