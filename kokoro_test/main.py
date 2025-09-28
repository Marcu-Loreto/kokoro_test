from tracemalloc import get_traced_memory
import numpy as np
import soundfile as sf
from kokoro import KPipeline
from openai import OpenAI

lang_code = "p"#"pt-BR"

pipeline = KPipeline(lang_code = lang_code)

text = """
Oi, tudo bem? Meu nome é Lorêto e eu estou aprendendo a usar o kokoro...
para testa o aplicativo e gera audios de graça
"""
generator = pipeline(text, voice = "pm_santa")
audio_chunck = []

for gs, ps, audio in generator : 
    audio_chunck.append(audio)

audio_completo = np.concatenate(audio_chunck)
sf.write('audio_completo.wav' , audio_completo, 24000)