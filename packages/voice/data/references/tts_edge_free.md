# Edge TTS (Free) | Voice Technology

**Domain**: voice_technology
**Type**: concept
**Quality**: 0.85

Microsoft Edge TTS e uma opcao gratuita para prototipagem.

## Caracteristicas
- **Custo**: Gratuito (usa API do Edge)
- **Qualidade**: Boa para prototipos
- **Idiomas**: 40+ idiomas, incluindo pt-BR

## Vozes Brasileiras
- pt-BR-FranciscaNeural (feminina)
- pt-BR-AntonioNeural (masculino)

## Instalacao
```
pip install edge-tts
edge-tts --text "Ola mundo" --voice pt-BR-FranciscaNeural --write-media output.mp3
```

## Quando Usar
- Prototipagem, testes, fallback
- Projetos sem budget
- Evitar para producao profissional (use ElevenLabs)

---
**Generated**: 2025-12-11
**Source**: voice_agent FONTES enrichment
