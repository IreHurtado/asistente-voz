from fastapi import APIRouter
from fastapi.responses import JSONResponse
import base64
import faiss
import numpy as np
from openai import OpenAI
import re

from app.database.faqs_repository import obtener_faqs
from app.flows.constants import WHATSAPP_URL
from app.flows.intents import detectar_intent_general, detectar_saludo
from app.ai.tts import generar_audio
from app.config.settings import FAISS_INDEX_PATH, OPENAI_API_KEY

router = APIRouter()

# =========================
# SETUP
# =========================

client = OpenAI(api_key=OPENAI_API_KEY)
MODEL = "text-embedding-3-small"
UMBRAL_FAISS = 1.4

faqs = obtener_faqs()
preguntas = [f[1] for f in faqs]
respuestas = [f[2] for f in faqs]

index = faiss.read_index(FAISS_INDEX_PATH)

# =========================
# UTILIDADES
# =========================

def limpiar_para_audio(texto: str) -> str:
    """Evita que el TTS lea URLs"""
    return re.sub(r"https?://\S+", "", texto).strip()


def embed_query(texto: str) -> np.ndarray:
    emb = client.embeddings.create(model=MODEL, input=texto)
    return np.array(emb.data[0].embedding).astype("float32")


def responder(texto_respuesta: str) -> JSONResponse:
    texto_audio = limpiar_para_audio(texto_respuesta)
    audio_bytes = generar_audio(texto_audio)
    audio_b64 = base64.b64encode(audio_bytes).decode()

    return JSONResponse({
        "texto": texto_respuesta,
        "audio_b64": audio_b64
    })


# =========================
# ENDPOINT
# =========================

@router.get("/preguntar")
def preguntar(q: str):
    print("🔎 Pregunta:", q)
    
    # 0️⃣ saludo vacío
    respuesta_saludo = detectar_saludo(q)
    if respuesta_saludo:
        return responder(respuesta_saludo)

    # 1️⃣ Intent general (reglas humanas directas)
    respuesta_intent = detectar_intent_general(q)
    if respuesta_intent:
        return responder(respuesta_intent)

    # 2️⃣ FAISS
    query_vec = embed_query(q).reshape(1, -1)
    d, I = index.search(query_vec, 1)

    idx = I[0][0]
    distancia = d[0][0]

    print("📏 Distancia FAISS:", distancia)
    print("📌 Pregunta FAQ emparejada:", preguntas[idx])

    if distancia < UMBRAL_FAISS:
        return responder(respuestas[idx])

    # 3️⃣ Fallback humano
    return responder(
        "Para orientarte correctamente, necesito un poco más de información "
        "sobre el trámite que deseas realizar.\n\n"
        "Por favor escríbenos por WhatsApp y con gusto te ayudamos:\n"
        f"{WHATSAPP_URL}"
    )
