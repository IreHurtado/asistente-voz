from fastapi import APIRouter
from fastapi.responses import JSONResponse
import base64
import faiss
import numpy as np
from openai import OpenAI

from app.database.faqs_repository import obtener_faqs
from app.ai.llm import respuesta_ia
from app.ai.tts import generar_audio
from app.config.settings import FAISS_INDEX_PATH, OPENAI_API_KEY

router = APIRouter()

client = OpenAI(api_key=OPENAI_API_KEY)

faqs = obtener_faqs()
preguntas = [f[1] for f in faqs]
respuestas = [f[2] for f in faqs]

index = faiss.read_index(FAISS_INDEX_PATH)
MODEL = "text-embedding-3-small"


def embed_query(text):
    emb = client.embeddings.create(model=MODEL, input=text)
    return np.array(emb.data[0].embedding).astype("float32")


@router.get("/preguntar")
def preguntar(q: str):
    print("🔎 Pregunta:", q)

    # 1. Embedding
    query_vec = embed_query(q).reshape(1, -1)

    # 2. FAISS search
    d, I = index.search(query_vec, 1)
    idx = I[0][0]
    distancia = d[0][0]

    # 3. FAQ o IA
    if distancia < 0.5:
        texto_respuesta = respuestas[idx]
    else:
        texto_respuesta = respuesta_ia(q, preguntas[idx])

    print("📝 Respuesta:", texto_respuesta)

    # 4. Audio en bytes
    audio_bytes = generar_audio(texto_respuesta)

    # 5. Codificar audio en base64 para enviarlo por JSON
    audio_b64 = base64.b64encode(audio_bytes).decode()

    return JSONResponse({
        "texto": texto_respuesta,
        "audio_b64": audio_b64
    })
