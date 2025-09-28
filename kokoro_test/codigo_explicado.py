from tracemalloc import get_traced_memory
import numpy as np
import soundfile as sf
from kokoro import KPipeline
from openai import OpenAI

# Definição do idioma (Português)
lang_code = "p"  # "pt-BR"

# Criação do pipeline de TTS
pipeline = KPipeline(lang_code=lang_code)

# Texto de entrada
text = """
Oi, tudo bem? Meu nome é Lorêto e eu estou aprendendo a usar o kokoro...
para testa o aplicativo e gera áudios de graça e é fácil de instalar
"""

# Geração do áudio usando a voz escolhida
generator = pipeline(text, voice="pf_dora")  # outras vozes: "pm_santa", "pm_alex"

audio_chunck = []

# O pipeline retorna fragmentos de áudio (chunks), que são acumulados
for gs, ps, audio in generator:
    audio_chunck.append(audio)

# Concatena os fragmentos em um único arquivo de áudio
audio_completo = np.concatenate(audio_chunck)

# Salva o áudio final em formato WAV (24kHz)
sf.write("audio_completo.wav", audio_completo, 24000)
