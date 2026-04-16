#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX LiteLLM Integration Test -- Verify routing to all providers.

Tests LiteLLM routing to Ollama (local), Anthropic (cloud), and Google (cloud).
Run after starting the LiteLLM proxy: powershell -File boot/litellm_proxy.ps1

Usage:
    python _tools/cex_litellm_test.py              # Test all available providers
    python _tools/cex_litellm_test.py --local-only  # Test only Ollama routing
    python _tools/cex_litellm_test.py --direct       # Test without proxy (direct SDK)
"""

import argparse
import json
import os
import sys
import time

# Test without proxy first (direct litellm SDK call)
PROXY_URL = "http://localhost:4000"
OLLAMA_URL = "http://localhost:11434"

TEST_PROMPT = "What is the 8F pipeline? Answer in one sentence."


def test_ollama_direct() -> bool:
    """Test Ollama is alive and responding."""
    import requests
    print("[TEST] Ollama direct (localhost:11434)...")
    try:
        resp = requests.post(
            f"{OLLAMA_URL}/v1/chat/completions",
            json={
                "model": "qwen3:8b",
                "messages": [{"role": "user", "content": TEST_PROMPT}],
                "max_tokens": 100,
            },
            timeout=60,
        )
        if resp.status_code == 200:
            data = resp.json()
            text = data["choices"][0]["message"]["content"][:80]
            print(f"  [OK] Ollama qwen3:8b -> {text}...")
            return True
        else:
            print(f"  [FAIL] Status {resp.status_code}: {resp.text[:100]}")
            return False
    except Exception as e:
        print(f"  [FAIL] {e}")
        return False


def test_litellm_direct() -> bool:
    """Test LiteLLM SDK calling Ollama directly (no proxy)."""
    print("[TEST] LiteLLM SDK -> Ollama (direct, no proxy)...")
    try:
        import litellm
        resp = litellm.completion(
            model="ollama/qwen3:8b",
            messages=[{"role": "user", "content": TEST_PROMPT}],
            api_base=OLLAMA_URL,
            max_tokens=100,
        )
        text = resp.choices[0].message.content[:80]
        print(f"  [OK] litellm -> ollama/qwen3:8b -> {text}...")
        return True
    except Exception as e:
        print(f"  [FAIL] {e}")
        return False


def test_litellm_proxy(model_name: str) -> bool:
    """Test LiteLLM proxy routing."""
    import requests
    print(f"[TEST] LiteLLM proxy -> {model_name}...")
    try:
        resp = requests.post(
            f"{PROXY_URL}/v1/chat/completions",
            json={
                "model": model_name,
                "messages": [{"role": "user", "content": TEST_PROMPT}],
                "max_tokens": 100,
            },
            headers={"Authorization": "Bearer sk-cex-test"},
            timeout=120,
        )
        if resp.status_code == 200:
            data = resp.json()
            text = data["choices"][0]["message"]["content"][:80]
            print(f"  [OK] {model_name} -> {text}...")
            return True
        else:
            print(f"  [FAIL] Status {resp.status_code}: {resp.text[:200]}")
            return False
    except Exception as e:
        print(f"  [FAIL] {e}")
        return False


def test_proxy_health() -> bool:
    """Check if LiteLLM proxy is running."""
    import requests
    try:
        resp = requests.get(f"{PROXY_URL}/health", timeout=5)
        return resp.status_code == 200
    except Exception:
        return False


def main() -> None:
    parser = argparse.ArgumentParser(description="CEX LiteLLM Integration Test")
    parser.add_argument("--local-only", action="store_true",
                        help="Test only local Ollama routing")
    parser.add_argument("--direct", action="store_true",
                        help="Test LiteLLM SDK directly (no proxy)")
    args = parser.parse_args()

    results = {}
    total = 0
    passed = 0

    # Test 1: Ollama direct
    total += 1
    if test_ollama_direct():
        passed += 1
        results["ollama_direct"] = "PASS"
    else:
        results["ollama_direct"] = "FAIL"

    # Test 2: LiteLLM SDK direct
    if args.direct or not test_proxy_health():
        total += 1
        if test_litellm_direct():
            passed += 1
            results["litellm_sdk_direct"] = "PASS"
        else:
            results["litellm_sdk_direct"] = "FAIL"

    # Test 3: LiteLLM proxy (if running)
    if not args.direct:
        if test_proxy_health():
            print("[INFO] LiteLLM proxy is running on :4000")
            models = ["cex-n07", "cex-n03", "cex-n01"]
            if not args.local_only:
                models = ["cex-n01", "cex-n02", "cex-n03", "cex-n04", "cex-n05", "cex-n06", "cex-n07"]
            for m in models:
                total += 1
                if test_litellm_proxy(m):
                    passed += 1
                    results[f"proxy_{m}"] = "PASS"
                else:
                    results[f"proxy_{m}"] = "FAIL"
        else:
            print("[WARN] LiteLLM proxy not running. Start: powershell -File boot/litellm_proxy.ps1")
            print("[INFO] Testing SDK direct mode instead.")
            total += 1
            if test_litellm_direct():
                passed += 1
                results["litellm_sdk_direct"] = "PASS"
            else:
                results["litellm_sdk_direct"] = "FAIL"

    # Summary
    print(f"\n{'='*50}")
    print(f"LITELLM TEST RESULTS: {passed}/{total} passed")
    print(f"{'='*50}")
    for test, result in results.items():
        status = "[OK]" if result == "PASS" else "[FAIL]"
        print(f"  {status} {test}")

    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()
