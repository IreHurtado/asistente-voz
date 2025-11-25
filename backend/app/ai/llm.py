from openai import OpenAI
from app.config.settings import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def respuesta_ia(pregunta, contexto=None):
    system = "Eres un asistente claro, conciso y amable."
    if contexto:
        system += f" Usa este contexto si es útil: {contexto}"

    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": pregunta}
        ],
        max_tokens=150
    )

    return res.choices[0].message.content

