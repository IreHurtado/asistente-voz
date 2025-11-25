import faiss
import numpy as np
from openai import OpenAI
from app.database.faqs_repository import obtener_faqs
from app.config.settings import OPENAI_API_KEY, FAISS_INDEX_PATH, FAISS_DIR
import os

client = OpenAI(api_key=OPENAI_API_KEY)

MODEL = "text-embedding-3-small"

def generar_embeddings(textos):
    res = client.embeddings.create(model=MODEL, input=textos)
    return np.array([e.embedding for e in res.data]).astype("float32")

def construir_faiss():
    print("Cargando FAQs…")
    faqs = obtener_faqs()

    if not faqs:
        print("No hay FAQs, no se genera índice")
        return
    
    preguntas = [f[1] for f in faqs]

    print("Generando embeddings…")
    emb = generar_embeddings(preguntas)
    dim = emb.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(emb)

    os.makedirs(FAISS_DIR, exist_ok=True)
    faiss.write_index(index, FAISS_INDEX_PATH)

    print("Índice FAISS generado correctamente!")
