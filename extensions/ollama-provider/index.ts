/**
 * CEX Ollama Provider Extension
 * 
 * Provides FREE local LLM fallback via Ollama.
 * Models: codexaft (fine-tuned), qwen2.5-coder, llama3.1, mistral
 * 
 * Usage:
 *   pi -e ./extensions/ollama-provider --model ollama/codexaft:v3
 *   pi -e ./extensions/ollama-provider --model ollama/qwen2.5-coder:7b
 */

import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";

export default function (pi: ExtensionAPI) {
    pi.registerProvider("ollama", {
        baseUrl: "http://localhost:11434/v1",
        apiKey: "ollama",  // Ollama doesn't need a real key but the field is required
        api: "openai-completions",
        models: [
            {
                id: "codexaft:v3",
                name: "CodexaFT v3 (Fine-tuned Qwen 3.1B)",
                reasoning: false,
                input: ["text"],
                cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
                contextWindow: 8192,
                maxTokens: 4096
            },
            {
                id: "qwen2.5-coder:7b",
                name: "Qwen 2.5 Coder 7B",
                reasoning: false,
                input: ["text"],
                cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
                contextWindow: 32768,
                maxTokens: 8192
            },
            {
                id: "llama3.1:8b",
                name: "Llama 3.1 8B",
                reasoning: false,
                input: ["text"],
                cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
                contextWindow: 131072,
                maxTokens: 8192
            },
            {
                id: "mistral:7b",
                name: "Mistral 7B",
                reasoning: false,
                input: ["text"],
                cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
                contextWindow: 32768,
                maxTokens: 8192
            },
            {
                id: "deepseek-coder-v2:16b",
                name: "DeepSeek Coder V2 16B",
                reasoning: false,
                input: ["text"],
                cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
                contextWindow: 131072,
                maxTokens: 8192
            }
        ]
    });
}
