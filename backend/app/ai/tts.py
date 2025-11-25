from openai import OpenAI
from app.config.settings import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generar_audio(texto: str) -> bytes:
    """Genera audio MP3 en memoria y devuelve bytes."""
    audio = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=texto
    )
    return audio.read()   

