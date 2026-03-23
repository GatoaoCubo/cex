"""
CEX Audio Feedback — Generates TTS audio for specialist feedback.

Uses Edge TTS (Microsoft, free, unlimited, PT-BR neural voices).

Usage:
  python generate_audio_feedback.py --text "feedback text" --output result.mp3
  python generate_audio_feedback.py --file resultado.md --output result.mp3
  python generate_audio_feedback.py --result-data '{"source":"file.pdf","score":8.7,"status":"APROVADO","extractions":["..."],"feedback":"..."}'
"""
import asyncio
import argparse
import json
import sys
from pathlib import Path

VOICE = "pt-BR-FranciscaNeural"
RATE = "+5%"


def build_feedback_script(data: dict) -> str:
    """Build natural speech script from structured result data."""
    source = data.get("source", "seu arquivo")
    score = data.get("score", 0)
    status = data.get("status", "processado")

    # Convert score to spoken format
    score_int = int(score)
    score_dec = int((score - score_int) * 10)
    score_spoken = f"{score_int} ponto {score_dec}" if score_dec else str(score_int)

    script = f"Oi! Aqui eh a CODEXA com o resultado do seu arquivo.\n\n"
    script += f"Seu arquivo {source} foi processado. "
    script += f"Score: {score_spoken} de dez. Status: {status}.\n\n"

    extractions = data.get("extractions", [])
    if extractions:
        script += "O que foi extraido:\n"
        for e in extractions:
            script += f"{e}\n"
        script += "\n"

    feedback = data.get("feedback", "")
    if feedback:
        script += f"Feedback: {feedback}\n\n"

    suggestions = data.get("suggestions", [])
    if suggestions:
        script += "Para proximas contribuicoes:\n"
        for s in suggestions:
            script += f"{s}\n"
        script += "\n"

    if status == "APROVADO":
        script += "Nenhuma acao necessaria da sua parte. "
        script += "O conhecimento ja foi integrado ao sistema.\n"
    else:
        script += "Revise o arquivo com as sugestoes acima e envie novamente.\n"

    script += "\nObrigada pela contribuicao!"
    return script


async def generate(text: str, output: str):
    """Generate MP3 from text using Edge TTS."""
    import edge_tts
    comm = edge_tts.Communicate(text, VOICE, rate=RATE)
    await comm.save(output)
    size_kb = Path(output).stat().st_size // 1024
    print(f"[OK] {output} ({size_kb}KB)")


def main():
    p = argparse.ArgumentParser(description="CEX Audio Feedback Generator")
    p.add_argument("--text", type=str, help="Direct text to speak")
    p.add_argument("--file", type=str, help="Read text from file")
    p.add_argument("--result-data", type=str, help="JSON with structured result")
    p.add_argument("--output", type=str, required=True, help="Output MP3 path")
    p.add_argument("--voice", default=VOICE, help=f"Voice (default: {VOICE})")
    a = p.parse_args()

    if a.result_data:
        data = json.loads(a.result_data)
        text = build_feedback_script(data)
    elif a.file:
        text = Path(a.file).read_text(encoding="utf-8")
    elif a.text:
        text = a.text
    else:
        p.print_help()
        sys.exit(1)

    asyncio.run(generate(text, a.output))


if __name__ == "__main__":
    main()
